# 28E — Preservation, Search Geometry, and Detectability-Conditioned Negative Evidence

<!-- MKUFT-PROVENANCE-HEADER:START -->
**Author:** Mark Charles McLaughlin  
**Framework:** McLaughlin–Kairos Unified Field Theory (MKUFT)  
**Provenance:** This module is part of the public MKUFT canon. Exact revisions are timestamped by Git history.  
**Citation:** See [`../PROVENANCE_DOI_AND_ATTRIBUTION.md`](../PROVENANCE_DOI_AND_ATTRIBUTION.md).  
<!-- MKUFT-PROVENANCE-HEADER:END -->

**Status:** public methodological refinement for conditioning negative evidence on record state, search surface, sampling process, and readout. It does not by itself establish a new physical mechanism or empirical result.

## 1. Purpose

**Scope:** this module applies wherever a human, automated, or hybrid process uses non-detection from a bounded search/readout as evidence. It is not limited to human-led inquiry and is not an AI or software blueprint. Each application must instantiate preservation, accessibility, coverage, detection/readout and nuisance structure in the receiving domain or operational system.

A non-detection is not a context-free object.

Before absence is allowed to carry strong evidential weight, the analysis must ask whether the predicted trace should have:

1. survived or remained present;
2. remained accessible to the search;
3. fallen inside the actual sampling/search coverage;
4. been detectable by the declared instrument, observer, assay, query, archive, or readout;
5. been distinguished from the strongest ordinary sources of false negative or missed registration.

The core rule is:

> **Model the search surface before spending the null.**

This rule is symmetric. Poor preservation or poor detectability can weaken a negative result, but they do **not** become positive evidence that the missing object existed. Conversely, strong expected preservation, strong coverage, and high detection probability can make a clean null genuinely informative.

## 2. Addressed search state

For hypothesis $H$, target trace $T$, and declared search or measurement operation, define an addressed search state

```math
\mathcal G
=
(\mathcal P,\mathcal A,\mathcal C,\mathcal D,\mathcal N),
```

where, in domain-native form:

- $\mathcal P$ = preservation / persistence conditions for the predicted trace;
- $\mathcal A$ = accessibility of the relevant search surface or sample;
- $\mathcal C$ = actual coverage / sampling geometry;
- $\mathcal D$ = detector, assay, observer, query, archive, or readout sensitivity and resolution;
- $\mathcal N$ = nuisance, contamination, censoring, missingness, false-negative, and classification conditions that materially affect registration.

These symbols are role labels only. A real application must replace them with the field's native quantities, procedures, uncertainties, and controls.

The search state is part of the comparison address only when changing it can change the evidential interpretation of the null.

## 3. Detectability-conditioned non-detection

Let

```math
q_H
=
P(\text{detect }T\mid H,\mathcal G)
```

be the probability that the declared procedure would register the target trace if $H$ and the addressed search state held.

For a single binary detection opportunity,

```math
P(\varnothing\mid H,\mathcal G)=1-q_H,
```

where $\varnothing$ denotes non-detection.

For comparison between hypotheses $H_1$ and $H_0$, the evidential role of the null depends on the addressed likelihood ratio

```math
\Lambda_{\varnothing}
=
\frac{P(\varnothing\mid H_1,\mathcal G)}
     {P(\varnothing\mid H_0,\mathcal G)}.
```

A null is therefore informative only relative to a declared comparison and a declared search state.

If several detection opportunities are combined, do **not** multiply independent miss probabilities unless the domain justifies the independence or dependence model. Correlated coverage, shared blind spots, common calibration errors, repeated use of one archive, or common preprocessing can materially change the joint non-detection probability.

Where $q_H$ is not known, preserve an interval, distribution, sensitivity analysis, or explicit unresolved state rather than inventing a point estimate.

## 4. Preservation is part of the evidential geometry

A predicted trace can be real and still become unavailable to later observation through ordinary processes.

Depending on domain, preservation may depend on:

- decay, degradation, corrosion, weathering, burial, erosion, deposition, reworking, glaciation, submergence, tectonics, reuse, destruction, curation, or archive loss;
- biological turnover, decomposition, mutation, selection, sampling survival, or tissue/time-window effects;
- logging retention, overwritten storage, telemetry configuration, redaction, format conversion, data loss, or retention policy;
- instrument duty cycle, transient duration, source variability, visibility window, masking, saturation, or thresholding.

The relevant question is not whether preservation is imaginable, but whether the proposed preservation model changes the expected availability of the trace under the addressed comparison.

