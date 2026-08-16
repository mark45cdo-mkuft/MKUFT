#!/usr/bin/env python3
"""Fail when public Markdown can expose raw/broken mathematical source on GitHub.

This checker encodes the carrier lesson from the August 2026 repo-wide rendering repair:
source-valid mathematics is not publication-valid until the user-facing Markdown carrier can render it.
"""

from pathlib import Path
import re
import sys
import unicodedata

ROOT = Path(__file__).resolve().parents[1]

MATH_COMMAND = re.compile(
    r"\\(?:mathcal|mathfrak|mathbf|mathrm|text|alpha|beta|gamma|delta|Delta|lambda|Lambda|"
    r"Psi|Xi|Pi|rho|mu|nu|sum|int|boxed|left|right|rightarrow|longrightarrow|rightleftarrows|"
    r"approx|neq|in|le|ge|circ|mid|widetilde|bigsqcup|lVert|rVert|qquad|quad|times|subseteq)\b"
)
INLINE_CODE = re.compile(r"`[^`]*`")


def markdown_paths():
    return sorted(
        p for p in ROOT.rglob("*.md")
        if ".git" not in p.parts
    )


def audit(path: Path):
    text = path.read_text(encoding="utf-8")
    problems = []

    if "\ufffd" in text:
        problems.append("contains Unicode replacement character U+FFFD")

    for c in text:
        if unicodedata.category(c) == "Cc" and c not in "\n\r\t":
            problems.append(f"contains hidden control character U+{ord(c):04X}")
            break

    if r"\operatorname" in text:
        problems.append(r"contains unsupported GitHub math macro \operatorname; use a supported construction such as \mathrm")

    in_fence = False
    fence_kind = ""
    for lineno, line in enumerate(text.splitlines(), 1):
        stripped = line.strip()

        if stripped.startswith("```"):
            if not in_fence:
                in_fence = True
                fence_kind = stripped[3:].strip().lower()
            else:
                in_fence = False
                fence_kind = ""
            continue

        if in_fence:
            continue

        if stripped in ("$$", r"\[", r"\]"):
            problems.append(f"line {lineno}: legacy display-math delimiter; use fenced ```math")

        if r"\(" in line or r"\)" in line:
            problems.append(f"line {lineno}: legacy inline-math delimiter; use $...$")

        # Strip inline-code literals before looking for naked TeX. A line carrying '$'
        # is allowed because it is explicitly using GitHub inline math.
        visible = INLINE_CODE.sub("", line)
        if MATH_COMMAND.search(visible) and "$" not in visible:
            problems.append(f"line {lineno}: TeX-like command is outside an explicit GitHub math carrier")

    if in_fence:
        problems.append(f"unbalanced fenced code block (opened as {fence_kind or 'plain'})")

    return problems


def main():
    paths = markdown_paths()
    failures = []
    for path in paths:
        problems = audit(path)
        if problems:
            failures.append((path.relative_to(ROOT), problems))

    print(f"Audited {len(paths)} Markdown files.")
    if failures:
        for path, problems in failures:
            print(f"\n{path}")
            for problem in problems:
                print(f"  - {problem}")
        print(f"\nFAILED: {len(failures)} Markdown files violate the rendering contract.")
        return 1

    print("PASS: all Markdown files satisfy the GitHub rendering contract.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
