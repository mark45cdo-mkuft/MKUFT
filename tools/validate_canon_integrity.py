#!/usr/bin/env python3
"""Minimum machine gate for MKUFT public-canon write integrity.

This is intentionally conservative. It blocks known transfer/rendering faults and
retired live-canon identifiers. With --base it also rejects newly introduced
math-like fenced `text` blocks in changed Markdown.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RETIRED = ROOT / "CANON_RETIRED_IDENTIFIERS.txt"

# GitHub Markdown renders $...$ and $$...$$ reliably for this repository.
# These legacy delimiter forms previously survived transfer as visible source.
LEGACY_MATH_DELIMITERS = (r"\[", r"\]", r"\(", r"\)")

MATH_COMMAND_RE = re.compile(
    r"\\(?:frac|sum|int|prod|sqrt|mathcal|operatorname|text|begin|end|neq|approx|"
    r"in|notin|subset|supset|ge|le|rightarrow|leftarrow|leftrightarrow|mid|cdot|times)\b"
)
MATH_SYMBOL_RE = re.compile(r"(?:=|≈|≠|≤|≥|∈|∉|⊂|⊆|⊃|⊇|∑|∫|√)")


def markdown_files() -> list[Path]:
    files: list[Path] = []
    for path in ROOT.rglob("*.md"):
        rel = path.relative_to(ROOT)
        if any(part in {".git", ".github"} for part in rel.parts):
            continue
        files.append(path)
    return sorted(files)


def retired_identifiers() -> list[str]:
    if not RETIRED.exists():
        return []
    values: list[str] = []
    for raw in RETIRED.read_text(encoding="utf-8").splitlines():
        item = raw.strip()
        if item and not item.startswith("#"):
            values.append(item)
    return values


def extract_text_fences(text: str) -> list[str]:
    blocks: list[str] = []
    lines = text.splitlines()
    inside = False
    language = ""
    buf: list[str] = []

    for line in lines:
        stripped = line.strip()
        if stripped.startswith("```"):
            if not inside:
                inside = True
                language = stripped[3:].strip().lower()
                buf = []
            else:
                if language in {"", "text"}:
                    blocks.append("\n".join(buf).strip())
                inside = False
                language = ""
                buf = []
            continue
        if inside:
            buf.append(line)
    return blocks


def equation_like_text_fence(block: str) -> bool:
    if not block:
        return False
    # Route/file-tree diagrams remain allowed. A new text fence is treated as an
    # equation when it contains mathematical commands or equation/comparison signs.
    if MATH_COMMAND_RE.search(block):
        return True
    if MATH_SYMBOL_RE.search(block):
        # Avoid flagging ordinary arrow-only architecture diagrams.
        return True
    return False


def git_show(ref: str, rel: Path) -> str | None:
    proc = subprocess.run(
        ["git", "show", f"{ref}:{rel.as_posix()}"],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
    )
    if proc.returncode != 0:
        return None
    return proc.stdout


def changed_markdown(base: str) -> list[Path]:
    proc = subprocess.run(
        ["git", "diff", "--name-only", f"{base}...HEAD", "--", "*.md"],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or "git diff failed")
    return [ROOT / line for line in proc.stdout.splitlines() if line.strip()]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base", help="Base commit/ref for write-forward fence checks")
    args = parser.parse_args()

    errors: list[str] = []
    retired = retired_identifiers()

    for path in markdown_files():
        rel = path.relative_to(ROOT)
        text = path.read_text(encoding="utf-8")
        lower = text.lower()

        for token in LEGACY_MATH_DELIMITERS:
            if token in text:
                errors.append(
                    f"{rel}: legacy math delimiter {token!r}; use GitHub rendered $...$ or $$...$$"
                )

        for identifier in retired:
            if identifier.lower() in lower:
                errors.append(f"{rel}: retired live-canon identifier remains: {identifier}")

    if args.base:
        try:
            changed = changed_markdown(args.base)
        except RuntimeError as exc:
            errors.append(str(exc))
            changed = []

        for path in changed:
            if not path.exists():
                continue
            rel = path.relative_to(ROOT)
            current = path.read_text(encoding="utf-8")
            previous = git_show(args.base, rel) or ""
            old_blocks = set(extract_text_fences(previous))
            for block in extract_text_fences(current):
                if block not in old_blocks and equation_like_text_fence(block):
                    preview = block.replace("\n", " ")[:120]
                    errors.append(
                        f"{rel}: newly introduced equation-like fenced text block; "
                        f"render as Markdown math instead: {preview!r}"
                    )

    if errors:
        print("CANON INTEGRITY: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    print("CANON INTEGRITY: PASS")
    print("- no retired live-canon identifiers found")
    print("- no legacy math delimiters found")
    if args.base:
        print("- no newly introduced equation-like text fences found")
    return 0


if __name__ == "__main__":
    sys.exit(main())
