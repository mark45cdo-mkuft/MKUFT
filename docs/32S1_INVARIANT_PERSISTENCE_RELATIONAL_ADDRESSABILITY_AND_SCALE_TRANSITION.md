# 32S1 — Invariant Persistence, Relational Addressability, and Scale Transition

**Author:** Mark Charles McLaughlin  
**Framework:** McLaughlin–Kairos Unified Field Theory (MKUFT)  
**MKUFT DOI:** [10.5281/zenodo.17780566](https://doi.org/10.5281/zenodo.17780566)  
**Canonical parent:** [32S — Load-Bearing Relation Sets and Scale-Transition Tests](32S_LOAD_BEARING_RELATION_SETS_AND_SCALE_TRANSITION_TESTS.md)  
**Root owner:** [32 — Recursive Constraint Closure and Reachable-State Geometry](32_RECURSIVE_CONSTRAINT_CLOSURE_AND_REACHABLE_STATE_GEOMETRY.md)  
**Comparison owner:** [31 — Context-Conditioned State Comparison and Observability](31_CONTEXT_CONDITIONED_STATE_COMPARISON_AND_OBSERVABILITY.md)  
**Novelty boundary:** [32A — Module 32 Novelty Audit and Contribution Boundary](32A_MODULE_32_NOVELTY_AUDIT_AND_CONTRIBUTION_BOUNDARY.md)  
**Public formulation date:** 15 August 2026  
**Revision date:** 15 August 2026  
**Status:** canonical formal refinement. It sharpens the operational meaning of a scale transition and corrects a hidden fixed-self assumption in the first formulation. It does not establish consciousness, an independent information layer, or a universal law of emergence.

## 1. Core refinement

A lower-scale degree of freedom need not be physically destroyed when a higher-scale organisation forms. The stronger and more testable possibility is that the lower-scale variable remains physically instantiated while losing **independent relational addressability** for the lower-scale individuality that previously possessed it.

The first formulation of this supplement treated the relevant identity class as though it could be held fixed while that loss was measured. That is not always lawful. If the system's boundary, maintenance relations, active construction address, or constitutive coupling to its environment changes strongly enough, the operational definition of the individuality under comparison may also change.

The corrected distinction is therefore:

1. **physical persistence** — the underlying variable or invariant still exists in the realised substrate;
2. **independent addressability** — the current organised object can still vary, recruit, or route that variable as an independently available relation to itself;
3. **identity address** — the declared boundary, organisation, environment-coupling relations, history, and equivalence rule under which states count as continuations of the same individuality;
4. **scale ownership** — a lower-scale variable may remain causally active while becoming bound into a higher-scale constraint relation rather than remaining a free coordinate of the earlier individuality.

> The invariant can persist while its independent address changes.

> The self-address can also change. Do not assume the same self merely because the substrate persists.

## 2. Operational individuality address

Let a lower-scale physical state be

$$
x_t\in\mathcal X_{\alpha_t},
$$

where $\alpha_t$ is the active construction/state-space address inherited from Modules 31 and 32.

Let

$$
g_t^{SE}\in\mathcal G_t^{SE}
$$

denote the realised typed coupling state between the candidate system $S$ and the relevant environment $E$. This may include exchange, sensing, action, adhesion, boundary, regulatory, or other domain-appropriate relations. It is not a new physical layer.

Define an **operational individuality address**

$$
\sigma_t
=
\left(
\alpha_t,
\mathcal B_t,
\mathcal G_t^{SE},
\mathcal M_t,
H_t,
\sim_t^{\mathrm{id}}
\right),
$$

where $\mathcal B_t$ is the active boundary, $\mathcal M_t$ the relevant maintenance/closure relations, $H_t$ the retained lineage or history, and $\sim_t^{\mathrm{id}}$ the declared identity-equivalence rule for the claim being tested.

A corresponding operational self-state may be represented as the equivalence class

$$
s_t
=
[(x_t,g_t^{SE})]_{\sim_t^{\mathrm{id}}}
$$

inside the quotient induced by the declared identity rule.

This is an operational systems object, not a metaphysical definition of personhood. The identity rule must be declared at the layer and scale of the actual claim.

## 3. Same-self parity guard

A scale transition can change not only state but the criterion under which two states count as the same individual.

If

$$
\sigma_{t+1}\neq\sigma_t
$$

because a constitutive boundary, environment coupling, maintenance relation, construction address, or identity-equivalence rule has changed, then the statement

```text
"the same self lost degree of freedom i"
```

is not automatically licensed.

A lawful same-self continuation requires a declared continuation or translation map

$$
T_{t\rightarrow t+1}^{\mathrm{id}}:
\mathcal S_t\supseteq\mathcal D_t
\rightarrow
\mathcal S_{t+1},
$$

where $\mathcal S_t$ and $\mathcal S_{t+1}$ are the relevant identity-state spaces or quotients.

Let

$$
J_t:\mathcal S_t\rightarrow\mathcal J
$$

be a declared identity-bearing invariant or invariant family. Same-self continuity to tolerance $\varepsilon_J$ requires

$$
d_J\!\left(
J_{t+1}(T_{t\rightarrow t+1}^{\mathrm{id}}s_t),
J_t(s_t)
\right)
\leq\varepsilon_J,
$$

plus any domain-specific lineage, viability, or boundary conditions required by the identity claim.

If no lawful continuation map or identity-bearing invariant can be supplied, then the correct description is not automatically `the same self changed`. The event may instead be a reconstituted individuality, incorporation into another individuality, replacement of the comparison class, or an unresolved identity transition.

> Same substrate is not same self. Same name is not same self. Same components are not same self. Prove the continuation relation at the address where identity is claimed.

## 4. Identity-relative reachable set

Let

$$
\mathcal V_{\sigma_t}\subseteq\mathcal X_{\alpha_t}
$$

be the lower-realisation set compatible with persistence of the individuality class specified by $\sigma_t$.

Define the identity-relative reachable set

$$
\mathcal R^{\mathrm{id}}_{\sigma_t}(x_t)
=
\left\{
 x'\in\mathcal R_t(x_t):
 x'\in\mathcal V_{\sigma_t}
\right\}.
$$

This contains states reachable without leaving the declared individuality class under the active boundary, coupling, maintenance and viability conditions.

A lower-scale variable may therefore remain physically present while becoming impossible to vary independently inside this identity-relative set.

The phrase `identity-preserving reachable set` is valid only relative to the declared $\sigma_t$. If $\sigma_t$ changes, the old and new sets must not be compared as though one fixed identity class had silently persisted.

## 5. Independent relational addressability

Let

$$
\mathcal A_\ell(t)=\{I_1,I_2,\ldots,I_n\}
$$

be the declared lower-scale relations or variables that were independently addressable before consolidation.

For tolerance pair $(\varepsilon_i,\delta_{\sigma})$, call $I_i$ **independently addressable under individuality address $\sigma_t$** when there exist

$$
x',x''\in\mathcal R^{\mathrm{id}}_{\sigma_t}(x_t)
$$

such that

$$
\left\lVert I_i(x')-I_i(x'')\right\rVert>\varepsilon_i,
$$

while the other declared identity-bearing variables required to remain fixed for the test vary by no more than $\delta_{\sigma}$.

Define

$$
\mathcal A_{\ell\mid\sigma_t}
=
\left\{
I_i\in\mathcal A_\ell(t):
I_i\text{ passes the identity-relative addressability test}
\right\}.
$$

This is a statement about **which relations remain independently deployable while remaining within the declared individuality class**. It is not a statement that molecules, forces, variables, or lower-scale physical possibilities have vanished.

## 6. Cross-address comparison of addressability

If $\sigma_{t_2}=\sigma_{t_1}$, ordinary before/after comparison may be available under the declared measure $\mu_A$.

If the individuality address changes, a naive expression such as

$$
\mu_A(\mathcal A_{\ell\mid\sigma_{t_2}})
-
\mu_A(\mathcal A_{\ell\mid\sigma_{t_1}})
$$

may be malformed for the same reason that Module 32 forbids subtraction across unaligned state spaces.

Let

$$
T_A:
\mathcal A_{\ell\mid\sigma_{t_1}}
\rightarrow
\widetilde{\mathcal A}_{\ell\mid\sigma_{t_2}}
$$

be a lawful comparison map for the relevant relation class. Then an addressed change in independent accessibility may be written

$$
\Delta_T A_\ell
=
\mu_A\!\left(\mathcal A_{\ell\mid\sigma_{t_2}}\right)
-
\mu_A\!\left(T_A(\mathcal A_{\ell\mid\sigma_{t_1}})\right).
$$

If no such map is justified, report the two addressability structures separately rather than manufacturing one scalar difference.

This is the **same-self parity extension** of the no-false-subtraction rule.

## 7. Constraint binding rather than destruction

Suppose a lower-scale action or movement set before consolidation is

$$
\mathcal U_{\ell}^{\mathrm{self}}(x).
$$

Under a higher-scale organisation with individuality address $\sigma_L$, the identity-compatible subset may be

$$
\mathcal U_{\ell\mid\sigma_L}^{\mathrm{self}}(x)
=
\mathcal U_{\ell}^{\mathrm{self}}(x)
\cap
\mathcal U_{\sigma_L}^{\mathrm{adm}}(x),
$$

with

$$
\mathcal U_{\ell\mid\sigma_L}^{\mathrm{self}}(x)
\subsetneq
\mathcal U_{\ell}^{\mathrm{self}}(x).
$$

The excluded routes are not necessarily physically impossible in isolation. They are inaccessible **while remaining within the organised identity class being tested**.

If the identity address itself changes across the transition, this statement must be translated through the same-self parity guard before the phrase `the old self lost access` is used.

## 8. Three scale-transition identity classes

The corrected formalism distinguishes at least three cases.

### 8.1 Same-address restriction

The individuality address remains inside the same declared comparison class and lower-scale independent addressability decreases:

$$
\sigma_{t_2}\sim_{\mathrm{id}}\sigma_{t_1},
\qquad
\Delta A_\ell<0.
$$

Here it is meaningful to say that the same operational individuality became more constrained, subject to the declared tolerance.

### 8.2 Readdressed continuation

The individuality address changes, but a lawful continuation map preserves the declared identity-bearing invariant:

$$
\sigma_{t_2}\neq\sigma_{t_1},
\qquad
T_{t_1\rightarrow t_2}^{\mathrm{id}}\text{ exists}.
$$

Here the individuality may be said to persist through reorganisation, but comparisons of freedom, capability, state or self require the translation map.

### 8.3 Identity replacement, incorporation, or unresolved transition

The individuality address changes and no adequate continuation map has been established.

Then the formalism does **not** call the pre- and post-transition objects the same self by default. A lower-scale individuality may have been incorporated into a higher-scale whole, replaced as the relevant comparison object, or left unresolved with respect to identity continuity.

These cases must not be collapsed into one word such as `emergence`.

## 9. Scale-transition onset and completion

A scale transition should not be defined only by the later appearance of a new capability.

When same-self or readdressed continuity has been established, a provisional onset may be associated with a sustained reduction in lower-scale independent addressability under an emerging load-bearing closure:

$$
t_{\mathrm{access}}
=
\inf\left\{
t:
\Delta_T A_\ell(t)<-\eta_A
\text{ and }
\Gamma_L(t)\ge\tau_\Gamma
\right\},
$$

where $\Gamma_L$ is a declared measure of higher-scale closure or organisational persistence.

A fuller transition requires separately measured higher-scale gain, for example

$$
\Delta_T A_\ell<0,
\qquad
\Delta_T A_L>0,
\qquad
\Delta_T K_L>0,
$$

with lawful comparison at every address.

If the identity equivalence rule itself changes and no continuation map is available, the earliest scientifically defensible marker is instead the **identity-address transition**: the point at which the old comparison class ceases to support the observed organisation and a new one becomes necessary.

This separates:

- **access loss** — formerly independent relations become bound;
- **identity readdressing** — the operational criterion of self-continuation changes;
- **higher-scale gain** — new stable relations or capabilities become available.

The three events may coincide, occur in sequence, or form an extended transition region.

## 10. Environment coupling can be constitutive

Environment is not automatically constitutive of identity, but it cannot be assumed incidental either.

Module 31 already carries environment $\mathcal E_t$, boundary $\mathcal B_t$, history and support conditions inside the context descriptor precisely because changing them can alter object class or admissible dynamics.

For an individuality claim, test the system–environment coupling directly. Let

$$
D_E
$$

be a controlled deformation of the environment or system–environment relation that preserves as much internal component state as the domain permits.

If

$$
D_E[\sigma_t]
\notin
\mathcal M_{\mathrm{id}},
$$

where $\mathcal M_{\mathrm{id}}$ is the declared same-individuality comparison class, then the changed coupling is constitutive for that identity claim rather than merely background context.

This does not mean the environment `is the self`. It means some relations to the environment may participate in defining which organised individuality is actually present.

## 11. Distinguishing endogenous address change from observer coarse-graining

Ordinary coarse-graining can remove fine detail from **our model** while leaving the real system unchanged. A claimed scale or self-address transition therefore needs more than a successful macroscopic description.

Useful controls include:

1. **observer-only coarse-graining control** — change model resolution without changing physical coupling; lower-scale behavioural access should remain unchanged;
2. **constraint-release control** — remove the proposed higher-scale binding while preserving lower machinery; predicted lower-scale autonomy should return where reversible;
3. **environment-coupling deformation** — change the candidate constitutive system–environment relation while preserving internal machinery as far as possible and test whether the individuality class changes predictably;
4. **boundary-shift control** — perturb the proposed boundary while tracking whether the same maintenance/identity relations remain closed;
5. **identity-map falsification** — propose the continuation map before examining the full outcome and test whether the declared invariant actually survives;
6. **component-preservation control** — verify that the machinery underlying the old capability remains present when independent deployment is suppressed;
7. **higher-scale gain control** — show that lost lower-scale access is associated with separately measured higher-scale capability rather than mere suppression.

## 12. Example geometry — motile cells to organised collective

For a motile lower-scale unit, a free heading or movement repertoire can remain physically supported by cytoskeleton, motors, receptors and energy supply while adhesion, signalling, polarity, collective geometry and environmental coupling restrict which trajectories remain independently available.

The test should ask simultaneously whether:

- the machinery for the old trajectory class is still present;
- release from the organising relation restores part of the old trajectory repertoire;
- restriction occurs selectively while higher-scale coordinated movement improves;
- the relevant system–environment coupling has changed in a way that alters the viable individuality class;
- a new collective coordinate, such as coherent group direction or centre-of-mass navigation, becomes controllable or predictively useful;
- a declared continuation map is required before calling the pre- and post-transition unit `the same self`.

A strong incorporation pattern is therefore not merely

$$
\Delta A_\ell<0,
\qquad
\Delta K_L>0,
$$

but

$$
\text{lower machinery persists}
\;\land\;
\text{identity relation is declared}
\;\land\;
\Delta_T A_\ell<0
\;\land\;
\Delta_T K_L>0.
$$

That supports **constraint incorporation under an explicit identity address**, rather than literal destruction of the lower variables.

## 13. Relationship to established neighbours

This refinement sits near substantial prior work and does not claim the broad ingredients as inventions.

- Varela, Maturana and Uribe (1974) formulate autopoietic organisation as the organisation that makes a living system an autonomous unity.
- Di Paolo (2005) develops adaptivity and sense-making as regulation relative to conditions of viability.
- Moreno and Etxeberria (2005) treat self-construction and activity in the environment as aspects of one organisation in basic autonomous systems.
- Barandiaran, Di Paolo and Rohde (2009) explicitly require an agent to define its individuality and describe agency as autonomous organisation adaptively regulating its coupling with the environment.
- Aguilera and Di Paolo (2018; published extension 2019) use perturbational/information-integration methods to delimit an integrated unit from its environment and model adaptive preservation of integrity under environmental change.
- Coarse-graining, quotient spaces, multiscale modelling, controlled/uncontrolled manifolds and organisational closure already supply neighbouring mathematical and methodological tools.

The broad claim that individuality is relational, self-maintaining, boundary-dependent, or coupled to environment is therefore **not** attributed to MKUFT as a first discovery.

The present MKUFT refinement is narrower: **apply the addressed-state/no-false-parity discipline to the individuality criterion itself, so that changing boundary or environment coupling can readdress the self-state and make naive before/after freedom comparisons undefined until a lawful identity-continuation map is supplied.**

Historical priority for that exact integration is not asserted here.

Relevant references include:

- Varela, F. G., Maturana, H. R., and Uribe, R. (1974). *Autopoiesis: The organization of living systems, its characterization and a model*. BioSystems 5, 187–196. DOI `10.1016/0303-2647(74)90031-8`.
- Di Paolo, E. A. (2005). *Autopoiesis, adaptivity, teleology, agency*. Phenomenology and the Cognitive Sciences 4, 429–452. DOI `10.1007/s11097-005-9002-y`.
- Moreno, A. and Etxeberria, A. (2005). *Agency in natural and artificial systems*. Artificial Life 11, 161–176. DOI `10.1162/1064546053278919`.
- Barandiaran, X. E., Di Paolo, E. A., and Rohde, M. (2009). *Defining Agency: Individuality, Normativity, Asymmetry, and Spatio-temporality in Action*. Adaptive Behavior 17, 367–386. DOI `10.1177/1059712309343819`.
- Aguilera, M. and Di Paolo, E. A. (2018). *Integrated Information and Autonomy in the Thermodynamic Limit*. Artificial Life Conference Proceedings, 113–120. DOI `10.1162/isal_a_00030`.
- Aguilera, M. and Di Paolo, E. A. (2019). *Integrated information in the thermodynamic limit*. Neural Networks 114, 136–146. DOI `10.1016/j.neunet.2019.03.001`.
- Montévil, M. and Mossio, M. (2015). *Biological organisation as closure of constraints*. Journal of Theoretical Biology 372, 179–191. DOI `10.1016/j.jtbi.2015.02.029`.
- Scholz, J. P. and Schöner, G. (1999). *The uncontrolled manifold concept: identifying control variables for a functional task*. Experimental Brain Research 126, 289–306. DOI `10.1007/s002210050738`.

## 14. Failure and reduction conditions

This refinement is weakened or reduced if:

- the lower-scale capability disappears because its physical machinery is destroyed rather than relationally bound;
- the apparent loss of access occurs only in the observer's coarse-grained model;
- changing environment coupling does not alter the claimed individuality class where the model predicts it should;
- the proposed same-self continuation map is post-hoc, arbitrary, or fails preregistered invariant tests;
- release of the proposed organising constraint does not restore lower-scale autonomy where reversibility is predicted;
- no stable higher-scale closure or capability appears;
- the claimed higher-scale object adds no predictive or interventional value beyond independent lower-scale components;
- the result depends on arbitrary post-hoc choices of identity rule, addressability threshold, macrostate definition, or environment boundary.

If those failures occur, use the simpler physical, organismic, dynamical, or coarse-grained description instead.

## 15. Claim boundary

This module does **not** establish that every emergence event is a scale transition of this form. It does not establish a universal sharp transition time. It does not establish consciousness, survival after death, reincarnation, `source`, or independent I→P dynamics.

It also does not claim that identity is always environmentally extended. Environment coupling must earn constitutive status for the specific individuality claim under test.

The scientifically useful claim is narrower:

> A candidate scale transition can require simultaneous auditing of **physical persistence, independent relational accessibility, and identity parity**. Lower variables can persist while higher-scale closure removes their independent deployment; if constitutive system–environment relations or the identity equivalence rule also change, the self-state itself is readdressed and same-self comparison requires a lawful continuation map.

## 16. Compressed rules

> **Do not ask only whether the old degree of freedom still exists. Ask whether the old individuality can still address it independently while remaining within a lawfully comparable identity class.**

> **If the relation to the environment changes the criterion of individuality, prove same-self parity before comparing old and new freedom.**

> **The invariant may persist while its address changes. The self-address may change with it.**

> **A scale transition can begin with load-bearing loss of lower-scale addressability, but completion and identity continuity are separate questions that must each earn their own comparison map.**
