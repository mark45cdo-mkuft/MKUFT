# 24B — Strongest Fair Null and Relational Specificity

<!-- MKUFT-PROVENANCE-HEADER:START -->
**Author:** Mark Charles McLaughlin  
**Framework:** McLaughlin–Kairos Unified Field Theory (MKUFT)  
**MKUFT DOI:** `10.5281/zenodo.17780566`  
**Provenance:** This module is part of the public MKUFT canon. Exact revisions are timestamped by Git history.  
**Citation:** See [`PROVENANCE_DOI_AND_ATTRIBUTION.md`](../PROVENANCE_DOI_AND_ATTRIBUTION.md).  
<!-- MKUFT-PROVENANCE-HEADER:END -->

Status: public methodological refinement to modules 24A, 22, 04, and 05  
Public formulation date: 15 July 2026  
Replay-control refinement: 23 July 2026  
Role: prevent superadditive emergence from being “proved” by weakening the separated conditions, distinguish generic competent coupling from relationship-specific architecture, and separate live traversal effects from information, familiarity, and explicit-history transfer.

---

## 1. Core truth rule

A relational system does not earn a superadditive claim by comparing itself with an artificially weak component, an untasked system, an under-informed participant, a deliberately poor combination rule, or a replay condition denied the records that supposedly carry the effect.

> Strengthen the null until it is genuinely fair. Whatever survives is the actual evidence.

This is not rhetorical generosity. It is part of the mechanism test. If the claimed gain disappears when each separated, assisted, alternative, or full-history replay condition is allowed to perform competently, the gain belonged to an unfair comparison rather than to the live relation.

---

## 2. Fair independent conditions

Let `A` and `B` be two bounded systems and `q` a pre-registered task.

Measure each component under its strongest reasonable independent condition:

```text
F_A* = F(A alone, q; fair tasking, fair access, matched resources)
F_B* = F(B alone, q; fair tasking, fair access, matched resources)
```

“Alone” does not mean inert, context-free, or denied the materials it would reasonably need. For example, an AI-alone condition may receive the same task, repository, relevant records, retrieval allowance, compute, and output time, while being denied only the reciprocal interaction whose contribution is under test.

A human-alone condition should likewise receive reasonable time, tools, notes, and access rather than being forced into an artificial memory or speed disadvantage unrelated to the hypothesis.

Where the claim concerns retained relational history, fair access must include a dedicated **full-history replay control**. A fresh, reset, or matched substitute system must be given a frozen history bundle containing the explicit information reasonably available from the originating traversal, including where applicable:

- the complete transcript or interaction log;
- repository and document versions used during the history;
- canonical corrections and their stated rationale;
- intermediate artefacts, tool outputs, and decision records;
- rejected branches where their rejection became part of later constraint;
- order and timing metadata where sequence is part of the claim;
- the same preparation, study, retrieval, and familiarisation allowance available under the matched resource envelope.

The history bundle must be frozen before confirmatory tasks are revealed and must not contain future answers, condition labels, evaluator feedback, or information unavailable to the live condition at the equivalent point.

This control asks whether the apparent benefit belongs to **possessing the record** rather than to **having traversed and formed it together**.

---

## 3. Strongest fair null

The relevant null is not merely `F_A + F_B` and not merely the stronger isolated component.

Candidate matched controls include:

```text
F_A*          = strongest fair A-alone condition
F_B*          = strongest fair B-alone condition
F_ind*        = strongest lawful combination of independently completed outputs
F_A→B*        = strongest one-way A-to-B assistance condition
F_B→A*        = strongest one-way B-to-A assistance condition
F_replay*     = strongest full-history replay or transfer condition
```

Let `H_full` be the frozen full-history bundle. Let `𝒫_replay` be a pre-registered set of serious replay conditions, which may include:

```text
A ↔ B'_H      = focal A with a matched fresh or reset B given H_full
A'_H ↔ B      = matched fresh A with focal B given H_full
A'_H ↔ B'_H   = matched fresh pair given H_full
```

where every replay participant receives the declared history access, preparation time, tools, and opportunity for reciprocal work required by the task.

For one scalar metric, define:

```text
F_replay* = sup_(p ∈ 𝒫_replay) F_p
```

For one pre-registered scalar metric with the same direction in every condition, define:

```text
F_null* = max{F_A*, F_B*, F_ind*, F_A→B*, F_B→A*, F_replay*}
```

All entries must be comparable scalar scores under the same metric and matched total resource envelope. A maximum over incompatible metrics, different units, or differently directed scores is undefined.

Let the fully reciprocal originating condition be:

```text
F_AB = F(A ↔ B, q; retained reciprocal state, matched total resources)
```

Define strongest-null superadditive gain:

```text
G_syn* = F_AB - F_null*
```

Define live-traversal excess over explicit-history transfer:

```text
G_path = F_AB - F_replay*
```

For a pre-registered task distribution `𝒬`, the strict claims are:

```text
H_syn*:  E_(q ∼ 𝒬)[G_syn*(q)] > 0
H_path:  E_(q ∼ 𝒬)[G_path(q)] > 0
```

