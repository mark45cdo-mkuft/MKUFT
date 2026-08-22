#!/usr/bin/env python3
"""Check that MKUFT standalone research objects remain discoverable and correctly typed."""

from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]

VOYNICH_VERSION = "10.5281/zenodo.18178638"
VOYNICH_CONCEPT = "10.5281/zenodo.18178637"
ATLD_VERSION = "10.5281/zenodo.21341521"
ATLD_CONCEPT = "10.5281/zenodo.21341520"
MKUFT_VERSION = "10.5281/zenodo.21973064"
MKUFT_CONCEPT = "10.5281/zenodo.17780565"
MKUFT_HISTORICAL = "10.5281/zenodo.17780566"
LAYER_BEFORE_LAW_VERSION = "10.5281/zenodo.21971270"
RCC_VERSION = "10.5281/zenodo.21971425"
AAF_VERSION = "10.5281/zenodo.22031333"
AAF_CONCEPT = "10.5281/zenodo.22031332"
FSSR_VERSION = "10.5281/zenodo.22058303"
FSSR_CONCEPT = "10.5281/zenodo.22058302"
FSSR_PAPER = "2026-08-22_FUTURE_SPLITTING_STATE_RECRUITMENT_v1.0.md"
FSSR_MODULE = "33S7_FUTURE_SPLITTING_STATE_RECRUITMENT_STATE_ADEQUACY_AND_PROSPECTIVE_MECHANISM_LOCALISATION.md"

REQUIRED = {
    "README.md": [
        "papers/README.md",
        VOYNICH_VERSION,
        ATLD_VERSION,
        FSSR_VERSION,
        "Future-Splitting State Recruitment",
        FSSR_PAPER,
        FSSR_MODULE,
        "Recursive Constraint Closure",
        "Layer Before Law",
    ],
    "INDEX.md": [
        "papers/README.md",
        VOYNICH_VERSION,
        ATLD_VERSION,
        FSSR_VERSION,
        "FSSR_STANDALONE_PUBLICATION.md",
        FSSR_PAPER,
        FSSR_MODULE,
        "VOYNICH_STANDALONE_PUBLICATION.md",
        "LAYER_BEFORE_LAW_STANDALONE_PUBLICATION.md",
    ],
    "CANON_MAP.md": [
        FSSR_VERSION,
        FSSR_MODULE,
        "Future-Splitting State Recruitment",
        "33S4–33S7",
    ],
    "papers/README.md": [
        VOYNICH_VERSION,
        ATLD_VERSION,
        LAYER_BEFORE_LAW_VERSION,
        RCC_VERSION,
        AAF_VERSION,
        FSSR_VERSION,
        "FSSR_STANDALONE_PUBLICATION.md",
        FSSR_PAPER,
        FSSR_MODULE,
        "2026-08-15_RECURSIVE_CONSTRAINT_CLOSURE_AND_REACHABLE_STATE_GEOMETRY_PREPRINT.md",
        "2026-08-16_LAYER_BEFORE_LAW_CANONICAL_PREPRINT_v1.0.md",
        "not a standalone paper",
    ],
    "PUBLIC_DISCOVERY_ANCHOR.md": [
        VOYNICH_VERSION,
        VOYNICH_CONCEPT,
        ATLD_VERSION,
        ATLD_CONCEPT,
        AAF_VERSION,
        AAF_CONCEPT,
        FSSR_VERSION,
        FSSR_CONCEPT,
        "papers/README.md",
        "Future-Splitting State Recruitment",
        "Layer Before Law",
        "Recursive Constraint Closure",
    ],
    "DISCOVERY_KEYWORDS.md": [
        VOYNICH_VERSION,
        ATLD_VERSION,
        LAYER_BEFORE_LAW_VERSION,
        RCC_VERSION,
        AAF_VERSION,
        AAF_CONCEPT,
        FSSR_VERSION,
        FSSR_CONCEPT,
        "Future-Splitting State Recruitment",
        "FSSR",
        FSSR_MODULE,
    ],
    "PROVENANCE_DOI_AND_ATTRIBUTION.md": [
        MKUFT_VERSION,
        MKUFT_CONCEPT,
        MKUFT_HISTORICAL,
        VOYNICH_VERSION,
        VOYNICH_CONCEPT,
        ATLD_VERSION,
        ATLD_CONCEPT,
        LAYER_BEFORE_LAW_VERSION,
        RCC_VERSION,
        AAF_VERSION,
        AAF_CONCEPT,
        FSSR_VERSION,
        FSSR_CONCEPT,
        "FSSR_STANDALONE_PUBLICATION.md",
        f"docs/{FSSR_MODULE}",
        "VOYNICH_STANDALONE_PUBLICATION.md",
        "papers/README.md",
    ],
    "MODULE_RIGHTS_MATRIX.md": [
        FSSR_VERSION,
        FSSR_CONCEPT,
        AAF_VERSION,
        AAF_CONCEPT,
        FSSR_MODULE,
        "All rights reserved",
    ],
    "RIGHTS_AND_LICENSE_NOTICE.md": [
        FSSR_VERSION,
        FSSR_CONCEPT,
        AAF_VERSION,
        AAF_CONCEPT,
        "Future-Splitting State Recruitment standalone paper",
        "All rights reserved",
    ],
    "papers/2026-05-20_VOYNICH_MANUSCRIPT_SYSTEMS_ENGINE_FRAMEWORK.md": [
        VOYNICH_VERSION,
        VOYNICH_CONCEPT,
        "docs/09_VOYNICH_PROCEDURAL_ENGINE.md",
    ],
    "VOYNICH_STANDALONE_PUBLICATION.md": [
        VOYNICH_VERSION,
        VOYNICH_CONCEPT,
    ],
    "papers/2026-07-13_ATLD_EVALUATION_PROTOCOL_v1.0.md": [
        ATLD_VERSION,
        ATLD_CONCEPT,
        "publications/ATLD_Evaluation_Protocol_v1.0",
    ],
    "ATLD_STANDALONE_PUBLICATION.md": [
        ATLD_VERSION,
        ATLD_CONCEPT,
        "papers/2026-07-13_ATLD_EVALUATION_PROTOCOL_v1.0.md",
    ],
    "FSSR_STANDALONE_PUBLICATION.md": [
        FSSR_VERSION,
        FSSR_CONCEPT,
        f"papers/{FSSR_PAPER}",
        f"docs/{FSSR_MODULE}",
        "All rights reserved",
    ],
    f"papers/{FSSR_PAPER}": [
        FSSR_VERSION,
        FSSR_CONCEPT,
        "Future-Splitting State Recruitment",
        "Canonical MKUFT fold",
    ],
    f"docs/{FSSR_MODULE}": [
        FSSR_VERSION,
        FSSR_CONCEPT,
        "future-splitting",
        "state-recruitment event",
        "33S6",
    ],
    "publications/README.md": [
        VOYNICH_VERSION,
        ATLD_VERSION,
        FSSR_VERSION,
        FSSR_CONCEPT,
        FSSR_PAPER,
        FSSR_MODULE,
        "Layer Before Law",
        "Recursive Constraint Closure",
    ],
    "papers/2026-08-15_RECURSIVE_CONSTRAINT_CLOSURE_AND_REACHABLE_STATE_GEOMETRY_PREPRINT.md": [
        RCC_VERSION,
        "Recursive Constraint Closure",
    ],
    "RECURSIVE_CONSTRAINT_CLOSURE_STANDALONE_PUBLICATION.md": [
        RCC_VERSION,
        "Recursive Constraint Closure",
    ],
    "papers/2026-08-16_LAYER_BEFORE_LAW_CANONICAL_PREPRINT_v1.0.md": [
        LAYER_BEFORE_LAW_VERSION,
        "Layer Before Law",
        "Standalone DOI",
    ],
    "LAYER_BEFORE_LAW_STANDALONE_PUBLICATION.md": [
        LAYER_BEFORE_LAW_VERSION,
        "Layer Before Law",
    ],
    "AAF_STANDALONE_PUBLICATION.md": [
        AAF_VERSION,
        AAF_CONCEPT,
        "33S6_ADDRESSED_ADMISSIBLE_FUTURES",
    ],
    "RENDERING_AND_PUBLICATION_INTEGRITY.md": [
        "Source correctness does not prove publication correctness",
        "Every standalone paper must have a direct route",
    ],
}

