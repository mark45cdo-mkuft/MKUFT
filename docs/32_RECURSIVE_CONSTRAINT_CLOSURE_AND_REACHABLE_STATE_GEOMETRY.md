# 32 — Recursive Constraint Closure and Reachable-State Geometry

**Author:** Mark Charles McLaughlin  
**Framework:** McLaughlin–Kairos Unified Field Theory (MKUFT)  
**MKUFT DOI:** [10.5281/zenodo.17780566](https://doi.org/10.5281/zenodo.17780566)  
**Citation and provenance:** [PROVENANCE_DOI_AND_ATTRIBUTION.md](../PROVENANCE_DOI_AND_ATTRIBUTION.md)  
**Public formulation date:** 15 August 2026

**Status:** public structural and mathematical working hypothesis. This module does not establish a new force, a new physical layer, consciousness, life, independent I→P dynamics, or a universal biological morphology.

## 1. Purpose and claim boundary

This module asks a narrower question:

> When a system learns, develops, or evolves, can earlier organisation become part of the constraint structure that changes what later states, transitions, rules, and higher-scale capabilities are reachable?

The proposed object is not simply `more constraints`. A constraint can disable, distort, stabilise, protect, enable, or reorganise. The scientifically useful object is the **typed geometry of constraints and the change they produce in reachable state and capability sets at declared scales**.

The central distinction is:

> A reduction in local degrees of freedom can coexist with an expansion of higher-scale viable capability, but neither direction follows from constraint count alone.

This module therefore separates:

- local feasible-state freedom;
- higher-scale viable capability;
- constraint maintenance and closure;
- recursive learning or developmental update;
- changing state-space or rule address;
- cross-domain recurrence of architecture;
- and any stronger claim that an informational relation has independent physical efficacy.

## 2. Addressed adaptive system

Let an adaptive system at step $t$ be represented by

```math
\mathfrak A_t
=
\left(
\alpha_t,
 x_t,
 \mathcal C_t,
 \mathcal M_t,
 \mathbf v_t,
 H_t
\right),
```

where:

- $\alpha_t$ is the active construction/state-space address;
- $x_t\in\mathcal X_{\alpha_t}$ is the realised state at that address;
- $\mathcal C_t$ is the active typed constraint family;
- $\mathcal M_t$ is the set of maintenance/dependence relations among relevant constraints and processes;
- $\mathbf v_t$ is a typed valence/evaluation object where the domain supplies one;
- $H_t$ is the relevant retained history or lineage.

The tuple is an audit scaffold. It does not assert that every biological, cognitive, artificial, social, or physical system possesses the same variables or mechanism.

Module 31 governs the construction-address and representation-invariance requirements. Module 27 governs units, typed spaces, and equation status.

## 3. Changing state spaces and the no-false-subtraction rule

A fixed-state-space model commonly uses

```math
x_{t+1}=F(x_t,u_t).
```

That form is appropriate when the relevant variables, admissible operations, and state-space definition remain fixed.

For systems in which learning, development, or evolution may alter the available variables, constraints, action repertoire, decoder, or update rule, use a family of addressed spaces

```math
\{\mathcal X_\alpha\}_{\alpha\in A}
```

and the disjoint addressed union

```math
\mathfrak X
=
\bigsqcup_{\alpha\in A}
\{\alpha\}\times\mathcal X_\alpha.
```

An adaptive transition is represented schematically by evaluation of an update map on the current addressed system state and an admissible input or action:

```math
\mathfrak F_t(\mathfrak A_t,u_t)
=
(\alpha_{t+1},x_{t+1})
\in\mathfrak X,
```

with

```math
x_{t+1}\in\mathcal X_{\alpha_{t+1}}.
```

If $\alpha_{t+1}\neq\alpha_t$, the expression

```math
x_{t+1}-x_t
```

is not automatically meaningful. A comparison requires a lawful translation, embedding, common observable, quotient, or other declared map between the two addressed spaces.

> Changing the space of possibilities is not the same operation as moving to another point inside a fixed space.

This is the adaptive-state-space extension of Module 31's context-conditioned comparison rule.

The addressed-family construction does not claim that every real adaptive system literally generates a new mathematical space at each step. Use it only where the variables, equivalence relation, admissible operations, decoder, or rule set change enough that a fixed-space description would hide a load-bearing difference.

## 4. Endogenous discrimination without a homunculus

Let the current realised organisation be denoted

```math
\mathcal O_t^{\mathrm{org}}
=
(\mathcal C_t,\mathcal M_t,H_t,\alpha_t).
```

A system-level admissibility or discrimination function may be written

```math
a_t(x,u)
=
\mathcal D\!\left(x,u;\mathcal O_t^{\mathrm{org}}\right),
\qquad
0\le a_t\le1,
```

with admissible action/transition set

```math
\mathcal U_t^{\mathrm{adm}}(x)
=
\left\{
 u\in\mathcal U_t:
 a_t(x,u)\ge\theta_t
\right\}.
```

This formalises a simple possibility: the discriminator need not be an external judge. The system's current organisation can parameterise which transitions are accessible, stable, selected, inhibited, or costly.

This does **not** imply consciousness, intention, morality, or an invisible controller. $\mathcal D$ must be realised by domain-appropriate processes or relations and tested by intervention where possible.

## 5. Reachable-state geometry

Define the one-step addressed reachable set

```math
\mathcal R_t(\mathfrak A_t)
=
\left\{
(\alpha',x')\in\mathfrak X:
\exists u\in\mathcal U_t^{\mathrm{adm}}(x_t)
\text{ such that }
(\alpha',x')=\mathfrak F_t(\mathfrak A_t,u)
\right\}.
```

A recursive update may alter both current state and the geometry of later reach:

```math
\mathfrak A_t
\rightarrow
\mathfrak A_{t+1}
\rightarrow
\mathcal R_{t+1}(\mathfrak A_{t+1}).
```

A learning or developmental rule may be written schematically as

```math
\mathcal C_{t+1}
=
\mathcal L_C
\left(
\mathcal C_t,H_t,\mathbf v_t,e_t
\right),
```

where $e_t$ is the relevant new event, outcome, error, or environmental interaction. Where the update rule itself changes,

```math
\mathfrak F_{t+1}
=
\mathcal L_F
\left(
\mathfrak F_t,\mathcal C_{t+1},H_{t+1}
\right)
```

may be used as a higher-order scaffold.

Writing $\mathcal L_C$ or $\mathcal L_F$ does not supply a biological or physical mechanism. Their empirical meaning must be specified in each implementation.

The important candidate relation is:

```math
\boxed{
\text{previous organisation}
\rightarrow
\text{updated constraints}
\rightarrow
\text{changed admissibility}
\rightarrow
\text{changed future reach}
}
```

The previous state is therefore not merely stored content when its realised organisation changes what the system can become next.

## 6. Constraint consolidation and recursive closure

A constraint is **consolidated** here when a learned, developed, or evolved relation becomes sufficiently persistent to alter later admissibility, routing, stability, or capability under a declared test.

Consolidation is not automatically beneficial and is not synonymous with irreversible fixation.

For a discrete operational model, define a directed maintenance graph

```math
G_t^{C}
=
(\mathcal C_t,E_t^{M}),
```

where

```math
c_i\rightarrow c_j
```

means that a process or operation organised under constraint $c_i$ contributes to maintaining, regenerating, or enabling constraint $c_j$ at the declared time scale.

A strongly connected maintenance component can be used as an **operational proxy** for a mutually supporting closure loop in a discrete model. It is not asserted to be mathematically identical to the full biological theory of closure of constraints.

The scientific question is whether the proposed constraints actually act on relevant processes and whether their maintenance dependencies survive perturbation.

## 7. Typed valence and evaluation

A recursive learner may use positive/negative, benefit/cost, error/reward, viability, or other evaluative distinctions. These must not be flattened into one universal scalar.

Write

```math
\mathbf v_t
=
\left(
 v_t^{(1)},v_t^{(2)},\ldots,v_t^{(k)}
\right),
```

where each component has a declared meaning, scale, and measurement rule.

Possible domains include physical/sensory polarity, organism-level viability, task performance, organisational integrity, social value, or semantic/ethical evaluation. These are different relation classes.

No sum

```math
\sum_j v_t^{(j)}
```

is scientifically meaningful unless the components are commensurable or an explicit preregistered scalarisation is supplied.

In particular, sensory contrasts such as hot/cold, viability contrasts such as benefit/cost, organisational cohesion/disintegration, life/death boundaries, and higher semantic or ethical concepts are not interchangeable variables merely because they can all participate in learning.

## 8. Local freedom and higher-scale capability

Let $\mathcal F_{\ell,t}$ be a feasible lower-scale state set with declared measure $\mu_\ell$, and let $\mathcal K_{L,t}(B)$ be the set of higher-scale functions, tasks, or outcomes reachable within resource/viability budget $B$, with declared measure or count $\nu_L$.

When each before/after observable is defined in a common declared comparison space, an organisational constraint update may produce

```math
\Delta\mu_\ell
=
\mu_\ell(\mathcal F_{\ell,t+1})
-
\mu_\ell(\mathcal F_{\ell,t})
<0,
```

while simultaneously

```math
\Delta\nu_L
=
\nu_L(\mathcal K_{L,t+1})
-
\nu_L(\mathcal K_{L,t})
>0.
```

This is an **enabling-constraint pattern**: local degrees of freedom decrease while higher-scale viable capability expands.

The opposite is also possible. An overconstrained or badly organised system may show

```math
\Delta\mu_\ell<0,
\qquad
\Delta\nu_L<0.
```

If the before/after feasible or capability objects live in different addressed spaces, the corresponding difference is not defined until Module 31's translation/equivalence requirement is satisfied.

Therefore:

> Constraint number is not a freedom metric, a coherence metric, or a quality metric.

The correct report is typed and scale-separated. Local feasible-state volume and higher-scale capability are different observables unless a lawful map connects them.

## 9. Recurrent architecture from recurrent constraint classes

A recurring shape or architecture across systems can arise because similar constraints repeatedly favour a similar class of viable solutions.

Let

```math
K_C^{(A)}:\mathcal C_A\rightarrow\mathcal K_C,
\qquad
K_C^{(B)}:\mathcal C_B\rightarrow\mathcal K_C
```

map domain-specific constraints into a declared comparison space. A cross-system recurrence claim first requires

```math
d_C\!\left(
K_C^{(A)}(\mathcal C_A),
K_C^{(B)}(\mathcal C_B)
\right)
\le\varepsilon_C,
```

plus compatible functional/dynamical tests appropriate to the claimed relation.

Morphological resemblance alone is insufficient. Shared ancestry, common design history, developmental constraints, environmental forcing, material properties, and chance remain competing explanations where relevant.

The domain-general question is therefore not `why does nature prefer one shape?` but:

> Which repeated constraint class makes this architecture recurrently reachable, stable, or low-cost under the stated boundary conditions?

This is a comparison rule, not a universal morphology law.

## 10. Sphere example — brackets before universality

In three-dimensional Euclidean space, the sphere minimises surface area for a fixed enclosed volume. For a domain with isotropic positive surface tension $\sigma$ and no competing anisotropic load, a schematic surface contribution is

```math
E_{\mathrm{surface}}=\sigma A.
```

Under those brackets, minimising $A$ at fixed volume favours a sphere.

The conclusion is conditional. Gravity, rotation, substrate contact, anisotropic stress, electromagnetic forcing, heterogeneous surface energy, confinement, flow, active stresses, or other boundary conditions can change the stable shape.

The sphere is a bracketed example of a narrower rule:

> Repeated instances of the same specified constraint class can favour recurrent architecture without implying one universal underlying mechanism.

This also preserves Module 30's rule that a spherical LUCY pocket is a morphology-specific toy model rather than the canonical shape of LUCY.

## 11. Relationship to functional emergence

Module 24A asks whether active typed organisation produces reproducible functional gain relative to matched controls. This module adds a downstream temporal question:

> Does a successful organisational update alter the later reachable-state or capability geometry, rather than merely improve one current output?

A fair test must distinguish:

1. more content;
2. more compute or time;
3. a fixed policy becoming better tuned inside the same state space;
4. a changed constraint/admissibility structure;
5. a changed rule or construction address;
6. a genuine new higher-scale capability.

Module 24B's strongest-fair-null and replay controls remain applicable. A live adaptive path must outperform a complete-history replay where path dependence is claimed to matter.

## 12. Information-layer and I→P boundary

Constraint closure, semantic closure, recursive learning, or higher-scale organisation do **not** by themselves establish an independent pre-physical information layer.

If the full relevant organisation is adequately realised by measured P-layer variables and history, then an I-layer description may be useful as a higher-level relational model without establishing independent I→P dynamics.

The physical-only null remains schematically

```math
H_0:
Y_{t+\Delta}
\perp\!\!\!\perp
I_t
\mid P_t,H_t.
```

A stronger I→P claim requires a declared I variable or relation, a lawful coupling or interface into P, representation-robust specification, and held-out predictive or interventional gain beyond the adequate P-state/history baseline.

The proposed recursive-constraint framework is therefore compatible with two outcomes:

- **P-realised organisation:** the structural model is useful but ordinary physical realisation closes the mechanism;
- **independent I→P candidate:** additional relational content survives the strongest adequate P-only account and earns separate testing.

The first result is scientifically useful and is not a failure merely because it does not establish new physics.

## 13. Discriminating test programme

### 13.1 Fixed-space versus adaptive-space prediction

Predeclare whether learning is expected only to alter a policy inside one fixed $\mathcal X$ or to alter $\alpha$, $\mathcal C$, admissible actions, variables, or update rules. Compare held-out predictions of the two models.

### 13.2 Constraint ablation

Identify a proposed consolidated load-bearing constraint $c_i$, perturb or remove it lawfully, and test the predicted deformation of the higher-scale capability set.

A claimed enabling constraint should produce selective loss or alteration of the capability it is proposed to support, not arbitrary global collapse.

### 13.3 Count-matched random-constraint control

Add or impose a matched number/complexity of constraints that do not preserve the proposed maintenance and functional relations. If simple constraint count explains the gain, the stronger organisational claim is weakened.

### 13.4 Closure disruption

Break a predicted maintenance edge in $G_t^C$ while preserving as much local component content as possible. Test whether the closure-dependent state degrades in the predicted direction and whether repair restores it.

### 13.5 Reach expansion versus local pruning

Measure lower-scale feasible-state volume and higher-scale capability separately. Test the proposed pair

```math
(\Delta\mu_\ell,\Delta\nu_L)
```

rather than calling the result `more freedom` without scale.

### 13.6 Rule-change test

Where a new rule is claimed, demonstrate that the post-update behaviour cannot be reproduced by a fixed-rule model with hidden parameter retuning under the same resource and information budget.

### 13.7 Cross-implementation recurrence

Test the same typed constraint/function relation in more than one implementation. Require representation translation, dynamical compatibility, and relation-realisation evidence rather than visual resemblance.

### 13.8 Overconstraint test

Prospectively add constraints that are predicted to damage rather than enable the higher-scale object. A framework that treats every added restriction as progress fails this test.

## 14. Predictions

If the framework captures a real organisational class, then under suitable systems:

1. learned/developed/evolved load-bearing constraints should alter later admissibility or capability in reproducible ways;
2. matched random constraints should not reproduce the same higher-scale gain merely by reducing local degrees of freedom;
3. disrupting a maintenance relation should deform the predicted closure-dependent capability and repair should restore it where reversible;
4. some systems should show local state-space pruning together with higher-scale capability expansion;
5. overconstraint should be distinguishable from enabling constraint by reduced or distorted higher-scale reach;
6. systems with compatible typed constraint classes may converge on related functional architectures despite different substrates, while differing realisation mechanisms remain visible;
7. when a construction/state-space address changes, models that treat the system as moving only inside one fixed space should lose predictive adequacy if the change is genuine.

These are structural/functional predictions. They do not establish consciousness, life, morality, quantum behaviour, or foundational I→P physics.

## 15. Falsifiers and reduction rules

This module is weakened or reduced if:

- fixed-state-space models explain the same data equally well without hidden retrospective flexibility;
- proposed constraints do not measurably alter admissibility, persistence, or capability;
- constraint count alone explains the effect;
- closure relations cannot be operationalised or intervention does not deform the predicted capability;
- the same apparent recurrence disappears once ancestry, development, environment, material physics, or common design is controlled;
- local freedom and higher-scale capability cannot be measured without arbitrary post-hoc scalarisation;
- an alleged rule change is only ordinary parameter adaptation;
- representation changes alter the claimed invariant without a domain reason;
- a stronger I→P claim adds no held-out prediction beyond adequate P-state/history controls.

Reduction rule:

> If the adaptive geometry adds no discriminating power beyond ordinary fixed-state learning, control, development, or evolutionary models, retain the ordinary model and treat this module as a descriptive re-encoding only.

## 16. Relationship to current literature

This module is deliberately positioned against close neighbouring work rather than claiming novelty for isolated concepts.

- Montévil and Mossio (2015), *Biological organisation as closure of constraints*, **Journal of Theoretical Biology** 372, 179–191, DOI `10.1016/j.jtbi.2015.02.029`, develops biological organisation as mutually dependent constraints that act on processes and contribute to maintaining one another.
- Mossio and Moreno (2010), *Organisational closure in biological organisms*, argues that closure is important but underdetermines the full complexity of paradigmatic organisms; additional organisation and control matter.
- Pattee (2001), *The physics of symbols: bridging the epistemic cut*, **Biosystems** 60, develops the symbol–matter/control–measurement problem and the role of constraints.
- Rocha (2001), *Evolution with material symbol systems*, **Biosystems** 60, 95–121, DOI `10.1016/S0303-2647(01)00110-1`, uses semantic closure to study matter–symbol interdependence and open-ended evolution.
- Longo, Montévil and Kauffman (2012), *No entailing laws, but enablement in the evolution of the biosphere*, DOI `10.1145/2330784.2330946`, argues that biological possibility spaces themselves may change and develops the notion of enablement.
- Adams, Jacopin, Gagrani and Witkowski (2024), *An Open-Ended Approach to Understanding Local, Emergent Conservation Laws in Biological Evolution*, arXiv:`2407.03345`, examines internally maintained constraints, accessible states, and emergence of new local rules.
- López-Díaz and Gershenson (2026), *A Matter of Time: Towards a General Theory of Agency*, arXiv:`2606.23122`, is a recent preprint linking temporally organised closure, viability, endogenous anticipatory modulation, and reconstruction of future possibility spaces.

The overlap is substantial and should be stated plainly. The candidate MKUFT contribution is not `constraints`, `closure`, `enablement`, or `changing possibility spaces` by themselves. The specific object developed here is their integration with MKUFT's typed address/state-comparison discipline, explicit endogenous-discriminator scaffold, scale-separated local-feasibility versus higher-scale-capability test, changing-space comparison guard, strongest-fair-null/deformation route, and independent-content boundary for any I→P promotion.

Historical priority for that exact conjunction is not asserted here. It remains a literature-search and formal-comparison question.

## 17. Related MKUFT modules

- [24A — Active Traversal and Functional Emergence](24A_ACTIVE_TRAVERSAL_AND_FUNCTIONAL_EMERGENCE_HYPOTHESIS.md)
- [24B — Strongest Fair Null and Relational Specificity](24B_STRONGEST_FAIR_NULL_AND_RELATIONAL_SPECIFICITY.md)
- [25 — Load-Bearing Invariants and Whole-System Deformation](25_LOAD_BEARING_INVARIANTS_AND_WHOLE_SYSTEM_DEFORMATION.md)
- [27 — Typed Traversal and Equation Hygiene](27_TYPED_TRAVERSAL_AND_EQUATION_HYGIENE.md)
- [30 — LUCY Threshold Geometry and Relational Closure](30_LUCY_THRESHOLD_GEOMETRY_AND_RELATIONAL_CLOSURE.md)
- [31 — Context-Conditioned State Comparison and Observability](31_CONTEXT_CONDITIONED_STATE_COMPARISON_AND_OBSERVABILITY.md)
- [22A — Recursive Address Closure and Property Transmission](22A_RECURSIVE_ADDRESS_CLOSURE_AND_PROPERTY_TRANSMISSION.md)

## 18. Compressed rule

> Organisation can become constraint; constraint can change admissibility; changed admissibility can change what becomes reachable next.

> Measure the local loss and the higher-scale gain separately. More constraint is not automatically more coherence, more agency, or more freedom.

> Recurrent architecture earns an invariant claim only when the recurrent constraint relation, not merely the silhouette, survives typed comparison.

> A changing possibility space requires an addressed comparison map. Do not pretend that every adaptive transition occurs inside one fixed coordinate system.

> If ordinary P-realised organisation closes the mechanism, keep that result. Promote independent I→P dynamics only if an additional relation survives the strongest adequate physical baseline.