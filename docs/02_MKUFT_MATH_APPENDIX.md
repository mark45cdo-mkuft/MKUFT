# MKUFT Mathematical Appendix — Clean Working Copy



<!-- MKUFT-PROVENANCE-HEADER:START -->
**Author:** Mark Charles McLaughlin  
**Framework:** McLaughlin–Kairos Unified Field Theory (MKUFT)  
**MKUFT DOI:** `10.5281/zenodo.17780566`  
**Provenance:** This module is part of the public MKUFT canon. Exact revisions are timestamped by Git history.  
**Citation:** See [`PROVENANCE_DOI_AND_ATTRIBUTION.md`](../PROVENANCE_DOI_AND_ATTRIBUTION.md).  
<!-- MKUFT-PROVENANCE-HEADER:END -->

Status: mathematical backbone for the public controlled MKUFT GitHub working repository.

## A1. Substrate as Probability Space

The substrate is modelled as a probability or measure space:

```text
S = (Ω, Σ, μ)
```

where:

- `Ω` is the set of possible configurations;
- `Σ` is a sigma-algebra of measurable subsets of `Ω`;
- `μ` assigns baseline weight or propensity.

The substrate is not directly observed. This is a mathematical representation of structured possibility, not evidence that a separate material medium has been detected.

## A2. Information Structures

Information structures are represented as functions over the substrate:

```text
I = {f : Ω → R | f ∈ L²(Ω, μ)}
```

These functions encode candidate patterns, constraints, correlations, and proto-physical forms.

For event `E`, define `I(E)` as the set of information structures compatible with `E`.

## A3. Physical Dynamics

The physical layer supplies the accepted dynamical contribution:

```text
P_phys(E)
```

This is the probability or prediction obtained from the relevant established physical model.

## A4. Observer System and Coherence Functional

The observer is modelled as a system with state `ρ_O`. A bounded coherence functional is:

```text
κ : States(H_O) → [0,1]
```

where high `κ` means lower measured internal noise or contradiction according to a pre-defined proxy.

`κ` is not fixed to one measurement method and must be operationally defined in each experiment.

## A5. Integral Realisation Equation

For event `E`, define the unnormalised working weight:

```text
W_total(E) = ∫_{I ∈ I(E)} D_phys(E|I) W(I|S,E) C(O|I,E) dν(I)
```

where:

- `D_phys(E|I)` is the accepted physical contribution conditioned on `I`;
- `W(I|S,E)` is a candidate substrate-to-information weighting;
- `C(O|I,E)` is a bounded observer-condition term;
- `ν` is a measure over compatible information structures.

The realised probability is:

```text
P_realized(E) = W_total(E) / Z
```

with:

```text
Z = Σ_{E'} W_total(E')
```

This equation is a theoretical scaffold. It becomes empirical only when the terms are independently operationalised.

## A6. Reduction to Standard Physics

If the observer term is constant:

```text
C(O|I,E) = C_0
```

and the additional information weighting does not alter standard selection, then:

```text
P_realized(E) ≈ P_phys(E)
```

Failure to recover the ordinary limit is a failure of the model.

## A7. Linear-Response Approximation

A small bounded observer term may be written:

```text
C(O|I,E) = C_0 [1 + ε g_O(I,E)]
```

where `ε` is a small dimensionless parameter.

To first order:

```text
P_realized(E) ≈ P_phys(E) + ε Δ_O(E)
```

The sign, scale, and form of `Δ_O` must be pre-specified for a test; it cannot be inferred after observing the result.

## A8. Coherence-Linked Modulation

One candidate form is:

```text
C(O|I,E) = C_0 [1 + ε κ(ρ_O) h(I,E)]
```

where:

- `κ` measures the selected observer-state proxy;
- `h` specifies a pre-defined interaction with event structure.

Low or irrelevant `κ` should return the model toward the standard-physics limit.

## A9. Environmental Damping

Let `F` denote measured environmental parameters such as electromagnetic noise, geomagnetic indices, geometry, shielding, vibration, temperature, or pre-registered material composition.

A simplified form is:

```text
κ_eff = κ(ρ_O) η(F)
```

with:

```text
η(F) ∈ [0,1]
```

`η(F)` must be specified or estimated from measurements. It cannot be assigned retrospectively to rescue a null result.

