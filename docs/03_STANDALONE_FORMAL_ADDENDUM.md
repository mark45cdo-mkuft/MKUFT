# MKUFT — Standalone Formal Addendum


<!-- MKUFT-PROVENANCE-HEADER:START -->
**Author:** Mark Charles McLaughlin  
**Framework:** McLaughlin–Kairos Unified Field Theory (MKUFT)  
**MKUFT DOI:** `10.5281/zenodo.17780566`  
**Provenance:** This module is part of the public MKUFT canon. Exact revisions are timestamped by Git history.  
**Citation:** See [`PROVENANCE_DOI_AND_ATTRIBUTION.md`](../PROVENANCE_DOI_AND_ATTRIBUTION.md).  
<!-- MKUFT-PROVENANCE-HEADER:END -->

## Mathematical Formalisation, Falsifiability, and Experimental Pathways

Status: public formal addendum inside the controlled MKUFT GitHub working copy  
Relationship to core: sharpens and operationalises the core without replacing the DOI-linked source work.

This addendum introduces mathematical objects and failure conditions for structural concepts already present in MKUFT.

The objects below are working models. They are not established physical laws merely because they are written mathematically.

---

## 1. Purpose

This addendum aims to:

- formalise constrained state and transition structure;
- define traversal cost;
- connect path availability to candidate probability models;
- state explicit falsifiers;
- show how the Silver Update extends the original graph formalism.

No new entity or ontology is established by this document.

---

## 2. Architectural premise

MKUFT tests the hypothesis that geometry, relation, boundary, and constraint help determine:

- which states are stable;
- which transitions are admissible;
- what transitions cost;
- what outcomes persist.

The public claim is not that all physical law has already been derived from MKUFT geometry. The claim is that constrained traversal provides a common modelling grammar that can be tested across layers.

---

## 3. Constrained state graph

Represent a modelled state space as:

```text
G = (N,E)
```

where:

- `N` is a set of stable or operationally distinguishable states;
- `E` is a set of admissible transitions.

Whether `N` is finite, countable, or continuous depends on the domain and discretisation. No universal finiteness claim is made.

A node may represent an attractor, physical state, information state, role, address, or repeatable configuration.

---

## 4. Trajectories

A trajectory is an ordered path:

```text
γ = (n_0 → n_1 → ... → n_k)
```

Traversal is constrained by adjacency or by the continuous equivalent defined for the chosen domain.

Agency, interaction, and evolution can be analysed as movement through available state structure. This does not imply that genuinely new effective states can never emerge; it requires any claimed state creation to be defined rather than smuggled into the model.

---

## 5. Traversal cost

A candidate cost functional is:

```text
C[γ] = ∫_γ λ(x) ds
```

where:

- `λ(x)` is a domain-specific local cost, friction, instability, contradiction, or gradient term;
- `ds` is a path element.

`λ` must be given units or a clearly normalised scale in any quantitative application.

Low `C[γ]` indicates a comparatively accessible route under the selected model. High `C[γ]` indicates resistance, instability, or low admissibility.

---

## 6. Path-weight model

A candidate transition weighting is:

```text
P(B|A) ∝ Σ_{γ ∈ Γ(A→B)} exp[-C[γ]]
```

where `Γ(A→B)` is the set of modelled admissible paths from `A` to `B`.

This is a Gibbs-like path-weight model. It does not establish that fundamental probability is nothing but path density. It tests whether path availability and cost improve prediction in a specified domain.

The model fails where accepted domain models predict better without this additional structure.

---

## 7. Learning and adaptation

One useful learning model is local cost reduction along repeatedly successful trajectories:

```text
λ_{t+1}(x) < λ_t(x)
```

for relevant segments of the practiced route.

This can represent skill acquisition, habit, improved control, or lower prediction error.

It is not claimed that learning can never create new effective representations or states. The narrower claim is that many learning curves can be modelled as changes in accessibility and cost over an existing or expanding state graph.

---

## 8. Experienced time

A working phenomenological hypothesis is:

```text
T_experienced ∝ Σ_i C[γ_i]
```

This predicts that high processing burden, conflict, threat, or constrained traversal may correlate with experienced slowing, while fluent low-cost traversal may correlate with time compression.

This is a model of experienced time, not proof that physical time is non-fundamental.

---

## 9. Core falsifiability

### 9.1 Path structure

Prediction:

