# MKUFT Worked Examples — RNG Bias and Environmental Modulation

Author: Mark Charles McLaughlin

Status: public worked-example appendix inside the controlled MKUFT GitHub working copy.

## Purpose

This document shows how selected MKUFT equations could connect to measurable predictions.

The numerical values below are illustrative only. They are not observed results, expected effect sizes, or evidence for MKUFT.

If MKUFT is to function scientifically, it must state what would be measured, how uncertainty is calculated, and what result would count against the model.

## 1. Realisation Equation

For event `E`:

```text
P_realized(E) = W_total(E) / Σ_{E'} W_total(E')
```

with unnormalised weight:

```text
W_total(E) = ∫ D_phys(E|I) W(I|S,E) C(O|I,E) dν(I)
```

where:

- `D_phys(E|I)` = standard physical dynamics;
- `W(I|S,E)` = substrate-to-information weighting;
- `C(O|I,E)` = observer-condition modulation;
- `dν(I)` = measure over compatible information structures.

This is a working formal scaffold. The model gains empirical content only when each term is operationally defined for a specific experiment.

## 2. Linear-Response Form

A bounded observer term may be written:

```text
C(O|I,E) = C_0 [1 + ε κ(O) h(I,E)]
```

where:

- `κ(O) ∈ [0,1]` is a measured coherence proxy;
- `ε` is a small coupling parameter;
- `h(I,E)` is a pre-specified event-structure interaction term.

Define:

```text
W_phys(E) = ∫ D_phys(E|I) W(I|S,E) dν(I)
```

and:

```text
ΔW_O(E) = ∫ D_phys(E|I) W(I|S,E) h(I,E) dν(I)
```

Then:

```text
W_total(E) = C_0 [W_phys(E) + ε κ(O) ΔW_O(E)]
```

For small `ε`, the testable approximation is:

```text
P_realized(E) ≈ P_phys(E) + ε Δ_O(E)
```

Plain English:

Standard physics supplies the baseline. MKUFT permits only a small, bounded correction that must be estimated rather than assumed.

## 3. Binary RNG Example

Let a binary random number generator produce:

```text
E_1 = output 1
E_0 = output 0
```

For a fair generator:

```text
P_phys(E_1) = P_phys(E_0) = 0.5
```

A pre-registered MKUFT test would compare two independent blocks:

- baseline or control;
- coherence/intention condition.

The null hypothesis is:

```text
p_control = p_condition = 0.5
```

The alternative is a small condition-linked difference specified before data collection.

## 4. Correct Two-Proportion Numerical Example

Assume two independent blocks with:

```text
N_control = 10,000,000
N_condition = 10,000,000
```

Illustrative proportions:

```text
p_control = 0.5000
p_condition = 0.5007
```

Difference:

```text
Δp = 0.0007
```

For two independent proportions near `p = 0.5`, the approximate standard error of the difference is:

```text
SE_diff = sqrt[p_control(1-p_control)/N_control
             + p_condition(1-p_condition)/N_condition]
```

Numerically:

```text
SE_diff ≈ sqrt(0.25/10,000,000 + 0.25/10,000,000)
        ≈ 0.0002236
```

Therefore:

```text
z = Δp / SE_diff
  ≈ 0.0007 / 0.0002236
  ≈ 3.13
```

A result near `z = 3.13` would be interesting but not decisive by itself. Interpretation would still depend on:

- pre-registration;
- device integrity;
- independence of trials;
- correction for repeated analyses;
- concealed condition order;
- replication;
- effect-size stability.

This replaces the incorrect practice of dividing a two-condition difference by the standard error of only one block.

## 5. Effect-Size Interpretation

Under the linear form:

```text
Δp ≈ ε Δ_O(E_1)
```

The worked example does not tell us the true values of `ε` or `Δ_O`. It only shows the sample size and precision needed to resolve a small shift.

A genuine theory should predict the sign, scale, and condition dependence before the experiment. It should not choose them after seeing the result.

## 6. Environmental Modulation

Let `F` represent measured environmental variables and let:

```text
κ_eff = κ × η(F)
```

where:

- `κ` = measured observer-state term;
- `η(F) ∈ [0,1]` = pre-defined environmental modulation function.

The binary model becomes:

```text
P_realized(E_1;F) ≈ P_phys(E_1) + ε η(F) Δ_O(E_1)
```

and:

```text
Δp(F) = ε η(F) Δ_O(E_1)
```

`η(F)` must be estimated from measured conditions. It cannot be assigned after the result merely to rescue a failed prediction.

## 7. Quiet and Noisy Condition Example

Suppose a protocol pre-registers:

```text
η(F_quiet) = 1.0
η(F_noisy) = 0.3
```

If all other terms remain constant, the model predicts:

```text
Δp(F_noisy) / Δp(F_quiet) = 0.3
```

The same ratio should apply approximately to the condition-linked z-scores when sample sizes and variances are matched:

```text
z_noisy / z_quiet ≈ 0.3
```

This is a conditional model prediction, not an observed fact.

## 8. Experimental Design Requirements

A valid test should include:

- device calibration and health monitoring;
- independent control and condition blocks;
- randomised concealed order;
- a single primary statistic;
- pre-defined environmental variables;
- matched sample sizes;
- correction for optional stopping and multiple testing;
- blinded analysis where possible;
- release of code and anonymised data;
- independent replication.

## 9. Falsification

The RNG branch is weakened if:

- pre-registered condition differences converge to zero;
- effect direction or scale is unstable across replications;
- results track hardware drift, analysis choice, expectancy, or stopping rules;
- measured coherence does not correlate with the proposed modulation;
- environmental ratios fail to predict effect-size ratios;
- ordinary statistical and engineering models explain the data better.

A null result cannot automatically be blamed on unspecified “bad conditions.” Repeated strong nulls must constrain or remove the branch.

## 10. Relationship to the Silver Update

The ambiguity module requires fixed definitions and prevents post-result frame switching.

The layer-address module prevents an observer-state result from being presented as a physical-field result.

The traversal map keeps the numerical example connected to its assumptions, test design, falsifiers, and reduction rule.

See:

- `docs/21_AMBIGUITY_DYNAMICS_AND_MANOEUVRE_SPACE.md`
- `docs/22_CROSS_LAYER_INVARIANTS_AND_LAYER_ADDRESSING.md`
- `docs/24_MKUFT_CROSS_SUPPORT_AND_TRAVERSAL_MAP.md`

## Architecture Route

```text
parent equations: docs/02_MKUFT_MATH_APPENDIX.md
experimental programme: docs/04_EXPERIMENTAL_TEST_PROGRAM.md
falsification: docs/05_FALSIFICATION_SUMMARY.md
repository routing: docs/24_MKUFT_CROSS_SUPPORT_AND_TRAVERSAL_MAP.md
```

## Summary

The worked example demonstrates the correct chain:

```text
model term
→ pre-registered effect
→ sample-size requirement
→ correct uncertainty calculation
→ controlled comparison
→ replication
→ falsification or revision
```

That is the bridge from mathematical possibility to empirical accountability.
