#!/usr/bin/env python3
"""Check that MKUFT standalone research objects remain discoverable and correctly typed."""

from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]

VOYNICH_CURRENT = "10.5281/zenodo.22071229"
VOYNICH_VERSION = "10.5281/zenodo.18178638"  # historical predecessor
VOYNICH_CONCEPT = "10.5281/zenodo.18178637"
VOYNICH_CURRENT_PAPER = "2026-08-23_VOYNICH_ESRT_ESF_CONSOLIDATED_v2.0.md"
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
BELL_VERSION = "10.5281/zenodo.22100926"
BELL_CONCEPT = "10.5281/zenodo.22100925"
BELL_PAPER = "2026-08-25_BELL_CONSTRAINTS_TYPED_BOUNDARIES_v1.0.md"
CROSS_DOMAIN_VERSION = "10.5281/zenodo.22166468"
CROSS_DOMAIN_PREVIOUS = "10.5281/zenodo.22166005"
CROSS_DOMAIN_EARLIER = "10.5281/zenodo.22164562"
CROSS_DOMAIN_CONCEPT = "10.5281/zenodo.22164561"
CROSS_DOMAIN_PAPER = "2026-08-29_CROSS_DOMAIN_COMPOSITIONAL_SCHEMA_v0.4.md"
CROSS_DOMAIN_MODULE = "33S7A_FUTURE_SUFFICIENT_ADDRESS_INVARIANT_AND_LAYER_BEFORE_LAW_PRECEDENCE.md"
CROSS_DOMAIN_BELL_MODULE = "28A_CROSS_DOMAIN_COMPOSITIONAL_SCHEMA_BELL_CHSH_CALIBRATION.md"
CROSS_DOMAIN_MD5 = "d5a56561e82ca5d64a8766ca8122a956"
CROSS_DOMAIN_SHA256 = "bcb5c7618962bac98c2ae0ad097f7bba8e9758d4c86879b6546d037736c73b83"

