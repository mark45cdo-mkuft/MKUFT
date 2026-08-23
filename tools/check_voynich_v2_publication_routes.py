#!/usr/bin/env python3
"""Verify the Voynich v2 publication fold without erasing historical lineage."""

from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]

CURRENT = "10.5281/zenodo.22071229"
CONCEPT = "10.5281/zenodo.18178637"
HISTORICAL = "10.5281/zenodo.18178638"
MKUFT_CURRENT = "10.5281/zenodo.21973064"
MKUFT_HISTORICAL = "10.5281/zenodo.17780566"
CURRENT_PAPER = "papers/2026-08-23_VOYNICH_ESRT_ESF_CONSOLIDATED_v2.0.md"
HISTORICAL_PAPER = "papers/2026-05-20_VOYNICH_MANUSCRIPT_SYSTEMS_ENGINE_FRAMEWORK.md"
SUPPORT = "docs/07_ESRT_ESF_AND_VOYNICH_SUPPORT.md"
METHOD = "docs/10_ESRT_ESF_METHOD_APPENDIX.md"
HYPOTHESIS = "docs/09_VOYNICH_PROCEDURAL_ENGINE.md"
MD5 = "dd0d6a7176da51ce69b9466408df4c39"
SHA256 = "367f961ef33961ade02e19ac3e440844606dc6fc250b269d59951d366540fcff"

REQUIRED = {
    "VOYNICH_STANDALONE_PUBLICATION.md": [
        CURRENT,
        CONCEPT,
        HISTORICAL,
        MKUFT_CURRENT,
        MKUFT_HISTORICAL,
        CURRENT_PAPER,
        HISTORICAL_PAPER,
        SUPPORT,
        HYPOTHESIS,
        METHOD,
        "16",
        "430,789",
        MD5,
        SHA256,
        "does not erase",
    ],
    CURRENT_PAPER: [
        CURRENT,
        CONCEPT,
        HISTORICAL,
        MKUFT_CURRENT,
        MKUFT_HISTORICAL,
        "Candidate Procedural-Executable Information System",
        "Addressing",
        "State",
        "Flow",
        "does not claim",
        SUPPORT,
        HYPOTHESIS,
        METHOD,
        MD5,
        SHA256,
    ],
    HISTORICAL_PAPER: [
        HISTORICAL,
        CONCEPT,
    ],
    "papers/README.md": [
        CURRENT,
        CONCEPT,
        HISTORICAL,
        CURRENT_PAPER,
        HISTORICAL_PAPER,
        "recommended scientific reading object",
    ],
    "INDEX.md": [
        CURRENT,
        CONCEPT,
        HISTORICAL,
        CURRENT_PAPER,
        SUPPORT,
        HYPOTHESIS,
        METHOD,
    ],
    "PROVENANCE_DOI_AND_ATTRIBUTION.md": [
        CURRENT,
        CONCEPT,
        HISTORICAL,
        CURRENT_PAPER,
        HISTORICAL_PAPER,
        MD5,
        SHA256,
    ],
    "PUBLIC_DISCOVERY_ANCHOR.md": [
        CURRENT,
        CONCEPT,
        HISTORICAL,
        CURRENT_PAPER,
        "procedural-executable",
    ],
    "DISCOVERY_KEYWORDS.md": [
        CURRENT,
        CONCEPT,
        HISTORICAL,
        CURRENT_PAPER,
        "Addressing State Flow",
    ],
    SUPPORT: [
        CURRENT,
        CONCEPT,
        HISTORICAL,
        CURRENT_PAPER,
        "does not erase",
    ],
}


def main() -> int:
    failures = []

    for rel, needles in REQUIRED.items():
        path = ROOT / rel
        if not path.exists():
            failures.append(f"missing Voynich v2 route: {rel}")
            continue
        text = path.read_text(encoding="utf-8")
        for needle in needles:
            if needle not in text:
                failures.append(f"{rel}: missing required Voynich v2 marker: {needle}")

    try:
        codemeta = json.loads((ROOT / "codemeta.json").read_text(encoding="utf-8"))
    except Exception as exc:
        failures.append(f"codemeta.json invalid: {exc}")
    else:
        citations = set(codemeta.get("citation", []))
        for doi in (CURRENT, CONCEPT, HISTORICAL, MKUFT_CURRENT, MKUFT_HISTORICAL):
            url = f"https://doi.org/{doi}"
            if url not in citations:
                failures.append(f"codemeta.json missing Voynich/MKUFT lineage citation: {url}")
        subjects = set(codemeta.get("subjectOf", []))
        expected_subject = "https://github.com/mark45cdo-mkuft/MKUFT/blob/main/" + CURRENT_PAPER
        if expected_subject not in subjects:
            failures.append("codemeta.json missing current Voynich v2 paper route")

    historical_text = (ROOT / HISTORICAL_PAPER).read_text(encoding="utf-8")
    if CURRENT in historical_text:
        failures.append("historical Voynich reading edition was silently rewritten with the v2 DOI")

    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        return 1

    print(
        "PASS: Voynich v2.0 current DOI, concept lineage, historical predecessor, "
        "MKUFT support routes, discovery/provenance metadata, and frozen-carrier identity are coherent."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
