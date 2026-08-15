# MKUFT Integrated Master Spine

<!-- MKUFT-PROVENANCE-HEADER:START -->
**Author:** Mark Charles McLaughlin  
**Framework:** McLaughlin–Kairos Unified Field Theory (MKUFT)  
**MKUFT DOI:** `10.5281/zenodo.17780566`  
**Provenance:** This module is part of the public MKUFT canon. Exact revisions are timestamped by Git history.  
**Citation:** See [`PROVENANCE_DOI_AND_ATTRIBUTION.md`](PROVENANCE_DOI_AND_ATTRIBUTION.md).  
<!-- MKUFT-PROVENANCE-HEADER:END -->

**Status:** public integrated synthesis for the evolving MKUFT GitHub canon.

## 0. Purpose and claim boundary

MKUFT is a speculative research framework, not an accepted completed physical theory.

This master spine is a **synthesis and routing document**. Dedicated modules own full derivations, definitions, experiments, references, and falsifiers. If a compressed expression here conflicts with its canonical owner, the canonical owner controls and this spine must be corrected.

MKUFT survives only where it remains:

- typed by domain and layer;
- compatible with established results in their demonstrated regimes;
- explicit about whether an equation is notation, scaffold, model, or derived mechanism;
- open to ordinary explanations and strong alternatives;
- falsifiable at the branch where the claim is made;
- reconstructable from several public entry routes without changing meaning.

## 1. Core research question

MKUFT asks whether stable outcomes can be studied through a recurring grammar of:

```text
possibility
→ constraint
→ admissible transition
→ cost
→ coherence / stability
→ boundary
→ measurement / registration
→ falsification
→ outcome
```

The recurrence of this grammar across domains does not establish one identical mechanism across those domains.

## 2. Typed S–I–P–O architecture

```text
S = Substrate / structured possibility
I = Information / relation / constraint
P = Physical expression and dynamics
O = Observer-positioned registration and bounded participation
```

The layers are typed addresses, not four ordinary spatial dimensions.

### S — Substrate

A mathematical handle is the measure space

$$
S=(\Omega,\Sigma,\mu).
$$

This is a formal representation of a possibility/source domain. It is not evidence that a hidden material medium, lattice, or additional physical space has been detected.

### I — Information

To avoid symbol collision, use

$$
\mathcal I=L^2(\Omega,\mu),
\qquad i\in\mathcal I,
$$

where $I$ remains the layer label, $\mathcal I$ the selected information-state/function space, and $i$ one information structure.

Information earns independent physical significance only where a defined coupling adds measurable content beyond an adequate physical description.

### P — Physical

The P-layer contains measurable physical states, fields, bodies, instruments, environments, timing, and dynamics. Physical claims require physical variables, units, controls, conservation accounting where applicable, and ordinary-physics baselines.

### O — Observer

The O-layer contains observer-positioned registration, measurement context, record, attention, interpretation, and any bounded state variable that is operationally defined.

Observer language cannot replace a missing physical mechanism.

## 3. Realisation scaffold

For event $E$, a working unnormalised weight is

$$
\widetilde W(E)
=
\int
D_{\mathrm{phys}}(E\mid i)
W_{SI}(i\mid S,E)
C_O(O\mid i,E)
\,d\nu(i),
$$

with

$$
P_{\mathrm{realized}}(E)
=
\frac{\widetilde W(E)}{Z}.
$$

$D_{\mathrm{phys}}$ represents the accepted physical contribution, $W_{SI}$ a candidate substrate-to-information weighting, and $C_O$ a bounded observer-condition term.

These are working scaffolds. Every additional term must be operationalised and the complete probability model must be normalisable.

The ordinary limit is mandatory:

$$
P_{\mathrm{realized}}(E)
\approx
P_{\mathrm{phys}}(E)
$$

when additional terms are absent, constant, negligible, or empirically unnecessary within a declared regime and tolerance.

## 4. Constrained traversal

Represent a state structure as

$$
\mathcal G=(N,E_{\mathcal G}),
$$

with trajectory

$$
\gamma=(n_0\rightarrow n_1\rightarrow\cdots\rightarrow n_k).
$$

For one declared state space, a candidate traversal cost is

$$
C[\gamma]
=
\int_\gamma\lambda(x)\,ds.
$$

The path element, cost density, and resulting units must be defined.

A Gibbs-like path model requires a dimensionless exponent. With inverse cost scale $\beta$,

$$
P(B\mid A)
=
\frac{1}{Z_A}
\sum_{\gamma\in\Gamma(A\to B)}
\exp[-\beta C[\gamma]].
$$