FROZEN_PDF_MIRRORS = [
    "publications/MKUFT_RELATIONAL_ARCHITECTURE_v2_DOI_10.5281_zenodo.21973064.pdf",
    "publications/HISTORICAL_V1_MKUFT_FALSIFICATIONS_DOI_10.5281_zenodo.17780566.pdf",
    "publications/HISTORICAL_V1_MKUFT_MATH_APPENDIX_DOI_10.5281_zenodo.17780566.pdf",
    "publications/FUTURE_SPLITTING_STATE_RECRUITMENT_v1.0_DOI_10.5281_zenodo.22058303.pdf",
    "publications/ADDRESSED_ADMISSIBLE_FUTURES_v0.1_DOI_10.5281_zenodo.22031333.pdf",
    "publications/LAYER_BEFORE_LAW_v1.0_DOI_10.5281_zenodo.21971270.pdf",
    "publications/RECURSIVE_CONSTRAINT_CLOSURE_v0.1_DOI_10.5281_zenodo.21971425.pdf",
    "publications/ATLD_EVALUATION_PROTOCOL_v1.0_DOI_10.5281_zenodo.21341521.pdf",
]

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
        CROSS_DOMAIN_VERSION,
        "docs/28A_CROSS_DOMAIN_COMPOSITIONAL_SCHEMA_BELL_CHSH_CALIBRATION.md",
        "docs/33S7A_FUTURE_SUFFICIENT_ADDRESS_INVARIANT_AND_LAYER_BEFORE_LAW_PRECEDENCE.md",
        "protocol-relative exact-relation deformation",
    ],
    "INDEX.md": [
        "papers/README.md",
        VOYNICH_CURRENT,
        VOYNICH_VERSION,
        VOYNICH_CONCEPT,
        VOYNICH_CURRENT_PAPER,
        ATLD_VERSION,
        FSSR_VERSION,
        BELL_VERSION,
        BELL_CONCEPT,
        CROSS_DOMAIN_VERSION,
        CROSS_DOMAIN_PREVIOUS,
        CROSS_DOMAIN_EARLIER,
        CROSS_DOMAIN_CONCEPT,
        CROSS_DOMAIN_PAPER,
        CROSS_DOMAIN_MODULE,
        CROSS_DOMAIN_BELL_MODULE,
        "CROSS_DOMAIN_COMPOSITIONAL_SCHEMA_STANDALONE_PUBLICATION.md",
        "BELL_CONSTRAINTS_STANDALONE_PUBLICATION.md",
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
        CROSS_DOMAIN_VERSION,
        "28A_CROSS_DOMAIN_COMPOSITIONAL_SCHEMA_BELL_CHSH_CALIBRATION.md",
        "Cross-Domain Compositional Schema Bell/CHSH Calibration",
    ],
    "papers/README.md": [
        VOYNICH_CURRENT,
        VOYNICH_VERSION,
        VOYNICH_CONCEPT,
        VOYNICH_CURRENT_PAPER,
        ATLD_VERSION,
        LAYER_BEFORE_LAW_VERSION,
        RCC_VERSION,
        AAF_VERSION,
        FSSR_VERSION,
        BELL_VERSION,
        BELL_CONCEPT,
        CROSS_DOMAIN_VERSION,
        CROSS_DOMAIN_PREVIOUS,
        CROSS_DOMAIN_EARLIER,
        CROSS_DOMAIN_CONCEPT,
        CROSS_DOMAIN_PAPER,
        "CROSS_DOMAIN_COMPOSITIONAL_SCHEMA_STANDALONE_PUBLICATION.md",
        "BELL_CONSTRAINTS_STANDALONE_PUBLICATION.md",
        "FSSR_STANDALONE_PUBLICATION.md",
        FSSR_PAPER,
        FSSR_MODULE,
        "2026-08-15_RECURSIVE_CONSTRAINT_CLOSURE_AND_REACHABLE_STATE_GEOMETRY_PREPRINT.md",
        "2026-08-16_LAYER_BEFORE_LAW_CANONICAL_PREPRINT_v1.0.md",
        "not a standalone paper",
        "MKUFT_RELATIONAL_ARCHITECTURE_v2_DOI_10.5281_zenodo.21973064.pdf",
        "HISTORICAL_V1_MKUFT_FALSIFICATIONS_DOI_10.5281_zenodo.17780566.pdf",
        "HISTORICAL_V1_MKUFT_MATH_APPENDIX_DOI_10.5281_zenodo.17780566.pdf",
        "FUTURE_SPLITTING_STATE_RECRUITMENT_v1.0_DOI_10.5281_zenodo.22058303.pdf",
        "ADDRESSED_ADMISSIBLE_FUTURES_v0.1_DOI_10.5281_zenodo.22031333.pdf",
        "LAYER_BEFORE_LAW_v1.0_DOI_10.5281_zenodo.21971270.pdf",
        "RECURSIVE_CONSTRAINT_CLOSURE_v0.1_DOI_10.5281_zenodo.21971425.pdf",
        "ATLD_EVALUATION_PROTOCOL_v1.0_DOI_10.5281_zenodo.21341521.pdf",
    ],
    "PUBLIC_DISCOVERY_ANCHOR.md": [
        VOYNICH_CURRENT,
        VOYNICH_VERSION,
        VOYNICH_CONCEPT,
        VOYNICH_CURRENT_PAPER,
        ATLD_VERSION,
        ATLD_CONCEPT,
        AAF_VERSION,
        AAF_CONCEPT,
        FSSR_VERSION,
        FSSR_CONCEPT,
        BELL_VERSION,
        BELL_CONCEPT,
        CROSS_DOMAIN_VERSION,
        CROSS_DOMAIN_PREVIOUS,
        CROSS_DOMAIN_EARLIER,
        CROSS_DOMAIN_CONCEPT,
        CROSS_DOMAIN_PAPER,
        "papers/README.md",
        "Future-Splitting State Recruitment",
        "Layer Before Law",
        "Recursive Constraint Closure",
        "Cross-Domain Compositional Schema",
        "Bell Constraints as Typed Boundaries",
    ],
    "DISCOVERY_KEYWORDS.md": [
        VOYNICH_CURRENT,
        VOYNICH_VERSION,
        VOYNICH_CONCEPT,
        VOYNICH_CURRENT_PAPER,
        ATLD_VERSION,
        LAYER_BEFORE_LAW_VERSION,
        RCC_VERSION,
        AAF_VERSION,
        AAF_CONCEPT,
        FSSR_VERSION,
        FSSR_CONCEPT,
        BELL_VERSION,
        BELL_CONCEPT,
        CROSS_DOMAIN_VERSION,
        CROSS_DOMAIN_PREVIOUS,
        CROSS_DOMAIN_EARLIER,
        CROSS_DOMAIN_CONCEPT,
        CROSS_DOMAIN_PAPER,
        CROSS_DOMAIN_MODULE,
        CROSS_DOMAIN_BELL_MODULE,
        "Future-Splitting State Recruitment",
        "FSSR",
        FSSR_MODULE,
        "Addressing State Flow",
        "Cross-Domain Compositional Schema",
        "exact relation ablation",
        "Bell Constraints as Typed Boundaries",
    ],
    "PROVENANCE_DOI_AND_ATTRIBUTION.md": [
        MKUFT_VERSION,
        MKUFT_CONCEPT,
        MKUFT_HISTORICAL,
        VOYNICH_CURRENT,
        VOYNICH_VERSION,
        VOYNICH_CONCEPT,
        VOYNICH_CURRENT_PAPER,
        ATLD_VERSION,
        ATLD_CONCEPT,
        LAYER_BEFORE_LAW_VERSION,
        RCC_VERSION,
        AAF_VERSION,
        AAF_CONCEPT,
        FSSR_VERSION,
        FSSR_CONCEPT,
        BELL_VERSION,
        BELL_CONCEPT,
        CROSS_DOMAIN_VERSION,
        CROSS_DOMAIN_PREVIOUS,
        CROSS_DOMAIN_EARLIER,
        CROSS_DOMAIN_CONCEPT,
        CROSS_DOMAIN_PAPER,
        CROSS_DOMAIN_MD5,
        CROSS_DOMAIN_SHA256,
        "CROSS_DOMAIN_COMPOSITIONAL_SCHEMA_STANDALONE_PUBLICATION.md",
        "BELL_CONSTRAINTS_STANDALONE_PUBLICATION.md",
        "FSSR_STANDALONE_PUBLICATION.md",
        f"docs/{FSSR_MODULE}",
        "VOYNICH_STANDALONE_PUBLICATION.md",
        "papers/README.md",
        "publications/MKUFT_RELATIONAL_ARCHITECTURE_v2_DOI_10.5281_zenodo.21973064.pdf",
        "publications/HISTORICAL_V1_MKUFT_FALSIFICATIONS_DOI_10.5281_zenodo.17780566.pdf",
        "publications/HISTORICAL_V1_MKUFT_MATH_APPENDIX_DOI_10.5281_zenodo.17780566.pdf",
        "publications/FUTURE_SPLITTING_STATE_RECRUITMENT_v1.0_DOI_10.5281_zenodo.22058303.pdf",
        "publications/ADDRESSED_ADMISSIBLE_FUTURES_v0.1_DOI_10.5281_zenodo.22031333.pdf",
        "publications/LAYER_BEFORE_LAW_v1.0_DOI_10.5281_zenodo.21971270.pdf",
        "publications/RECURSIVE_CONSTRAINT_CLOSURE_v0.1_DOI_10.5281_zenodo.21971425.pdf",
        "publications/ATLD_EVALUATION_PROTOCOL_v1.0_DOI_10.5281_zenodo.21341521.pdf",
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
    f"papers/{VOYNICH_CURRENT_PAPER}": [
        VOYNICH_CURRENT,
        VOYNICH_VERSION,
        VOYNICH_CONCEPT,
        "Candidate Procedural-Executable Information System",
        "Addressing",
        "State",
        "Flow",
        "VOYNICH_STANDALONE_PUBLICATION.md",
        "docs/07_ESRT_ESF_AND_VOYNICH_SUPPORT.md",
        "docs/09_VOYNICH_PROCEDURAL_ENGINE.md",
        "docs/10_ESRT_ESF_METHOD_APPENDIX.md",
        "dd0d6a7176da51ce69b9466408df4c39",
        "367f961ef33961ade02e19ac3e440844606dc6fc250b269d59951d366540fcff",
    ],
    "VOYNICH_STANDALONE_PUBLICATION.md": [
        VOYNICH_CURRENT,
        VOYNICH_VERSION,
        VOYNICH_CONCEPT,
        VOYNICH_CURRENT_PAPER,
        "430,789",
        "dd0d6a7176da51ce69b9466408df4c39",
        "367f961ef33961ade02e19ac3e440844606dc6fc250b269d59951d366540fcff",
    ],
    "docs/07_ESRT_ESF_AND_VOYNICH_SUPPORT.md": [
        VOYNICH_CURRENT,
        VOYNICH_VERSION,
        VOYNICH_CONCEPT,
        VOYNICH_CURRENT_PAPER,
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
        "Future-Splitting State Recruitment",
        "state-recruitment event",
        "33S6",
    ],
    "BELL_CONSTRAINTS_STANDALONE_PUBLICATION.md": [
        BELL_VERSION,
        BELL_CONCEPT,
        BELL_PAPER,
        "CC BY 4.0",
    ],
    f"papers/{BELL_PAPER}": [
        BELL_VERSION,
        BELL_CONCEPT,
        "Bell Constraints as Typed Boundaries",
    ],
    "CROSS_DOMAIN_COMPOSITIONAL_SCHEMA_STANDALONE_PUBLICATION.md": [
        CROSS_DOMAIN_VERSION,
        CROSS_DOMAIN_PREVIOUS,
        CROSS_DOMAIN_EARLIER,
        CROSS_DOMAIN_CONCEPT,
        CROSS_DOMAIN_PAPER,
        CROSS_DOMAIN_MD5,
        CROSS_DOMAIN_SHA256,
        CROSS_DOMAIN_MODULE,
        CROSS_DOMAIN_BELL_MODULE,
        "CC BY 4.0",
    ],
    f"papers/{CROSS_DOMAIN_PAPER}": [
        CROSS_DOMAIN_VERSION,
        CROSS_DOMAIN_PREVIOUS,
        "Cross-Domain Compositional Schema",
        CROSS_DOMAIN_MODULE,
        CROSS_DOMAIN_BELL_MODULE,
        "no new Bell inequality",
    ],
    f"docs/{CROSS_DOMAIN_MODULE}": [
        CROSS_DOMAIN_VERSION,
        CROSS_DOMAIN_PREVIOUS,
        "Cross-Domain Compositional Schema",
        "\\mathrm{Eval}",
        "\\mathrm{LB}",
    ],
    f"docs/{CROSS_DOMAIN_BELL_MODULE}": [
        CROSS_DOMAIN_VERSION,
        CROSS_DOMAIN_PREVIOUS,
        BELL_VERSION,
        "valid quantum-correlator points",
        "TETRAHEDRAL PRIVILEGE REJECTED",
    ],
    "publications/CROSS_DOMAIN_COMPOSITIONAL_SCHEMA_v0.4/README.md": [
        CROSS_DOMAIN_VERSION,
        CROSS_DOMAIN_PREVIOUS,
        CROSS_DOMAIN_CONCEPT,
        CROSS_DOMAIN_MD5,
        CROSS_DOMAIN_SHA256,
        "394810",
        "31",
    ],
    "publications/README.md": [
        VOYNICH_VERSION,
        ATLD_VERSION,
        FSSR_VERSION,
        FSSR_CONCEPT,
        FSSR_PAPER,
        FSSR_MODULE,
        BELL_VERSION,
        BELL_CONCEPT,
        CROSS_DOMAIN_VERSION,
        CROSS_DOMAIN_PREVIOUS,
        CROSS_DOMAIN_MD5,
        CROSS_DOMAIN_PAPER,
        "CROSS_DOMAIN_COMPOSITIONAL_SCHEMA_STANDALONE_PUBLICATION.md",
        "BELL_CONSTRAINTS_STANDALONE_PUBLICATION.md",
        "Layer Before Law",
        "Recursive Constraint Closure",
        "MKUFT_RELATIONAL_ARCHITECTURE_v2_DOI_10.5281_zenodo.21973064.pdf",
        "HISTORICAL_V1_MKUFT_FALSIFICATIONS_DOI_10.5281_zenodo.17780566.pdf",
        "HISTORICAL_V1_MKUFT_MATH_APPENDIX_DOI_10.5281_zenodo.17780566.pdf",
        "FUTURE_SPLITTING_STATE_RECRUITMENT_v1.0_DOI_10.5281_zenodo.22058303.pdf",
        "ADDRESSED_ADMISSIBLE_FUTURES_v0.1_DOI_10.5281_zenodo.22031333.pdf",
        "LAYER_BEFORE_LAW_v1.0_DOI_10.5281_zenodo.21971270.pdf",
        "RECURSIVE_CONSTRAINT_CLOSURE_v0.1_DOI_10.5281_zenodo.21971425.pdf",
        "ATLD_EVALUATION_PROTOCOL_v1.0_DOI_10.5281_zenodo.21341521.pdf",
        "deposited/public Voynich publication object is DOCX",
    ],
    "papers/2026-08-15_RECURSIVE_CONSTRAINT_CLOSURE_AND_REACHABLE_STATE_GEOMETRY_PREPRINT.md": [
        RCC_VERSION,
        "Recursive Constraint Closure",
        "Published standalone Zenodo paper",
        "RECURSIVE_CONSTRAINT_CLOSURE_STANDALONE_PUBLICATION.md",
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
    "docs/25_LOAD_BEARING_INVARIANTS_AND_WHOLE_SYSTEM_DEFORMATION.md": [
        CROSS_DOMAIN_VERSION,
        "Protocol-relative exact relation ablation",
        "\\mathrm{LB}_F",
        "33S7A_FUTURE_SUFFICIENT_ADDRESS_INVARIANT_AND_LAYER_BEFORE_LAW_PRECEDENCE.md",
    ],
    "docs/32S3_RELATIONAL_BRACKETS_COMPLETION_GEOMETRY_AND_I_TO_P_ADMISSIBILITY.md": [
        CROSS_DOMAIN_VERSION,
        "Parent completion and native-owner custody",
        "native parent constraints",
        "33S7A_FUTURE_SUFFICIENT_ADDRESS_INVARIANT_AND_LAYER_BEFORE_LAW_PRECEDENCE.md",
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
            VOYNICH_CURRENT,
            VOYNICH_CONCEPT,
            VOYNICH_VERSION,
            ATLD_VERSION,
            BELL_VERSION,
            BELL_CONCEPT,
            CROSS_DOMAIN_VERSION,
            CROSS_DOMAIN_PREVIOUS,
        ):
            url = f"https://doi.org/{doi}"
            if url not in citations:
                failures.append(f"codemeta.json: missing citation {url}")
        subjects = set(codemeta.get("subjectOf", []))
        current_voynich_url = f"https://github.com/mark45cdo-mkuft/MKUFT/blob/main/papers/{VOYNICH_CURRENT_PAPER}"
        current_cross_domain_url = f"https://github.com/mark45cdo-mkuft/MKUFT/blob/main/papers/{CROSS_DOMAIN_PAPER}"
        current_bell_url = f"https://github.com/mark45cdo-mkuft/MKUFT/blob/main/papers/{BELL_PAPER}"
        if current_voynich_url not in subjects:
            failures.append("codemeta.json: current Voynich v2 paper route missing")
        if current_cross_domain_url not in subjects:
            failures.append("codemeta.json: current Cross-Domain v0.3 paper route missing")
        if current_bell_url not in subjects:
            failures.append("codemeta.json: Bell v1.0 paper route missing")
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

    for rel in FROZEN_PDF_MIRRORS:
        path = ROOT / rel
        if not path.exists():
            failures.append(f"missing frozen DOI PDF mirror: {rel}")
            continue
        if path.stat().st_size <= 5:
            failures.append(f"empty or truncated frozen DOI PDF mirror: {rel}")
            continue
        if path.read_bytes()[:5] != b"%PDF-":
            failures.append(f"frozen DOI mirror is not a PDF carrier: {rel}")

    historical_voynich = (ROOT / "papers/2026-05-20_VOYNICH_MANUSCRIPT_SYSTEMS_ENGINE_FRAMEWORK.md").read_text(encoding="utf-8")
    if VOYNICH_CURRENT in historical_voynich:
        failures.append("historical Voynich reading edition was silently rewritten with current v2 DOI")

    if not (ROOT / "docs/33_SIPO_CAPSTONE_CONSTRAINT_CONDITIONED_ADDRESSED_UPDATE_LAW.md").exists():
        failures.append("missing live SIPO capstone module")
    if not (ROOT / f"docs/{FSSR_MODULE}").exists():
        failures.append("missing live FSSR Module 33S7")
    if not (ROOT / f"docs/{CROSS_DOMAIN_MODULE}").exists():
        failures.append("missing live Cross-Domain future-sufficiency fold Module 33S7A")
    if not (ROOT / f"docs/{CROSS_DOMAIN_BELL_MODULE}").exists():
        failures.append("missing live Cross-Domain Bell calibration Module 28A")
    if (ROOT / "papers/33_SIPO_CAPSTONE_CONSTRAINT_CONDITIONED_ADDRESSED_UPDATE_LAW.md").exists():
        failures.append("SIPO capstone has been silently promoted into papers without an explicit publication object")

    temp_workflows = sorted((ROOT / ".github" / "workflows").glob("_temp_*.yml"))
    if temp_workflows:
        failures.append("temporary repair workflows remain: " + ", ".join(str(p.relative_to(ROOT)) for p in temp_workflows))

    one_shot = ROOT / ".github" / "workflows" / "populate_publication_pdf_mirrors.yml"
    if one_shot.exists():
        failures.append("one-shot PDF mirror carrier remains after closure")

    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        return 1

    print("PASS: publication routes, DOI custody, Bell/Cross-Domain folds, historical/current version lineages, deposited PDF mirrors, discovery metadata, rights routing, and module/paper boundaries are intact.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
