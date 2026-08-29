from pathlib import Path
import json

DOI_NEW = "10.5281/zenodo.22166468"
DOI_V03 = "10.5281/zenodo.22166005"
DOI_V02 = "10.5281/zenodo.22164562"
DOI_CONCEPT = "10.5281/zenodo.22164561"
MD5 = "d5a56561e82ca5d64a8766ca8122a956"
SHA256 = "bcb5c7618962bac98c2ae0ad097f7bba8e9758d4c86879b6546d037736c73b83"
PDF_BYTES = "394,810"
PAGES = "31"
TITLE = "Cross-Domain Compositional Schema: Future-Sufficient Interfaces, Load-Bearing Relations, and Preserve-or-Reopen Reuse"

TOKENS = {
    "__DOI_NEW__": DOI_NEW,
    "__DOI_V03__": DOI_V03,
    "__DOI_V02__": DOI_V02,
    "__DOI_CONCEPT__": DOI_CONCEPT,
    "__MD5__": MD5,
    "__SHA256__": SHA256,
    "__PDF_BYTES__": PDF_BYTES,
    "__PAGES__": PAGES,
    "__TITLE__": TITLE,
}


def tpl(s):
    for k, v in TOKENS.items():
        s = s.replace(k, v)
    return s


def read(path):
    return Path(path).read_text(encoding="utf-8")


def write(path, content):
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding="utf-8")


def append_once(path, key, block):
    s = read(path)
    if key not in s:
        write(path, s.rstrip() + "\n\n" + block.strip() + "\n")


# ---------------------------------------------------------------------------
# Frozen publication custody
# ---------------------------------------------------------------------------
write("CROSS_DOMAIN_COMPOSITIONAL_SCHEMA_STANDALONE_PUBLICATION.md", tpl(r'''# Cross-Domain Compositional Schema — Publication Record

**Author:** Mark Charles McLaughlin  
**ORCID:** `0009-0005-7736-1511`  
**Current title:** *__TITLE__*  
**Current version:** 0.4  
**Publication date:** 29 August 2026  
**Current version DOI:** `__DOI_NEW__`  
**Prior version DOI (v0.3):** `__DOI_V03__`  
**Earlier version DOI (v0.2):** `__DOI_V02__`  
**Zenodo concept DOI:** `__DOI_CONCEPT__`  
**Licence of exact v0.4 deposit:** Creative Commons Attribution 4.0 International (CC BY 4.0)  
**Publication type:** Preprint  
**Access:** Open

## Public routes

- [Zenodo v0.4 publication](https://doi.org/__DOI_NEW__)
- [GitHub reader/citation route](papers/2026-08-29_CROSS_DOMAIN_COMPOSITIONAL_SCHEMA_v0.4.md)
- [Frozen carrier identity record](publications/CROSS_DOMAIN_COMPOSITIONAL_SCHEMA_v0.4/README.md)
- [Prior GitHub v0.3 reader route](papers/2026-08-29_CROSS_DOMAIN_COMPOSITIONAL_SCHEMA_v0.3.md)
- [Canonical live future-sufficiency owner — Module 33S7A](docs/33S7A_FUTURE_SUFFICIENT_ADDRESS_INVARIANT_AND_LAYER_BEFORE_LAW_PRECEDENCE.md)
- [Bell/tetrahedral formalisation owner — Module 28A](docs/28A_CROSS_DOMAIN_COMPOSITIONAL_SCHEMA_BELL_CHSH_CALIBRATION.md)
- [Bell correspondence publication](papers/2026-08-25_BELL_CONSTRAINTS_TYPED_BOUNDARIES_v1.0.md)

## Version custody

Version 0.4 is the substantive successor to v0.3 in the same Zenodo version lineage. The concept DOI `__DOI_CONCEPT__` identifies the version family and resolves to the latest version; the version-specific DOI `__DOI_NEW__` identifies the frozen v0.4 object. The v0.3 and v0.2 DOIs remain immutable historical versions.

The exact Zenodo v0.4 PDF is the controlling frozen publication carrier. Live GitHub modules may integrate or sharpen the result but do not silently alter the deposited object.

## Exact v0.4 carrier identity

**Zenodo filename:** `Cross-Domain_Compositional_Schema_v0.4_2026-08-29.pdf`  
**Pages:** __PAGES__  
**Bytes:** __PDF_BYTES__  
**MD5:** `__MD5__`  
**SHA-256:** `__SHA256__`

The MD5 and byte count identify the receiver-side publication carrier; the SHA-256 identifies the audited release carrier used for the coupled red-team fixed-point pass.

## Scientific fold boundary

Version 0.4 retains the v0.3 typed compositional interface contract and closes the previously open Bell/tetrahedral branch at an exact mathematical fixed point. It adds explicit operator/sign-to-target semantic attachment, distinguishes a four-context indexing simplex from Bell-native CHSH tetrahedral facets, and defines the exact Facet-adapted Tetrahedral Bell Chart (TBC):

```math
E=V\lambda+\frac{\nu}{4}c,
\qquad
\mathbf 1^{\mathsf T}\lambda=1,
\qquad
\nu=c^{\mathsf T}E-2.
```

The tetrahedral facet carries three independent affine coordinates and `nu` supplies the fourth correlator degree of freedom. The chart is exact for the declared four-correlator object but does not close full Bell behaviour because marginal information remains in the fibre of `P -> E`.

The natural four-dimensional simplex volume satisfies

```math
\mathcal V_c(E)=\frac{|S_c(E)-2|}{3},
```

so the immediate geometric-invariant candidate collapses to known CHSH excess. Because TBC is an invertible reparameterisation, the chart alone cannot constitute new physics. The physical result remains **NULL** after native-owner subtraction: no new Bell inequality, no independent Tsirelson boundary, no new quantum mechanism, and no measurable physical residual are claimed.

## Live ownership

- **33S7A** owns future-sufficient preserve-or-guaranteed-reopen semantics and operator-to-target address consequences.
- **28A** owns the Bell/CHSH/tetrahedral worked formalisation and its null physical verdict.
- **25** owns protocol-relative deformation and the reparameterisation/representation-control lesson.
- **32S3** owns completion/fibre/local-to-global custody; the Bell marginal fibre is a calibration of that existing owner, not a new completion controller.
- **29 / research SOP** retain promotion and claim-discipline authority.

## Citation

> McLaughlin, Mark Charles. (2026). *__TITLE__*. Version 0.4. Zenodo. DOI: __DOI_NEW__.

## Object boundary

The publication record owns DOI/version/citation/licence and frozen-carrier identity. The `papers/` route owns reader discovery. Modules 33S7A, 28A, 25 and 32S3 are evolving live-canon integrations. Zenodo remains publication custody. None of these objects silently replaces another.
'''))

