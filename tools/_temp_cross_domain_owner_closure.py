#!/usr/bin/env python3
from pathlib import Path

CROSS_DOMAIN_CURRENT = "10.5281/zenodo.22166005"

# Module 25 owns deformation semantics, not the future-sufficiency controller.
p25 = Path("docs/25_LOAD_BEARING_INVARIANTS_AND_WHOLE_SYSTEM_DEFORMATION.md")
text = p25.read_text(encoding="utf-8")
header_anchor = "**Citation and provenance:** [PROVENANCE_DOI_AND_ATTRIBUTION.md](../PROVENANCE_DOI_AND_ATTRIBUTION.md)\n"
header_add = "**Compositional-interface calibration:** [Cross-Domain Compositional Schema v0.3](../CROSS_DOMAIN_COMPOSITIONAL_SCHEMA_STANDALONE_PUBLICATION.md), DOI `10.5281/zenodo.22166005`; future-sufficiency ownership remains in [33S7A](33S7A_FUTURE_SUFFICIENT_ADDRESS_INVARIANT_AND_LAYER_BEFORE_LAW_PRECEDENCE.md).  \n"
if header_add.strip() not in text:
    text = text.replace(header_anchor, header_anchor + header_add, 1)
section25 = r'''### 7.3A Protocol-relative exact relation ablation

The Cross-Domain Compositional Schema v0.3 sharpens a deformation rule that belongs at this module's assay layer: **exact relation ablation is a prospectively declared lawful protocol, not an automatic delete operation and not automatically a physical intervention.**

Let `\mathcal A_r` be the preregistered family of lawful protocols capable of removing, neutralising, substituting, or counterfactually suppressing the exact addressed relation `r` while holding the declared comparison object fixed as far as the domain permits. For a declared future-operation family `F`, the assay returns a three-way state

```math
\mathrm{LB}_F(r;\mathcal G,\mathcal A_r)
\in
\{0,1,?\}.
```

Use the states as follows:

- `1` — at least one prospectively admissible exact-relation protocol produces the preregistered loss of declared evaluation/closure, with restoration returning the declared function under the required control;
- `0` — the prospectively controlling lawful protocol family leaves every declared evaluation equivalent within tolerance;
- `?` — exact ablation is unavailable, the comparison is not lawfully isolable, or prospectively allowed protocols disagree without a preregistered resolution rule.

Unknown is a scientific result. It must not be converted into `0` merely because an exact ablation could not be engineered, and it must not be converted into `1` because a coarse representation edit happened to damage performance.

Where a physical causal claim is intended, the intervention must additionally satisfy the native domain's causal and confounding requirements. A representation-level removal can establish architectural load without by itself establishing a new physical mechanism.

Module 33S7A owns the corresponding preserve/reopen consequence for future-sufficient interfaces. Module 25 owns only the deformation semantics, remove/restore discipline, redundancy controls, and classification burden.

'''
anchor25 = "### 7.4 Temporal maintenance-path deformation\n"
if "### 7.3A Protocol-relative exact relation ablation" not in text:
    text = text.replace(anchor25, section25 + anchor25, 1)
p25.write_text(text, encoding="utf-8")

# Module 32S3 owns local-to-global/parent-completion custody, not a new generic solver.
p32 = Path("docs/32S3_RELATIONAL_BRACKETS_COMPLETION_GEOMETRY_AND_I_TO_P_ADMISSIBILITY.md")
text = p32.read_text(encoding="utf-8")
header_anchor32 = "**Novelty boundary:** [32A — Module 32 Novelty Audit and Contribution Boundary](32A_MODULE_32_NOVELTY_AUDIT_AND_CONTRIBUTION_BOUNDARY.md)  \n"
header_add32 = "**Compositional-interface publication:** [Cross-Domain Compositional Schema v0.3](../CROSS_DOMAIN_COMPOSITIONAL_SCHEMA_STANDALONE_PUBLICATION.md), DOI `10.5281/zenodo.22166005`; preserve/reopen ownership remains in [33S7A](33S7A_FUTURE_SUFFICIENT_ADDRESS_INVARIANT_AND_LAYER_BEFORE_LAW_PRECEDENCE.md).  \n"
if header_add32.strip() not in text:
    text = text.replace(header_anchor32, header_anchor32 + header_add32, 1)