Alternatively, use an explicitly dimensionless normalised cost $\widetilde C[\gamma]$ in $\exp[-\widetilde C[\gamma]]$.

This is a candidate model, not a declaration that all probability is fundamentally path density.

## 5. Time-dependent traversal geometry

Where admissibility changes with time, use

$$
\mathcal G(t)=(N,E_{\mathcal G}(t)).
$$

A temporally addressed path may be represented as

$$
\gamma_t=((n_0,t_0)\rightarrow(n_1,t_1)\rightarrow\cdots\rightarrow(n_k,t_k)),
$$

with

$$
C[\gamma_t]
=
\int_\gamma \lambda(x(s),t(s))\,ds.
$$

A candidate conditional weighting is then

$$
P(B,t_B\mid A,t_A)
=
\frac{1}{Z}
\sum_{\gamma_t\in\Gamma_{t_A\to t_B}(A\to B)}
\exp[-\beta C[\gamma_t]].
$$

The stationary model is recovered when the relevant transition structure and cost are effectively time-independent over the interval.

Time dependence adds scientific value only where it improves prospective prediction beyond ordinary time-dependent models rather than adding retrospective flexibility.

## 6. Independent-content criterion

A central scientific distinction is whether an I-layer description is merely a useful representation of the adequate P-layer state or carries independently measurable predictive content.

Let:

- $X_t$ = measured physical/environmental state;
- $H_t$ = relevant measured physical history;
- $I_t$ = candidate information-layer variable;
- $Y_{t+\Delta}$ = preregistered later physical outcome.

The physical-only null is schematically

$$
H_0:\quad
Y_{t+\Delta}
\perp\!\!\!\perp
I_t
\mid X_t,H_t.
$$

The stronger I-layer claim earns support only if $I_t$ improves held-out prediction after $X_t$ and $H_t$ are controlled, survives appropriate relation-preserving re-encoding, and cannot be reduced to an adequate physical-state function.

If

$$
I_t=f(X_t,H_t),
$$

then the I-layer may remain a useful effective description or compression, but this test has not established independent I→P dynamics.

The same reduction discipline applies to observer variables.

## 7. Ambiguity dynamics

For a declared domain $d$, let $\Omega_t^{(d)}$ be the unresolved feasible region compatible with current evidence and constraints. A dimensionless ambiguity-volume index is

$$
A_{t,\mathrm{vol}}^{(d)}
=
\log\!\left(1+\frac{\mu_d(\Omega_t^{(d)})}{\mu_{0,d}}\right).
$$

With normalised route connectivity $R_t$ and preserved access $X_t$,

$$
M_t=A_{t,\mathrm{vol}}^{(d)}R_tX_t.
$$

$M_t$ is a heuristic audit index, not a universal law. The product form must compete with additive and interaction alternatives.

Canonical owner: [`docs/21_AMBIGUITY_DYNAMICS_AND_MANOEUVRE_SPACE.md`](docs/21_AMBIGUITY_DYNAMICS_AND_MANOEUVRE_SPACE.md).

## 8. Cross-layer addressing

For candidate invariant $K$ at layer $L$,

$$
K_L=A_L(K;\theta_L).
$$

A cross-layer coupling must identify source and receiving spaces, variables, units or normalisation, observable consequence, ordinary baseline, and falsifier.

A typed coupling may be represented as

$$
C_{LM}:\mathcal X_L\rightarrow\mathcal X_M.
$$

Repeated algebraic form does not prove one physical mechanism.

The recursive integrity rule is:

> **No untyped inheritance.**

Provenance, evidence, licence, causation, authority, responsibility, units, and other properties do not automatically transfer merely because two objects are linked.

Canonical owners: Modules 22 and 22A.

## 9. Recursive constraint closure and reachable-state geometry

For adaptive systems whose relevant variables, admissible operations, decoder, or update rule may change, Module 32 uses addressed state-space families rather than assuming that every update occurs inside one fixed coordinate system.

Let

$$
\mathfrak X
=
\bigsqcup_{\alpha\in A}
\{\alpha\}\times\mathcal X_\alpha.
$$

A schematic adaptive update is

$$
\mathfrak F_t(\mathfrak A_t,u_t)
=
(\alpha_{t+1},x_{t+1})
\in\mathfrak X.
$$

When $\alpha_{t+1}\neq\alpha_t$, direct subtraction or state equivalence requires a lawful translation, embedding, quotient, or common observable. Construction-address change is not silently treated as motion inside one fixed space.

The recursive candidate is:

```text
previous organisation
→ consolidated typed constraints
→ changed admissibility
→ changed reachable states / capabilities
→ updated organisation
```

