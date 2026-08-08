# MKUFT–Dollard Field Geometry Notes

**Author:** Mark Charles McLaughlin  
**Framework:** McLaughlin–Kairos Unified Field Theory (MKUFT)  
**MKUFT DOI:** [10.5281/zenodo.17780566](https://doi.org/10.5281/zenodo.17780566)  
**Citation and provenance:** [PROVENANCE_DOI_AND_ATTRIBUTION.md](../PROVENANCE_DOI_AND_ATTRIBUTION.md)

**Status:** public comparative field-language bridge. It is not a new electrodynamic theory and does not establish equivalence between MKUFT, Tesla/Dollard terminology, aether models, or established electromagnetic theory.

## Purpose

This note compares selected MKUFT terms with field-realist electrical language associated with Tesla- and Dollard-influenced engineering discussions. Its role is translational: identify potentially useful structural correspondences while preserving the distinction between established electromagnetism, historical terminology, engineering heuristics, and MKUFT hypotheses.

A vocabulary bridge is not evidence that two theories share one ontology or mechanism.

## 1. Shared structural questions

Both electrical engineering and MKUFT frequently ask how stored state, boundary condition, geometry, resonance, propagation mode, and coupling determine an observed response.

The common research questions are therefore legitimate even where the surrounding vocabularies differ:

- What quantity is stored?
- What defines the boundary?
- Which mode propagates?
- How does geometry alter the solution?
- What establishes resonance?
- Which variables are physically measured?
- What ordinary theory already explains the observation?
- What result would require additional modelling?

## 2. Translation table

| MKUFT term | Possible comparative electrical language | Required caution |
|---|---|---|
| substrate/source-potential | aether, counterspace, background medium in historical or alternative literature | Translation only; no physical identity established |
| constraint or stored-state gradient | dielectric stress, potential gradient | Use Maxwell/material variables where they already suffice |
| circulation/rotational structure | magnetic induction, curl-like field structure | Must be represented by the appropriate vector field |
| resonance | tuned electrical response | Standard resonance theory remains baseline |
| boundary geometry | transmission-line, cavity, dielectric or electrode geometry | Ordinary field solutions must be modelled first |
| addressing/state matching | mode, frequency, phase or impedance matching | Does not imply nonlocal destination addressing |
| physical rendering | measured voltage, current, field, phase, heat, force or motion | Observable must be defined and instrumented |

## 3. Dielectric and magnetic structure

In standard electromagnetism, electric and magnetic fields are defined physical quantities with established units and equations. A dielectric modifies field response through material properties such as permittivity, polarisation, loss, and dispersion.

MKUFT may use **stored tension** as an intuitive bridge for a scalar candidate variable $\tau(x,t)$, but the physical model must map that variable to established observables or show a distinct measurable residual.

A gradient may be written

$$
\mathbf G_\tau=-\nabla\tau.
$$

If rotational structure is required, it must arise from an appropriate vector field $\mathbf A_\tau$:

$$
\mathbf H_\tau=\nabla\times\mathbf A_\tau.
$$

A scalar field does not acquire a curl by terminology.

A schematic effective functional may contain terms such as

$$
\mathcal F
=
\frac{1}{2}\alpha\lVert\nabla\tau\rVert^2
+
\frac{1}{2}\beta\lVert\nabla\times\mathbf A_\tau\rVert^2
+V(\tau,\mathbf A_\tau),
$$

but this is not automatically an electromagnetic energy density. Units, couplings, and empirical interpretation must be supplied.

## 4. Transmission geometry

Transmission lines, waveguides, cavities, dielectric interfaces, conductors, ground planes, and surrounding media are already geometric electromagnetic systems. Their behaviour depends on boundary conditions, impedance, propagation modes, losses, dispersion, and material response.

A generic candidate field variable may obey a wave-like equation,

$$
\frac{\partial^2\tau}{\partial t^2}
=
v_\tau^2\nabla^2\tau
-\mathcal L(\tau,\nabla\tau,\text{boundary},\text{material}),
$$

where $v_\tau$ and $\mathcal L$ require physical definition before comparison with electromagnetic propagation.

The existence of guided, longitudinal, evanescent, phase, group, or near-field behaviour in ordinary electromagnetism does not establish a distinct superluminal information channel. Signal velocity, causality, and detector timing remain governed by the physical model and experiment.

## 5. Resonance

Resonance is strong response under compatible forcing and boundary conditions. It is standard physics.

MKUFT's useful comparative question is whether resonance can be represented as reduced transition or coupling cost in a declared state space without losing the established electrodynamic description.

A candidate path weight may be written

$$
P(B\mid A)
\propto
\sum_{\gamma\in\Gamma(A\to B)}
\exp[-\beta C[\gamma]],
$$

where $C[\gamma]$ and $\beta$ are defined for the chosen model. This is a modelling bridge, not an alternative derivation of Maxwell's equations.

## 6. Earth–ionosphere and telluric systems

The Earth–ionosphere system is a real electromagnetic environment containing ground conductivity, oceans, atmosphere, ionosphere, geomagnetic field, solar-wind interaction, telluric currents, and global resonant modes including Schumann resonances.

Site-dependent electromagnetic behaviour may therefore depend on geology, water content, conductivity, atmospheric state, geomagnetic activity, frequency, and geometry.

A serious field study should measure those variables directly and compare observations with established electromagnetic and geophysical models before introducing an additional MKUFT term.

## 7. Solar field environment

The Sun is simultaneously a gravitating body, plasma system, radiative source, magnetic-field generator, and driver of the heliospheric environment. Standard solar physics provides the baseline.

MKUFT may compare the solar environment with a larger constraint or coherence system only where that comparison produces a defined observable or useful modelling distinction. Historical or symbolic systems that associate planetary configuration with human events do not become physical evidence by proximity to solar-field science.

## 8. Gravitation

Newtonian gravitation is written

$$
F=G\frac{m_1m_2}{r^2},
$$

while general relativity relates spacetime geometry to stress–energy through

$$
G_{\mu\nu}+\Lambda g_{\mu\nu}
=
\frac{8\pi G}{c^4}T_{\mu\nu}.
$$

MKUFT's physics-facing question is whether a deeper relational architecture can eventually recover this geometric regime rather than merely redescribe it.

It is therefore inaccurate to treat “field tension” or “constraint geometry” as an already established replacement for gravitation. Any such proposal must recover general relativity where tested and produce a distinct quantitative discriminator.

See [Layer Before Law](26_LAYER_BEFORE_LAW_MKUFT_QUANTUM_GRAVITY_REFRAMING.md) and [LUCY Threshold Geometry and Relational Closure](30_LUCY_THRESHOLD_GEOMETRY_AND_RELATIONAL_CLOSURE.md).

## 9. Dark matter and dark energy

Dark matter and dark energy are constrained by a broad cosmological evidence base. Hidden geometry or relational structure may be considered only as a competing quantitative model, not as an explanatory label.

A useful placeholder decomposition is

$$
G_{\mathrm{obs}}
=
G_{\mathrm{visible}}+G_{\mathrm{unexplained}},
$$

where the unexplained term may ultimately correspond to unseen matter, modified dynamics, effective geometry, systematic error, or another physical model. MKUFT does not currently derive the required cosmological term.

## 10. Experimental directions

The bridge is most useful when it produces ordinary controlled tests.

### Guided-mode propagation

Compare measured propagation, phase, and amplitude with transmission-line and waveguide models under varied geometry and grounding. Control cable delay, reflections, pickup, detector saturation, trigger artefacts, and ground loops.

### Dielectric and optical response

Measure phase, refractive index, nonlinear response, loss, temperature, humidity, pressure, and field strength. Any residual must survive established Kerr, Pockels, plasma, thermal, and material models.

### Telluric and site-dependent measurements

Measure conductivity, local electromagnetic spectra, geomagnetic indices, weather, geology, and instrumentation response. Site dependence alone is not anomalous.

### Toroidal and boundary-geometry tests

Compare preregistered geometries under matched drive, material, dimensions, field energy, sensor placement, and thermal conditions. The relevant result is a reproducible residual beyond the accepted electromagnetic solution.

### Timing tests

Any apparent anomalous timing requires independent clocks and rigorous control of cable delay, ringing, trigger leakage, RF pickup, reflection paths, and reconstruction error before a propagation claim is considered.

## 11. Falsification and limits

This bridge adds no new scientific value if established electromagnetic, material, geophysical, plasma, optical, or gravitational models explain the observations equally well; the translated terms cannot be given independent operational meaning; proposed scalar and vector quantities cannot be made dimensionally consistent; or a claimed new mode fails timing, causality, or replication tests.

It must also be reduced if the comparison depends on historical vocabulary alone rather than on a measurable difference.

## 12. Relationship to MKUFT

The role of this module is comparative rather than foundational. It may help identify candidate correspondences among gradient, boundary, resonance, stored state, circulation, and propagation, but the canonical scientific claims remain in the [Core](01_MKUFT_CORE_EXTENDED.md), [Mathematical Appendix](02_MKUFT_MATH_APPENDIX.md), [Gradient Mechanics](16_GRADIENT_MECHANICS_BOUNDARY_SHEAR_GEOMETRY.md), [Layer Before Law](26_LAYER_BEFORE_LAW_MKUFT_QUANTUM_GRAVITY_REFRAMING.md), and [Falsification Summary](05_FALSIFICATION_SUMMARY.md).

## Summary

The technically useful common ground is modest:

> Stored state, boundary geometry, resonance, circulation, and propagation are real organising concepts in field systems. MKUFT may compare them with its deeper constraint language only where the translation remains typed, dimensionally lawful, and experimentally accountable.

A translation is not an equivalence, and a suggestive analogy is not evidence.
