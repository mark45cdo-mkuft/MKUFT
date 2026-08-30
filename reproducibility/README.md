# MKUFT Reproducibility

**Owner:** Mark Charles McLaughlin  
**Framework:** McLaughlin–Kairos Unified Field Theory (MKUFT)  
**Status:** operational reproducibility index; not a separate scientific theory or publication

This directory contains machine-checkable packages that reproduce named calculations, transformations, or analysis steps used by MKUFT research objects.

The governing distinction is:

> **Reproducibility evidence is evidence that a declared procedure can be re-executed and returns the declared result. It is not automatically independent evidence that the underlying scientific claim is true.**

A package derived deterministically from the same equations, assumptions, or source object inherits that ancestry. Machine-readable output, a second file format, a later execution, or external hosting does not by itself create an independent evidential source.

Use the typed relation:

```text
source derivation / declared inputs
→ executable verifier
→ derived verification output
→ integrity record
```

This can establish or strengthen:

- arithmetic and transcription checking;
- implementation consistency;
- reproducibility of a declared transformation;
- exact machine-readable values;
- carrier integrity and later re-execution.

It does **not** by itself establish:

- new empirical evidence;
- an independent physical measurement;
- a new mechanism;
- novelty beyond the native mathematical owner;
- independent confirmation of a result when the package is generated from that same result.

If a verifier consumes independently obtained measurements, a held-out dataset, or another independently specified evidential source, any additional evidential weight belongs to that independent source and its native controls, not to the packaging step itself.

## Current package

### MKUFT Preprints v1.2 — Bell/CHSH computational verification

[`MKUFT_PREPRINTS_v1.2_BELL_CHSH_CALIBRATION/`](MKUFT_PREPRINTS_v1.2_BELL_CHSH_CALIBRATION/)

This package reproduces the symmetric Tsirelson-point calculation used in the 30 August 2026 Layer Before Law submission synthesis. It checks the CHSH score, transverse coordinate, facet projection, barycentric coordinates, exact reconstruction, and the candidate four-volume reduction.

Its scientific status remains the status of the owning Bell calculation: the chart is exact; the natural four-volume reduces to known CHSH excess; the independent new-physics residual is **NULL**.

## Canonical owners

- [Module 28A — Bell/CHSH calibration](../docs/28A_CROSS_DOMAIN_COMPOSITIONAL_SCHEMA_BELL_CHSH_CALIBRATION.md)
- [Module 34 — Research Object Identity, Release Integrity, and Reproducibility](../docs/34_RESEARCH_OBJECT_IDENTITY_RELEASE_INTEGRITY_AND_REPRODUCIBILITY.md)
- [Research Derivation and Closure SOP](../RESEARCH_DERIVATION_AND_CLOSURE_SOP.md)

## Minimum package contract

Where a calculation is promoted into a reusable verification package, preserve at least:

1. the exact source object or equation family being reproduced;
2. declared inputs and conventions;
3. executable or otherwise deterministic reproduction procedure;
4. expected outputs and tolerances;
5. captured verification output where useful;
6. integrity hashes for the declared package files where useful;
7. an explicit statement of whether the output is derived verification data, independent empirical data, or another typed evidence class;
8. the failure condition: what mismatch would make the package fail.

Do not create a reproducibility package merely to satisfy an external form. Keep it only when the package leaves the scientific object more recoverable, checkable, or falsifiable than before.
