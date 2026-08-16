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
MKUFT_DOI = "10.5281/zenodo.17780566"

REQUIRED = {
    "README.md": [
        "papers/README.md",
        VOYNICH_VERSION,
        ATLD_VERSION,
        "Recursive Constraint Closure",
        "Layer Before Law",
    ],
    "INDEX.md": [
        "papers/README.md",
        VOYNICH_VERSION,
        ATLD_VERSION,
        "VOYNICH_STANDALONE_PUBLICATION.md",
        "LAYER_BEFORE_LAW_STANDALONE_PUBLICATION.md",
    ],
    "papers/README.md": [
        VOYNICH_VERSION,
        ATLD_VERSION,
        "2026-08-15_RECURSIVE_CONSTRAINT_CLOSURE_AND_REACHABLE_STATE_GEOMETRY_PREPRINT.md",
        "2026-08-16_LAYER_BEFORE_LAW_CANONICAL_PREPRINT_v1.0.md",
        "not a standalone paper",
    ],
    "PUBLIC_DISCOVERY_ANCHOR.md": [
        VOYNICH_VERSION,
        VOYNICH_CONCEPT,
        ATLD_VERSION,
        ATLD_CONCEPT,
        "papers/README.md",
        "Layer Before Law",
        "Recursive Constraint Closure",
    ],
    "DISCOVERY_KEYWORDS.md": [
        VOYNICH_VERSION,
        ATLD_VERSION,
        "Layer Before Law standalone DOI: pending",
        "Recursive Constraint Closure standalone DOI: pending",
    ],
    "PROVENANCE_DOI_AND_ATTRIBUTION.md": [
        MKUFT_DOI,
        VOYNICH_VERSION,
        VOYNICH_CONCEPT,
        ATLD_VERSION,
        ATLD_CONCEPT,
        "VOYNICH_STANDALONE_PUBLICATION.md",
        "papers/README.md",
        "standalone DOI: pending exact frozen deposit",
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
    "publications/README.md": [
        VOYNICH_VERSION,
        ATLD_VERSION,
        "Layer Before Law",
        "Recursive Constraint Closure",
    ],
    "papers/2026-08-15_RECURSIVE_CONSTRAINT_CLOSURE_AND_REACHABLE_STATE_GEOMETRY_PREPRINT.md": [
        "Recursive Constraint Closure",
    ],
    "RECURSIVE_CONSTRAINT_CLOSURE_STANDALONE_PUBLICATION.md": [
        "Recursive Constraint Closure",
    ],
    "papers/2026-08-16_LAYER_BEFORE_LAW_CANONICAL_PREPRINT_v1.0.md": [
        "Layer Before Law",
        "Standalone DOI",
    ],
    "LAYER_BEFORE_LAW_STANDALONE_PUBLICATION.md": [
        "Layer Before Law",
        "pending",
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

    # JSON-LD must remain valid JSON and expose all frozen DOI-bearing research nodes.
    codemeta_path = ROOT / "codemeta.json"
    try:
        codemeta = json.loads(codemeta_path.read_text(encoding="utf-8"))
    except Exception as exc:
        failures.append(f"codemeta.json is not valid JSON: {exc}")
    else:
        citations = set(codemeta.get("citation", []))
        for doi in (MKUFT_DOI, VOYNICH_VERSION, ATLD_VERSION):
            url = f"https://doi.org/{doi}"
            if url not in citations:
                failures.append(f"codemeta.json: missing citation {url}")
        author = codemeta.get("author", {})
        if author.get("identifier") != "https://orcid.org/0009-0005-7736-1511":
            failures.append("codemeta.json: author ORCID route missing or incorrect")

    # CITATION.cff intentionally identifies the MKUFT backbone rather than pretending
    # to be one omnibus citation for every separately published paper.
    citation_text = (ROOT / "CITATION.cff").read_text(encoding="utf-8")
    if MKUFT_DOI not in citation_text:
        failures.append("CITATION.cff: MKUFT backbone DOI missing")
    if "preferred-citation" not in citation_text:
        failures.append("CITATION.cff: preferred-citation missing")

    for rel in FROZEN_ATLD:
        if not (ROOT / rel).exists():
            failures.append(f"missing frozen ATLD preservation object: {rel}")

    # The live SIPO capstone is intentionally a module, not a paper.
    if not (ROOT / "docs/33_SIPO_CAPSTONE_CONSTRAINT_CONDITIONED_ADDRESSED_UPDATE_LAW.md").exists():
        failures.append("missing live SIPO capstone module")
    if (ROOT / "papers/33_SIPO_CAPSTONE_CONSTRAINT_CONDITIONED_ADDRESSED_UPDATE_LAW.md").exists():
        failures.append("SIPO capstone has been silently promoted into papers without an explicit publication object")

    # Temporary repair machinery must not remain in the public workflow surface.
    temp_workflows = sorted((ROOT / ".github" / "workflows").glob("_temp_*.yml"))
    if temp_workflows:
        failures.append("temporary repair workflows remain: " + ", ".join(str(p.relative_to(ROOT)) for p in temp_workflows))

    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        return 1

    print("PASS: publication routes, DOI custody, discovery metadata, and module/paper boundaries are intact.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