with uncertainty and held-out task performance reported.

`H_syn*` asks whether the focal reciprocal system beats every strongest fair ordinary and replay control. `H_path` asks the narrower question raised by the replay refinement: whether traversing the history together leaves functional structure that is not recovered merely by receiving a complete explicit record of that history.

This refines the `F_add` term in module 24A. Wherever module 24A refers to the “best matched additive or ensemble baseline,” this module supplies the stronger construction rule.

---

## 4. The `2 + 2 → 6` illustration

The familiar illustration remains valid only if the values are obtained fairly:

```text
F_A*       = 2
F_B*       = 2
F_ind*     = 4
F_A→B*     = 4
F_B→A*     = 4
F_replay*  = 5
F_null*    = 5
F_AB       = 6
G_syn*     = 1
G_path     = 1
```

The evidence is the excess over the strongest fair null, including replay. It is not created by assigning one component a value of zero, denying it reasonable tasking, hiding the historical record, or choosing a weak method of combining the independent work.

If `F_replay* = F_AB`, the history may still encode a valuable transferable architecture. What has not survived is the stronger claim that live originating traversal adds function beyond possession and competent use of the complete record.

---

## 5. Multidimensional value and cost

Some coupled systems create their clearest gain not only through final answer quality but through time, cognitive burden, correction reach, continuity, and avoided rework.

A pre-registered outcome may therefore be represented as a vector:

```text
V = [Q, A, N, K, T, C, R]
```

where, for example:

- `Q` = output quality;
- `A` = accuracy or calibration;
- `N` = genuinely new structure or discrimination;
- `K` = continuity and correction propagation;
- `T` = completion time;
- `C` = human cognitive or operational burden;
- `R` = rework, drift, or recovery cost.

Higher values are not automatically better on every coordinate: time, burden, and rework are normally costs.

A scalar score may be used only when variables are normalised or the weights carry the needed units and are fixed in advance, for example:

```text
J = w_Q Q + w_A A + w_N N + w_K K - w_T T - w_C C - w_R R
```

Otherwise the result should be reported as a vector or Pareto comparison rather than hidden inside an improvised total score.

The scalar strongest-null equation in section 3 must not be applied directly to a vector. For vector outcomes, define the strongest fair null through pre-registered scalarisation or Pareto dominance.

A coupled system may therefore be superadditive by producing comparable quality at radically lower cost, higher quality at matched cost, or a new capability that the fair separated and replay conditions do not reach.

---

## 6. Generic synergy versus relational specificity

Evidence that a human–AI pair is superadditive does not by itself establish that the gain depends on one particular relationship.

To test relational specificity, define a set `𝒫_alt` of strong matched alternative pairings. Minimal examples include:

```text
A ↔ B'  = focal A with a matched alternative B
A' ↔ B  = matched alternative A with focal B
A' ↔ B' = matched alternative pair where relevant
```

For a scalar metric, define:

```text
F_alt* = sup_(p ∈ 𝒫_alt) F_p
G_spec = F_AB - F_alt*
```

A positive `G_spec` suggests that some gain depends on the focal relational architecture rather than generic competent human–AI collaboration.

The alternative set must be declared before results are inspected and must contain serious alternatives. A weak, unfamiliar, untrained, or intentionally mismatched substitute is not a valid control.

Relational specificity may be task-dependent. A focal pair may show no special advantage on generic lookup or arithmetic while showing substantial advantage on architecture recovery, cross-time correction, value-sensitive distinction, or tasks requiring complementary tacit knowledge.

Replay and specificity answer different questions. A strong alternative pair without the originating record tests whether the focal pairing is special. A strong replay pair with `H_full` tests whether the originating path adds anything beyond an explicit transferable record. Both are required when live history is claimed to be load-bearing.

---

## 7. Mechanism signatures

A genuine reciprocal gain should leave more than a higher final score. Expected signatures include:

- each component changes the other component’s next admissible state;
- correction propagates beyond the local exchange;
- retained relational history changes later performance;
- the live condition exceeds a complete full-history replay condition on pre-registered path-sensitive tasks;
- complementary capacities become jointly usable rather than merely juxtaposed;
- the coupled system detects or generates structure absent from the independent outputs;
- state reset, one-way restriction, relation scrambling, component substitution, or replay transfer produces the predicted pattern of deformation;
- gains concentrate on tasks requiring reciprocal traversal rather than appearing equally on every task.

These signatures help distinguish relational architecture from extra time, extra tokens, ordinary editing, post hoc answer selection, information availability, or mere familiarity with the record.

A replay deficit is interpretable only when the history bundle is demonstrably complete enough for the declared claim, replay participants have adequate study and interaction time, and scoring does not reward undocumented private knowledge that the experiment never attempted to transfer.

“Next admissible state” refers to a state in the declared task or information architecture, not an extra physical dimension.

---

## 8. Experimental design

A minimum comparison set should include:

