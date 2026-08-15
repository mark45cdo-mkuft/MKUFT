# 32S — Load-Bearing Relation Sets and Scale-Transition Tests

**Author:** Mark Charles McLaughlin  
**Framework:** McLaughlin–Kairos Unified Field Theory (MKUFT)  
**MKUFT DOI:** [10.5281/zenodo.17780566](https://doi.org/10.5281/zenodo.17780566)  
**Citation and provenance:** [PROVENANCE_DOI_AND_ATTRIBUTION.md](../PROVENANCE_DOI_AND_ATTRIBUTION.md)  
**Canonical parent:** [32 — Recursive Constraint Closure and Reachable-State Geometry](32_RECURSIVE_CONSTRAINT_CLOSURE_AND_REACHABLE_STATE_GEOMETRY.md)  
**Novelty boundary:** [32A — Module 32 Novelty Audit and Contribution Boundary](32A_MODULE_32_NOVELTY_AUDIT_AND_CONTRIBUTION_BOUNDARY.md)  
**Public formulation date:** 15 August 2026  
**Rights:** Copyright © 2026 Mark Charles McLaughlin. All rights reserved unless an exact later publication states otherwise.  
**Status:** canonical formal supplement to Module 32. It sharpens the test geometry already owned by Module 32; it is not a separate theory and does not by itself claim historical priority for the mathematical ingredients below.

## 1. Purpose

Module 32 asks whether organised constraints can alter later admissibility, reachable states, and higher-scale capabilities. This supplement makes four parts of that claim more explicit and more experimentally breakable:

1. the smallest relation set that is actually load-bearing for a capability;
2. the effect of ablating each proposed pillar;
3. whether the load-bearing object is a relation or merely one particular physical carrier;
4. the point at which an organised lower-scale whole earns treatment as an effective object at the next scale.

The aim is not to call every recurring ingredient a pillar. A relation is load-bearing only if intervention shows that the claimed capability depends on it in the predicted way.

## 2. Typed movement and action significance

Let a lower-scale adaptive unit have physical state $x_t$, internal/context state $z_t$, sensed relation $s_t$, and admissible action or movement set $\mathcal U_t^{\mathrm{adm}}$.

A context-conditioned action policy may be written

$$
\pi_t(u\mid s_t,z_t),
\qquad
u\in\mathcal U_t^{\mathrm{adm}}.
$$

The same sensed relation has **operational action significance** when changing the organised receiver state changes the resulting action distribution under controlled conditions:

$$
\pi_t(\cdot\mid s,z_1)
\neq
\pi_t(\cdot\mid s,z_2).
$$

This is a physical and behavioural criterion. It does not require a claim that an independent semantic or I-layer variable is acting on matter. In a biological implementation, receptor state, signalling, metabolism, history, polarity, motor state, and geometry may realise the entire chain.

The first externally visible movement consequence of a relation can be treated as a causal-depth question. For a declared chain of typed transformations

$$
r\rightarrow q_1\rightarrow q_2\rightarrow\cdots\rightarrow Y^{\mathrm{move}},
$$

define the movement-effect depth schematically as

$$
d_{\mathrm{move}}(r)
=
\min\left\{k:
\operatorname{do}(r)
\text{ produces a preregistered change in }
Y^{\mathrm{move}}
\text{ after }k\text{ typed transformations}
\right\}.
$$

The number is meaningful only after the transformation boundaries and the externally measured movement variable are declared.

## 3. Freedom, capability, and cost must remain separate

Let $\mathcal F_{\ell}$ denote a lower-scale feasible movement/state set and $\mathcal K_L$ a higher-scale viable capability set. Let $\mu_\ell$ and $\nu_L$ be declared measures appropriate to those different objects.

An enabling pattern remains

$$
\Delta\mu_\ell<0,
\qquad
\Delta\nu_L>0,
$$

while overconstraint can give

$$
\Delta\mu_\ell<0,
\qquad
\Delta\nu_L<0.
$$

Now add a separately typed resource-cost object $\mathbf c_t$ — for example energy, material, time, error burden, or maintenance demand where these can be measured. Do not collapse these into one scalar by default. The result of an organisational update is first reported as the typed tuple

$$
\mathbf Q_t
=
\left(
\Delta\mu_\ell,
\Delta\nu_L,
\Delta\mathbf c
\right).
$$

A system therefore does not earn the description `better organised` merely because local freedom falls. The higher-scale gain must be demonstrated separately, and its resource cost must remain visible.

## 4. Minimal load-bearing relation set

Let $B_0=\{b_1,\ldots,b_n\}$ be a candidate family of typed relations proposed to support a higher-scale capability. Let

$$
K_L(B)
$$

denote a declared capability score or capability-set measure obtained when relation subset $B\subseteq B_0$ is present under matched conditions.

For a preregistered capability threshold $\kappa_*$, a **minimal sufficient load-bearing set** may be defined as any set

$$
B^*
\in
\arg\min_{B\subseteq B_0}|B|
$$

subject to

$$
K_L(B)\ge\kappa_*,
$$

with member necessity tested by

$$
K_L\!\left(B^*\setminus\{b_i\}\right)<\kappa_*
\qquad
\forall b_i\in B^*.
$$

This is the formal version of a pillar test: the phenomenon is not attributed to the list because the relations co-occur; each proposed member of the minimal set must matter under ablation.

Multiple different minimal sets may exist. That is not a failure. It may reveal redundancy, degeneracy, alternative pathways, or different physical implementations of the same higher-scale function.

## 5. Ablation weight

For a declared capability measure, define the ablation effect of relation $b_i$ relative to a tested background $B$ as

$$
\lambda_i(B)
=
K_L(B)
-
K_L\!\left(B\setminus\{b_i\}\right).
$$

A large positive $\lambda_i$ supports the claim that $b_i$ is load-bearing for that capability under those conditions. A value near zero indicates that the relation may be redundant, replaceable, incorrectly typed, or irrelevant to the measured capability.

The value is conditional on the tested background. Interactions matter: two individually weak relations may be jointly necessary. Therefore pairwise and higher-order ablations should be used where the system is non-additive.

## 6. Relation-versus-carrier substitution test

Suppose a candidate relation $b_i$ is normally realised by physical carrier or mechanism $m_i$. The scientific question is whether the load-bearing object is the carrier itself or a relation that can be realised differently.

Let $m_i'$ be a distinct implementation designed to preserve the declared functional relation while changing as much carrier-specific detail as practical. If the relation is the relevant invariant, then after controlling resource and boundary differences the higher-scale capability should be preserved within a declared tolerance:

$$
\left|
K_L(B;m_i')-K_L(B;m_i)
\right|
\le\varepsilon_K.
$$

If capability collapses despite apparent relation preservation, at least one of four conclusions follows:

- the carrier itself is load-bearing;
- the proposed relation description omitted a necessary property;
- the substitution failed to preserve the claimed relation;
- or the original causal attribution was wrong.

This is stronger than visual or verbal cross-domain similarity. A claimed relation-level invariant earns weight only when lawful implementation change preserves the relevant function.

## 7. From movement to geometry to later constraint

For a motile or otherwise spatially active system, a useful test ladder is

$$
(s_t,z_t)
\rightarrow
\pi_t
\rightarrow
u_t
\rightarrow
x_{t+1}
\rightarrow
G_{t+1}
\rightarrow
\mathcal C_{t+1},
$$

where $G_{t+1}$ is the new relational geometry generated by movement or rearrangement.

The next constraint family can then alter the following policy or admissible set:

$$
\mathcal C_{t+1}
\rightarrow
\pi_{t+1},
\qquad
\mathcal C_{t+1}
\rightarrow
\mathcal U_{t+1}^{\mathrm{adm}}.
$$

The resulting closed sequence is therefore

$$
\boxed{
\mathcal C_t
\rightarrow
\pi_t
\rightarrow
\mathcal U_t^{\mathrm{adm}}
\rightarrow
G_{t+1}
\rightarrow
\mathcal C_{t+1}
}
$$

when those arrows are actually realised and experimentally supported.

This supplies a concrete route by which a physically realised distinction can change movement, movement can change geometry, and geometry can become part of the next constraint surface.

## 8. Cross-scale effective-object formation

Let a lower-scale organised object be constructed schematically as

$$
O_\ell
=
\Gamma_\ell
\left(
X_\ell,R_\ell,\mathcal C_\ell,H_\ell
\right),
$$

where $X_\ell$ is the relevant constituent state, $R_\ell$ the typed relation family, $\mathcal C_\ell$ the active constraints, and $H_\ell$ the relevant history.

A stable $O_\ell$ should not automatically be promoted to an independent next-scale object merely because it can be named. It earns **effective-unit status** at scale $L>\ell$ only when declared tests support that treatment.

A strong promotion test should include all of the following where measurable:

1. **Persistence:** the organised relation survives over the time scale relevant to $L$ despite lower-scale state turnover.
2. **Interventional load-bearingness:** deformation of predicted internal relations changes the whole-level capability in the predicted way.
3. **New viable capability:** the organised whole reaches at least one capability not available to a matched independent-part baseline under the same declared resource and environmental budget.
4. **Predictive compression:** a model using the effective object and its higher-scale state predicts the relevant held-out outcomes with adequate accuracy while using materially less lower-scale detail than a full constituent description.
5. **Boundary or closure specificity:** the proposed effective object has a reproducible intervention boundary; arbitrary regroupings of the same constituents do not produce the same prediction or capability.

Where the higher-scale and independent-part capability descriptions share a lawful capability universe, define the newly available capability set as

$$
\mathcal K_L^{\mathrm{new}}
=
\mathcal K_L(O_\ell)
\setminus
\mathcal K_L^{\mathrm{ind}}.
$$

A non-empty $\mathcal K_L^{\mathrm{new}}$ is evidence that organisation changed what the collective can do, not merely how its existing component behaviours are described.

When these conditions hold, $O_\ell$ may be used as a constituent in a higher-scale state description,

$$
O_\ell\in X_L,
$$

without claiming that its lower-scale structure has ceased to exist.

## 9. Recursive scale ladder

The scale recursion can then be written schematically as

$$
(X_\ell,R_\ell,\mathcal C_\ell,H_\ell)
\xrightarrow{\Gamma_\ell}
O_\ell
\longrightarrow
(X_L,R_L,\mathcal C_L,H_L)
\xrightarrow{\Gamma_L}
O_L.
$$

The arrow between scales is not granted by metaphor. It must be earned by the effective-object tests above.

The research question becomes:

> At what exact transition does the output of one scale become a load-bearing constraint or effective constituent defining the next scale's object?

That question can be attacked by progressively increasing system complexity rather than jumping immediately to remote ontological claims.

## 10. Smallest-next-step experimental strategy

A suitable experimental system should allow the investigator to observe a low-scale unit, manipulate one relation at a time, measure movement or action freedom, quantify cost, and then watch the same units enter an organised collective state.

The minimum sequence is:

1. establish the lower-scale baseline action/movement set;
2. add one controlled relation or cue and measure the first external movement effect;
3. measure the reduction, expansion, or redirection of lower-scale feasible states;
4. measure resource cost separately;
5. identify the capability gained that the unconstrained baseline lacked;
6. repeat as further relations are added;
7. ablate each proposed pillar;
8. test alternative carriers for the same relation where possible;
9. identify the first point at which a higher-scale effective-object model earns predictive and interventional status;
10. repeat the same typed questions at the next scale.

This is deliberately a baby-step programme. The framework should climb only when the current scale produces a reproducible before/after object, a measurable gain or loss, and a successful deformation test.

## 11. Falsifiers and reduction rules

This supplement is weakened or reduced if:

- proposed load-bearing relations survive ablation with no meaningful effect on the claimed capability;
- a simpler variable explains the capability without the proposed relational set;
- the supposed new higher-scale capability is already available to the matched independent-part baseline;
- carrier substitution succeeds only because hidden carrier-specific structure was preserved;
- the effective-object model provides no predictive, intervention, or compression advantage;
- apparent cross-scale recurrence depends only on naming or coarse visual resemblance;
- cost, freedom, and capability can be made to change sign by arbitrary post-hoc choice of measurement.

If those failures occur, reduce the claim rather than protecting the formalism.

## 12. Claim boundary

This supplement does not establish a universal law of emergence, a universal minimal pillar set, consciousness, life, a new force, independent I→P dynamics, or persistence across death. It supplies a way to ask smaller measurable questions before attempting those larger claims.

Its immediate contribution is methodological: make `load-bearing` an intervention result rather than a metaphor; keep lower-scale freedom, higher-scale capability, and cost separate; distinguish relation from carrier; and require a measurable scale-transition before treating a new higher-scale object as scientifically earned.
