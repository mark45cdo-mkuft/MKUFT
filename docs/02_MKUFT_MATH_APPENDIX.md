# MKUFT Mathematical Appendix — Clean Working Copy

Author: Mark McLaughlin

Status: mathematical backbone for the public controlled MKUFT GitHub working repository.

## A1. Substrate as Probability Space

The substrate is modelled as a probability or measure space:

```text
S = (Ω, Σ, μ)
```

Where:

- Ω is the set of possible configurations.
- Σ is a sigma-algebra of measurable subsets of Ω.
- μ is a measure assigning baseline weight or propensity to configurations.

The substrate is not directly observed; it is the possibility field from which physically realised events are selected.

## A2. Information Structures

Information structures are represented as functions over the substrate:

```text
I = { f : Ω → R | f ∈ L²(Ω, μ) }
```

These structures encode patterns, constraints, correlations, and proto-physical forms.

For a physical event E, define I(E) as the set of information structures compatible with E.

## A3. Physical Dynamics

The physical layer supplies the standard dynamical contribution. Standard dynamics map initial physical states to probability distributions over future events.

For an event E:

```text
P_phys(E)
```

is the standard physical probability derived from accepted physical dynamics.

## A4. Observer System and Coherence Functional

The observer O is modelled as a system with internal state ρ_O. Coherence is represented by a functional:

```text
κ : States(H_O) → [0, 1]
```

Where:

- κ close to 1 indicates high coherence: focused, aligned, low internal contradiction.
- κ close to 0 indicates fragmentation, noise, or disorder.

κ is not fixed to one measurement method. It may be approximated through physiological, cognitive, or behavioural proxies.

## A5. Integral Realisation Equation

For event E, the unnormalised MKUFT weight is:

```text
W_total(E) = ∫_{I ∈ I(E)} D_phys(E | I) · W(I | S, E) · C(O | I, E) dν(I)
```

Where:

- D_phys(E | I) is the standard physical contribution conditioned on information structure I.
- W(I | S, E) is the substrate-to-information weighting.
- C(O | I, E) is the observer-dependent coherence modulation.
- ν is a measure over compatible information structures.

The realised probability is:

```text
P_realized(E) = W_total(E) / Z
```

with:

```text
Z = Σ_{E'} W_total(E')
```

## A6. Reduction to Standard Physics

If observer coherence does not contribute, then:

```text
C(O | I, E) = C_0
```

If information weighting introduces no additional selection beyond standard physics, then:

```text
P_realized(E) ≈ P_phys(E)
```

This recovers standard physics as the limiting case.

## A7. Linear Response Approximation

Observer influence is treated as a small perturbation:

```text
C(O | I, E) = C_0 [1 + ε g_O(I, E)]
```

Where:

- ε is a small dimensionless strength parameter.
- g_O(I, E) encodes observer-state-dependent weighting.

To first order:

```text
P_realized(E) ≈ P_phys(E) + ε Δ_O(E)
```

This gives a disciplined bridge between standard physics and small systematic deviations.

## A8. Coherence-Linked Modulation

Tie observer coherence directly to the modulation term:

```text
C(O | I, E) = C_0 [1 + ε κ(ρ_O) h(I, E)]
```

Where h(I, E) captures pattern matching between observer state and information structure.

Interpretation:

- κ determines how strong the observer modulation can become.
- h determines which event structures are favoured.
- Low κ drives the system back toward standard physics.

## A9. Environmental Damping

Let F denote environmental parameters such as EM field characteristics, geomagnetic indices, iron concentration, geometry, and noise.

Both W and C may depend on F:

```text
W(I | S, E, F)
C(O | I, E, F)
```

A simplified environmental damping form is:

```text
κ_eff = κ(ρ_O) · η(F)
```

Where η(F) ∈ [0,1]. Disruptive environments reduce effective coherence.

## A10. Group Coherence

For a group of observers {O_1, ..., O_N}, define:

```text
κ_group = Φ(κ_1, ..., κ_N, C_corr)
```

Where C_corr represents alignment or correlation of intention/state.

Possible approximations include:

```text
κ_group = (1/N) Σ κ_i
κ_group = A · (1/N) Σ κ_i
```

Where A ∈ [0,1] is an alignment factor.

## A11. Experimental Connections

- RNG/REG experiments: E corresponds to bit sequences or summary statistics.
- Remote viewing: E corresponds to correct or incorrect target-description matches.
- Synchronicity: E encodes theme-compatible co-occurrences.
- Environmental modulation: F changes κ_eff and effect size.
- Group effects: κ_group predicts amplification under shared coherent alignment.

## A12. Ambiguity Volume

For a live claim or system at time `t`, define the feasible region:

```text
Ω_t = {states, paths, interpretations, identities, or hypotheses compatible with E_t and C_t}
```

where `E_t` is available evidence and `C_t` is the active constraint set.

Let `μ_0` be a reference measure. Define dimensionless ambiguity volume:

```text
A_t = log(1 + μ(Ω_t) / μ_0)
```

This is a formal audit handle, not a claim that every dimension is directly measurable.

The ambiguity module adds route connectivity `R_t` and preserved access `X_t`:

```text
M_t = A_t × R_t × X_t
```

`M_t` is a working measure of manoeuvrability inside unresolved state space.

- High `A_t` alone means many possibilities remain.
- High `R_t` means low-cost transitions exist between unresolved frames or states.
- High `X_t` means those transitions preserve access, influence, extraction, or credibility.

See `21_AMBIGUITY_DYNAMICS_AND_MANOEUVRE_SPACE.md` for definitions, discriminators, predictions, and falsifiers.

## A13. Cross-Layer Address Map

Let `K` be a candidate invariant and `L ∈ {S,I,P,O}` the active layer.

Let `θ_L` denote the layer-specific constraints, observables, units, noise terms, and admissible transitions.

Define the layer expression:

```text
K_L = A_L(K ; θ_L)
```

This does not make a new ontology at every layer. It states that the same invariant may require a different measurable expression at each address.

A valid address map must preserve:

- the defining relation of `K`;
- explicit changes in variables;
- layer-appropriate evidence;
- independent falsifiers;
- a stated cross-layer coupling where one is claimed.

See `22_CROSS_LAYER_INVARIANTS_AND_LAYER_ADDRESSING.md`.

## A14. Agency Accessibility

Let `U_t` be the actions actually available to an agent and `Û_t` the actions perceived as available.

Let `G_t(u ; T_t, H_t)` be the gating function for action `u`, with `T_t` representing perceived threat and `H_t` representing reinforcement history.

Define the practically accessible action set:

```text
U_t^access = {u ∈ U_t : G_t(u ; T_t, H_t) > θ_access}
```

Let `a_t ∈ [0,1]` represent practical accessibility to retained agency:

```text
Agency_effective(t) = Agency_capacity × a_t
```

This is an operational distinction, not a complete moral or clinical equation.

See `23_AGENCY_ACCESSIBILITY_AND_CAPTURE_GEOMETRY.md` for capture variables, responsibility gradients, recovery mechanics, and ontology boundaries.

## A15. Silver Update Reduction Rules

The new formal handles must reduce cleanly:

- If `R_t` or `X_t` is negligible, high ambiguity does not imply high manoeuvrability.
- If one layer address fails, the failure must not be hidden by evidence from another address.
- If perceived and actual action sets do not differ, the agency-accessibility mechanism is unnecessary.
- If simpler noise, incentive, habit, uncertainty, or standard physical models explain the data better, use them.
- No formal expression counts as evidence merely because it is mathematically writable.

## Notation Correction

Converted-source glitches such as `Prealized` are normalised as `P_realized`. Broken placeholder symbols are rendered as I(E), Ω, or other explicit notation where context is clear.