FROZEN_ATLD = [
    "publications/ATLD_Evaluation_Protocol_v1.0/README.md",
    "publications/ATLD_Evaluation_Protocol_v1.0/SHA256SUMS.txt",
] + [f"publications/ATLD_Evaluation_Protocol_v1.0/part-{i:02d}.txt" for i in range(1, 9)]


def main():
    failures = []

    for rel, needles in REQUIRED.items():
        path = ROOT / rel
        if not path.exists():
            failures.append(f"missing required publication route: {rel}")
            continue
        text = path.read_text(encoding="utf-8")
        for needle in needles:
            if needle not in text:
                failures.append(f"{rel}: missing required identity marker: {needle}")

    codemeta_path = ROOT / "codemeta.json"
    try:
        codemeta = json.loads(codemeta_path.read_text(encoding="utf-8"))
    except Exception as exc:
        failures.append(f"codemeta.json is not valid JSON: {exc}")
    else:
        citations = set(codemeta.get("citation", []))
        for doi in (
            MKUFT_VERSION,
            MKUFT_CONCEPT,
            MKUFT_HISTORICAL,
            FSSR_VERSION,
            AAF_VERSION,
            LAYER_BEFORE_LAW_VERSION,
            RCC_VERSION,
            VOYNICH_VERSION,
            ATLD_VERSION,
        ):
            url = f"https://doi.org/{doi}"
            if url not in citations:
                failures.append(f"codemeta.json: missing citation {url}")
        author = codemeta.get("author", {})
        if author.get("identifier") != "https://orcid.org/0009-0005-7736-1511":
            failures.append("codemeta.json: author ORCID route missing or incorrect")

    citation_text = (ROOT / "CITATION.cff").read_text(encoding="utf-8")
    if MKUFT_VERSION not in citation_text:
        failures.append("CITATION.cff: current principal MKUFT DOI missing")
    if "preferred-citation" not in citation_text:
        failures.append("CITATION.cff: preferred-citation missing")

    for rel in FROZEN_ATLD:
        if not (ROOT / rel).exists():
            failures.append(f"missing frozen ATLD preservation object: {rel}")

    if not (ROOT / "docs/33_SIPO_CAPSTONE_CONSTRAINT_CONDITIONED_ADDRESSED_UPDATE_LAW.md").exists():
        failures.append("missing live SIPO capstone module")
    if not (ROOT / f"docs/{FSSR_MODULE}").exists():
        failures.append("missing live FSSR Module 33S7")
    if (ROOT / "papers/33_SIPO_CAPSTONE_CONSTRAINT_CONDITIONED_ADDRESSED_UPDATE_LAW.md").exists():
        failures.append("SIPO capstone has been silently promoted into papers without an explicit publication object")

    temp_workflows = sorted((ROOT / ".github" / "workflows").glob("_temp_*.yml"))
    if temp_workflows:
        failures.append("temporary repair workflows remain: " + ", ".join(str(p.relative_to(ROOT)) for p in temp_workflows))

    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        return 1

    print("PASS: publication routes, DOI custody, discovery metadata, rights routing, and module/paper boundaries are intact.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
