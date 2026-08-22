# Future-Splitting State Recruitment
## A Cross-Domain Assay for State Adequacy and Prospective Mechanism Activation

**Author:** Mark Charles McLaughlin  
**ORCID:** 0009-0005-7736-1511  
**Affiliation:** Independent Researcher  
**Framework lineage:** McLaughlin–Kairos Unified Field Theory (MKUFT) / Addressed Admissible Futures (AAF) / Typed Viability Traversal (TVT)  
**Status:** Published standalone Zenodo preprint — prospective empirical testing  
**Version:** 1.0  
**Publication date:** 22 August 2026  
**Version DOI:** [10.5281/zenodo.22058303](https://doi.org/10.5281/zenodo.22058303)  
**Concept DOI:** [10.5281/zenodo.22058302](https://doi.org/10.5281/zenodo.22058302)  
**Rights:** Copyright © 2026 Mark Charles McLaughlin. All rights reserved.

> **Version boundary.** The Zenodo object at DOI `10.5281/zenodo.22058303` is the frozen publication object for FSSR v1.0. This GitHub file is the public reader/source route and the live canonical specialisation is Module 33S7. Later repository revisions are later research states and are not silently backdated into the deposited PDF.

## Abstract

History-dependent dynamical systems are commonly modelled by augmenting observable state with latent or internal variables. Modern methods can learn such variables, select latent dimension, impose thermodynamic structure and optimise experiments for parameter identifiability; predictive-state formalisms define state by the futures a history supports under admissible inputs; and active-probing methods can expose approaching transitions. These results leave a narrower empirical question: can the **failure and repair of a state representation itself** serve as a prospective physical signal and mechanism-localisation instrument?

Future-Splitting State Recruitment (FSSR) provides a direct test. A candidate state map `Θ` is sufficient for target `q`, horizon `Δ`, regime `λ` and challenge family `U` only when histories mapped to the same state remain future-equivalent within a preregistered tolerance. A future-splitting challenge is an admissible continuation chosen to maximise divergence between futures of histories that `Θ` has merged. If confirmatory divergence exceeds tolerance under an independent continuation source, `Θ` has failed. The state is then augmented by the smallest preregistered, physically typed coordinate or coalition that restores predictive closure on held-out data; reproducible failure, restoration and remove/restore deformation define a **state-recruitment event**.

FSSR makes three discriminating predictions. First, where an emerging physical mechanism becomes future-discriminating before its conventional macroscopic marker is overt, recruitment can precede that marker. Second, recruitment can occur without a detectable change in snapshot intrinsic dimension because the missing distinction may reside in history, phase, boundary relation or another coordinate absent from the instantaneous observable manifold. Third, loading selected to falsify state adequacy need not coincide with loading selected to maximise parameter information. The paper specifies independent-continuation, near-state matching, probe-induction and nested-confirmation gates; a deterministic holographic calibration; a single-cell biological anchor; and a flagship test in learned history-dependent constitutive mechanics.

**Keywords:** Future-Splitting State Recruitment; FSSR; Addressed Admissible Futures; history dependence; internal variables; predictive state; constitutive modelling; state sufficiency; experimental design; active probing; early warning; mechanism activation; multiscale mechanics; readdressing.

## 1. Scientific placement

The ingredient-level territory is established. Projection methods show how unresolved degrees of freedom return as memory. Computational mechanics and predictive-state representations define states through predictive futures. State-identification theory uses input sequences to distinguish hidden states. Constitutive-learning methods learn internal variables and, in recent work, their effective dimension or identifiable subspace. Bayesian experimental design selects loading histories that maximise information about constitutive parameters. Active probing and early-warning methods can expose approaching transitions.

FSSR therefore does **not** claim novelty for memory, hidden variables, future-defined state, state identification, adaptive latent dimension, optimal loading, active probing or early warning separately.

The residual operation is narrower:

> **Choose lawful futures specifically to test whether the current state representation is adequate; when supposedly identical states split, repair the failure with the smallest physically typed information and test whether the onset and identity of that recruitment prospectively reveal an emerging mechanism.**

The reviewed literatures contain the surrounding ingredients. The full experimental composition above is treated as the paper's bounded novelty hypothesis and empirical burden.

Public routes:

- [Zenodo publication](https://doi.org/10.5281/zenodo.22058303)
- [Canonical MKUFT fold — Module 33S7](../docs/33S7_FUTURE_SPLITTING_STATE_RECRUITMENT_STATE_ADEQUACY_AND_PROSPECTIVE_MECHANISM_LOCALISATION.md)
- [Standalone publication record](../FSSR_STANDALONE_PUBLICATION.md)
- [AAF parent publication](https://doi.org/10.5281/zenodo.22031333)

## 2. State adequacy as a future claim

Let `H_t` denote retained history. A candidate state representation is

```math
\Theta:\mathcal H\rightarrow\mathcal Z_{\Theta}.
```

Fix target `q`, horizon `\Delta`, admissible challenge family `\mathcal U`, regime `\lambda`, environment/boundary class `E`, discrepancy `d` and closure tolerance `\varepsilon_q`.

Two histories are future-equivalent when

```math
h\sim_{q,\Delta,\mathcal U,\lambda}h'
\iff
\mathcal L_{\lambda}(q^+_{\Delta}\mid h,u,E)
=
\mathcal L_{\lambda}(q^+_{\Delta}\mid h',u,E)
\quad\forall u\in\mathcal U.
```

A state representation is sufficient only if

```math
\Theta(h)=\Theta(h')
\Longrightarrow
h\sim_{q,\Delta,\mathcal U,\lambda}h'.
```

Thus “same state” is not merely a coordinate convention. It is an empirical commitment that no admissible declared future can materially expose a distinction the representation has erased.

## 3. Closure residual

For histories collapsed by `\Theta`, define challenge-conditioned divergence

```math
\delta_{q,\Delta}(h,h';u,\lambda)
=
d\!\left[
\mathcal L_{\lambda}(q^+_{\Delta}\mid h,u,E),
\mathcal L_{\lambda}(q^+_{\Delta}\mid h',u,E)
\right].
```

The exact worst-case closure residual is

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

Two calibration monotonicities follow directly.

A lawful refinement of state cannot increase the exact same-state residual:

```math
\Theta_2\text{ refines }\Theta_1
\Longrightarrow
R_q(\Theta_2)\leq R_q(\Theta_1).
```

Expanding the admissible challenge family cannot reduce the exact worst-case residual:

```math
\mathcal U_1\subseteq\mathcal U_2
\Longrightarrow
R_q(\Theta;\mathcal U_1)
\leq
R_q(\Theta;\mathcal U_2).
```

The exact invariant is future-equivalence partition refinement, not a universal increase in latent dimension.

## 4. Future-splitting challenge

FSSR selects an admissible continuation to stress the state claim itself:

```math
u^{\star}
\in
\arg\max_{u\in\mathcal U}
\widehat{\mathcal J}_{\mathrm{split}}(u;\Theta,\lambda).
```

A practical score compares future laws only inside matched or near-matched candidate-state fibres. The challenge, admissible perturbation budget and scoring rule are frozen before confirmatory testing.

This differs from parameter-information design. Parameter information gain asks which experiment best identifies uncertain model parameters. FSSR asks which experiment best tests whether histories already collapsed by the current state representation are actually future-equivalent. The two objectives may coincide; they need not.

## 5. Independent-continuation gate

The same closed surrogate whose state is under test may not be the only source used to certify its future.

A Markov surrogate can merge histories into one latent state and then, by construction, be unable to produce a difference between those histories. That proves internal consistency, not physical adequacy.

Confirmatory continuation must therefore come from a source independent of the candidate state map: a microstate-resolved simulator, a separately validated higher-fidelity model or the physical experiment itself.

## 6. State recruitment

Suppose a state is sufficient at baseline and later fails:

```math
R_q(\Theta_0;\lambda_0)\leq\varepsilon_q,
\qquad
R_q(\Theta_0;\lambda_1)>\varepsilon_q.
```

For a preregistered physically typed candidate augmentation `c`, define a repair when

```math
R_q(\Theta_0\oplus c;\lambda_1)\leq\varepsilon_q.
```

Select the smallest repair under a declared burden `C(c)`:

```math
\boxed{
c^{\star}
\in
\arg\min_c C(c)
\quad\text{subject to}\quad
R_q(\Theta_0\oplus c;\lambda_1)\leq\varepsilon_q.
}
```

A positive **state-recruitment event** requires:

1. prior baseline certification;
2. independent held-out future splitting;
3. frozen typed repair;
4. held-out restoration;
5. removal of the repair reopens failure;
6. restoration closes it again;
7. ordinary stronger-state and matching controls fail to explain the result more simply.

An arbitrary latent neuron is not automatically a physical mechanism. Mechanism-localisation language requires a measurable physical descriptor, invariant subspace or physically typed coalition that survives deformation and held-out testing.

## 7. Prospective prediction

Let `\lambda_R` denote the earliest regime in which a new typed augmentation is required, and let `\lambda_T` denote a preregistered conventional transition marker.

```math
\boxed{L=\lambda_T-\lambda_R.}
```

For time-resolved data,

```math
\boxed{L_t=t_T-t_R.}
```

The primary prospective prediction is:

> **Where an emerging mechanism becomes future-discriminating before its conventional macroscopic marker is overt, state recruitment can occur first, giving positive recruitment lead.**

This is deliberately conditional rather than universal. A zero or negative lead is a legitimate failure for the claimed precursor regime.

## 8. Experimental triangle

### Holography — deterministic physical calibration

Two coherent optical fields can have equal intensity at one plane but different phase:

```math
U_j(x,y,0)=A(x,y)e^{i\phi_j(x,y)},
\qquad
|U_1|^2=|U_2|^2=A^2.
```

After propagation,

```math
I_j(x,y,z)=|\mathcal P_z U_j|^2.
```

A later intensity readout can separate the fields. Intensity alone was therefore insufficient for that future; phase or the complex field repairs deterministic closure. This is a calibration of layer/state typing using known physics, not a claim that FSSR discovered optical phase.

### Single-cell biology — independent natural-system anchor

Single-cell fate systems supply experimentally measured state position, velocity, phase and retained history. The FSSR target is not “history matters.” It is the earliest held-out time at which a previously sufficient state begins to require a new typed coordinate, and whether that recruitment precedes an independently defined overt fate marker.

### History-dependent materials — prospective flagship

The flagship experiment uses history-dependent constitutive mechanics with rich microstate-resolved continuation data, initially targeting HCP magnesium or an equivalent system where learned internal variables and temperature/loading history are already active scientific problems.

The protocol is:

```text
certify baseline state
→ near-match distinct histories
→ optimise a bounded future-splitting challenge
→ freeze the challenge
→ confirm the split independently
→ search a preregistered physical repair library
→ identify the smallest repair
→ remove / restore
→ compare recruitment time with conventional mechanism marker.
```

Candidate repairs include twin volume fraction, slip-system activity summaries, hardening variables, local texture descriptors, temperature-history summaries and other domain-justified measurable coordinates.

The specific prospective wager is that in a correctly selected twinning/detwinning or related history-sensitive regime, a twinning/slip-related descriptor can become necessary for future closure before the corresponding macroscopic constitutive signature is fully overt.

## 9. Strongest fair nulls

FSSR loses force where any stronger ordinary explanation closes the same object:

- inadequate state matching explains the split;
- an omitted standard physical variable closes the future without further structure;
- the same surrogate defines and certifies its own state;
- the probe creates rather than reveals the transition;
- a latent coordinate cannot be given transformation-invariant or physical meaning;
- an ordinary early-warning statistic gives the same prospective information and mechanism localisation;
- parameter-information and state-splitting design remain empirically equivalent after fair tuning.

## 10. Relation to AAF and MKUFT

AAF defines future-sufficient Address: histories belong to the same effective state when their declared admissible futures remain equivalent.

FSSR is the assay that attacks that equivalence claim with lawful continuations and asks whether a previously omitted physical distinction must be recruited.

The layer boundary is therefore strict:

> **FSSR does not turn an informational equivalence class into a new physical force. It identifies when a physical distinction omitted from the declared state becomes necessary to preserve lawful future equivalence.**

The recursive fold is

```text
Address
→ admissible future family
→ future-splitting challenge
→ realised continuation
→ closure or split
→ typed recruitment if required
→ readdressing
→ new admissible future family.
```

## 11. Falsification boundary

The central construction fails for a claimed regime if:

- no lawful challenge separates the supposedly same states;
- the split disappears under adequate matching;
- a strong conventional state/history model closes the future without recruitment;
- the proposed repair fails held-out restoration;
- remove/restore deformation does not reproduce the result;
- the probe itself induces the mechanism;
- the recruitment event does not prospectively precede the claimed marker where positive lead was predicted.

## 12. Preferred citation

> McLaughlin, Mark Charles. (2026). *Future-Splitting State Recruitment: A Cross-Domain Assay for State Adequacy and Prospective Mechanism Activation*. Version 1.0. Zenodo. DOI: 10.5281/zenodo.22058303.

## 13. Selected literature context

The publication's full bibliography remains in the controlling Zenodo PDF. Principal neighbouring literatures include:

- Chorin, A. J., Hald, O. H., & Kupferman, R. (2000). Optimal prediction and the Mori–Zwanzig representation of irreversible processes. *PNAS*, 97(7), 2968–2973. DOI: 10.1073/pnas.97.7.2968.
- Shalizi, C. R., & Crutchfield, J. P. (2001). Computational Mechanics: Pattern and Prediction, Structure and Simplicity. *Journal of Statistical Physics*, 104, 817–879. DOI: 10.1023/A:1010388907793.
- Littman, M. L., Sutton, R. S., & Singh, S. (2001). Predictive Representations of State. *NeurIPS 14*.
- Liu, B., Ocegueda, E., Trautner, M., Stuart, A. M., & Bhattacharya, K. (2023). Learning macroscopic internal variables and history dependence from microscopic models. *Journal of the Mechanics and Physics of Solids*, 178, 105329. DOI: 10.1016/j.jmps.2023.105329.
- Qu, G. et al. (2020). Reprogrammable meta-hologram for optical encryption. *Nature Communications*, 11, 5484. DOI: 10.1038/s41467-020-19312-9.
- Venkatachalapathy, H. et al. (2024). Inertial effect of cell state velocity on the quiescence-proliferation fate decision. *npj Systems Biology and Applications*, 10, 111. DOI: 10.1038/s41540-024-00428-3.
- Hollenweger, Y., Kochmann, D. M., & Liu, B. (2026). Temperature-aware recurrent neural operator for temperature-dependent anisotropic plasticity in HCP materials. *Journal of the Mechanics and Physics of Solids*, 211, 106553. DOI: 10.1016/j.jmps.2026.106553.
- Raj, M., Cao, L., Stuart, A., & Bhattacharya, K. (2026). A neural-network framework to learn history-dependent constitutive laws and identifiability of internal variables. *Journal of the Mechanics and Physics of Solids*, 106807. DOI: 10.1016/j.jmps.2026.106807.

## 14. Publication integrity

The DOI-bearing Zenodo PDF is the controlling frozen visual object for v1.0. This Markdown route is maintained for public readability and linkage into the live MKUFT canon. It must not silently acquire scientific revisions and still be presented as though those revisions were present in the deposited PDF.
