# 32S3 — Relational Brackets, Completion Geometry, and I→P Admissibility

**Author:** Mark Charles McLaughlin  
**Framework:** McLaughlin–Kairos Unified Field Theory (MKUFT)  
**MKUFT DOI:** [10.5281/zenodo.17780566](https://doi.org/10.5281/zenodo.17780566)  
**Citation and provenance:** [PROVENANCE_DOI_AND_ATTRIBUTION.md](../PROVENANCE_DOI_AND_ATTRIBUTION.md)  
**Canonical root:** [32 — Recursive Constraint Closure and Reachable-State Geometry](32_RECURSIVE_CONSTRAINT_CLOSURE_AND_REACHABLE_STATE_GEOMETRY.md)  
**Scale-transition owner:** [32S — Load-Bearing Relation Sets and Scale-Transition Tests](32S_LOAD_BEARING_RELATION_SETS_AND_SCALE_TRANSITION_TESTS.md)  
**Identity guards:** [32S1 — Invariant Persistence, Relational Addressability, and Scale Transition](32S1_INVARIANT_PERSISTENCE_RELATIONAL_ADDRESSABILITY_AND_SCALE_TRANSITION.md); [32S2 — Temporal Continuity Kernels and Minimum Identity Horizon](32S2_TEMPORAL_CONTINUITY_KERNELS_AND_MINIMUM_IDENTITY_HORIZON.md)  
**Novelty boundary:** [32A — Module 32 Novelty Audit and Contribution Boundary](32A_MODULE_32_NOVELTY_AUDIT_AND_CONTRIBUTION_BOUNDARY.md)  
**Public formulation date:** 15 August 2026  
**Rights:** Copyright © 2026 Mark Charles McLaughlin. All rights reserved unless an exact later publication states otherwise.  
**Status:** canonical formal refinement of the Module 32 family. It supplies a local-to-global compatibility scaffold, a completion-set definition for relationally constrained absence, a temporal mismatch measure, and a sharper operational form of the I→P admissibility question. It does not establish an independent information layer, holographic biology, consciousness, a new force, or a universal law of emergence.

## 1. Purpose

The Module 32 family already distinguishes changing state-space address, reachable-state geometry, load-bearing relations, scale-separated freedom and capability, relational addressability, individuality parity, and temporal continuity.

This supplement sharpens one remaining object:

> How can surrounding or overlapping relations specify what may occupy an address, how can that specification survive removal of one physical occupant, and how should the same mathematics be used to test a candidate I→P effect without assuming that information behaves like a message travelling through a hidden physical wire?

The central refinement is that three apparently different questions can be represented as the same **typed operation** at different addresses:

1. local-to-global compatibility — which local states can coexist as one organised object;
2. completion geometry — which states could lawfully occupy a missing or unobserved address given the remaining relations;
3. I→P admissibility — whether a declared information/relation variable changes the support or weighting of later physical transitions after the strongest adequate physical baseline is controlled.

The shared object is not a universal mechanism. It is a reusable **constraint-to-admissibility map** whose physical realisation remains domain-specific.

## 2. Relational bracket as a local-to-global compatibility object

Let a declared system domain at time `t` be covered by overlapping addressed regions

$$
\mathcal U_t=\{U_1,\ldots,U_n\}.
$$

Let

$$
N_t=N(\mathcal U_t)
$$

be the nerve of the cover: a simplex

$$
\sigma=\{i_0,\ldots,i_k\}\in N_t
$$

is present when the declared joint overlap

$$
U_\sigma
=\bigcap_{i\in\sigma}U_i
$$

is non-empty in the model.

Associate to each region `U` a typed local state space

$$
\mathcal F_t(U),
$$

and where a lawful restriction or translation is available, write

$$
\rho_{U\rightarrow V}:\mathcal F_t(U)\rightarrow\mathcal F_t(V),
\qquad V\subseteq U.
$$

This notation is deliberately **sheaf-compatible**, but the object must not be called a sheaf merely because restriction maps are written. Exact sheaf language is licensed only when the required locality and gluing axioms are actually satisfied by the implementation.

A local assignment is

$$
a_t=(a_1,\ldots,a_n),
\qquad
a_i\in\mathcal F_t(U_i).
$$

For each tested non-empty overlap `U_sigma`, define a compatibility residual

$$
e_\sigma(a_t)
=
\Psi_\sigma
\left(
\left\{
\rho_{U_i\rightarrow U_\sigma}(a_i)
\right\}_{i\in\sigma}
\right)
\geq0,
$$

where `Psi_sigma` is declared so that

$$
e_\sigma=0
$$

means exact compatibility under the tested relation and larger values mean larger disagreement in the declared residual geometry.

Different residuals must not be summed merely because they are numbers. If they have different units or meanings, retain the typed residual vector

$$
\mathbf e_B(a_t)
=
\left(e_\sigma(a_t)\right)_{\sigma\in N_t^+}.
$$

Only after each residual has a lawful scale `s_sigma>0` may a dimensionless aggregate be formed:

$$
\widetilde e_\sigma
=
\frac{e_\sigma}{s_\sigma},
$$

and, for declared weights `w_sigma>=0` and `p>=1`,

$$
E_B(a_t)
=
\left[
\frac{
\sum_{\sigma\in N_t^+}w_\sigma\widetilde e_\sigma(a_t)^p
}{
\sum_{\sigma\in N_t^+}w_\sigma
}
\right]^{1/p}.
$$

If no lawful normalisation exists, do not manufacture `E_B`; report the typed residuals separately.

Define the **relational bracket scaffold**

$$
\boxed{
\mathfrak B_t
=
\left(
\mathcal U_t,
N_t,
\mathcal F_t,
\rho_t,
\Psi_t,
\Theta_t
\right),
}
$$

where `Theta_t` contains declared tolerances, normalisations, and comparison rules.

The bracket is therefore not a container drawn around an object. It is the addressed architecture that states **which local descriptions overlap, how they are translated onto shared domains, and what counts as compatible there**.

## 3. Completion geometry — formalising a relationally specified absence

Suppose one addressed region `U_k` has no current occupant, is unobserved, or is intentionally ablated while the remaining assignment

$$
a_{-k}
$$

is retained.

For tolerance `epsilon_B`, define the **compatible completion set**

$$
\boxed{
\Omega_{k,t}^{\mathrm{comp}}
\left(a_{-k};\varepsilon_B\right)
=
\left\{
x\in\mathcal F_t(U_k):
E_B\!\left(a_{-k}\cup\{x\}\right)
\leq\varepsilon_B
\right\}.
}
$$

This object asks a precise negative-space question:

> Given everything that remains, what could occupy this address without violating the declared local-to-global relations beyond tolerance?

Several cases must remain distinct.

### 3.1 Narrow compatible absence

If

$$
\Omega_{k,t}^{\mathrm{comp}}\neq\varnothing
$$

and its declared diameter or uncertainty is small, the surrounding organisation strongly constrains the missing address even though the occupant is absent.

This supports the statement **relational address persists under occupant removal** only at the tested scale and tolerance. It does not establish a non-physical object occupying the missing region.

### 3.2 Broad compatible absence

If the completion set is large, the surrounding relations preserve an address but leave substantial unresolved freedom about what can fill it.

Where a lawful measure `mu_k` exists, Module 21's ambiguity discipline can be reused:

$$
A_{k,t}^{\mathrm{comp}}
=
\log\!\left(
1+
\frac{
\mu_k\!\left(\Omega_{k,t}^{\mathrm{comp}}\right)
}{
\mu_{0,k}
}
\right).
$$

A large value is not `more information`; it is greater unresolved completion volume under the declared measure.

### 3.3 Incompatible or disordered absence

If

$$
\Omega_{k,t}^{\mathrm{comp}}=\varnothing
$$

or the residual structure remains above tolerance for every tested completion, the missing region is not a neat latent slot under the current bracket. The surrounding relations themselves may be mutually incompatible, corrupted, or insufficiently specified.

This prevents the phrase **negative space** from being silently equated with an ordered template. Absence, ambiguity, and inconsistency are different objects.

## 4. Stable closure must survive time and perturbation

One low-residual instant is not enough to promote a higher-scale object.

For a declared temporal window `tau`, let the bracket satisfy a persistence criterion only when

$$
\Pr_{s\sim[t,t+\tau]}
\left[
E_B(a_s)\leq\varepsilon_B
\right]
\geq1-\delta_B,
$$

where the temporal sampling rule, tolerance `epsilon_B`, and failure fraction `delta_B` are specified in advance.

In deterministic implementations the probability notation may be replaced by a direct proportion of sampled times or by an appropriate continuous-time measure.

A closure claim should also survive preregistered perturbations inside a declared robustness neighbourhood. A bracket that closes only at one finely tuned point is a different object from a stable basin.

This is the temporal and perturbational extension of the Module 32S promotion requirement.

## 5. One typed operation behind bracket, completion, and reachable-state geometry

The preceding constructions can be compressed into a domain-typed **constraint-to-admissibility operator**.

At a declared layer/address `lambda`, let

$$
\mathfrak A_{\lambda,t}:
\left(
R_{\lambda,t},
X_{\lambda,t},
H_{\lambda,t}
\right)
\longrightarrow
2^{\mathcal X_{\lambda,t}}
$$

map the active relation/context structure `R`, current state information `X`, and retained history `H` to an admissible subset of the relevant state space:

$$
\mathfrak A_{\lambda,t}
\left(R,X,H\right)
=
\Omega_{\lambda,t}^{\mathrm{adm}}.
$$

This is a mathematical scaffold, not a claim that every domain implements one literal universal operator.

It contains several Module 32-family objects as specialisations:

- **completion geometry:** the remaining relations map to `Omega_k^comp` for a missing address;
- **ordinary reachable-state geometry:** current organisation maps to the subset of later states reachable under admissible transitions;
- **scale-conditioned action:** higher organisation removes some lower-scale states from the identity-compatible reachable set without destroying the underlying carrier;
- **candidate I→P admissibility:** a declared I-layer relation is tested for whether it changes the support or weighting of later P-layer transitions beyond an adequate physical baseline.

The important structural result is therefore:

> **Bracket and reach are not separate ideas. A bracket is one way of specifying the geometry of admissible completion and transition.**

## 6. I→P as an admissibility question rather than a message-pipe assumption

Let

$$
p_t\in\mathcal P_t
$$

be the measured physical state, `H_t^P` the relevant measured physical history, and

$$
i_t\in\mathcal I_t
$$

a candidate information/relation variable.

Instead of assuming that `i_t` acts as a force or travels through a hidden carrier, represent the empirical question by a conditional physical transition kernel

$$
K_P
\left(
 dp_{t+\Delta}
 \mid
 p_t,H_t^P,i_t
\right).
$$

The corresponding physical transition support is

$$
\Omega_{P,t}^{\mathrm{adm}}(i_t)
=
\operatorname{supp}
K_P
\left(
\cdot
\mid
p_t,H_t^P,i_t
\right).
$$

A candidate I-relation is **P-admissibility load-bearing** only if a preregistered deformation or relation-scramble

$$
i_t\rightarrow\widetilde i_t
$$

changes a declared property of the later physical transition distribution or support under matched conditions.

For a declared statistical distance or divergence `D_P`, a generic effect score is

$$
\Lambda_{I\rightarrow P}
=
\mathbb E
\left[
D_P
\left(
K_P(\cdot\mid p,H,i),
K_P(\cdot\mid p,H,\widetilde i)
\right)
\right].
$$

The expectation, sampling distribution, control construction, and distance must all be defined by the implementation. No universal choice is implied.

A support-level version may instead test

$$
d_\Omega
\left(
\Omega_P^{\mathrm{adm}}(i),
\Omega_P^{\mathrm{adm}}(\widetilde i)
\right)
>\eta_\Omega,
$$

where `d_Omega` is a lawful distance between the declared support objects.

### 6.1 P-realised semantic relation versus independent I→P dynamics

A non-zero `Lambda_(I→P)` does **not** by itself establish an independent information layer. A relation encoded entirely in measured physical organisation can be causally load-bearing while remaining P-realised.

The existing physical-only null remains controlling:

$$
H_0:
Y_{t+\Delta}
\perp\!\!\!\perp
I_t
\mid P_t,H_t^P.
$$

If

$$
i_t=f(P_t,H_t^P)
$$

under an adequate physical description, then the I-layer variable may be a useful relational abstraction, compression, or semantic description, but this test has not established independent I→P dynamics.

A stronger independent I→P candidate requires all of the following:

1. a declared information/relation variable that is not merely post-hoc naming;
2. representation-robust specification under relation-preserving re-encoding;
3. a strongest adequate P-state/history baseline;
4. held-out predictive or interventional gain beyond that baseline;
5. a deformation result that tracks the relation rather than one accidental carrier;
6. an explicit falsifier and ordinary-physics recovery regime.

This sharpens the I→P edge without converting a semantic description into a new physical ontology by definition.

## 7. Semantic load-bearingness is causal, not merely interpretive

The word `semantic` should not mean simply `meaningful to an observer`.

A relation earns **operational semantic load-bearingness** in a declared system only when preserving versus scrambling that relation changes a system-relevant future observable, viability condition, action distribution, admissible state support, or other preregistered consequence while the relevant lower-level statistics are controlled as far as the implementation permits.

This sits near established intervention-based semantic-information work. MKUFT does not claim invention of causal semantics. The narrower use here is to connect the intervention discipline directly to addressed reachable-state and completion geometry.

The public rule is:

> **If changing the relation does not change the tested future physical or functional possibilities, do not call that relation load-bearing for that claim.**

## 8. Temporal mismatch exposure — absence is not automatically cost

Persistent incompatibility may matter even when no single residual is catastrophic. To keep this idea typed, first use a dimensionless bracket residual `E_B(t)` as defined above.

For a declared horizon `T`, define cumulative **mismatch exposure**

$$
D_B(t;T)
=
\int_{t-T}^{t}
E_B(s)\,ds.
$$

`D_B` has units of time when `E_B` is dimensionless. It is not automatically energy, entropy, disease burden, repair cost, or biological damage.

A normalised temporal average may instead be used:

$$
\overline E_B(t;T)
=
\frac{1}{T}
D_B(t;T).
$$

For recency-sensitive systems, a non-negative declared kernel `w_T(t-s)` may give

$$
D_B^{(w)}(t)
=
\int_{t-T}^{t}
w_T(t-s)E_B(s)\,ds.
$$

The kernel must be justified rather than tuned after seeing the outcome.

Mismatch exposure earns a **cost** interpretation only if it predicts or causally changes a separately measured typed cost object

$$
\mathbf c_t
=
\left(
 c_t^{(1)},\ldots,c_t^{(m)}
\right)
$$

such as maintenance demand, energy use, repair load, error rate, viability loss, or another domain-specific quantity.

A useful promotion test is therefore whether

$$
D_B(t;T)
$$

adds held-out predictive or interventional value for later `c_(t+Delta)` or closure loss beyond instantaneous residual, measured P-state, and relevant history.

This keeps the exploratory idea of accumulated unresolved mismatch without declaring a universal `constraint debt` law.

## 9. Readout and scale promotion

A local-to-global relational structure can be mathematically compressible without being a new endogenous physical object. Readout and promotion must therefore remain separate.

Let

$$
R_{\ell\rightarrow L}:
\mathcal A_\ell
\rightarrow
\mathcal Y_L
$$

be a declared readout or coarse-graining map on admissible lower-scale assignments.

A candidate higher-scale state is

$$
y_L
=
R_{\ell\rightarrow L}(a_\ell).
$$

The readout induces an equivalence relation

$$
a\sim_R a'
\quad\Longleftrightarrow\quad
R_{\ell\rightarrow L}(a)
=
R_{\ell\rightarrow L}(a')
$$

or a tolerance-based analogue where exact equality is inappropriate.

This alone may describe only the observer's compression. A higher-scale **effective object** is promoted only when the Module 32S tests also pass: persistence, interventional load-bearingness, new viable capability, predictive compression, and boundary/closure specificity.

When those tests pass, the recursive handoff may be written

$$
\boxed{
\left(\mathfrak B_\ell,a_\ell\right)
\xrightarrow[
\text{stable closure}
]{R_{\ell\rightarrow L}}
O_L,
\qquad
O_L\in X_L.
}
$$

The promoted object may then participate as one constituent or load-bearing relation in the next-scale bracket:

$$
O_L
\in
\mathfrak B_L
\quad\text{in the typed role declared by the implementation}.
$$

This is the formal version of the recursive statement:

```text
lower-scale relations close
→ a higher-scale effective object becomes addressable
→ that whole becomes one participant in the next relational architecture
```

The recursion is asserted only across scales for which the promotion tests pass. It is not assumed to continue without bound.

Identity does not automatically transfer through this handoff. Modules 32S1 and 32S2 control same-address, readdressed-continuity, incorporation, and history-dependent identity claims.

## 10. Holography as a physical comparator, not an ontological shortcut

Optical holography supplies a useful controlled comparator because a spatial reconstruction can depend on distributed phase relations and a declared propagation/readout transform.

A simple scalar scaffold is

$$
U_z
=
\mathcal H_z
\left[
A(x,y)e^{i\phi(x,y)}
\right],
$$

where `A` is an aperture/amplitude field, `phi` a phase field, and `H_z` the declared optical propagation or reconstruction operator.

Under a mask `M(x,y)`,

$$
U_z^{(M)}
=
\mathcal H_z
\left[
M(x,y)A(x,y)e^{i\phi(x,y)}
\right].
$$

Phase-only holography provides a literal example in which local geometrical orientation can encode phase and the physically reconstructed object appears only after the relevant optical transform. Masking studies also show that partial loss can degrade the quality of the reconstructed image rather than implement a simple one-region-of-mask to one-region-of-image deletion.

The scientific use in MKUFT is therefore a **deformation template**:

> If another system is claimed to possess holographic or distributed reconstruction geometry, specify the encoding variables, transform/readout, and predicted response to local masking or phase deformation before calling the analogy physical.

Visual similarity, sacred geometry, or the phrase `the whole is in every part` is not sufficient.

## 11. Empirical P-layer comparators

The following examples are retained only as typed comparators. They do not establish an independent I layer.

### 11.1 Boundary geometry and interior address

Guruciaga et al. (2026) show that boundary geometry controls three-dimensional polar-defect configurations in a physical model of the mouse epiblast, and that predicted defect positions correspond to lumen nucleation sites. Experimental deformation of embryo shape produced additional lumen initiation sites near predicted defect locations.

For the present framework, the relevance is narrow and concrete:

> **relations at a boundary can constrain the location of an interior physical event.**

This is a P-layer example of surrounding geometry participating in an interior address.

### 11.2 Physical removal with persistent higher-order representation

Schone et al. (2025) longitudinally imaged people before and after arm amputation and found stable cortical hand/finger representations after the physical hand was removed.

For the present framework, the permitted statement is:

> **removal of a physical endpoint need not immediately erase every higher-order physical representation associated with that endpoint.**

The surviving nervous system is a physical implementation. Phantom-limb evidence does not by itself establish a non-physical hand or independent I→P dynamics.

## 12. Discriminating tests

### 12.1 Cover and representation robustness

Change the lawful cover, coordinate chart, encoding, or local representation while preserving the declared physical/relational object. A bracket claim should preserve its relevant completion and closure predictions within tolerance. If only one arbitrary partition makes the effect appear, treat the bracket as representation-dependent until shown otherwise.

### 12.2 Completion prediction

Remove, hide, or ablate a local occupant while preserving surrounding relations as far as possible. Use the remaining bracket to predict

$$
\Omega_k^{\mathrm{comp}}.
$$

Then restore or allow the region to repopulate. The realised completion should fall inside the preregistered predicted set at the stated rate. A bracket that cannot predict admissible completion is descriptive rather than load-bearing for this claim.

### 12.3 Surrounding-relation deformation

Preserve the candidate occupant state while changing selected surrounding relations. If the completion/address claim is correct, the admissible completion set or later realised state should deform in the predicted direction.

### 12.4 Higher-order overlap test

Test pairwise, triple, and higher-order overlap relations separately. If the claimed global organisation depends on genuine higher-order compatibility, pairwise agreement alone should fail to reproduce the full prediction in preregistered cases.

### 12.5 Temporal mismatch test

Compare instantaneous residual `E_B(t)` against `D_B(t;T)` or its justified kernel form for held-out prediction of later closure failure or independently measured cost. If accumulated exposure adds no information, retain the simpler instantaneous model.

### 12.6 I→P relation-scramble test

Construct `i` and `i_tilde` so that as much carrier-specific and lower-order statistical structure as possible is preserved while the proposed load-bearing relation is broken. Test the declared transition-kernel or support difference against the adequate P-only model.

### 12.7 Holographic deformation comparator

Where a system is explicitly claimed to have holographic/distributed reconstruction structure, predeclare its analogue of local masking, phase deformation, and reconstruction readout. Compare the measured degradation pattern with the predicted transform response and with simpler distributed-network alternatives.

### 12.8 Scale-promotion test

Do not promote a low-residual bracket to a higher-scale object unless the complete Module 32S effective-unit test passes. Observer-side compression alone is insufficient.

## 13. Failure and reduction conditions

Reduce this refinement if:

- local variables predict the tested outcome as well as the overlap/compatibility architecture;
- completion sets fail to predict lawful occupancy, regeneration, recovery, or held-out state resolution;
- the result depends on an arbitrary cover, coordinate system, or encoding and fails representation-preserving translation;
- pairwise relations explain the phenomenon and the proposed higher-order overlap adds no predictive value;
- temporal mismatch exposure adds no held-out value beyond instantaneous state/history;
- relation scrambling produces no predicted physical or functional change;
- the I variable is fully reducible to an adequate P-state/history description where independent I→P dynamics were claimed;
- a proposed readout is only observer coarse-graining and adds no endogenous interventional or predictive value;
- a holographic claim fails the preregistered transform/deformation response or is explained equally well by a simpler distributed system;
- scale recurrence survives only as visual resemblance or naming rather than typed relation and deformation equivalence.

If those failures occur, use the simpler local, physical, coarse-grained, network, or ordinary dynamical description.

## 14. Prior-art and novelty boundary

The broad mathematical and scientific ingredients used here have substantial prior art and are not claimed as MKUFT inventions.

Relevant neighbouring work includes:

- nerve constructions and local-to-global topology, which relate cover intersections to global topological information under explicit hypotheses;
- sheaf theory and approximate consistency of local assignments, including Michael Robinson's consistency-radius framework for noisy assignments;
- intervention-based semantic information, including Kolchinsky and Wolpert's causal-scrambling approach;
- causal emergence and information conversion across scales, including Varley and Hoel's treatment of macro-scale synergy;
- optical holography and phase encoding/reconstruction;
- established coarse-graining, quotient, constraint-closure, morphogenetic, and systems-biology methods.

The candidate MKUFT contribution is narrower:

> integrate addressed state-space discipline, load-bearing relation tests, local-to-global completion geometry, persistent mismatch exposure, scale promotion, and the I→P physical-null boundary into one operational audit in which `relationally specified absence` and `changed physical admissibility` are tested by the same typed constraint-to-admissibility grammar.

Historical priority for that exact integration is not asserted without broader literature review. Module 32A owns the evolving novelty audit.

## 15. References

- Robinson, M. (2018). *Assignments to sheaves of pseudometric spaces*. arXiv:1805.08927.
- Kolchinsky, A. and Wolpert, D. H. (2018). *Semantic information, autonomous agency and non-equilibrium statistical physics*. Interface Focus 8:20180041. DOI `10.1098/rsfs.2018.0041`.
- Varley, T. F. and Hoel, E. (2022). *Emergence as the conversion of information: a unifying theory*. Philosophical Transactions of the Royal Society A 380:20210150. DOI `10.1098/rsta.2021.0150`.
- Ni, X. et al. (2013). *Three-dimensional optical holography using a plasmonic metasurface*. Nature Communications 4:2807. DOI `10.1038/ncomms3808`.
- Guruciaga, P. C. et al. (2026). *Boundary geometry controls a topological defect transition that determines lumen nucleation in embryonic development*. Nature Materials 25, 1278–1287. DOI `10.1038/s41563-026-02594-7`.
- Schone, H. R. et al. (2025). *Stable cortical body maps before and after arm amputation*. Nature Neuroscience 28, 2015–2021. DOI `10.1038/s41593-025-02037-7`.

## 16. Compressed rules

> **The bracket is not the missing object. It is the addressed compatibility architecture that constrains what could occupy or follow from the current relations.**

> **Physically absent does not imply relationally unspecified; relationally specified does not imply physically occupied.**

> **Negative space can be narrow, ambiguous, or inconsistent. Do not call all three one thing.**

> **A persistent mismatch is not automatically a cost. Measure mismatch first; measure cost separately; then test the coupling.**

> **The I→P question can be posed as a change in physical transition support or weighting without assuming that information is a hidden force or message carrier.**

> **A non-zero relational effect may still be fully P-realised. Independent I→P dynamics must beat the adequate P-state/history null.**

> **Readout does not create an endogenous scale transition. Promotion requires persistence, intervention, new capability, predictive compression, and boundary specificity.**

> **Holography is a deformation-tested physical comparator, not a licence to call every distributed relation holographic.**

> **At every justified scale: relations constrain admissibility; stable closure can become an effective object; that object may then participate in the next bracket.**