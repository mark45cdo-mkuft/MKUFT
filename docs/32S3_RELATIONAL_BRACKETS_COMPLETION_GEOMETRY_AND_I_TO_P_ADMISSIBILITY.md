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
**Status:** canonical formal refinement of the Module 32 family. It supplies a typed relation-scope compatibility scaffold, completion geometry for relationally constrained absence, a fiber/quotient scale-handoff representation, temporal mismatch measures, and an operational I→P admissibility test. It does not establish an independent information layer, holographic biology, consciousness, a new force, nonlocal signalling, or a universal law of emergence.

## 1. Purpose

The Module 32 family already distinguishes changing state-space address, reachable-state geometry, load-bearing relations, scale-separated freedom and capability, relational addressability, individuality parity, and temporal continuity.

This supplement sharpens a common mathematical object behind three questions:

1. **compatibility** — which local or distributed states can coexist under the declared relations;
2. **completion** — what could lawfully occupy a missing or unobserved address given the relations that remain;
3. **I→P admissibility** — whether a declared information/relation variable changes the support or weighting of later physical transitions after the strongest adequate physical baseline is controlled.

The shared object is a typed **constraint-to-admissibility grammar**, not a claim that every domain uses one physical mechanism.

## 2. Local coordinates, geometric overlap, and typed relation scopes

Let a declared system at time `t` have addressed components or regions

$$
\mathcal U_t=\{U_1,\ldots,U_n\},
$$

with local state spaces

$$
\mathcal F_t(U_i).
$$

The ambient assignment space is

$$
\mathcal L_t
=
\prod_{i=1}^{n}\mathcal F_t(U_i).
$$

This product is bookkeeping for simultaneous coordinate assignments. It does **not** assert statistical independence, causal independence, separability, or physical isolation of the factors.

Where physical/geometric overlap is meaningful, let

$$
N_t=N(\mathcal U_t)
$$

be the nerve of the cover. A simplex `sigma` records a declared non-empty overlap among its indexed regions. The nerve is useful for genuinely local geometric relations, but it is not the whole bracket.

Define a broader typed relation-scope family

$$
\mathfrak E_t=\{r_1,\ldots,r_m\}.
$$

Each relation `r` has a non-empty support

$$
S(r)\subseteq\{1,\ldots,n\},
$$

identifying the coordinates on which that relation depends, together with a declared relation type, scale, and measurement rule.

A relation scope may represent geometric overlap, regulatory coupling, system–environment coupling, temporal linkage, contextual compatibility, semantic/functional relation, or another operationally defined relation class. A non-geometric scope does **not** by itself imply a nonlocal physical mechanism or a new layer.

Geometric overlap relations form at most a typed subfamily

$$
\mathfrak E_t^{\mathrm{geom}}\subseteq\mathfrak E_t.
$$

For a relation `r` and coordinate `i\in S(r)`, let

$$
\eta_{i\rightarrow r}:
\mathcal F_t(U_i)
\rightarrow
\mathcal Y_{r,i}
$$

extract or translate the state information relevant to that relation. For a genuine geometric overlap, `eta` may reduce to an ordinary restriction map onto the shared domain. For other relation types it must be separately defined and justified.

This separation is deliberate:

> **spatial overlap is one way for relations to be load-bearing; it is not assumed to be the only way.**

## 3. Relational bracket and compatible assignment region

For assignment

$$
a_t=(a_1,\ldots,a_n)\in\mathcal L_t,
$$

define a typed residual for each declared relation

$$
e_r(a_t)
=
\Psi_r
\left(
\left\{
\eta_{i\rightarrow r}(a_i)
\right\}_{i\in S(r)}
\right)
\geq0,
$$

where `Psi_r` is defined so that `e_r=0` means exact compatibility under that relation and larger values mean larger disagreement in the declared residual geometry.

Let `epsilon_r` be a preregistered tolerance in the same units as `e_r`. Define the componentwise compatibility indicator

$$
\chi_B(a_t)
=
\mathbf 1
\left[
e_r(a_t)\leq\varepsilon_r
\quad\forall r\in\mathfrak E_t
\right].
$$

The componentwise test is primary. Different residual types must not be summed merely because they are numerical.

The bracket selects the compatible assignment region

