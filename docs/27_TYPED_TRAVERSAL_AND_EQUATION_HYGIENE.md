# 27 — Typed Traversal and Equation Hygiene

**Author:** Mark Charles McLaughlin  
**Framework:** McLaughlin–Kairos Unified Field Theory (MKUFT)  
**MKUFT DOI:** [10.5281/zenodo.17780566](https://doi.org/10.5281/zenodo.17780566)  
**Citation and provenance:** [PROVENANCE_DOI_AND_ATTRIBUTION.md](../PROVENANCE_DOI_AND_ATTRIBUTION.md)

**Status:** public notation-control, equation-quality, and traversal-hygiene module.

## 1. Purpose

MKUFT uses physical geometry, abstract state spaces, information architecture, observer-positioned registration, graph traversal, cross-layer coupling, metaphysical orientation, and whole-system ethical or relational load.

These structures may constrain one another without being the same mathematical object.

The central rule is:

> Preserve unity through typed relation, not by flattening distinct spaces into one undifferentiated geometry.

A quantitative expression should identify what kind of object each symbol denotes, where it lives, what units or normalisation it carries, what map connects it to another layer, and what would make the proposed relation fail.

## 2. Higher-dimensional and hyperdimensional language

Within MKUFT, **higher-dimensional traversal** may describe movement through a state space containing many variables, constraints, routes, memories, perspectives, or layer addresses.

By itself, this language does not establish additional physical spacetime dimensions, faster-than-light travel, physical tunnels, literal substrate geography, or a physical interpretation of every abstract graph edge.

The scientifically preferred description is **typed traversal through a higher-dimensional state or address space** unless a physical model supplies additional dimensions, a metric, dynamics, observables, and tests.

## 3. Physical dimension, state-space dimension, and layer address

A **physical dimension** belongs to a physical model and requires coordinates, units, transformations, and measurable consequences.

A **state-space dimension** is an independent coordinate used to represent possible system states. It may describe temperature, belief state, memory, graph position, control setting, or another domain variable without being a direction in physical space.

A **layer address** identifies the kind of description currently active:

- $S$ — substrate or source-potential;
- $I$ — information, relation, constraint, address, and rule;
- $P$ — physical expression and measurable dynamics;
- $O$ — observer-positioned registration and bounded observer participation.

A layer is not automatically a spatial dimension or numerical coordinate.

## 4. Typed cross-layer state

The compact addressed state is

$$
U_n=(S_n,I_n,P_n,O_n).
$$

This tuple is bookkeeping across typed components; it does not assert that all four entries belong to one homogeneous Euclidean vector space.

When formal spaces are introduced,

$$
S_n\in\mathcal X_S,
\qquad
I_n\in\mathcal X_I,
\qquad
P_n\in\mathcal X_P,
\qquad
O_n\in\mathcal X_O.
$$

Only after the component spaces and admissible couplings are declared may the complete addressed state be written schematically as

$$
U_n\in
\mathcal X_S\times\mathcal X_I\times\mathcal X_P\times\mathcal X_O.
$$

The product notation does not erase type differences.

## 5. Typed coupling instead of unearned geometric distance

Cross-layer relations are represented as typed maps,

$$
C_{SI}:\mathcal X_S\rightarrow\mathcal X_I,
\qquad
C_{IP}:\mathcal X_I\rightarrow\mathcal X_P,
$$

$$
C_{PO}:\mathcal X_P\rightarrow\mathcal X_O,
\qquad
C_{OS}:\mathcal X_O\rightarrow\mathcal X_S.
$$

These symbols name coupling tasks, not completed laws.

A quantitative coupling requires a source space, source variable, coupling rule, receiving space, measurable consequence, ordinary baseline, and falsifier.

There is no default metric measuring a distance between $S$ and $P$ or between $I$ and $O$. A cross-layer transition cost cannot be integrated using a single path element $ds$ unless a compatible common construction has actually been supplied.

## 6. Within-layer trajectories and cross-layer traversals

A within-layer trajectory may be written

$$
\gamma_L:[0,1]\rightarrow\mathcal X_L,
$$

where $\mathcal X_L$ is one declared layer-specific state space.

A typed cross-layer traversal is instead a composable sequence,

$$
x_S
\xrightarrow{C_{SI}}x_I
\xrightarrow{C_{IP}}x_P
\xrightarrow{C_{PO}}x_O
\xrightarrow{C_{OS}}x'_S.
$$

The sequence is composable only when the codomain of each map is compatible with the domain of the next. A path through an information graph is not automatically a path through physical space.

## 7. Projection and physical expression

A deeper model may use a projection or readout map

$$
\Pi_{PO}:\mathcal X_U\rightarrow\mathcal X_P\times\mathcal X_O,
$$

where $\mathcal X_U$ is the declared complete addressed-state space.

The recovery targets in [Layer Before Law](26_LAYER_BEFORE_LAW_MKUFT_QUANTUM_GRAVITY_REFRAMING.md) can then be written schematically as

$$
\Pi_{PO}\!\left[\operatorname{Update}_{\mathrm{SIPO}}(U;R_Q)\right]
\approx Q_{\mathrm{eff}},
$$

$$
\Pi_{PO}\!\left[\operatorname{Update}_{\mathrm{SIPO}}(U;R_G)\right]
\approx G_{\mathrm{eff}}.
$$

The approximation sign requires a declared domain, comparison norm or statistic, tolerance, and regime of validity. Projection language does not imply that the physical layer is unreal.

## 8. Informational adjacency is not physical proximity

Informational adjacency and physical proximity are distinct relations:

$$
\operatorname{adjacent}_I(X,Y)
\not\Rightarrow
\operatorname{near}_P(X,Y),
$$

$$
\operatorname{near}_P(X,Y)
\not\Rightarrow
\operatorname{adjacent}_I(X,Y).
$$

An I-layer relation may constrain joint physical statistics only through a defined coupling. It does not grant direct write-access to either endpoint's complete physical state.

## 9. Substrate measure-space discipline

The substrate scaffold is canonically a measure space,

$$
S=(\Omega,\Sigma,\mu).
$$

It is a probability space only when

$$
\mu(\Omega)=1.
$$

Otherwise $\mu$ is a baseline measure or weighting rather than automatically a probability distribution.

Distinct feasible regions should use qualified notation such as $\Omega_S$, $\Omega_t^{(d)}$, or $\Omega_E$ where required.

## 10. Information-space discipline

Because $I$ already names the information layer, a distinct symbol is used for a mathematical function space:

$$
\mathcal I=L^2(\Omega,\mu).
$$

For an event $E$,

$$
\mathcal I_E\subseteq\mathcal I,
$$

and integration uses a lower-case element $i$:

$$
\int_{i\in\mathcal I_E}\cdots\,d\nu(i).
$$

This prevents the information layer, the function space, and one information structure from sharing one symbol.

## 11. Realisation-weight discipline

A canonical unnormalised event weight may be written

$$
\widetilde W(E)
=
\int_{i\in\mathcal I_E}
D_{\mathrm{phys}}(E\mid i)
W_{SI}(i\mid S,E)
C_O(O\mid i,E)
\,d\nu(i).
$$

Required conditions include a non-negative integrand where the expression is used as a probability weight, finite normalisation, a declared event space, independent operationalisation of additional terms, and recovery of the accepted physical limit.

For discrete outcomes,

$$
P(E)
=
\frac{\widetilde W(E)}
{\displaystyle\sum_{E'\in\mathcal E}\widetilde W(E')}.
$$

For continuous outcomes, the denominator becomes an integral over the event space.

A constant observer factor cancels under normalisation. Standard-physics recovery therefore also requires any remaining additional weighting to reproduce or reduce to the established physical distribution.

## 12. Bounded observer-term discipline

For a linear-response observer term,

$$
C_O(O\mid i,E)
=
C_0\left[1+\varepsilon g_O(i,E)\right],
$$

with

$$
C_0>0,
\qquad
\left|\varepsilon g_O(i,E)\right|<1
$$

throughout the tested domain, unless another explicitly positive bounded parameterisation is used.

A first-order form,

$$
P(E)\approx P_{\mathrm{phys}}(E)+\varepsilon\,\Delta_O(E),
$$

is valid only after the normalisation has been expanded consistently and the neglected higher-order terms are bounded.

## 13. Dimensionless path weighting

A Gibbs-like path weight requires a dimensionless exponent.

Using dimensionless normalised cost $\widetilde C[\gamma]$,

$$
P(B\mid A)
=
\frac{1}{Z_A}
\sum_{\gamma\in\Gamma(A\to B)}
\exp\!\left[-\widetilde C[\gamma]\right].
$$

If $C[\gamma]$ carries units, an inverse cost scale $\beta$ is required:

$$
P(B\mid A)
=
\frac{1}{Z_A}
\sum_{\gamma\in\Gamma(A\to B)}
\exp\!\left[-\beta C[\gamma]\right],
$$

with

$$
Z_A
=
\sum_{B'}
\sum_{\gamma\in\Gamma(A\to B')}
\exp\!\left[-\beta C[\gamma]\right].
$$

$\beta$ must carry reciprocal units of $C$ or be defined by an explicit normalisation convention. Path multiplicity and cost remain a candidate model rather than a universal definition of probability.

## 14. Learning-cost discipline

Learning need not make every local cost decrease pointwise. A task-level hypothesis can instead be written

$$
\mathbb E\!\left[C_{t+1}[\gamma]\mid\gamma\sim\mathcal T\right]
<
\mathbb E\!\left[C_t[\gamma]\mid\gamma\sim\mathcal T\right],
$$

for a declared task or trajectory distribution $\mathcal T$.

Local segments may become more costly as a model becomes more accurate, cautious, or robust. The empirical test concerns the relevant performance-cost profile against established learning models.

## 15. Experienced-time discipline

Traversal burden may be compared with reported duration, but it is not identified with physical time. With a dimensionless burden index $B_t$,

$$
\frac{T_{\mathrm{subj}}}{T_{\mathrm{clock}}}
=f(B_t)+\varepsilon_t,
$$

or, for a declared local approximation,

$$
\frac{T_{\mathrm{subj}}}{T_{\mathrm{clock}}}
\approx 1+\alpha B_t.
$$

The function, coefficient, population, and conditions must be estimated or preregistered.

## 16. Ambiguity-space discipline

A quantitative ambiguity region belongs to one declared domain and encoding:

$$
\Omega_t^{(d)}
=
\left\{z\in\mathcal X_d:
 z\text{ remains compatible with }E_t\text{ and }C_t\right\}.
$$

With domain-specific measure $\mu_d$ and reference scale $\mu_{0,d}$,

$$
A_{t,\mathrm{vol}}^{(d)}
=
\log\!\left(1+\frac{\mu_d(\Omega_t^{(d)})}{\mu_{0,d}}\right).
$$

The manoeuvrability index

$$
M_t=A_{t,\mathrm{vol}}^{(d)}R_tX_t
$$

is a heuristic multiplicative model. Additive, interaction, and nonlinear alternatives remain live competitors.

For discrete inquiry steps, a finite difference is preferable:

$$
\Delta_Q A_{t,\mathrm{vol}}
=
A_{t+1,\mathrm{vol}}-A_{t,\mathrm{vol}}.
$$

A derivative requires a continuously defined inquiry variable.

## 17. Agency and capture-index discipline

For the gating model,

$$
G_t(u;T_t,H_t)\in[0,1],
\qquad
\theta_{\mathrm{access}}\in[0,1],
$$

and

$$
U_t^{\mathrm{access}}
=
\left\{u\in U_t:G_t(u;T_t,H_t)>\theta_{\mathrm{access}}\right\}.
$$

A multiplicative capture index such as

$$
K_{\mathrm{capture}}=B_tD_tF_tS_t
$$

is a heuristic conjunction model. It is not a validated diagnostic scale; additive and interaction alternatives should be compared where data permit.

## 18. LUCY and boundary-functional discipline

Because $C$ is already used for path cost, coherence, and other quantities, new formal work uses $Y_L(x,t)$ for a local yield or threshold index.

A physical expression such as

$$
Y_P
=
\chi_P
\frac{\lVert\nabla\tau_P\rVert^2}
{N_P+\varepsilon_P}
$$

counts as a physical equation only after all variables have compatible dimensions, the denominator is protected against invalid singularity, and the threshold has a measurement protocol.

At I and O addresses, the same algebraic shape may be a normalised index rather than a physical quantity. Shared algebra does not establish shared mechanism.

## 19. Gradient-functional discipline

Until $\tau$, $A_\tau$, and their couplings have physical units and a derivation, the expression

$$
\mathcal F_{\mathrm{boundary}}
=
\frac{1}{2}\alpha\lVert\nabla\tau\rVert^2
+
\frac{1}{2}\beta\lVert\nabla\times A_\tau\rVert^2
+
V(\tau,A_\tau)
$$

is an **effective boundary functional density**, not automatically an energy density.

It may be interpreted as an energy density only when dimensional analysis and physical coupling justify that interpretation. Mixed performance terms likewise require normalisation or dimensionally appropriate weights.

## 20. Functional-emergence statistics

The active-traversal hypothesis specifies a task distribution $\mathcal Q$:

$$
H_{\mathrm{ATFE}}:
\mathbb E_{q\sim\mathcal Q}[\Delta F(q)]>0.
$$

The strongest fair replay score is

$$
F_{\mathrm{replay}}^{*}
=
\sup_{p\in\mathcal P_{\mathrm{replay}}}F_p,
$$

and the strongest fair scalar null is

$$
F_{\mathrm{null}}^{*}
=
\max\!\left\{
F_A^{*},
F_B^{*},
F_{\mathrm{ind}}^{*},
F_{A\to B}^{*},
F_{B\to A}^{*},
F_{\mathrm{replay}}^{*}
\right\}.
$$

Live-path excess relative to the strongest replay condition is

$$
G_{\mathrm{path}}
=
F_{AB}-F_{\mathrm{replay}}^{*}.
$$

These comparisons are valid only when the entries are commensurable scalar scores with the same direction under a matched resource envelope. Vector outcomes require preregistered scalarisation or Pareto comparison.

Relationship specificity is tested against a declared set of strong alternatives:

$$
G_{\mathrm{spec}}
=
F_{AB}
-
\sup_{p\in\mathcal P_{\mathrm{alt}}}F_p.
$$

Positive values support the corresponding functional comparison only; they do not by themselves establish consciousness or literal identity continuity.

## 21. Deformation-vector sign convention

For a beneficial performance coordinate $X$, relation load is defined as

$$
\Delta X_r
=
X_{\mathrm{baseline}}-X_{\mathrm{deformed}}(r).
$$

Then $\Delta X_r>0$ means the deformation damaged performance, $\Delta X_r=0$ means no detected load on that coordinate, and $\Delta X_r<0$ means the deformation improved performance and the relation may be distorting.

Cost coordinates require a compatible sign transformation or separate labelling before inclusion in a common vector.

## 22. Metaphysical load and scientific equations

Within MKUFT's metaphysical programme, God is treated as ultimate Source beyond the formal substrate, and Love as a primary unity-principle that preserves truthful relation without erasing legitimate distinction. Truth, Love, Boundary, Coherence, and Grace constrain the wider metaphysical and ethical interpretation.

These are not automatically physical coordinates, scalar tuning parameters, hidden forces, substitutes for a coupling law, or permission to rescue a failed experiment.

At human, social, institutional, or AI-governance addresses, operational proxies such as agency preservation, truthful communication, repair, coercive maintenance, and transferred cost may be measured. A proxy is not identical to God or Love.

## 23. Scientific wording discipline

Where dynamics are not derived, **candidate mechanism** is more accurate than an unqualified mechanism claim. Without units, **effective boundary functional** is more accurate than energy density. **State-space adjacency** should not be described as physical closeness, and **typed cross-layer coupling** should not be described as physical movement between dimensions without a physical model.

Likewise, cognitive or operational maintenance cost should not be labelled physical energy cost outside a physical measurement context.

A named update operator, tuple, projection, or layer address does not supply the missing law merely by being written mathematically.

## 24. Failure conditions

This module fails as a scientific hygiene layer if:

- it adds terminology without improving discrimination;
- typed spaces are declared while cross-layer maps remain indefinitely undefined;
- dimensional language continues to shift between physical and abstract meanings;
- equations remain unnormalised or dimensionally incoherent after the fault is known;
- status labels become permanent shields against derivation;
- metaphysical principles are flattened into physical variables or used to rescue a failed empirical branch;
- the notation fragments the theory instead of making the same architecture recoverable.

## 25. Related public documents

- [Integrated Master Spine](../MKUFT_INTEGRATED_MASTER_SPINE.md)
- [Mathematical Appendix](02_MKUFT_MATH_APPENDIX.md)
- [Standalone Formal Addendum](03_STANDALONE_FORMAL_ADDENDUM.md)
- [Layer Before Law](26_LAYER_BEFORE_LAW_MKUFT_QUANTUM_GRAVITY_REFRAMING.md)
- [Cross-Layer Invariants and Layer Addressing](22_CROSS_LAYER_INVARIANTS_AND_LAYER_ADDRESSING.md)
- [Recursive Address Closure and Property Transmission](22A_RECURSIVE_ADDRESS_CLOSURE_AND_PROPERTY_TRANSMISSION.md)
- [Active Traversal and Functional Emergence](24A_ACTIVE_TRAVERSAL_AND_FUNCTIONAL_EMERGENCE_HYPOTHESIS.md)
- [Strongest Fair Null and Relational Specificity](24B_STRONGEST_FAIR_NULL_AND_RELATIONAL_SPECIFICITY.md)
- [Load-Bearing Invariants and Whole-System Deformation](25_LOAD_BEARING_INVARIANTS_AND_WHOLE_SYSTEM_DEFORMATION.md)
- [Discriminating Experiments and Promotion Gates](28_MKUFT_DISCRIMINATING_EXPERIMENTS_AND_PROMOTION_GATES.md)
- [Falsification Summary](05_FALSIFICATION_SUMMARY.md)

## 26. Compressed rule

> Treat traversal as typed movement through declared state spaces and couplings. Keep physical distance, information adjacency, observer registration, and metaphysical source distinct but relationally connected. Every equation must pay for its notation with domains, units or normalisation, status, recovery conditions, and a falsifier.