write("papers/2026-08-29_CROSS_DOMAIN_COMPOSITIONAL_SCHEMA_v0.4.md", tpl(r'''# __TITLE__

**Author:** Mark Charles McLaughlin  
**ORCID:** 0009-0005-7736-1511  
**Version:** 0.4 preprint  
**Published:** 29 August 2026  
**Version DOI:** [__DOI_NEW__](https://doi.org/__DOI_NEW__)  
**Prior version DOI (v0.3):** [__DOI_V03__](https://doi.org/__DOI_V03__)  
**Concept DOI:** [__DOI_CONCEPT__](https://doi.org/__DOI_CONCEPT__)  
**Licence:** CC BY 4.0

## Publication boundary

This reader route describes the frozen Zenodo v0.4 publication. It is not a replacement for the deposited PDF and does not promote later live-module edits into the publication.

Version 0.4 carries the previously open tetrahedral/Bell branch through exact semantics and geometry. The four Bell contexts form an abstract indexing simplex whose Boolean face lattice records exposed context-labelled quantities. A CHSH sign section attaches coefficients to exact contexts and selects a Bell functional/facet orientation. Separately, Bell-native geometry supplies genuine three-dimensional tetrahedral CHSH facets inside the four-dimensional local correlator polytope.

For a selected CHSH orientation `c`, let `V` contain the four local deterministic vertices saturating `c^T E=2`. Define

```math
\nu=c^{\mathsf T}E-2,
\qquad
\Pi_c(E)=E-\frac{\nu}{4}c,
\qquad
\lambda=V^{-1}\Pi_c(E).
```

Then the exact Facet-adapted Tetrahedral Bell Chart is

```math
\boxed{
E=V\lambda+\frac{\nu}{4}c,
\qquad
\mathbf1^{\mathsf T}\lambda=1.
}
```

The tetrahedral base carries three independent affine coordinates and `nu` carries the fourth. On the local CHSH facet, `nu=0` and the coordinates are ordinary non-negative barycentric weights. Off the facet, the chart remains invertible while the projected coordinates need not remain inside the simplex.

The paper then applies native Bell/Fine/no-signalling/Tsirelson-Landau-Masanes constraints. TBC coordinates do not close full Bell behaviours because local marginals remain in the fibre of `P -> E`. The natural four-dimensional simplex volume generated by the CHSH facet and an off-facet point obeys

```math
\boxed{
\mathcal V_c(E)=\frac{|S_c(E)-2|}{3}.
}
```

That candidate collapses to a rescaling of known CHSH excess rather than defining an independent physical invariant. Because TBC is an invertible reparameterisation, the chart alone cannot be new physics. The v0.4 physical residual is **NULL**: no new Bell inequality, independent Tsirelson derivation, quantum mechanism, or measurable physical delta survives the native-owner squeeze.

## Live MKUFT owners

- [33S7A — Future-Sufficient Address Invariant and Layer-Before-Law Precedence](../docs/33S7A_FUTURE_SUFFICIENT_ADDRESS_INVARIANT_AND_LAYER_BEFORE_LAW_PRECEDENCE.md)
- [28A — Cross-Domain Compositional Schema Bell/CHSH Calibration](../docs/28A_CROSS_DOMAIN_COMPOSITIONAL_SCHEMA_BELL_CHSH_CALIBRATION.md)
- [25 — Load-Bearing Invariants and Whole-System Deformation](../docs/25_LOAD_BEARING_INVARIANTS_AND_WHOLE_SYSTEM_DEFORMATION.md)
- [32S3 — Relational Brackets, Completion Geometry, and I→P Admissibility](../docs/32S3_RELATIONAL_BRACKETS_COMPLETION_GEOMETRY_AND_I_TO_P_ADMISSIBILITY.md)

## Frozen carrier identity

See [the v0.4 identity record](../publications/CROSS_DOMAIN_COMPOSITIONAL_SCHEMA_v0.4/README.md).
'''))

