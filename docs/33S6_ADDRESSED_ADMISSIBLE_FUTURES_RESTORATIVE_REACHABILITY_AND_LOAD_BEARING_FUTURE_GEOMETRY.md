# 33S6 — Addressed Admissible Futures, Restorative Reachability, and Load-Bearing Future Geometry

**Author:** Mark Charles McLaughlin  
**Framework:** McLaughlin–Kairos Unified Field Theory (MKUFT)  
**Current principal MKUFT publication:** [10.5281/zenodo.21973064](https://doi.org/10.5281/zenodo.21973064)  
**MKUFT concept DOI:** [10.5281/zenodo.17780565](https://doi.org/10.5281/zenodo.17780565)  
**Citation and provenance:** [PROVENANCE_DOI_AND_ATTRIBUTION.md](../PROVENANCE_DOI_AND_ATTRIBUTION.md)  
**Architectural parent:** [33 — SIPO Capstone](33_SIPO_CAPSTONE_CONSTRAINT_CONDITIONED_ADDRESSED_UPDATE_LAW.md)  
**Address-sufficiency parent:** [33S4 — Address Sufficiency, Predictive Closure, and Reachable-Future Geometry](33S4_ADDRESS_SUFFICIENCY_PREDICTIVE_CLOSURE_AND_REACHABLE_FUTURE_GEOMETRY.md)  
**Rate/history parent:** [33S5 — Rate-Conditioned Addressing, Time-Parameterised Traversal, and Adaptive Reorganisation](33S5_RATE_CONDITIONED_ADDRESSING_TIME_PARAMETERISED_TRAVERSAL_AND_ADAPTIVE_REORGANISATION.md)  
**Recoverability parent:** [33S3 — Cross-Scale Performance, Recoverability, and Hysteretic Readdressing](33S3_CROSS_SCALE_PERFORMANCE_RECOVERABILITY_AND_HYSTERETIC_READDRESSING.md)  
**Reachability parent:** [32 — Recursive Constraint Closure and Reachable-State Geometry](32_RECURSIVE_CONSTRAINT_CLOSURE_AND_REACHABLE_STATE_GEOMETRY.md)  
**Public formulation date:** 20 August 2026  
**Rights:** Copyright © 2026 Mark Charles McLaughlin. All rights reserved unless an exact later publication states otherwise.  
**Status:** canonical companion refinement of the existing recursive S-I-P-O addressed-update family. It defines the future-equivalence object induced by a target-sufficient Address, distinguishes present viability from restorative reachability, defines restorative-future reserve and counterfactual load-bearing relation structure, and closes the result back through recursive readdressing. It is **not** a separate law stack beside MKUFT and does not establish a new force, field, biological mechanism, universal graph law, or independent I→P coupling.

## 1. Purpose and placement

The existing MKUFT canon already contains the load-bearing pieces:

```text
complete addressed S-I-P-O state
→ admissibility
→ active lawful continuation / physical-law object
→ realised transition and registration
→ readdressing
→ next addressed state.
```

Module 33S4 asks whether the current operational Address is sufficient for a declared future target. Module 33S5 tests whether rate, dwell, phase, schedule or bounded history must enter that Address. Module 33S3 separates present organisation from recoverability. Module 32 supplies changing reachable-state geometry.

The present module folds those pieces onto one explicit future object:

> **What future-equivalence class is induced by a state description sufficient for the declared target, and how much viable restorative route structure remains inside that future?**

The compact recursion is

```text
Address
→ admissible future
→ realised transition
→ readdressing
→ new admissible future.
```

This is a specialisation of the existing S-I-P-O update architecture, not a competing architecture.

## 2. Future-sufficient Address

Let `H_t` denote the retained history available at time `t`. Let `Σ` denote the declared system specification: target variables, prediction horizon, physical dynamics or transition kernel, boundary/environment class, admissible intervention class, measurement resolution, and any typed relational constraints that genuinely determine continuation.

Let `X⁺` denote the future path object after `t`, and let `Π_adm` be the admissible policy/intervention family.

Two histories are **future-equivalent** when they generate the same future law for every admissible policy:

```math
H_t \sim_{\Sigma} H'_t
\iff
\mathbb P_{\Sigma}\!\left(X^+\mid H_t,\pi\right)
=
\mathbb P_{\Sigma}\!\left(X^+\mid H'_t,\pi\right)
\quad
\forall\pi\in\Pi_{\mathrm{adm}}.
```

The effective Address is the equivalence class

```math
\boxed{
A_t=[H_t]_{\sim_{\Sigma}}.
}
```

For deterministic systems, equality of future probability laws reduces to equality of the declared reachable/admissible future. For finite noisy data, exact equality is replaced by a preregistered discrepancy and tolerance.

This gives the membership rule:

> **A coordinate belongs in the effective Address only when omitting it merges histories whose declared future laws differ beyond tolerance.**

Thus velocity, phase, charge, rate, schedule, hysteresis, boundary state, connectivity or another coordinate may enter Address when it changes the future; none is compulsory by name.

## 3. Operational address residual and minimum-sufficient frontier

For a target `q` over horizon `Δ`, let `Θ(H_t)` be a candidate coordinate description. Let `\mathcal L(q^+\mid h)` be the conditional law of the future target and let `d` be a declared discrepancy.

Define

```math
\boxed{
\mathcal R_q(\Theta)
=
\sup_{\Theta(h)=\Theta(h')}
 d\!\left(
 \mathcal L(q^+\mid h),
 \mathcal L(q^+\mid h')
 \right).
}
```

The Address is `ε_q`-sufficient when

```math
\mathcal R_q(\Theta)\leq\varepsilon_q.
```

If `Θ_2` lawfully augments `Θ_1` without discarding a load-bearing parent relation, the induced equivalence classes refine rather than broaden, so the exact residual obeys

```math
\Theta_1\subseteq\Theta_2
\quad\Longrightarrow\quad
\mathcal R_q(\Theta_2)\leq\mathcal R_q(\Theta_1).
```

Define the sufficient family and its minimal elements:

```math
\mathcal S_q
=
\{\Theta:\mathcal R_q(\Theta)\leq\varepsilon_q\},
```

```math
\mathcal M_q
=
\{\Theta\in\mathcal S_q:
\text{no proper lawful subset is sufficient}\}.
```

`\mathcal S_q` is upward closed under lawful augmentation, while `\mathcal M_q` may contain several incomparable minimal descriptions. The result is a **minimum-sufficient address frontier**, not a claim that one universal scale must always govern.

The frontier remains target-, horizon-, intervention-, environment-, resolution- and tolerance-relative.

## 4. Admissible future

Let

```math
\mathcal F^+(A_t)
```

denote the admissible future induced by the current Address under the declared system specification. Depending on the domain, this may be represented as:

- a reachable set;
- a family of path measures;
- a directed time-indexed transition structure;
- a controlled viability kernel;
- another domain-appropriate carrier preserving the declared future distinction.

The future object is prior to any one summary of it. Path count, probability, topology, flow, energy cost, recovery time and bottleneck structure are readouts, not automatically the parent object.

## 5. Present viability is not restorative reachability

Let `J(a)` index the load-bearing viability constraints at address `a`. Define

```math
\mathcal V(a)
=
\{z:h_j(z;a)\geq0\ \forall j\in J(a)\},
```

with present viability margin

```math
\boxed{
H(z,a)=\min_{j\in J(a)} h_j(z;a).
}
```

`H>0` says the present state lies inside the declared viable region. It does **not** establish that a sufficient path remains to maintain or restore the required organisation.

Let `G(A_t)` be a declared restored/recovered target set. Let `Q(\gamma)` measure task sufficiency with threshold `\kappa`, and let `D_{\mathrm{irr}}(\gamma)` be a vector of domain-defined irreversible losses constrained by `d_R`.

Define the restorative future

```math
\boxed{
\Gamma_R(A_t)
=
\left\{
\gamma\in\mathcal F^+(A_t):
\gamma\subseteq\mathcal V(A_t),
\ \gamma\rightarrow G(A_t),
\ Q(\gamma)\geq\kappa,
\ D_{\mathrm{irr}}(\gamma)\preceq d_R
\right\}.
}
```

Its simplest existence indicator is

```math
\boxed{
\chi_R(A_t)
=
\mathbf 1\!\left[\Gamma_R(A_t)\neq\varnothing\right].
}
```

This keeps three objects distinct:

1. the system is presently viable;
2. at least one sufficient restorative continuation exists;
3. the restorative continuation set is robust rather than knife-edge.

## 6. Restorative-future reserve

Existence can be brittle. Let `\mathcal D` be a preregistered family of physically/operationally meaningful deformations of the admissibility structure, with cost `c(\Delta)`.

Define restorative-future reserve

```math
\boxed{
\rho_R(A_t)
=
\inf_{\Delta\in\mathcal D}
\left\{
c(\Delta):
\Gamma_R(A_t;\Delta)=\varnothing
\right\}.
}
```

Interpretation:

- high `\rho_R`: substantial admissibility deformation is required before every sufficient restorative route disappears;
- low `\rho_R`: restoration remains possible but fragile;
- `\chi_R=0`: no sufficient restorative route remains under the declared construction.

A system can therefore satisfy

```math
H>0
\qquad\text{while}\qquad
\rho_R\downarrow0,
```

so present viability can outlive recoverability.

The deformation family and cost must be declared before outcome inspection. They do not become scientific merely because a graph can be drawn.

## 7. Counterfactual load-bearing relation

Let `C` be a relation or coalition of relations in the typed structure carrying the restorative future. Let `\Psi` be a preregistered functional readout of that future: existence, reserve, recovery probability, time-to-restoration, irreversible cost, or another declared quantity.

Define relational load by counterfactual deformation:

```math
\boxed{
\Lambda_C^{\Psi}(A_t)
=
\Psi\!\left(\Gamma_R(A_t)\right)
-
\Psi\!\left(\Gamma_R^{-C}(A_t)\right).
}
```

A relation is **load-bearing relative to `(A_t,\Psi)`** when removing or deforming it materially changes the declared future readout. It is terminally load-bearing when removal changes `\chi_R` from `1` to `0`.

This rejects weak proxies:

- high centrality is not sufficient;
- high present flow is not sufficient;
- visual prominence is not sufficient;
- repetition is not sufficient.

A dormant backup relation may carry almost no present flow while dominating future recoverability. A heavily used relation may be replaceable and therefore non-terminal. Coalitions matter because jointly necessary relations may each look dispensable under single ablation.

## 8. Finite graph estimator

For finite trajectory data, approximate the restorative future by a directed or time-expanded network `K_R`. Nodes represent addressed states or microstates; directed edges represent empirically supported admissible transitions; `c_e` is a preregistered edge capacity/robustness weight.

For present node `s` and restorative target set `G`, a graph estimator of reserve is

```math
\boxed{
\widehat{\rho}_R(s,G)
=
\min_{C\in\mathrm{Cut}(s,G)}
\sum_{e\in C} c_e.
}
```

By max-flow/min-cut duality, this can be interpreted as supported bottleneck capacity of route structure from the present node to the target.

Raw path count is not equivalent. Many nominal routes sharing one fragile bottleneck can carry less reserve than a few genuinely independent routes.

This estimator is subordinate to the abstract definition. If another domain requires a different physically meaningful deformation metric, use that metric rather than forcing graph cuts.

## 9. Recursive readdressing

A realised transition changes the retained history and may therefore move the effective Address:

```math
\boxed{
A_t
\rightarrow
\mathcal F_t^+
\rightarrow
\tau_t
\rightarrow
A_{t+1}
\rightarrow
\mathcal F_{t+1}^+.
}
```

This is the point of attachment to the S-I-P-O capstone:

```text
addressed state/context
→ admissibility descriptor
→ lawful continuation
→ realised transition / registration
→ updated history and context
→ readdressed state
→ changed future geometry.
```

Traversal therefore need not occur on one fixed possibility map. The transition itself can alter the Address that determines the next admissible future.

## 10. Moving frontier and early structural warning

The minimum-sufficient frontier `\mathcal M_q` can move as the system changes.

A coarse Address may initially close a target. Later, states carrying the same coarse description can diverge because a previously dormant lower-scale, cross-scale, temporal, interface or relational coordinate has become dynamically load-bearing. Then `\mathcal R_q` rises above tolerance and readdressing is required.

A direct test sequence is:

1. establish an Address that closes the target at baseline;
2. perturb or drive the system;
3. retest the same Address prospectively;
4. identify the smallest independently measurable coordinate that restores closure;
5. ablate/remove that coordinate and require closure to worsen as predicted;
6. restore/intervene and require the discrimination to return;
7. test whether frontier movement or restorative reserve changes before the conventional overt failure marker.

The method stops when predictive/interventional closure is earned. Additional resolution that changes neither the target, falsifier, admissibility boundary, implementation nor decision is not evidence of progress.

## 11. Calibration examples

### 11.1 Position and velocity

For a one-dimensional body with bounded acceleration,

```math
\dot x=v,
\qquad
\dot v=u,
\qquad
|u|\leq u_{\max},
```

and unsafe boundary `x=1`, the minimum stopping distance for positive velocity is

```math
\boxed{
d_{\mathrm{stop}}
=
\frac{v^2}{2u_{\max}}.
}
```

Two objects can share the same position and present boundary margin while having different restorative futures. Velocity therefore enters the sufficient Address for the target “can the system stop before the boundary?” because position alone merges futures that differ.

This is ordinary dynamics; it is a calibration of the Address rule, not exotic physics.

### 11.2 p21/Cdk2 state velocity

Venkatachalapathy et al. reported that p21/Cdk2 position plus cell-state velocity predicted quiescence/proliferation fate better than position alone in their single-cell construction. AAF does not claim that result as new. It uses it as a direct calibration: if similar instantaneous positions retain different future distributions because velocity differs, position is incomplete for that target.

### 11.3 p53 phase resetting

Venkatachalapathy et al. later showed that repeated DNA-damage stimulus timing can reset p53 phase and alter downstream p21 dynamics and arrest robustness. Again, the result is established work. The AAF reading is narrower: phase/schedule earns Address status when omitting it merges histories with different declared future laws.

These examples support the operational Address rule. They do not validate the entire AAF composition or an MKUFT-specific physical mechanism.

## 12. First preregistered empirical route

The companion standalone paper freezes a first test using public single-cell p21 data associated with the 2025 p53 phase-resetting study.

The primary question is not whether the published 4.0-hour and 5.5-hour treatment schedules differ; that broad direction is already known. The prospective burden is whether a future-sufficient directed restorative-reserve construction predicts **individual arrest escape** beyond conventional summaries using the same pre-outcome information.

Core fixed elements include:

- prediction time `t*=5.0 h`;
- no post-5 h measurement may enter the predictor;
- outcome: escape from high-p21 arrest during `5.0–8.0 h` versus maintained arrest through `8.0 h`, inherited from the source analysis;
- candidate Address: pre-5 h p21 history plus NCS regimen and elapsed time since the most recent dose;
- leave-one-biological-replicate-out evaluation;
- directed time-addressed transition network estimated only from training folds;
- `\chi_R` and `\rho_R` as AAF readouts;
- regularised same-history baseline as the crucial comparator;
- time-history scrambling, relation-preserving/relation-destroying controls and label permutation;
- a strong result only if AAF readouts improve held-out prediction and the real directed relation structure beats the rewired control.

If the same-information conventional predictor performs equivalently, future topology/reserve does not earn independent predictive credit in that test.

## 13. Prior-art and contribution boundary

The ingredients used here are established and are not claimed as standalone inventions:

- predictive-state representations;
- computational-mechanics causal/future states;
- state sufficiency and observability;
- viability and capture/reachability theory;
- control barrier methods;
- graph cuts and max-flow/min-cut;
- recurrent-flow/Hodge methods where applicable;
- history, phase, rate and hysteresis in dynamical systems.

The candidate MKUFT contribution is the explicit composition and placement:

```text
future-sufficient typed Address
→ admissible future
→ restorative subfuture
→ restorative reserve
→ counterfactual load-bearing relation
→ realised transition
→ recursive readdressing.
```

The composition earns scientific weight only through prospective discrimination, ablation/restoration, strong baselines and failure conditions. Internal architectural coherence is not evidence by itself.

## 14. Failure and reduction conditions

Reduce, reject or narrow the AAF claim when any of the following occurs:

- the proposed Address does not improve target-relative future closure;
- omitted variables do not create stable held-out future splitting;
- a simpler ordinary measurable state closes the target equally well;
- apparent future splitting is estimator error, leakage, regime mixing or uncontrolled environment/preparation difference;
- restorative reserve adds no held-out information beyond adequate present-state/history baselines;
- reserve collapses only at or after the conventional failure marker when an earlier warning was claimed;
- a claimed Address coordinate fails ablation/restoration;
- rewired relation structure predicts as well as the real directed relation structure;
- raw graph density/path count performs as well where a bottleneck-specific reserve advantage was claimed;
- cross-domain applications require changing the formal definitions after seeing outcomes;
- a predictive relation is described causally without intervention or a justified causal model.

## 15. Claim boundary

This module does **not** establish:

- a fundamental new physical force or field;
- a universal biological repair law;
- a universal moral metric;
- that graph topology is always the correct carrier;
- that every system has a finite-dimensional sufficient Address;
- that predictive load proves causal load;
- that observer registration causes physical dynamics;
- an independent informational-layer physical coupling;
- fundamental quantum-gravity dynamics.

It supplies a narrower scientific object:

> **For a declared target, horizon, intervention/environment class and tolerance, identify the minimum retained Address that closes the target-relevant future; then measure whether a sufficient restorative subfuture exists, how robust it is to admissibility deformation, and which typed relations are counterfactually load-bearing for that future.**

## 16. References

1. McLaughlin, M. C. *MKUFT — A Relational Architecture for Physical Law and Cross-Scale Dynamics*. Version v2. Zenodo. DOI `10.5281/zenodo.21973064` (2026).
2. Shalizi, C. R. & Crutchfield, J. P. “Computational Mechanics: Pattern and Prediction, Structure and Simplicity.” *Journal of Statistical Physics* 104, 817–879 (2001). DOI `10.1023/A:1010388907793`.
3. Littman, M. L. & Sutton, R. S. “Predictive Representations of State.” *Advances in Neural Information Processing Systems* 14 (2001).
4. Ferns, N., Panangaden, P. & Precup, D. “Bisimulation Metrics for Continuous Markov Decision Processes.” *SIAM Journal on Computing* 40(6), 1662–1714 (2011). DOI `10.1137/10080484X`.
5. Aubin, J.-P. *Viability Theory*. Birkhäuser (1991).
6. Ames, A. D. et al. “Control Barrier Functions: Theory and Applications.” *2019 European Control Conference*, 3420–3431 (2019). DOI `10.23919/ECC.2019.8796030`.
7. Venkatachalapathy, H. et al. “Inertial effect of cell state velocity on the quiescence-proliferation fate decision.” *npj Systems Biology and Applications* 10, 111 (2024). DOI `10.1038/s41540-024-00428-3`.
8. Venkatachalapathy, H. et al. “Pulsed stimuli enable p53 phase resetting to synchronize single cells and modulate cell fate.” *Molecular Systems Biology* 21(4), 390–412 (2025). DOI `10.1038/s44320-025-00091-8`.
9. Batchelor, E., contributor. *Venkatachalapathy et al — p53 phase resetting*. Mendeley Data, Version 1 (2025). DOI `10.17632/xrc7k83tjv.1`.
10. Ford, L. R. Jr & Fulkerson, D. R. “Maximal Flow Through a Network.” *Canadian Journal of Mathematics* 8, 399–404 (1956).

## Compact rules

> **Address is earned by future closure, not by naming more variables.**

> **Present viability is not restorative reachability.**

> **A relation is load-bearing when its controlled removal deforms the declared future, not when it merely looks central.**

> **Traversal can rewrite the Address that governs the next admissible future.**

> **AAF is a future-object specialisation of the existing S-I-P-O addressed-update architecture, not a separate law stack.**
