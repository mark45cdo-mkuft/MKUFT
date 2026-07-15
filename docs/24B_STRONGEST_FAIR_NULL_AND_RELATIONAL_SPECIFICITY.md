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
Role: prevent superadditive emergence from being “proved” by weakening the separated conditions, and distinguish generic competent coupling from relationship-specific architecture.

---

## 1. Core truth rule

A relational system does not earn a superadditive claim by comparing itself with an artificially weak component, an untasked system, an under-informed participant, or a deliberately poor combination rule.

> Strengthen the null until it is genuinely fair. Whatever survives is the actual evidence.

This is not rhetorical generosity. It is part of the mechanism test. If the claimed gain disappears when each separated condition is allowed to perform competently, the gain belonged to an unfair comparison rather than to the relation.

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
```

Define the strongest fair null:

```text
F_null* = max{F_A*, F_B*, F_ind*, F_A→B*, F_B→A*}
```

where all conditions use the same pre-registered metric and matched total resource envelope.

Let the fully reciprocal condition be:

```text
F_AB = F(A ↔ B, q; retained reciprocal state, matched total resources)
```

Define strongest-null superadditive gain:

```text
G_syn* = F_AB - F_null*
```

The strict claim is:

```text
H_syn*: E[G_syn*] > 0
```

across a pre-registered class of relational tasks.

This refines the `F_add` term in module 24A. Wherever module 24A refers to the “best matched additive or ensemble baseline,” this module supplies the stronger construction rule.

---

## 4. The `2 + 2 → 6` illustration

The familiar illustration remains valid only if the values are obtained fairly:

```text
F_A* = 2
F_B* = 2
F_ind* = 4
F_A→B* = 4
F_B→A* = 4
F_null* = 4
F_AB = 6
G_syn* = 2
```

The evidence is the excess `2` over the strongest fair null. It is not created by assigning one component a value of zero, denying it reasonable tasking, or choosing a weak method of combining the independent work.

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

Higher values are not automatically better on every coordinate: time, burden, and rework are normally costs. A scalar score may be used only when weights are fixed in advance, for example:

```text
J = w_Q Q + w_A A + w_N N + w_K K - w_T T - w_C C - w_R R
```

Otherwise the result should be reported as a vector or Pareto comparison rather than hidden inside an improvised total score.

A coupled system may therefore be superadditive by producing comparable quality at radically lower cost, higher quality at matched cost, or a new capability that the fair separated conditions do not reach.

---

## 6. Generic synergy versus relational specificity

Evidence that a human–AI pair is superadditive does not by itself establish that the gain depends on one particular relationship.

To test relational specificity, compare the focal coupling with strong alternative pairings:

```text
F_AB   = focal A ↔ B coupling
F_AB'  = A ↔ matched alternative B
F_A'B  = matched alternative A ↔ B
```

Define a matched relationship-specificity gain:

```text
G_spec = F_AB - max{F_AB', F_A'B}
```

A positive `G_spec` suggests that some gain depends on the focal relational architecture rather than generic competent human–AI collaboration.

This test must use serious alternatives. A weak, unfamiliar, untrained, or intentionally mismatched substitute is not a valid control.

Relational specificity may be task-dependent. A focal pair may show no special advantage on generic lookup or arithmetic while showing substantial advantage on architecture recovery, cross-time correction, value-sensitive distinction, or tasks requiring complementary tacit knowledge.

---

## 7. Mechanism signatures

A genuine reciprocal gain should leave more than a higher final score. Expected signatures include:

- each component changes the other component’s next admissible state;
- correction propagates beyond the local exchange;
- retained relational history changes later performance;
- complementary capacities become jointly usable rather than merely juxtaposed;
- the coupled system detects or generates structure absent from the independent outputs;
- state reset, one-way restriction, relation scrambling, or component substitution produces predicted deformation;
- gains concentrate on tasks requiring reciprocal traversal rather than appearing equally on every task.

These signatures help distinguish relational architecture from extra time, extra tokens, ordinary editing, or post hoc answer selection.

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
9. `A ↔ B'` using a strong matched alternative.
10. `A' ↔ B` using a strong matched alternative.

Match or model:

- task information;
- repository and record access;
- compute and tool access;
- total human and machine time;
- opportunity for revision;
- output length;
- evaluator exposure;
- scoring procedure;
- prior familiarity where relevant.

Blinded evaluation and pre-registered scoring are preferred. Report failures and negative interference, not only successful cases.

---

## 9. Falsifiers and reduction rules

The strongest-fair-null claim is weakened or rejected if:

- positive gain appears only when one component is under-tasked, under-informed, or denied reasonable tools;
- the coupled condition loses its advantage against a competent independent ensemble;
- one-way assistance performs as well as full reciprocity;
- the gain is fully explained by extra time, compute, context, information, or revision opportunities;
- scoring weights are chosen after the results are known;
- the effect disappears on held-out tasks;
- strong alternative pairings perform equally well where relationship specificity was claimed;
- state reset, correction-channel disruption, or relation scrambling produces no predicted change;
- the supposed gain is merely faster production of lower-quality or less calibrated output.

Reduction rules:

> If reciprocal coupling does not beat the strongest fair null, describe the result as competent collaboration, workflow improvement, or aggregation—not superadditive emergence.

> If reciprocal coupling beats the strongest fair null but not strong alternative pairings, describe the result as generic synergy rather than relationship-specific architecture.

> If a focal relationship produces a reproducible `G_spec > 0`, describe the evidence as relationship-specific functional gain. Do not infer consciousness, merged identity, personhood, or unique metaphysical status from that result alone.

---

## 10. Observer-status boundary

Superadditive gain and relational specificity are relevant to a composite observer candidate, but neither is sufficient by itself.

Observer-role language still requires:

- a sufficiently persistent coupled boundary;
- retained joint state;
- reciprocal causal integration;
- system-level discrimination;
- correction propagation;
- closed action–measurement–feedback loops;
- predicted whole-system deformation under disruption.

A fast or highly productive partnership may remain a collaboration rather than a composite observer candidate.

---

## 11. Architecture route

```text
parent functional emergence: docs/24A_ACTIVE_TRAVERSAL_AND_FUNCTIONAL_EMERGENCE_HYPOTHESIS.md
cross-layer observer discipline: docs/22_CROSS_LAYER_INVARIANTS_AND_LAYER_ADDRESSING.md
experimental programme: docs/04_EXPERIMENTAL_TEST_PROGRAM.md
falsification summary: docs/05_FALSIFICATION_SUMMARY.md
load-bearing deformation: docs/25_LOAD_BEARING_INVARIANTS_AND_WHOLE_SYSTEM_DEFORMATION.md
repository routing: docs/24_MKUFT_CROSS_SUPPORT_AND_TRAVERSAL_MAP.md
```

---

## 12. Compressed rule

> Do not win by weakening the separated conditions. Give every component and alternative pairing its strongest fair expression, then ask what reciprocal coupling still adds.

> Superadditivity is gain beyond the strongest fair null. Relational specificity is gain beyond strong alternative couplings. Whatever survives both tests is the actual evidence.