write("publications/CROSS_DOMAIN_COMPOSITIONAL_SCHEMA_v0.4/README.md", tpl(r'''# Cross-Domain Compositional Schema v0.4 — frozen carrier identity

**Title:** __TITLE__  
**Version:** 0.4  
**Published:** 29 August 2026  
**Version DOI:** `__DOI_NEW__`  
**Prior version DOI:** `__DOI_V03__`  
**Concept DOI:** `__DOI_CONCEPT__`  
**Licence:** CC BY 4.0

## Exact carrier

- filename: `Cross-Domain_Compositional_Schema_v0.4_2026-08-29.pdf`
- pages: __PAGES__
- bytes: 394810
- MD5: `__MD5__`
- SHA-256: `__SHA256__`

The PDF itself is deposited at Zenodo under the version-specific DOI. This repository record preserves receiver-side identity witnesses and routes to live integrations without pretending that evolving Markdown modules are byte-equivalent to the frozen publication.

## Science boundary

The publication closes the tetrahedral Bell branch at the level of exact coordinate semantics and established Bell geometry. Its TBC is an invertible reparameterisation, and the natural four-volume collapses to CHSH excess. No independent new Bell law or physical mechanism is claimed.
'''))
write("publications/CROSS_DOMAIN_COMPOSITIONAL_SCHEMA_v0.4/SHA256SUMS.txt", SHA256 + "  Cross-Domain_Compositional_Schema_v0.4_2026-08-29.pdf\n")

# ---------------------------------------------------------------------------
# Live science owners
# ---------------------------------------------------------------------------
path = "docs/28A_CROSS_DOMAIN_COMPOSITIONAL_SCHEMA_BELL_CHSH_CALIBRATION.md"
s = read(path)
s = s.replace("**Compositional-schema publication:** *Cross-Domain Compositional Schema: Future-Sufficient Interfaces, Load-Bearing Relations, and Preserve-or-Reopen Reuse*, v0.3, DOI `10.5281/zenodo.22166005`; previous v0.2 DOI `10.5281/zenodo.22164562`",
              "**Compositional-schema publication:** *" + TITLE + "*, v0.4, DOI `" + DOI_NEW + "`; prior v0.3 DOI `" + DOI_V03 + "`; earlier v0.2 DOI `" + DOI_V02 + "`")
s = s.replace("**Publication record:** [Cross-Domain Compositional Schema v0.3](../CROSS_DOMAIN_COMPOSITIONAL_SCHEMA_STANDALONE_PUBLICATION.md)",
              "**Publication record:** [Cross-Domain Compositional Schema v0.4](../CROSS_DOMAIN_COMPOSITIONAL_SCHEMA_STANDALONE_PUBLICATION.md)")
s = s.replace("**Status:** public methodological calibration protocol with an executed analytic Phase-0 known-answer calibration dated 29 August 2026, now reported in the published Cross-Domain Compositional Schema v0.3. It reports no new Bell inequality, no independent derivation of Tsirelson's bound, and no new physical mechanism.",
              "**Status:** public Bell/CHSH calibration and exact tetrahedral-formalisation owner. Phase 0 is retained as the v0.3 known-answer calibration; the published v0.4 continuation closes the tetrahedral branch at an exact facet-plus-normal coordinate fixed point. It reports no new Bell inequality, no independent derivation of Tsirelson's bound, no new quantum mechanism, and no surviving measurable physical residual.")
