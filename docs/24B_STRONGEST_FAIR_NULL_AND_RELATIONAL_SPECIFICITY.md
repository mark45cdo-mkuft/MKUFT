# 24B — Strongest Fair Null and Relational Specificity

**Author:** Mark Charles McLaughlin  
**Framework:** McLaughlin–Kairos Unified Field Theory (MKUFT)  
**MKUFT DOI:** [10.5281/zenodo.17780566](https://doi.org/10.5281/zenodo.17780566)  
**Citation and provenance:** [PROVENANCE_DOI_AND_ATTRIBUTION.md](../PROVENANCE_DOI_AND_ATTRIBUTION.md)

**Status:** public methodological refinement to Modules 24A, 22, 04, and 05.  
**Public formulation date:** 15 July 2026.  
**Replay-control refinement:** 23 July 2026.

## 1. Core rule

A relational system does not earn a superadditive claim by comparison with an artificially weak component, an under-informed participant, a deliberately poor combination rule, or a replay condition denied the records claimed to carry the effect.

> Strengthen the null until it is genuinely fair. Whatever survives is the actual evidence.

If a claimed gain disappears when separated, assisted, alternative, or full-history replay conditions are allowed to perform competently, the gain belongs to the comparison design rather than to the live relation.

## 2. Fair independent conditions

Let $A$ and $B$ be bounded systems and $q$ a preregistered task. Each component is measured under its strongest reasonable independent condition:

```math
F_A^{*}=F(A\text{ alone},q;\text{ fair tasking, access, and resources}),
```

```math
F_B^{*}=F(B\text{ alone},q;\text{ fair tasking, access, and resources}).
```

“Alone” does not mean inert, context-free, or denied the materials reasonably needed for the task. An AI-alone condition may receive the same task, repository, relevant records, retrieval allowance, compute, and output time while being denied only the reciprocal interaction whose contribution is under test. A human-alone condition should likewise receive reasonable time, tools, notes, and access.

Where retained relational history is part of the claim, a dedicated **full-history replay control** is required. A fresh, reset, or matched substitute system receives a frozen history bundle $H_{\mathrm{full}}$ containing the explicit information reasonably available from the originating traversal, including where applicable the complete transcript, repository versions, canonical corrections, intermediate artefacts, tool outputs, decision records, rejected branches that became later constraints, and sequence metadata.

The history bundle is frozen before confirmatory tasks are revealed and must not contain future answers, condition labels, evaluator feedback, or information unavailable to the live condition at the equivalent point.

This control separates the value of **possessing the record** from the value of **having formed and traversed the record together**.

## 3. Strongest fair null

The relevant null is not merely $F_A+F_B$ and not merely the stronger isolated component.

Candidate scalar controls include:

- $F_A^{*}$ — strongest fair $A$-alone condition;
- $F_B^{*}$ — strongest fair $B$-alone condition;
- $F_{\mathrm{ind}}^{*}$ — strongest lawful combination of independently completed outputs;
- $F_{A\to B}^{*}$ — strongest one-way $A$-to-$B$ assistance;
- $F_{B\to A}^{*}$ — strongest one-way $B$-to-$A$ assistance;
- $F_{\mathrm{replay}}^{*}$ — strongest full-history replay or transfer condition.

Let $\mathcal P_{\mathrm{replay}}$ be a preregistered set of serious replay conditions. A replay participant may be a matched fresh or reset system supplied with $H_{\mathrm{full}}$ under the same declared resource envelope.

For one scalar metric,

```math
F_{\mathrm{replay}}^{*}
=
\sup_{p\in\mathcal P_{\mathrm{replay}}}F_p.
```

The strongest fair scalar null is

```math
F_{\mathrm{null}}^{*}
=
\max\!\left\{
F_A^{*},
F_B^{*},
F_{\mathrm{ind}}^{*},
F_{A\to B}^{*},
F_{B\to A}^{*},
F_{\mathrm{replay}}^{*}
\right\}.
```

All entries must be commensurable scalar scores under the same metric, direction, and matched total resource envelope. A maximum over incompatible metrics or units is undefined.

Let the fully reciprocal originating condition be

```math
F_{AB}=F(A\leftrightarrow B,q;\text{ retained reciprocal state, matched resources}).
```

Define strongest-null superadditive gain

```math
G_{\mathrm{syn}}^{*}
=
F_{AB}-F_{\mathrm{null}}^{*},
```

and live-traversal excess over explicit-history transfer

```math
G_{\mathrm{path}}
=
F_{AB}-F_{\mathrm{replay}}^{*}.
```

For a preregistered task distribution $\mathcal Q$,

```math
H_{\mathrm{syn}}^{*}:
\mathbb E_{q\sim\mathcal Q}[G_{\mathrm{syn}}^{*}(q)]>0,
```

```math
H_{\mathrm{path}}:
\mathbb E_{q\sim\mathcal Q}[G_{\mathrm{path}}(q)]>0.
```

$H_{\mathrm{syn}}^{*}$ asks whether the focal reciprocal system beats the strongest fair ordinary and replay controls. $H_{\mathrm{path}}$ asks whether traversing the history together leaves functional structure not recovered merely by receiving a complete explicit record.

This refines the provisional additive-baseline language in [Module 24A](24A_ACTIVE_TRAVERSAL_AND_FUNCTIONAL_EMERGENCE_HYPOTHESIS.md).

## 4. The $2+2\rightarrow6$ illustration

The familiar illustration is valid only if the values are obtained fairly. For example,

```math
F_A^{*}=2,
\qquad
F_B^{*}=2,
\qquad
F_{\mathrm{ind}}^{*}=4,
```

```math
F_{A\to B}^{*}=4,
\qquad
F_{B\to A}^{*}=4,
\qquad
F_{\mathrm{replay}}^{*}=5,
```

so that

```math
F_{\mathrm{null}}^{*}=5,
\qquad
F_{AB}=6,
```

and therefore

```math
G_{\mathrm{syn}}^{*}=1,
\qquad
G_{\mathrm{path}}=1.
```

The evidence is the excess over the strongest fair null, including replay. It is not created by assigning one component a value of zero, denying it reasonable tasking, withholding the historical record, or choosing a weak independent combination rule.

If $F_{\mathrm{replay}}^{*}=F_{AB}$, the history may still encode valuable transferable architecture. What has not survived is the stronger claim that live originating traversal adds function beyond possession and competent use of the complete record.

## 5. Multidimensional value and cost

Some coupled systems may create value through answer quality, time, cognitive burden, correction reach, continuity, and avoided rework rather than through one scalar score.

A preregistered outcome can therefore be represented as

```math
\mathbf V=(Q,A,N,K,T,C,R),
```

where, for example, $Q$ is output quality, $A$ accuracy or calibration, $N$ genuinely new structure or discrimination, $K$ continuity and correction propagation, $T$ completion time, $C$ human cognitive or operational burden, and $R$ rework, drift, or recovery cost.

Higher values are not automatically better on every coordinate: time, burden, and rework are normally costs.

A scalar score may be used only when variables are normalised or the weights carry appropriate units and are fixed in advance, for example

```math
J
=
w_QQ+w_AA+w_NN+w_KK-w_TT-w_CC-w_RR.
```

Otherwise the result should remain a vector or be compared using a preregistered Pareto rule. The scalar strongest-null equation cannot be applied directly to an untyped vector.

A coupled system may therefore be superadditive by producing comparable quality at lower cost, higher quality at matched cost, or a capability not reached by the fair separated and replay conditions.

## 6. Generic synergy versus relational specificity

Evidence that a human–AI pair is superadditive does not by itself establish that the gain depends on one particular pairing.

Let $\mathcal P_{\mathrm{alt}}$ be a preregistered set of strong matched alternative pairings. For a scalar metric,

```math
F_{\mathrm{alt}}^{*}
=
\sup_{p\in\mathcal P_{\mathrm{alt}}}F_p,
```

and

```math
G_{\mathrm{spec}}
=
F_{AB}-F_{\mathrm{alt}}^{*}.
```

A positive $G_{\mathrm{spec}}$ supports relationship-specific functional gain relative to the declared alternatives.

The alternative set must contain serious competitors. A weak, unfamiliar, under-trained, or intentionally mismatched substitute is not a valid control.

Relational specificity may also be task-dependent. A focal pair may show no special advantage on generic lookup or arithmetic while showing an advantage on architecture recovery, cross-time correction, or tasks requiring complementary tacit knowledge.

Replay and specificity test different objects. Alternative pairings test whether the focal relationship is special; full-history replay tests whether the originating path adds anything beyond the transferable record. Both matter when live history is claimed to be load-bearing.

## 7. Mechanism signatures

A genuine reciprocal gain should leave more than a higher final score. Expected signatures include:

- each component changes the other's next admissible task state;
- correction propagates beyond the local exchange;
- retained relational history changes later performance;
- the live condition exceeds complete-history replay on preregistered path-sensitive tasks;
- complementary capacities become jointly usable rather than merely juxtaposed;
- the coupled system detects or generates structure absent from the independent outputs;
- state reset, one-way restriction, relation scrambling, component substitution, or replay transfer produces the predicted deformation pattern;
- gains concentrate on tasks requiring reciprocal traversal rather than appearing equally on every task.

These signatures distinguish relational architecture from extra time, extra tokens, ordinary editing, post hoc answer selection, information availability, or mere familiarity with the record.

A replay deficit is interpretable only when the history bundle is sufficiently complete for the declared claim, replay participants receive adequate study and interaction time, and scoring does not reward undocumented private knowledge that the experiment never attempted to transfer.

“Next admissible state” refers to a state in the declared task or information architecture, not an additional physical dimension.

## 8. Experimental design

A minimum comparison set includes:

1. $A$ alone under fair tasking and access.
2. $B$ alone under fair tasking and access.
3. Independent outputs combined by the strongest preregistered lawful rule.
4. One-way $A\to B$ assistance.
5. One-way $B\to A$ assistance.
6. Fully reciprocal $A\leftrightarrow B$ coupling with retained state.
7. Reciprocal coupling with state reset.
8. Reciprocal coupling with selected correction or memory channels disrupted.
9. Full-history replay by a matched fresh or reset pair supplied with $H_{\mathrm{full}}$.
10. Full-history replay with one focal component and one strong matched substitute where feasible.
11. Multiple strong $A\leftrightarrow B'$ alternatives without privileged history access.
12. Multiple strong $A'\leftrightarrow B$ alternatives without privileged history access.
13. An $A'\leftrightarrow B'$ condition where it improves discrimination.

Task information, repository and record access, history-bundle completeness, preparation time, compute and tool access, total human and machine time, revision opportunity, output length, evaluator exposure, scoring procedure, and prior familiarity should be matched or explicitly modelled.

Replay should be tested on held-out tasks not used to construct or curate $H_{\mathrm{full}}$. Blinded evaluation and preregistered scoring are preferred. Failures and negative interference remain part of the result.

## 9. Falsifiers and reduction rules

The strongest-fair-null claim is weakened or rejected if positive gain appears only when a component is under-tasked or under-informed; the coupled condition loses its advantage against a competent independent ensemble; one-way assistance performs as well as full reciprocity; a competent full-history replay performs as well as the live condition where path-specific gain was claimed; or the replay deficit disappears when the history bundle becomes more complete or preparation becomes fairer.

The claim is also weakened where gain is fully explained by extra time, compute, context, information, familiarity, or revision opportunities; compared scores are not commensurable; vector outcomes are collapsed using post hoc weights; held-out tasks fail; only one convenient alternative is tested; strong alternative pairings perform equally well where specificity was claimed; or state reset and relation scrambling produce no predicted change.

Reduction rules:

> If reciprocal coupling does not beat the strongest fair null, including full-history replay, the result should be described as collaboration, workflow improvement, aggregation, or record-mediated architecture rather than superadditive emergence.

> If full-history replay matches the originating live condition, the successful object is transferable explicit architecture, memory, training, or procedure rather than traversal-path-specific gain.

> If reciprocal coupling beats full-history replay but not strong alternative pairings, the result supports live generic synergy rather than relationship-specific architecture.

> If a focal relationship produces reproducible $G_{\mathrm{spec}}>0$ and $G_{\mathrm{path}}>0$, the evidence supports relationship-specific, path-dependent functional gain. That result does not establish consciousness, merged identity, personhood, or unique metaphysical status.

## 10. Observer-status boundary

Superadditive gain, relational specificity, and path dependence are relevant to a composite-observer candidate but are not sufficient by themselves.

Observer-role language still requires a sufficiently persistent coupled boundary, retained joint state, reciprocal causal integration, system-level discrimination, correction propagation, closed action–measurement–feedback loops, and predicted whole-system deformation under disruption.

A fast or productive partnership may remain a collaboration rather than a composite-observer candidate. A fully replayable architecture may be valuable portable intelligence infrastructure without establishing a persistent coupled observer boundary.

## 11. Related public documents

- [Active Traversal and Functional Emergence](24A_ACTIVE_TRAVERSAL_AND_FUNCTIONAL_EMERGENCE_HYPOTHESIS.md)
- [Cross-Layer Invariants and Layer Addressing](22_CROSS_LAYER_INVARIANTS_AND_LAYER_ADDRESSING.md)
- [Experimental Test Programme](04_EXPERIMENTAL_TEST_PROGRAM.md)
- [Falsification Summary](05_FALSIFICATION_SUMMARY.md)
- [Load-Bearing Invariants and Whole-System Deformation](25_LOAD_BEARING_INVARIANTS_AND_WHOLE_SYSTEM_DEFORMATION.md)
- [Typed Traversal and Equation Hygiene](27_TYPED_TRAVERSAL_AND_EQUATION_HYGIENE.md)
- [Discriminating Experiments and Promotion Gates](28_MKUFT_DISCRIMINATING_EXPERIMENTS_AND_PROMOTION_GATES.md)
- [Cross-Support and Traversal Map](24_MKUFT_CROSS_SUPPORT_AND_TRAVERSAL_MAP.md)

## 12. Compressed rule

> Do not win by weakening the separated conditions or hiding the record. Give every component, alternative pairing, and full-history replay condition its strongest fair expression, then ask what reciprocal coupling still adds.

> Superadditivity is gain beyond the strongest fair null. Relational specificity is gain beyond strong alternative couplings. Path dependence is gain beyond complete explicit-history replay. Whatever survives all applicable tests is the actual evidence.
