"""The paper's long-run accumulation framework (p.15, following Durán-Cabré &
Esteller-Moré 2019/09), implemented exactly as stated: every unit's wealth grows at
a uniform constant g; under taxation it is additionally reduced each year.

This module exists mainly to demonstrate the scale-invariance point behind REVIEW.md
finding `equivalized-longrun-artefact`: with uniform g the NO-TAX distribution's Gini
is constant, so any reported rise under a near-proportional-to-wealth tax at tiny
cumulative rates is a construction artefact, not economics.
"""
import numpy as np


def project(w0, annual_tax_rate, g: float, T: int):
    """w_i(T) = w_i(0) · [(1+g)(1−t_i)]^T with per-unit constant rates t_i.

    `annual_tax_rate` may be a scalar or a per-unit array (each unit's own average
    rate, e.g. liability_i / wealth_i in year 0 — the paper's constant-t reading).
    """
    w0 = np.asarray(w0, float)
    t = np.broadcast_to(np.asarray(annual_tax_rate, float), w0.shape)
    return w0 * ((1.0 + g) * (1.0 - t)) ** T


def cumulative_effective_rate(w0, annual_tax_rate, g: float, T: int) -> float:
    """t_l/r per the paper's Table 5 note: cumulative tax over accumulated wealth,
    computed as 1 − Σ w_i(T)^taxed / Σ w_i(T)^untaxed (g cancels)."""
    taxed = project(w0, annual_tax_rate, g, T).sum()
    untaxed = project(w0, 0.0, g, T).sum()
    return 1.0 - taxed / untaxed