$$
\boxed{
\mathfrak C_{B,t}
=
\left\{
a\in\mathcal L_t:
\chi_B(a)=1
\right\}
\subseteq\mathcal L_t.
}
$$

For reporting, retain the typed residual vector

$$
\mathbf e_B(a_t)
=
\left(e_r(a_t)\right)_{r\in\mathfrak E_t}.
$$

Only after each residual has a lawful scale `s_r>0` may a dimensionless aggregate be formed:

$$
\widetilde e_r
=
\frac{e_r}{s_r},
$$

$$
E_B(a_t)
=
\left[
\frac{
\sum_{r\in\mathfrak E_t}w_r\widetilde e_r(a_t)^p
}{
\sum_{r\in\mathfrak E_t}w_r
}
\right]^{1/p},
\qquad
w_r\ge0,
\quad p\ge1.
$$

If no lawful normalisation exists, do not manufacture `E_B`; retain the typed residual vector.

Define the relational bracket scaffold

$$
\boxed{
\mathfrak B_t
=
\left(
\mathcal U_t,
N_t,
\mathfrak E_t,
\mathcal F_t,
\eta_t,
\Psi_t,
\Theta_t
\right),
}
$$

where `Theta_t` contains declared tolerances, normalisations, comparison rules, and representation assumptions.

The bracket is not a container surrounding an object. It is the addressed architecture specifying **which coordinates participate in which relations and what joint assignments those relations permit**.

## 4. Completion geometry — a missing address as a conditional fiber

Suppose coordinate `k` is missing, unobserved, or intentionally ablated while the remaining partial assignment

$$
a_{-k}
$$

is retained.

For candidate completion

$$
x\in\mathcal F_t(U_k),
$$

define

$$
a_{-k}\oplus_k x
=
(a_1,\ldots,a_{k-1},x,a_{k+1},\ldots,a_n).
$$

Separate relations that touch the missing address from those that do not:

$$
\mathfrak E_{k,t}
=
\{r\in\mathfrak E_t:k\in S(r)\},
$$

$$
\mathfrak E_{-k,t}
=
\{r\in\mathfrak E_t:k\notin S(r)\}.
$$

Define the retained-background test

$$
\chi_{B,-k}(a_{-k})
=
\mathbf 1
\left[
e_r(a_{-k})\leq\varepsilon_r
\quad\forall r\in\mathfrak E_{-k,t}
\right],
$$

for residuals well-defined without coordinate `k`.

Define the local completion test

$$
\chi_{B,k}(a_{-k}\oplus_k x)
=
\mathbf 1
\left[
e_r(a_{-k}\oplus_k x)\leq\varepsilon_r
\quad\forall r\in\mathfrak E_{k,t}
\right].
$$

When the retained background is compatible,

$$
\chi_{B,-k}(a_{-k})=1,
$$

the compatible completion set is

$$
\boxed{
\Omega_{k,t}^{\mathrm{comp}}(a_{-k})
=
\left\{
x\in\mathcal F_t(U_k):
\chi_{B,k}(a_{-k}\oplus_k x)=1
\right\}.
}
$$

If the retained background is already inconsistent, a missing-address inference is confounded: unrelated relation failures cannot be attributed to the missing coordinate.

If

$$
\mathfrak E_{k,t}=\varnothing,
$$

the current bracket supplies no relation constraining that coordinate. The address is unconstrained by this bracket rather than positively specified.

### 4.1 Fiber form

Let

$$
\pi_{-k}:\mathcal L_t
\rightarrow
\prod_{i\neq k}\mathcal F_t(U_i)
$$

forget coordinate `k`, and let

$$
\pi_k:\mathcal L_t\rightarrow\mathcal F_t(U_k)
$$

select it.

The compatibility fiber over the retained assignment is

$$
\mathfrak F_{k,t}(a_{-k})
=
\mathfrak C_{B,t}
\cap
\pi_{-k}^{-1}(a_{-k}).
$$

The completion set is its missing-coordinate image:

$$
\boxed{
\Omega_{k,t}^{\mathrm{comp}}(a_{-k})
=
\pi_k\!\left(
\mathfrak F_{k,t}(a_{-k})
\right).
}
$$

This is standard fiber/projection mathematics. Its role here is operational: **hold the retained relational address fixed and ask what values remain admissible at the missing coordinate.**

### 4.2 Four distinct absence cases