A weak preservation expectation gives a weak absence argument:

```math
P(T\text{ preserved and accessible}\mid H,\mathcal G)\ll 1
```

does not support

```math
\neg H.
```

It also does not support $H$. It limits how much evidential weight can be extracted from the missing trace.

## 5. Search and sampling coverage

A search that is large in absolute size may still be small relative to the space in which the target was predicted to occur.

The application should therefore state, where material:

- the declared target population, region, archive, state space, time window, or search domain;
- what fraction or subset was actually accessible;
- how sampling was chosen;
- which regions or classes were excluded;
- the spatial, temporal, categorical, or network geometry of the search;
- whether the search was adaptive, opportunistic, convenience-based, targeted, blinded, or preregistered;
- whether the same search rule would have been used if the result had been positive.

A post-hoc change to the search surface that is introduced only to rescue a preferred hypothesis does not count as a prospective explanation of the null.

## 6. Detector and readout sufficiency

A null can be strong only when the readout could have resolved the predicted difference at the relevant scale.

This includes, where applicable:

- sensitivity and specificity;
- limit of detection;
- spatial and temporal resolution;
- signal-to-noise ratio;
- calibration;
- observer/classifier reliability;
- query recall and indexing completeness;
- archive completeness;
- false-negative rate;
- censoring and missingness;
- back-action or intervention effects;
- classification threshold.

The negative result is weakened when the detector is poorly matched to the predicted signature.

This composes with [31 — Context-Conditioned State Comparison and Observability](31_CONTEXT_CONDITIONED_STATE_COMPARISON_AND_OBSERVABILITY.md): a distinction that is not resolvable by the declared readout cannot be treated as though the readout established its absence.

## 7. Relation to evidence semantics

This module refines the negative-evidence branch of [28D — Evidence Semantics and Claim-Promotion Guard](28D_EVIDENCE_SEMANTICS_AND_CLAIM_PROMOTION_GUARD.md).

The correct sequence is:

```text
predicted trace under H
→ addressed preservation / accessibility state
→ actual coverage / sampling
→ readout / detector model
→ nuisance and false-negative controls
→ non-detection likelihood
→ hypothesis update
```

The following are invalid:

```text
not observed
→ did not exist                                  [INVALID]

poor preservation
→ therefore probably existed                     [INVALID]

search was extensive
→ therefore coverage was sufficient              [INVALID]

many archives were checked
→ therefore evidential ancestry was independent  [INVALID]

detector saw nothing
→ detector had adequate sensitivity              [INVALID]
```

The evidential state must remain attached to the actual comparison.

## 8. Strong-null and ordinary-model relation

A fair negative-evidence test should include the strongest adequate ordinary explanations for missed registration.

Depending on domain, these may include:

- taphonomic loss;
- sampling bias;
- inaccessible regions;
- survey incompleteness;
- imperfect detection;
- calibration drift;
- archive gaps;
- logging or retention limits;
- censoring;
- class imbalance;
- threshold effects;
- transient visibility;
- nuisance variation;
- model mismatch.

The target hypothesis earns contraction only to the degree that the predicted trace should have survived and been found under a well-specified search state and still failed to appear.

A null that remains strong after these controls is not weakened merely because it is negative. A null that collapses after them should not be spent as though the search had been decisive.

## 9. Cross-domain instantiation

The same structural relation can be instantiated in different domains without implying one common mechanism.

### Archaeology / palaeontology / geology

Replace the generic roles with taphonomy, burial, erosion, deposition, submergence, exposure history, surveyable terrain, excavation/sampling coverage, dating context, material-specific survival, and the sensitivity of the method used to detect the predicted trace.

### Ecology / conservation

Use occupancy, sampling frame, repeat-survey design, observation process, detectability, season, habitat access, observer/instrument performance, and false-negative structure.

### Astronomy / transient search

Use survey footprint, cadence, duty cycle, limiting flux/magnitude, wavelength band, source duration, masking, weather/instrument availability, pipeline thresholds, and follow-up coverage.

### Medicine / biology

Use biological persistence, sampling time, tissue/compartment access, assay sensitivity/specificity, treatment or turnover effects, sample adequacy, censoring, and the comparison population.

### Digital forensics / software / security

Use log generation, telemetry enablement, retention window, collection scope, indexing/search completeness, clock alignment, parser/classifier coverage, overwritten state, and the distinction between no recorded event and no event.

