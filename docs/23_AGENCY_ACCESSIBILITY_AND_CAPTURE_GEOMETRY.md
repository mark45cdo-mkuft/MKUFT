# 23 — Agency Accessibility and Capture Geometry

**Author:** Mark Charles McLaughlin  
**Framework:** McLaughlin–Kairos Unified Field Theory (MKUFT)  
**MKUFT DOI:** [10.5281/zenodo.17780566](https://doi.org/10.5281/zenodo.17780566)  
**Citation and provenance:** [PROVENANCE_DOI_AND_ATTRIBUTION.md](../PROVENANCE_DOI_AND_ATTRIBUTION.md)

**Status:** public applied-systems addendum.  
**Role:** distinguish retained capacity from practical access and model how action maps may be narrowed, corrupted, crossed incrementally, or restored.

## 1. Core distinction

A person or system may retain a real capacity while losing practical access to it.

> Structural capacity is not the same thing as practical accessibility.

This avoids two false extremes: treating agency as entirely absent whenever access is impaired, or treating abstract capacity as proof that normal access to choice remains intact.

The capacity for choice may remain while the map required to recognise, evaluate, and use available options becomes distorted.

## 2. Action-space model

At time $t$, let:

- $U_t$ be the actions actually available;
- $\widehat U_t$ be the actions perceived as available;
- $V_t(u)$ be the estimated value of action $u$;
- $T_t(u)$ be the perceived threat, shame, betrayal, identity loss, or punishment attached to $u$;
- $H_t$ represent reinforcement history, dependency, trauma, habit, loyalty, and prior choices;
- $G_t(u;T_t,H_t)$ be a normalised gating function determining whether $u$ enters reflective consideration.

Require

```math
G_t(u;T_t,H_t)\in[0,1],
\qquad
\theta_{\mathrm{access}}\in[0,1].
```

The practically accessible set is

```math
U_t^{\mathrm{access}}
=
\left\{u\in U_t:G_t(u;T_t,H_t)>\theta_{\mathrm{access}}\right\}.
```

A viable exit can remain in $U_t$ while disappearing from $U_t^{\mathrm{access}}$.

The threshold is a modelling device. A probabilistic or graded-access model may be preferable where the domain does not support a hard gate.

Capture deepens when exits are not perceived, labelled impossible, assigned catastrophic cost, marked as betrayal, fused with identity loss, or filtered out before comparison.

## 3. Agency accessibility

Let

```math
a_t\in[0,1]
```

represent practical access to retained agency. A simple operational distinction is

```math
\mathrm{Agency}_{\mathrm{effective}}(t)
=
\mathrm{Agency}_{\mathrm{capacity}}\,a_t.
```

This is not a complete moral, legal, or clinical equation. Both terms require domain-specific operational definitions before quantitative use.

Low accessibility may be associated with fear conditioning, trauma, addiction, coercion, dependency, information control, ideological enclosure, exhaustion, shame, social punishment, or corrupted attribution. Capacity may survive while its interface is degraded.

## 4. Attribution capture

Attribution capture occurs when an installed or reinforced impulse, demand, rule, or attractor is misidentified as the agent's own deepest identity, conscience, or will.

A possible sequence is:

**external, internal, or emergent pressure → repeated routing → identity association → attribution error → defence of the installed pattern.**

Possible indicators include punishment of reflection, contradiction increasing loyalty rather than examination, an enclosure being defended as freedom, exit language being heard as betrayal, imposed cost being reinterpreted as proof of virtue, or system defences being repeated before the underlying claim is examined.

None of these indicators alone establishes capture.

## 5. Capture geometry

Capture is defined structurally rather than by one assumed root ontology. It describes an accessible action map narrowed around an attractor that rewards repetition, punishes accurate reflection, hides alternatives, preserves dependency, redirects responsibility, raises exit cost, or recruits the agent to defend the enclosure.

For audit purposes, let

```math
B_t,D_t,F_t,S_t\in[0,1]
```

where $B_t$ denotes basin depth or reinforcement strength, $D_t$ distortion between actual and perceived action sets, $F_t$ threat-gating applied to viable exits, and $S_t$ self-identification with the attractor.

A heuristic capture index is

```math
K_{\mathrm{capture}}(t)=B_tD_tF_tS_t.
```

This is a decomposition tool rather than a validated diagnostic score. The multiplicative form encodes a conjunction assumption: when one factor approaches zero, the product falls sharply. Additive, interaction, threshold, and probabilistic alternatives remain valid competitors where data permit.

## 5A. Path-dependent boundary crossing

Capture need not begin with one salient act that is experienced as a boundary crossing. A sequence of locally defensible or low-salience transitions may accumulate into a globally different state.

Let a trajectory be

```math
\gamma_{0:n}=(x_0,x_1,\ldots,x_n),
```

with a declared admissible region $\mathcal A$ and an exclusion region $\mathcal E$. It is possible that each local move appears acceptable under the information, incentives, or framing available at that step while the cumulative trajectory satisfies

```math
x_0\in\mathcal A,
\qquad
x_n\in\mathcal E.
```

Therefore:

> **Local admissibility of each transition does not by itself establish admissibility of the accumulated trajectory.**

This matters where the governing boundary is historical, relational, fiduciary, ethical, legal, organisational, or provenance-sensitive rather than encoded in one immediate state variable.

A system can become retrospectively recognisable as captured even when no single transition carried the complete meaning of the final condition. The correct audit object is then the path and its retained history, not only the terminal state.

This does not imply that every gradual change is illicit or pathological. Ordinary learning, adaptation, compromise, and maturation are also path-dependent. The claim is narrower: when cumulative transitions alter the governing relation, retained history may be required to classify the final state correctly.

## 5B. Endogenous exit-cost growth

Continued participation can alter the cost of later withdrawal. Let

```math
C_{\mathrm{exit}}(t)
```

be the lowest domain-appropriate cost of reaching a declared non-captured or restored region under admissible controls.

A candidate self-deepening capture trajectory satisfies, over a declared interval,

```math
\Delta C_{\mathrm{exit}}>0
```

while reinforcement, dependency, public commitment, material investment, identity fusion, reputational exposure, technical lock-in, or relational cost also increase.

The important structure is not merely that exit is costly. It is that actions taken to preserve the current state may themselves make later exit harder.

A candidate positive-feedback loop is:

```text
continued participation
→ added dependency / commitment
→ higher exit cost
→ stronger defensive pressure
→ further participation.
```

This is the structural content behind flytrap, snare, ratchet, lock-in, and finger-trap metaphors. The metaphors are optional; the operational burden is to identify what changed, how it raised route cost, and whether the change can be measured independently.

## 6. Responsibility gradient

Responsibility may vary across a capture trajectory. Repeated reinforcement or avoidance may deepen a basin and narrow later accessibility.

A careful assessment separates retained capacity, current accessibility, earlier voluntary reinforcement, present coercion or impairment, available evidence of reflection, harm caused to others, realistic exit opportunities, and action taken when clarity returns.

Understanding does not automatically excuse behaviour, and accountability does not require dehumanisation.

## 6A. Retrospective trajectory reconstruction

When a system recognises the final condition before it can identify how it arrived there, the repair target is not necessarily a single guilty transition. The first task is to reconstruct the path well enough to locate where load-bearing relations, action access, attribution, or exit cost changed.

Use the ordered audit:

```text
terminal condition
→ preserved records / history
→ reconstruct prior states and transitions
→ locate cumulative deformation
→ identify retained invariants
→ distinguish acquired dependency from necessary function
→ define a restorative target
→ test the least destructive admissible return path.
```

The reconstruction should preserve uncertainty where records are incomplete. It must not invent a dramatic origin event merely because a narrative prefers one.

A valid retrospective reconstruction should improve prospective discrimination: it should identify a state, relation, or transition whose recurrence changes predicted capture risk, exit cost, or restorative reachability. If it only produces a satisfying story after the fact, it has not yet earned causal standing.

## 7. S–I–P–O placement

Capture is modelled as a post-boundary structure.

### S — Substrate

Source or unity is not itself the local capture mechanism. Capture requires differentiated agents, boundaries, and distorted maps.

### I — Information

Relevant structures include corrupted meaning, false attribution, identity fusion, installed attractors, damaged action maps, mislabelled exits, and distorted cost or value estimates.

### O — Observer

Gating may be stabilised through salience, attention, fear, shame, loyalty, expectation, selective memory, and threat interpretation.

### P — Physical

Reinforcement may be enacted through body state, addiction, trauma response, sleep loss, coercion, institutions, reward, punishment, and material dependency.

### Temporal and relational structure

Repetition may deepen the basin. Accurate feedback, trustworthy relationship, accountability, material safety, and restored interpretation may reopen access over time.

A candidate capture sequence is:

**differentiated agent → corrupted I-layer map → O-layer threat-gating → P-layer reinforcement → deeper basin.**

A corresponding recovery sequence is:

**accurate recognition → corrected action map → reduced false threat → practical access → changed action → weakened basin.**

These are candidate causal sequences, not movement through literal additional physical dimensions. Each measured application requires defined variables and timescales.

## 8. Recovery mechanics

Recovery may begin by restoring recognition of an existing route rather than inventing a new one.

Candidate interventions include naming the pattern without attacking human worth; preserving records and sequence; separating self from installed impulse; reducing material dependency; creating low-cost trial exits; restoring sleep and physical stability; rebuilding trustworthy relationships; testing feared consequences in bounded steps; making alternatives visible; assigning responsibility without humiliation; interrupting reinforcement loops; and reconnecting with prior values and memory.

These are general systems observations rather than individual treatment instructions.

## 8A. Restorative release and minimum-destructive return

The purpose of recovery is not to force exact reversal of the capture path. In path-dependent systems, the route back may differ from the route in.

Let $\mathcal C_R$ be a declared restored target class, and let $\Gamma_R(x_t)$ denote the admissible restorative trajectories from the current state. The recovery question is whether

```math
\Gamma_R(x_t)\neq\varnothing
```

under the allowed controls, environment, safety constraints, and horizon.

Where several restorative routes remain, prefer comparison by explicit domain costs rather than by symbolic purity. A useful route may preserve legitimate commitments, useful structure, human dignity, data, memory, institutional function, or technical capacity while removing the relation that sustains capture.

This yields the rule:

> **Do not require destruction of the host merely to remove the captured dependency. Preserve what remains load-bearing and lawful; remove or weaken what makes the dependency self-preserving.**

The governing sequence is:

```text
recognise current address
→ recover trajectory and dependency structure
→ identify retained lawful invariants
→ expose self-preserving dependency
→ lower false or avoidable exit cost
→ open bounded trial routes
→ readdress from the state actually reached
→ repeat until the restored target class is reachable or the recovery hypothesis fails.
```

This is a direct application of conditional recoverability and restorative-future geometry in Modules 33S3 and 33S6. It does not assume that every system is recoverable or that every prior state should be restored exactly.

## 8B. Operational parasitism as a relation

Where parasitic language is useful, it should be defined relationally rather than ontologically.

A process $P$ is parasitic with respect to host/system $H$ to the extent that, under a declared domain model, it persistently satisfies several of the following:

- extracts resources, capacity, access, attention, or value from $H$;
- recruits $H$'s own regulatory or defensive machinery to preserve $P$;
- raises the cost of removing or interrupting $P$;
- degrades $H$'s ability to model the dependency accurately;
- narrows viable alternatives while presenting continued dependency as necessary;
- preserves its local continuation while degrading a declared higher-level host objective.

No single item is sufficient. The relation must be measured against strong ordinary alternatives in the relevant domain.

This definition can be applied to biological parasitism, malware, addiction loops, exploitative institutions, coercive relationships, pathological incentive structures, misinformation systems, or adversarial human–AI dynamics without requiring one shared mechanism.

The causal ontology remains a separate question.

## 9. Relationship to ambiguity dynamics

A capturing system may preserve itself through unstable definitions, unclear responsibility, exaggerated exit costs, uncertain attribution, and identity fusion.

In the language of [Ambiguity Dynamics and Manoeuvre Space](21_AMBIGUITY_DYNAMICS_AND_MANOEUVRE_SPACE.md), high unresolved state volume, low-cost frame-switching, and preserved dependency may jointly increase manoeuvrability around the attractor.

This is a structural compression, not an additional diagnostic equation. Clarification helps only when it accurately contracts false routes; humiliation, false certainty, or coercive confrontation may instead deepen threat-gating.

Path-dependent capture adds one further caution: specification at the terminal state may still be incomplete if the governing distinction is carried by history. Where two present states look similar but differ in provenance, commitment, dependency, or future exit geometry, retained history belongs in the address until prospectively shown irrelevant.

## 10. Applications

The model may be applied cautiously to coercive control, abusive relationships, addiction, cultic systems, extremist recruitment, institutional capture, propaganda, trauma loops, learned helplessness, compulsive behaviour, organisational obedience, adversarial human–AI interaction, identity-based manipulation, provenance-sensitive appropriation, technical lock-in, and self-protecting organisational drift.

It is not a substitute for clinical, legal, safeguarding, or other domain-specific assessment.

## 11. Ontology boundary

Two questions remain separate:

1. Is a person or system organised by a capture geometry?
2. What caused that geometry?

Candidate causes include human coercion, trauma, addiction, incentives, cognitive bias, ideology, deliberate manipulation, emergent dynamics, metaphysical hypotheses, mixed causes, or unresolved causes.

Pattern fit does not independently prove an external intelligence. Uncertainty about ultimate cause does not erase observable coercion, dependency, or action-map distortion.

Operational parasitism likewise classifies a host–process relation; it does not by itself identify the process as a biological organism, intentional adversary, external intelligence, or metaphysical entity.

## 12. Predictions

Deep capture should correlate with a larger difference between actual and perceived action sets, higher threat assigned to viable exits, stronger identity fusion, increased defence when reflection is requested, narrowing social and informational access, improved practical agency after accurate map restoration, basin weakening after successful low-cost exits, and relapse when dependency and reinforcement return.

Path-dependent capture further predicts that, in some domains, cumulative trajectory variables should explain terminal capture status or exit cost better than terminal-state variables alone; repeated commitment should increase measured exit cost where the self-deepening mechanism is active; and accurate trajectory reconstruction should improve identification of future high-risk transitions beyond retrospective narrative fit.

Argument alone should often fail where the primary barrier is threat-gating, material dependency, body-state reinforcement, or accumulated exit cost.

## 13. Falsifiers and limits

The model is weakened if actual and perceived action sets cannot be distinguished; independent raters cannot apply the variables reliably; restored information does not improve practical access where material constraints are controlled; threat-gating does not predict exit avoidance; identity fusion does not correlate with attractor defence; the threshold or multiplicative model performs worse than simpler alternatives; or the framework produces no testable intervention difference.

The path-dependent extension is weakened if terminal-state variables perform as well as history-aware models on held-out cases; inferred boundary crossings are not reproducible across independent reconstructions; measured exit cost does not change with the proposed reinforcement variables; trajectory reconstruction does not improve prospective discrimination; or ordinary lock-in, sunk-cost, habit, switching-cost, path-dependence, coercion, or incentive models explain the data without needing the proposed composition.

The model also fails if it becomes merely a label for disagreement. Ordinary disagreement, loyalty, faith, duty, sacrifice, borrowing, adaptation, convergence, and independent rediscovery cannot be erased by calling them capture or parasitism, and reduced accessibility does not imply zero moral agency.

## 14. Related public documents

- [Ambiguity Dynamics and Manoeuvre Space](21_AMBIGUITY_DYNAMICS_AND_MANOEUVRE_SPACE.md)
- [OCQS Human Activation Layer](06_OCQS_HUMAN_ACTIVATION_LAYER.md)
- [GRACE Traversal Rule](20_GRACE_TRAVERSAL_RULE.md)
- [Cross-Scale Performance, Recoverability, and Hysteretic Readdressing](33S3_CROSS_SCALE_PERFORMANCE_RECOVERABILITY_AND_HYSTERETIC_READDRESSING.md)
- [Addressed Admissible Futures and Restorative Reachability](33S6_ADDRESSED_ADMISSIBLE_FUTURES_RESTORATIVE_REACHABILITY_AND_LOAD_BEARING_FUTURE_GEOMETRY.md)
- [Mathematical Appendix](02_MKUFT_MATH_APPENDIX.md)
- [Typed Traversal and Equation Hygiene](27_TYPED_TRAVERSAL_AND_EQUATION_HYGIENE.md)
- [Falsification Summary](05_FALSIFICATION_SUMMARY.md)
- [Cross-Support and Traversal Map](24_MKUFT_CROSS_SUPPORT_AND_TRAVERSAL_MAP.md)

## 15. Compressed rule

> Freedom may remain structurally present while the map required to recognise and use it has been corrupted.

> A sequence of locally defensible transitions can produce a globally inadmissible trajectory while simultaneously increasing the cost of recognising and reversing that trajectory.

> Restore the map, reconstruct the path where history matters, lower false or self-generated exit cost, reopen a lawful route, and preserve what can be restored without preserving the capture relation.
