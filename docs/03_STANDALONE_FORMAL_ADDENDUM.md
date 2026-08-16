# MKUFT — Standalone Formal Addendum

**Author:** Mark Charles McLaughlin  
**Framework:** McLaughlin–Kairos Unified Field Theory (MKUFT)  
**MKUFT DOI:** [10.5281/zenodo.17780566](https://doi.org/10.5281/zenodo.17780566)  
**Citation and provenance:** [PROVENANCE_DOI_AND_ATTRIBUTION.md](../PROVENANCE_DOI_AND_ATTRIBUTION.md)

## Mathematical Formalisation, Falsifiability, and Experimental Pathways

**Status:** public formal addendum.  
**Relationship to core:** sharpens and operationalises the core without replacing the DOI-linked source work.

The mathematical objects below are working models. They are not established physical laws merely because they are written formally.

## 1. Purpose

This addendum formalises constrained state and transition structure, defines traversal cost, connects path availability to candidate probability models, states explicit falsifiers, incorporates Silver Update structures, and preserves typed distinctions among physical space, abstract state space, and cross-layer address.

No new entity or ontology is established by this document.

## 2. Architectural premise

MKUFT tests whether geometry, relation, boundary, and constraint help determine which states are stable, which transitions are admissible, what transitions cost, and what outcomes persist.

The claim is not that all physical law has already been derived from MKUFT geometry. The narrower proposal is that constrained traversal provides a common modelling grammar that can be tested across layers.

A shared grammar does not establish one shared metric, unit system, or physical mechanism. Cross-layer traversal therefore uses typed maps rather than treating S, I, P, and O as ordinary spatial axes.

## 3. Constrained state graph

Represent a modelled state structure as

```math
\mathcal G=(N,E_{\mathcal G}),
```

where $N$ is a set of stable or operationally distinguishable states and $E_{\mathcal G}$ a set of admissible transitions.

Whether $N$ is finite, countable, or continuous depends on the domain and discretisation. A node may represent an attractor, physical state, information state, role, address, or repeatable configuration. Nodes of different types cannot be combined quantitatively unless their common encoding and transition rules are declared.

## 4. Trajectories

A discrete trajectory is an ordered path,

```math
\gamma=(n_0\rightarrow n_1\rightarrow\cdots\rightarrow n_k).
```

For a continuous within-layer state space $\mathcal X_L$,

```math
\gamma_L:[0,1]\rightarrow\mathcal X_L.
```

A typed cross-layer route is instead a composable sequence,

```math
x_S
\xrightarrow{C_{SI}}x_I
\xrightarrow{C_{IP}}x_P
\xrightarrow{C_{PO}}x_O
\xrightarrow{C_{OS}}x'_S.
```

An information-graph edge is not automatically a physical path, and informational adjacency is not physical proximity.

Agency, interaction, and evolution may be analysed as movement through available state structure. This does not imply that genuinely new effective states can never emerge; any claimed state creation must be defined rather than assumed.

## 5. Traversal cost

For a trajectory within one declared state space, a candidate cost functional is

```math
C[\gamma]
=
\int_{\gamma}\lambda(x)\,ds,
```

where $\lambda(x)$ is a domain-specific local cost, friction, instability, contradiction, or gradient term and $ds$ is a path element belonging to the declared state space.

$\lambda$, $ds$, and $C[\gamma]$ require units or a clearly normalised dimensionless scale in any quantitative application. The integral cannot be applied across incompatible S, I, P, and O spaces without a typed common construction and measure.

Low $C[\gamma]$ indicates a comparatively accessible route under the selected model; high $C[\gamma]$ indicates greater resistance, instability, or lower admissibility.

## 6. Path-weight model

A Gibbs-like path weight requires a dimensionless exponent.

Using dimensionless normalised cost $\widetilde C[\gamma]$,

```math
P(B\mid A)
=
\frac{1}{Z_A}
\sum_{\gamma\in\Gamma(A\to B)}
\exp\!\left[-\widetilde C[\gamma]\right].
```

If $C[\gamma]$ carries units, introduce an inverse cost scale $\beta$:

```math
P(B\mid A)
=
\frac{1}{Z_A}
\sum_{\gamma\in\Gamma(A\to B)}
\exp\!\left[-\beta C[\gamma]\right],
```

with

```math
Z_A
=
\sum_{B'}
\sum_{\gamma\in\Gamma(A\to B')}
\exp\!\left[-\beta C[\gamma]\right].
```

Here $\Gamma(A\to B)$ is the modelled admissible path set and $\beta C[\gamma]$ is dimensionless.

This is a candidate model rather than a claim that fundamental probability is nothing but path density. It fails where accepted domain models predict better without the additional structure.

## 7. Learning and adaptation

Learning need not make every local segment cheaper pointwise. For a declared task or trajectory distribution $\mathcal T$, a cleaner hypothesis is

```math
\mathbb E\!\left[C_{t+1}[\gamma]\mid\gamma\sim\mathcal T\right]
<
\mathbb E\!\left[C_t[\gamma]\mid\gamma\sim\mathcal T\right]
```

on the relevant performance-cost profile.

Some local costs may rise as a system becomes more accurate, cautious, calibrated, or robust. The empirical question is whether the task-level profile improves against established learning models.

The narrower claim is that many learning curves can be modelled as changes in accessibility and cost over an existing or expanding state graph.

## 8. Experienced time

A working phenomenological hypothesis is that reported duration may covary with a dimensionless traversal-burden index $B_t$:

```math
\frac{T_{\mathrm{subj}}}{T_{\mathrm{clock}}}
=f(B_t)+\varepsilon_t,
```

or, for a declared local approximation,

```math
\frac{T_{\mathrm{subj}}}{T_{\mathrm{clock}}}
\approx1+\alpha B_t.
```

$T_{\mathrm{subj}}$ is reported or behaviourally inferred duration, $T_{\mathrm{clock}}$ measured clock duration, and $\alpha$ a fitted or preregistered coefficient.

This is a phenomenological model of experienced time, not evidence that physical time is generated by cognitive traversal cost.

## 9. Core falsifiability

### 9.1 Path structure

**Prediction:** path availability and cost improve outcome prediction beyond simpler baselines.  
**Failure condition:** they add no predictive value, or preferred outcomes occur independently of the defined path structure.

### 9.2 Learning

**Prediction:** practice changes measurable route cost, error, accessibility, or performance-cost trade-offs.  
**Failure condition:** the cost model performs worse than standard learning models and adds no useful discrimination.

### 9.3 Boundary-edge clustering

**Prediction:** some predefined anomaly classes cluster near measurable thresholds, gradients, or adjacency changes.  
**Failure condition:** no clustering survives selection-bias controls, exposure correction, and out-of-sample testing.

### 9.4 Measurement context

**Prediction:** measurement context changes routing or recorded statistics in ways specified before the test.  
**Failure condition:** no predicted context effect remains after accepted physical and statistical explanations.

## 10. Experimental pathways

Candidate tests include computational simulation of constrained graphs, learning-curve comparisons, threshold and boundary experiments, measurement-context studies, and preregistered anomaly-distribution analysis.

Each experiment requires declared domain variables, state space, baseline model, primary outcome, and failure condition.

## 11. Unresolved feasible regions

The resolved-state graph can be extended by the unresolved region still compatible with evidence and constraint.

For declared domain $d$,

```math
\Omega_t^{(d)}
=
\left\{z\in\mathcal X_d:
 z\text{ remains compatible with evidence and active constraints}\right\}.
```

Define

```math
A_{t,\mathrm{vol}}^{(d)}
=
\log\!\left(1+\frac{\mu_d(\Omega_t^{(d)})}{\mu_{0,d}}\right),
```

where $\mu_d$ is a domain-specific measure and $\mu_{0,d}$ a reference scale.

Let

```math
R_t\in[0,1],
\qquad
X_t\in[0,1]
```

represent normalised low-cost connectivity and preserved access. The heuristic manoeuvrability index is

```math
M_t=A_{t,\mathrm{vol}}^{(d)}R_tX_t.
```

The product is a joint-dependence hypothesis and should be compared with additive, interaction, and nonlinear alternatives.

See [Ambiguity Dynamics and Manoeuvre Space](21_AMBIGUITY_DYNAMICS_AND_MANOEUVRE_SPACE.md).

## 12. Layer addressing

Let $K$ be a candidate invariant, $L\in\{S,I,P,O\}$ the active layer, and $\theta_L$ the layer-specific constraints and observables.

```math
K_L=A_L(K;\theta_L).
```

A valid address identifies the invariant relation, active layer, changed variables and units, evidence required at that layer, any cross-layer coupling, and an independent falsifier.

Repeated algebraic form does not prove an identical mechanism across layers. Cross-layer claims therefore use typed maps such as

```math
C_{LM}:\mathcal X_L\rightarrow\mathcal X_M
```

rather than treating the layers as ordinary spatial dimensions.

See [Cross-Layer Invariants and Layer Addressing](22_CROSS_LAYER_INVARIANTS_AND_LAYER_ADDRESSING.md) and [Typed Traversal and Equation Hygiene](27_TYPED_TRAVERSAL_AND_EQUATION_HYGIENE.md).

## 13. Agency accessibility

Let

```math
G_t(u;T_t,H_t)\in[0,1],
\qquad
\theta_{\mathrm{access}}\in[0,1].
```

For actual action set $U_t$, the practically accessible subset is

```math
U_t^{\mathrm{access}}
=
\left\{u\in U_t:G_t(u;T_t,H_t)>\theta_{\mathrm{access}}\right\}.
```

A retained capacity may remain while access is degraded:

```math
\mathrm{Agency}_{\mathrm{effective}}(t)
=
\mathrm{Agency}_{\mathrm{capacity}}\,a_t,
\qquad
a_t\in[0,1].
```

This is an operational distinction rather than a complete moral, legal, or clinical equation.

See [Agency Accessibility and Capture Geometry](23_AGENCY_ACCESSIBILITY_AND_CAPTURE_GEOMETRY.md).

## 14. Integrity rule

A formal expression earns scientific value only where it improves discrimination, supports prediction, states a null result, survives ordinary explanations, keeps layer evidence separate, declares domains and units or normalisation, and can be revised or removed after failure.

A failed submodel cannot be protected by the breadth of the wider framework. A named operator, state tuple, projection, graph, or path integral does not supply the missing mechanism merely by existing in notation.

## 15. Related public documents

- [MKUFT Core Extended](01_MKUFT_CORE_EXTENDED.md)
- [Mathematical Appendix](02_MKUFT_MATH_APPENDIX.md)
- [Experimental Test Programme](04_EXPERIMENTAL_TEST_PROGRAM.md)
- [Falsification Summary](05_FALSIFICATION_SUMMARY.md)
- [Ambiguity Dynamics and Manoeuvre Space](21_AMBIGUITY_DYNAMICS_AND_MANOEUVRE_SPACE.md)
- [Cross-Layer Invariants and Layer Addressing](22_CROSS_LAYER_INVARIANTS_AND_LAYER_ADDRESSING.md)
- [Agency Accessibility and Capture Geometry](23_AGENCY_ACCESSIBILITY_AND_CAPTURE_GEOMETRY.md)
- [Typed Traversal and Equation Hygiene](27_TYPED_TRAVERSAL_AND_EQUATION_HYGIENE.md)
- [Cross-Support and Traversal Map](24_MKUFT_CROSS_SUPPORT_AND_TRAVERSAL_MAP.md)

## 16. Canon status

This document is a public formal expansion of MKUFT. It sharpens the current working canon while preserving the provenance and identity of the original DOI-linked material.
