# Recursive Constraint Closure and Reachable-State Geometry

## An Addressed Formalism for Adaptive Systems with Changing Possibility Spaces

**Author:** Mark Charles McLaughlin  
**Framework:** McLaughlin–Kairos Unified Field Theory (MKUFT)  
**Status:** Public preprint / standalone paper candidate  
**Version:** 0.1  
**Public preprint date:** 15 August 2026  
**MKUFT backbone DOI:** [10.5281/zenodo.17780566](https://doi.org/10.5281/zenodo.17780566)  
**First public formulation anchor:** Git commit [`8e4fe4160ba57874c5cf6a7213d44ba3d0c97287`](https://github.com/mark45cdo-mkuft/MKUFT/commit/8e4fe4160ba57874c5cf6a7213d44ba3d0c97287), 15 August 2026, 01:20:48 BST  
**Canonical source module:** [`docs/32_RECURSIVE_CONSTRAINT_CLOSURE_AND_REACHABLE_STATE_GEOMETRY.md`](../docs/32_RECURSIVE_CONSTRAINT_CLOSURE_AND_REACHABLE_STATE_GEOMETRY.md)  
**Rights:** Copyright © 2026 Mark Charles McLaughlin. All rights reserved unless a later frozen publication expressly states another licence. See [`RIGHTS_AND_LICENSE_NOTICE.md`](../RIGHTS_AND_LICENSE_NOTICE.md) and [`MODULE_RIGHTS_MATRIX.md`](../MODULE_RIGHTS_MATRIX.md).

---

## Abstract

Adaptive systems are often represented as trajectories through a fixed state space. That representation can become inadequate when learning, development, evolution, or architecture change modifies the active variables, admissible operations, decoder, constraint structure, or update rule itself. This paper develops an addressed formalism in which adaptive states inhabit a family of construction-dependent spaces rather than being forced into one fixed coordinate system. The framework combines four ideas that are usually treated separately: organisational closure and maintained constraints; recursive learning or developmental update; changing reachable-state geometry; and scale-separated comparison between local feasible-state freedom and higher-scale viable capability.

The central proposal is that prior organisation can become part of the active constraint structure which conditions later admissibility. In schematic form,

```math
\text{previous organisation}
\rightarrow
\text{consolidated typed constraints}
\rightarrow
\text{changed admissibility}
\rightarrow
\text{changed future reach}
\rightarrow
\text{updated organisation}.
```

The framework introduces an explicit construction/state-space address, a no-false-subtraction rule for comparisons across changed addresses, an endogenous admissibility scaffold that requires no internal homunculus, and a two-scale distinction under which a decrease in lower-scale feasible-state volume may coexist with an increase in higher-scale viable capability. It also supplies an overconstraint control, relation-typed recurrence test, ablation programme, fixed-space null, and a strict boundary between useful higher-level informational description and any stronger claim of independent information-to-physical dynamics.

The paper does **not** claim that constraints, closure, enablement, changing possibility spaces, semantic closure, viability, or adaptive state spaces are individually new. The candidate contribution is their specific integration with addressed comparison discipline, endogenous admissibility, scale-separated freedom/capability observables, controlled deformation, and a strongest-fair-null route. Historical priority for that exact conjunction is asserted only as a dated public formulation claim and remains defeasible by earlier prior art.

---

## 1. Problem

A conventional adaptive model often takes the form

```math
x_{t+1}=F(x_t,u_t),
```

with a fixed state space, fixed interpretation of the variables, and a transition rule whose domain remains stable. This is an excellent representation when the system changes **inside** one already-defined space.

It is less adequate when adaptation changes the space being used to define the system itself. Examples include systems in which learning or development changes:

- the active constraint family;
- the admissible action repertoire;
- the decoder or representation;
- the variables that are operationally meaningful;
- the relation among subsystems;
- the update rule;
- or the higher-scale capabilities realised by the organised whole.

The resulting distinction is simple but consequential:

> **Moving to another state inside a fixed space is not the same operation as changing the address of the space in which a state is defined.**

A theory that fails to separate these operations can accidentally compare mathematically incommensurate states, interpret restriction at one scale as restriction at another, or call a recurrent morphology an invariant without showing that the underlying relation class also recurs.

---

## 2. Addressed adaptive system

Let the adaptive system at step $t$ be represented by

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
- $\mathcal M_t$ is the maintenance/dependence relation among relevant constraints and processes;
- $\mathbf v_t$ is a typed evaluation or valence object where the domain supplies one;
- $H_t$ is retained history or lineage relevant to the next transition.

This tuple is an audit scaffold rather than a claim that all adaptive systems possess identical mechanisms.

Define the family of addressed spaces

```math
\{\mathcal X_\alpha\}_{\alpha\in A}
```

and their disjoint addressed union

```math
\mathfrak X
=
\bigsqcup_{\alpha\in A}
\{\alpha\}\times\mathcal X_\alpha.
```

An adaptive transition is then evaluated on the current addressed system state and an admissible input or action:

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

The explicit address prevents a quiet category error: if $\alpha_{t+1}\neq\alpha_t$, the two state objects need not inhabit one common vector space merely because both are denoted by $x$.

---

## 3. The no-false-subtraction rule

If the address changes, an expression such as

```math
x_{t+1}-x_t
```

is **not automatically defined**.

A lawful comparison requires at least one declared relation such as:

- an embedding into a common space;
- a translation map;
- a quotient preserving the relevant invariant;
- a common observable;
- a decoder relation;
- an explicitly defined cross-address metric;
- or another domain-valid comparison map.

This rule is a direct extension of context-conditioned state comparison. It applies not only to subtraction but to claims such as:

- “the state is unchanged”;
- “the system moved farther”;
- “the new state is more coherent”;
- “freedom increased”;
- or “the same variable has a larger value.”

Before such claims are accepted, the comparison relation must be valid across the active addresses.

The rule is methodological rather than metaphysical. It does not assert that nature literally creates a new mathematical manifold at each learning step. It says that a fixed-space representation must not be retained when changes in variables, admissibility, equivalence, decoder, or rule make that representation materially misleading.

---

## 4. Endogenous admissibility without a homunculus

Let the realised organisation be

```math
\mathcal O_t^{\mathrm{org}}
=
(\mathcal C_t,\mathcal M_t,H_t,\alpha_t).
```

Define an admissibility or discrimination function

```math
a_t(x,u)
=
\mathcal D\!\left(x,u;\mathcal O_t^{\mathrm{org}}\right),
\qquad
0\le a_t\le1,
```

and the admissible transition set

```math
\mathcal U_t^{\mathrm{adm}}(x)
=
\left\{
 u\in\mathcal U_t:
 a_t(x,u)\ge\theta_t
\right\}.
```

The point is structural: the discriminator need not be represented as a second executive agent observing the system from inside. The **current realised organisation** can parameterise which transitions are accessible, stable, selected, inhibited, costly, or destructive.

This does not imply consciousness, intention, morality, or a hidden controller. In any concrete application, $\mathcal D$ must be realised by domain-appropriate processes and should be testable by intervention or deformation.

---

## 5. Reachable-state geometry

Define the one-step reachable set

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

An adaptive update may therefore alter not only the realised state but the geometry of later reach:

```math
\mathfrak A_t
\rightarrow
\mathfrak A_{t+1}
\rightarrow
\mathcal R_{t+1}(\mathfrak A_{t+1}).
```

A constraint-learning rule may be represented schematically as

```math
\mathcal C_{t+1}
=
\mathcal L_C
\left(
\mathcal C_t,H_t,\mathbf v_t,e_t
\right),
```

where $e_t$ denotes an event, error, outcome, or environmental interaction.

Where the update rule itself changes,

```math
\mathfrak F_{t+1}
=
\mathcal L_F
\left(
\mathfrak F_t,\mathcal C_{t+1},H_{t+1}
\right)
```

can be used as a higher-order scaffold.

The candidate invariant is therefore:

```math
\boxed{
\text{organisation}
\rightarrow
\text{constraint update}
\rightarrow
\text{admissibility update}
\rightarrow
\text{reachable-set update}
}
```

When this relation is realised, earlier organisation is not merely stored historical content. It participates in the conditions under which later states can be reached.

---

## 6. Constraint consolidation and closure

A constraint is **consolidated** when an acquired, developed, or evolved relation persists strongly enough to alter later admissibility, routing, stability, maintenance, or capability under a declared test.

Consolidation is not synonymous with beneficial progress and need not be irreversible.

For a discrete operational model, define a directed maintenance graph

```math
G_t^C=(\mathcal C_t,E_t^M),
```

where

```math
c_i\rightarrow c_j
```

means that a process organised under constraint $c_i$ contributes to maintaining, regenerating, or enabling $c_j$ at the stated time scale.

A strongly connected component of this graph can serve as an operational proxy for a mutually supporting closure loop. It is not asserted to be identical to every biological formulation of closure of constraints.

The empirical burden remains clear: the proposed constraints must measurably act on relevant processes, and the predicted maintenance relation should deform when a load-bearing edge is perturbed.

---

## 7. Typed valence rather than universal polarity

Adaptive systems may contain evaluative distinctions: positive/negative, reward/error, benefit/cost, viability, regulatory success, social value, or higher semantic evaluation.

These must not be collapsed into one universal scalar merely because each can influence learning.

Write

```math
\mathbf v_t
=
\left(v_t^{(1)},v_t^{(2)},\ldots,v_t^{(k)}\right),
```

where each component has a declared scale, meaning, measurement rule, and relation class.

A scalarisation such as

```math
\sum_jv_t^{(j)}
```

is scientifically meaningful only if the components are commensurable or an explicit transformation is justified in advance.

Physical/sensory contrast, organism-level viability, organisational cohesion, life/death boundaries, and semantic or ethical evaluation may interact while remaining different variables.

---

## 8. Local feasible freedom and higher-scale capability

Let $\mathcal F_{\ell,t}$ denote a feasible lower-scale state set with measure $\mu_\ell$, and let $\mathcal K_{L,t}(B)$ denote the higher-scale functions, outcomes, or tasks reachable within budget $B$, with measure or count $\nu_L$.

When each before/after observable has a lawful common comparison space, an organisational update may produce

```math
\Delta\mu_\ell
=
\mu_\ell(\mathcal F_{\ell,t+1})
-
\mu_\ell(\mathcal F_{\ell,t})
<0,
```

while

```math
\Delta\nu_L
=
\nu_L(\mathcal K_{L,t+1})
-
\nu_L(\mathcal K_{L,t})
>0.
```

This is an **enabling-constraint pattern**: lower-scale degrees of freedom decrease while higher-scale viable capability expands.

An overconstrained system may instead exhibit

```math
\Delta\mu_\ell<0,
\qquad
\Delta\nu_L<0.
```

Therefore constraint count is not itself a measure of freedom, agency, quality, intelligence, or coherence.

This result resolves an apparent paradox without flattening scale. The lower-scale units and the higher-scale organised object do not share one undifferentiated freedom variable.

---

## 9. Recurrent architecture from recurrent constraint classes

Similar architectures may recur because comparable constraint classes repeatedly make a family of solutions reachable, stable, or low-cost.

For systems $A$ and $B$, let

```math
K_C^{(A)}:\mathcal C_A\rightarrow\mathcal K_C,
\qquad
K_C^{(B)}:\mathcal C_B\rightarrow\mathcal K_C
```

map domain-specific constraints into a declared comparison space.

A recurrence claim should require

```math
d_C\!\left(
K_C^{(A)}(\mathcal C_A),
K_C^{(B)}(\mathcal C_B)
\right)
\le\varepsilon_C,
```

plus functional or dynamical compatibility appropriate to the claimed relation.

Morphological similarity alone is insufficient. Competing explanations include common ancestry, common engineering history, environmental forcing, developmental constraint, substrate properties, and chance.

The stronger question is therefore:

> **Which repeated constraint class makes this architecture recurrently reachable, stable, or low-cost under the stated boundary conditions?**

The sphere provides a simple bracketed example. In Euclidean three-space, under fixed volume and isotropic positive surface tension with no dominant competing deformation, minimising surface area favours a sphere. Add gravity, rotation, substrate interaction, anisotropic stress, electromagnetic forcing, heterogeneous surface energy, confinement, flow, or active stresses and the stable form may change.

Recurrent geometry therefore supports a recurrent-constraint hypothesis only inside explicit brackets.

---

## 10. Relation to existing work

This framework sits close to several mature and current research programmes.

### 10.1 Closure of constraints

Montévil and Mossio develop biological organisation in terms of mutually dependent constraints acting on processes and contributing to one another's maintenance. Mossio and Moreno separately argue that organisational closure is important but does not exhaust the organisation and control required by paradigmatic organisms.

### 10.2 Symbol–matter and semantic closure

Pattee's work on the epistemic cut and the physics of symbols addresses how constraints, measurement, control, and symbolic relations connect material dynamics to functional information. Rocha develops material symbol systems and semantic closure in the context of open-ended evolution.

### 10.3 Enablement and changing possibility spaces

Longo, Montévil and Kauffman argue that biological evolution cannot always be represented as motion through a fully prestated phase space and use **enablement** to describe how organisation can make new possibilities available.

### 10.4 Internally maintained constraints and emergent local rules

Adams, Jacopin, Gagrani and Witkowski investigate internally generated or maintained constraints as a route to emergent local rules in open-ended evolution.

### 10.5 Agency and reconstructed future possibility

López-Díaz and Gershenson propose a temporally organised account of agency involving viability, endogenous anticipation, and reconstruction of future possibility spaces.

These overlaps are substantial. They are not treated as defects to hide. They constrain the contribution claim.

---

## 11. Candidate contribution

No priority is claimed here for the following ideas in isolation:

- constraints;
- closure of constraints;
- semantic closure;
- enablement;
- viability;
- open-ended evolution;
- changing possibility spaces;
- state-space models;
- adaptive control;
- or emergence through organisation.

The candidate contribution advanced in this paper is the **specific conjunction and operationalisation** of:

1. an explicit construction/state-space address $\alpha_t$;
2. a family of addressed spaces rather than forced fixed-space comparison;
3. the no-false-subtraction / no-unearned-state-parity rule across changed addresses;
4. endogenous admissibility parameterised by current realised organisation without introducing a homunculus;
5. recursive constraint consolidation that changes later reachable-state geometry;
6. a scale-separated pair of observables for lower-scale feasible-state freedom and higher-scale viable capability;
7. an explicit overconstraint case in which both shrink;
8. a typed relation-realisation criterion for recurrent architectures across substrates;
9. strongest-fair-null and deformation/ablation tests capable of reducing the framework back toward ordinary fixed-space adaptation when the added structure provides no discrimination;
10. and a strict boundary between a useful informational description and any claim of independent information-to-physical dynamics.

The public provenance claim is limited accordingly:

> **By 15 August 2026, Mark Charles McLaughlin had publicly formulated this addressed recursive-constraint/reachable-state synthesis in the MKUFT repository, with the first recoverable public source-module commit at 01:20:48 BST. This establishes a dated public formulation record for the specified conjunction; it does not prove that no earlier equivalent formulation exists anywhere in the literature.**

That statement is intended as a precise provenance and scientific-priority claim, not as a patent claim or a claim of ownership over abstract scientific principles.

---

## 12. Discriminating test programme

### 12.1 Fixed-space versus adaptive-address prediction

Predeclare whether the system is expected merely to tune a policy inside a fixed $\mathcal X$, or whether learning is expected to alter $\alpha$, $\mathcal C$, admissible actions, variables, decoder, or update rule. Compare held-out predictive performance of the two model classes.

### 12.2 Load-bearing constraint ablation

Identify a proposed consolidated constraint $c_i$, perturb or remove it while preserving as much unrelated structure as possible, and measure the predicted change in higher-scale capability.

A claimed enabling constraint should cause selective deformation of the capability it is proposed to support rather than arbitrary global damage.

### 12.3 Count-matched random-constraint control

Introduce a comparable number or complexity of constraints that do not preserve the proposed maintenance and functional relations. If mere restriction reproduces the same higher-scale gain, the stronger organisational interpretation is weakened.

### 12.4 Closure-edge disruption

Break a predicted maintenance edge in $G_t^C$ while preserving component inventory. Test whether the closure-dependent organisation degrades in the predicted direction and whether repair restores it where reversible.

### 12.5 Scale-separated freedom/capability measurement

Measure $\Delta\mu_\ell$ and $\Delta\nu_L$ independently. Do not infer one from the other.

### 12.6 Rule-change discriminator

Where a genuinely new update rule is claimed, show that the post-update behaviour cannot be reproduced by fixed-rule parameter retuning under the same information and resource budget.

### 12.7 Cross-implementation recurrence

Test the same typed constraint/function relation across different substrates or implementations. Require relation-realisation evidence rather than visual or topical resemblance.

### 12.8 Overconstraint prediction

Prospectively impose constraints predicted to damage the higher-scale system. A framework that interprets every additional restriction as improvement fails this test.

---

## 13. Reduction and falsification

The framework should be reduced toward an ordinary fixed-space account if:

- a fixed-state model predicts equally well without hidden retrospective flexibility;
- proposed constraints do not measurably alter admissibility, persistence, or capability;
- constraint count alone explains the effect;
- maintenance relations cannot be operationalised;
- ablation does not deform the predicted capability;
- apparent recurrence disappears after ancestry, environment, substrate, development, or common design is controlled;
- the proposed cross-address comparison depends on arbitrary post-hoc translation;
- alleged rule change is ordinary parameter adaptation;
- or the additional informational description adds no held-out discrimination beyond an adequate physical state/history model.

A null result is scientifically meaningful. If ordinary physical organisation closes the mechanism, the structural framework can remain useful without being promoted into a new physical ontology.

---

## 14. Information-layer boundary

Within MKUFT, the framework can be represented at an information-layer address, but constraint closure, semantic closure, recursive learning, or higher-scale organisation do **not** by themselves establish an independent pre-physical information layer.

The physical-only null can be written schematically as

```math
H_0:
Y_{t+\Delta}
\perp\!\!\!\perp
I_t
\mid P_t,H_t.
```

A stronger information-to-physical claim requires a defined informational variable or relation, a lawful interface into the physical layer, representation-robust specification, and prospective or interventional gain beyond the strongest adequate physical state/history baseline.

The framework therefore admits two legitimate outcomes:

1. **P-realised organisation:** the higher-level constraint description is useful, but its mechanism is adequately realised by ordinary physical processes and history;
2. **independent I→P candidate:** additional informational structure survives the strongest adequate physical account and earns separate testing.

The first outcome is not a failure.

---

## 15. Implications

If the framework survives testing, several consequences follow.

First, adaptive history can matter in a stronger way than simple stored memory: previous organisation may alter the admissible geometry in which later learning occurs.

Second, lower-scale restriction and higher-scale agency-like capability need not be contradictory because they are different scale-addressed observables.

Third, recurrent structures across biology, cognition, artificial systems, and engineered systems should be compared by typed constraint/function relation before being classified as the same architecture.

Fourth, recursive learning systems may be evaluated not only by output improvement but by whether a learned relation becomes durable architecture whose presence changes future reachable reasoning or action states.

These are testable structural claims. They are not evidence by themselves for consciousness, life, morality, quantum effects, alien morphology, or a new force.

---

## 16. Priority, attribution, and rights boundary

This manuscript records **authorship and chronology of a particular written formulation**. It is not an attempt to claim ownership of facts, abstract ideas, scientific principles, mathematical relationships, methods, or independently produced implementations beyond rights actually supplied by applicable law.

The first public Module 32 commit named above is the earlier public chronology anchor for the core formulation. This paper consolidates that already-public material into a citable standalone form.

The scientific-priority claim is deliberately narrow and falsifiable by documentary evidence:

> Mark Charles McLaughlin publicly formulated the specific conjunction stated in Section 11 by the recorded 15 August 2026 Git history, subject to any subsequently identified earlier publication containing the same conjunction at equivalent operational resolution.

The paper's expression, organisation, prose, diagrams if later added, and other copyright-protected authorship remain subject to the exact rights notice attached to this version. Publication does not itself create patent rights.

A later frozen Zenodo publication should receive its own version DOI and should cite both the first public Git commit and the MKUFT backbone DOI.

---

## 17. References

1. Montévil, M., & Mossio, M. (2015). Biological organisation as closure of constraints. *Journal of Theoretical Biology*, 372, 179–191. https://doi.org/10.1016/j.jtbi.2015.02.029
2. Mossio, M., & Moreno, A. (2010). Organisational closure in biological organisms. *History and Philosophy of the Life Sciences*, 32(2–3), 269–288.
3. Pattee, H. H. (2001). The physics of symbols: bridging the epistemic cut. *BioSystems*, 60, 5–21.
4. Rocha, L. M. (2001). Evolution with material symbol systems. *BioSystems*, 60, 95–121. https://doi.org/10.1016/S0303-2647(01)00110-1
5. Longo, G., Montévil, M., & Kauffman, S. (2012). No entailing laws, but enablement in the evolution of the biosphere. *Proceedings of the 14th Annual Conference Companion on Genetic and Evolutionary Computation*. https://doi.org/10.1145/2330784.2330946
6. Adams, A., Jacopin, E., Gagrani, P., & Witkowski, O. (2024). An Open-Ended Approach to Understanding Local, Emergent Conservation Laws in Biological Evolution. arXiv:2407.03345.
7. López-Díaz, A., & Gershenson, C. (2026). A Matter of Time: Towards a General Theory of Agency. arXiv:2606.23122.

---

## 18. Citation

Until a standalone DOI exists, cite this public preprint as:

> McLaughlin, Mark Charles. (2026). *Recursive Constraint Closure and Reachable-State Geometry: An Addressed Formalism for Adaptive Systems with Changing Possibility Spaces*. MKUFT public preprint, version 0.1, 15 August 2026. `mark45cdo-mkuft/MKUFT`. First public formulation commit: `8e4fe4160ba57874c5cf6a7213d44ba3d0c97287`. MKUFT backbone DOI: 10.5281/zenodo.17780566.

For the exact frozen version after later Zenodo deposit, use the version-specific DOI assigned to that deposit.
