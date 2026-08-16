# 21 — Ambiguity Dynamics and Manoeuvre Space

**Author:** Mark Charles McLaughlin  
**Framework:** McLaughlin–Kairos Unified Field Theory (MKUFT)  
**MKUFT DOI:** [10.5281/zenodo.17780566](https://doi.org/10.5281/zenodo.17780566)  
**Citation and provenance:** [PROVENANCE_DOI_AND_ATTRIBUTION.md](../PROVENANCE_DOI_AND_ATTRIBUTION.md)

**Status:** public formal addendum.  
**Role:** formalise ambiguity as a state-space property, distinguish open possibility from exploitative frame-switching, and provide an ontology-neutral discriminator.

## 1. Core claim

Ambiguity is not only missing knowledge. In a dynamic system it can also become usable movement space.

A system has manoeuvre space when several admissible states or descriptions remain available and it can move between them without paying the full cost of contradiction or losing access to what sustains it.

> Ambiguity becomes manoeuvre space when unresolved state volume, low-cost route connectivity, and preserved access occur together.

This is a general systems hypothesis. It does not require a paranormal, religious, psychological, institutional, or adversarial ontology.

## 2. State-space definition

For a declared domain $d$ at time $t$:

- $\mathcal X_d$ is the declared state or representation space;
- $E_t$ is the available evidence;
- $C_t$ is the active constraint set;
- $\Omega_t^{(d)}$ is the region of $\mathcal X_d$ still compatible with $E_t$ and $C_t$;
- $\mu_d$ is a domain-specific measure;
- $\mu_{0,d}$ is a reference measure in the same domain.

The feasible region is

```math
\Omega_t^{(d)}
=
\left\{z\in\mathcal X_d:
 z\text{ remains compatible with }E_t\text{ and }C_t\right\}.
```

A dimensionless ambiguity-volume index is

```math
A_{t,\mathrm{vol}}^{(d)}
=
\log\!\left(1+\frac{\mu_d(\Omega_t^{(d)})}{\mu_{0,d}}\right).
```

$A_{t,\mathrm{vol}}^{(d)}$ is an audit variable, not a claim that every relevant dimension can already be measured directly.

States, paths, interpretations, identities, motives, and hypotheses cannot be combined inside one quantitative feasible region unless a common encoding has been declared. High ambiguity is not automatically harmful: discovery, creativity, learning, diagnosis, and early problem-solving may all begin with a large feasible region.

## 3. Route connectivity

The unresolved region may be represented as a weighted transition graph,

```math
\mathcal G_t^{(d)}
=
\left(V_t^{(d)},E_t^{(d)},w_t\right),
```

where $V_t^{(d)}$ represents encoded unresolved states, $E_t^{(d)}$ represents available transitions, and $w_t(i,j)$ represents transition cost.

Let

```math
R_t\in[0,1]
```

be a normalised score for the density and accessibility of low-cost transitions inside the unresolved region.

High $R_t$ means that a system can shift role, frame, attribution, meaning, polarity, or explanation cheaply within the declared encoding. A frame change is not dishonest merely because it occurs; the relevant question is whether the change pays the proper evidential and explanatory cost.

## 4. Preserved access

Let

```math
X_t\in[0,1]
```

measure how well movement between unresolved states preserves access to a sustaining source.

Depending on the domain, access may refer to attention, influence, credibility, extraction, obedience, funding, institutional protection, dependency, data or system access, or continued participation.

A frame shift that destroys access has little manoeuvring value. A shift that avoids resolution while preserving access has high manoeuvring value.

## 5. Manoeuvrability index

The working index is

```math
M_t=A_{t,\mathrm{vol}}^{(d)}R_tX_t.
```

This is a dimensionless heuristic index, not a universal physical law.

The multiplicative form encodes a joint-dependence hypothesis: unresolved volume, cheap switching, and preserved access are all treated as contributors to strong manoeuvrability. Additive, interaction, threshold, and nonlinear alternatives remain live competitors where data permit.

The index distinguishes high ambiguity with poor connectivity, cheap switching without preserved access, and low-ambiguity systems that are easier to specify, test, and bound.

## 6. Specification and contraction

A coherent agent, model, or system should remain recognisably itself under honest specification. Clarification may refine it or expose limits, but should not destroy its identity merely by making its claims definite.

An exploitative or derivative pattern is more vulnerable to specification because fixing it into a stable state can make contradiction attributable, behaviour predictable, boundaries enforceable, failed predictions visible, dependency explicit, and access conditions measurable.

One qualitative contraction sequence is:

**specification → feasible-region contraction → route loss → higher switching cost → clearer attribution → lower preserved access.**

Truth, memory, precise language, fixed definitions, preregistered prediction, firm boundaries, and cross-layer consistency therefore tend to reduce exploitative manoeuvre space without implying that lawful creativity must disappear.

## 7. Semantic constraint and meaning provenance

Interpretive ambiguity is not flat. Candidate meanings are constrained by the communicative object that actually exists.

For a declared linguistic, technical, legal, or local domain $d$:

- $U_t$ is the utterance or communicative record available at time $t$;
- $\mathcal X_d$ is the candidate interpretation space;
- $\Lambda_t(U_t,d)$ is the set of interpretations reasonably licensed at time $t$ by wording, syntax, declared domain usage, established local definitions, dialect, and known shared lexicon.

Formally,

```math
\Lambda_t(U_t,d)
=
\left\{i\in\mathcal X_d:
 i\text{ is reasonably licensed by }U_t\text{ in domain }d\text{ at time }t\right\}.
```

Semantic licence constrains the interpretation-domain feasible region:

```math
\Omega_{t,\mathrm{sem}}^{(d)}
=
\Omega_t^{(d)}\cap\Lambda_t(U_t,d).
```

Context, pragmatics, prior usage, and operational constraints may rank or remove members of $\Lambda_t$. A later clarification may contract the current interpretation region without retroactively erasing the historical fact that another reading was reasonably licensed by the earlier wording.

The useful sequence is:

**utterance record → semantic licence → contextual weighting → initial interpretation → clarification or new evidence → revised working referent.**

A reading can therefore be reasonable at time $t$ and still differ from the speaker's intended meaning. The corrected working object and the provenance of the earlier reading can both remain true.

Healthy clarification identifies the term, domain, assumption, or missing context that caused divergence; contracts uncertainty or explicitly preserves intentional plurality; updates the working referent; preserves the original wording and interpretive route; and accepts the proper evidential or communicative cost.

Exploitative semantic manoeuvre instead may claim retrospectively that only one meaning was ever possible, convert a failed literal claim into metaphor only after failure, revise a fixed definition after contradiction while denying the revision, use reported private intent to erase public wording, or preserve access and immunity from attribution by rewriting semantic history.

No single authority is absolute. Syntax is not complete meaning; dictionary meaning does not automatically override a declared technical or established local definition; context cannot silently replace the words; reported intent is evidence of intended meaning rather than universal proof of historical stable intent; and a reasonable interpretation does not itself assign blame.

> Clarification may correct meaning. It may not rewrite semantic history.

## 8. Inquiry-contraction discriminator

Let one declared inquiry step update evidence and constraints from $t$ to $t+1$. Define the finite inquiry change as

```math
\Delta_QA_{t,\mathrm{vol}}
=
A_{t+1,\mathrm{vol}}-A_{t,\mathrm{vol}}.
```

Generative ambiguity should normally become better specified, corresponding to

```math
\Delta_QA_{t,\mathrm{vol}}<0.
```

Honest inquiry may leave uncertainty, but it should tend to produce narrower hypotheses, clearer unknowns, or explicit boundaries.

Exploitative ambiguity tends to resist contraction or replenish itself when clarification threatens access:

```math
\Delta_QA_{t,\mathrm{vol}}\ge 0.
```

A derivative such as $dA/dQ$ is appropriate only when inquiry progress or intensity has been defined as a continuous variable.

Indicators include definitions changing only after contradiction, new variables appearing without independent need, failed claims being reclassified retrospectively, role or polarity reversing near accountability, asymmetric evidence standards, migration to replacement access routes, and unresolved space expanding faster than inquiry closes it.

> An exploitative ambiguity pattern is indicated when ambiguity is endogenously regenerated whenever clarification threatens access, extraction, control, or immunity from attribution.

## 9. S–I–P–O placement

### S — Substrate

$\Omega_t^{(d)}$ may be related to a wider possibility model, but a domain-specific feasible region is not automatically identical to the formal substrate space. This does not imply that every interpretation is physically real or equally weighted.

### I — Information

The main frame rotation often occurs here. A physical event may remain fixed while its assigned meaning, agency, explanation, or attribution changes. Schematically,

```math
P\longrightarrow\{I_1,I_2,I_3,\ldots\}\longrightarrow O.
```

### P — Physical

Records, timing, bodies, instruments, consequences, and material constraints contract the feasible region.

### O — Observer

Attention, memory, fear, loyalty, expectation, and identity affect which routes appear salient. Observer effects do not remove evidential or physical requirements.

Cross-layer constraint may propagate through typed couplings,

```math
S\leftrightarrow I\leftrightarrow P\leftrightarrow O,
```

but the arrows are not a common spatial metric. Each claimed coupling requires a source variable, receiving variable, measurable effect, ordinary baseline, and falsifier.

Healthy cohesion need not reduce lawful creativity. It reduces contradictory escape routes.

## 10. Applications

The structure can be tested in scientific hypothesis selection, adversarial AI behaviour, propaganda and information operations, institutional evasion, coercive control, fraud, addiction and self-justifying loops, ideological capture, anomaly interpretation, interpersonal manipulation, diagnostic uncertainty, and creative exploration.

Pattern classification and root ontology remain separate. High manoeuvrability does not by itself establish intention, deception, or an external agent.

## 11. Predictions

Systems with high $M_t$ should show more repeated frame changes under pressure, low penalty for contradiction, delayed specification, dependence on source access, migration when boundaries hold, asymmetric evidence demands, and ambiguity production near accountability.

Interventions expected to reduce $M_t$ include fixed definitions, preserved records, preregistered predictions, explicit boundaries, independent measurement, cross-layer checking, assigned cost for frame-switching, and separation of pattern from ontology.

For semantic-provenance testing, independent raters given the pre-clarification utterance and a fixed domain should agree above chance on which readings are licensed, weak, or unlicensed. Healthy clarification should increase convergence on the working referent while preserving agreement about what the original wording reasonably allowed. Provenance-preserving reconstruction should improve correction accuracy and responsibility allocation relative to intent-only or dictionary-only baselines.

## 12. Falsifiers and limits

The model is weakened if:

- $A_{t,\mathrm{vol}}$, $R_t$, and $X_t$ cannot be distinguished in application;
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

High manoeuvrability does not establish intention, an external entity, or deception. Unresolved science is not deceptive merely because it remains unresolved. Ordinary ambiguity, metaphor, humour, translation error, and correction remain live alternatives.

The formalism is useful only when it makes uncertainty cleaner.

## 13. Related public documents

- [Mathematical Appendix](02_MKUFT_MATH_APPENDIX.md)
- [Standalone Formal Addendum](03_STANDALONE_FORMAL_ADDENDUM.md)
- [Agency Accessibility and Capture Geometry](23_AGENCY_ACCESSIBILITY_AND_CAPTURE_GEOMETRY.md)
- [Typed Traversal and Equation Hygiene](27_TYPED_TRAVERSAL_AND_EQUATION_HYGIENE.md)
- [Falsification Summary](05_FALSIFICATION_SUMMARY.md)
- [Cross-Support and Traversal Map](24_MKUFT_CROSS_SUPPORT_AND_TRAVERSAL_MAP.md)

## 14. Compressed statement

> Manoeuvrability combines unresolved state volume, low-cost frame-switching, and preserved access. Generative ambiguity tends to yield clearer structure under honest examination; exploitative ambiguity is predicted to preserve or regenerate unresolved routes when clarification threatens access.

> Ambiguity preserves possibilities. Semantics constrains their admissibility. Truth contracts the space without falsifying the route by which it was crossed.