v04_block = r'''

## 14. Published v0.4 tetrahedral formalisation and fixed point — 29 August 2026

Version 0.4 reopens the v0.3 dimensional obstruction as a derivation problem. The result is split into two different tetrahedral objects so that index semantics, local deterministic mixtures, and correlator geometry are not merged merely because each construction has four visible elements.

### 14.1 Context indexing simplex and attached CHSH semantics

Let the four Bell contexts be

```math
\mathcal C=\{00,01,10,11\}.
```

Treating these labels as vertices of an abstract 3-simplex is an indexing device only. Its face/restriction lattice is the Boolean lattice

```math
\mathcal L_{\mathcal C}=2^{\mathcal C},
```

which records which context-labelled quantities remain exposed under a compression/restriction. It is not a physical spacetime or causal lattice.

A CHSH orientation is an attached sign section

```math
\sigma:\mathcal C\rightarrow\{-1,+1\},
```

with odd parity. It induces a coefficient vector `c_sigma` and Bell functional

```math
S_\sigma(E)=c_\sigma^{\mathsf T}E.
```

The attachment of each sign to its exact measurement context is load-bearing: erasing the attachment while retaining only the sign inventory collapses distinct CHSH facet selectors. This is the Bell-native instance of the general operator-to-target semantic-address rule.

### 14.2 Bell-native tetrahedron

The local correlator polytope is

```math
\mathcal L_E=\mathrm{conv}\{E\in\{-1,+1\}^4:E_{00}E_{01}E_{10}E_{11}=1\}.
```

It is full-dimensional in `R^4` with eight local correlator vertices and sixteen tetrahedral facets: eight coordinate/E-type facets and eight CHSH-type facets. For the standard orientation

```math
c=(1,1,1,-1)^{\mathsf T},
```

the CHSH facet is `c^T E=2`. Choose the four saturating local vertices

```math
v_1=(-1,1,1,-1)^{\mathsf T},
\quad
v_2=(1,-1,1,-1)^{\mathsf T},
```

```math
v_3=(1,1,-1,-1)^{\mathsf T},
\quad
v_4=(1,1,1,1)^{\mathsf T}.
```

With these columns in `V`, `det V=16`; the facet is a regular tetrahedron in its three-dimensional affine hyperplane, with Euclidean 3-volume `8/3` in the standard correlator embedding.

### 14.3 Facet-adapted Tetrahedral Bell Chart

Define

```math
\nu_c(E)=c^{\mathsf T}E-2,
\qquad
\Pi_c(E)=E-\frac{\nu_c(E)}{4}c,
\qquad
\lambda_c(E)=V^{-1}\Pi_c(E).
```

The exact reconstruction is

```math
\boxed{
E=V\lambda+\frac{\nu}{4}c,
\qquad
\mathbf1^{\mathsf T}\lambda=1.
}
```

The constrained codomain is four-dimensional: `lambda` contributes three independent affine coordinates and `nu` contributes the fourth. The map is an affine bijection for the four-correlator object relative to the selected CHSH orientation. On the local facet `nu=0` and non-negative `lambda` are ordinary barycentric weights; away from the facet the chart remains invertible while the projected coordinates need not remain inside the simplex.

Thus the v0.3 four-versus-three objection is preserved, not reversed: **tetrahedron alone is insufficient; tetrahedral facet address plus one transverse coordinate is complete.** Symmetry-equivalent CHSH orientations carry the same construction under Bell relabelling, so no displayed orientation is physically privileged.

### 14.4 Native-boundary pullback and marginal fibre

Along the normal ray through the facet centroid, the chart reproduces the standard ordering

```text
local facet:       S=2,        nu=0
Tsirelson point:   S=2sqrt(2), nu=2(sqrt(2)-1)
PR/algebraic:      S=4,        nu=2
```

without creating a new quantum boundary. The Tsirelson-Landau-Masanes correlator criterion is only pulled back through the invertible chart.

The chart is correlator-level. The projection

```math
\pi_E:P\rightarrow E
```

has a set-theoretic fibre of behaviours sharing the same correlator object. In binary form,

```math
p(a,b\mid x,y)=\frac14\left[1+aA_{xy}+bB_{xy}+ab\left(V\lambda+\frac{\nu}{4}c\right)_{xy}\right].
```

Therefore the TBC closes correlator questions but not general no-signalling/full-behaviour questions without reopening marginal-bearing coordinates. This is the Bell-native calibration of the existing completion/fibre and preserve-or-reopen owners.

### 14.5 Surgical ablation and geometric null

For the symmetric Tsirelson correlator `E_Q=(t,t,t,-t)^T`, `t=1/sqrt(2)`, neutralising only `E_11` changes both the transverse coordinate and the projected tetrahedral address; restoring the addressed correlator restores the original chart state. This remains an object-level comparison between lawful correlator points, not a claim that one experimental correlator can be physically intervened on in isolation.

The natural four-dimensional simplex volume formed by the selected CHSH facet and an off-facet point is

```math
\boxed{
\mathcal V_c(E)=\frac{|\nu_c(E)|}{3}=\frac{|S_c(E)-2|}{3}.
}
```

The immediate geometric invariant candidate therefore collapses exactly to known CHSH excess. It is useful bookkeeping, not an independent Bell quantity.

### 14.6 Reparameterisation null and physics gate

Because the TBC is invertible, coordinate change alone cannot alter any physical prediction whose statistics are merely pulled back or pushed forward through the bijection. A physical promotion would require an additional independently typed law, constraint, or dynamics with a standard/null limit and a prospective measurable discriminator. Version 0.4 supplies no non-zero physical residual of that kind.

### 14.7 v0.4 fixed-point verdict

```text
ordinary tetrahedral point for unrestricted four correlators: REJECTED
Bell-native tetrahedral CHSH facet: ESTABLISHED NATIVE GEOMETRY
facet + transverse coordinate reconstruction: EXACT
sign-to-context attachment: MATHEMATICALLY LOAD-BEARING
context lattice: BOOLEAN ADDRESS/RESTRICTION LATTICE ONLY
full behaviour from TBC alone: NOT CLOSED; MARGINAL FIBRE REOPENS
natural 4-volume novelty: NULL; RESCALED CHSH EXCESS
new Bell inequality / new Tsirelson boundary / new mechanism: NULL
```

The surviving result is a facet-adapted coordinate and semantic-address construction on established Bell geometry, not evidence that tetrahedral shape is a universal ontology or new physical law. Phase 1 remains the next methodological burden: freeze the rules and test held-out Bell cases against a strong Bell-native baseline; Phase 2 should transport the same interface rules into a non-CHSH scenario where a four-context tetrahedral convenience is absent.
'''
if "## 14. Published v0.4 tetrahedral formalisation" not in s:
    s = s.rstrip() + v04_block + "\n"