1. **Narrow completion:** `Omega_k^comp` is non-empty and small under a lawful uncertainty/diameter measure. The remaining relations strongly constrain what belongs there.
2. **Broad completion:** `Omega_k^comp` is large. The address is retained but substantially ambiguous.
3. **Local incompatibility:** the retained background is compatible but `Omega_k^comp` is empty. No tested value satisfies all relations touching the missing address.
4. **Background inconsistency:** relations not involving the missing address are already failing, so local completion cannot be interpreted cleanly.

Thus:

> **physically absent does not imply relationally unspecified; relationally specified does not imply physically occupied.**

## 5. Ambiguity and temporal mismatch exposure

Where a lawful measure `mu_k` exists on a completion space, a completion-ambiguity index may reuse Module 21's discipline:

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

This measures unresolved completion volume under the declared encoding; it is not automatically information, energy, or cost.

One compatible instant is not enough to establish stable closure. For a time interval over which the bracket observables remain lawfully comparable, define

$$
P_B(t;\tau)
=
\frac{1}{\tau}
\int_t^{t+\tau}
\chi_B(a_s)\,ds.
$$

A persistence criterion may require

$$
P_B(t;\tau)\ge1-\delta_B.
$$

If the relation family, local state spaces, encodings, tolerances, or comparison rules change materially, use Module 31 transport/comparison discipline, partition the interval, or do not report one persistence scalar.

Where a lawful dimensionless aggregate `E_B(t)` exists, define mismatch exposure

$$
D_B(t;T)
=
\int_{t-T}^{t}E_B(s)\,ds.
$$

`D_B` has units of time if `E_B` is dimensionless. It is not automatically energy, entropy, damage, disease burden, or maintenance cost.

A mismatch exposure earns a **cost** interpretation only if it predicts or causally changes a separately measured typed cost object

$$
\mathbf c_t
=
\left(c_t^{(1)},\ldots,c_t^{(m)}\right)
$$

under held-out or interventional testing.

## 6. Addressed constraint-to-admissibility operator

The preceding objects can be compressed into a typed constraint-to-admissibility operator without forcing a fixed state space.

At declared layer/address `lambda`, let

$$
\mathfrak X_\lambda
=
\bigsqcup_{\alpha\in A_\lambda}
\{\alpha\}\times\mathcal X_{\lambda,\alpha}
$$

be the addressed state family.

For current construction address `alpha_t`, define schematically

$$
\mathcal Q_{\lambda,t}:
\mathfrak E_{\lambda,t}
\times
\mathcal X_{\lambda,\alpha_t}
\times
\mathcal H_{\lambda,t}
\longrightarrow
2^{\mathfrak X_\lambda},
$$

with

$$
\mathcal Q_{\lambda,t}(\mathfrak E,x,h)
=
\Omega_{\lambda,t}^{\mathrm{adm}}.
$$

The output is an **addressed admissible region** and may include transitions into a different construction/state-space address where the implementation permits that change.

This operator is a scaffold, not a universal physical law. It covers as typed specialisations:

- compatible completion of a missing address;
- ordinary reachable-state restriction;
- scale-conditioned loss of lower-level independent addressability;
- candidate I→P changes in later physical transition support or weighting.

The parent structural statement is:

> **bracket and reach are two views of constraint-shaped admissibility.**

## 7. I→P as an admissibility question, not a message-pipe assumption

Let

$$
p_t\in\mathcal P_t
$$

be measured physical state, `H_t^P` the relevant measured physical history, and

$$
i_t\in\mathcal I_t
$$

a candidate information/relation variable.

Represent the empirical question by a conditional physical transition kernel

$$
K_P
\left(
dp_{t+\Delta}
\mid
p_t,H_t^P,i_t
\right).
$$

The corresponding support is

$$
\Omega_{P,t}^{\mathrm{adm}}(i_t)
=
\operatorname{supp}
K_P
\left(
\cdot\mid p_t,H_t^P,i_t
\right).
$$

For a preregistered lawful relation deformation

$$
i_t\rightarrow\widetilde i_t,
$$

a generic distributional effect score is

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
\right],
$$

where the sampling distribution and distance/divergence `D_P` are declared by the implementation.

A support-level test may instead use

$$
d_\Omega
\left(
\Omega_P^{\mathrm{adm}}(i),
\Omega_P^{\mathrm{adm}}(\widetilde i)
\right)
>\eta_\Omega.
$$

