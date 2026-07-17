# MKUFT Mathematical Appendix — Clean Working Copy

<!-- MKUFT-PROVENANCE-HEADER:START -->
**Author:** Mark Charles McLaughlin  
**Framework:** McLaughlin–Kairos Unified Field Theory (MKUFT)  
**MKUFT DOI:** `10.5281/zenodo.17780566`  
**Provenance:** This module is part of the public MKUFT canon. Exact revisions are timestamped by Git history.  
**Citation:** See [`PROVENANCE_DOI_AND_ATTRIBUTION.md`](../PROVENANCE_DOI_AND_ATTRIBUTION.md).  
<!-- MKUFT-PROVENANCE-HEADER:END -->

Status: mathematical backbone for the public controlled MKUFT GitHub working repository.

## A1. Substrate as Measure Space

The substrate scaffold is modelled as a measure space:

```text
S = (Ω, Σ, μ)
```

where:

- `Ω` is the set of possible configurations;
- `Σ` is a sigma-algebra of measurable subsets of `Ω`;
- `μ` assigns baseline measure, weight, or propensity.

This becomes a probability space only when:

```text
μ(Ω) = 1
```

The substrate is not directly observed. This is a mathematical representation of structured possibility, not evidence that a separate material medium has been detected.

## A2. Information Structures

Because `I` already names the information layer, use `𝓘` for the mathematical function space:

```text
𝓘 = L²(Ω, μ)
```

An element `i ∈ 𝓘` represents one candidate information structure over the substrate. Such structures may encode patterns, constraints, correlations, and proto-physical forms.

For event `E`, define:

```text
𝓘_E ⊆ 𝓘
```

as the set of information structures compatible with `E` under the active model.

## A3. Physical Dynamics

The physical layer supplies the accepted dynamical contribution:

```text
P_phys(E)
```

This is the probability, probability density, or prediction obtained from the relevant established physical model. The type must be stated for the active event space.

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
W̃(E) = ∫_(i ∈ 𝓘_E)
        D_phys(E|i)
        W_SI(i|S,E)
        C_O(O|i,E)
        dν(i)
```

where:

- `D_phys(E|i)` is the accepted physical contribution conditioned on information structure `i`;
- `W_SI(i|S,E)` is a candidate substrate-to-information weighting;
- `C_O(O|i,E)` is a bounded observer-condition term;
- `ν` is a measure over compatible information structures.

Where this is used as a probability weight, the integrand must be non-negative and the normalisation finite.

For a discrete event space `𝓔`, the realised probability is:

```text
P_realized(E) = W̃(E) / Z
```

with:

```text
Z = Σ_(E' ∈ 𝓔) W̃(E')
```

For a continuous event space, replace the sum with an integral over a declared event-space measure.

This equation is a theoretical scaffold. It becomes empirical only when the terms are independently operationalised.

## A6. Reduction to Standard Physics

If the observer term is constant:

```text
C_O(O|i,E) = C_0
```

then that constant cancels under normalisation. Standard-physics recovery additionally requires the substrate-to-information weighting and compatible-structure integral to reproduce, or reduce to, the accepted physical distribution:

```text
P_realized(E) ≈ P_phys(E)
```

within a declared regime and tolerance.

Failure to recover the ordinary limit is a failure of the physics-facing model.

## A7. Linear-Response Approximation

A small observer-linked term may be written:

```text
C_O(O|i,E) = C_0 [1 + ε g_O(i,E)]
```

with:

```text
C_0 > 0
|ε g_O(i,E)| < 1
```

throughout the tested domain, so the weight remains positive.

After consistent expansion of both numerator and normalisation, a first-order form may be written:

```text
P_realized(E) ≈ P_phys(E) + ε Δ_O(E)
```

The sign, scale, and form of `Δ_O` must be pre-specified for a test; it cannot be inferred after observing the result. Neglected higher-order terms must remain bounded.

## A8. Coherence-Linked Modulation

One candidate form is:

```text
C_O(O|i,E) = C_0 [1 + ε κ(ρ_O) h(i,E)]
```

where:

- `κ` measures the selected observer-state proxy;
- `h` specifies a pre-defined interaction with event structure;
- positivity must hold throughout the tested domain.

Low, irrelevant, or experimentally unsupported `κ` should return the model toward the standard-physics limit.

## A9. Environmental Damping

Let `F_env` denote measured environmental parameters such as electromagnetic noise, geomagnetic indices, geometry, shielding, vibration, temperature, or pre-registered material composition.

A simplified form is:

```text
κ_eff = κ(ρ_O) η(F_env)
```

with:

```text
η(F_env) ∈ [0,1]
```

`η(F_env)` must be specified or estimated from measurements. It cannot be assigned retrospectively to rescue a null result.

## A10. Group Coherence

For observers `{O_1, ..., O_N}`:

```text
κ_group = Φ(κ_1, ..., κ_N, C_corr)
```

where `C_corr` represents measured alignment or correlation and the range of `Φ` must be declared.

A simple bounded candidate approximation is:

```text
κ_group = A_align × (1/N) Σ_i κ_i
```

with:

```text
A_align ∈ [0,1]
κ_i ∈ [0,1]
```

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

A quantitative ambiguity space must belong to one declared domain `d` with state space `X_d` and an explicit encoding.

For a live claim or system at time `t`, define:

```text
Ω_t^(d) = {z ∈ X_d : z remains compatible with E_t and C_t}
```

where `E_t` is available evidence and `C_t` is the active constraint set.

Let `μ_d` be a domain-specific measure and `μ_0,d` a reference measure. Define:

```text
A_t,vol^(d) = log[1 + μ_d(Ω_t^(d)) / μ_0,d]
```

This is dimensionless. States, paths, interpretations, identities, and hypotheses must not be placed into one measured set unless a common encoding has been defined.

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
M_t = A_t,vol × R_t × X_t
```