A scale-separated enabling-constraint pattern can occur when lower-scale feasible-state volume decreases while higher-scale viable capability increases:

$$
\Delta\mu_\ell<0,
\qquad
\Delta\nu_L>0,
$$

provided each before/after difference is defined in a common declared comparison space. This is not a universal monotonic law. Overconstraint can reduce both quantities, and constraint count is not a proxy for coherence, agency, or freedom.

Recurrent architecture across domains supports a stronger comparison only when the recurrent **constraint relation and function** survive typed equivalence tests. Shape alone is insufficient.

### 9.1 Relational brackets and compatible completion

Module 32S3 gives the local-to-global part of the same architecture an explicit compatibility object. A relational bracket records overlapping addressed domains, their local state spaces, restriction/translation maps, and typed compatibility tests.

For a missing or unobserved address `U_k`, the compatible completion set is schematically

$$
\Omega_{k,t}^{\mathrm{comp}}(a_{-k})
=
\left\{
x\in\mathcal F_t(U_k):
\chi_B(a_{-k}\cup\{x\})=1
\right\}.
$$

This separates three cases that must not be flattened: a narrowly constrained missing address, a broad ambiguous completion space, and an incompatible/disordered absence for which no tested completion satisfies the bracket.

The same supplement introduces a typed constraint-to-admissibility grammar

$$
\mathcal Q_{\lambda,t}(r,x,h)
=
\Omega_{\lambda,t}^{\mathrm{adm}},
$$

which can represent compatible completion, ordinary reachable-state restriction, and a candidate I→P admissibility test without asserting that all domains share one physical mechanism.

At the I→P boundary, the empirical question can be posed through a physical transition kernel

$$
K_P(dp_{t+\Delta}\mid p_t,H_t^P,i_t)
$$

and a preregistered relation deformation. A non-zero relational effect can remain fully P-realised. Independent I→P dynamics still require predictive or interventional content beyond the strongest adequate P-state/history model.

Stable local compatibility is not itself a scale transition. Promotion to an effective higher-scale object still requires the Module 32S persistence, intervention, new-capability, predictive-compression, and boundary-specificity tests.

Canonical owners: [`docs/32_RECURSIVE_CONSTRAINT_CLOSURE_AND_REACHABLE_STATE_GEOMETRY.md`](docs/32_RECURSIVE_CONSTRAINT_CLOSURE_AND_REACHABLE_STATE_GEOMETRY.md), [`docs/32S_LOAD_BEARING_RELATION_SETS_AND_SCALE_TRANSITION_TESTS.md`](docs/32S_LOAD_BEARING_RELATION_SETS_AND_SCALE_TRANSITION_TESTS.md), [`docs/32S1_INVARIANT_PERSISTENCE_RELATIONAL_ADDRESSABILITY_AND_SCALE_TRANSITION.md`](docs/32S1_INVARIANT_PERSISTENCE_RELATIONAL_ADDRESSABILITY_AND_SCALE_TRANSITION.md), [`docs/32S2_TEMPORAL_CONTINUITY_KERNELS_AND_MINIMUM_IDENTITY_HORIZON.md`](docs/32S2_TEMPORAL_CONTINUITY_KERNELS_AND_MINIMUM_IDENTITY_HORIZON.md), and [`docs/32S3_RELATIONAL_BRACKETS_COMPLETION_GEOMETRY_AND_I_TO_P_ADMISSIBILITY.md`](docs/32S3_RELATIONAL_BRACKETS_COMPLETION_GEOMETRY_AND_I_TO_P_ADMISSIBILITY.md).

## 10. LUCY

LUCY means **Local Unified Coherence Yield**.

Its canonical invariant is a thresholded addressed crossing:

```text
addressed relational state
→ coherence / closure threshold
→ consequential change at the next addressed layer
```

Current formal work uses a yield index $Y_L$ rather than overloading $C$:

$$
Y_L(x,t)
=
\chi_L
\frac{\lVert\nabla\tau_L(x,t)\rVert^2}
{N_L(x,t)+\varepsilon_L},
$$

with candidate threshold

$$
Y_L(x,t)\ge Y_*.
$$

Where a physical implementation produces boundary morphology:

```text
LUCY-1 = membrane-like boundary condition, when present
LUCY-2 = sustained local region, when present
```

These are conditional downstream morphologies, not automatic consequences of every LUCY crossing.

Canonical owners: Modules 08, 22, 27, and the physical specialisation in Module 30. Module 32 supplies a structural adaptive-constraint comparison, and Module 32S3 supplies a typed completion/admissibility test at the I→P boundary; neither establishes the I→P crossing or a physical LUCY mechanism.