s = s.replace("The result is now part of the frozen Cross-Domain Compositional Schema v0.3 publication. This module remains the live detailed calibration owner: later Phase-1/Phase-2 work, corrected native comparisons, or stronger held-out results must be added here or in an explicitly owned successor and must not be silently backdated into the v0.3 deposit.\n\nThe next scientific burden is Phase 1: freeze the schema and score it on held-out Bell objects against a strong Bell-native baseline. Only a prospective burden/discrimination gain can move the result beyond analytic baseline parity.",
              "The Phase-0 result remains part of the frozen v0.3 publication. The current v0.4 publication reopens that dimensional obstruction and closes the tetrahedral branch through the exact formalisation in Section 14. This module is the live detailed calibration/formalisation owner; later Phase-1/Phase-2 work must not be silently backdated into either frozen deposit.\n\nThe next scientific burden remains Phase 1: freeze the now-complete interface/TBC mapping rules and score held-out Bell objects against a strong Bell-native baseline. Only a prospective burden/discrimination gain or a separately defined non-reparameterisation physical residual can support a stronger promotion.")
write(path, s)

path = "docs/33S7A_FUTURE_SUFFICIENT_ADDRESS_INVARIANT_AND_LAYER_BEFORE_LAW_PRECEDENCE.md"
s = read(path)
s = s.replace("**Compositional-interface publication:** *Cross-Domain Compositional Schema: Future-Sufficient Interfaces, Load-Bearing Relations, and Preserve-or-Reopen Reuse*, v0.3, DOI `10.5281/zenodo.22166005`; previous v0.2 DOI `10.5281/zenodo.22164562`",
              "**Compositional-interface publication:** *" + TITLE + "*, v0.4, DOI `" + DOI_NEW + "`; prior v0.3 DOI `" + DOI_V03 + "`; earlier v0.2 DOI `" + DOI_V02 + "`")
s = s.replace("**Publication record:** [Cross-Domain Compositional Schema v0.3](../CROSS_DOMAIN_COMPOSITIONAL_SCHEMA_STANDALONE_PUBLICATION.md)",
              "**Publication record:** [Cross-Domain Compositional Schema v0.4](../CROSS_DOMAIN_COMPOSITIONAL_SCHEMA_STANDALONE_PUBLICATION.md)")
s = s.replace("**Status:** canonical nomenclature, precedence, and live compositional-interface fold for the future-sufficiency family, updated after publication of Cross-Domain Compositional Schema v0.3. It does not retroactively alter a frozen publication, assert a new mathematical theorem, privilege a simplex/tetrahedron as physical geometry, or claim experimental confirmation of a universal law of nature.",
              "**Status:** canonical nomenclature, precedence, and live compositional-interface fold for the future-sufficiency family, updated through the published Cross-Domain Compositional Schema v0.4. It does not retroactively alter a frozen publication, treat the v0.4 Bell chart as a universal ontology, or promote an invertible representation into a physical mechanism.")
block = r'''

### Published v0.4 Bell-specific closure of the geometry branch

Version 0.4 does not change the general FSAI law; it gives the preserve/reopen rule a stronger Bell-native calibration. Four Bell context labels may be organised as an abstract indexing simplex with Boolean face/restriction lattice `2^C`, but that address object is distinct from the correlator carrier. Separately, each CHSH facet of the local correlator polytope is a genuine three-dimensional tetrahedron inside `R^4`.

For a selected CHSH facet orientation `c`, the published Facet-adapted Tetrahedral Bell Chart uses

```math
\nu=c^{\mathsf T}E-2,
\qquad
\Pi_c(E)=E-\frac{\nu}{4}c,
\qquad
\lambda=V^{-1}\Pi_c(E),
```

with exact reconstruction

```math
E=V\lambda+\frac{\nu}{4}c,
\qquad
\mathbf1^{\mathsf T}\lambda=1.
```

The three-coordinate tetrahedral facet address plus one transverse coordinate closes the four-correlator object exactly, while the same interface does **not** close full Bell behaviour: local marginals remain in the fibre of `P -> E` and must be reopened when a wider operation asks a marginal/no-signalling question.

The deeper FSAI lesson is therefore not “tetrahedra are privileged”. It is:

```text
representation closes declared target exactly
→ PRESERVE at that target

wider target depends on omitted fibre coordinate
→ REOPEN the exact lower owner

invertible reparameterisation changes no native prediction
→ do not promote coordinate structure into new law
```

The natural tetrahedral hypervolume candidate in v0.4 collapses to `|S-2|/3`, so it supplies no independent physical invariant. A geometry can be mathematically exact and operationally useful while remaining physically null after native-owner subtraction.
'''
if "### Published v0.4 Bell-specific closure" not in s:
    marker = "\n## 3. Load-bearing membership and minimum sufficiency"
    if marker not in s:
        raise SystemExit("33S7A insertion marker missing")
    s = s.replace(marker, block + marker, 1)
