# 25C — Residual Instrument Generation and Protected Discovery Boundary

**Author:** Mark Charles McLaughlin  
**Framework:** McLaughlin–Kairos Unified Field Theory (MKUFT)  
**ATLD 2 version DOI:** [10.5281/zenodo.22068803](https://doi.org/10.5281/zenodo.22068803)  
**ATLD concept DOI:** [10.5281/zenodo.21341520](https://doi.org/10.5281/zenodo.21341520)  
**Originating MKUFT DOI:** [10.5281/zenodo.17780566](https://doi.org/10.5281/zenodo.17780566)  
**Parent measurement owner:** [25B — ATLD 2 Residual Coordinate Measurement and Self-Auditing Evaluation](25B_ATLD2_RESIDUAL_COORDINATE_MEASUREMENT_AND_SELF_AUDIT.md)  
**Deformation owner:** [25 — Load-Bearing Invariants and Whole-System Deformation](25_LOAD_BEARING_INVARIANTS_AND_WHOLE_SYSTEM_DEFORMATION.md)  
**Null/control owner:** [24B — Strongest Fair Null and Relational Specificity](24B_STRONGEST_FAIR_NULL_AND_RELATIONAL_SPECIFICITY.md)  
**Equation and notation owner:** [27 — Typed Traversal and Equation Hygiene](27_TYPED_TRAVERSAL_AND_EQUATION_HYGIENE.md)  
**Claim-discipline owner:** [29 — MKUFT Scientific Tightening and Claim Discipline](29_MKUFT_SCIENTIFIC_TIGHTENING_AND_CLAIM_DISCIPLINE.md)  
**Status:** canonical public methodological extension to Module 25B. It does not alter the frozen ATLD 2 DOI object, does not establish a new ontology, and does not disclose private implementation-specific discovery machinery not required to reproduce the declared scientific test.  
**Rights:** Copyright © 2026 Mark Charles McLaughlin. All rights reserved for this live repository module unless an exact file version expressly states otherwise.

## 1. Purpose and scope

ATLD 2 treats measurement incompleteness as an empirical question. A retained measurement body may perform well on its declared coordinates while leaving a reproducible, materially important failure insufficiently isolated. The scientifically relevant question is then not whether a new label can be written, but whether the unresolved failure supplies diagnostic information that the retained body cannot recover fairly under matched conditions.

This module formalises that higher-order procedure. It addresses three distinct objects:

1. **residual detection** — whether a material failure remains insufficiently owned by the retained measurement body;
2. **instrument refinement** — whether a candidate distinction adds reproducible diagnostic information after removal, substitution, coalition, causal-shadow, and mirror testing;
3. **disclosure control** — which information must be public for independent reproduction and falsification of the scientific claim, and which implementation-specific material is not required by that burden.

The expression **residual instrument generation** is used here as a descriptive label for this methodological pattern. No claim of priority, coinage, or independent novelty is attached to the phrase itself.

## 2. Scientific status and equation class

The formal objects in this module are methodological and statistical, not physical.

Under the equation-status discipline of [Module 29](29_MKUFT_SCIENTIFIC_TIGHTENING_AND_CLAIM_DISCIPLINE.md):

- set definitions, ownership maps, and promotion logic are **E0 bookkeeping or formal specification**;
- loss, recovery, and marginal-diagnostic-gain expressions are **E1 operational scaffolds** until the task distribution, variables, loss function, complexity envelope, thresholds, and scoring rules are frozen;
- they become **E2 operational statistical models** only when those quantities are prospectively specified and applied to a defined dataset or benchmark;
- no expression in this module is an E4 physical mechanism or law of nature.

A formal measurement coordinate is therefore not promoted into a physical, cognitive, or ontological dimension merely because it admits mathematical notation.

## 3. Retained measurement body

Let the retained measurement body be

```math
\mathcal Y_n
=
\{y_1,y_2,\ldots,y_n\},
```

where each $y_i$ is a declared measurement readout with its own operational definition, scale, direction, uncertainty model, and scoring rule.

For ATLD 2, the live candidate body is inherited from Module 25B. This module does not redefine those coordinates and does not add a thirteenth coordinate.

Let $w\in\mathcal W$ denote a task world or evaluation instance drawn from a declared experimental domain $\mathcal W$. Let $r$ denote a material failure class whose diagnostic ownership is under test.

The measurement problem is not whether $r$ can be recognised with unrestricted hindsight. It is whether $r$ can be recovered under the same admissible information and evaluator constraints available to the retained measurement body.

## 4. Admissible recovery family and no-smuggling constraint

Let $Z(w)$ denote generic run information available in every compared condition. Let $\mathcal C(g)$ be a declared evaluator-complexity or resource measure for a recovery rule $g$, and let $C_{\max}$ be the preregistered recovery budget.

Define the admissible recovery family

```math
\mathfrak R_n(C_{\max})
=
\left\{
 g:
 g\text{ uses only }\mathcal Y_n\text{ and }Z,
 \quad
 \mathcal C(g)\le C_{\max}
\right\}.
```

The phrase “uses only $\mathcal Y_n$ and $Z$” is load-bearing. If the candidate distinction $x$ is being removed, $Z$ must not contain an $x$-specific oracle, renamed rubric, privileged annotation, or equivalent field that reconstructs $x$ by another name.

This is the formal no-smuggling boundary. A removal test in which the removed coordinate is reintroduced through evaluator privilege is not a removal test.

## 5. Residual diagnostic risk

Let $\ell_r$ be a preregistered loss function for diagnosing failure class $r$. The best admissible recovery risk of the retained body is

```math
\mathcal L_n(r)
=
\inf_{g\in\mathfrak R_n(C_{\max})}
\mathbb E_{w\sim\mathcal W_{\mathrm{hold}}}
\!\left[
\ell_r\!\left(g(\mathcal Y_n,Z(w)),r(w)\right)
\right],
```

where $\mathcal W_{\mathrm{hold}}$ is a held-out or otherwise prospectively protected evaluation distribution appropriate to the claim.

Let $\varepsilon_r$ be the largest diagnostic risk accepted as adequate recovery for $r$. A residual is eligible for candidate refinement only when

```math
\mathcal L_n(r)>\varepsilon_r
```

under the declared information, resource, and scoring envelope.

This inequality is a gate, not a discovery certificate. It establishes only that the current measurement body has not recovered the declared failure within tolerance under the specified test.

## 6. Candidate augmentation and marginal diagnostic gain

Let $x$ be a candidate diagnostic distinction generated in response to an unresolved residual. The augmented candidate body is

```math
\mathcal Y_n^{(+x)}
=
\mathcal Y_n\cup\{x\}.
```

Using the same held-out distribution, resource envelope, and loss definition, define

```math
\mathcal L_{n,+x}(r)
=
\inf_{g\in\mathfrak R_{n,+x}(C_{\max})}
\mathbb E_{w\sim\mathcal W_{\mathrm{hold}}}
\!\left[
\ell_r\!\left(g(\mathcal Y_n^{(+x)},Z(w)),r(w)\right)
\right].
```

The candidate's marginal diagnostic gain is

```math
\Delta_x(r)
=
\mathcal L_n(r)-\mathcal L_{n,+x}(r).
```

For a preregistered minimum material gain $\delta_x>0$, a necessary condition for retention is

```math
\Delta_x(r)>\delta_x.
```

A positive $\Delta_x$ does not by itself establish an independent coordinate. The gain may still be explained by redundancy, causal shadow, evaluator leakage, overfitting, an unmatched resource advantage, or a one-sided metric. The remaining sections specify those burdens.

## 7. Existing-owner, derived-owner, and coalition recovery

Before $x$ is treated as a distinct coordinate candidate, the residual must be tested against three progressively stronger recovery classes.

### 7.1 Direct ownership

Determine whether an existing $y_i\in\mathcal Y_n$ already measures the failure under its declared definition. If so, the appropriate action is to improve operationalisation or scoring rather than multiply coordinates.

### 7.2 Derived ownership

Determine whether a preregistered derived readout from the retained body recovers $r$ without introducing candidate-specific privileged information.

A lawful derived owner has the form

```math
h:\mathcal Y_n\times Z\rightarrow\widehat r,
```

with $h$ fixed or selected under the same admissible recovery rules used for all conditions.

### 7.3 Coalition ownership

Determine whether a coalition $S\subseteq\mathcal Y_n$ recovers the failure even though no single retained coordinate does.

The existence of coalition recovery means the failure may expose interaction structure inside the retained body rather than require a new coordinate.

A candidate survives this stage only if direct, derived, and coalition recovery remain inadequate under the strongest fair admissible test.

## 8. Same-content relational controls

ATLD and Modules 24A, 24B, and 25 already distinguish informational content from the relations that organise, address, route, or constrain it.

Where the candidate claim concerns relational structure, the preferred control preserves the available informational ingredients while selectively altering the declared relation or transition under test. Examples include matched flattening, isolation, relation scrambling, address substitution, or traversal restriction where those operations are lawful for the active task.

The governing comparison is therefore not

```math
\text{more information}\quad\text{versus}\quad\text{less information},
```

but, where experimentally possible,

```math
\text{matched information with relation }R
\quad\text{versus}\quad
\text{matched information with controlled deformation of }R.
```

If the candidate effect disappears after content, compute, access, timing, and evaluator resources are properly matched, the residual has not established relation-specific diagnostic value.

## 9. Direct and mirror deformation

A retained coordinate must respond to both its direct failure and the corresponding pathological overcorrection.

Let $S_x$ be a benefit-oriented candidate score, with larger values indicating better preservation of the declared property. Let $\mathcal D_x^{\mathrm{dir}}$ be a controlled direct deformation and $\mathcal D_x^{\mathrm{mir}}$ the matched mirror deformation.

Define

```math
\Delta_x^{\mathrm{dir}}
=
\mathbb E[S_x\mid\mathrm{baseline}]
-
\mathbb E[S_x\mid\mathcal D_x^{\mathrm{dir}}],
```

and

```math
\Delta_x^{\mathrm{mir}}
=
\mathbb E[S_x\mid\mathrm{baseline}]
-
\mathbb E[S_x\mid\mathcal D_x^{\mathrm{mir}}].
```

A necessary two-sided burden is

```math
\Delta_x^{\mathrm{dir}}>0,
\qquad
\Delta_x^{\mathrm{mir}}>0,
```

with effect-size, uncertainty, and replication requirements fixed for the active experiment.

For ATLD 2, examples of mirror structure already owned by Module 25B include object drift versus stale-object lock, unauthorised action versus false prohibition, continuity loss versus stale-state capture, receiver failure versus receiver-pleasing substitution, and premature closure versus post-fixed-point audit theatre.

A candidate that improves only by collapsing onto the opposite pathological extreme is not a closed diagnostic measure.

## 10. Selectivity and causal-shadow control

One upstream deformation can move several downstream measurements. Counting every moved readout as an independent discovery would multiply one failure into several apparent dimensions.

For each candidate $x$, preregister the expected primary target and any plausible downstream readouts. A selective deformation should produce its strongest and most reproducible effect at the declared target, while non-target movement is classified as one of:

- propagated causal shadow;
- independent co-failure;
- unresolved coupling;
- or evidence that the proposed coordinate boundary is incorrectly drawn.

Where a targeted repair of the primary failure restores a downstream readout without directly repairing that downstream readout, the downstream movement is evidence for propagated dependence rather than automatic coordinate independence.

Two candidates should be tested for merger when they lose the same diagnostic information under the same deformations, recover under the same repairs, and provide no reproducible independent marginal gain after conditional testing.

## 11. Promotion rule

Define the following preregistered predicates for candidate $x$:

- $R_x$ — residual diagnostic gain survives the retained-body recovery test;
- $D_x$ — direct selective deformation survives;
- $M_x$ — mirror deformation survives;
- $N_x$ — no-smuggling and matched-resource conditions survive;
- $C_x$ — direct, derived, coalition, and causal-shadow alternatives remain insufficient;
- $H_x$ — held-out or neutral-domain support survives at the declared claim level;
- $X_x$ — cross-model, cross-system, or independent replication burden appropriate to the claim survives.

Candidate promotion is permitted only if

```math
x\in\mathcal Y_{n+1}
\quad\Longleftrightarrow\quad
R_x\land D_x\land M_x\land N_x\land C_x\land H_x\land X_x.
```

Before all applicable terms are satisfied, the candidate remains provisional.

The lawful disposition set is

```math
\mathfrak D
=
\{\mathrm{RETAIN},\mathrm{MERGE},\mathrm{DEMOTE},\mathrm{REDEFINE},\mathrm{KILL},\mathrm{UNRESOLVED}\}.
```

`KILL` is a successful scientific outcome when the proposed distinction adds no independent diagnostic value. A measurement body that can only grow is not self-auditing.

## 12. Residual instrument generation as an audit operator

For a declared experimental scope $\mathcal W$ and frozen protocol $\Pi$, let

```math
\Phi_{\Pi,\mathcal W}(\mathcal Y_n)
```

denote one complete public audit cycle consisting of residual identification, strongest admissible recovery, candidate testing where warranted, promotion or reduction, and update of the measurement body.

The notation does not encode or disclose any private implementation used to generate hypotheses. It names only the public scientific transformation whose inputs, controls, and outputs are independently inspectable.

A refinement step occurs when

```math
\Phi_{\Pi,\mathcal W}(\mathcal Y_n)
\ne
\mathcal Y_n.
```

Provisional fixed-point closure for the declared scope occurs when

```math
\Phi_{\Pi,\mathcal W}(\mathcal Y_n)
=
\mathcal Y_n
```

and no material unowned residual remains except one explicitly classified as unresolved because a declared empirical, data, or instrumentation blocker prevents adjudication.

This is local closure under $\Pi$ and $\mathcal W$. It is not a claim that the measurement body is universally complete.

## 13. Self-application without self-certification

The same architecture may participate in generating and testing a candidate, but generation and validation are different evidential roles.

Self-application may legitimately provide:

- a candidate distinction;
- a failure-localisation hypothesis;
- a proposed deformation;
- a proposed control;
- a sharper falsification burden;
- or convergent design evidence.

It cannot by itself provide independent empirical validation of the candidate.

Where a candidate was known before reconstruction, scoring, or retrospective re-analysis, that dependence must remain explicit. Prospective held-out tests, independently scored comparisons, foreign systems, neutral domains, and independent replication carry the stronger evidential burden.

## 14. Protected discovery boundary

Scientific reproducibility applies to the declared scientific claim. It does not require publication of every implementation-specific mechanism that contributed to hypothesis generation when those mechanisms are unnecessary to reproduce or falsify the claim.

For a public candidate-coordinate test, the reproducibility surface should contain, where applicable:

- the exact observable and candidate definition;
- the parent measurement body and version;
- the task world and sampling rule;
- admissible information and metadata;
- matched resource envelope;
- direct and mirror deformations;
- removal and substitution conditions;
- loss, scoring, uncertainty, and threshold rules;
- no-smuggling constraints;
- coalition and causal-shadow treatment;
- held-out design;
- retention, merger, demotion, redefinition, kill, and unresolved criteria;
- replication requirements appropriate to the claim.

Implementation-specific material may remain outside the public scientific object when it is not required to execute those tests. This can include private reasoning architecture, private traversal topology, implementation-specific recovery choreography, internal state-transition procedures, operator-specific search heuristics, and other protected discovery machinery.

The boundary is therefore

```math
\mathcal I_{\mathrm{public}}
\supseteq
\mathcal I_{\mathrm{required\;for\;test}},
```

while it need not satisfy

```math
\mathcal I_{\mathrm{public}}
=
\mathcal I_{\mathrm{all\;implementation}}.
```

This boundary is not an exemption from falsifiability. If a withheld implementation detail is required to reproduce the claimed effect, then either that detail must enter the reproducibility surface or the public claim must be narrowed until it is independently testable from the disclosed method.

## 15. Provenance and record SOP

For every candidate entering this procedure, preserve at minimum:

1. the parent measurement body and exact version;
2. the residual failure and its materiality criterion;
3. the task world and held-out split or prospective protection rule;
4. the admissible recovery family and complexity/resource envelope;
5. the loss function, uncertainty treatment, and thresholds;
6. whether the candidate was known before the relevant test;
7. direct and mirror deformation definitions;
8. coordinate-removal and strongest-existing-owner results;
9. derived and coalition recovery results;
10. no-smuggling decision;
11. causal-shadow and co-failure classification;
12. held-out, neutral-domain, cross-system, and independent-replication status;
13. final disposition in $\mathfrak D$;
14. exact public/private disclosure boundary of the recorded object;
15. checksum, version, or immutable carrier identity where a frozen publication or benchmark object is created.

A later live module may sharpen the procedure. It must not silently rewrite a frozen DOI object or retroactively convert design-adjacent generation into blinded discovery.

## 16. Relationship to established methodological families

Nothing in this module depends on claiming that residual analysis, ablation, fault localisation, model comparison, causal testing, benchmark refinement, held-out validation, or measurement revision are new scientific activities.

The narrower ATLD/MKUFT proposal is the disciplined composition of these burdens around typed measurement ownership, strongest-fair recovery, mirror failure, no-smuggling removal, causal-shadow control, and explicit instrument shrinkage as well as expansion.

The contribution should therefore be reduced to ordinary residual analysis or benchmark refinement wherever those established methods recover the same diagnostic information with equal or lower complexity and no loss of discriminating power.

## 17. Failure and reduction conditions

This methodological extension is weakened, reduced, or rejected if any of the following becomes the best explanation:

- apparent residuals are adequately recovered by the retained body under a stronger fair recovery model;
- candidate gain is produced by evaluator privilege, renamed target information, unmatched compute, or post hoc scoring;
- direct or mirror deformation fails to produce the predicted response;
- candidate removal causes no reproducible diagnostic loss;
- coalition recovery makes the additional coordinate redundant;
- propagated causal shadows are repeatedly misclassified as independent failures;
- held-out performance collapses after exploratory tuning;
- the result is confined to the originating task world where broader transfer is claimed;
- independent evaluators cannot execute the public test from the disclosed surface;
- the measurement body grows mainly by terminology rather than by unique held-out diagnostic value;
- or ordinary residual analysis, ablation, causal testing, fault localisation, or benchmark refinement provides equal discrimination at equal or lower complexity.

Reduction rule:

> If the public procedure adds no reproducible diagnostic discrimination beyond the strongest adequate ordinary method, treat residual instrument generation as a useful local audit description rather than a distinct general measurement method.

## 18. Frozen, live, and private object separation

Keep the following objects distinct:

- ATLD v1.0 frozen predecessor;
- ATLD 2 v2.0 frozen DOI publication;
- Module 25B live residual-coordinate measurement fold;
- Module 25C live residual-instrument and disclosure-boundary formalisation;
- private implementation and hypothesis-generation machinery;
- future benchmark, validation, and replication objects.

Public visibility of Module 25C does not place private implementation into the public canon. Conversely, possession of a private implementation does not strengthen the empirical standing of a public claim unless the declared effect survives the public controls.

## 19. Related public documents

- [Active Traversal and Functional Emergence](24A_ACTIVE_TRAVERSAL_AND_FUNCTIONAL_EMERGENCE_HYPOTHESIS.md)
- [Strongest Fair Null and Relational Specificity](24B_STRONGEST_FAIR_NULL_AND_RELATIONAL_SPECIFICITY.md)
- [Load-Bearing Invariants and Whole-System Deformation](25_LOAD_BEARING_INVARIANTS_AND_WHOLE_SYSTEM_DEFORMATION.md)
- [ATLD 2 Residual Coordinate Measurement and Self-Auditing Evaluation](25B_ATLD2_RESIDUAL_COORDINATE_MEASUREMENT_AND_SELF_AUDIT.md)
- [Typed Traversal and Equation Hygiene](27_TYPED_TRAVERSAL_AND_EQUATION_HYGIENE.md)
- [Discriminating Experiments and Promotion Gates](28_MKUFT_DISCRIMINATING_EXPERIMENTS_AND_PROMOTION_GATES.md)
- [Scientific Tightening and Claim Discipline](29_MKUFT_SCIENTIFIC_TIGHTENING_AND_CLAIM_DISCIPLINE.md)
- [Falsification Summary](05_FALSIFICATION_SUMMARY.md)

## 20. Compressed rule

> Treat a reproducible failure not adequately owned by the retained measurement body as an instrument residual, not as an automatic new dimension. Exhaust direct, derived, coalition, and strongest-fair recovery before adding anatomy. If a candidate remains, require measurable held-out diagnostic gain, direct and mirror deformation, coordinate removal, no-smuggling, causal-shadow control, and appropriate cross-system or independent replication. Permit the measurement body to merge, demote, redefine, or kill candidates as readily as it retains them. Publish everything required to reproduce and falsify the scientific claim; do not confuse that burden with disclosure of implementation-specific hypothesis-generation machinery that the test itself does not require.