A non-zero conditional difference is not automatically causal. If `i` cannot be changed or causally identified independently of relevant P variables, report predictive association rather than causal I→P evidence.

The existing physical-only null remains controlling:

$$
H_0:
Y_{t+\Delta}
\perp\!\!\!\perp
I_t
\mid P_t,H_t^P.
$$

If the candidate relation is fully reducible to adequate measured physical organisation/history—for example

$$
i_t=f(P_t,H_t^P),
$$

then the I-layer variable may remain a useful relational abstraction or compression, but independent I→P dynamics have not been established.

A stronger independent I→P candidate requires representation robustness, a strongest adequate P baseline, held-out predictive or interventional gain, relation-specific deformation that does not merely introduce an uncontrolled P change, ordinary-limit recovery, and an explicit falsifier.

## 8. Operational semantic load-bearingness

The word `semantic` should not mean merely `meaningful to an observer`.

A declared relation earns **operational semantic load-bearingness** only when preserving versus disrupting that relation changes a preregistered system-relevant future observable, action distribution, viability condition, admissible state support, or other consequence while relevant lower-order statistics and carrier details are controlled as far as the implementation permits.

This is adjacent to established intervention-based semantic-information work. MKUFT does not claim invention of causal semantics.

The public rule is:

> **If changing the relation does not change the tested future physical or functional possibilities, do not call that relation load-bearing for that claim.**

## 9. Fiber–quotient scale handoff

The compatibility region supports two complementary questions.

### 9.1 Zoom in — fiber

Fix retained coordinates and ask which states remain admissible at a missing coordinate. Section 4 gives this as the fiber/projection object

$$
\mathfrak F_{k,t}(a_{-k})
=
\mathfrak C_{B,t}
\cap
\pi_{-k}^{-1}(a_{-k}),
$$

$$
\Omega_{k,t}^{\mathrm{comp}}
=
\pi_k(\mathfrak F_{k,t}).
$$

### 9.2 Zoom out — quotient

Let a declared higher-scale readout be

$$
R_{\ell\rightarrow L}:
\operatorname{Dom}(R_{\ell\rightarrow L})
\subseteq
\mathfrak C_{B,\ell}
\longrightarrow
\mathcal Y_L.
$$

Define

