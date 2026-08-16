#!/usr/bin/env python3
"""Check that MKUFT standalone research objects remain discoverable and correctly typed."""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = {
    "papers/README.md": [
        "10.5281/zenodo.18178638",
        "10.5281/zenodo.21341521",
        "2026-08-15_RECURSIVE_CONSTRAINT_CLOSURE_AND_REACHABLE_STATE_GEOMETRY_PREPRINT.md",
        "2026-08-16_LAYER_BEFORE_LAW_CANONICAL_PREPRINT_v1.0.md",
    ],
    "papers/2026-05-20_VOYNICH_MANUSCRIPT_SYSTEMS_ENGINE_FRAMEWORK.md": [
        "10.5281/zenodo.18178638",
        "10.5281/zenodo.18178637",
        "docs/09_VOYNICH_PROCEDURAL_ENGINE.md",
    ],
    "VOYNICH_STANDALONE_PUBLICATION.md": [
        "10.5281/zenodo.18178638",
        "10.5281/zenodo.18178637",
    ],
    "papers/2026-07-13_ATLD_EVALUATION_PROTOCOL_v1.0.md": [
        "10.5281/zenodo.21341521",
        "10.5281/zenodo.21341520",
        "publications/ATLD_Evaluation_Protocol_v1.0",
    ],
    "ATLD_STANDALONE_PUBLICATION.md": [
        "10.5281/zenodo.21341521",
        "10.5281/zenodo.21341520",
    ],
    "publications/README.md": [
        "10.5281/zenodo.18178638",
        "10.5281/zenodo.21341521",
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

    for rel in FROZEN_ATLD:
        if not (ROOT / rel).exists():
            failures.append(f"missing frozen ATLD preservation object: {rel}")

    # The live SIPO capstone is intentionally a module, not a paper.
    if not (ROOT / "docs/33_SIPO_CAPSTONE_CONSTRAINT_CONDITIONED_ADDRESSED_UPDATE_LAW.md").exists():
        failures.append("missing live SIPO capstone module")
    if (ROOT / "papers/33_SIPO_CAPSTONE_CONSTRAINT_CONDITIONED_ADDRESSED_UPDATE_LAW.md").exists():
        failures.append("SIPO capstone has been silently promoted into papers without an explicit publication object")

    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        return 1

    print("PASS: publication routes, DOI custody, and module/paper boundaries are intact.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
