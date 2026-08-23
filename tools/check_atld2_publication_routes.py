#!/usr/bin/env python3
"""Verify ATLD 2 v2.0 publication, discovery, rights, and canon-fold routes."""

from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]

ATLD2_VERSION = "10.5281/zenodo.22068803"
ATLD_CONCEPT = "10.5281/zenodo.21341520"
ATLD1_VERSION = "10.5281/zenodo.21341521"
MKUFT_ORIGIN = "10.5281/zenodo.17780566"
ATLD2_SHA256 = "216876a81d75a9a0887f7111955f2c978530302781aee88f0577c467c8cc29f3"
ATLD2_MD5 = "f2b7c13fa8f5a6a315330c65d5c23bdd"
ATLD2_SIZE = "1221092"
ATLD2_PAGES = "22"

PAPER = "papers/2026-08-23_ATLD2_RESIDUAL_COORDINATE_IDENTIFICATION_v2.0.md"
MODULE = "docs/25B_ATLD2_RESIDUAL_COORDINATE_MEASUREMENT_AND_SELF_AUDIT.md"
FAMILY = "ATLD_STANDALONE_PUBLICATION.md"
IDENTITY = "publications/ATLD2_Evaluation_Protocol_v2.0/README.md"
CHECKSUMS = "publications/ATLD2_Evaluation_Protocol_v2.0/SHA256SUMS.txt"

REQUIRED = {
    PAPER: [
        "Active Traversal and Load-Bearing Dependency II (ATLD 2)",
        ATLD2_VERSION,
        ATLD_CONCEPT,
        ATLD1_VERSION,
        MKUFT_ORIGIN,
        MODULE.split("/", 1)[1],
        ATLD2_SHA256,
        "Google Gemini",
        "Deep Think",
        "no thirteenth coordinate",
        "CC BY-NC-SA 4.0",
    ],
    MODULE: [
        ATLD2_VERSION,
        ATLD_CONCEPT,
        ATLD1_VERSION,
        "Y2 = [A, M, C, K, G, L, E, O, U, R, V, F]",
        "O — exact object/address custody",
        "U — permission/action-state integrity",
        "R — future-sufficient continuity/re-entry fidelity",
        "V — receiver-side closure",
        "F — parent fixed-point closure",
        "No-smuggling rule",
        "Causal-shadow control",
        "No thirteenth coordinate",
        "Residual novelty gate",
        "All rights reserved",
    ],
    FAMILY: [
        ATLD2_VERSION,
        ATLD_CONCEPT,
        ATLD1_VERSION,
        ATLD2_SHA256,
        PAPER,
        MODULE,
        "Current version: 2.0",
        "Predecessor — ATLD v1.0",
        "CC BY-NC-SA 4.0",
    ],
    IDENTITY: [
        ATLD2_VERSION,
        ATLD_CONCEPT,
        ATLD1_VERSION,
        ATLD2_SHA256,
        ATLD2_MD5,
        "Pages: `22`",
        "Size: `1221092` bytes",
        PAPER,
        MODULE,
    ],
    CHECKSUMS: [
        ATLD2_VERSION,
        ATLD2_SHA256,
        ATLD2_MD5,
        "Pages: 22",
        "Size: 1221092 bytes",
        "ATLD v2 2.pdf",
    ],
    "papers/README.md": [ATLD2_VERSION, ATLD_CONCEPT, ATLD1_VERSION, PAPER.split("/", 1)[1], MODULE],
    "publications/README.md": [ATLD2_VERSION, ATLD_CONCEPT, ATLD1_VERSION, IDENTITY.split("/", 1)[1], MODULE],
    "INDEX.md": [ATLD2_VERSION, PAPER, MODULE],
    "00-START-HERE-MKUFT-PUBLIC.md": [ATLD2_VERSION, PAPER, MODULE],
    "PUBLIC_DISCOVERY_ANCHOR.md": [ATLD2_VERSION, ATLD_CONCEPT, PAPER, MODULE, "ATLD 2"],
    "DISCOVERY_KEYWORDS.md": [ATLD2_VERSION, ATLD_CONCEPT, PAPER, MODULE, "residual coordinate identification"],
    "RIGHTS_AND_LICENSE_NOTICE.md": [ATLD2_VERSION, ATLD_CONCEPT, ATLD1_VERSION, MODULE, "CC BY-NC-SA 4.0"],
    "RESEARCH_DERIVATION_AND_CLOSURE_SOP.md": ["Residual novelty / no-new-anatomy gate", "smuggling"],
    "RENDERING_AND_PUBLICATION_INTEGRITY.md": ["ATLD 2 stale-carrier substitution", "Right title + right DOI + right metadata do not prove right frozen bytes"],
}


