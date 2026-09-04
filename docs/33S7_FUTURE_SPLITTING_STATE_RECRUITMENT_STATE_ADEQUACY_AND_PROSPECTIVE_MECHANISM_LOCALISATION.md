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
**Minimum-decisive flagship implementation:** [28C — History-Dependent HCP Magnesium Mechanics](28C_FSAI_FSSR_MINIMUM_DECISIVE_FLAGSHIP_HCP_MAGNESIUM_PROTOCOL.md)  
**HCP flagship v1.0 publication route:** [paper route](../papers/2026-09-04_FSSR_HCP_MAGNESIUM_MINIMUM_DECISIVE_PROTOCOL_v1.0.md) · published DOI [`10.5281/zenodo.22309144`](https://doi.org/10.5281/zenodo.22309144)  
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

## 4A. The challenge and boundary are addressed objects too

A future split cannot be assigned to hidden state merely because two samples were labelled as receiving the same perturbation. The state, the challenge, the boundary/environment and the declared stochastic model are separate objects and must be made equivalent at the resolution required by the target.

For a pair `h,h'`, the positive FSSR burden is therefore not only

```text
Theta(h) = Theta(h')
→ different futures
```

but, as far as the native experiment permits,

```text
matched declared state
+ matched challenge/intervention at load-bearing coordinates
+ matched boundary/environment class
+ declared measurement and stochastic uncertainty
→ future divergence beyond tolerance
```

A nominally identical cold shock, drug pulse, load path, optical propagation, control input or other intervention is not automatically an identical experimental object. Dose, timing, duration, spatial delivery, phase, instrument burden, environment, forcing history and other target-relevant coordinates may belong to the challenge or boundary rather than to the system state.

Accordingly, an observed split first opens a typed audit over at least these candidate locations:

```text
state mismatch / omitted state
challenge mismatch / intervention geometry
boundary or environment mismatch
measurement / registration error
already-licensed stochastic spread
probe induction
```

This is where negative space becomes experimental information. Every adequately controlled alternative that fails to explain the split removes explanatory territory. If tighter challenge matching removes the effect, the split was not evidence for hidden system state. If environment control removes it, the environment carried the distinction. If the split remains fully inside the model's declared stochastic distribution, state closure has not failed. If those explanations are progressively excluded and a structured residual remains, the burden on the candidate state representation increases.

The low state is equally load-bearing. A strong separating challenge that produces **no material split beyond the declared uncertainty and tolerance** supports provisional preservation of the simpler representation for that target, regime and challenge family:

```text
strong lawful separating challenge
+ no material future split
→ no recruitment burden from that test
→ preserve current compression provisionally
```

This does not prove the representation is universally complete. It says the current attack did not expose a target-relevant distinction. FSSR is therefore bidirectional: it can earn reopening when equivalence fails and earn preservation when equivalence survives.

> **Do not ask only whether the systems split. Ask whether the state, the poke, the boundary and the allowed uncertainty were equivalent enough that the split has somewhere legitimate to land. Then use both the surviving residual and the eliminated alternatives as data.**

## 4B. Observer/registration closure through SIPO

The FSSR test is not complete until the **registration address** is carried with the state, challenge and boundary. A future can only be said to split relative to a declared target and a declared family of measurements or records capable of resolving that target.

In MKUFT, `O` is used conservatively here as the observer/registration position: the operational readout, record or measurement context through which a physical continuation becomes available to the analysis. This does **not** mean that a conscious observer is assumed to create the split. Where measurement has physical back-action, that interaction belongs to the P-layer instrument; where it is effectively passive for the target, the relevant P-state is unchanged to the declared tolerance.

Module 31 states the observability condition explicitly. If two physical states `x,x'` are indistinguishable under the declared admissible readout family,

```math
x\sim_O x'
\quad\Longleftrightarrow\quad
\mathcal R_{O,q}(x)=\mathcal R_{O,q}(x')
\quad\forall q\in\mathcal Q_O^{\mathrm{adm}},
```

then the experiment has not yet resolved a distinction at that O-address. For stochastic or noisy measurements, the corresponding output distributions and preregistered tolerance control.

The target-relative condition is stronger than simply seeing different raw records. A difference matters to FSSR only when unresolved states inside one O-equivalence class still separate the declared future target beyond tolerance. If the target factors through the O-resolved quotient, distinctions hidden below that readout are irrelevant to the declared target and do not force reopening.

This closes FSSR back into the [SIPO Capstone](33_SIPO_CAPSTONE_CONSTRAINT_CONDITIONED_ADDRESSED_UPDATE_LAW.md). SIPO already types the cycle as

```text
current addressed S/I/P/O state + context/history
→ typed admissibility descriptor
→ assemble active P-law object
→ propagate physically
→ P→(P,O) instrument produces the realised physical state and registration record
→ realised path + record + context readdress the next state
→ repeat
```

FSSR occupies a controlled test inside that cycle:

```text
candidate addressed state
→ choose a lawful separating challenge
→ propagate under the declared P-law and boundary
→ register the continuation through a declared P→(P,O) instrument/readout
→ compare target-relevant future distributions
→ split beyond tolerance OR no material split
→ use controls/negative space to localise the result
→ recruit the smallest typed distinction if required, otherwise preserve
→ Readdress updates state/history/context for the next SIPO cycle
```

The observer therefore has two disciplined roles in this assay:

1. **resolution:** it specifies what can actually be distinguished by the declared measurement family;
2. **return:** the registered outcome becomes part of the evidence/history used by `Readdress` to decide whether the next addressed state should preserve its current compression or recruit an additional distinction.

No stronger observer-dependent physical mechanism is inherited from this bookkeeping. An independent O-linked physical effect would require its own measurable carrier, baseline and falsifier.

> **FSSR is not only state → poke → future. The complete loop is addressed state + addressed challenge + boundary + physical propagation + addressed registration → target-relative split or closure → negative-space localisation → preserve or minimally readdress → next SIPO law object.**

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

The full minimum-decisive implementation is now specified in [28C — History-Dependent HCP Magnesium Mechanics](28C_FSAI_FSSR_MINIMUM_DECISIVE_FLAGSHIP_HCP_MAGNESIUM_PROTOCOL.md). It preserves the flagship target below but upgrades the execution burden: the confirmatory state must be the strongest practical predeclared domain-native reduced state rather than a straw-man macroscopic state; the FSSR challenge faces a matched parameter-information design; one primary reverse-loading trajectory is frozen; candidate repairs are predeclared and physically typed; computational and physical deformation are kept separate; and state-sufficiency, challenge-design, mechanism-localisation and prospective-lead verdicts cannot promote one another.

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

FSSR closes both **downstream into an experiment** and **upstream back into the addressed SIPO state**. The experiment is not the end of the architecture; its registered result is one input to the next law-selection cycle.

The full return is:

```text
addressed S/I/P/O state + history/context
→ admissible future/challenge family
→ choose a lawful separating challenge
→ active P-law + boundary generate a physical continuation
→ declared P→(P,O) instrument/readout registers that continuation
→ target-relative future split or closure is assessed at the declared O-resolution
→ control failures and eliminated alternatives provide negative-space localisation
→ if required, recruit the smallest typed state/history/boundary distinction that restores held-out closure
→ if no material split survives, preserve the simpler address provisionally
→ Readdress incorporates realised path, O-record, context and retained history
→ next effective possibility/admissibility state
→ next SIPO law object.
```

This means FSSR is neither merely a downstream methods paper nor an observer claim. It is an experimental specialisation of the same Layer-Before-Law recursion: the current address determines which law/challenge is meaningful, physical propagation generates the continuation, the declared registration surface determines what distinction is actually observable, and the result returns upstream to test whether the address used to choose the law was sufficient.

The loop is therefore bidirectional in scientific use:

```text
ADDRESS → LAW → FUTURE → REGISTRATION
                       ↓
              SPLIT / NO SPLIT
                       ↓
READDRESS ← NEGATIVE-SPACE / CONTROL AUDIT
```

A split can force a finer address; a clean non-split can preserve the current compression. Neither outcome upgrades the whole framework by itself.

This makes FSSR a downstream experimental specialisation of 33S4–33S6 **and** an upstream diagnostic return into SIPO, not a competing architecture.

## 13. Public routes

- [Published FSSR v1.0 — Zenodo](https://doi.org/10.5281/zenodo.22058303)
- [FSSR public paper route](../papers/2026-08-22_FUTURE_SPLITTING_STATE_RECRUITMENT_v1.0.md)
- [Minimum Decisive FSAI/FSSR Flagship — HCP Magnesium](28C_FSAI_FSSR_MINIMUM_DECISIVE_FLAGSHIP_HCP_MAGNESIUM_PROTOCOL.md)
- [FSSR standalone publication record](../FSSR_STANDALONE_PUBLICATION.md)
- [AAF parent publication](https://doi.org/10.5281/zenodo.22031333)
- [Papers and Publications index](../papers/README.md)

## 14. Standing invariant

> **Do not ask only whether a model predicts well. Ask whether histories it calls the same can be made to behave differently under a lawful future. Address the state, challenge, boundary, registration surface and allowed uncertainty at the resolution the target requires. If a future split survives those controls beyond tolerance, use the eliminated alternatives as negative-space information, recruit the smallest physically typed distinction that restores held-out closure, and return that registered result through SIPO readdressing before assembling the next law object. If a strong separating challenge produces no material split, preserve the simpler state provisionally at that declared scope. Observer/registration determines what distinction is actually available to the analysis; it does not by itself supply a new physical mechanism.**