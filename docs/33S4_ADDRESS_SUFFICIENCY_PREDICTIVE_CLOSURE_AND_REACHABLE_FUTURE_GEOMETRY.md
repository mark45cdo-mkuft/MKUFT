# 33S4 — Address Sufficiency, Predictive Closure, and Reachable-Future Geometry

**Author:** Mark Charles McLaughlin  
**Framework:** McLaughlin–Kairos Unified Field Theory (MKUFT)  
**Current principal MKUFT publication:** [10.5281/zenodo.21973064](https://doi.org/10.5281/zenodo.21973064)  
**MKUFT concept DOI:** [10.5281/zenodo.17780565](https://doi.org/10.5281/zenodo.17780565)  
**Citation and provenance:** [PROVENANCE_DOI_AND_ATTRIBUTION.md](../PROVENANCE_DOI_AND_ATTRIBUTION.md)  
**Architectural parent:** [33 — SIPO Capstone](33_SIPO_CAPSTONE_CONSTRAINT_CONDITIONED_ADDRESSED_UPDATE_LAW.md)  
**Law-descent parent:** [33S2 — Relational Closure, Law Descent, and Bidirectional Readdressing](33S2_RELATIONAL_CLOSURE_LAW_DESCENT_AND_BIDIRECTIONAL_READDRESSING.md)  
**Reachability parent:** [32 — Recursive Constraint Closure and Reachable-State Geometry](32_RECURSIVE_CONSTRAINT_CLOSURE_AND_REACHABLE_STATE_GEOMETRY.md)  
**Observability parent:** [31 — Context-Conditioned State Comparison and Observability](31_CONTEXT_CONDITIONED_STATE_COMPARISON_AND_OBSERVABILITY.md)  
**Public formulation date:** 18 August 2026  
**Rights:** Copyright © 2026 Mark Charles McLaughlin. All rights reserved unless an exact later publication states otherwise.  
**Status:** canonical companion refinement of Modules 31, 32, 33, and 33S2. It formalises target-relative address sufficiency, predictive closure, residual future divergence, address augmentation, and readdressing. It does not assert universal determinism, a unique hidden state, observer-caused dynamics, or a new physical force or field.

## 1. Purpose

MKUFT already distinguishes addressed state, context, retained history, reachable-state geometry, measurement-relative observability, property-specific law descent, and readdressing when a higher description loses sufficiency.

A remaining question is operational:

> **When is the present address complete enough for the specific future quantity being predicted or controlled?**

The answer cannot be “when every conceivable variable is included.” A useful address is target-relative. It should contain the smallest typed set of coordinates required for the declared target, horizon, environment, intervention class, and tolerance.

This module therefore treats predictive disagreement as a testable address question:

> **If states assigned the same operational address retain materially different target futures under matched conditions, the current address is not yet sufficient for that target unless the divergence is already accounted for by the declared stochastic model and tolerance.**

Compressed rule:

> **When the future does not close, test the address before multiplying laws.**

## 2. Operational address map

Let `X` be a state space containing the variables required by the implementation under study. Let `Theta` denote a declared typed coordinate family used to construct an operational address.

Define

```math
A_{\Theta}:\mathcal X\rightarrow\mathcal Z_{\Theta}.
```

For a realised state `x`,

```math
z=A_{\Theta}(x)
```

is the operational address used for the present prediction or intervention problem.

The coordinate family `Theta` may include, where load-bearing and measurable:

- state variables;
- relational variables;
- boundary conditions;
- environment;
- preparation class;
- retained history or memory;
- scale or resolution;
- interface state;
- observer/registration conditions where they alter the declared readout or admissibility problem;
- another domain-specific coordinate whose inclusion can change the target-relevant future distribution.

No coordinate is included merely because it is available. A coordinate earns load-bearing status only when its removal or restoration changes the declared discrimination, prediction, intervention, or closure result under controlled testing.

Two lower states are equivalent at the candidate address when

```math
x\sim_{\Theta}x'
\quad\Longleftrightarrow\quad
A_{\Theta}(x)=A_{\Theta}(x').
```

This equivalence is target-independent at the level of address construction. Whether it is sufficient is target-dependent.

## 3. Target-relative predictive closure

Let

```math
q:\mathcal X\rightarrow\mathcal Q
```

be the declared target quantity or observable, and let `Delta` be the prediction horizon.

Let

```math
K^{\Delta}(\cdot\mid x,u,e)
```

be the physical or modelled transition kernel over horizon `Delta` under intervention/control `u` and environment `e`.

The pushed-forward target distribution is

```math
q_*K^{\Delta}(\cdot\mid x,u,e).
```

Choose a declared discrepancy `d_Q` on target distributions. For deterministic targets this may reduce to a metric on `Q`; for stochastic targets it must compare probability distributions using a stated choice such as total variation, Wasserstein distance, another probability metric, or a domain-specific preregistered discrepancy.

Define the **address residual**

```math
\mathcal R_q(\Theta;U,E,\Delta)
=
\sup_{\substack{x\sim_{\Theta}x'\\u\in U,\,e\in E}}
 d_Q\!\left(
 q_*K^{\Delta}(\cdot\mid x,u,e),
 q_*K^{\Delta}(\cdot\mid x',u,e)
 \right).
```

For a preregistered tolerance `epsilon_q`, the address is **predictively sufficient for `q`** over the declared regime when

```math
\boxed{
\mathcal R_q(\Theta;U,E,\Delta)
\leq
\varepsilon_q.
}
```

This is **predictive closure at the declared address**. It does not imply complete knowledge of the underlying system.

## 4. Deterministic and stochastic cases

### 4.1 Deterministic case

For deterministic dynamics

```math
F^{\Delta}:\mathcal X\times U\times E\rightarrow\mathcal X,
```

predictive closure reduces to

```math
A_{\Theta}(x)=A_{\Theta}(x')
\Rightarrow
 d_{\mathcal Q}\!\left(
 q(F^{\Delta}(x,u,e)),
 q(F^{\Delta}(x',u,e))
 \right)
\leq
\varepsilon_q
```

for the declared regime.

If `epsilon_q=0`, same-address representatives must produce the same target future under matched conditions.

### 4.2 Stochastic case

A stochastic process need not collapse to one future state for the address to be sufficient.

The correct burden is distributional:

```math
A_{\Theta}(x)=A_{\Theta}(x')
\Rightarrow
q_*K^{\Delta}(\cdot\mid x,u,e)
\approx
q_*K^{\Delta}(\cdot\mid x',u,e)
```

within the declared discrepancy and tolerance.

Therefore:

> **Predictive closure does not mean a unique future. It means that unresolved same-address distinctions no longer alter the target-relevant future distribution beyond tolerance.**

## 5. Reachable-future geometry at an address

For an address value `z` under fixed matched intervention `u` and environment `e`, define the target-future family

```math
\mathscr P_{q,\Delta}(z,u,e;\Theta)
=
\left\{
q_*K^{\Delta}(\cdot\mid x,u,e):
A_{\Theta}(x)=z
\right\}.
```

Its address-conditioned diameter is

```math
\mathrm{Diam}_{q,\Delta}(z,u,e;\Theta)
=
\sup_{P,P'\in\mathscr P_{q,\Delta}(z,u,e;\Theta)}
d_Q(P,P').
```

Then

```math
\mathcal R_q(\Theta;U,E,\Delta)
=
\sup_{\substack{z\in\mathcal Z_{\Theta}\\u\in U,\,e\in E}}
\mathrm{Diam}_{q,\Delta}(z,u,e;\Theta)
```

on the tested region.

The conditioning on the same `u` and `e` is essential: differences caused by changing the intervention or environment are not same-address representative divergence unless those quantities were themselves omitted from the declared matching conditions.

This gives a direct geometric interpretation:

- a coarse or incomplete address leaves a wide family of target futures associated with one address value under matched conditions;
- a load-bearing address refinement separates representatives that should not have been grouped together;
- predictive closure is reached when the remaining same-address future family is sufficiently narrow in the declared target metric.

This is a geometry of **target-relevant future distributions**, not a claim that the full physical state space literally contracts.

## 6. Address refinement and completion gain

Let `c` be a candidate additional coordinate and define

```math
\Theta^+=\Theta\cup\{c\}.
```

The theoretical address-completion gain is

```math
\Gamma_q(c\mid\Theta)
=
\mathcal R_q(\Theta;U,E,\Delta)
-
\mathcal R_q(\Theta^+;U,E,\Delta).
```

Where exact population quantities are unavailable, estimate the same object on training data and require the gain to survive held-out or prospective testing.

A candidate coordinate earns inclusion when all applicable conditions hold:

1. it is typed and operationally measurable or otherwise independently specified;
2. it separates same-address representatives that previously produced materially different target futures;
3. the reduction in residual survives held-out or prospective testing;
4. the gain is not explained by information leakage, post-hoc target encoding, sample-selection artefact, or a changed intervention/environment class;
5. a simpler existing coordinate or ordinary state variable does not achieve the same closure with lower complexity.

A larger address is not automatically a better address.

> **Address sufficiency is minimum sufficient typed information for the declared target, not maximum context.**

## 7. Monotonic refinement in the exact construction

If `Theta_1` is a subset of `Theta_2`, then exact address refinement partitions each `Theta_1` equivalence class into equal or smaller classes.

Under the same target, transition kernel, intervention/environment set, and discrepancy,

```math
\Theta_1\subseteq\Theta_2
\quad\Longrightarrow\quad
\mathcal R_q(\Theta_2;U,E,\Delta)
\leq
\mathcal R_q(\Theta_1;U,E,\Delta)
```

for the exact population object.

This monotonicity does **not** guarantee better empirical performance after adding variables. Finite data, noise, overfitting, estimator variance, nonstationarity, or measurement error can make an enlarged empirical model worse. The empirical burden therefore remains prospective or held-out.

## 8. Residual divergence as an address diagnostic

Suppose

```math
\mathcal R_q(\Theta;U,E,\Delta)
>
\varepsilon_q.
```

The address has failed to close the target under the declared model and regime.

The failure does not identify one cause by itself. At minimum, distinguish:

1. **omitted load-bearing state** — a physical or system variable needed for the target is missing;
2. **omitted history or memory** — present state is insufficient because bounded path information carries predictive load;
3. **boundary/environment/preparation mismatch** — states labelled alike were not actually matched on a load-bearing condition;
4. **scale/address mismatch** — the active description is at the wrong scale or omits a coupled multiscale variable;
5. **measurement aliasing** — the current readout groups distinct target-relevant states together;
6. **regime mixture or nonstationarity** — one address class spans materially different dynamical regimes;
7. **model error** — the transition model or target map is wrong;
8. **insufficient data or estimator error** — the apparent divergence is not stable;
9. **genuine unresolved stochastic structure** — after the address and model are correctly specified, the remaining uncertainty belongs to the target distribution rather than to hidden representative dependence.

The scientific operation is therefore diagnostic, not metaphysical:

```text
same claimed address
+ materially different target futures
→ localise the divergence
→ test smallest plausible missing coordinate or model defect
→ readdress if the coordinate earns load
→ retest predictive closure
```

## 9. Reverse-engineering the missing address

Residual divergence can constrain what kind of coordinate is missing without uniquely determining it.

Let `B` be the set of same-address representative pairs contributing materially to the residual. A candidate coordinate `c` is useful only if it separates those pairs in a way that predicts the observed target divergence.

A practical search sequence is:

1. identify the target and the same-address pairs producing the largest stable residual;
2. classify the difference by candidate type — state, relation, history, boundary, environment, preparation, scale, interface, measurement, or model regime;
3. add the smallest independently measurable candidate coordinate;
4. recompute or re-estimate `R_q`;
5. require prospective or held-out improvement;
6. remove the candidate again to verify that closure degrades as predicted;
7. retain the coordinate only if the effect survives the ablation/restoration cycle.

Several different coordinates may produce similar closure. In that case the address remains underdetermined until an intervention, independent measurement, complexity penalty, or another discriminator separates them.

> **The lower predictive failure can constrain what an adequate fuller address must encode without proving a unique completion.**

## 10. Predictive versus interventional address sufficiency

Passive prediction and control remain distinct.

An address may satisfy

```math
\mathcal R_q(\Theta;U_{\mathrm{obs}},E,\Delta)
\leq\varepsilon_q
```

for an observational or passive regime while failing under a broader intervention class `U_int`:

```math
\mathcal R_q(\Theta;U_{\mathrm{int}},E,\Delta)
>
\varepsilon_q.
```

If the address will be used for manipulation, diagnosis, control, policy, or causal inference, the relevant burden is interventional sufficiency over the declared action class.

> **An address that closes observation may still open under intervention.**

## 11. Relation to law descent and law ownership

Module 33S2 permits a higher/effective address to own the active law object for a declared property only while that address has demonstrated sufficiency.

Module 33S4 sharpens the diagnostic burden.

If

```math
\mathcal R_q(\Theta;U,E,\Delta)
\leq\varepsilon_q,
```

the address has earned predictive closure for `q` over the declared regime. That result may support law descent at that address to the demonstrated strength.

If

```math
\mathcal R_q(\Theta;U,E,\Delta)
>\varepsilon_q,
```

the active address has not closed the target. The next action is not automatically to invent a new law. Test whether the address must be refined, moved downward, moved upward, augmented with bounded history, or replaced by a coupled multiscale description.

Thus:

```text
address
→ target-relative closure test
→ if closed: retain current law owner for that scope
→ if open: localise residual
→ refine / readdress / repair model
→ retest
```

This preserves Module 33S2's property-relative law ownership while giving predictive failure an explicit readdressing route.

## 12. Address ablation and restoration tests

The cleanest tests use systems where candidate address coordinates can be deliberately removed and restored.

### 12.1 Known-state dynamical system

Begin with a controlled deterministic or stochastic system whose relevant state variables are independently measurable.

1. construct a candidate sufficient address;
2. verify target closure on held-out trajectories;
3. remove one known load-bearing coordinate;
4. measure the increase in `R_q`;
5. restore the coordinate;
6. require the residual to return toward its original level.

### 12.2 History-bearing system

Use a system where matched present states can be reached through different recent histories.

If present-state addressing fails while bounded history restores closure, history earns address status for that target and horizon.

### 12.3 Boundary or environment ablation

Hold internal state as closely matched as possible while changing a declared boundary or environment variable.

If same internal states produce systematically different target futures and the boundary/environment coordinate predicts the split prospectively, the original address was incomplete for that target.

### 12.4 Scale test

Construct a higher/effective address that is sufficient for one property and then probe another property or intervention class.

If hidden lower-scale dependence reappears, the model must readdress downward or multiscale rather than declare the higher object unreal.

### 12.5 Negative control

Add coordinates expected to be irrelevant.

If arbitrary extra coordinates appear to improve closure only in-sample but fail held-out testing, the test correctly rejects context accumulation as address completion.

## 13. Strongest fair comparators

Before attributing a predictive-closure failure to a deeper MKUFT-specific structure, compare against the strongest adequate ordinary explanation.

Depending on the domain, this includes:

- a fuller physical state vector;
- standard state estimation or observability analysis;
- bounded history or memory augmentation;
- preparation and boundary conditioning;
- conventional coarse-graining or state aggregation;
- stochastic latent-state models;
- nonstationary or regime-switching models;
- measurement-error models;
- known control-theoretic or reduced-order representations.

If an ordinary model with an explicit measurable state variable closes the target, that variable belongs in the operational address and no stronger interpretation is required.

## 14. Relation to established predictive-state formalisms

Several established mathematical frameworks ask when a representation is sufficient for prediction, reconstruction, or coarse dynamics.

Relevant comparators include:

- computational mechanics and causal-state constructions, which group histories by equality of future conditional distributions;
- predictive state representations, which represent dynamical state through predictions of future observations under actions;
- observability and state-estimation theory, which ask whether the underlying state can be reconstructed or adequately inferred from available measurements;
- Markov lumpability and coarse-graining, which ask when projected states admit closed effective dynamics;
- reduced-dynamics and memory approaches, which show how omitted state can appear as history dependence or non-Markovian behaviour.

The present module uses those established burdens where appropriate and places them inside the MKUFT addressed-state, reachable-geometry, law-descent, and readdressing sequence.

Selected references:

- Shalizi, C. R. & Crutchfield, J. P. “Computational Mechanics: Pattern and Prediction, Structure and Simplicity.” *Journal of Statistical Physics* 104, 817–879 (2001). DOI `10.1023/A:1010388907793`.
- Littman, M. L. & Sutton, R. S. “Predictive Representations of State.” *Advances in Neural Information Processing Systems* 14 (2001).
- Kemeny, J. G. & Snell, J. L. *Finite Markov Chains*. D. Van Nostrand (1960).
- Kalman, R. E. “A New Approach to Linear Filtering and Prediction Problems.” *Journal of Basic Engineering* 82, 35–45 (1960).

## 15. Failure and reduction conditions

Reduce, reject, or retype the proposed address-completion claim when any of the following occurs:

- same-address representatives do not show stable target divergence under replication;
- the apparent residual disappears after correcting measurement or estimator error;
- a simpler standard state variable closes the target equally well;
- a candidate coordinate improves only in-sample and fails held-out or prospective testing;
- the coordinate encodes target information post-hoc or leaks future data;
- the intervention, environment, preparation, or time horizon changes between comparison groups without being declared;
- address refinement does not materially reduce the target residual;
- several candidate coordinates remain observationally equivalent and no discriminator separates them;
- the target itself is changed after inspecting results;
- stochastic variability already predicted by the declared transition distribution is incorrectly treated as address failure;
- the proposed higher-address law fails while a coupled multiscale model succeeds, requiring readdressing rather than forced closure.

## 16. Claim boundary

This module does **not** establish:

- universal determinism;
- that a complete address always exists at finite dimension;
- that every future can be uniquely predicted;
- that observer registration causes physical dynamics;
- that every missing coordinate is hidden physical state;
- that higher-scale law ownership is permanent;
- that predictive closure proves ontological completeness;
- or that mathematical closure alone establishes a new physical mechanism.

It supplies a narrower scientific question:

> **For a declared target, horizon, environment, intervention class, and tolerance, what is the smallest typed address for which unresolved same-address distinctions no longer change the target-relevant future distribution?**

## 17. Compressed rules

> **Address sufficiency is target-relative, not absolute.**

> **Predictive closure means same-address distinctions no longer change the declared target future beyond tolerance.**

> **A stochastic address can be sufficient without selecting one unique future.**

> **Residual future divergence is a diagnostic: test omitted state, history, boundary, environment, preparation, scale, measurement, regime, and model error before multiplying laws.**

> **Add the smallest coordinate that earns held-out predictive or interventional load. More context is not more complete address by default.**

> **If the address no longer closes the property, readdress and retest law ownership.**