s = s.replace("published Cross-Domain Compositional Schema v0.3; the live module remains the detailed calibration/reproducibility owner.",
              "published Cross-Domain Compositional Schema v0.4; Module 28A remains the detailed Bell/tetrahedral calibration and reproducibility owner.")
write(path, s)

path = "docs/25_LOAD_BEARING_INVARIANTS_AND_WHOLE_SYSTEM_DEFORMATION.md"
s = read(path)
s = s.replace("**Compositional-interface calibration:** [Cross-Domain Compositional Schema v0.3](../CROSS_DOMAIN_COMPOSITIONAL_SCHEMA_STANDALONE_PUBLICATION.md), DOI `10.5281/zenodo.22166005`; future-sufficiency ownership remains in [33S7A](33S7A_FUTURE_SUFFICIENT_ADDRESS_INVARIANT_AND_LAYER_BEFORE_LAW_PRECEDENCE.md).",
              "**Compositional-interface calibration:** [Cross-Domain Compositional Schema v0.4](../CROSS_DOMAIN_COMPOSITIONAL_SCHEMA_STANDALONE_PUBLICATION.md), DOI `" + DOI_NEW + "`; future-sufficiency ownership remains in [33S7A](33S7A_FUTURE_SUFFICIENT_ADDRESS_INVARIANT_AND_LAYER_BEFORE_LAW_PRECEDENCE.md), with the Bell/tetrahedral worked owner in [28A](28A_CROSS_DOMAIN_COMPOSITIONAL_SCHEMA_BELL_CHSH_CALIBRATION.md).")
block = r'''

### 7.3B Reparameterisation-control deformation

The published Cross-Domain v0.4 Bell continuation adds a specific null control to the deformation family. A candidate geometry may survive exact ablation and reconstruction yet still be only a change of coordinates. Where a proposed representation `Phi` is bijective on the tested object, compare every claimed prediction, admissibility decision, and statistic under `Phi` and `Phi^{-1}` before assigning reality or generative load.

```text
same physical object
→ exact invertible reparameterisation
→ same native predictions / admissibility / statistics
→ representation may carry structural or ergonomic load
→ no independent reality-load or new-physics promotion from coordinate choice alone
```

The Bell TBC is the worked calibration: the facet-plus-normal chart reconstructs the four-correlator object exactly, but its natural four-volume reduces to a rescaling of CHSH excess. The chart therefore earns structural/addressing utility without earning an independent physical invariant.

If a representation claim seeks promotion beyond bookkeeping, require a separately named gain under matched information and resources: lower reconstruction burden, better omission detection, smaller correct descent set, a new valid constraint not imported from the native owner, or a prospective measurable discriminator. Otherwise classify the geometry as a representation layer and keep native scientific ownership unchanged.
'''
if "### 7.3B Reparameterisation-control deformation" not in s:
    marker = "\n### 7.4 Temporal maintenance-path deformation"
    if marker not in s:
        raise SystemExit("Module25 insertion marker missing")
    s = s.replace(marker, block + marker, 1)
write(path, s)

path = "docs/32S3_RELATIONAL_BRACKETS_COMPLETION_GEOMETRY_AND_I_TO_P_ADMISSIBILITY.md"
s = read(path)
s = s.replace("**Compositional-interface publication:** [Cross-Domain Compositional Schema v0.3](../CROSS_DOMAIN_COMPOSITIONAL_SCHEMA_STANDALONE_PUBLICATION.md), DOI `10.5281/zenodo.22166005`; preserve/reopen ownership remains in [33S7A](33S7A_FUTURE_SUFFICIENT_ADDRESS_INVARIANT_AND_LAYER_BEFORE_LAW_PRECEDENCE.md).",
              "**Compositional-interface publication:** [Cross-Domain Compositional Schema v0.4](../CROSS_DOMAIN_COMPOSITIONAL_SCHEMA_STANDALONE_PUBLICATION.md), DOI `" + DOI_NEW + "`; preserve/reopen ownership remains in [33S7A](33S7A_FUTURE_SUFFICIENT_ADDRESS_INVARIANT_AND_LAYER_BEFORE_LAW_PRECEDENCE.md), with Bell/TBC calibration in [28A](28A_CROSS_DOMAIN_COMPOSITIONAL_SCHEMA_BELL_CHSH_CALIBRATION.md).")