## 11. Observer and procedural support modules

### OCQS

OCQS is a bounded observer-state hypothesis. It does not prove remote information, probability modulation, synchronicity, or substrate access. Its value depends on operational measures and comparison with established cognitive models.

### GRACE

GRACE—Geometry, Relation, Admissibility, Coherence, Emergence—is a traversal filter. It does not create a new layer or supply evidence by acronym.

### ESRT / ESF

ESRT/ESF test whether an artefact or representation contains reproducible **addressing, state, and flow** structure. A pass identifies an executable-system candidate, not a hidden meaning or historical use by assertion.

### Voynich

The Voynich branch is an applied procedural hypothesis. It must compete with linguistic, cipher, scribal, decorative, mnemonic, diagrammatic, and null models under blinded, quantitative, held-out tests. It is not evidence for foundational MKUFT physics.

## 12. Foundational physics — Layer Before Law

The foundational proposal asks whether quantum and gravitational effective behaviour may arise from a deeper typed update architecture rather than being fundamental objects at the same descriptive layer.

The proposed update remains a placeholder task:

$$
U_n
\xrightarrow{\operatorname{Update}_{\mathrm{SIPO}}}
U_{n+1}.
$$

Writing the operator does not supply the missing dynamics.

A developed mechanism must recover:

- Bell-compatible quantum correlations;
- no-signalling;
- the Born-rule and relevant quantum/QFT limits;
- general-relativistic or experimentally equivalent gravitational behaviour;
- dimensional and conservation requirements;
- at least one operational difference from strong alternatives.

If those burdens are not met, the branch remains an architectural reframing or interpretation rather than completed unification.

## 13. Experimental and promotion discipline

A broad interesting effect is not automatically an MKUFT result.

The public experimental route is:

```text
calibration
→ reconnaissance
→ locked discriminating signature
→ strongest fair null
→ deformation / ablation
→ held-out prediction
→ independent replication
→ bounded interpretation
```

A branch is reduced or removed when its variables cannot be operationalised, simpler models predict equally or better, the effect disappears under controls, results do not replicate, definitions move after failure, or evidence from another layer is used to rescue it.

Canonical owners: Modules 04, 05, 27, 28, and 29.

## 14. Metaphysical boundary

MKUFT contains a wider metaphysical interpretation in which God and Love may have explicit philosophical roles. Those roles are not inserted into physical equations as unmeasured variables and cannot rescue a failed empirical claim.

Scientific claims remain answerable to the variables, measurements, alternatives, and falsifiers of the domain in which they are made.

## 15. Public integrity boundary

The public canon must not contain non-public personal data, private correspondence, credentials, internal-only operating instructions, or uncleared personal case material.

Development-stage context should be translated into a public invariant or retired rather than published merely because it helped discovery.

## 16. One-page compression

```text
S–I–P–O:
Substrate → Information → Physical → Observer

Information notation:
I = layer
𝓘 = selected information state/function space
i ∈ 𝓘 = one information structure

Traversal:
𝒢 = (N,E_𝒢)
C[γ] = ∫ λ(x) ds
P(B|A) ∝ Σ exp[-βC[γ]]

Dynamic traversal:
𝒢(t) = (N,E_𝒢(t))
C[γ_t] = ∫ λ(x(s),t(s)) ds

Independent-content null:
Y_(t+Δ) ⟂ I_t | X_t,H_t

Ambiguity:
A_t,vol = log(1 + μ(Ω_t)/μ_0)
M_t = A_t,vol R_t X_t

Layer address:
K_L = A_L(K;θ_L)

Adaptive addressed space:
𝔛 = ⨆_α ({α} × 𝒳_α)
𝔉_t(𝔄_t,u_t) = (α_(t+1),x_(t+1)) ∈ 𝔛

Relational completion:
Ω_k,comp(a_-k) = {x ∈ 𝓕(U_k) : χ_B(a_-k ∪ {x}) = 1}

Constraint-to-admissibility:
𝒬_(λ,t)(r,x,h) = Ω_(λ,t)^adm

Enabling-constraint pair, when comparable:
Δμ_ℓ < 0 while Δν_L > 0

LUCY:
Y_L = χ_L ||∇τ_L||²/(N_L+ε_L)
Y_L ≥ Y_*

Integrity:
Define once. Type the address. Test the coupling. Recover the baseline. Keep the falsifier.
```

## 17. Final statement

MKUFT should not read as a pile of similarities.

It should read as one research architecture in which bold proposals remain bold **because their evidential status, ordinary limits, alternatives, and failure conditions remain visible**.