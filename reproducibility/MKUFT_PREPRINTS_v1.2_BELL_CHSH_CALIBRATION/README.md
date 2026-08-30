# MKUFT Preprints v1.2 - Bell/CHSH computational verification package

This folder reproduces the worked Bell/CHSH calibration used in **MKUFT - Layer Before Law: A Typed Relational Architecture for Physical-Law Selection, Future-Sufficient Interfaces, and Cross-Scale Dynamics**, Preprints synthesis v1.2 (30 August 2026).

## Scope

The package verifies a standard symmetric Tsirelson-point calculation in the facet-adapted tetrahedral Bell chart used by the manuscript. It checks:

1. `c = (1,1,1,-1)` and `E_Q = c/sqrt(2)`;
2. `S = c^T E_Q = 2*sqrt(2)`;
3. `nu = S - 2 = 2*sqrt(2)-2`;
4. `Pi_c(E_Q) = E_Q - (nu/4)c = c/2`;
5. the facet projection has barycentric coordinates `lambda = (1/4,1/4,1/4,1/4)` with respect to the four local deterministic vertices saturating `c^T E = 2`;
6. exact reconstruction `E_Q = V lambda + (nu/4)c`;
7. the natural candidate four-volume `V_c(E_Q) = |S-2|/3`.

The final quantity is a fixed rescaling of already-known CHSH excess. Therefore this package supports the manuscript's **null new-physics residual**: the chart is an exact and useful representation, but this calculation does not establish a new Bell inequality, a new Tsirelson derivation, a quantum mechanism, or an independent physical invariant.

## Files

- `bell_chsh_calibration.csv` - compact computational verification data.
- `verify_bell_calibration.py` - standard-library Python script that recomputes the values and exits non-zero on a failed check.
- `verification_output.txt` - captured output from the verification run used to freeze this package.
- `SHA256SUMS.txt` - file-integrity hashes for the package contents.

## Reproduce

```bash
python verify_bell_calibration.py
```

Expected result: all six checks report `PASS`.

## Evidential status

These are **original computational verification data generated for the revised manuscript**. They reproduce algebraic results already stated in the manuscript. They are not empirical measurements and do not constitute independent evidence for a new physical mechanism.

## Related public research objects

- Principal MKUFT: DOI `10.5281/zenodo.21973064`
- Layer Before Law: DOI `10.5281/zenodo.21971270`
- Cross-Domain Compositional Schema v0.4: DOI `10.5281/zenodo.22166468`