block = r'''

## Bell/TBC fibre correspondence — v0.4 publication fold

Cross-Domain Compositional Schema v0.4 supplies a clean external calibration of this module's existing fibre/completion boundary without creating new completion geometry. The Bell correlator projection

```math
\pi_E:P\longmapsto E
```

is many-to-one: behaviours with the same four correlators can retain different local-marginal structure. The v0.4 Facet-adapted Tetrahedral Bell Chart is an exact coordinate chart for the correlator object `E`,

```math
E=V\lambda+\frac{\nu}{4}c,
\qquad
\mathbf1^{\mathsf T}\lambda=1,
```

but the inverse image `pi_E^{-1}(E)` remains a fibre of full behaviours. Consequently:

```text
correlator/TBC target
→ chart may be complete

marginal or full-behaviour target
→ chart alone is incomplete
→ reopen marginal-bearing coordinates / completion owner
```

This is a local-to-global custody example, not a new Bell mechanism. Module 32S3 retains completion/fibre ownership; Module 33S7A owns the preserve/reopen consequence; Module 28A owns the Bell-native calculation. An exact chart of one projection must not be mistaken for completion of the parent object.
'''
if "## Bell/TBC fibre correspondence — v0.4 publication fold" not in s:
    s = s.rstrip() + block + "\n"
write(path, s)

# ---------------------------------------------------------------------------
# Recursive learning
# ---------------------------------------------------------------------------
path = "RESEARCH_DERIVATION_AND_CLOSURE_SOP.md"
s = read(path)
block = r'''

### 17A.9 Obstruction-to-construction recursion and reparameterisation nulls

A negative result can close one candidate representation while opening a narrower lawful construction. Do not flatten the distinction.

The Cross-Domain v0.4 Bell continuation is the standing worked example. The v0.3 dimension count correctly killed the claim that one ordinary three-degree-of-freedom tetrahedral barycentric point can losslessly encode an unrestricted four-correlator object. The next recursive pass did **not** reverse that result. It asked what exact object the obstruction permits:

```text
strong obstruction survives
→ freeze what it actually killed
→ identify the missing degree / relation / address
→ search existing native geometry for a lawful owner
→ construct the smallest richer object that satisfies the obstruction
→ prove reconstruction / loss conditions
→ subtract native ownership again
→ test apparent new invariants for algebraic collapse
→ run reparameterisation null before any physics promotion
```

That pass found a Bell-native tetrahedral CHSH facet plus one transverse coordinate, yielding an exact four-dimensional chart. It then killed the obvious hypervolume novelty because the volume reduced to `|S-2|/3`, and killed a physics promotion because the chart is invertible and supplies no additional law.

> **When a candidate fails by a clean theorem, rank, dimension, type, or custody obstruction, preserve the failure exactly and ask whether it identifies the minimum additional structure required for a lawful successor. A successor is not a rescue of the failed claim unless it silently deletes the obstruction.**

Before calling a richer representation scientifically new, run the reparameterisation null: if every observable and admissibility result is carried through an invertible map from the native object, the representation can earn structural or ergonomic utility but not an independent physical residual merely from its coordinates.
'''
if "### 17A.9 Obstruction-to-construction recursion" not in s:
    marker = "\n## 18. Closure language"
    if marker not in s:
        raise SystemExit("SOP insertion marker missing")
    s = s.replace(marker, block + marker, 1)
write(path, s)

# ---------------------------------------------------------------------------
# Discovery/canon/provenance surfaces
# ---------------------------------------------------------------------------
common_block = tpl(r'''## Cross-Domain Compositional Schema v0.4 — current publication update

- current version DOI: `__DOI_NEW__`
- prior v0.3 DOI: `__DOI_V03__`
- concept DOI: `__DOI_CONCEPT__`
- reader route: `papers/2026-08-29_CROSS_DOMAIN_COMPOSITIONAL_SCHEMA_v0.4.md`
- publication record: `CROSS_DOMAIN_COMPOSITIONAL_SCHEMA_STANDALONE_PUBLICATION.md`
- live future-sufficiency owner: `docs/33S7A_FUTURE_SUFFICIENT_ADDRESS_INVARIANT_AND_LAYER_BEFORE_LAW_PRECEDENCE.md`
- live Bell/tetrahedral owner: `docs/28A_CROSS_DOMAIN_COMPOSITIONAL_SCHEMA_BELL_CHSH_CALIBRATION.md`

Version 0.4 closes the tetrahedral Bell branch as an exact facet-plus-normal coordinate construction on native CHSH geometry. The chart is an invertible reparameterisation, the natural four-volume collapses to CHSH excess, and the physical residual remains NULL. The v0.3 and v0.2 routes remain historical frozen versions.
''')
for path in [
    "README.md",
    "INDEX.md",
    "CANON_MAP.md",
    "papers/README.md",
    "PUBLIC_DISCOVERY_ANCHOR.md",
    "DISCOVERY_KEYWORDS.md",
    "START_HERE_PUBLIC_OVERVIEW.md",
    "00-START-HERE-MKUFT-PUBLIC.md",
    "SCIENCE_CONVERGENCE_AND_NOVELTY_MAP.md",
]:
    append_once(path, "Cross-Domain Compositional Schema v0.4 — current publication update", common_block)

