#!/usr/bin/env python3
"""Fail when public Markdown can expose raw/broken mathematical source on GitHub.

This checker encodes the carrier lesson from the August 2026 repo-wide rendering repair:
source-valid mathematics is not publication-valid until the user-facing Markdown carrier can render it.

It is intentionally conservative. It does not attempt to reimplement GitHub's mathematics renderer;
it blocks known-bad constructs and catches source-level failures that should never reach public preview.
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
INLINE_CODE_CAPTURE = re.compile(r"`([^`\n]+)`")

SCIENTIFIC_ROOT_ROUTES = {
    "MKUFT_INTEGRATED_MASTER_SPINE.md",
    "SCIENTIFIC_READER_TRAVERSAL_GUIDE.md",
    "PROFESSIONAL_DOMAIN_INSTANTIATION_GUIDE.md",
    "FSAI_CANONICAL_NAMING_NOTE.md",
    "ATLD_STANDALONE_PUBLICATION.md",
    "AAF_STANDALONE_PUBLICATION.md",
    "FSSR_STANDALONE_PUBLICATION.md",
    "TDR_STANDALONE_PUBLICATION.md",
}

LITERAL_CONTEXT = re.compile(
    r"\b(?:literal|source token|source fragment|command|syntax|filename|file name|path|"
    r"repository identifier|code span|code-style|identifier string)\b",
    re.IGNORECASE,
)

PLAIN_GREEK_NAMES = {
    "Theta", "Sigma", "Delta", "Omega", "Phi", "Psi", "Pi", "Gamma", "Lambda", "Xi",
    "lambda", "rho", "epsilon", "varepsilon", "tau", "chi", "kappa",
    "eta", "nu", "alpha", "beta", "gamma", "delta", "mu", "sigma", "pi",
}

PLAIN_GREEK_IN_MATH = re.compile(
    r"(?<!\\\\)\\b(?:Theta|Sigma|Delta|Omega|Phi|Psi|Pi|Gamma|Lambda|Xi|"
    r"lambda|rho|epsilon|varepsilon|tau|chi|kappa|eta|nu|alpha|beta|gamma|delta|mu|sigma|pi)"
    r"(?=_[A-Za-z0-9{])"
)


def is_scientific_route(path: Path) -> bool:
    try:
        rel = path.relative_to(ROOT).as_posix()
    except ValueError:
        # Fixture files exercise the same scientific-route rules.
        return True
    return rel.startswith("docs/") or rel.startswith("papers/") or rel in SCIENTIFIC_ROOT_ROUTES


def looks_like_literal_resource(span: str) -> bool:
    s = span.strip()
    if "/" in s or "\\\\" in s:
        return True
    if re.search(r"\.(?:md|py|json|pdf|txt|yml|yaml|cff|csv|tsv|png|jpg|jpeg|svg)$", s, re.IGNORECASE):
        return True
    if s.startswith(("http://", "https://", "10.5281/", "MKUFT_PREPRINTS_")):
        return True
    return False


def looks_like_semantic_math(span: str) -> bool:
    s = span.strip()
    if not s:
        return False
    if re.fullmatch(r"[Α-Ωα-ω]", s):
        return True
    if re.fullmatch(r"\\d+(?:\\.\\d+)?/\\d+(?:\\.\\d+)?", s):
        return True
    if looks_like_literal_resource(s):
        return False
    if MATH_COMMAND.search(s) or re.search(r"\\[A-Za-z]+", s):
        return True
    if re.search(r"[A-Za-zΑ-Ωα-ω][A-Za-z0-9]*(?:_|\^)", s):
        return True
    if re.search(r"(?:<=|>=|!=|≤|≥|∈|∉|≈|≃|≠)", s):
        return True
    if re.search(r"(?:->|<->)", s):
        return True
    if re.search(r"(?:→|↔|⇒|⇔)", s) and not re.search(r"\s", s):
        return True
    if re.fullmatch(r"[A-Za-zΑ-Ωα-ω]\*", s):
        return True
    if s in PLAIN_GREEK_NAMES:
        return True
    if re.fullmatch(r"[A-Za-z]", s):
        return True
    if re.fullmatch(r"(?:Drop|Aug|Eval|Abl|Adm|Rec)", s):
        return True
    if re.match(r"^(?:det|rank|tr)\\s+[A-Za-zΑ-Ωα-ω][^=]*=", s):
        return True
    if re.match(r"^(?:Theta|Sigma|Delta|Omega|Phi|Psi|Pi|Gamma|Lambda|Xi|lambda|rho|epsilon|varepsilon|tau|chi|kappa|eta|nu|alpha|beta|gamma|delta|mu|sigma|pi)\\s*=", s):
        return True
    if re.match(r"^[A-Za-zΑ-Ωα-ω](?:[_^][^=\\s]+)?\\s*=", s):
        return True
    return False


def audit_semantic_inline_code(line: str, lineno: int):
    if LITERAL_CONTEXT.search(line):
        return []
    problems = []
    for match in INLINE_CODE_CAPTURE.finditer(line):
        span = match.group(1)
        if looks_like_semantic_math(span):
            problems.append(
                f"line {lineno}: mathematical notation is in a literal inline-code carrier: `{span}`; use $...$ for semantic inline mathematics"
            )
    return problems

# GitHub's public math carrier rejects these in this repository's observed rendering path.
BANNED_MATH_MACROS = {
    r"\operatorname": r"use a supported construction such as \mathrm{...}",
}


def markdown_paths():
    return sorted(
        p for p in ROOT.rglob("*.md")
        if ".git" not in p.parts
    )


def unescaped_brace_balance(text: str):
    r"""Return (ok, first_negative_offset, final_depth) for TeX grouping braces.

    Display braces written as \{ or \} are ignored. This is a source-integrity check,
    not a full TeX parser.
    """
    depth = 0
    first_negative = None
    for i, ch in enumerate(text):
        if ch not in "{}":
            continue
        # A brace immediately preceded by an odd number of backslashes is escaped.
        backslashes = 0
        j = i - 1
        while j >= 0 and text[j] == "\\":
            backslashes += 1
            j -= 1
        if backslashes % 2:
            continue
        if ch == "{":
            depth += 1
        else:
            depth -= 1
            if depth < 0 and first_negative is None:
                first_negative = i
    return first_negative is None and depth == 0, first_negative, depth


def audit_math_fence(path: Path, start_line: int, lines):
    problems = []
    text = "\n".join(lines)

    for macro, replacement in BANNED_MATH_MACROS.items():
        if macro in text:
            problems.append(
                f"math fence opened line {start_line}: unsupported GitHub math macro {macro}; {replacement}"
            )

    plain_greek = PLAIN_GREEK_IN_MATH.search(text)
    if plain_greek:
        problems.append(
            f"math fence opened line {start_line}: ASCII Greek-name token {plain_greek.group(0)} is not TeX Greek notation"
        )

    ok, first_negative, depth = unescaped_brace_balance(text)
    if not ok:
        if first_negative is not None:
            problems.append(
                f"math fence opened line {start_line}: unmatched closing brace in TeX group"
            )
        if depth > 0:
            problems.append(
                f"math fence opened line {start_line}: {depth} unclosed TeX grouping brace(s)"
            )

    if text.count(r"\begin{aligned}") != text.count(r"\end{aligned}"):
        problems.append(
            f"math fence opened line {start_line}: unbalanced aligned environment"
        )

    if "$$" in text:
        problems.append(
            f"math fence opened line {start_line}: nested legacy $$ delimiter inside fenced math"
        )

    return problems


def audit(path: Path):
    text = path.read_text(encoding="utf-8")
    problems = []

    if "\ufffd" in text:
        problems.append("contains Unicode replacement character U+FFFD")

    for c in text:
        if unicodedata.category(c) == "Cc" and c not in "\n\r\t":
            problems.append(f"contains hidden control character U+{ord(c):04X}")
            break

    in_fence = False
    fence_kind = ""
    fence_start = None
    fence_lines = []

    for lineno, line in enumerate(text.splitlines(), 1):
        stripped = line.strip()

        if stripped.lower() == "~~~math":
            problems.append(
                f"line {lineno}: unsupported tilde math fence; use fenced ```math"
            )
            continue

        if stripped.startswith("```"):
            if not in_fence:
                in_fence = True
                fence_kind = stripped[3:].strip().lower()
                fence_start = lineno
                fence_lines = []
            else:
                if fence_kind == "math":
                    problems.extend(audit_math_fence(path, fence_start, fence_lines))
                in_fence = False
                fence_kind = ""
                fence_start = None
                fence_lines = []
            continue

        if in_fence:
            fence_lines.append(line)
            continue

        if stripped in ("$$", r"\[", r"\]"):
            problems.append(f"line {lineno}: legacy display-math delimiter; use fenced ```math")

        if r"\(" in line or r"\)" in line:
            problems.append(f"line {lineno}: legacy inline-math delimiter; use $...$")

        # Inline code is a literal carrier, not a math carrier. On scientific routes,
        # reject math-like spans when they are being used semantically rather than
        # explicitly quoted as literal source/code.
        if is_scientific_route(path):
            problems.extend(audit_semantic_inline_code(line, lineno))

        # Strip literal-code carriers before checking the remaining prose for naked TeX.
        visible = INLINE_CODE.sub("", line)

        for macro, replacement in BANNED_MATH_MACROS.items():
            if macro in visible:
                problems.append(
                    f"line {lineno}: unsupported GitHub math macro {macro}; {replacement}"
                )

        # A line carrying '$' is allowed because it is explicitly using GitHub inline math.
        if MATH_COMMAND.search(visible) and "$" not in visible:
            problems.append(f"line {lineno}: TeX-like command is outside an explicit GitHub math carrier")

    if in_fence:
        problems.append(f"unbalanced fenced code block (opened as {fence_kind or 'plain'} at line {fence_start})")

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
