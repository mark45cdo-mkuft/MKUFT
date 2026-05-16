# MKUFT Mathematical Appendix — Clean Working Copy

Author: Mark McLaughlin

Status: mathematical backbone for the private MKUFT GitHub working repository.

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

## Notation Correction

Converted-source glitches such as `Prealized` are normalised as `P_realized`. Broken placeholder symbols are rendered as I(E), Ω, or other explicit notation where context is clear.