section32 = r'''### 4.3 Parent completion and native-owner custody

Local validity and parent completion are different questions. A set of lower objects may each be valid at its own address while their proposed joint parent has no compatible completion because a shared identity, resource, boundary condition, import, runtime, measurement context, or other relation receives mutually incompatible requirements.

For lower objects `Y_1,\ldots,Y_m` proposed for one parent composition `P`, write schematically

```math
\Omega_P^{\mathrm{comp}}(Y_1,\ldots,Y_m)
=
\left\{
z\in\mathcal Z_P:
\text{the native parent constraints are jointly satisfied}
\right\}.
```

This is an **interface wrapper**, not a replacement for the domain's established global-consistency machinery. Depending on the domain, the native owner may be a constraint solver, minimal-unsatisfiable-subset or diagnosis method, dependency graph, sheaf/local-to-global construction, proof/import checker, configuration resolver, probability model, or another justified completion formalism.

The compositional verdict is bounded:

```text
all lower objects locally admissible
+ parent completion non-empty
→ parent composition remains admissible at this gate

all lower objects locally admissible
+ parent completion empty
→ local validity does not close the parent
→ identify the smallest native conflict/restoration set where the owning method supports it

parent completion not lawfully decidable at the declared resolution
→ WITHHOLD / REOPEN rather than inventing a completion
```

A parent-completion failure does not by itself imply a new higher law, hidden physical mechanism, or failure of every lower object. It says that the proposed composition is not jointly closed under the declared parent relations.

This is the 32S3 owner-side fold of the published Cross-Domain v0.3 local-to-global result. Module 33S7A owns whether a closed lower object may be reused as a future-sufficient interface and when targeted descent is required; 32S3 owns the completion geometry and native local-to-global custody used when that descent reaches a parent-consistency question.

'''
anchor32 = "## 5. Ambiguity, persistence, and temporal mismatch exposure\n"
if "### 4.3 Parent completion and native-owner custody" not in text:
    text = text.replace(anchor32, section32 + anchor32, 1)
p32.write_text(text, encoding="utf-8")

# Reader-facing front door.
readme = Path("README.md")
text = readme.read_text(encoding="utf-8")
science_anchor = "The present architecture earns support where those distinctions produce prospective predictive, interventional, explanatory, or model-selection value beyond the strongest adequate ordinary description."
science_add = "The published *Cross-Domain Compositional Schema* v0.3 (DOI `10.5281/zenodo.22166005`) is folded into that architecture without creating a parallel controller: Module 25 owns protocol-relative exact-relation deformation and remove/restore discipline; 32S3 owns parent-completion/local-to-global custody; 33S7A owns future-sufficient preserve-or-reopen reuse; and 28A owns the Bell/CHSH hostile calibration. The Bell pass remains a methodological calibration with a null new-physics result, while unrestricted tetrahedral privilege is not earned.\n\n"
if science_add.strip() not in text:
    text = text.replace(science_anchor, science_add + science_anchor, 1)
physics_anchor = "17. [Scientific References and Current Literature](SCIENTIFIC_REFERENCES_AND_CURRENT_LITERATURE.md) — primary literature, neighbouring programmes, disputes, and strongest alternatives.\n"
physics_add = "\nSupporting current interface and calibration routes:\n\n- [Future-Sufficient Address Invariant and Layer-Before-Law Precedence](docs/33S7A_FUTURE_SUFFICIENT_ADDRESS_INVARIANT_AND_LAYER_BEFORE_LAW_PRECEDENCE.md) — live future-sufficient compositional-interface owner and published v0.3 fold.\n- [Cross-Domain Compositional Schema Bell/CHSH Calibration](docs/28A_CROSS_DOMAIN_COMPOSITIONAL_SCHEMA_BELL_CHSH_CALIBRATION.md) — hostile known-answer calibration; no new Bell inequality, Tsirelson derivation, or physical mechanism is claimed.\n"
if "Supporting current interface and calibration routes:" not in text:
    text = text.replace(physics_anchor, physics_anchor + physics_add, 1)
readme.write_text(text, encoding="utf-8")

