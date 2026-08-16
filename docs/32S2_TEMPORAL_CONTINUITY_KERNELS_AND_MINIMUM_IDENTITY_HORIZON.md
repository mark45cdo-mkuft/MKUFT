# 32S2 — Temporal Continuity Kernels and Minimum Identity Horizon

**Author:** Mark Charles McLaughlin  
**Framework:** McLaughlin–Kairos Unified Field Theory (MKUFT)  
**MKUFT DOI:** [10.5281/zenodo.17780566](https://doi.org/10.5281/zenodo.17780566)  
**Canonical parent:** [32S1 — Invariant Persistence, Relational Addressability, and Scale Transition](32S1_INVARIANT_PERSISTENCE_RELATIONAL_ADDRESSABILITY_AND_SCALE_TRANSITION.md)  
**Root owner:** [32 — Recursive Constraint Closure and Reachable-State Geometry](32_RECURSIVE_CONSTRAINT_CLOSURE_AND_REACHABLE_STATE_GEOMETRY.md)  
**Novelty boundary:** [32A — Module 32 Novelty Audit and Contribution Boundary](32A_MODULE_32_NOVELTY_AUDIT_AND_CONTRIBUTION_BOUNDARY.md)  
**Public formulation date:** 15 August 2026  
**Status:** canonical temporal-continuity refinement. It extends the same-self parity machinery from point-state comparison to recent trajectory/history comparison where history is load-bearing. It does not establish consciousness, a metaphysical soul, survival after death, or a universal law of identity.

## 1. Core refinement

Module 32S1 correctly distinguishes within-address state equivalence, address-class parity, and cross-address continuity, but its compact continuation test is written primarily on the realised self-state `s_t` at one time.

For many adaptive or living systems, that is too thin. The object that carries continuity may be a **recent trajectory of self-states and relations**, not one instantaneous state. The immediate past is therefore the smallest temporal candidate, while a longer recent history may be required when memory, adaptation, lineage, hysteresis, or path-dependence is constitutive.

> Continuity need not be point-state invariance. It can be invariance of a lawful recent trajectory relation.

This does not mean all past history is equally relevant. The scientific task is to determine the **minimum history horizon whose removal destroys the claimed continuity discrimination**.

## 2. Recent self-history

Let the operational self-state from Module 32S1 be

```math
s_t\in\mathcal S_t.
```

For an integer history depth `m >= 1`, define the recent self-history

```math
h_t^{(m)}
=
\left(
 s_{t-m},\ldots,s_{t-1},s_t
\right)
\in
\mathcal H_t^{(m)}.
```

The smallest genuinely temporal case is `m=1`, which retains the immediate predecessor and current state:

```math
h_t^{(1)}=(s_{t-1},s_t).
```

A single instantaneous state is recovered only as the degenerate point-state case and should not be called a temporal-continuity test.

For irregular or continuous time, use a declared recent interval `[t-\tau,t]` rather than forcing equal discrete steps.

## 3. Continuity-bearing history functional

Let

```math
K_t^{(m)}:
\mathcal H_t^{(m)}
\rightarrow
\mathcal J
```

be a declared **continuity-bearing history functional**. It extracts the relation or invariant family claimed to carry identity continuity over that history window.

`K_t^(m)` may depend on ordered transition structure, boundary persistence, maintenance relations, system–environment coupling, lineage, memory, or another declared identity-bearing relation. It must not be chosen post-hoc merely because it makes continuity appear.

No universal weighted sum is assumed. If a particular implementation uses recency weights, those weights must be justified and preregistered. The immediate past may dominate in one system while a longer path-dependent history is load-bearing in another.

## 4. Cross-address history transport

When individuality addresses remain in the same address class, recent histories may be compared through common declared observables.

When address-class parity fails but cross-address continuity is proposed, pointwise state transport is not automatically enough. Define a lawful history transport

```math
T_{a\rightarrow b}^{\mathrm{hist},(m)}:
\mathcal H_a^{(m)}
\supseteq
\mathcal D_a^{(m)}
\rightarrow
\mathcal H_b^{(m)}.
```

Temporal continuity to tolerance `epsilon_J` requires

```math
d_J\!\left(
K_b^{(m)}\!\left(T_{a\rightarrow b}^{\mathrm{hist},(m)}h_a^{(m)}\right),
K_a^{(m)}\!\left(h_a^{(m)}\right)
\right)
\leq
\varepsilon_J,
```

plus the domain-specific lineage, viability, boundary, maintenance, and address conditions required by the individuality claim.

This is the temporal extension of the same-self parity guard:

> If identity depends on path, a map between endpoints does not by itself prove continuity of the path-dependent individuality.

## 5. Minimum identity horizon

The framework should not assume that more remembered history is always better or more constitutive.

Define the **minimum identity horizon** `m*` as the smallest recent history depth that supports a stable, non-post-hoc continuity discrimination under the declared tests:

```math
m^*
=
\min\left\{
 m\geq1:
 \mathcal C_{\mathrm{id}}(m)=1
\right\},
```

where `C_id(m)=1` means that the continuity criterion at depth `m` survives the preregistered perturbation, replay, and held-out checks.

A stronger operational requirement is that shorter histories fail or materially degrade the discrimination:

```math
\mathcal C_{\mathrm{id}}(m^*)=1,
\qquad
\mathcal C_{\mathrm{id}}(m)<1
\text{ or degrades materially for }m<m^*.
```

If the immediate-past pair is sufficient, then `m*=1`. If a longer recent trajectory is required, `m*>1`. If no tested finite history closes the individuality claim, report the history requirement as unresolved rather than forcing a finite kernel.

## 6. History ablation and survivability

A history term earns load-bearing status only if removing or scrambling it produces the predicted continuity failure while preserving the remaining comparison conditions as far as possible.

Useful tests include:

- **history truncation:** progressively shorten the recent history and identify where continuity discrimination fails;
- **temporal shuffle:** preserve the same states but scramble their order; a trajectory-bearing identity relation should degrade if order is constitutive;
- **immediate-past ablation:** remove or replace `s_(t-1)` while retaining older history to test whether the immediate predecessor is specifically load-bearing;
- **remote-history ablation:** remove older states while retaining the immediate trajectory to determine whether continuity is local or genuinely long-memory;
- **matched-state / different-history control:** compare systems with similar present state but different recent trajectories;
- **matched-history / perturbed-endpoint control:** test whether the history relation remains predictive when the current endpoint is perturbed within the admissible identity class.

These tests distinguish **state resemblance** from **trajectory continuity**.

## 7. Relation to the smallest survivable identity object

The smallest survivable identity object should therefore not be assumed to be one static invariant or one present state.

A stronger candidate is:

> the smallest **continuity-bearing relational history** that can be transported through lawful change while preserving the declared identity criterion.

In the minimal temporal case this may be the relation between the immediate past state and the present state. In a path-dependent system it may require several recent states or a finite recent interval.

This produces a sharper hierarchy:

```text
same substrate
≠ same present state
≠ same recent trajectory
≠ same individuality by default
```

and, positively:

```text
recent relational history
+ lawful continuation map
+ preserved identity-bearing functional
+ surviving viability / lineage conditions
→ supported same-self continuity claim
```

## 8. Interaction with scale transition

During a scale transition, the lower individuality may lose independent access to old relations while the individuality address itself changes.

The temporal test asks whether the later individuality is connected to the earlier one by a continuity-bearing trajectory rather than by endpoint resemblance alone.

Three cases remain distinct:

1. **same address class, continuous trajectory** — ordinary development or adaptation inside the same individuality class;
2. **readdressed but trajectory-continuous** — the individuality criterion changes class, yet a lawful history transport preserves the declared continuity-bearing functional;
3. **trajectory discontinuity or unresolved transport** — incorporation, replacement, branching, or another identity transition must remain open rather than being labelled `the same self` by default.

This makes `identity transition` a dynamical object rather than a comparison of two frozen snapshots.

## 9. Prior-art boundary

The broad idea that biological individuality is historical, temporally extended, processual, or spatiotemporally continuous is established prior work and is not attributed to MKUFT as a first discovery.

Moreno, Etxeberria, and Umerez (2008) explicitly argue that theories of biological autonomy must include historical and structural features. Other work on biological individuality treats living individuals as spatiotemporally restricted, continuous, historic entities whose parts may be replaced while the organised life process persists.

The present MKUFT contribution candidate is narrower: **couple recent-history dependence to the addressed-state / same-self parity machinery, require lawful history transport across readdressing, and define a minimum identity horizon by history ablation rather than assuming either point-state identity or unlimited historical memory.** Historical priority for that exact integration is not asserted here.

Relevant references include:

- Moreno, A., Etxeberria, A., and Umerez, J. (2008). *The autonomy of biological individuals and artificial models*. BioSystems 91(2), 309–319. DOI `10.1016/j.biosystems.2007.05.009`.
- Doolittle, W. F. (2016). *Life on Earth is an individual*. Theory in Biosciences 135, 1–10. DOI `10.1007/s12064-016-0221-2`.
- Varela, F. G., Maturana, H. R., and Uribe, R. (1974). *Autopoiesis: The organization of living systems, its characterization and a model*. BioSystems 5, 187–196. DOI `10.1016/0303-2647(74)90031-8`.

## 10. Failure and reduction conditions

Reduce this refinement if:

- present-state variables predict continuity as well as the proposed history functional;
- temporal order can be shuffled without changing the claimed identity discrimination;
- the selected history depth is chosen post-hoc and fails held-out testing;
- a shorter history performs equally well, making the larger kernel non-load-bearing;
- the claimed continuity survives only because the comparison map smuggles the desired identity into the translation;
- no measurable identity-relevant consequence differs between matched present states with different histories.

If these failures occur, use the simpler point-state or shorter-history model.

## 11. Claim boundary

This module does **not** identify a metaphysical soul. It does not establish personal survival after death, reincarnation, consciousness, or independent I→P dynamics.

It provides a scientific systems question:

> **What is the shortest recent relational trajectory that must survive lawful transformation for a same-individuality claim to remain predictive and interventionally stable?**

That question is empirical in any implementation that supplies measurable state, relation, history, and intervention variables.

## 12. Compressed rules

> **Continuity is not automatically in the present state. Test the recent trajectory.**

> **The immediate past is the smallest temporal candidate; longer history must earn its load by ablation.**

> **If identity is path-dependent, endpoint parity is insufficient. Transport the history, not only the state.**

> **Find the minimum identity horizon: the shortest recent history whose removal destroys the continuity relation.**