`M_t` is a heuristic multiplicative audit index, not a validated universal law. Its product form encodes a joint-dependence hypothesis and should be compared with additive, interaction, and non-linear alternatives.

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

For formal cross-layer work, declare typed spaces and couplings rather than assuming one common geometry:

```text
C_LM : X_L → X_M
```

See:

- `docs/22_CROSS_LAYER_INVARIANTS_AND_LAYER_ADDRESSING.md`
- `docs/27_TYPED_TRAVERSAL_AND_EQUATION_HYGIENE.md`

## A14. Agency Accessibility

Let `U_t` be the actions actually available and `Û_t` the actions perceived as available.

Let:

```text
G_t(u;T_t,H_t) ∈ [0,1]
θ_access ∈ [0,1]
```

where `T_t` represents perceived threat and `H_t` represents reinforcement history.

```text
U_t^access = {u ∈ U_t : G_t(u;T_t,H_t) > θ_access}
```

Let `a_t ∈ [0,1]` represent practical accessibility:

```text
Agency_effective(t) = Agency_capacity × a_t
```

This is an operational distinction, not a moral, legal, or clinical equation.

See `docs/23_AGENCY_ACCESSIBILITY_AND_CAPTURE_GEOMETRY.md`.

## A15. Path Cost and Weighting

For a trajectory `γ` in one declared state space, a candidate path cost is:

```text
C[γ] = ∫_γ λ(x) ds
```

The path element `ds`, local cost `λ`, and resulting units must be declared. This integral must not be applied across incompatible S, I, P, and O spaces without a typed common construction.

A Gibbs-like path weighting requires a dimensionless exponent. Use either a dimensionless normalised cost `C̃[γ]`:

```text
P(B|A) = (1/Z_A) Σ_(γ ∈ Γ(A→B)) exp[-C̃[γ]]
```

or an inverse cost scale `β`:

```text
P(B|A) = (1/Z_A) Σ_(γ ∈ Γ(A→B)) exp[-β C[γ]]
```

with:

```text
Z_A = Σ_(B') Σ_(γ ∈ Γ(A→B')) exp[-β C[γ]]
```

Path multiplicity and cost are candidate predictors, not a universal definition of probability.

## A16. Silver Update Reduction Rules

- If `R_t` or `X_t` is negligible, high ambiguity does not imply high manoeuvrability.
- If one layer address fails, evidence from another address cannot conceal the failure.
- If perceived and actual action sets do not differ, the agency-accessibility mechanism is unnecessary.
- If simpler noise, incentive, habit, uncertainty, or standard physical models perform better, use them.
- A mathematical expression is not evidence merely because it can be written.
- A tuple, projection, or named update map does not prove that the component spaces or couplings have been derived.

## A17. Architecture Route

```text
conceptual core: docs/01_MKUFT_CORE_EXTENDED.md
trajectory formalism: docs/03_STANDALONE_FORMAL_ADDENDUM.md
experiments: docs/04_EXPERIMENTAL_TEST_PROGRAM.md
worked examples: docs/14_WORKED_EXAMPLES_RNG_AND_ENVIRONMENT.md
falsification: docs/05_FALSIFICATION_SUMMARY.md
typed traversal and equation hygiene: docs/27_TYPED_TRAVERSAL_AND_EQUATION_HYGIENE.md
repository routing: docs/24_MKUFT_CROSS_SUPPORT_AND_TRAVERSAL_MAP.md
```

## Notation Correction

Converted-source glitches such as `Prealized` are normalised as `P_realized`. The symbols `I`, `𝓘`, and `i` are kept distinct for the information layer, information-function space, and one information structure respectively. Domain-qualified symbols are used where one unqualified symbol would hide incompatible spaces.