Path availability and cost improve outcome prediction beyond simpler baselines.

Failure condition:

They add no predictive value, or preferred outcomes occur independently of the defined path structure.

### 9.2 Learning

Prediction:

Practice changes measurable route cost, error, or accessibility.

Failure condition:

The cost model performs worse than standard learning models and adds no useful discrimination.

### 9.3 Boundary-edge clustering

Prediction:

Some pre-defined anomaly classes cluster near measurable thresholds, gradients, or adjacency changes.

Failure condition:

No clustering survives selection-bias controls, exposure correction, and out-of-sample testing.

### 9.4 Measurement context

Prediction:

Measurement context changes routing or recorded statistics in ways specified before the test.

Failure condition:

No predicted context effect remains after accepted physical and statistical explanations.

---

## 10. Experimental pathways

Candidate tests include:

- computational simulation of constrained graphs;
- learning-curve comparisons;
- threshold and boundary experiments;
- measurement-context studies;
- pre-registered anomaly-distribution analysis.

Each experiment must define its domain variables, baseline model, primary outcome, and failure condition.

---

## 11. Silver Update — unresolved feasible regions

The original graph describes resolved or operationally named states. The Silver Update adds the unresolved region still compatible with evidence and constraint.

```text
A_t^vol = log(1 + μ(Ω_t)/μ_0)
```

where:

- `Ω_t` is the unresolved feasible region;
- `μ_0` is a reference scale.

Let:

```text
R_t ∈ [0,1]
```

represent normalised low-cost connectivity, and:

```text
X_t ∈ [0,1]
```

represent normalised preserved access.

The heuristic manoeuvrability index is:

```text
M_t = A_t^vol × R_t × X_t
```

This extends the graph model:

- nodes describe states that can be held or named;
- `Ω_t` describes unresolved alternatives;
- `R_t` describes movement among them;
- `X_t` describes whether movement preserves access or influence.

See `docs/21_AMBIGUITY_DYNAMICS_AND_MANOEUVRE_SPACE.md`.

---

## 12. Silver Update — layer addressing

Let `K` be a candidate invariant, `L ∈ {S,I,P,O}` the active layer, and `θ_L` the layer-specific constraints and observables.

```text
K_L = A_L(K;θ_L)
```

A valid address must specify:

- the invariant relation;
- the active layer;
- changed variables and units;
- evidence required at that layer;
- any cross-layer coupling;
- an independent falsifier.

A repeated algebraic form does not prove an identical mechanism across layers.

See `docs/22_CROSS_LAYER_INVARIANTS_AND_LAYER_ADDRESSING.md`.

---

## 13. Silver Update — agency accessibility

Let `U_t` be the actual action set and `U_t^access` the practically accessible subset:

```text
U_t^access = {u ∈ U_t : G_t(u;T_t,H_t) > θ_access}
```

A retained capacity may remain while access is degraded:

```text
Agency_effective(t) = Agency_capacity × a_t
```

with `a_t ∈ [0,1]`.

This is an operational distinction, not a complete moral, legal, or clinical equation.

See `docs/23_AGENCY_ACCESSIBILITY_AND_CAPTURE_GEOMETRY.md`.

---

## 14. Integrity rule

A formal expression counts only when it:

- improves discrimination;
- supports prediction;
- states a null result;
- survives ordinary explanations;
- keeps layer evidence separate;
- can be revised or removed after failure.

A failed submodel must not be protected by the breadth of the wider framework.

---

## 15. Architecture route

```text
conceptual core: docs/01_MKUFT_CORE_EXTENDED.md
math definitions: docs/02_MKUFT_MATH_APPENDIX.md
experiments: docs/04_EXPERIMENTAL_TEST_PROGRAM.md
falsification: docs/05_FALSIFICATION_SUMMARY.md
ambiguity: docs/21_AMBIGUITY_DYNAMICS_AND_MANOEUVRE_SPACE.md
layer addressing: docs/22_CROSS_LAYER_INVARIANTS_AND_LAYER_ADDRESSING.md
agency accessibility: docs/23_AGENCY_ACCESSIBILITY_AND_CAPTURE_GEOMETRY.md
repository routing: docs/24_MKUFT_CROSS_SUPPORT_AND_TRAVERSAL_MAP.md
```

## 16. Canon status

This document is a public formal expansion of MKUFT. It sharpens the working copy while preserving the provenance and identity of the original DOI-linked material.
