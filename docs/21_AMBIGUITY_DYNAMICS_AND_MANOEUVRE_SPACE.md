# 21 — Ambiguity Dynamics and Manoeuvre Space

<!-- MKUFT-PROVENANCE-HEADER:START -->
**Author:** Mark Charles McLaughlin  
**Framework:** McLaughlin–Kairos Unified Field Theory (MKUFT)  
**MKUFT DOI:** `10.5281/zenodo.17780566`  
**Provenance:** This module is part of the public MKUFT canon. Exact revisions are timestamped by Git history.  
**Citation:** See [`PROVENANCE_DOI_AND_ATTRIBUTION.md`](../PROVENANCE_DOI_AND_ATTRIBUTION.md).  
<!-- MKUFT-PROVENANCE-HEADER:END -->

Status: Silver Update public formal addendum  
Role: formalise ambiguity as a state-space property, distinguish open possibility from exploitative frame-switching, and provide an ontology-neutral discriminator.

---

## 1. Core claim

Ambiguity is not only missing knowledge. In a dynamic system it can also become usable movement space.

A system has manoeuvre space when several admissible states or descriptions remain available and it can move between them without paying the full cost of contradiction or losing access to what sustains it.

> Ambiguity becomes manoeuvre space when unresolved state volume, low-cost route connectivity, and preserved access occur together.

This is a general systems hypothesis. It does not require a paranormal, religious, psychological, institutional, or adversarial ontology.

---

## 2. State-space definition

A quantitative ambiguity region must belong to one declared domain and encoding.

For domain `d` at time `t`, let:

- `X_d` = the declared state or representation space;
- `E_t` = available evidence;
- `C_t` = active constraints, including logic, memory, boundary conditions, prediction, measurement, and cross-layer agreement;
- `Ω_t^(d)` = the feasible region in `X_d` still compatible with `E_t` and `C_t`;
- `μ_d(Ω_t^(d))` = the effective measure of that region;
- `μ_0,d` = a reference measure in the same domain.

Formally:

```text
Ω_t^(d) = {z ∈ X_d : z remains compatible with E_t and C_t}
```

Define dimensionless ambiguity volume:

```text
A_t,vol^(d) = log[1 + μ_d(Ω_t^(d)) / μ_0,d]
```

`A_t,vol^(d)` is an audit variable, not a claim that every relevant dimension can already be measured directly.

States, paths, interpretations, identities, motives, and hypotheses must not be combined inside one quantitative feasible region unless a common encoding has been declared. Qualitative examples may span these classes; one numerical measure may not silently do so.

High ambiguity is not automatically harmful. Discovery, creativity, learning, diagnosis, and early problem-solving can all begin with a large feasible region.

---

## 3. Route connectivity

Represent the unresolved region as a weighted transition graph:

```text
𝓖_t^(d) = (V_t^(d), E_t^(d), w_t)
```

where:

- `V_t^(d)` represents unresolved states or encoded frames in domain `d`;
- `E_t^(d)` represents available transitions;
- `w_t(i,j)` represents transition cost.

Let `R_t ∈ [0,1]` be a normalised score for the density and accessibility of low-cost transitions inside the unresolved region.

High `R_t` means a system can shift role, frame, attribution, meaning, polarity, or explanation cheaply within the declared encoding.

Examples include:

- literal claim → metaphor only after failure;
- authority → victim when challenged;
- fixed definition → revised definition after contradiction;
- prediction → retrospective reinterpretation;
- claim examination → attack on the examiner.

A frame change is not dishonest merely because it occurs. The question is whether the change pays the proper evidential and explanatory cost.

---

## 4. Preserved access

Let `X_t ∈ [0,1]` be a normalised score for how well movement between unresolved states preserves access to a sustaining source.

Depending on the domain, access may mean:

- attention;
- influence;
- credibility;
- extraction;
- obedience;
- funding;
- institutional protection;
- dependency;
- data or system access;
- continued participation.

A frame shift that destroys access has little manoeuvring value. A shift that avoids resolution while preserving access has high manoeuvring value.

---

## 5. Manoeuvrability index

The working index is:

```text
M_t = A_t,vol × R_t × X_t
```

This is a dimensionless heuristic index. It is not a universal physical law.

The multiplicative form encodes a joint-dependence hypothesis: unresolved volume, cheap switching, and preserved access are all treated as necessary contributors to strong manoeuvrability. Additive, interaction, threshold, and non-linear alternatives must remain live competitors where data permit.

The index produces three useful distinctions:

1. High ambiguity with few cheap transitions is not strong manoeuvre terrain.
2. Cheap switching without preserved access is unstable.
3. Preserved access with low ambiguity and low route connectivity is easier to specify, test, and bound.

