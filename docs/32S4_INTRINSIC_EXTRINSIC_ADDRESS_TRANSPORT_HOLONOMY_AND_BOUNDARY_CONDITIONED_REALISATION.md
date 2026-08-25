# 32S4 — Intrinsic–Extrinsic Address Transport, Holonomy, and Boundary-Conditioned Realisation

**Author:** Mark Charles McLaughlin  
**Framework:** McLaughlin–Kairos Unified Field Theory (MKUFT)  
**MKUFT DOI:** [10.5281/zenodo.17780566](https://doi.org/10.5281/zenodo.17780566)  
**Canonical root:** [32 — Recursive Constraint Closure and Reachable-State Geometry](32_RECURSIVE_CONSTRAINT_CLOSURE_AND_REACHABLE_STATE_GEOMETRY.md)  
**Relation/scale owner:** [32S — Load-Bearing Relation Sets and Scale-Transition Tests](32S_LOAD_BEARING_RELATION_SETS_AND_SCALE_TRANSITION_TESTS.md)  
**Identity/history guards:** [32S1](32S1_INVARIANT_PERSISTENCE_RELATIONAL_ADDRESSABILITY_AND_SCALE_TRANSITION.md); [32S2](32S2_TEMPORAL_CONTINUITY_KERNELS_AND_MINIMUM_IDENTITY_HORIZON.md)  
**Bracket/completion owner:** [32S3](32S3_RELATIONAL_BRACKETS_COMPLETION_GEOMETRY_AND_I_TO_P_ADMISSIBILITY.md)  
**Novelty boundary:** [32A — Module 32 Novelty Audit and Contribution Boundary](32A_MODULE_32_NOVELTY_AUDIT_AND_CONTRIBUTION_BOUNDARY.md)  
**Public formulation date:** 15 August 2026  
**Rights:** Copyright © 2026 Mark Charles McLaughlin. All rights reserved unless an exact later publication states otherwise.  
**Status:** canonical formal refinement of the Module 32 family. It separates intrinsic relational organisation from extrinsic contextual address, makes transport path/history explicit, introduces a bundle-compatible but not automatically bundle-valued realisation family, and uses boundary-conditioned field modes and holographic reconstruction as controlled P-layer comparators. It does not establish an independent I layer, vacuum-energy extraction, nonlocal signalling, holographic reality, or a universal transport law.

## 1. Purpose

Modules 32S1–32S3 distinguish relational identity, temporal continuity, completion fibers, compatible assignment regions, and scale realisation classes. One further distinction is needed.

An object may preserve its **intrinsic relational organisation** while its **extrinsic address** changes. Moving or re-embedding the object changes its relations to environment, boundary conditions, measurement frame, and history even when the relations among its own constitutive parts remain invariant to the declared tolerance.

The new question is therefore:

> **What must be transported when an internally coherent object changes contextual address, and when does the surrounding address alter the set of physical realisations available to that same intrinsic relational class?**

This refinement prevents two opposite errors:

1. treating a change of place/context as if it necessarily changed the object's intrinsic organisation;
2. treating preserved intrinsic organisation as if it guaranteed the same physical realisation independently of context, boundary and path.

## 2. Intrinsic relation class versus extrinsic address

Let

```math
x_t\in\mathcal X_{\alpha_t}
```

be a realised state at construction address `alpha_t`.

Let

```math
\kappa_t:\mathcal X_{\alpha_t}\rightarrow\mathcal K_t
```

extract the declared **intrinsic relational descriptor**: the relation family claimed to remain constitutive under admissible relocation or re-embedding.

Let

```math
b_t\in\mathcal B_t
```

be the declared **extrinsic address**, containing only the contextual variables relevant to the claim: for example position, orientation, external boundary, system–environment coupling, field configuration, neighbouring objects, measurement frame, or another operationally specified context.

The split

```math
(\kappa_t,b_t)
```

is claim-relative. It is not an assertion that nature factorises into two independent substances.

For an admissible relocation or re-embedding operation `g`, intrinsic preservation means

```math
d_{\mathcal K}\!\left(
\kappa(g\cdot x),
\kappa(x)
\right)
\leq\varepsilon_{\kappa},
```

while the extrinsic address is allowed to change:

```math
b\rightarrow b'.
```

Thus:

> **same intrinsic relation class does not imply same extrinsic address; changed extrinsic address does not imply changed intrinsic relation class.**

Any property that depends on both must be evaluated on the joint addressed object rather than on either coordinate alone.

## 3. Context-indexed realisation fibers

For physical applications, let

```math
\mathfrak P
=
\bigsqcup_{\beta\in A_P}
\{\beta\}\times\mathcal P_\beta
```

be the addressed family of physical state spaces.

For an intrinsic relational class `kappa`, extrinsic address `b`, and relevant history `h`, define the **compatible P-realisation set**

```math
\boxed{
\mathcal F_P(\kappa;b,h)
=
\left\{
p\in\mathfrak P:
\chi_{P}(p;\kappa,b,h)=1
\right\}.
}
```

`chi_P` is an implementation-specific compatibility test and may include several typed relations from Module 32S3. The set can be empty, broad, narrow, or split across several physical construction addresses.

This creates a bundle-compatible addressed family

```math
\mathfrak R_\kappa
=
\bigsqcup_{b\in\mathcal B}
\{b\}\times\mathcal F_P(\kappa;b,h_b),
```

but it must not be called a fiber bundle unless the mathematical conditions required for a bundle—such as an appropriate projection and local triviality—are actually demonstrated.

The key distinction is:

```text
intrinsic relational specification
≠ compatible physical realisation
≠ actual physical occupancy
```

A non-empty `F_P` means that the declared model permits one or more P-realisations at that address. It does not mean that one of them is actually occupied. An empty set means the model supplies no compatible P-realisation under the tested conditions; it does not imply that a hidden physical object remains present but invisible.

This is the sober version of a `latent address`: **a relational specification may remain mathematically addressable even when current P-occupancy is absent.**

## 4. Transport along contextual paths

Let

```math
\gamma:[0,1]\rightarrow\mathcal B
```

be a declared path through extrinsic/context space from

```math
\gamma(0)=b_0
```

to

```math
\gamma(1)=b_1.
```

Where a lawful transport exists, define

```math
T_\gamma:
\mathcal F_P(\kappa_0;b_0,h_0)
\supseteq\mathcal D_\gamma
\rightarrow
\mathcal F_P(\kappa_1;b_1,h_1).
```

Transport preserves the intrinsic relation class to tolerance when

```math
d_{\mathcal K}\!\left(
\kappa_1(T_\gamma p),
\kappa_0(p)
\right)
\leq\varepsilon_\kappa.
```

Identity continuity still requires the separate 32S1/32S2 conditions. A transport map is not by itself a proof of same-self continuity.

The important new point is that the map may be **path-dependent**:

```math
T_{\gamma_1}\neq T_{\gamma_2}
```

even when `gamma_1` and `gamma_2` have the same endpoints.

This gives a precise place for history to remain load-bearing after ordinary endpoint coordinates agree.

## 5. Closed-loop transport and holonomy

For a closed contextual loop

```math
\gamma(0)=\gamma(1)=b,
```

define the loop transport

```math
\mathcal H_\gamma
=
T_\gamma.
```

If

```math
\mathcal H_\gamma(p)\neq p
```

under the declared observable/equivalence relation, the system carries a **non-trivial path memory** around that loop.

Where the implementation is genuinely a connection on a bundle, `H_gamma` may be called holonomy in the standard mathematical sense. Otherwise `loop transport` is the safer term.

Berry's geometric phase and Simon's bundle/holonomy formulation are established physical precedents showing that a system can return to the same endpoint in parameter space while retaining a path-dependent geometric phase.

This does **not** imply that ordinary spatial translation of an arbitrary object generates a Berry phase. The comparator applies only where the system's actual control/parameter space and transport law support the required connection.

For MKUFT, the methodological refinement is:

> **same endpoint is insufficient whenever the candidate identity, state, phase, or admissibility is path-dependent. Test the transport around the path, not only the coordinates at its ends.**

This is the connection-level sharpening of Module 32S2's history guard.

## 6. Nested relational systems and joint address compatibility

An object generally participates in several relation families at once: internal organisation, local environment, larger-scale boundary, field context, observer-accessible readout, and other declared layers/scales.

Let the jointly relevant constraints be indexed by `(s,r)`, where `s` denotes scale/layer address and `r` a typed relation. For one total candidate state `z`, define

```math
\mathfrak C_{\mathrm{nested}}
=
\left\{
z:
 e_{s,r}(z)\leq\varepsilon_{s,r}
\quad
\forall(s,r)\in\mathfrak E_{\mathrm{tested}}
\right\}.
```

This is intentionally generic. Where the component state spaces differ, the implementation must use lawful pullbacks, fiber products, embeddings, or other typed comparison maps rather than pretending every constraint lives in one common Euclidean space.

A candidate realisation can therefore preserve its internal class while failing a larger contextual compatibility condition.

That gives the sharpened sequence:

```text
intrinsic organisation preserved
+ extrinsic address transported
+ nested contextual constraints compatible
→ P-realisation remains admissible
```

If the final condition fails, the correct conclusion is **loss or change of admissible realisation under that context**, not destruction of the intrinsic relation definition by fiat.

## 7. Boundary-conditioned P-state geometry

Established physics supplies direct P-layer examples in which external boundary conditions change available physical mode structure.

For a field/operator `L_b` under boundary/context `b`, an admissible mode family may be represented schematically by

```math
\widehat L_b\phi_n^{(b)}
=
\lambda_n(b)\phi_n^{(b)},
```

with boundary condition

```math
\widehat B_b\phi_n^{(b)}=0.
```

Changing geometry, material response, separation, or another lawful boundary variable can change the allowed spectrum

```math
\{\lambda_n(b)\}
```

and therefore the physically accessible field configurations.

Casimir experiments with nanostructured surfaces provide direct examples in which geometry and material boundary conditions change measured fluctuation-induced forces. This is a direct P-layer example of **boundary-conditioned mode structure and measurable response**.

The scale language must remain accurate: `mesoscopic` means an intermediate finite scale, not an infinitesimal edge. Casimir and related boundary effects can become experimentally important at micro- and nanometre separations depending on the system.

### 7.1 Static vacuum language requires care

Casimir forces are often described through changes in zero-point mode structure, but equivalent formulations can emphasize quantum interactions of charges and currents rather than treating a literal zero-point-energy reservoir as the unique ontology.

Therefore MKUFT should use the conservative statement:

> **quantum boundary conditions and material/geometry relations alter measurable field observables and fluctuation-induced interactions.**

Do not infer an extractable hidden energy reservoir merely from a mode-counting picture.

### 7.2 Dynamical boundary conditions

A time-dependent boundary/context

```math
b=b(t)
```

can change the mode structure non-adiabatically. The dynamical Casimir effect provides an experimentally demonstrated case in which rapid modulation of an effective electromagnetic boundary generates real photons.

This is highly relevant as a comparator because it shows:

```text
boundary relation changes
→ admissible field-mode structure changes
→ physically measurable excitations can appear
```

But the boundary modulation is actively driven. Any MKUFT energy claim must therefore carry complete energy accounting. Generated photons or mechanical work cannot be labelled `self-power`, `free vacuum energy`, or `zero-point extraction` unless a closed-cycle experiment explicitly identifies an additional energy source after all drive, preparation, non-equilibrium, thermal, chemical, electromagnetic, mechanical and measurement inputs are accounted for.

Ground-state/passivity results provide the controlling thermodynamic guard against treating the vacuum as a free cyclic work reservoir.

## 8. Holography as a transport/readout comparator

Metasurface holography supplies a controlled physical comparator.

Let the incident optical field be

```math
U_{\mathrm{inc}}(x,y),
```

and let

```math
t_{\mathrm{meta}}(x,y)
```

denote the metasurface transfer/encoding function. Schematically, the field immediately after the surface is

```math
U_0(x,y)
=
U_{\mathrm{inc}}(x,y)t_{\mathrm{meta}}(x,y),
```

and propagation/readout produces

```math
U_{\mathrm{out}}
=
\mathcal H_{b,R}\left[U_0\right],
```

where `b` contains the remaining physical boundary/propagation conditions and `R` the declared readout plane or transform.

Geometric-phase metasurfaces provide direct optical examples in which the orientation of subwavelength elements determines local phase and the collective phase distribution reconstructs a holographic field only after propagation.

A deliberately bounded MKUFT comparator is narrower than `the whole is in every part`:

> **a distributed relational encoding can remain physically present while the target gestalt is absent from direct local inspection and appears only under the correct transform/readout conditions.**

The same encoded structure can produce a different readout when illumination, polarization, propagation distance, phase relation, aperture, or observation geometry changes.

### 8.1 Matched incident/surface phase as a controlled physical comparator

Qu et al. (2020) provide an especially useful controlled example because the phase specification required for one holographic image is explicitly separated into two physical matrices: one carried by the incident beam and one encoded in the metasurface.

Their interaction can be written schematically as

```math
U_{\mathrm{out}}(x,y,z)
=
\mathcal H_z
\left[
U_{\mathrm{inc}}(x_0,y_0)
U_{\mathrm{meta}}(x_0,y_0)
\right],
```

with the paper giving the corresponding diffraction integral through the system impulse response.

The important comparator is not the encryption application. It is the relation:

```text
fixed encoded surface
+ matched external phase structure
+ propagation/readout
→ intended holographic gestalt
```

Experimentally, the same metasurface illuminated with an incorrect uniform beam produced misleading rather than intended information, while the designed incident phase recovered the intended image. The same static metasurface could also produce different holographic images when the incident phase distribution was changed.

In native optical terms, this is a controlled P-layer example in which the reconstructed field depends jointly on the incident field, metasurface response, and propagation/readout. As an MKUFT comparator, it motivates asking whether a separately controlled contextual variable changes a claimed higher-order realisation while intrinsic encoding is held fixed. Neither physical matrix alone should be relabelled as an I layer, and the optical result does not establish a general holographic ontology.

It does, however, motivate a discriminating question for any claimed context-indexed realisation:

> **Can the same intrinsic encoding be held fixed while a separately controlled contextual relation switches the predicted higher-order realisation on, off, or into a different admissible class?**

This motivates a deformation-test programme; it does not establish that biological or cosmological systems are holograms.

## 9. Relation to I→P

The present refinement does not identify the I layer with a fiber, connection, optical phase, vacuum field, or geometric phase.

It instead sharpens the empirical I→P question from Module 32S3.

Let the physical family be addressed:

```math
\mathfrak P
=
\bigsqcup_{\beta\in A_P}
\{\beta\}\times\mathcal P_\beta.
```

Then a candidate I-conditioned physical transition kernel should be written on that addressed family:

```math
K_P\!\left(
dp_{t+\Delta}
\mid
\beta_t,p_t,H_t^P,i_t
\right),
\qquad
p_t\in\mathcal P_{\beta_t}.
```

Its support is

```math
\Omega_{P,t}^{\mathrm{adm}}(i_t)
=
\mathrm{supp}
K_P\!\left(
\cdot
\mid
\beta_t,p_t,H_t^P,i_t
\right)
\subseteq\mathfrak P.
```

A candidate I relation could therefore, in principle, be tested for changing:

1. transition weights inside one P-address;
2. the support inside one P-address;
3. the reachable P-address itself.

Case 3 requires the same no-false-comparison discipline as Module 32: if the physical construction address changes, cross-address distances or state subtraction require a lawful comparison map.

This section **supersedes any fixed-P-space reading of the schematic I→P kernel in 32S3**. It does not by itself provide evidence that an independent I variable exists.

## 10. Discriminating tests

### 10.1 Rigid-relocation / intrinsic-invariance test

Move or re-embed a physical object through a preregistered set of extrinsic addresses while preserving internal organisation as far as possible. Test which observables remain invariant and which track external address.

If the claimed intrinsic descriptor changes under ordinary relocation when it was supposed to remain invariant, reduce the descriptor.

### 10.2 Same-endpoint / different-path test

Prepare matched starting states and transport them through two different paths with the same endpoint context. If the endpoint observable differs prospectively in the predicted path-dependent quantity, history/transport is load-bearing. If not, prefer endpoint-only modelling.

### 10.3 Closed-loop transport test

Return the system to the same declared context after a loop and test for a preregistered phase/state/identity-relevant residual. A loop effect must compete with drift, hysteresis, thermal memory, mechanical backlash, instrument memory and ordinary field-history explanations.

### 10.4 Context-conditioned realisation test

Preserve the intrinsic relation class while changing one external relation at a time. Predict how `F_P(kappa;b,h)` changes. A claim that context shapes realisation must predict the direction/class of the change before measurement.

### 10.5 Boundary-spectrum test

For a physical field system, preregister a boundary deformation and predict the corresponding mode, resonance, force or other observable shift using the accepted domain physics before testing any residual MKUFT term.

### 10.6 Holographic transform and matched-context test

Where a holographic analogy is claimed physically, specify the encoding, illumination, propagation operator and readout plane. Hold the encoding fixed while deforming incident phase/context, then hold the incident context fixed while deforming encoding. Compare the resulting reconstruction with a preregistered model and with the matched-joint condition. Visual resemblance alone does not pass.

### 10.7 Energy-accounting gate

For any vacuum, Casimir, dynamical-boundary or `self-power` claim, measure all known inputs and outputs over a complete repeatable cycle. No anomalous energy claim is promoted unless the residual survives calibration, uncertainty, hidden-storage, drive, thermal, chemical, electromagnetic, mechanical and non-equilibrium accounting.

## 11. Prior-art and novelty boundary

The broad ingredients are established prior art and are not claimed as MKUFT inventions:

- fiber bundles, connections, parallel transport and holonomy;
- Berry phase and geometric phase;
- gauge covariance and path-dependent phase transport;
- boundary-value problems and boundary-conditioned spectra;
- Casimir and fluctuation-induced forces;
- dynamical Casimir photon generation under driven boundary modulation;
- optical and metasurface holography, including jointly encoded incident/surface phase schemes;
- coarse-graining, multiple realisation and context-dependent physical response.

The candidate MKUFT contribution is narrower:

> **integrate intrinsic/extrinsic relational address separation, path-dependent transport, completion/realisation fibers, nested bracket compatibility, addressed I→P transition support, matched-context holographic deformation, and boundary/energy-accounting controls into the Module 32 scale-and-identity audit without allowing latent relational specification to become physical occupancy or boundary-conditioned quantum effects to become an unaccounted energy source.**

Historical priority for this exact conjunction is not asserted without broader review. Module 32A owns the evolving novelty boundary.

## 12. References

- Simon, B. (1983). *Holonomy, the Quantum Adiabatic Theorem, and Berry's Phase*. Physical Review Letters 51, 2167. DOI `10.1103/PhysRevLett.51.2167`.
- Berry, M. V. (1984). *Quantal phase factors accompanying adiabatic changes*. Proceedings of the Royal Society A 392, 45–57. DOI `10.1098/rspa.1984.0023`.
- Jaffe, R. L. (2005). *Casimir effect and the quantum vacuum*. Physical Review D 72, 021301(R). DOI `10.1103/PhysRevD.72.021301`.
- Chan, H. B. et al. (2008). *Measurement of the Casimir Force between a Gold Sphere and a Silicon Surface with Nanoscale Trench Arrays*. Physical Review Letters 101, 030401. DOI `10.1103/PhysRevLett.101.030401`.
- Bao, Y. et al. (2010). *Casimir Force on a Surface with Shallow Nanoscale Corrugations: Geometry and Finite Conductivity Effects*. Physical Review Letters 105, 250402. DOI `10.1103/PhysRevLett.105,250402`.
- Wilson, C. M. et al. (2011). *Observation of the dynamical Casimir effect in a superconducting circuit*. Nature 479, 376–379. DOI `10.1038/nature10561`.
- Huang, L., Chen, X., Mühlenbernd, H. et al. (2013). *Three-dimensional optical holography using a plasmonic metasurface*. Nature Communications 4, 2808. DOI `10.1038/ncomms3808`.
- Frey, M., Funo, K., and Hotta, M. (2014). *Strong local passivity in finite quantum systems*. Physical Review E 90, 012127. DOI `10.1103/PhysRevE.90.012127`.
- Qu, G., Yang, W., Song, Q. et al. (2020). *Reprogrammable meta-hologram for optical encryption*. Nature Communications 11, 5484. DOI `10.1038/s41467-020-19312-9`.

## 13. Compressed rules

> **Separate what the object is internally from where and how it is embedded externally.**

> **Move the address without silently moving the identity criterion.**

> **When history can matter, compare paths, not only endpoints.**

> **A relational specification can remain addressable without being physically occupied.**

> **Boundary conditions can change physical mode structure; that is a P-layer fact, not automatic evidence for an independent I layer.**

> **A holographic encoding and its reconstructed gestalt are different addressed objects connected by a physical transform.**

> **A fixed encoding can require a matched external relation for a specific gestalt to realise; test the joint condition rather than either component alone.**

> **Vacuum/boundary effects do not waive energy accounting.**

> **At scale: preserve intrinsic relation where justified, transport extrinsic address lawfully, test nested compatibility, then ask which P-realisations remain admissible.**