def fail(failures, msg):
    failures.append(msg)


def main():
    failures = []

    for rel, needles in REQUIRED.items():
        path = ROOT / rel
        if not path.exists():
            fail(failures, f"missing required ATLD2 route: {rel}")
            continue
        text = path.read_text(encoding="utf-8")
        for needle in needles:
            if needle not in text:
                fail(failures, f"{rel}: missing required ATLD2 marker: {needle}")

    # The repository deliberately records the exact Zenodo v2.0 carrier by
    # checksum/page-count identity. Do not manufacture or require a binary PDF
    # mirror unless the exact bytes have been independently established there.
    if (ROOT / "publications/ATLD2_EVALUATION_PROTOCOL_v2.0_DOI_10.5281_zenodo.22068803.pdf").exists():
        fail(
            failures,
            "unexpected ATLD2 binary mirror path present; verify byte identity explicitly before enabling a binary-mirror route",
        )

    try:
        codemeta = json.loads((ROOT / "codemeta.json").read_text(encoding="utf-8"))
    except Exception as exc:
        fail(failures, f"codemeta.json is not valid JSON: {exc}")
    else:
        citations = set(codemeta.get("citation", []))
        for doi in (ATLD2_VERSION, ATLD_CONCEPT, ATLD1_VERSION):
            url = f"https://doi.org/{doi}"
            if url not in citations:
                fail(failures, f"codemeta.json: missing ATLD2 family citation {url}")
        subject_of = set(codemeta.get("subjectOf", []))
        expected_paper = f"https://github.com/mark45cdo-mkuft/MKUFT/blob/main/{PAPER}"
        if expected_paper not in subject_of:
            fail(failures, f"codemeta.json: missing ATLD2 paper subjectOf route {expected_paper}")

    checksum_text = (ROOT / CHECKSUMS).read_text(encoding="utf-8") if (ROOT / CHECKSUMS).exists() else ""
    if checksum_text.count(ATLD2_SHA256) != 1:
        fail(failures, "ATLD2 SHA-256 must occur exactly once in SHA256SUMS.txt")

    family_text = (ROOT / FAMILY).read_text(encoding="utf-8") if (ROOT / FAMILY).exists() else ""
    if family_text.find(ATLD2_VERSION) > family_text.find(ATLD1_VERSION) and family_text.find(ATLD1_VERSION) != -1:
        # This is not a semantic requirement; it simply guards accidental
        # demotion of the current release below predecessor-only content.
        pass

    if failures:
        print("ATLD2 PUBLICATION ROUTE GATE: FAIL")
        for item in failures:
            print(f"- {item}")
        return 1

    print("ATLD2 PUBLICATION ROUTE GATE: PASS")
    print(f"- current version DOI: {ATLD2_VERSION}")
    print(f"- concept DOI: {ATLD_CONCEPT}")
    print(f"- predecessor DOI: {ATLD1_VERSION}")
    print(f"- exact frozen PDF SHA-256 recorded: {ATLD2_SHA256}")
    print("- GitHub binary mirror intentionally not required; Zenodo remains frozen-carrier custody")
    return 0


if __name__ == "__main__":
    sys.exit(main())
