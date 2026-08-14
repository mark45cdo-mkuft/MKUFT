# 31 — Context-Conditioned State Comparison and Observability

**Author:** Mark Charles McLaughlin  
**Framework:** McLaughlin–Kairos Unified Field Theory (MKUFT)  
**MKUFT DOI:** [10.5281/zenodo.17780566](https://doi.org/10.5281/zenodo.17780566)  
**Citation and provenance:** [PROVENANCE_DOI_AND_ATTRIBUTION.md](../PROVENANCE_DOI_AND_ATTRIBUTION.md)

**Status:** public structural and mathematical addendum.

## 1. Purpose

This module constrains four operations used across MKUFT: controlled deformation of an object, measurement-relative state resolution, comparison of relational structure across different implementations, and abstraction across different representations of a declared object.

Its core rule is:

> A valid comparison must preserve the declared comparison class, a measurement claim must respect the information available through the declared readout family, cross-implementation equivalence must preserve relevant dynamics as well as relational form, and an abstraction claim must state what survives lawful representation change.

This module adds no new S–I–P–O layer, force, field, ontology, or physical substrate claim.

## 2. Context-conditioned addressed state

Let

$$
\mathcal A_X(t)
=
\left(
S_X(t),I_X(t),P_X(t),O_X(t);\mathcal C_X(t)
\right),
$$

with context descriptor

$$
\mathcal C_X(t)
=
\left(
\mathcal E_t,\mathcal B_t,\mathcal H_t,\ell_t,\Xi_t
\right).
$$

Here $\mathcal E_t$ is the relevant environment, $\mathcal B_t$ the active boundary, $\mathcal H_t$ the relevant history or lineage, $\ell_t$ the active scale or resolution, and $\Xi_t$ the declared support or carrier conditions.

$\mathcal C_X$ is not a fifth layer. A context variable is retained only where changing it can alter the object class, admissible dynamics, or the load-bearing conclusion under test.

## 3. Admissible comparison class

Let $\mathcal M_X$ be the declared class within which two states may still be compared as instances or lawful continuations of the object under test.

A deformation $D$ is admissible for a same-class comparison only when

$$
D[\mathcal A_X]\in\mathcal M_X.
$$

Define

$$
\mathfrak D_X^{\mathrm{adm}}
=
\left\{D:D[\mathcal A_X]\in\mathcal M_X\right\}.
$$

If changing a relation, boundary, carrier, history term, or environmental condition moves the result outside $\mathcal M_X$, the operation has changed the comparison class rather than isolated one variable inside the same object.

The preferred test is therefore the smallest lawful deformation that changes the target relation while preserving the declared comparison class.

Context is not automatically constitutive. A variable may be incidental for one claim and constitutive for another.

### 3.1 Local admissible directions

Where $\mathcal M_X$ has a usable local geometric structure, an infinitesimal same-class perturbation $v$ should lie in the tangent cone

$$
v\in T_{\mathcal M_X}(\mathcal A_X).
$$

If $\mathcal M_X$ is smooth at the active address, this reduces to the ordinary tangent space condition.

A coordinate direction that points outside the tangent cone is not a lawful local same-class counterfactual, even if that coordinate can be set algebraically to another value.

This gives a local version of the comparison rule:

> algebraic freedom is not the same as admissible physical or structural freedom.

## 4. Measurement-relative observability

Let $x\in\mathcal X$ be a system state and let $\mathcal Q_O^{\mathrm{adm}}$ be the declared family of admissible measurements or probes associated with registration address $O$.

For each probe $q$, define

$$
\mathcal R_{O,q}:\mathcal X\rightarrow\mathcal Y_q.
$$

States are indistinguishable relative to that readout family when

$$
x\sim_O x'
\quad\Longleftrightarrow\quad
\mathcal R_{O,q}(x)=\mathcal R_{O,q}(x')
\quad
\forall q\in\mathcal Q_O^{\mathrm{adm}}.
$$

For stochastic or noisy readouts, exact equality should be replaced by equality or preregistered statistical indistinguishability of the corresponding output distributions under the declared measurement model.

The equivalence class is

$$
[x]_O
=
\{x'\in\mathcal X:x'\sim_O x\},
$$

and the resolved description belongs to the quotient

$$
\mathcal X/\!\sim_O.
$$

Define the quotient projection

$$
\pi_O:\mathcal X\rightarrow\mathcal X/\!\sim_O,
\qquad
\pi_O(x)=[x]_O.
$$

If $x\neq x'$ while $x\sim_O x'$, the distinction is unobservable relative to the declared model, boundary, and measurement family. This does not imply that every conceivable measurement system would share the same limitation.

## 5. Closure and resolution are distinct

Let $\mathsf C_L(x)=1$ denote satisfaction of a declared layer-specific closure or crossing condition.

It is consistent to have

$$
\mathsf C_L(x)=1
$$

while some $x'\neq x$ still satisfies

$$
x'\sim_O x.
$$

Therefore

$$
\text{layer-specific closure}
\not\Rightarrow
\text{complete measurement resolution}.
$$

The reverse implication also does not hold. A registration system may resolve a state without thereby establishing a stronger physical or relational closure claim.

For LUCY this means that a valid addressed crossing need not imply complete O-layer resolution.

## 6. Consequence-weighted ambiguity

Module 21 defines an unresolved feasible region $\Omega_t^{(d)}$ and ambiguity-volume index $A_{t,\mathrm{vol}}^{(d)}$. The size of the feasible region does not by itself show whether the remaining alternatives matter to a specific target.

Let

$$
F_Y:\Omega_t^{(d)}\rightarrow\mathcal Y
$$

map each admissible state to the predicted target quantity or outcome. Let $d_Y$ be a declared metric or non-negative symmetric discrepancy on $\mathcal Y$; a non-symmetric divergence should be symmetrised or otherwise explicitly handled before the quantity below is called a diameter.

Define the **consequence diameter**

$$
\Delta_Y(\Omega_t^{(d)})
=
\sup_{z,z'\in\Omega_t^{(d)}}
d_Y(F_Y(z),F_Y(z')).
$$

A useful ambiguity report is therefore the pair

$$
\mathfrak S_t^{(Y)}
=
\left(
A_{t,\mathrm{vol}}^{(d)},
\Delta_Y(\Omega_t^{(d)})
\right),
$$

rather than a single universal scalar.

For preregistered tolerance $\delta_Y$, target-relative closure is

$$
\Delta_Y(\Omega_t^{(d)})\leq\delta_Y.
$$

This permits a prediction, decision, or experimental question to close even when several underlying states remain unresolved.

> Close the declared target that has earned closure; do not promote that result into complete state resolution.

### 6.1 Target factorisation through the measurement quotient

Let

$$
\Omega=\Omega_t^{(d)}\subseteq\mathcal X
$$

be the feasible region on which $F_Y$ is defined, and restrict the quotient projection to

$$
\pi_O^{\Omega}
=
\pi_O\!\mid_{\Omega}:
\Omega\rightarrow\pi_O(\Omega).
$$

The target is exactly recoverable from the $O$-resolved state on $\Omega$ when there exists a map

$$
\overline F_Y:\pi_O(\Omega)\rightarrow\mathcal Y
$$

such that

$$
F_Y
=
\overline F_Y\circ\pi_O^{\Omega}.
$$

Equivalently, for states inside the feasible region,

$$
x,x'\in\Omega,
\quad
x\sim_O x'
\quad\Longrightarrow\quad
F_Y(x)=F_Y(x').
$$

If this condition holds, distinctions hidden inside one measurement-equivalence class are irrelevant to that target on the tested region.

For approximate recovery, define the within-class target diameter

$$
\Delta_Y([x]_O\cap\Omega)
=
\sup_{z,z'\in[x]_O\cap\Omega}
d_Y(F_Y(z),F_Y(z')).
$$

Then $O$ resolves target $Y$ to tolerance $\delta_Y$ on the tested region when

$$
\Delta_Y([x]_O\cap\Omega)
\leq\delta_Y
$$

for every measurement-equivalence class intersecting $\Omega$.

If the target does not factor through the restricted quotient, the declared readout family is insufficient by itself to determine that target without additional information or assumptions.

This connects observability and ambiguity directly: unresolved state distinctions become consequential only relative to the target they separate.

## 7. Context-conditioned LUCY

The canonical LUCY definition remains the addressed threshold at which a relation becomes consequential at the next layer.

Where context is load-bearing, a yield index may be written schematically as

$$
Y_L(x,t;\mathcal C_X)
$$

with threshold

$$
Y_L(x,t;\mathcal C_X)\geq Y_*.
$$

The context argument records that a relational pattern need not have the same consequence under a different boundary, scale, support regime, history, or physical implementation.

A LUCY crossing does not require a visible membrane, complete measurement resolution, or identical behaviour from every formally similar relation in another implementation.

## 8. Relational coordinates carried by physical geometry

A P-layer coordinate may participate in an I-layer relation without the two layers becoming identical.

For physical separation $d$ and wavelength $\lambda$,

$$
\rho=\frac{d}{\lambda}
$$

is a dimensionless relational coordinate. A phase relation may use

$$
\varphi=\mathbf k\cdot\mathbf r.
$$

The physical distance, wavelength, field, material, and geometry remain P-layer quantities. The ratio or phase relation may be used as an I-layer descriptor.

Preserving the ratio or phase under scaling does not establish transfer of the full phenomenon. Support and dynamics must also be compatible.

## 9. Cross-implementation relational equivalence

Let systems $A$ and $B$ have state spaces $\mathcal X_A$ and $\mathcal X_B$, dynamics $F_A$ and $F_B$, and invariant maps into a common comparison space $\mathcal K$:

$$
K_A:\mathcal X_A\rightarrow\mathcal K,
\qquad
K_B:\mathcal X_B\rightarrow\mathcal K.
$$

For proposed mapping

$$
\Phi:\mathcal X_A\rightarrow\mathcal X_B,
$$

relational preservation requires

$$
d_K\!\left(K_B(\Phi x),K_A(x)\right)
\leq\varepsilon_K.
$$

A stronger functional comparison also requires approximate dynamical compatibility:

$$
d_B\!\left(
F_B(\Phi x),
\Phi(F_A(x))
\right)
\leq\varepsilon_F.
$$

For stochastic systems, transition kernels or predictive distributions replace deterministic update maps.

The target state $\Phi x$ must also satisfy the support conditions of the target comparison class.

Therefore same graph form, ratio, symmetry, or verbal pattern is insufficient by itself. A cross-implementation equivalence claim must preserve the relevant relation and the lawful work that relation performs.

## 10. Scale-level functional objects

Let

$$
\Pi:\mathcal X\rightarrow\mathcal Z,
\qquad
Z_t=\Pi(X_t)
$$

define a candidate macrostate from lower-level state $X_t$.

One candidate criterion for approximate predictive closure is

$$
I\!\left(
Z_{t+1};X_{\leq t}\mid Z_t
\right)
\leq\varepsilon,
$$

where the conditional mutual information is used only when the relevant distributions can be specified or estimated.

The criterion asks whether the macrostate contains nearly all lower-level history needed to predict the next macrostate under the tested regime.

Predictive closure alone does not establish intelligence, consciousness, personhood, a new force, or fundamental ontology. A stronger scale-level functional-object claim additionally requires held-out prediction, lawful perturbation, support persistence, and reproducible deformation when load-bearing macro relations are changed under fair controls.

## 11. Addressed abstraction and representation invariance

### 11.1 Operational access rule

A declared mathematical or scientific object does not enter an analysis without some representation, encoding, coordinate system, syntax, diagram, measurement interface, or other address through which operations can be performed on it.

This is a methodological claim about access, not a proof that observer-independent mathematical objects do or do not exist.

Let $\alpha$ denote a **construction address** containing the choices that are load-bearing for the active model, schematically

$$
\alpha
=
\left(
\mathcal V_\alpha,
\sim_\alpha,
\mathcal B_\alpha,
\mathcal T_\alpha,
\mathcal Q_\alpha
\right),
$$

where $\mathcal V_\alpha$ denotes the selected primitives or variables, $\sim_\alpha$ the declared equivalence rule, $\mathcal B_\alpha$ the model boundary or scope, $\mathcal T_\alpha$ the admissible transformations, and $\mathcal Q_\alpha$ the available questions, observables, or formal operations.

These entries are retained only where changing them can alter a conclusion. A psychological belief, philosophical preference, or author identity is not inserted into the mathematics merely because it may have influenced model construction.

> No model is operationally address-free. The scientific question is which conclusions survive lawful changes of construction address.

### 11.2 Representation family

Let

$$
\{\mathcal X_\alpha\}_{\alpha\in A}
$$

be a declared family of representations intended to encode the same comparison object or structural target under different construction addresses.

For an admissible pair of addresses, let

$$
T_{\alpha\beta}:\mathcal D_{\alpha\beta}\subseteq\mathcal X_\alpha
\rightarrow\mathcal X_\beta
$$

be a translation, re-encoding, coordinate change, or other lawful representation map on the domain where the comparison is defined.

A candidate abstract invariant is represented at each address by

$$
K_\alpha:\mathcal X_\alpha\rightarrow\mathcal K,
$$

where $\mathcal K$ is a declared comparison space.

Representation stability requires

$$
d_K\!\left(
K_\beta(T_{\alpha\beta}x),
K_\alpha(x)
\right)
\leq\varepsilon_K
$$

for the preregistered admissible translations and states under test.

Exact invariance is the special case $\varepsilon_K=0$.

This gives the operational rule:

> Abstraction is not absence of address. It is the preservation of declared structure across admissible changes of address.

### 11.3 Representation-dependence test

Let $\mathcal P_{\mathrm{adm}}$ be the declared set of admissible triples $(\alpha,\beta,x)$ for which the translation and comparison are defined. A representation-dependence diameter may be written

$$
D_K^{\mathrm{rep}}
=
\sup_{(\alpha,\beta,x)\in\mathcal P_{\mathrm{adm}}}
 d_K\!\left(
K_\beta(T_{\alpha\beta}x),
K_\alpha(x)
\right).
$$

$D_K^{\mathrm{rep}}$ is not a universal truth score. It measures sensitivity of the declared invariant to the tested representation family.

Small $D_K^{\mathrm{rep}}$ across a strong and varied address family supports representation-robust structure. Large $D_K^{\mathrm{rep}}$ may indicate that the supposed invariant depends materially on the chosen partition, encoding, coordinate system, equivalence rule, boundary, or operation set.

The test is only meaningful when the translations preserve the intended target. A failed comparison caused by changing the subject is not evidence that the original structure was merely observer-created.

### 11.4 Construction-address robustness of conclusions

Let $G_\alpha(x)$ be a prediction, theorem-level consequence, classification, or model conclusion expressed at construction address $\alpha$.

A cross-address robustness test has the same form:

$$
d_G\!\left(
G_\beta(T_{\alpha\beta}x),
G_\alpha(x)
\right)
\leq\varepsilon_G.
$$

Where this fails under a lawful translation, the analysis should identify which load-bearing construction choice carries the difference before attributing the disagreement to reality, observer effects, or a new mechanism.

This provides a disciplined way to investigate how much of a model conclusion belongs to the selected representation rather than assuming the first formal partition was neutral.

It does not prove that the surviving structure is ontologically fundamental. It shows only that the conclusion is less dependent on the tested construction addresses.

## 12. Established neighbouring concepts and novelty boundary

Observability, state equivalence, quotient representations, quotient factorisation, tangent cones, coordinate and gauge invariance, representation invariance, naturality, dimensionless similarity, sufficient statistics, coarse-graining, Markov lumpability, and dynamical conjugacy or approximate conjugacy are established mathematical and systems concepts.

The proposed MKUFT contribution is not ownership of those tools. It is their typed conjunction with S–I–P–O addressing, recursive address closure, ambiguity dynamics, LUCY, cross-layer carrier discipline, and explicit construction-address testing.

Analogies involving holography, resonant systems, computation, biology, or other organised systems may suggest candidate relational structures. They do not identify the literal MKUFT substrate or establish a shared mechanism across domains.

## 13. Failure modes and reduction rules

The module is weakened if comparison classes cannot be defined before testing, context variables are added only after failure, measurement equivalence has no declared probe family, consequence diameter adds no useful discrimination, cross-implementation dynamics cannot be compared where equivalence is claimed, construction-address families are chosen only after seeing the desired result, or the framework uses context or representation language to make a claim immune to falsification.

Reduction rules:

- if a target variable can be changed within one ordinary comparison class, use the simpler ordinary counterfactual;
- if context variables are incidental to the active claim, omit them;
- if indistinguishable states never differ in accessible consequences, retain the quotient description rather than multiplying ontology;
- if two representations differ only cosmetically, do not count their agreement as strong evidence of abstraction;
- if an address translation changes the target meaning or comparison class, do not treat disagreement as representation dependence;
- if a standard domain model already captures the required support, observability, invariance, and coarse-graining without loss, use that model and treat MKUFT terminology as an address map only.

## 14. Relationship to existing canon

This module composes rather than replaces existing owners:

- [21 — Ambiguity Dynamics](21_AMBIGUITY_DYNAMICS_AND_MANOEUVRE_SPACE.md);
- [22 — Cross-Layer Invariants](22_CROSS_LAYER_INVARIANTS_AND_LAYER_ADDRESSING.md);
- [22A — Recursive Address Closure](22A_RECURSIVE_ADDRESS_CLOSURE_AND_PROPERTY_TRANSMISSION.md);
- [24A — Active Traversal](24A_ACTIVE_TRAVERSAL_AND_FUNCTIONAL_EMERGENCE_HYPOTHESIS.md);
- [25A — Fundamental Traversal Coherence Nodes](25A_FUNDAMENTAL_TRAVERSAL_COHERENCE_NODES.md);
- [27 — Typed Traversal and Equation Hygiene](27_TYPED_TRAVERSAL_AND_EQUATION_HYGIENE.md);
- [08 — LUCY](08_LUCY_BOUNDARY_THRESHOLD_FRAMEWORK.md);
- [30 — LUCY Threshold Geometry](30_LUCY_THRESHOLD_GEOMETRY_AND_RELATIONAL_CLOSURE.md).

The present owner is limited to context-conditioned comparison, admissible deformation, measurement-relative state equivalence, target-relative ambiguity closure, support-preserving cross-implementation comparison, and representation-invariance tests across declared construction addresses.

## 15. Compressed rule

> Preserve the comparison class before perturbing it. Preserve support before transferring a relation. Distinguish measurement resolution from system closure. Close only the target that has earned closure. Every operational model is addressed; abstraction earns strength by surviving lawful changes of address.