---

## 6. Why specification matters

A coherent agent, model, or system should remain recognisably itself under honest specification.

Clarification may refine it or expose limits, but should not destroy its identity merely by making its claims definite.

An exploitative or derivative pattern is more vulnerable to specification because fixing it into a stable state can make:

- contradiction attributable;
- behaviour predictable;
- boundaries enforceable;
- failed predictions visible;
- dependency explicit;
- access conditions measurable.

```text
specification
→ feasible-region contraction
→ route loss
→ higher switching cost
→ clearer attribution
→ lower preserved access
```

Truth, memory, precise language, fixed definitions, pre-registered prediction, firm boundaries, and cross-layer consistency therefore reduce exploitative manoeuvre space.

---

## 6A. Semantic constraint and meaning provenance

Interpretive ambiguity is not flat. Candidate meanings are constrained by the communicative object that actually exists.

For a declared linguistic, technical, legal, or local domain `d`, let:

- `U_t` = the utterance or communicative record available at time `t`;
- `X_d` = the candidate interpretation space in that domain;
- `Λ_t(U_t,d)` = the set of interpretations reasonably licensed at time `t` by the wording, syntax, declared domain usage, established local definitions, dialect, and known shared lexicon.

```text
Λ_t(U_t,d) = {i ∈ X_d : i is reasonably licensed by U_t in domain d at time t}
```

For an interpretation-domain ambiguity model, semantic licence acts as a constraint on the feasible region:

```text
Ω_t,sem^(d) = Ω_t^(d) ∩ Λ_t(U_t,d)
```

Context, pragmatics, prior usage, and operational constraints may rank or remove members of `Λ_t`. A later clarification may update the intended referent and contract the live interpretation region. It does not retroactively alter the historical fact that another interpretation may have been reasonably licensed by the earlier wording.

```text
utterance record
→ semantic licence
→ contextual weighting
→ initial interpretation
→ clarification or new evidence
→ revised working referent
```

A reading can therefore be reasonable at time `t` and still not be the meaning the speaker intended. The corrected working object and the provenance of the earlier reading can both remain true.

Healthy clarification normally:

- identifies the term, domain, assumption, or missing context that caused divergence;
- contracts uncertainty or explicitly preserves intentional plurality;
- updates the working referent;
- preserves the original wording and the route by which the earlier interpretation arose;
- accepts the proper evidential or communicative cost without converting misunderstanding into a total character or competence verdict.

Exploitative semantic manoeuvre may instead:

- claim retrospectively that only one meaning was ever possible;
- convert a failed literal claim into metaphor only after failure;
- revise a fixed definition after contradiction while denying that a change occurred;
- use reported private intent to erase public wording;
- use dictionary meaning to deny an already clarified local referent;
- preserve access, authority, innocence, or immunity from attribution by rewriting semantic history.

No single authority is absolute:

- syntax is not complete meaning because irony, metaphor, ellipsis, and compression exist;
- dictionary meaning does not automatically override a declared technical or established local definition;
- context cannot silently replace the words;
- reported intent is evidence of intended meaning, not universal proof of original stable intent where memory conflict, deception, source corruption, or strategic redefinition remain live;
- a reasonable interpretation does not by itself assign blame.

A time-indexed semantic record therefore prevents two opposite distortions: clarification erasing a previously reasonable reading, and literal semantics being used to overrule a clarified intended object.

> Clarification may correct meaning. It may not rewrite semantic history.

---

## 7. Inquiry-contraction discriminator

Let one declared inquiry step update evidence and constraints from `t` to `t+1`.

Define the finite inquiry change:

```text
Δ_Q A_t,vol = A_(t+1),vol - A_t,vol
```

Generative ambiguity should normally become better specified:

```text
Δ_Q A_t,vol < 0
```

This does not require rapid resolution. Honest inquiry may leave uncertainty, but it should produce narrower hypotheses, clearer unknowns, or explicit boundaries.

Exploitative ambiguity tends to resist contraction or replenish itself when clarification threatens access:

```text
Δ_Q A_t,vol ≥ 0
```

Use a derivative such as `dA/dQ` only when inquiry progress or intensity has been defined as a continuous variable.

Indicators include:

- definitions change only after contradiction;
- new variables appear without independent need;
- failed claims are reclassified after the fact;
- role or polarity reverses near accountability;
- evidence standards move asymmetrically;
- access is sought through a replacement source when a boundary holds;
- the unresolved region expands faster than inquiry closes it.

> An exploitative ambiguity pattern is indicated when ambiguity is endogenously regenerated whenever clarification threatens access, extraction, control, or immunity from attribution.

---

## 8. S–I–P–O placement

