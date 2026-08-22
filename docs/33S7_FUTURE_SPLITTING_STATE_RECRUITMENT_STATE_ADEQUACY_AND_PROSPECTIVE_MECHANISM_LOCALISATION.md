# 33S7 — Future-Splitting State Recruitment, State Adequacy, and Prospective Mechanism Localisation

**Author:** Mark Charles McLaughlin  
**Framework:** McLaughlin–Kairos Unified Field Theory (MKUFT)  
**Current principal MKUFT publication:** [10.5281/zenodo.21973064](https://doi.org/10.5281/zenodo.21973064)  
**MKUFT concept DOI:** [10.5281/zenodo.17780565](https://doi.org/10.5281/zenodo.17780565)  
**FSSR standalone publication:** [10.5281/zenodo.22058303](https://doi.org/10.5281/zenodo.22058303)  
**FSSR concept DOI:** [10.5281/zenodo.22058302](https://doi.org/10.5281/zenodo.22058302)  
**Citation and provenance:** [PROVENANCE_DOI_AND_ATTRIBUTION.md](../PROVENANCE_DOI_AND_ATTRIBUTION.md)  
**Architectural parent:** [33 — SIPO Capstone](33_SIPO_CAPSTONE_CONSTRAINT_CONDITIONED_ADDRESSED_UPDATE_LAW.md)  
**Address-sufficiency parent:** [33S4 — Address Sufficiency, Predictive Closure, and Reachable-Future Geometry](33S4_ADDRESS_SUFFICIENCY_PREDICTIVE_CLOSURE_AND_REACHABLE_FUTURE_GEOMETRY.md)  
**Rate/history parent:** [33S5 — Rate-Conditioned Addressing, Time-Parameterised Traversal, and Adaptive Reorganisation](33S5_RATE_CONDITIONED_ADDRESSING_TIME_PARAMETERISED_TRAVERSAL_AND_ADAPTIVE_REORGANISATION.md)  
**Future-equivalence parent:** [33S6 — Addressed Admissible Futures](33S6_ADDRESSED_ADMISSIBLE_FUTURES_RESTORATIVE_REACHABILITY_AND_LOAD_BEARING_FUTURE_GEOMETRY.md)  
**Observability support:** [31 — Context-Conditioned State Comparison and Observability](31_CONTEXT_CONDITIONED_STATE_COMPARISON_AND_OBSERVABILITY.md)  
**Promotion/falsification support:** [28 — Discriminating Experiments and Promotion Gates](28_MKUFT_DISCRIMINATING_EXPERIMENTS_AND_PROMOTION_GATES.md)  
**Public formulation date:** 22 August 2026  
**Rights:** Copyright © 2026 Mark Charles McLaughlin. All rights reserved unless an exact later publication states otherwise.  
**Status:** canonical experimental specialisation of the 33S4–33S6 future-sufficiency family. It turns future-equivalence into a direct assay of state adequacy, defines state recruitment by independently confirmed failure plus minimal typed repair, and tests whether recruitment can prospectively localise an emerging physical mechanism. It is not a separate law stack, a new force or field, or evidence of autonomous information-to-physical coupling.

## 1. Purpose and placement

Modules 33S4–33S6 already establish the parent architecture:

```text
candidate Address
→ target-relative predictive closure
→ future-equivalence class
→ admissible future
→ realised transition
→ recursive readdressing.
```

FSSR adds one operational question:

> **Can a lawful future be chosen specifically to test whether histories currently assigned the same state really remain equivalent?**

If the answer is no, the candidate state remains adequate for the declared target, horizon, challenge family and tolerance. If the answer is yes, the representation has erased a distinction that the future still carries.

The compact module recursion is:

```text
same declared state
→ separating lawful future
→ future split
→ state inadequacy
→ minimal typed repair
→ closure restored
→ remove / restore deformation
→ recursive readdressing.
```

This is the canonical MKUFT owner for the live FSSR object. The Zenodo v1.0 paper is the frozen publication object; later changes to this module are later research states and are not silently backdated into that deposit.

## 2. Declared state-adequacy problem

Let `H_t` be retained history and let

```math
\Theta:\mathcal H\rightarrow\mathcal Z_{\Theta}
```

be a candidate state representation.

Fix before testing:

- target `q`;
- prediction horizon `\Delta`;
- admissible challenge/intervention family `\mathcal U`;
- environment and boundary class `E`;
- physical regime `\lambda`;
- discrepancy `d`;
- closure tolerance `\varepsilon_q`.

Two histories are target-relative future-equivalent when

```math
h\sim_{q,\Delta,\mathcal U,\lambda}h'
\iff
\mathcal L_{\lambda}(q^+_{\Delta}\mid h,u,E)
=
\mathcal L_{\lambda}(q^+_{\Delta}\mid h',u,E)
\quad\forall u\in\mathcal U.
```

The state claim is therefore

```math
\Theta(h)=\Theta(h')
\Longrightarrow
h\sim_{q,\Delta,\mathcal U,\lambda}h'.
```

Operationally:

> **Calling two histories the same state commits the model to there being no admissible declared future that materially separates them.**

## 3. Future-splitting residual

For histories collapsed by `\Theta`, define

```math
\delta_{q,\Delta}(h,h';u,\lambda)
=
d\!\left[
\mathcal L_{\lambda}(q^+_{\Delta}\mid h,u,E),
\mathcal L_{\lambda}(q^+_{\Delta}\mid h',u,E)
\right].
```

The closure residual is

```math
\boxed{
R_q(\Theta;\lambda,\Delta,\mathcal U)
=
\sup_{\substack{h,h':\Theta(h)=\Theta(h')\\u\in\mathcal U}}
\delta_{q,\Delta}(h,h';u,\lambda).
}
```

`\Theta` is `\varepsilon_q`-sufficient when

```math
R_q(\Theta;\lambda,\Delta,\mathcal U)\leq\varepsilon_q.
```

Two order relations are calibration facts rather than novelty claims.

State refinement cannot increase the exact same-state residual:

```math
\Theta_2\text{ lawfully refines }\Theta_1
\Longrightarrow
R_q(\Theta_2)\leq R_q(\Theta_1).
```

Challenge-family expansion cannot decrease the exact worst-case residual:

```math
\mathcal U_1\subseteq\mathcal U_2
\Longrightarrow
R_q(\Theta;\mathcal U_1)
\leq
R_q(\Theta;\mathcal U_2).
```

The exact invariant is partition refinement. A broader admissible future family can expose distinctions that were irrelevant under a narrower family. This does **not** imply that the number of continuous latent coordinates must monotonically increase; a fixed-dimensional state can sometimes be reparameterised to encode a finer partition.

## 4. Future-splitting challenge

FSSR does not ask for the most informative experiment in general. It asks for the admissible continuation that most strongly tests the claim that `\Theta` is already a state.

A development-stage challenge may be chosen by

```math
u^{\star}
\in
\arg\max_{u\in\mathcal U}
\widehat{\mathcal J}_{\mathrm{split}}(u;\Theta,\lambda),
```

where `\widehat{\mathcal J}_{\mathrm{split}}` scores future divergence inside matched or near-matched candidate-state fibres.

The challenge design is frozen before confirmatory evaluation.

This differs from parameter-identification design. Parameter information gain asks which experiment best identifies a model parameter. FSSR asks which experiment best exposes a false state equivalence. The two objectives may coincide in some systems; their reproducible dissociation is one of the paper's discriminating predictions.

## 5. Independent-continuation gate

The model whose state is being tested may not certify its own state adequacy.

A closed Markov surrogate can make two histories identical by construction and then necessarily predict identical futures from its own collapsed state. That is internal consistency, not external validation.

Confirmatory future divergence must therefore come from an independent continuation source:

- a microstate-resolved simulator not defined by `\Theta`;
- a separately validated higher-fidelity physical model;
- or the physical experiment itself.

This gate is mandatory for a positive FSSR claim.

## 6. State recruitment

Suppose `\Theta_0` is adequate in a baseline regime and later fails:

```math
R_q(\Theta_0;\lambda_0)\leq\varepsilon_q,
\qquad
R_q(\Theta_0;\lambda_1)>\varepsilon_q.
```

Let `c` be a preregistered physically typed candidate augmentation: a measurable scalar, vector, field summary, relational descriptor, history functional, boundary variable, or coalition.

Define a recruitment candidate by

```math
R_q(\Theta_0\oplus c;\lambda_1)\leq\varepsilon_q.
```

The preferred repair is the smallest candidate according to a declared cost `C(c)`:

```math
\boxed{
c^{\star}
\in
\arg\min_c C(c)
\quad\text{subject to}\quad
R_q(\Theta_0\oplus c;\lambda_1)\leq\varepsilon_q.
}
```

A **state-recruitment event** is credited only when all of the following hold:

1. the old state was previously certified under the declared regime;
2. independent confirmatory futures now split beyond tolerance;
3. a frozen typed augmentation restores held-out closure;
4. removing that augmentation reopens the failure;
5. restoring it closes the failure again;
6. near-state matching and ordinary hidden-state baselines do not explain the result more simply.

For a neural latent state, an arbitrary neuron or coordinate is not automatically a physical mechanism. Latent variables may only be identifiable up to an invertible or linear transformation. Mechanism-localisation language therefore requires a preregistered physical descriptor, invariant subspace, or experimentally measurable coalition that survives deformation tests.

## 7. Prospective recruitment prediction

Let `\lambda_R` be the earliest regime at which a new typed augmentation is required to restore closure and let `\lambda_T` be a preregistered conventional transition/mechanism marker.

Define recruitment lead

```math
\boxed{L=\lambda_T-\lambda_R.}
```

For time-resolved systems,

```math
\boxed{L_t=t_T-t_R.}
```

The principal prospective prediction is:

> **In systems where an emerging mechanism becomes future-discriminating before its conventional macroscopic marker is overt, a reproducible state-recruitment event can occur first, so that `L>0` or `L_t>0`.**

This is not asserted as universal. The prediction fails in systems where the mechanism and the conventional marker become informative simultaneously, where the candidate state already contains the relevant distinction, or where no stable physically typed repair exists.

## 8. Experimental triangle

The same FSSR object is instantiated in three domains without changing its type.

### 8.1 Holography — deterministic calibration

Two coherent fields can have the same intensity at one plane while differing in phase:

```math
U_j(x,y,0)=A(x,y)e^{i\phi_j(x,y)},
\qquad
|U_1|^2=|U_2|^2=A^2.
```

Under propagation `\mathcal P_z`,

```math
I_j(x,y,z)=|\mathcal P_z U_j|^2.
```

For generic phase differences, a later intensity readout separates the fields. An intensity-only state is therefore insufficient for that future; adding phase or the complex field restores deterministic closure.

This is a known-physics calibration of the assay, not an FSSR discovery of optical phase.

### 8.2 Single-cell dynamics — independent natural-system anchor

Single-cell fate work supplies systems where present position, state velocity, phase and retained history can carry different future information. The FSSR burden is not to rediscover that history matters. It is to locate the earliest held-out time at which a previously adequate state begins to require one of those additions and to test whether recruitment precedes a preregistered overt fate marker.

### 8.3 History-dependent constitutive mechanics — prospective flagship

The flagship target is a learned history-dependent constitutive model for HCP magnesium or a comparable material with rich microstate-resolved continuation data.

The protocol is:

```text
certify a baseline state
→ find near-matched histories collapsed by that state
→ design a bounded lawful continuation that maximises future splitting
→ freeze the challenge
→ confirm the split independently
→ search a preregistered physical candidate library
→ identify the smallest repair
→ remove / restore
→ test whether recruitment precedes the conventional mechanism marker.
```

Candidate physical repairs may include twin volume fraction, slip-system activity summaries, hardening variables, local texture descriptors, temperature-history summaries, or another domain-justified measurable descriptor.

The specific prospective wager is that a twinning/detwinning or related mechanism can become future-discriminating before the ordinary macroscopic constitutive signature is fully overt, and that a twinning/slip-related descriptor will be among the minimal typed repairs where that regime is correctly selected.

## 9. Strongest fair nulls

A positive FSSR result must beat the strongest ordinary alternatives.

### Null A — ordinary state incompleteness

A standard measured physical variable omitted by poor feature selection explains the split. If adding that variable closes the future and no additional FSSR structure remains, the result is ordinary state reconstruction.

### Null B — matching artefact

The two histories were not sufficiently matched in the declared candidate state. Tightening the matching rule removes the split.

### Null C — surrogate tautology

The same model both defines and certifies the state. Independent continuation removes the apparent result.

### Null D — probe induction

The challenge creates the mechanism rather than revealing a pre-existing future distinction. The effect disappears under nested perturbation budgets or passive confirmation.

### Null E — latent-coordinate non-identifiability

An arbitrary latent coordinate is mistaken for a physical mechanism. The purported localisation fails under allowed latent transformations or cannot be reproduced with a measurable physical descriptor.

### Null F — generic early warning

A conventional early-warning statistic predicts the same transition equally well without state-recruitment structure or mechanism localisation.

### Null G — parameter-design equivalence

Parameter information gain and state-splitting design always select equivalent probes and produce equivalent held-out outcomes after fair tuning. If so, the separate FSSR challenge objective has not earned itself.

## 10. Promotion and failure conditions

FSSR earns stronger status only if the same typed object survives across calibration and prospective tests.

A strong result requires:

- preregistered target, horizon, tolerance and challenge family;
- baseline certification before regime change;
- independent continuation;
- frozen challenge design;
- held-out future splitting;
- minimal typed repair;
- remove/restore deformation;
- ordinary baseline comparison;
- probe-induction controls;
- prospective timing relative to an independently defined transition marker.

The module is weakened or falsified for a claimed regime if:

- no lawful future separates the supposedly same states;
- splits disappear under adequate state matching;
- a stronger ordinary state model closes the future without the recruitment object;
- the proposed repair fails held-out restoration;
- the repair cannot be localised beyond arbitrary latent coordinates;
- the probe itself creates the transition;
- or the claimed lead vanishes under preregistered confirmation.

## 11. Layer boundary

AAF supplies an information/address criterion: which histories count as the same state for a declared future.

FSSR is the assay that tests that criterion against real trajectories.

The recruited coordinate belongs to the physical or domain-specific state only when it is measured, typed and empirically necessary for closure.

Therefore:

> **FSSR does not promote an information-layer equivalence relation into a new physical interaction. It identifies when a physical distinction omitted from the declared state has become necessary to preserve lawful future equivalence.**

A stronger I→P interpretation would require additional evidence beyond the present construction and must survive an adequate physical baseline first.

## 12. Recursive closure into MKUFT

FSSR closes back into the parent architecture as

```text
Address
→ admissible future family
→ challenge against current state equivalence
→ realised physical continuation
→ future split or closure
→ typed recruitment if required
→ readdressing
→ new admissible future family.
```

This makes FSSR a downstream experimental specialisation of 33S4–33S6, not a competing architecture.

## 13. Public routes

- [Published FSSR v1.0 — Zenodo](https://doi.org/10.5281/zenodo.22058303)
- [FSSR public paper route](../papers/2026-08-22_FUTURE_SPLITTING_STATE_RECRUITMENT_v1.0.md)
- [FSSR standalone publication record](../FSSR_STANDALONE_PUBLICATION.md)
- [AAF parent publication](https://doi.org/10.5281/zenodo.22031333)
- [Papers and Publications index](../papers/README.md)

## 14. Standing invariant

> **Do not ask only whether a model predicts well. Ask whether histories it calls the same can be made to behave differently under a lawful future. If they can, the state has failed. Repair the failure with the smallest physically typed information, prove the repair by deformation, and test whether nature demanded that information before the transition announced itself.**
