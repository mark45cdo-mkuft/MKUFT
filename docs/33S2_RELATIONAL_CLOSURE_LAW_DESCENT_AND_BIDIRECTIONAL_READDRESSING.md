# 33S2 — Relational Closure, Law Descent, and Bidirectional Readdressing

**Author:** Mark Charles McLaughlin  
**Framework:** McLaughlin–Kairos Unified Field Theory (MKUFT)  
**MKUFT DOI:** [10.5281/zenodo.17780566](https://doi.org/10.5281/zenodo.17780566)  
**Citation and provenance:** [PROVENANCE_DOI_AND_ATTRIBUTION.md](../PROVENANCE_DOI_AND_ATTRIBUTION.md)  
**Architectural parent:** [33 — SIPO Capstone](33_SIPO_CAPSTONE_CONSTRAINT_CONDITIONED_ADDRESSED_UPDATE_LAW.md)  
**Interface parent:** [33S1 — Dynamic Interface Promotion](33S1_DYNAMIC_INTERFACE_PROMOTION_AND_RECURSIVE_BOUNDARY_CLOSURE.md)  
**Scale-transition parent:** [32S — Load-Bearing Relation Sets and Scale-Transition Tests](32S_LOAD_BEARING_RELATION_SETS_AND_SCALE_TRANSITION_TESTS.md)  
**Layer/address parent:** [26 — Layer Before Law](26_LAYER_BEFORE_LAW_MKUFT_QUANTUM_GRAVITY_REFRAMING.md)  
**Public formulation date:** 15 August 2026  
**Rights:** Copyright © 2026 Mark Charles McLaughlin. All rights reserved unless an exact later publication states otherwise.  
**Status:** canonical companion refinement of Modules 32S and 33. It separates token lineage, functional identity, relational closure, and whole-level law sufficiency; defines when a higher relational address is dynamically sufficient for a declared property; and requires bidirectional readdressing when that sufficiency changes. It does not claim a new quotient theorem, a universal emergence law, or evidence for an independent I→P mechanism.

## 1. Purpose

Modules 32S and 33 already permit an organised lower-scale system to earn treatment as a higher-scale effective object and require the active physical law object to be assembled at the addressed state. A remaining ambiguity is decisive:

> **When does a real higher-order functional object also possess a sufficiently autonomous law at that higher address, and for which property?**

A system can be a genuine organised whole while still requiring lower-scale variables to predict some of its behaviour. Conversely, a coarse-grained law may be highly predictive for one observable without establishing token identity, self-maintaining closure, or independence from lower-level physics.

This module therefore keeps four questions distinct:

1. **lineage** — which token or historical object is this?
2. **functional identity** — which relation makes it this kind of whole in the declared role and environment?
3. **closure** — how does that relation persist, remain enforced, or repair perturbation?
4. **law descent** — for which declared property does the lower dynamics support a sufficient higher-address transition law, at what strength and under which conditions?

Compressed rule:

> **Lineage identifies the token. Relation identifies the functional whole. Closure earns persistence. Law descent earns a higher-address law only for the property, regime, and strength actually demonstrated.**

## 2. Relational address

Let $X$ be a lower-address state space and let

$$
\pi_R:X\rightarrow Y
$$

map lower-level states into candidate higher-order relational states determined by a declared load-bearing relation $R$.

The map must be specified from the relevant relation, role/boundary, environment or input class, intervention class, resolution, and time horizon. It must not be chosen retrospectively merely because a particular partition produces a desired result.

Two lower states are equivalent at the candidate relational address when

$$
x\sim_R x'
\quad\Longleftrightarrow\quad
\pi_R(x)=\pi_R(x').
$$

$Y$ is then a candidate relational quotient address. It is not automatically an autonomous dynamical level.

### Token identity remains separate

Two systems may instantiate the same relational organisation while remaining different historical objects. Conversely, one token may preserve its functional organisation through substantial component turnover.

Where component membership changes, membership/topology belongs in the lower-address state or another explicit variable. Functional continuity may survive carrier replacement when lineage remains continuous and the load-bearing organisation is preserved to the declared tolerance.

> **Relational equivalence can establish functional type without erasing provenance.**

## 3. Closure is not correlation

A relation can be:

- externally imposed or hard constrained;
- engineered or contract enforced;
- dynamically self-restoring;
- mutually or organisationally maintained;
- statistical/effective;
- merely descriptive.

Correlation, synchrony, mutual information, repeated co-occurrence, or a visually stable pattern are not by themselves constitutive closure.

A closure claim requires a declared persistence, admissibility, maintenance, restoration, or fracture criterion. If perturbing the proposed relation does not change the declared whole-level identity, capability, admissible support, stability class, or response, the relation has not been shown to be load-bearing for that claim.

## 4. Strong deterministic law descent

Let the lower-address deterministic dynamics under matched control/intervention $u$ and environment $e$ be

$$
F_X:(X,u,e)\rightarrow X.
$$

A whole-state deterministic law

$$
F_Y:(Y,u,e)\rightarrow Y
$$

is well defined through $\pi_R$ when representatives of the same higher state have the same projected next higher state:

$$
\boxed{
\pi_R(x)=\pi_R(x')
\Rightarrow
\pi_R\!\left(F_X(x,u,e)\right)
=
\pi_R\!\left(F_X(x',u,e)\right)
}
$$

for the declared regime.

Where this holds,

$$
F_Y\circ\pi_R
=
\pi_R\circ F_X
$$

under the matched conditions.

This is standard quotient/congruence logic and is not claimed as a new theorem. Its role here is to make MKUFT scale promotion and addressed-law assembly explicit rather than verbal.

## 5. Property-relative law descent

Whole-level autonomy must not be granted with one global yes/no label.

Let

$$
q:Y\rightarrow Q
$$

be the declared target property or observable. It may represent, for example, stability, morphology, throughput, safety, liveness, position, response to intervention, or another addressed consequence.

For deterministic property-specific descent it is enough, to the declared tolerance, that

$$
\pi_R(x)=\pi_R(x')
\Rightarrow
q\!\left(\pi_R(F_X(x,u,e))\right)
\approx
q\!\left(\pi_R(F_X(x',u,e))\right).
$$

The same higher-order object may therefore support a sufficient law for one property while remaining irreducibly multiscale for another.

> **Do not ask only whether the whole has a law. Ask which property is lawful at that address.**

## 6. Stochastic and approximate descent

For a lower-address transition kernel over horizon $\Delta$,

$$
K_X^{\Delta}(\cdot\mid x,u,e),
$$

strong stochastic descent requires equality, or declared near-equality, of the pushed-forward higher-state transition distributions for lower representatives of the same higher state:

$$
\pi_R(x)=\pi_R(x')
\Rightarrow
\pi_{R*}K_X^{\Delta}(\cdot\mid x,u,e)
\approx
\pi_{R*}K_X^{\Delta}(\cdot\mid x',u,e).
$$

An approximate discrepancy can be declared as

$$
\epsilon_{\mathrm{strong}}(U,E,\Delta)
=
\sup_{x\sim_R x',\,u\in U,\,e\in E}
 d\!\left(
 \pi_{R*}K_X^{\Delta}(\cdot\mid x,u,e),
 \pi_{R*}K_X^{\Delta}(\cdot\mid x',u,e)
 \right),
$$

with a preregistered tolerance $\epsilon_*$. Strong approximate descent is supported only where

$$
\epsilon_{\mathrm{strong}}\leq\epsilon_*.
$$

For a property $q$, the same test is applied after push-forward into the property space $Q$ rather than falsely certifying every feature of $Y$.

## 7. Ensemble and history-augmented descent

A legitimate effective law need not be representative-independent for every microscopic realization.

Let

$$
\mu_y(dx\mid u,e)
$$

be an independently justified conditional preparation or maintained ensemble over lower states compatible with higher state $y$. A candidate ensemble-level higher kernel is

$$
K_Y^{\Delta}(\cdot\mid y,u,e)
=
\int_{\pi_R^{-1}(y)}
\pi_{R*}K_X^{\Delta}(\cdot\mid x,u,e)
\,\mu_y(dx\mid u,e).
$$

This is an **ensemble/conditional** law, not strong representative-independent descent. If materially different admissible preparations inside the same $y$ produce different macro futures, preparation is part of the address and must be retained or the address refined.

Failure of one-step Markov closure also does not automatically force a return to microscopic description. Test whether bounded higher-level history closes the process, for example

$$
Y_t^{+}=(Y_t,Y_{t-1},\ldots,Y_{t-k+1}).
$$

Unlimited history must not be used to hide unresolved lower-state dependence.

Where material, label the actual supported class:

- **strong/exact**;
- **strong/approximate**;
- **ensemble/conditional**;
- **history-augmented**;
- **coupled multiscale**.

## 8. Predictive versus interventional descent

A higher address can be sufficient for passive prediction yet fail when the system is deliberately acted upon.

Therefore distinguish:

- **predictive descent** — higher-state information is sufficient for the declared observational forecast;
- **interventional descent** — sufficiency survives the declared action/control/intervention class $U$.

If the higher address is used for control, diagnosis, policy, manipulation, or a causal claim, interventional descent is the relevant burden.

> **An address that survives observation may still fail when touched.**

## 9. Bidirectional readdressing

Scale/address promotion is not one-way.

If a load-bearing relation becomes constitutive and the declared property passes the relevant descent test, the active local law may be assembled at the higher/effective address for that property and regime. Lower-address laws remain physical substrate constraints; they are not erased.

If hidden representative dependence, preparation dependence, fracture, changed intervention class, changed timescale, or a new load-bearing variable destroys higher-address sufficiency, the model must readdress downward or into a coupled multiscale description.

The minimal logic is

$$
\boxed{
\text{lower address}
\rightleftarrows
\text{effective/higher address}
\rightleftarrows
\text{coupled multiscale address}
}
$$

with the direction earned by current evidence and target property.

### Asynchronous lead–lag is permitted

Coupled layers or scales need not readdress simultaneously. During a genuine transition, one addressed variable may move first while another remains temporarily in its previous regime.

A transient mismatch is not automatically failure. It is admissible only where a typed transition model predicts the lead–lag and the downstream variable subsequently resolves within the declared bounds. Otherwise the mismatch is evidence against the proposed transition route.

## 10. Closure margin versus law-descent margin

The organised whole can remain intact even after a formerly sufficient higher-level law becomes inadequate for a particular property.

Define separately:

$$
M_C
$$

for the perturbation margin to loss of the constitutive closure relation, and

$$
M_D(q)
$$

for the perturbation margin to loss of higher-address predictive/interventional sufficiency for property $q$.

No universal ordering is assumed. A regime with

$$
M_D(q)<M_C
$$

means that the whole still exists while the simpler higher-address law for $q$ has already failed.

This distinction prevents functional identity from being confused with dynamical autonomy.

## 11. Integration with the SIPO capstone

Module 33 writes the active physical law object as

$$
\mathfrak L_{P,t}
=
(\mathcal D_{P,t},\mathcal T_{P,t},\mathcal W_{P,t}).
$$

Module 33S2 adds a scale/address sufficiency condition before treating a promoted relational state as the owner of that law object for a declared property.

Schematically:

$$
\mathcal U_t,E_t
\rightarrow
\text{resolve lineage, relation, closure, scale and target }q
\rightarrow
\text{test descent class}
\rightarrow
\Xi_t
\rightarrow
\mathfrak L_{P,t}
\rightarrow
P_{t+\Delta},O_{t+\Delta}
\rightarrow
\text{readdress}.
$$

If higher-address descent is supported for $q$, $\Xi_t$ may use that higher/effective state at the demonstrated scope. If it is not supported, the complete addressed state must retain the lower or coupled-multiscale variables needed for $q$.

Thus:

> **Layer before law is strengthened into address before law ownership: construct the law at the coarsest address that has actually earned sufficiency for the property being propagated, while retaining the lower laws that physically realise it.**

## 12. Relationship to Module 33S1

Module 33S1 asks whether an interface $\mathcal J_{AB,t}$ must be promoted from bundled context into explicit recursive state because it is trackable, prospectively load-bearing, and recursively updated.

Module 33S2 asks a different question after such organisation exists:

> **Does the promoted relational object carry enough state to support the declared downstream law, or must lower/interface variables remain explicitly coupled?**

State-variable promotion therefore precedes, but does not guarantee, whole-level law descent.

## 13. Failure and reduction rules

A higher-address law claim must be reduced, refined, or returned to a coupled multiscale address when any of the following materially occurs:

1. lower representatives mapped to the same higher state produce incompatible futures for the claimed property beyond tolerance;
2. the result depends on an undeclared preparation, environment, intervention, history, resolution, or timescale variable;
3. a purported constitutive relation survives fracture without changing the declared whole-level consequence;
4. passive predictive sufficiency is used to justify an intervention/control claim that fails under matched actions;
5. bounded whole-level memory does not close the apparent higher dynamics and lower-state dependence remains material;
6. a transient cross-layer mismatch is not predicted by a typed lead–lag transition model;
7. the whole remains functionally real but $M_D(q)$ is crossed before $M_C$ and the simpler macro law is nevertheless retained;
8. a P-recoverable relational or interface variable is relabelled as an independent I variable without additional held-out/interventional evidence.

Reduction does not imply that the higher-order object was unreal. It means the claimed **law sufficiency for that property** was too strong.

## 14. Contribution boundary

This module does not claim invention of quotient dynamics, coarse-graining, lumpability, effective theories, state aggregation, closure, multiscale modelling, ensemble reduction, memory augmentation, or intervention testing.

The candidate MKUFT contribution is the operational conjunction:

> **separate lineage, relational functional identity, closure and property-specific dynamical sufficiency; require the strength of law descent to be named; use that result to decide which scale/address may supply the active Module 33 law object; permit lawful bidirectional and asynchronous readdressing; and distinguish loss of a property-specific macro law from loss of the organised whole itself.**

Historical priority for that exact conjunction is not asserted without broader review.

## 15. Compressed canonical rule

Precise form:

> **A relation can define a real higher-order functional object without making that object dynamically autonomous for every property. Promote law ownership only for a declared property whose lower dynamics descend through the relational address at a stated strength, preparation, intervention class, timescale and tolerance. Preserve lower-level laws as substrate constraints; if sufficiency fails, readdress downward or multiscale without denying the whole.**

Mnemonic:

> **Relation makes the whole; descent earns its law.**