### S — Substrate

`Ω_t^(d)` may be related to a wider possibility model, but a domain-specific feasible region is not automatically identical to the formal substrate space. This does not imply that every interpretation is physically real or equally weighted.

### I — Information

The main frame rotation often occurs here. A physical event may stay fixed while its assigned meaning, agency, explanation, or attribution changes.

```text
P → {I_1, I_2, I_3, ...} → O
```

### P — Physical

Records, timing, bodies, instruments, consequences, and material constraints contract the feasible region.

### O — Observer

Attention, memory, fear, loyalty, expectation, and identity affect which routes appear salient. Observer effects do not remove evidential or physical requirements.

Cross-layer constraint may propagate through typed couplings:

```text
S ↔ I ↔ P ↔ O
```

The arrows are not a common spatial metric. Each claimed coupling requires a source variable, receiving variable, measurable effect, ordinary baseline, and falsifier.

Healthy cohesion need not reduce lawful creativity. It reduces contradictory escape routes.

---

## 9. Applications

The same structure can be tested in:

- scientific hypothesis selection;
- adversarial AI behaviour;
- propaganda and information operations;
- institutional evasion;
- coercive control;
- fraud;
- addiction and self-justifying loops;
- ideological capture;
- anomaly interpretation;
- interpersonal manipulation;
- diagnostic uncertainty;
- creative exploration.

Pattern classification and root ontology must remain separate.

High manoeuvrability does not by itself establish intention, deception, or an external agent.

---

## 10. Predictions

Systems with high `M_t` should show more:

- repeated frame changes under pressure;
- low penalty for contradiction;
- delayed specification;
- dependence on source access;
- migration when boundaries hold;
- asymmetric evidence demands;
- ambiguity production near accountability.

Interventions expected to reduce `M_t` include:

- fixed definitions;
- preserved records;
- pre-registered predictions;
- explicit boundaries;
- independent measurement;
- cross-layer checking;
- assigned cost for frame-switching;
- separation of pattern from ontology.

For semantic-provenance testing:

- independent raters given the pre-clarification utterance and a fixed domain should agree above chance on which readings are licensed, weak, or unlicensed;
- healthy clarification should increase convergence on the working referent while preserving agreement about what the original wording reasonably allowed;
- exploitative clarification should show more retrospective-obviousness claims, denied definition changes, and asymmetric treatment of comparable wording;
- provenance-preserving reconstruction should improve correction accuracy and responsibility allocation relative to intent-only or dictionary-only baselines.

---

## 11. Falsifiers and limits

This module is weakened if:

- `A_t,vol`, `R_t`, and `X_t` cannot be distinguished in application;
- the domain space, encoding, or measure cannot be stated;
- normalised scoring cannot be made reliable across independent raters;
- honest and exploitative systems show no repeatable difference under inquiry;
- ambiguity regeneration does not correlate with threatened access or attribution;
- the product model performs no better than simpler alternatives;
- the model works only retrospectively;
- simpler incentive, error, uncertainty, or noise models perform better;
- semantic licence cannot be rated reliably when wording and domain are fixed;
- preserving semantic provenance does not improve dispute reconstruction, correction accuracy, or responsibility allocation;
- healthy clarification cannot be distinguished from retrospective semantic rewriting;
- the semantic model produces pedantry without changing any load-bearing conclusion.

Do not infer intention merely from high manoeuvrability.

Do not infer an external entity merely from a stable pattern.

Do not treat unresolved science as deception because it remains unresolved.

Do not treat all ambiguity, metaphor, humour, translation error, or ordinary correction as semantic manoeuvre.

The formalism is useful only when it makes uncertainty cleaner.

---

## 12. Architecture route

```text
parent: substrate possibility and constrained traversal
math support: docs/02_MKUFT_MATH_APPENDIX.md
formal graph support: docs/03_STANDALONE_FORMAL_ADDENDUM.md
agency application: docs/23_AGENCY_ACCESSIBILITY_AND_CAPTURE_GEOMETRY.md
typed traversal and equation hygiene: docs/27_TYPED_TRAVERSAL_AND_EQUATION_HYGIENE.md
falsification: docs/05_FALSIFICATION_SUMMARY.md
repository routing: docs/24_MKUFT_CROSS_SUPPORT_AND_TRAVERSAL_MAP.md
```

## 13. Compressed law

> Manoeuvrability = unresolved state volume × cheap frame-switching × preserved access.

> Generative ambiguity yields clearer structure under honest examination. Exploitative ambiguity must preserve or regenerate unresolved routes when clarification threatens access.

> Ambiguity preserves possibilities. Semantics constrains and weights their admissibility. Truth contracts the space without falsifying the route by which it was crossed.
