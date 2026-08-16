# MKUFT Mathematical Appendix

**Author:** Mark Charles McLaughlin  
**Framework:** McLaughlin–Kairos Unified Field Theory (MKUFT)  
**MKUFT DOI:** [10.5281/zenodo.17780566](https://doi.org/10.5281/zenodo.17780566)  
**Citation and provenance:** [PROVENANCE_DOI_AND_ATTRIBUTION.md](../PROVENANCE_DOI_AND_ATTRIBUTION.md)

**Status:** mathematical backbone for the public MKUFT working canon.

## A1. Substrate as measure space

The substrate scaffold is represented as a measure space,

```math
S=(\Omega,\Sigma,\mu),
```

where $\Omega$ is a set of possible configurations, $\Sigma$ a sigma-algebra of measurable subsets, and $\mu$ a baseline measure, weight, or propensity.

The scaffold becomes a probability space only when

```math
\mu(\Omega)=1.
```

The substrate is not directly observed. This is a mathematical representation of structured possibility rather than evidence that a separate material medium has been detected.

## A2. Information structures

Because $I$ names the information layer, the mathematical function space is denoted by

```math
\mathcal I=L^2(\Omega,\mu).
```

An element $i\in\mathcal I$ represents one candidate information structure over the substrate. Such structures may encode patterns, constraints, correlations, and proto-physical forms.

For event $E$, define

```math
\mathcal I_E\subseteq\mathcal I
```

as the set of information structures compatible with $E$ under the active model.

## A3. Physical dynamics

The physical layer supplies an accepted dynamical contribution,

```math
P_{\mathrm{phys}}(E),
```

interpreted as a probability, probability density, or other prediction from the relevant established physical model. The mathematical type must be declared for the active event space.

## A4. Observer system and coherence functional

Let the observer state be $\rho_O$. A bounded observer-state coherence functional may be written

```math
\kappa:\mathrm{States}(\mathcal H_O)\rightarrow[0,1].
```

High $\kappa$ denotes lower measured internal noise or contradiction according to a predefined proxy. The functional is not fixed to one measurement method and requires operational definition in each experiment.

## A5. Integral realisation scaffold

For event $E$, define the unnormalised working weight

```math
\widetilde W(E)
=
\int_{i\in\mathcal I_E}
D_{\mathrm{phys}}(E\mid i)
W_{SI}(i\mid S,E)
C_O(O\mid i,E)
\,d\nu(i),
```

where $D_{\mathrm{phys}}(E\mid i)$ is the accepted physical contribution conditioned on information structure $i$, $W_{SI}(i\mid S,E)$ a candidate substrate-to-information weighting, $C_O(O\mid i,E)$ a bounded observer-condition term, and $\nu$ a measure over compatible information structures.

Where the expression is used as a probability weight, the integrand must be non-negative and the normalisation finite.

For a discrete event space $\mathcal E$,

```math
P_{\mathrm{realized}}(E)
=
\frac{\widetilde W(E)}{Z},
```

with

```math
Z
=
\sum_{E'\in\mathcal E}\widetilde W(E').
```

For a continuous event space, the sum is replaced by an integral over a declared event-space measure.

This is a theoretical scaffold. It becomes empirical only when its terms are independently operationalised.

## A6. Reduction to standard physics

If the observer term is constant,

```math
C_O(O\mid i,E)=C_0,
```

that constant cancels under normalisation. Standard-physics recovery additionally requires the substrate-to-information weighting and compatible-structure integral to reproduce, or reduce to, the accepted physical distribution:

```math
P_{\mathrm{realized}}(E)
\approx
P_{\mathrm{phys}}(E)
```

within a declared regime, comparison norm, and tolerance.

Failure to recover the ordinary limit is a failure of the physics-facing model.

## A7. Linear-response approximation

A small observer-linked term may be written

```math
C_O(O\mid i,E)
=
C_0\left[1+\varepsilon g_O(i,E)\right],
```

with

```math
C_0>0,
\qquad
\left|\varepsilon g_O(i,E)\right|<1
```

throughout the tested domain so that the weight remains positive.

After consistent expansion of numerator and normalisation, a first-order form may be written

```math
P_{\mathrm{realized}}(E)
\approx
P_{\mathrm{phys}}(E)+\varepsilon\Delta_O(E).
```

The sign, scale, and form of $\Delta_O$ must be specified before a confirmatory test, and neglected higher-order terms must remain bounded.

## A8. Coherence-linked modulation

One candidate form is

```math
C_O(O\mid i,E)
=
C_0\left[1+\varepsilon\kappa(\rho_O)h(i,E)\right],
```

where $\kappa$ measures the selected observer-state proxy and $h$ specifies a predefined interaction with event structure. Positivity must hold throughout the tested domain.

Low, irrelevant, or experimentally unsupported $\kappa$ should return the model toward the standard-physics limit.

## A9. Environmental damping

Let $F_{\mathrm{env}}$ denote measured environmental parameters such as electromagnetic noise, geomagnetic indices, geometry, shielding, vibration, temperature, or preregistered material composition.

A simplified form is

```math
\kappa_{\mathrm{eff}}
=
\kappa(\rho_O)\,\eta(F_{\mathrm{env}}),
```

with

```math
\eta(F_{\mathrm{env}})\in[0,1].
```

$\eta$ must be specified or estimated from measurements rather than assigned retrospectively to rescue a null result.

## A10. Group coherence

For observers $\{O_1,\ldots,O_N\}$,

```math
\kappa_{\mathrm{group}}
=
\Phi(\kappa_1,\ldots,\kappa_N,C_{\mathrm{corr}}),
```

where $C_{\mathrm{corr}}$ represents measured alignment or correlation and the range of $\Phi$ must be declared.

A simple bounded candidate approximation is

```math
\kappa_{\mathrm{group}}
=
A_{\mathrm{align}}
\frac{1}{N}\sum_{i=1}^{N}\kappa_i,
```

with

```math
A_{\mathrm{align}}\in[0,1],
\qquad
\kappa_i\in[0,1].
```

Group coherence is a coupled O/I/P condition rather than a fifth ontological layer.

## A11. Experimental connections

Candidate application classes include REG/RNG condition comparisons, strictly blinded remote-information protocols, preregistered co-occurrence studies, environmental modulation tests, and group-alignment tests.

These are proposed tests rather than established confirmations.

## A12. Ambiguity volume

A quantitative ambiguity space belongs to one declared domain $d$ with state space $\mathcal X_d$ and explicit encoding.

At time $t$, define

```math
\Omega_t^{(d)}
=
\left\{z\in\mathcal X_d:
 z\text{ remains compatible with }E_t\text{ and }C_t\right\},
```

where $E_t$ is available evidence and $C_t$ the active constraint set.

Let $\mu_d$ be a domain-specific measure and $\mu_{0,d}$ a reference measure. Define

```math
A_{t,\mathrm{vol}}^{(d)}
=
\log\!\left(1+\frac{\mu_d(\Omega_t^{(d)})}{\mu_{0,d}}\right).
```

This quantity is dimensionless. States, paths, interpretations, identities, and hypotheses cannot be placed into one measured set unless a common encoding has been defined.

Let

```math
R_t\in[0,1],
\qquad
X_t\in[0,1]
```

be normalised low-cost route connectivity and preserved access respectively. The working manoeuvrability index is

```math
M_t=A_{t,\mathrm{vol}}^{(d)}R_tX_t.
```

$M_t$ is a heuristic multiplicative audit index rather than a validated universal law. The product form should be compared with additive, interaction, and nonlinear alternatives.

See [Ambiguity Dynamics and Manoeuvre Space](21_AMBIGUITY_DYNAMICS_AND_MANOEUVRE_SPACE.md).

## A13. Cross-layer address map

Let $K$ be a candidate invariant and $L\in\{S,I,P,O\}$ the active layer. Let $\theta_L$ denote layer-specific constraints, observables, units, noise terms, and admissible transitions.

```math
K_L=A_L(K;\theta_L).
```

$A_L$ is an address map, not a new ontology.

A valid address map preserves the defining relation of $K$, explicit variable changes, layer-appropriate evidence, independent falsifiers, and a stated coupling where cross-layer influence is claimed.

Repeated algebraic form across layers does not establish the same physical mechanism. Formal cross-layer work therefore declares typed spaces and couplings, for example

```math
C_{LM}:\mathcal X_L\rightarrow\mathcal X_M.
```

See [Cross-Layer Invariants and Layer Addressing](22_CROSS_LAYER_INVARIANTS_AND_LAYER_ADDRESSING.md) and [Typed Traversal and Equation Hygiene](27_TYPED_TRAVERSAL_AND_EQUATION_HYGIENE.md).

## A14. Agency accessibility

Let $U_t$ be the actions actually available and $\widehat U_t$ the actions perceived as available. Let

```math
G_t(u;T_t,H_t)\in[0,1],
\qquad
\theta_{\mathrm{access}}\in[0,1],
```

where $T_t$ represents perceived threat and $H_t$ reinforcement history.

The practically accessible set is

```math
U_t^{\mathrm{access}}
=
\left\{u\in U_t:G_t(u;T_t,H_t)>\theta_{\mathrm{access}}\right\}.
```

Let $a_t\in[0,1]$ represent practical accessibility:

```math
\mathrm{Agency}_{\mathrm{effective}}(t)
=
\mathrm{Agency}_{\mathrm{capacity}}\,a_t.
```

This is an operational distinction rather than a moral, legal, or clinical equation.

See [Agency Accessibility and Capture Geometry](23_AGENCY_ACCESSIBILITY_AND_CAPTURE_GEOMETRY.md).

## A15. Path cost and weighting

For a trajectory $\gamma$ in one declared state space, a candidate path cost is

```math
C[\gamma]
=
\int_{\gamma}\lambda(x)\,ds.
```

The path element $ds$, local cost $\lambda$, and resulting units must be declared. This integral cannot be applied across incompatible S, I, P, and O spaces without a typed common construction.

A Gibbs-like path weighting requires a dimensionless exponent. Using a dimensionless normalised cost $\widetilde C[\gamma]$,

```math
P(B\mid A)
=
\frac{1}{Z_A}
\sum_{\gamma\in\Gamma(A\to B)}
\exp\!\left[-\widetilde C[\gamma]\right].
```

Alternatively, with inverse cost scale $\beta$,

```math
P(B\mid A)
=
\frac{1}{Z_A}
\sum_{\gamma\in\Gamma(A\to B)}
\exp\!\left[-\beta C[\gamma]\right],
```

where

```math
Z_A
=
\sum_{B'}
\sum_{\gamma\in\Gamma(A\to B')}
\exp\!\left[-\beta C[\gamma]\right].
```

Path multiplicity and cost are candidate predictors rather than a universal definition of probability.

## A16. Reduction rules

- If $R_t$ or $X_t$ is negligible, high ambiguity does not imply high manoeuvrability.
- If one layer address fails, evidence from another address cannot conceal the failure.
- If perceived and actual action sets do not differ, the agency-accessibility mechanism is unnecessary.
- If simpler noise, incentive, habit, uncertainty, or standard physical models perform better, they remain the preferred explanation.
- A mathematical expression is not evidence merely because it can be written.
- A tuple, projection, or named update map does not prove that its component spaces or couplings have been derived.

## A17. Related public documents

- [MKUFT Core Extended](01_MKUFT_CORE_EXTENDED.md)
- [Standalone Formal Addendum](03_STANDALONE_FORMAL_ADDENDUM.md)
- [Experimental Test Programme](04_EXPERIMENTAL_TEST_PROGRAM.md)
- [Worked Examples: RNG and Environment](14_WORKED_EXAMPLES_RNG_AND_ENVIRONMENT.md)
- [Falsification Summary](05_FALSIFICATION_SUMMARY.md)
- [Typed Traversal and Equation Hygiene](27_TYPED_TRAVERSAL_AND_EQUATION_HYGIENE.md)
- [Cross-Support and Traversal Map](24_MKUFT_CROSS_SUPPORT_AND_TRAVERSAL_MAP.md)

## Notation

The symbols $I$, $\mathcal I$, and $i$ are kept distinct for the information layer, information-function space, and one information structure respectively. Domain-qualified symbols are used where an unqualified symbol would hide incompatible spaces.