$$
a\sim_R a'
\quad\Longleftrightarrow\quad
R_{\ell\rightarrow L}(a)
=
R_{\ell\rightarrow L}(a'),
$$

or a tolerance-based analogue.

The quotient

$$
\mathfrak C_{B,\ell}/\!\sim_R
$$

groups compatible lower-scale assignments that are indistinguishable under the declared higher-scale readout.

This quotient is not automatically a physically autonomous object. Observer-side compression alone is insufficient.

A higher-scale effective object is promoted only after the Module 32S tests pass: persistence, interventional load-bearingness, new viable capability, predictive compression, and boundary/closure specificity.

When they pass, schematically

$$
\boxed{
\mathcal L_\ell
\supseteq
\mathfrak C_{B,\ell}
\longrightarrow
\mathfrak C_{B,\ell}/\!\sim_R
\xrightarrow{\text{promotion tests}}
O_L.
}
$$

To use the promoted whole at the next scale, declare a lawful typing map

$$
\iota_{L\rightarrow L^+}:
\mathcal O_L
\rightarrow
\mathcal X_{L^+}^{\mathrm{const}},
$$

so that

$$
\iota_{L\rightarrow L^+}(O_L)
\in
\mathcal X_{L^+}^{\mathrm{const}}.
$$

That typed constituent may then participate in the next bracket's relation scopes.

Thus the recursive scale grammar is

```text
local state product
→ relation-compatible subset
→ quotient under declared higher-scale readout
→ effective-object promotion when earned
→ typed constituent in the next relational bracket
```

while the complementary completion query is

```text
relation-compatible subset
→ fix retained coordinates
→ take a projection fiber
→ recover admissible completion of the missing coordinate
```

Fiber and quotient are two mathematical views of the same compatibility geometry, not two physical mechanisms.

The recursion is asserted only across scales where promotion tests pass. It is not assumed to continue without bound. Identity continuity remains governed separately by Modules 32S1 and 32S2.

## 10. Holography as a deformation-tested physical comparator

Optical holography is useful because a spatial reconstruction can depend on distributed phase relations and a declared propagation/readout transform.

A simple scalar scaffold is

$$
U_z
=
\mathcal H_z
\left[
A(x,y)e^{i\phi(x,y)}
\right].
$$

Under local mask `M(x,y)`,

$$
U_z^{(M)}
=
\mathcal H_z
\left[
M(x,y)A(x,y)e^{i\phi(x,y)}
\right].
$$

Metasurface holography provides a literal example in which local element orientation encodes phase and the reconstructed spatial object appears only after the relevant optical transform.

The MKUFT use is methodological:

> If another system is claimed to possess holographic or distributed reconstruction geometry, specify the encoding variables, transform/readout, and predicted response to local masking or phase deformation before calling the analogy physical.

Visual similarity, sacred geometry, or the phrase `the whole is in every part` is insufficient.

## 11. Empirical P-layer comparators

These examples remain P-layer comparators, not evidence for an independent I layer.

### 11.1 Boundary geometry and interior address

Guruciaga et al. (2026) report that boundary geometry controls polar-defect configuration in a model of the mouse epiblast and that predicted defect positions correspond to lumen nucleation sites. The narrow relevance here is that **relations at a boundary can constrain the location of an interior physical event**.

### 11.2 Physical removal with persistent higher-order representation

Schone et al. (2025) report stable cortical hand/finger representations after arm amputation. The permitted structural statement is that **removal of a physical endpoint need not immediately erase every higher-order physical representation associated with that endpoint**. The surviving nervous system remains a physical implementation.

## 12. Discriminating tests

### 12.1 Relation-family and representation robustness

Change the lawful cover, coordinate chart, encoding, or higher-order relation representation while preserving the declared underlying object. Compare geometric-nerve, hypergraph/relation-scope, or other justified representations where appropriate. If the effect appears only under one arbitrary representation, reduce the claim.

### 12.2 Completion prediction

Remove, hide, or ablate a local occupant while preserving surrounding relations as far as possible. First verify retained-background compatibility. Predict the completion fiber using only relations whose support includes the missing coordinate. On restoration or repopulation, test whether realised completions fall inside the preregistered predicted set at the stated rate.

### 12.3 Surrounding-relation deformation

Preserve the candidate occupant state while changing selected surrounding or contextual relations. The completion fiber or later realised state should deform in the predicted direction if those relations are load-bearing.

### 12.4 Higher-order relation test

Compare pairwise-only models with preregistered higher-order relation scopes. If higher-order compatibility is claimed to matter, it must add held-out predictive/interventional value rather than merely redescribe pairwise structure.

### 12.5 Temporal mismatch test

Compare instantaneous residuals against lawful cumulative mismatch exposure for held-out prediction of later closure failure or independently measured cost. If accumulated exposure adds no value, keep the simpler instantaneous model.

### 12.6 I→P relation-scramble test

Preserve as much carrier-specific and lower-order physical structure as practical while disrupting the proposed relation. Test the later transition kernel/support against the adequate P-only model. If causal isolation cannot be achieved, do not call the result causal I→P evidence.

### 12.7 Holographic deformation comparator

Predeclare the analogue of encoding, phase/amplitude deformation, mask, propagation/readout, and predicted reconstruction degradation. Compare with simpler distributed-network alternatives.

### 12.8 Scale-promotion test

Compare the proposed quotient/readout with alternative coarse-grainings. Promote a higher-scale object only if the full Module 32S effective-unit test passes.

## 13. Failure and reduction conditions

Reduce this refinement if:

- local or pairwise variables predict the outcome as well as the declared relation-scope architecture;
- completion fibers fail held-out occupancy, regeneration, recovery, or state-resolution tests;
- unrelated background inconsistency is mistaken for failure of a missing-address completion;
- the result depends on an arbitrary cover, relation representation, coordinate system, or encoding and fails representation-preserving translation;
- higher-order scopes add no value beyond pairwise relations;
- temporal mismatch is accumulated across non-comparable addresses without lawful transport or adds no value beyond instantaneous state/history;
- relation scrambling produces no predicted consequence;
- a claimed causal I→P result cannot separate relation change from uncontrolled P-layer change;
- the I variable reduces to the adequate P-state/history description where independent I→P dynamics were claimed;
- the quotient/readout is observer-only compression with no endogenous interventional or predictive gain;
- a holographic claim fails the preregistered transform/deformation response or is explained equally well by a simpler distributed model;
- cross-scale recurrence survives only as naming or visual resemblance rather than typed relation and deformation equivalence.

If these failures occur, use the simpler local, physical, pairwise, network, coarse-grained, or ordinary dynamical description.

## 14. Prior-art and novelty boundary

The broad ingredients used here are established and are not claimed as MKUFT inventions.

Relevant neighbours include:

- nerve constructions, sheaves, restriction/gluing, fibers, projections, quotients, and coarse-graining;
- hypergraphs and higher-order networks for arbitrary non-pairwise relation scopes;
- sheaf-theoretic local-to-global analysis over contextual measurement covers, including non-locality/contextuality work;
- intervention-based semantic information;
- causal emergence and information conversion across scales;
- optical holography and phase encoding/reconstruction;
- constraint-closure, morphogenetic, neural, and systems-biology methods.

The candidate MKUFT contribution is narrower:

> integrate addressed changing-state-space discipline, typed relation scopes, completion fibers, quotient-based scale readout with separate promotion tests, persistent mismatch exposure, and the I→P physical-null boundary into one operational audit in which relationally specified absence and changed physical admissibility are tested by the same constraint-to-admissibility grammar.

Historical priority for that exact integration is not asserted without broader literature review. Module 32A owns the evolving novelty audit.

## 15. References

- Abramsky, S. and Brandenburger, A. (2011). *The Sheaf-Theoretic Structure of Non-Locality and Contextuality*. arXiv:1102.0264; New Journal of Physics 13, 113036.
- Robinson, M. (2018). *Assignments to sheaves of pseudometric spaces*. arXiv:1805.08927.
- Kolchinsky, A. and Wolpert, D. H. (2018). *Semantic information, autonomous agency and non-equilibrium statistical physics*. Interface Focus 8:20180041. DOI `10.1098/rsfs.2018.0041`.
- Varley, T. F. and Hoel, E. (2022). *Emergence as the conversion of information: a unifying theory*. Philosophical Transactions of the Royal Society A 380:20210150. DOI `10.1098/rsta.2021.0150`.
- Zhang, Y., Lucas, M. and Battiston, F. (2023). *Higher-order interactions shape collective dynamics differently in hypergraphs and simplicial complexes*. Nature Communications 14:1605. DOI `10.1038/s41467-023-37190-9`.
- Huang, L., Chen, X., Mühlenbernd, H. et al. (2013). *Three-dimensional optical holography using a plasmonic metasurface*. Nature Communications 4:2808. DOI `10.1038/ncomms3808`.
- Guruciaga, P. C. et al. (2026). *Boundary geometry controls a topological defect transition that determines lumen nucleation in embryonic development*. Nature Materials 25, 1278–1287. DOI `10.1038/s41563-026-02594-7`.
- Schone, H. R. et al. (2025). *Stable cortical body maps before and after arm amputation*. Nature Neuroscience 28, 2015–2021. DOI `10.1038/s41593-025-02037-7`.

## 16. Compressed rules

> **Geometric overlap is one typed relation class, not the whole relation architecture.**

> **The ambient product of local state spaces is a coordinate scaffold, not an independence assumption.**

> **The bracket is the typed relation-scope architecture that selects compatible assignments.**

> **A missing-address question is a fiber of the compatible region; a higher-scale readout is a quotient of it.**

> **Physically absent does not imply relationally unspecified; relationally specified does not imply physically occupied.**

> **Negative space can be narrow, ambiguous, locally incompatible, or confounded by background inconsistency.**

> **Persistent mismatch is not automatically cost. Measure mismatch and cost separately, then test their coupling.**

> **The I→P question can be posed as changed physical transition support or weighting without assuming a hidden force, carrier, or message pipe.**

> **A non-zero relational effect may remain fully P-realised; a non-zero conditional difference is not automatically causal.**

> **Readout does not create a scale transition. Promotion requires persistence, intervention, new capability, predictive compression, and boundary specificity.**

> **Holography is a deformation-tested physical comparator, not an ontological shortcut.**

> **At every justified scale: typed relations constrain addressed admissibility; stable compatible structure can be promoted to an effective object; that object may become one typed participant in the next bracket.**