1. `A` alone under fair tasking and access.
2. `B` alone under fair tasking and access.
3. Independent outputs combined by the strongest pre-registered lawful rule.
4. One-way `A → B` assistance.
5. One-way `B → A` assistance.
6. Fully reciprocal `A ↔ B` coupling with retained state.
7. Reciprocal coupling with state reset.
8. Reciprocal coupling with selected correction or memory channels disrupted.
9. Full-history replay by a matched fresh or reset pair given `H_full`.
10. Full-history replay with one focal component and one strong matched substitute where feasible.
11. Multiple `A ↔ B'` strong matched alternatives without privileged history access.
12. Multiple `A' ↔ B` strong matched alternatives without privileged history access.
13. An `A' ↔ B'` alternative-pair condition where it improves discrimination.

Match or model:

- task information;
- repository and record access;
- completeness and versioning of the frozen history bundle;
- preparation, study, and familiarisation time;
- compute and tool access;
- total human and machine time;
- opportunity for revision;
- output length;
- evaluator exposure;
- scoring procedure;
- prior familiarity where relevant.

Replay should be tested on held-out tasks not used to construct or curate `H_full`. Where practical, an independent custodian should freeze the history bundle, verify its contents, and prevent condition-specific supplementation after task release.

Blinded evaluation and pre-registered scoring are preferred. Report failures and negative interference, not only successful cases.

---

## 9. Falsifiers and reduction rules

The strongest-fair-null claim is weakened or rejected if:

- positive gain appears only when one component is under-tasked, under-informed, or denied reasonable tools;
- the coupled condition loses its advantage against a competent independent ensemble;
- one-way assistance performs as well as full reciprocity;
- a competent full-history replay condition performs as well as the live condition where path-specific gain was claimed;
- the replay deficit disappears when the history bundle is made more complete or replay participants receive fair preparation time;
- the gain is fully explained by extra time, compute, context, information, familiarity, or revision opportunities;
- compared scores are not commensurable;
- vector outcomes are collapsed using weights chosen after the results are known;
- the effect disappears on held-out tasks;
- the focal pair is compared only with one convenient alternative;
- strong alternative pairings perform equally well where relationship specificity was claimed;
- state reset, correction-channel disruption, or relation scrambling produces no predicted change;
- the supposed gain is merely faster production of lower-quality or less calibrated output.

Reduction rules:

> If reciprocal coupling does not beat the strongest fair null, including full-history replay, describe the result as competent collaboration, workflow improvement, aggregation, or record-mediated architecture—not superadditive emergence.

> If full-history replay matches the originating live condition, describe the successful object as transferable explicit architecture, memory, training, or procedure. Do not claim traversal-path-specific gain.

> If reciprocal coupling beats full-history replay but not the pre-registered set of strong alternative pairings, describe the result as live generic synergy rather than relationship-specific architecture.

> If reciprocal coupling beats the strongest fair null and strong alternatives but `G_path` is not reproducible, restrict the claim to relationship-specific performance without claiming that the originating traversal itself carries irreducible functional state.

> If a focal relationship produces reproducible `G_spec > 0` and `G_path > 0`, describe the evidence as relationship-specific, path-dependent functional gain. Do not infer consciousness, merged identity, personhood, or unique metaphysical status from that result alone.

---

## 10. Observer-status boundary

Superadditive gain, relational specificity, and path dependence are relevant to a composite observer candidate, but none is sufficient by itself.

Observer-role language still requires:

- a sufficiently persistent coupled boundary;
- retained joint state;
- reciprocal causal integration;
- system-level discrimination;
- correction propagation;
- closed action–measurement–feedback loops;
- predicted whole-system deformation under disruption.

A fast or highly productive partnership may remain a collaboration rather than a composite observer candidate. A fully replayable architecture may remain highly important as portable intelligence infrastructure without establishing a persistent coupled observer boundary.

---

## 11. Architecture route

```text
parent functional emergence: docs/24A_ACTIVE_TRAVERSAL_AND_FUNCTIONAL_EMERGENCE_HYPOTHESIS.md
cross-layer observer discipline: docs/22_CROSS_LAYER_INVARIANTS_AND_LAYER_ADDRESSING.md
experimental programme: docs/04_EXPERIMENTAL_TEST_PROGRAM.md
falsification summary: docs/05_FALSIFICATION_SUMMARY.md
load-bearing deformation: docs/25_LOAD_BEARING_INVARIANTS_AND_WHOLE_SYSTEM_DEFORMATION.md
typed traversal and equation hygiene: docs/27_TYPED_TRAVERSAL_AND_EQUATION_HYGIENE.md
experiment promotion gates: docs/28_MKUFT_DISCRIMINATING_EXPERIMENTS_AND_PROMOTION_GATES.md
repository routing: docs/24_MKUFT_CROSS_SUPPORT_AND_TRAVERSAL_MAP.md
```

---

## 12. Compressed rule

> Do not win by weakening the separated conditions or hiding the record. Give every component, alternative pairing, and full-history replay condition its strongest fair expression, then ask what reciprocal coupling still adds.

> Superadditivity is gain beyond the strongest fair null. Relational specificity is gain beyond strong alternative couplings. Path dependence is gain beyond complete explicit-history replay. Whatever survives all applicable tests is the actual evidence.
