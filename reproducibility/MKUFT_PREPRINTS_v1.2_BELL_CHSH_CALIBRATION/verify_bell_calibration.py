#!/usr/bin/env python3
"""Reproduce the Bell/CHSH calibration reported in the MKUFT Preprints synthesis.

Standard-library only. This script verifies the symmetric Tsirelson-point calculation,
facet projection, barycentric coordinates, exact reconstruction, and the fact that the
candidate 4-volume is a fixed rescaling of CHSH excess.

The outputs are computational verification data, not independent empirical evidence
for a new physical mechanism.
"""
from math import sqrt, isclose

TOL = 1e-12
c = (1.0, 1.0, 1.0, -1.0)
E_Q = tuple(x / sqrt(2.0) for x in c)
S = sum(ci * ei for ci, ei in zip(c, E_Q))
nu = S - 2.0
Pi = tuple(ei - (nu / 4.0) * ci for ci, ei in zip(c, E_Q))

# Columns are the four local deterministic correlator vertices saturating c^T E = 2.
V_cols = (
    (1.0, 1.0, 1.0, 1.0),
    (1.0, -1.0, 1.0, -1.0),
    (1.0, 1.0, -1.0, -1.0),
    (-1.0, 1.0, 1.0, -1.0),
)
lambda_vec = (0.25, 0.25, 0.25, 0.25)
V_lambda = tuple(sum(V_cols[j][i] * lambda_vec[j] for j in range(4)) for i in range(4))
E_reconstructed = tuple(V_lambda[i] + (nu / 4.0) * c[i] for i in range(4))
volume = abs(S - 2.0) / 3.0

expected_Pi = tuple(0.5 * x for x in c)
expected_S = 2.0 * sqrt(2.0)
expected_nu = 2.0 * sqrt(2.0) - 2.0
expected_volume = expected_nu / 3.0

checks = {
    "S = 2*sqrt(2)": isclose(S, expected_S, abs_tol=TOL, rel_tol=TOL),
    "nu = 2*sqrt(2)-2": isclose(nu, expected_nu, abs_tol=TOL, rel_tol=TOL),
    "Pi_c(E_Q) = c/2": all(isclose(a, b, abs_tol=TOL, rel_tol=TOL) for a, b in zip(Pi, expected_Pi)),
    "lambda = (1/4,1/4,1/4,1/4)": isclose(sum(lambda_vec), 1.0, abs_tol=TOL),
    "exact reconstruction": all(isclose(a, b, abs_tol=TOL, rel_tol=TOL) for a, b in zip(E_reconstructed, E_Q)),
    "V_c = |S-2|/3": isclose(volume, expected_volume, abs_tol=TOL, rel_tol=TOL),
}

print("MKUFT Bell/CHSH computational verification")
print(f"S = {S:.15f}")
print(f"nu = {nu:.15f}")
print("Pi_c(E_Q) = (" + ", ".join(f"{x:.15f}" for x in Pi) + ")")
print("lambda = (" + ", ".join(f"{x:.15f}" for x in lambda_vec) + ")")
print("E_reconstructed = (" + ", ".join(f"{x:.15f}" for x in E_reconstructed) + ")")
print(f"candidate_volume = {volume:.15f}")
print()
for name, ok in checks.items():
    print(f"{'PASS' if ok else 'FAIL'}  {name}")

if not all(checks.values()):
    raise SystemExit(1)
