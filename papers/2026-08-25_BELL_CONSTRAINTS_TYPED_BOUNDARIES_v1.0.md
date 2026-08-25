# Bell Constraints as Typed Boundaries: Relation, Access, Completion, and Scale

**Author:** Mark Charles McLaughlin  
**Affiliation:** Independent Researcher, United Kingdom  
**ORCID:** [0009-0005-7736-1511](https://orcid.org/0009-0005-7736-1511)  
**Framework of origin:** McLaughlin–Kairos Unified Field Theory (MKUFT)  
**Publication date:** 25 August 2026  
**Version:** 1.0  
**Document type:** scientific preprint; Bell/CHSH typed-boundary and correspondence analysis  
**Version DOI:** [10.5281/zenodo.22100926](https://doi.org/10.5281/zenodo.22100926)  
**Concept DOI:** [10.5281/zenodo.22100925](https://doi.org/10.5281/zenodo.22100925)  
**Licence of the exact deposited publication:** Creative Commons Attribution 4.0 International (CC BY 4.0)

> **Publication boundary.** This is the GitHub human-reading and discovery route for the frozen v1.0 publication. The exact 12-page Zenodo PDF identified by DOI `10.5281/zenodo.22100926` controls the frozen publication identity, pagination, visual layout, and deposited equations. This route preserves the scientific object in renderer-safe Markdown without silently revising the deposited paper.

## Read and verify the published paper

- **[Exact Zenodo v1.0 publication](https://doi.org/10.5281/zenodo.22100926)**
- [Standalone publication record](../BELL_CONSTRAINTS_STANDALONE_PUBLICATION.md)
- [Frozen DOI PDF mirror](../publications/BELL_CONSTRAINTS_TYPED_BOUNDARIES_v1.0_DOI_10.5281_zenodo.22100926.pdf)
- [Frozen identity/checksum record](../publications/BELL_CONSTRAINTS_TYPED_BOUNDARIES_v1.0/)
- [Papers and Publications index](README.md)

## Abstract

Bell's theorem rules out a broad class of local hidden-variable explanations, but Bell violation, operational no-signalling, process-level locality, quantum admissibility, completion geometry, and the numerical quantum boundary are distinct statements. This paper applies a typed-boundary analysis to the Bell/CHSH setting and keeps those objects at separate scientific addresses.

The paper does **not** derive a new Bell inequality, does **not** derive Tsirelson's bound from a new physical principle, and does **not** claim that Bell's theorem has been solved. Its non-null result is methodological: factorisation, operational access, remote write-power, process-level conditional closure, local admissibility-law ownership, parent-level completion, and scale/resource custody are separated and tested against established native results. The analysis also distinguishes a target-specific CHSH residual from quantum-bound slack, finite-address excess, numerical certification gap, and experimental uncertainty. Under the comparator family examined in v1.0, the independent Bell-local new-physics delta is **null**; the typed correspondence and falsification architecture remains non-null.

## 1. Introduction and claim boundary

A Bell-local hidden-variable factorisation can fail while operational no-signalling remains intact. Operational no-signalling can hold while stronger history-conditioned process conditions fail. Quantum theory respects no-signalling while occupying only a strict subset of the no-signalling correlation set. Within the quantum set, compatibility structure, completion geometry, resource restrictions, and certification add further distinct boundaries.

The purpose here is not to rename those native results. It is to keep their logical ownership explicit so that one level cannot silently substitute for another. Agreement with established Bell, information-theoretic, compatibility, uncertainty, or dimension-witness results is treated as **correspondence, not novelty**.

## 2. Native Bell object

For separated parties with settings $x,y$, outcomes $a,b$, and hidden variable $\lambda$, Bell-local factorisation is

```math
p(a,b\mid x,y,\lambda)=p(a\mid x,\lambda)\,p(b\mid y,\lambda).
```

For binary $\pm1$ outcomes, define

```math
S=E_{00}+E_{01}+E_{10}-E_{11}.
```

Bell-local models satisfy

```math
|S|\le 2,
```

quantum theory permits

```math
|S|\le 2\sqrt{2},
```

and the algebraic maximum is

```math
|S|\le 4.
```

Operational no-signalling for Alice requires

```math
\sum_b p(a,b\mid x,y)=p(a\mid x),
```

independently of $y$, and analogously for Bob. Popescu-Rohrlich-type boxes supply the decisive null to any inference from no-signalling alone to the quantum boundary:

```math
\text{no-signalling}\not\Rightarrow\text{quantum boundary}.
```

Fine's theorem supplies the classical completion owner at the CHSH correlation-experiment scope: the relevant Bell inequalities, factorizable stochastic hidden-variable models, and compatible global joint distributions are mutually linked. This is a classical completion statement, not quantum completion geometry.

## 3. Typed boundary decomposition

The central typed distinction is

> **relation ≠ operational access ≠ remote write-power ≠ process closure ≠ local admissibility ownership ≠ parent completion.**

A stronger local process statement may be imposed on a declared history/state variable $h_A(t)$:

```math
p(a_t\mid x_t,y_t,h_A(t))=p(a_t\mid x_t,h_A(t)).
```

Under declared lawful marginalisation assumptions, including that the local-history distribution does not itself import remote-setting dependence, this stronger conditional closure can imply operational no-signalling after the local history is marginalised. The converse is not established. Conditional dependence can cancel under marginalisation.

A simple abstract counterexample makes the point: let a binary local-history variable be uniform and independent of the remote setting; for one remote setting Alice's output equals that history variable, while for the other it is the binary complement. Alice's observed marginal remains uniform for either remote setting even though the outcome conditioned on the local history depends maximally on the remote choice. Therefore ordinary no-signalling does not establish the stronger conditioned process relation.

At a separate address, Carmi-Cohen relativistic independence constrains remote choice from changing locally owned uncertainty relations. That native result is closer to a no-remote-write condition on local admissibility geometry than to marginal no-signalling, and therefore limits novelty claims based only on that rephrasing.

## 4. Completion geometry and the bounded CHSH residual

### Classical parity obstruction

Predetermined $\pm1$ values cannot satisfy all four algebraically perfect CHSH target relations simultaneously because

```math
(A_0B_0)(A_0B_1)(A_1B_0)(A_1B_1)=A_0^2A_1^2B_0^2B_1^2=+1,
```

whereas the target sign pattern $(+,+,+,-)$ multiplies to $-1$. This is a compact classical obstruction, not a derivation of the quantum bound.

### Tsirelson correlator geometry

At the bipartite binary correlator/XOR-game scope, Tsirelson's representation allows

```math
E_{xy}=u_x\cdot v_y
```

for real unit vectors. Then

```math
\begin{aligned}
|S|&=\left|u_0\cdot(v_0+v_1)+u_1\cdot(v_0-v_1)\right|\\
&\le \left\|v_0+v_1\right\|+\left\|v_0-v_1\right\|\\
&\le 2\sqrt{2},
\end{aligned}
```

using

```math
\left\|v_0+v_1\right\|^2+\left\|v_0-v_1\right\|^2=4.
```

This representation is scoped to the correlator/XOR object and is not a parametrisation of arbitrary full behaviours including all marginals.

For the $2\times2$ dichotomic correlator tuple, one representative Tsirelson-Landau-Masanes cycle inequality is

```math
\left|\arcsin E_{00}+\arcsin E_{01}+\arcsin E_{10}-\arcsin E_{11}\right|\le \pi.
```

On the isotropic specialization this gives

```math
4\arcsin(t)\le \pi,
```

hence

```math
t\le \frac{1}{\sqrt{2}}
```

and therefore

```math
|S|\le 2\sqrt{2}.
```

That boundary is established quantum correlator geometry. A typed cycle-completion description is correspondence unless an independent carrier law derives the transform and budget without importing the known answer.

### Target-specific CHSH residual

For the CHSH game, the optimal quantum winning probability is

```math
P_{\mathrm{win},Q}=\frac{2+\sqrt{2}}{4}=\cos^2\!\left(\frac{\pi}{8}\right).
```

Relative to perfect algebraic winning probability, define

```math
\rho_Q=1-P_{\mathrm{win},Q}=\frac{2-\sqrt{2}}{4}\approx 0.146447.
```

In CHSH-score units, the algebraic-to-quantum deficit is $4-2\sqrt2$. This is not the same object as quantum-bound slack

```math
2\sqrt{2}-S,
```

which vanishes at a quantum optimum. Neither quantity is a new substance, universal imperfection constant, or causal explanation. The first is distance from a declared algebraic target within the quantum admissibility category; the second is distance from the quantum CHSH optimum.

## 5. Native-owner correspondence map

The typed analysis is useful only if native ownership remains explicit:

- **Bell/Fine:** Bell-local factorisation and compatible classical global-joint completion.
- **Operational no-signalling:** no remote-setting dependence in observed local marginals; not a characterization of the quantum set.
- **Conditioned process closure:** a stronger augmented-state condition; one-way implication to observed no-signalling only under declared marginalisation assumptions.
- **Relativistic independence:** Carmi-Cohen no-remote-write constraint on local uncertainty structure at the scope they analyse.
- **TLM/elliptope geometry:** exact $2\times2$ dichotomic correlator boundary.
- **Joint measurability/incompatibility:** Wolf, Pérez-García and Fernández at their earned measurement scope.
- **Information Causality:** recursive information-amplification constraint on the standard isotropic CHSH/random-access-code line; not a full characterization of the quantum set.
- **NPA hierarchy:** positive/consistency completion with infinite-level convergence to the commuting-operator correlation set, not generally the closure of finite-dimensional tensor-product correlations.
- **Specker/Gonda:** compatibility/extendability constraints strong enough to exclude almost-quantum correlations under the full principle.
- **Uncertainty and steering:** Oppenheim-Wehner native owner linking nonlocal strength to uncertainty plus steering.
- **Stochastic-process neighbour:** Barandes, Hasan and Kagan (2026) obtain Tsirelson's bound within their stochastic-quantum/causal-locality representation; this supplies comparator pressure, not novelty credit to the typed map.

The result is a **local null on new Bell mathematics**. The surviving value is that different constraints remain at the correct address and cannot be substituted for one another without argument.

## 6. Scale, address and capacity custody

At least two scale axes must be separated. **Scenario scale** specifies the Bell experiment itself: parties, settings, outcomes, scoring functional, interventions/resources, and relevant assumptions. **Internal resource scale** specifies a capacity inside a fixed scenario and admissibility category.

Changing CHSH to I3322 is a scenario change $S\to S'$, not by itself an internal-capacity refinement. Conversely, changing a genuine internal resource, such as permitted local dimension, inside a fixed I3322 scenario can be a capacity question. Known I3322 dimension behaviour is calibration here, not prospective evidence.

For a genuine nested feasible-set refinement at fixed category, scenario, and functional,

```math
\sup_{x\in X_C(A')}F(x)\ge \sup_{x\in X_C(A)}F(x).
```

This elementary monotonicity does not imply that larger state spaces are physically better or that a changed scenario inherits the result. Ambient Hilbert-space dimension is also not the same as irreducibly used dimension; a lower-dimensional strategy can be embedded into a larger space. Dimension-witness and irreducible-dimension results remain the native owners of strict resource claims.

To keep residuals typed, fix scenario $S$, admissibility category $C$, target $R$, loss rule $L$, and internal address $A$:

```math
r_C(R\mid A,S)=\inf\left\{L(R,x):x\text{ is }C\text{-admissible and realisable at }A\text{ in fixed }S\right\}.
```

Define the category floor

```math
r_C^{*}(R\mid S)=\inf_A r_C(R\mid A,S),
```

and finite-address excess

```math
\Delta_C(R\mid A,S)=r_C(R\mid A,S)-r_C^{*}(R\mid S)\ge 0.
```

A nonzero category-floor residual is not evidence that more finite capacity will remove it. Certification/search error and experimental uncertainty remain separate objects. A refinement inherits monotonicity only if the coordinates on which the result depends are preserved; changes to medium/environment, boundary, transition/selection structure, history, weighting, scenario, or resource contract readdress the claim and require recomputation.

## 7. Strongest fair nulls, falsifiers, and reopening gate

The strongest fair nulls are serious alternatives capable of carrying the observation and changing the target conclusion:

1. **Standard quantum geometry:** if the typed analysis only redescribes TLM/elliptope/Tsirelson geometry, Bell-physics novelty is null.
2. **Established physical principles:** if a no-remote-write rule reduces to relativistic independence, uncertainty/steering, Information Causality, joint measurability, Specker-type compatibility, or another native principle at the relevant address, native ownership remains there.
3. **Completion machinery by renaming:** inserting positivity, Hilbert-space structure, target-fitted transforms, NPA-equivalent conditions, or the Tsirelson value by hand is not an independent derivation.
4. **Scale misattribution:** a changed scenario, larger ambient dimension, or better numerical candidate does not by itself establish an internal-capacity obstruction.
5. **Residual misattribution:** a persistent residual can belong to the admissibility category rather than finite capacity; numerical or experimental residuals can instead be certification or measurement effects.

A Bell-local reconstruction claim reopens only on a parent-changing separator. The candidate rule must be procedurally frozen without Bell-specific target-carrying machinery before the target/comparator lookup. A genuinely held-out same-domain Bell scenario is admissible under that custody rule; cross-domain transfer is stronger evidence for carrier-independence but is not logically required. If the target was already available before the test was frozen, the result is calibration rather than prospective evidence.

## 8. Discussion and conclusion

The Bell/CHSH setting contains several boundaries often compressed into one semantic object:

- Bell-local factorisation failure → no classical local completion of the tested form;
- operational no-signalling → no controllable remote write into observed local marginals;
- conditioned process closure → stronger augmented-state local independence;
- relativistic independence / uncertainty structure → local admissibility-law constraints;
- TLM/elliptope geometry → the joint correlator boundary;
- information, compatibility, and positive-completion principles → additional constraints at their earned scopes;
- resource and dimension witnesses → certified capacity statements inside fixed scenarios.

The paper therefore does not produce a new Bell theorem or a new derivation of $2\sqrt2$. Under the comparator family examined in v1.0, the independent Bell-local new-physics delta is null. The non-null contribution is the typed correspondence, custody, and falsification architecture, together with a disciplined route for prospective generalisation.

The appropriate closure state is: **close the present Bell-local reconstruction claim, preserve its falsifiers, and reopen only when a new controlled test can change the result.**

## Relationship to the live MKUFT canon

This is a **typed correspondence and falsification paper**, not a new Bell-law module. The closest live MKUFT owners are:

- [Module 24B — Strongest Fair Null and Relational Specificity](../docs/24B_STRONGEST_FAIR_NULL_AND_RELATIONAL_SPECIFICITY.md)
- [Module 27 — Typed Traversal and Equation Hygiene](../docs/27_TYPED_TRAVERSAL_AND_EQUATION_HYGIENE.md)
- [Module 29 — Scientific Tightening and Claim Discipline](../docs/29_MKUFT_SCIENTIFIC_TIGHTENING_AND_CLAIM_DISCIPLINE.md)
- [Module 32S3 — Relational Brackets, Completion Geometry, and I→P Admissibility](../docs/32S3_RELATIONAL_BRACKETS_COMPLETION_GEOMETRY_AND_I_TO_P_ADMISSIBILITY.md)

These live modules remain evolving objects. They do not become part of the frozen v1.0 deposit, and the Bell paper does not promote their wider physical hypotheses merely because the typed architecture maps established Bell constraints cleanly.

## Frozen-object verification

- **Pages:** 12
- **Size:** 251,625 bytes
- **MD5:** `efa1c01cbb40a621880f5aa5e2cb21d6`
- **SHA-256:** `bc8f99f71adc4f1cbc36436fb29fe49f2f9682c36b6ca43f3e42a5382756e0fa`
- **Version DOI:** `10.5281/zenodo.22100926`
- **Concept DOI:** `10.5281/zenodo.22100925`

## Licence

Copyright © 2026 Mark Charles McLaughlin.

The exact Bell Constraints v1.0 publication identified by DOI [10.5281/zenodo.22100926](https://doi.org/10.5281/zenodo.22100926) is licensed under **Creative Commons Attribution 4.0 International (CC BY 4.0)** according to the deposited Zenodo record. The licence of that exact publication does not silently relicense separate live MKUFT modules, later GitHub revisions, private working material, software, or other objects outside the deposit.

## References

Bell, J. S. (1964). *On the Einstein Podolsky Rosen paradox*. Physics 1, 195–200.

Clauser, J. F., Horne, M. A., Shimony, A., & Holt, R. A. (1969). Proposed experiment to test local hidden-variable theories. *Physical Review Letters* 23, 880–884. DOI: 10.1103/PhysRevLett.23.880.

Fine, A. (1982). Hidden Variables, Joint Probability, and the Bell Inequalities. *Physical Review Letters* 48, 291–295. DOI: 10.1103/PhysRevLett.48.291.

Tsirelson, B. S. (1980). Quantum generalizations of Bell's inequality. *Letters in Mathematical Physics* 4, 93–100.

Landau, L. J. (1988). Empirical two-point correlation functions. *Foundations of Physics* 18(4), 449–460. DOI: 10.1007/BF00732549.

Popescu, S., & Rohrlich, D. (1994). Quantum nonlocality as an axiom. *Foundations of Physics* 24(3), 379–385. DOI: 10.1007/BF02058098.

Masanes, Ll. (2003). Necessary and sufficient condition for quantum-generated correlations. arXiv:quant-ph/0309137.

Navascués, M., Pironio, S., & Acín, A. (2008). A convergent hierarchy of semidefinite programs characterizing the set of quantum correlations. *New Journal of Physics* 10, 073013. DOI: 10.1088/1367-2630/10/7/073013.

Pawłowski, M., Paterek, T., Kaszlikowski, D., Scarani, V., Winter, A., & Żukowski, M. (2009). Information causality as a physical principle. *Nature* 461, 1101–1104. DOI: 10.1038/nature08400.

Wolf, M. M., Pérez-García, D., & Fernández, C. (2009). Measurements Incompatible in Quantum Theory Cannot Be Measured Jointly in Any Other No-Signaling Theory. *Physical Review Letters* 103, 230402. DOI: 10.1103/PhysRevLett.103.230402.

Oppenheim, J., & Wehner, S. (2010). The uncertainty principle determines the non-locality of quantum mechanics. *Science* 330, 1072–1074. DOI: 10.1126/science.1192065.

Pál, K. F., & Vértesi, T. (2010). Maximal violation of a bipartite three-setting, two-outcome Bell inequality using infinite-dimensional quantum systems. *Physical Review A* 82, 022116. DOI: 10.1103/PhysRevA.82.022116.

Brunner, N., Pironio, S., Acín, A., Gisin, N., Méthot, A. A., & Scarani, V. (2008). Testing the Dimension of Hilbert Spaces. *Physical Review Letters* 100, 210503. DOI: 10.1103/PhysRevLett.100.210503.

Cong, W., Cai, Y., Bancal, J.-D., & Scarani, V. (2017). Witnessing Irreducible Dimension. *Physical Review Letters* 119, 080401. DOI: 10.1103/PhysRevLett.119.080401.

Gonda, T., Kunjwal, R., Schmid, D., Wolfe, E., & Sainz, A. B. (2018). Almost Quantum Correlations are Inconsistent with Specker's Principle. *Quantum* 2, 87. DOI: 10.22331/q-2018-08-27-87.

Carmi, A., & Cohen, E. (2019). Relativistic independence bounds nonlocality. *Science Advances* 5, eaav8370. DOI: 10.1126/sciadv.aav8370.

Barandes, J. A., Hasan, M., & Kagan, D. (2026). Clauser-Horne-Shimony-Holt game, Tsirelson's bound, and causal locality. *Physical Review A* 114, 022208. DOI: 10.1103/xfpf-734d.
