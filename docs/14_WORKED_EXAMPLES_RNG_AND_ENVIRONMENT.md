# MKUFT Worked Examples — RNG Bias and Environmental Modulation

Author: Mark Charles McLaughlin

Status: cleaned worked-example appendix for the private MKUFT GitHub repository.

## Purpose

This document gives concrete worked examples showing how the MKUFT equations connect to measurable predictions.

The goal is to close the gap between theory and experiment.

Plain English:

If MKUFT is real science, it must say what should change in the world, not only sound interesting.

## 1. Realisation Equation

MKUFT defines the realised probability of an event E as:

```text
P_realized(E) = W_total(E) / Σ_{E'} W_total(E')
```

with unnormalised weight:

```text
W_total(E) = ∫ D_phys(E|I) W(I|S,E) C(O|I,E) dν(I)
```

Where:

- D_phys(E|I) = standard physical dynamics,
- W(I|S,E) = substrate-to-information weighting,
- C(O|I,E) = observer-coherence modulation,
- dν(I) = integration over compatible information structures.

## 2. Linear Observer Response

Observer modulation can be modelled in linear-response form:

```text
C(O|I,E) = C₀ [1 + ε κ(O) h(I,E)]
```

Where:

- κ(O) ∈ [0,1] is observer coherence,
- ε is a small coupling coefficient,
- h(I,E) encodes alignment between information structures and the targeted event.

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
W_total(E) = C₀ [ W_phys(E) + ε κ(O) ΔW_O(E) ]
```

The constant C₀ cancels under normalisation.

For small ε:

```text
P_realized(E) ≈ P_phys(E) + ε Δ_O(E)
```

Plain English:

Standard physics gives the baseline probability. Observer coherence adds only a small correction, and only if the system is sensitive enough.

## 3. Binary RNG Example

Let a binary random number generator have two outcomes:

```text
E1 = output “1”
E0 = output “0”
```

For a fair physical RNG:

```text
P_phys(E1) = 0.5
P_phys(E0) = 0.5
```

Under MKUFT, with high observer coherence:

```text
P_realized(E1) ≈ 0.5 + ε Δ_O(E1)
```

and:

```text
P_realized(E0) ≈ 0.5 - ε Δ_O(E1)
```

Plain English:

If the observer effect exists, the RNG should shift very slightly away from 50/50 during coherent intention phases.

## 4. Numerical Example

Suppose the RNG baseline proportion is:

```text
p_base = 0.503
```

During a high-coherence intention phase, suppose the observed proportion is:

```text
p_coh = 0.520
```

For:

```text
N = 1,000,000 trials
```

The standard error under p = 0.5 is:

```text
σ = sqrt(p(1-p)/N)
```

Approximating p = 0.5:

```text
σ ≈ sqrt(0.25 / 1,000,000) = 0.0005
```

The observed deviation is:

```text
Δp = p_coh - p_base = 0.017
```

The z-score is:

```text
z = Δp / σ = 0.017 / 0.0005 ≈ 34
```

A z-score around 34 would be extraordinarily significant if obtained in a clean, pre-registered, well-controlled experiment.

## 5. Interpretation

Within MKUFT:

```text
p_coh = p_phys + ε Δ_O(E1)
```

For this numerical example:

```text
ε Δ_O(E1) ≈ 0.017
```

This does not prove MKUFT by itself.

It shows what kind of measurable shift MKUFT would expect under high-coherence conditions.

## 6. Environmental Modulation

MKUFT predicts that environment matters.

Observer coherence is not isolated from physical conditions.

Define effective coherence:

```text
κ_eff = κ η(F)
```

Where:

- κ = intrinsic observer coherence,
- η(F) ∈ [0,1] = environmental damping function,
- F = environmental conditions such as EM noise, iron mass, geomagnetic state, or shielding.

## 7. RNG with Environmental Term

The binary RNG case becomes:

```text
P_realized(E1; F) ≈ P_phys(E1) + ε η(F) Δ_O(E1)
```

The anomaly magnitude is:

```text
Δp(F) = ε η(F) Δ_O(E1)
```

Plain English:

The same observer may produce different effect sizes in different environments because the environment changes how much coherence reaches the system.

## 8. Quiet vs Noisy Environment

Consider:

```text
F_Q = quiet environment, η(F_Q) ≈ 1
F_N = noisy environment, η(F_N) = 0.3
```

Then:

```text
Δp(F_Q) = ε Δ_O(E1)
```

and:

```text
Δp(F_N) = 0.3 ε Δ_O(E1)
```

The ratio is:

```text
Δp(F_Q) / Δp(F_N) ≈ 1 / 0.3 ≈ 3.3
```

## 9. z-Score Scaling

For a binomial process with baseline probability p₀ ≈ 0.5:

```text
σ ≈ 0.5 / sqrt(N)
```

Define:

```text
z_Q = Δp(F_Q) / σ
z_N = Δp(F_N) / σ
```

Then:

```text
z_Q / z_N = Δp(F_Q) / Δp(F_N) = 1 / η(F_N)
```

For:

```text
η(F_N) = 0.3
```

we get:

```text
z_Q / z_N ≈ 3.3
```

So if a quiet condition produces:

```text
z_Q ≈ 30–35
```

MKUFT predicts a noisy/damping condition might produce:

```text
z_N ≈ 9–11
```

assuming all other factors are held constant.

## 10. Experimental Meaning

This gives a laboratory-testable prediction.

Run matched RNG experiments under:

- quiet low-noise conditions,
- EM-noisy conditions,
- iron-rich conditions,
- shielded conditions,
- geomagnetically different windows.

Measure:

- Δp,
- z-scores,
- observer coherence κ,
- environmental damping proxy η(F).

Prediction:

The same observer and protocol should show stronger deviations in coherent/quiet conditions and weaker deviations in damping/noisy conditions.

## 11. Falsification

The environmental modulation equation is weakened or falsified if:

- matched environments show no systematic effect-size difference,
- noisy/damping environments do not suppress deviations,
- effect ratios do not track any plausible η(F),
- pre-registered high-N experiments produce no coherence-phase deviation above baseline.

## 12. Why This Matters

These examples matter because they turn MKUFT from broad theory into measurable prediction.

The framework says:

```text
observer coherence + sensitive system + low damping = small probability shift
```

and:

```text
same observer + same protocol + higher damping = reduced shift
```

That is testable.

If it fails repeatedly under clean conditions, the model must change or fall.

## 13. Summary

The RNG and environmental examples show the chain:

```text
MKUFT equation -> observer coherence -> probability shift -> environmental damping -> measurable z-score change
```

This is exactly the kind of bridge a serious theory needs: from concept to number, from number to experiment, from experiment to possible falsification.
