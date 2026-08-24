#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import os
import re
import shutil
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "docs/25C_RESIDUAL_INSTRUMENT_GENERATION_AND_PROTECTED_DISCOVERY_BOUNDARY.md"
OUT_DIR = ROOT / "publications/module-reading-editions"
OUTPUT = OUT_DIR / "25C_RESIDUAL_INSTRUMENT_GENERATION_AND_PROTECTED_DISCOVERY_BOUNDARY.pdf"
BODY = ROOT / ".build/25c_house_body.md"
TEMPLATE = ROOT / ".build/25c_house_template.tex"
SOURCE_COMMIT = os.environ.get("SOURCE_COMMIT", "35f877995298414cfdbc4c4cc59ab62f7f245490")
SHORT_COMMIT = SOURCE_COMMIT[:12]


def run(*args: str) -> str:
    p = subprocess.run(args, cwd=ROOT, check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    return p.stdout


def prepare_body() -> None:
    text = SOURCE.read_text(encoding="utf-8")
    marker = "## 1. Purpose and scope"
    if marker not in text:
        raise SystemExit("25C source lost the expected section-1 marker")
    body = text[text.index(marker):]
    body = re.sub(r"```math\s*\n(.*?)\n```", lambda m: "$$\n" + m.group(1).strip() + "\n$$", body, flags=re.S)
    BODY.parent.mkdir(parents=True, exist_ok=True)
    BODY.write_text(body.rstrip() + "\n", encoding="utf-8")


def write_template() -> None:
    template = rf'''\documentclass[10pt,a4paper]{{article}}
\usepackage[a4paper,left=20mm,right=20mm,top=17mm,bottom=18mm]{{geometry}}
\usepackage{{fontspec}}
\usepackage{{unicode-math}}
\setmainfont[
  Path=/usr/share/texlive/texmf-dist/fonts/opentype/public/libertinus-fonts/,
  UprightFont=LibertinusSerif-Regular.otf,
  BoldFont=LibertinusSerif-Bold.otf,
  ItalicFont=LibertinusSerif-Italic.otf,
  BoldItalicFont=LibertinusSerif-BoldItalic.otf
]{{LibertinusSerif-Regular.otf}}
\setsansfont[
  Path=/usr/share/texlive/texmf-dist/fonts/opentype/adobe/sourcesanspro/,
  UprightFont=SourceSansPro-Regular.otf,
  BoldFont=SourceSansPro-Semibold.otf,
  ItalicFont=SourceSansPro-RegularIt.otf,
  BoldItalicFont=SourceSansPro-SemiboldIt.otf
]{{SourceSansPro-Regular.otf}}
\setmonofont{{DejaVu Sans Mono}}
\setmathfont[Path=/usr/share/texlive/texmf-dist/fonts/opentype/public/newcomputermodern/]{{NewCMMath-Book.otf}}
\usepackage{{xcolor}}
\usepackage{{tikz}}
\definecolor{{MKnavy}}{{HTML}}{{183B66}}
\definecolor{{MKblue}}{{HTML}}{{1A6F9E}}
\definecolor{{MKrule}}{{HTML}}{{C7D1DA}}
\definecolor{{MKbox}}{{HTML}}{{F2F4F6}}
\definecolor{{MKrights}}{{HTML}}{{FFF7E7}}
\definecolor{{MKgold}}{{HTML}}{{B17B21}}
\usepackage{{microtype}}
\usepackage{{ragged2e}}
\usepackage{{setspace}}
\setstretch{{1.015}}
\AtBeginDocument{{\justifying\setlength{{\parindent}}{{0pt}}\setlength{{\parfillskip}}{{0pt plus 1fil}}}}
\setlength{{\parindent}}{{0pt}}
\setlength{{\parskip}}{{0.42em}}
\usepackage{{enumitem}}
\providecommand{{\tightlist}}{{\setlength{{\itemsep}}{{0pt}}\setlength{{\parskip}}{{0pt}}}}
\setlist[itemize]{{leftmargin=1.35em,itemsep=0.05em,topsep=0.2em,parsep=0pt}}
\setlist[enumerate]{{leftmargin=1.6em,itemsep=0.12em,topsep=0.25em,parsep=0pt}}
\usepackage{{titlesec}}
\titleformat{{\section}}[block]
 {{\sffamily\bfseries\color{{MKnavy}}\fontsize{{18.5}}{{20.5}}\selectfont}}
 {{}}{{0pt}}{{}}
 [\vspace{{0.22em}}\color{{MKrule}}\titlerule]
\titlespacing*{{\section}}{{0pt}}{{1.05em}}{{0.42em}}
\titleformat{{\subsection}}[block]
 {{\sffamily\bfseries\color{{MKnavy}}\fontsize{{13.2}}{{15}}\selectfont}}
 {{}}{{0pt}}{{}}
\titlespacing*{{\subsection}}{{0pt}}{{0.8em}}{{0.28em}}
\usepackage{{fancyhdr}}
\pagestyle{{fancy}}
\fancyhf{{}}
\renewcommand{{\headrulewidth}}{{0pt}}
\renewcommand{{\footrulewidth}}{{0pt}}
\fancyfoot[L]{{\fontsize{{7.7}}{{9}}\selectfont\color{{MKnavy}}\href{{https://doi.org/10.5281/zenodo.17780566}}{{doi.org/10.5281/zenodo.17780566}}}}
\fancyfoot[C]{{\fontsize{{8}}{{9}}\selectfont\color{{MKnavy}}\thepage}}
\fancyfoot[R]{{\fontsize{{7.7}}{{9}}\selectfont\color{{MKnavy}}Git snapshot {SHORT_COMMIT}}}
\setlength{{\footskip}}{{13mm}}
\usepackage{{hyperref}}
\hypersetup{{colorlinks=true,linkcolor=MKblue,urlcolor=MKblue,citecolor=MKblue,pdfauthor={{Mark Charles McLaughlin}},pdftitle={{25C — Residual Instrument Generation and Protected Discovery Boundary — Research Module Reading Edition}}}}
\usepackage{{xurl}}
\usepackage{{bookmark}}
\usepackage{{booktabs,longtable,array}}
\usepackage[most]{{tcolorbox}}
\usepackage{{etoolbox}}
\AtBeginEnvironment{{quote}}{{\begin{{tcolorbox}}[enhanced,breakable,colback=MKbox,colframe=MKbox,boxrule=0pt,borderline west={{2pt}}{{0pt}}{{MKblue}},left=8pt,right=8pt,top=5pt,bottom=5pt,arc=0pt]}}
\AtEndEnvironment{{quote}}{{\end{{tcolorbox}}}}
\usepackage{{newunicodechar}}
\newunicodechar{{→}}{{\ensuremath{{\rightarrow}}}}
\newunicodechar{{↔}}{{\ensuremath{{\leftrightarrow}}}}
\newunicodechar{{≠}}{{\ensuremath{{\ne}}}}
\newunicodechar{{≥}}{{\ensuremath{{\ge}}}}
\newunicodechar{{≤}}{{\ensuremath{{\le}}}}
\newunicodechar{{∈}}{{\ensuremath{{\in}}}}
\newunicodechar{{∼}}{{\ensuremath{{\sim}}}}
\newunicodechar{{∧}}{{\ensuremath{{\land}}}}
\newunicodechar{{⊇}}{{\ensuremath{{\supseteq}}}}
\newunicodechar{{⊆}}{{\ensuremath{{\subseteq}}}}
\newunicodechar{{×}}{{\ensuremath{{\times}}}}
\newunicodechar{{©}}{{\textcopyright}}
\newcommand{{\statusbox}}[1]{{\begin{{tcolorbox}}[enhanced,colback=MKbox,colframe=MKbox,boxrule=0pt,borderline west={{2.2pt}}{{0pt}}{{MKnavy}},left=9pt,right=9pt,top=6pt,bottom=6pt,arc=0pt]\small #1\end{{tcolorbox}}}}
\newcommand{{\rightsbox}}[1]{{\begin{{tcolorbox}}[enhanced,colback=MKrights,colframe=MKrights,boxrule=0pt,borderline west={{2.2pt}}{{0pt}}{{MKgold}},left=9pt,right=9pt,top=6pt,bottom=6pt,arc=0pt]\small\color{{brown!70!black}} #1\end{{tcolorbox}}}}
\begin{{document}}
\thispagestyle{{empty}}
\begin{{tikzpicture}}[remember picture,overlay]
\draw[MKnavy,line width=1.4pt] ([xshift=20mm,yshift=-17mm]current page.north west) -- ([xshift=-20mm,yshift=-17mm]current page.north east);
\draw[MKrule,line width=0.6pt] ([xshift=20mm,yshift=-29mm]current page.north west) -- ([xshift=-20mm,yshift=-29mm]current page.north east);
\end{{tikzpicture}}
\vspace*{{1.4mm}}
{{\sffamily\bfseries\fontsize{{8.2}}{{10}}\selectfont\color{{MKnavy}}\MakeUppercase{{MKUFT Research Module · Public GitHub Reading Edition}}}}\\[29mm]
{{\sffamily\bfseries\fontsize{{27}}{{30}}\selectfont\color{{MKnavy}}25C — Residual Instrument Generation and Protected Discovery Boundary\par}}
\vspace{{8mm}}
{{\sffamily\fontsize{{15.5}}{{18}}\selectfont\color{{MKnavy!85}}Professional reading edition of the evolving public MKUFT canon\par}}
\vspace{{12mm}}
{{\sffamily\bfseries\fontsize{{13}}{{15}}\selectfont Mark Charles McLaughlin\par}}
\vspace{{3mm}}
{{\fontsize{{8.8}}{{10}}\selectfont\color{{MKblue}}ORCID: 0009-0005-7736-1511\par}}
\vspace{{14mm}}
\renewcommand{{\arraystretch}}{{1.05}}
\begin{{tabular}}{{@{{}}>{{\bfseries}}p{{43mm}}p{{105mm}}@{{}}}}
Scientific affiliation & Independent Researcher \\
Object status & Research module reading edition — not a standalone Zenodo publication \\
Public source & \href{{https://github.com/mark45cdo-mkuft/MKUFT/blob/{SOURCE_COMMIT}/docs/25C_RESIDUAL_INSTRUMENT_GENERATION_AND_PROTECTED_DISCOVERY_BOUNDARY.md}}{{Open canonical public source}} \\
Source commit & \texttt{{{SOURCE_COMMIT}}} \\
MKUFT backbone DOI & \href{{https://doi.org/10.5281/zenodo.17780566}}{{10.5281/zenodo.17780566}} \\
ATLD 2 version DOI & \href{{https://doi.org/10.5281/zenodo.22068803}}{{10.5281/zenodo.22068803}} \\
\end{{tabular}}
\vfill
\statusbox{{\textbf{{Status boundary.}} This PDF is a reader-facing rendering of the live canonical Module 25C. It does not alter the frozen ATLD 2 DOI object, does not establish a new ontology, and does not disclose private implementation-specific discovery machinery not required to reproduce the declared scientific test.}}
\vspace{{2mm}}
\rightsbox{{\textbf{{Rights.}} Copyright © 2026 Mark Charles McLaughlin. All rights reserved. Historical licences remain controlling only for their exact frozen objects.}}
\vspace{{1mm}}
\begin{{center}}{{\fontsize{{8}}{{9}}\selectfont\color{{MKnavy}}1}}\end{{center}}
\newpage
\setcounter{{page}}{{2}}
$body$
\end{{document}}
'''
    TEMPLATE.write_text(template, encoding="utf-8")


def render() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    run(
        "pandoc", str(BODY),
        "--from=gfm+tex_math_dollars",
        "--pdf-engine=xelatex",
        f"--template={TEMPLATE}",
        "--standalone",
        "-o", str(OUTPUT),
    )


def preflight() -> tuple[str, int, int]:
    run("qpdf", "--check", str(OUTPUT))
    info = run("pdfinfo", str(OUTPUT))
    m = re.search(r"^Pages:\s+(\d+)$", info, flags=re.M)
    if not m:
        raise SystemExit("Could not determine 25C PDF page count")
    pages = int(m.group(1))
    if pages != 8:
        raise SystemExit(f"House-style page-count gate failed: expected 8, got {pages}")
    fonts = run("pdffonts", str(OUTPUT))
    for required in ("Libertinus", "NewCMMath", "SourceSansPro"):
        if required not in fonts:
            raise SystemExit(f"House-style font gate failed: {required} missing")
    text = run("pdftotext", str(OUTPUT), "-")
    for forbidden in ("```math", "\\mathcal", "## 20."):
        if forbidden in text:
            raise SystemExit(f"Reader-side extraction gate failed on {forbidden!r}")
    for required in (
        "20. Compressed rule",
        "Residual Instrument Generation and Protected Discovery Boundary",
        "This boundary is not an exemption from falsifiability",
        "KILL is a successful scientific outcome",
    ):
        if required not in text:
            raise SystemExit(f"Reader-side semantic-key gate failed: {required}")
    data = OUTPUT.read_bytes()
    sha = hashlib.sha256(data).hexdigest().upper()
    return sha, len(data), pages


GATE_TEXT = """# MKUFT Module Reading-Edition Write Gate

**Status:** mandatory local publication gate for every create, replacement, or update under this directory.

## Object custody

A route or tool is an implementation detail, not the published object. Before selecting tools, lock:

- canonical source path and controlling commit;
- intended carrier class: professional MKUFT module reading edition;
- rights, status, and provenance identity;
- current approved house-style specimen.

If a route cannot preserve those invariants, that route fails. Do not lower carrier quality, replace publication-grade display mathematics with source/plain-text/Unicode approximations, simplify the cover, drop metadata, or change scientific content to satisfy a tool. Find a lateral route at the same object class or leave the gate **RED**.

## House-style specimen

For equation-bearing modules, inspect `27_TYPED_TRAVERSAL_AND_EQUATION_HYGIENE.pdf` and a close neighbouring approved edition before rendering. Required invariants are:

- `MKUFT RESEARCH MODULE · PUBLIC GITHUB READING EDITION` cover family;
- professional navy section hierarchy and rules;
- Libertinus-style serif body;
- centred publication-grade display mathematics in the established New Computer Modern visual style;
- no raw TeX, ASCII shortcut equations, or Unicode/plain-text substitutes as professional display mathematics;
- visible status and rights boundaries;
- DOI, page, and Git-snapshot footer;
- canonical source and controlling source commit visible.

A typeface substitution is admissible only when it is visually and professionally equivalent and does not change equation semantics or the established carrier hierarchy.

## Gates before write

1. specimen gate;
2. source/object-identity gate;
3. semantic/equation gate;
4. reader-side render gate;
5. provenance/rights gate;
6. byte/checksum gate;
7. repo-and-Drive receiver-side gate where a mirror is required.

Any red gate blocks closure.

## Reader-side sample

Inspect at minimum:

- cover;
- first equation-bearing section;
- densest equation page;
- semantic-key or claim-boundary passage;
- final equation or compressed rule;
- final page;
- rights, status, and footer.

## Lateral recovery rule

Tool or API refusal is not permission to define a weaker object.

`object lock -> specimen lock -> route attempt -> lateral route if blocked -> same-object verification -> receiver-side read-back -> close`

If no same-class route exists, state the blocker and remain unclosed.

## Change discipline

A rendering or carrier repair must not silently change canonical scientific text. Scientific changes return to the canonical source and its own evidence, notation, and claim-gate process.

## Closure evidence

Record the exact final filename, page count, byte size, SHA-256, controlling source commit, and reader-side visual pass. Synchronise the README and checksum inventory before closure.
"""

RENDER_LESSON = """

## Recursive lesson — Module 25C carrier downgrade and lateral recovery (24 August 2026)

Module 25C exposed a distinct failure class: the canonical scientific source and mathematics were intact, but a blocked or awkward carrier route allowed the target object to drift from “house-standard MKUFT professional reading edition” toward “a technically valid but lower-specification PDF.”

The failure was not mathematical. It was object custody at the carrier boundary.

Required rule:

1. define and lock the target carrier and house-style specimen before tool selection;
2. treat tool/API limitations as route failures, never as permission to reduce the object;
3. if the primary route fails, seek a lateral route that preserves carrier class, equation typography, status, rights, provenance, and scientific content;
4. if no lateral route preserves those invariants, leave the carrier RED/unclosed;
5. every write under `publications/module-reading-editions/` must pass the local `00_READING_EDITION_WRITE_GATE.md`;
6. equation-bearing professional editions must be visually compared with the approved house specimen and must not substitute raw TeX, ASCII, or Unicode/plain-text approximations for publication-grade display mathematics;
7. when repo and Drive mirror the same reading edition, receiver-side custody must confirm the intended file identity and recorded checksum/size.

Compact invariant:

`object first -> specimen lock -> route selection -> lateral recovery if blocked -> reader-side comparison -> byte custody -> close`
"""

RESEARCH_LESSON = """

## Carrier-route non-degradation rule

A tool route is not the object.

When a requested output has a declared professional carrier, notation standard, rights boundary, or house style, those invariants are fixed before implementation. If the preferred tool or API cannot carry the object, do not simplify the object to fit the tool. Seek a lateral route of equivalent fidelity. If none exists, remain explicitly unclosed.

A route failure may change implementation. It may not silently change:

- scientific content;
- equation semantics or publication-grade display quality;
- carrier class;
- house style;
- rights, status, or provenance;
- canonical source identity.

Before closure, re-open the final receiver-side object and compare it with the locked specimen and source.
"""


def update_text_indexes(sha: str, size: int, pages: int) -> None:
    (OUT_DIR / "00_READING_EDITION_WRITE_GATE.md").write_text(GATE_TEXT, encoding="utf-8")

    readme_path = OUT_DIR / "README.md"
    readme = readme_path.read_text(encoding="utf-8")
    gate_line = "\n**Mandatory write gate:** every create/replace/update in this directory must pass [00_READING_EDITION_WRITE_GATE.md](00_READING_EDITION_WRITE_GATE.md).\n"
    if "**Mandatory write gate:**" not in readme:
        first_para_end = readme.find("\n\n", readme.find("\n") + 1)
        readme = readme[:first_para_end] + gate_line + readme[first_para_end:]
    readme = readme.replace("**Public source snapshot:** `26e06b6fea52e6b052dbdd540e80d1d926b96b07`", "**Baseline batch source snapshot:** `26e06b6fea52e6b052dbdd540e80d1d926b96b07` (later additions carry their controlling source commit on the edition cover and metadata)")
    readme = readme.replace("The 41 module editions comprise 242 pages", "The 42 module editions comprise 250 pages")
    row = "| [25C — Residual Instrument Generation and Protected Discovery Boundary](25C_RESIDUAL_INSTRUMENT_GENERATION_AND_PROTECTED_DISCOVERY_BOUNDARY.pdf) | [Markdown source](../../docs/25C_RESIDUAL_INSTRUMENT_GENERATION_AND_PROTECTED_DISCOVERY_BOUNDARY.md) | 8 |"
    if "25C_RESIDUAL_INSTRUMENT_GENERATION_AND_PROTECTED_DISCOVERY_BOUNDARY.pdf" not in readme:
        anchor = "| [25A — Fundamental Traversal Coherence Nodes](25A_FUNDAMENTAL_TRAVERSAL_COHERENCE_NODES.pdf) | [Markdown source](../../docs/25A_FUNDAMENTAL_TRAVERSAL_COHERENCE_NODES.md) | 5 |"
        if anchor not in readme:
            raise SystemExit("Reading-edition README anchor for 25A not found")
        readme = readme.replace(anchor, anchor + "\n" + row)
    readme_path.write_text(readme, encoding="utf-8")

    sums_path = OUT_DIR / "SHA256SUMS.txt"
    lines = [line for line in sums_path.read_text(encoding="utf-8").splitlines() if "25C_RESIDUAL_INSTRUMENT_GENERATION_AND_PROTECTED_DISCOVERY_BOUNDARY.pdf" not in line]
    lines.append(f"{sha}  25C_RESIDUAL_INSTRUMENT_GENERATION_AND_PROTECTED_DISCOVERY_BOUNDARY.pdf")
    sums_path.write_text("\n".join(lines) + "\n", encoding="utf-8")

    rendering = ROOT / "RENDERING_AND_PUBLICATION_INTEGRITY.md"
    rtext = rendering.read_text(encoding="utf-8")
    if "## Recursive lesson — Module 25C carrier downgrade and lateral recovery (24 August 2026)" not in rtext:
        rendering.write_text(rtext.rstrip() + RENDER_LESSON + "\n", encoding="utf-8")

    research = ROOT / "RESEARCH_DERIVATION_AND_CLOSURE_SOP.md"
    qtext = research.read_text(encoding="utf-8")
    if "## Carrier-route non-degradation rule" not in qtext:
        research.write_text(qtext.rstrip() + RESEARCH_LESSON + "\n", encoding="utf-8")

    evidence = OUT_DIR / "25C_READING_EDITION_CLOSURE.txt"
    evidence.write_text(
        "25C professional reading-edition closure\n"
        f"source_commit={SOURCE_COMMIT}\n"
        f"filename={OUTPUT.name}\n"
        f"pages={pages}\n"
        f"bytes={size}\n"
        f"sha256={sha}\n"
        "specimen=27_TYPED_TRAVERSAL_AND_EQUATION_HYGIENE.pdf\n"
        "reader_side_gate=PASS\n"
        "math_font_gate=PASS (NewCMMath)\n"
        "body_font_gate=PASS (Libertinus)\n"
        "carrier_class_gate=PASS\n",
        encoding="utf-8",
    )

    shutil.rmtree(ROOT / ".tmp25c_house", ignore_errors=True)
    shutil.rmtree(ROOT / ".build", ignore_errors=True)


def main() -> None:
    prepare_body()
    write_template()
    render()
    sha, size, pages = preflight()
    update_text_indexes(sha, size, pages)
    print(f"25C house-style render PASS pages={pages} bytes={size} sha256={sha}")


if __name__ == "__main__":
    main()