# Canon map: expose 28A as live experimental/calibration owner.
canon = Path("CANON_MAP.md")
text = canon.read_text(encoding="utf-8")
physics_last = "21. [Scientific References and Current Literature](SCIENTIFIC_REFERENCES_AND_CURRENT_LITERATURE.md)\n"
physics_28a = "22. [Cross-Domain Compositional Schema Bell/CHSH Calibration](docs/28A_CROSS_DOMAIN_COMPOSITIONAL_SCHEMA_BELL_CHSH_CALIBRATION.md)\n"
if physics_28a.strip() not in text:
    text = text.replace(physics_last, physics_last + physics_28a, 1)
canon_anchor = "- **28 — Discriminating Experiments and Promotion Gates:** evidence tiers and promotion rules.\n"
canon_28a = "- **28A — Cross-Domain Compositional Schema Bell/CHSH Calibration:** hostile known-answer calibration of target-relative preserve/refine/reopen/refuse behaviour; physical Phase-0 delta remains null.\n"
if canon_28a.strip() not in text:
    text = text.replace(canon_anchor, canon_anchor + canon_28a, 1)
canon.write_text(text, encoding="utf-8")

# Regression guard for actual four-owner wiring and front-door routes.
checker = Path("tools/check_publication_routes.py")
text = checker.read_text(encoding="utf-8")
old_canon = '''    "CANON_MAP.md": [
        FSSR_VERSION,
        FSSR_MODULE,
        "Future-Splitting State Recruitment",
        "33S4–33S7",
    ],'''
new_canon = '''    "CANON_MAP.md": [
        FSSR_VERSION,
        FSSR_MODULE,
        "Future-Splitting State Recruitment",
        "33S4–33S7",
        CROSS_DOMAIN_CURRENT,
        "28A_CROSS_DOMAIN_COMPOSITIONAL_SCHEMA_BELL_CHSH_CALIBRATION.md",
        "Cross-Domain Compositional Schema Bell/CHSH Calibration",
    ],'''
if old_canon in text:
    text = text.replace(old_canon, new_canon, 1)
insert_anchor = '    "RENDERING_AND_PUBLICATION_INTEGRITY.md": [\n'
owner_checks = '''    "docs/25_LOAD_BEARING_INVARIANTS_AND_WHOLE_SYSTEM_DEFORMATION.md": [
        CROSS_DOMAIN_CURRENT,
        "Protocol-relative exact relation ablation",
        "\\\\mathrm{LB}_F",
        "33S7A_FUTURE_SUFFICIENT_ADDRESS_INVARIANT_AND_LAYER_BEFORE_LAW_PRECEDENCE.md",
    ],
    "docs/32S3_RELATIONAL_BRACKETS_COMPLETION_GEOMETRY_AND_I_TO_P_ADMISSIBILITY.md": [
        CROSS_DOMAIN_CURRENT,
        "Parent completion and native-owner custody",
        "native parent constraints",
        "33S7A_FUTURE_SUFFICIENT_ADDRESS_INVARIANT_AND_LAYER_BEFORE_LAW_PRECEDENCE.md",
    ],
'''
if '"docs/25_LOAD_BEARING_INVARIANTS_AND_WHOLE_SYSTEM_DEFORMATION.md": [' not in text:
    text = text.replace(insert_anchor, owner_checks + insert_anchor, 1)
old_readme_tail = '''        "Recursive Constraint Closure",
        "Layer Before Law",
    ],
    "INDEX.md": ['''
new_readme_tail = '''        "Recursive Constraint Closure",
        "Layer Before Law",
        CROSS_DOMAIN_CURRENT,
        "docs/28A_CROSS_DOMAIN_COMPOSITIONAL_SCHEMA_BELL_CHSH_CALIBRATION.md",
        "docs/33S7A_FUTURE_SUFFICIENT_ADDRESS_INVARIANT_AND_LAYER_BEFORE_LAW_PRECEDENCE.md",
        "protocol-relative exact-relation deformation",
    ],
    "INDEX.md": ['''
if '"protocol-relative exact-relation deformation"' not in text:
    text = text.replace(old_readme_tail, new_readme_tail, 1)
checker.write_text(text, encoding="utf-8")