These examples share an inference shape only. Their mechanisms, units, priors, controls, and evidence remain domain-native.

## 10. Prospective tests

A useful preservation/search-geometry rule should improve prediction or calibration prospectively.

Candidate tests include:

1. **Coverage expansion:** predict in advance how the negative-evidence weight should change as independently defined coverage increases.
2. **Detector upgrade:** predict which previously unresolved traces should become detectable under a higher-sensitivity readout.
3. **Matched-surface comparison:** compare regions/samples with similar target priors but different preservation or accessibility conditions.
4. **Blind recovery test:** hide known positives inside a realistic search surface and measure whether the declared procedure recovers them at the expected rate.
5. **Search-rule freeze:** freeze the search rule before result inspection and compare with an adaptive/post-hoc alternative.
6. **Independent surface:** repeat the search on a materially independent dataset, archive, region, instrument, or sample family where the hypothesis predicts the trace should also be available.
7. **Negative control:** use a target known to be absent or a search surface where the method should not report the focal trace.

The module earns value only if it changes a prediction, calibration, search design, falsifier, or interpretation beyond what the receiving field already captures more simply.

## 11. Failure and reduction conditions

Reduce, reject, or contract the module at the addressed application if:

1. preservation, access, coverage, and detector state cannot be operationalised well enough to alter the comparison;
2. the proposed search-state variables are chosen only after seeing the null;
3. detectability estimates are invented or unconstrained;
4. the same negative result receives different treatment solely because it favours or disfavors a preferred hypothesis;
5. a weak preservation model is converted into positive evidence for the missing object;
6. a strong high-detectability null is ignored because preservation failure is merely conceivable;
7. multiple dependent searches are counted as independent confirmation;
8. a domain-native occupancy, sampling, taphonomic, missing-data, screening, or detection model already closes the inference with equal or greater clarity and MKUFT adds no useful ordering, transfer rule, or falsifier;
9. the module becomes a generic excuse for any absent evidence;
10. the search state is widened without a corresponding change in the declared target, hypothesis, or comparison class.

## 12. Prior-art and module-scope boundary

Inference from absence, imperfect detection, sampling theory, taphonomy, missing-data models, occupancy/detection models, screening theory, survey selection effects, archival completeness, and search sensitivity are established research areas.

Those ingredients are established. The research contribution specific to 28E is narrower:

> **place preservation, accessibility, coverage, and readout sufficiency inside the addressed comparison before a non-detection is assigned strong negative evidential weight or used to materially contract or close the addressed hypothesis; preserve that search state through cross-domain or cross-system translation; and require the negative-evidence weight to change prospectively when the search geometry changes.**

If this ordering supplies no cleaner discrimination, transfer, falsifier, search-design improvement, inference, or decision beyond the receiving domain or operational system's ordinary model, 28E at that application reduces to synthesis/translation.

## 13. Canonical integration

This module composes with:

- [28D — Evidence Semantics and Claim-Promotion Guard](28D_EVIDENCE_SEMANTICS_AND_CLAIM_PROMOTION_GUARD.md);
- [24B — Strongest Fair Null and Relational Specificity](24B_STRONGEST_FAIR_NULL_AND_RELATIONAL_SPECIFICITY.md);
- [31 — Context-Conditioned State Comparison and Observability](31_CONTEXT_CONDITIONED_STATE_COMPARISON_AND_OBSERVABILITY.md);
- [33S4 — Address Sufficiency, Predictive Closure, and Reachable-Future Geometry](33S4_ADDRESS_SUFFICIENCY_PREDICTIVE_CLOSURE_AND_REACHABLE_FUTURE_GEOMETRY.md);
- [34 — Research Object Identity, Release Integrity, and Reproducibility](34_RESEARCH_OBJECT_IDENTITY_RELEASE_INTEGRITY_AND_REPRODUCIBILITY.md);
- [29 — MKUFT Scientific Tightening and Claim Discipline](29_MKUFT_SCIENTIFIC_TIGHTENING_AND_CLAIM_DISCIPLINE.md).

It changes no frozen DOI-bearing publication.

## 14. Compressed rule

> **Absence is evidence only through an addressed search. Ask whether the predicted trace should have survived, remained accessible, fallen inside the actual coverage, and been resolvable by the declared readout. Weak detectability weakens a null but does not support the missing object. Strong detectability can make a clean null powerful. Never invent detectability, never count dependent searches as independent, and let the receiving domain or operational system's native model win when it already closes the inference more cleanly.**