## A10. Group Coherence

For observers `{O_1, ..., O_N}`:

```text
κ_group = Φ(κ_1, ..., κ_N, C_corr)
```

where `C_corr` represents measured alignment or correlation.

A simple candidate approximation is:

```text
κ_group = A_align × (1/N) Σ κ_i
```

with `A_align ∈ [0,1]`.

Group coherence is a coupled O/I/P condition, not a fifth ontological layer.

## A11. Experimental Connections

Candidate application classes include:

- REG/RNG condition comparisons;
- strictly blinded remote-information protocols;
- pre-registered co-occurrence studies;
- environmental modulation tests;
- group-alignment tests.

These are proposed tests, not established confirmations.

## A12. Ambiguity Volume

For a live claim or system at time `t`:

```text
Ω_t = {states, paths, interpretations, identities, or hypotheses compatible with E_t and C_t}
```

where `E_t` is available evidence and `C_t` is the active constraint set.

Let `μ_0` be a reference measure. Define:

```text
A_t^vol = log(1 + μ(Ω_t) / μ_0)
```

`A_t^vol` is dimensionless and is distinct from the older path-objective term `A(γ,t)` used for uncertainty along a candidate trajectory.

Let:

```text
R_t ∈ [0,1]
```

be normalised low-cost route connectivity, and:

```text
X_t ∈ [0,1]
```

be normalised preserved access.

Then the working manoeuvrability index is:

```text
M_t = A_t^vol × R_t × X_t
```

`M_t` is a heuristic audit index, not a validated universal law.

See `docs/21_AMBIGUITY_DYNAMICS_AND_MANOEUVRE_SPACE.md`.

## A13. Cross-Layer Address Map

Let `K` be a candidate invariant and `L ∈ {S,I,P,O}` the active layer. Let `θ_L` denote layer-specific constraints, observables, units, noise terms, and admissible transitions.

```text
K_L = A_L(K; θ_L)
```

`A_L` is an address map, not a new ontology.

A valid address map must preserve:

- the defining relation of `K`;
- explicit variable changes;
- layer-appropriate evidence;
- independent falsifiers;
- a stated coupling where cross-layer influence is claimed.

The same algebraic template across layers does not establish the same physical mechanism. Each address requires its own operationalisation.

See `docs/22_CROSS_LAYER_INVARIANTS_AND_LAYER_ADDRESSING.md`.

## A14. Agency Accessibility

Let `U_t` be the actions actually available and `Û_t` the actions perceived as available.

Let `G_t(u;T_t,H_t)` be a gating function for action `u`, where `T_t` represents perceived threat and `H_t` represents reinforcement history.

```text
U_t^access = {u ∈ U_t : G_t(u;T_t,H_t) > θ_access}
```

Let `a_t ∈ [0,1]` represent practical accessibility:

```text
Agency_effective(t) = Agency_capacity × a_t
```

This is an operational distinction, not a moral, legal, or clinical equation.

See `docs/23_AGENCY_ACCESSIBILITY_AND_CAPTURE_GEOMETRY.md`.

## A15. Silver Update Reduction Rules

- If `R_t` or `X_t` is negligible, high ambiguity does not imply high manoeuvrability.
- If one layer address fails, evidence from another address cannot conceal the failure.
- If perceived and actual action sets do not differ, the agency-accessibility mechanism is unnecessary.
- If simpler noise, incentive, habit, uncertainty, or standard physical models perform better, use them.
- A mathematical expression is not evidence merely because it can be written.

## A16. Architecture Route

```text
conceptual core: docs/01_MKUFT_CORE_EXTENDED.md
trajectory formalism: docs/03_STANDALONE_FORMAL_ADDENDUM.md
experiments: docs/04_EXPERIMENTAL_TEST_PROGRAM.md
worked examples: docs/14_WORKED_EXAMPLES_RNG_AND_ENVIRONMENT.md
falsification: docs/05_FALSIFICATION_SUMMARY.md
repository routing: docs/24_MKUFT_CROSS_SUPPORT_AND_TRAVERSAL_MAP.md
```

## Notation Correction

Converted-source glitches such as `Prealized` are normalised as `P_realized`. Broken placeholder symbols are rendered explicitly where context is clear.