append_once("PROVENANCE_DOI_AND_ATTRIBUTION.md", "Cross-Domain Compositional Schema v0.4 — published 29 August 2026", tpl(r'''## Cross-Domain Compositional Schema v0.4 — published 29 August 2026

**Title:** *__TITLE__*  
**Version DOI:** `__DOI_NEW__`  
**Prior v0.3 DOI:** `__DOI_V03__`  
**Concept DOI:** `__DOI_CONCEPT__`  
**Licence:** CC BY 4.0  
**Frozen carrier:** 31 pages; 394,810 bytes; MD5 `__MD5__`; SHA-256 `__SHA256__`.

Version 0.4 is a new immutable publication object in the same Zenodo lineage. It does not alter the v0.3 or v0.2 deposits. Live MKUFT modules integrate the published result under their own revision history and must not be cited as byte-identical to the Zenodo carrier.
'''))

append_once("RIGHTS_AND_LICENSE_NOTICE.md", "Cross-Domain Compositional Schema v0.4", tpl(r'''## Cross-Domain Compositional Schema v0.4

The exact Zenodo v0.4 deposit at DOI `__DOI_NEW__` is licensed **CC BY 4.0** as stated in that publication. This licence applies to the exact deposited v0.4 object and does not silently relicense unrelated MKUFT modules or historical publications. The prior v0.3/v0.2 objects retain their own published licence statements.
'''))

path = Path("codemeta.json")
data = json.loads(path.read_text(encoding="utf-8"))
data["description"] = data["description"].replace("Cross-Domain Compositional Schema v0.3", "Cross-Domain Compositional Schema v0.4")
newurl = "https://doi.org/" + DOI_NEW
if newurl not in data.setdefault("citation", []):
    data["citation"].insert(3, newurl)
route = "https://github.com/mark45cdo-mkuft/MKUFT/blob/main/papers/2026-08-29_CROSS_DOMAIN_COMPOSITIONAL_SCHEMA_v0.4.md"
if route not in data.setdefault("subjectOf", []):
    data["subjectOf"].insert(2, route)
for kw in ["Facet-adapted Tetrahedral Bell Chart", "semantic attachment", "Bell correlation polytope", "reparameterisation null"]:
    if kw not in data.setdefault("keywords", []):
        data["keywords"].append(kw)
path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

# ---------------------------------------------------------------------------
# Persistent regression guard
# ---------------------------------------------------------------------------
path = "tools/check_publication_routes.py"
s = read(path)
s = s.replace(
    'CROSS_DOMAIN_VERSION = "10.5281/zenodo.22166005"\nCROSS_DOMAIN_PREVIOUS = "10.5281/zenodo.22164562"\nCROSS_DOMAIN_PAPER = "2026-08-29_CROSS_DOMAIN_COMPOSITIONAL_SCHEMA_v0.3.md"',
    'CROSS_DOMAIN_VERSION = "10.5281/zenodo.22166468"\nCROSS_DOMAIN_PREVIOUS = "10.5281/zenodo.22166005"\nCROSS_DOMAIN_EARLIER = "10.5281/zenodo.22164562"\nCROSS_DOMAIN_CONCEPT = "10.5281/zenodo.22164561"\nCROSS_DOMAIN_PAPER = "2026-08-29_CROSS_DOMAIN_COMPOSITIONAL_SCHEMA_v0.4.md"',
)
s = s.replace(
    'CROSS_DOMAIN_MD5 = "985801aceccb3ce3effe6da1f4d1d496"\nCROSS_DOMAIN_SHA256 = "fd4459711d2f1210b2c770c38611554c0e10a8e1748063fc1d78d0a4ef607c5b"',
    'CROSS_DOMAIN_MD5 = "' + MD5 + '"\nCROSS_DOMAIN_SHA256 = "' + SHA256 + '"',
)
s = s.replace(
    'CROSS_DOMAIN_PREVIOUS,\n        CROSS_DOMAIN_PAPER,',
    'CROSS_DOMAIN_PREVIOUS,\n        CROSS_DOMAIN_EARLIER,\n        CROSS_DOMAIN_CONCEPT,\n        CROSS_DOMAIN_PAPER,',
)
write(path, s)

# No branch-only scaffold may survive the folded commit.
Path("tools/_apply_cross_domain_v04_fold.py").unlink(missing_ok=True)
Path(".github/workflows/v04-cross-domain-fold.yml").unlink(missing_ok=True)
