# MKUFT Worked Examples — RNG Bias and Environmental Modulation

**Author:** Mark Charles McLaughlin  
**Framework:** McLaughlin–Kairos Unified Field Theory (MKUFT)  
**MKUFT DOI:** [10.5281/zenodo.17780566](https://doi.org/10.5281/zenodo.17780566)  
**Citation and provenance:** [PROVENANCE_DOI_AND_ATTRIBUTION.md](../PROVENANCE_DOI_AND_ATTRIBUTION.md)

**Status:** public worked-example appendix.

## Purpose

This document illustrates how selected MKUFT equations could connect to measurable predictions. The numerical values are illustrative only; they are not observed results, expected effect sizes, or evidence for MKUFT.

A scientifically useful model must state what is measured, how uncertainty is calculated, and what result would count against it.

## 1. Realisation equation

For event $E$,

```math
P_{\mathrm{realized}}(E)
=
\frac{\widetilde W(E)}{\displaystyle\sum_{E'}\widetilde W(E')},
```

with unnormalised weight

```math
\widetilde W(E)
=
\int
D_{\mathrm{phys}}(E\mid i)
W_{SI}(i\mid S,E)
C_O(O\mid i,E)
\,d\nu(i).
```

$D_{\mathrm{phys}}$ represents accepted physical dynamics, $W_{SI}$ a candidate substrate-to-information weighting, $C_O$ a bounded observer-condition term, and $\nu$ a measure over compatible information structures.

The scaffold acquires empirical content only when each term is operationally defined for a specific experiment.

## 2. Linear-response form

A bounded observer term may be written

```math
C_O(O\mid i,E)
=
C_0\left[1+\varepsilon\kappa(O)h(i,E)\right],
```

where $\kappa(O)\in[0,1]$ is a measured coherence proxy, $\varepsilon$ a small coupling parameter, and $h(i,E)$ a prespecified event-structure interaction.

Define

```math
W_{\mathrm{phys}}(E)
=
\int
D_{\mathrm{phys}}(E\mid i)
W_{SI}(i\mid S,E)
\,d\nu(i),
```

and

```math
\Delta W_O(E)
=
\int
D_{\mathrm{phys}}(E\mid i)
W_{SI}(i\mid S,E)
h(i,E)
\,d\nu(i).
```

Then

```math
\widetilde W(E)
=
C_0\left[W_{\mathrm{phys}}(E)+\varepsilon\kappa(O)\Delta W_O(E)\right].
```

For sufficiently small $\varepsilon$, a testable first-order form is

```math
P_{\mathrm{realized}}(E)
\approx
P_{\mathrm{phys}}(E)+\varepsilon\Delta_O(E),
```

provided the normalisation is expanded consistently and higher-order terms remain bounded.

## 3. Binary RNG example

Let a binary random number generator produce outcomes $E_1$ and $E_0$. For a fair generator,

```math
P_{\mathrm{phys}}(E_1)
=
P_{\mathrm{phys}}(E_0)
=0.5.
```

A preregistered MKUFT test could compare two independent blocks: a baseline/control block and a coherence/intention block.

The null hypothesis is

```math
p_{\mathrm{control}}
=
p_{\mathrm{condition}}
=0.5.
```

The alternative is a small condition-linked difference whose direction and analysis are specified before data collection.

## 4. Correct two-proportion numerical example

Assume two independent blocks with

```math
N_{\mathrm{control}}
=N_{\mathrm{condition}}
=10{,}000{,}000.
```

Take illustrative proportions

```math
p_{\mathrm{control}}=0.5000,
\qquad
p_{\mathrm{condition}}=0.5007,
```

so

```math
\Delta p=0.0007.
```

For two independent proportions, the approximate standard error of the difference is

```math
SE_{\mathrm{diff}}
=
\sqrt{
\frac{p_{\mathrm{control}}(1-p_{\mathrm{control}})}{N_{\mathrm{control}}}
+
\frac{p_{\mathrm{condition}}(1-p_{\mathrm{condition}})}{N_{\mathrm{condition}}}
}.
```

Using the illustrative values,

```math
SE_{\mathrm{diff}}
\approx
\sqrt{
\frac{0.25}{10{,}000{,}000}
+
\frac{0.25}{10{,}000{,}000}
}
\approx0.0002236.
```

Therefore

```math
z
=
\frac{\Delta p}{SE_{\mathrm{diff}}}
\approx
\frac{0.0007}{0.0002236}
\approx3.13.
```

A result near $z=3.13$ would be interesting but not decisive by itself. Interpretation would still depend on preregistration, device integrity, independence of trials, correction for repeated analyses, concealed condition order, replication, and effect-size stability.

This calculation uses the uncertainty of the difference between two independent proportions rather than the standard error of only one block.

## 5. Effect-size interpretation

Under the linear model,

```math
\Delta p\approx\varepsilon\Delta_O(E_1).
```

The worked example does not determine the real values of $\varepsilon$ or $\Delta_O$. It illustrates the precision required to resolve a small shift.

A developed theory should predict sign, scale, and condition dependence before the experiment rather than choosing them after observing the result.

## 6. Environmental modulation

Let $F$ represent measured environmental variables and

```math
\kappa_{\mathrm{eff}}
=
\kappa\,\eta(F),
\qquad
\eta(F)\in[0,1].
```

The binary model becomes

```math
P_{\mathrm{realized}}(E_1;F)
\approx
P_{\mathrm{phys}}(E_1)
+
\varepsilon\eta(F)\Delta_O(E_1),
```

so

```math
\Delta p(F)
=
\varepsilon\eta(F)\Delta_O(E_1).
```

$\eta(F)$ must be specified or estimated from measured conditions rather than assigned after the result to rescue a failed prediction.

## 7. Quiet and noisy condition illustration

Suppose a protocol preregisters

```math
\eta(F_{\mathrm{quiet}})=1.0,
\qquad
\eta(F_{\mathrm{noisy}})=0.3.
```

If all other terms remain constant, the model predicts

```math
\frac{\Delta p(F_{\mathrm{noisy}})}
{\Delta p(F_{\mathrm{quiet}})}
=0.3.
```

When sample sizes and variances are matched, the condition-linked $z$ scores should show approximately the same ratio:

```math
\frac{z_{\mathrm{noisy}}}{z_{\mathrm{quiet}}}
\approx0.3.
```

This is a conditional model prediction, not an observed fact.

## 8. Experimental design requirements

A valid test should include device calibration and health monitoring, independent control and condition blocks, randomised concealed order, one primary statistic, predefined environmental variables, matched sample sizes, correction for optional stopping and multiple testing, blinded analysis where practical, release of code and anonymised data, and independent replication.

## 9. Falsification

The RNG branch is weakened if preregistered condition differences converge to zero; effect direction or scale is unstable across replications; results track hardware drift, analysis choice, expectancy, or stopping rules; measured coherence does not correlate with the proposed modulation; environmental ratios fail to predict effect-size ratios; or ordinary statistical and engineering models explain the data better.

A null result cannot automatically be attributed to unspecified adverse conditions. Repeated strong nulls must constrain or remove the branch.

## 10. Related public documents

- [Mathematical Appendix](02_MKUFT_MATH_APPENDIX.md)
- [Experimental Test Programme](04_EXPERIMENTAL_TEST_PROGRAM.md)
- [Falsification Summary](05_FALSIFICATION_SUMMARY.md)
- [Ambiguity Dynamics and Manoeuvre Space](21_AMBIGUITY_DYNAMICS_AND_MANOEUVRE_SPACE.md)
- [Cross-Layer Invariants and Layer Addressing](22_CROSS_LAYER_INVARIANTS_AND_LAYER_ADDRESSING.md)
- [Cross-Support and Traversal Map](24_MKUFT_CROSS_SUPPORT_AND_TRAVERSAL_MAP.md)

## Summary

The worked example demonstrates the scientific chain **model term → preregistered effect → sample-size requirement → correct uncertainty calculation → controlled comparison → replication → falsification or revision**.

That is the bridge from mathematical possibility to empirical accountability.
