"""Progressivity and redistribution indices used by the paper (Sec. 4.3).

Weighted implementations of the Gini coefficient, concentration index, Kakwani,
Suits, and Reynolds–Smolensky. The Díaz et al. (2010, 2011) level/distance
decomposition of ΔR–S is NOT implemented yet: the paper's eq. (5) as printed
contains a typo ("ΔR-S = S-S1 − R-S0") and we implement nothing whose exact
formula we have not read — see NOTES.md.
"""
import numpy as np


def _sorted_by(x, ranker, w):
    order = np.argsort(ranker, kind="stable")
    return np.asarray(x, float)[order], np.asarray(w, float)[order]


def concentration_index(x, ranker, w=None) -> float:
    """Concentration index of x when units are ranked by `ranker` (Gini if x==ranker).
    Weighted covariance formulation: C = 2 cov_w(x, F) / mean_w(x), with F the
    weighted mid-rank. Handles negative values the same way the Gini literature does."""
    x = np.asarray(x, float)
    w = np.ones_like(x) if w is None else np.asarray(w, float)
    xs, ws = _sorted_by(x, ranker, w)
    W = ws.sum()
    cum = np.cumsum(ws)
    F = (cum - 0.5 * ws) / W  # weighted fractional mid-ranks
    mu = np.average(xs, weights=ws)
    if mu == 0:
        return 0.0
    cov = np.average((xs - mu) * (F - np.average(F, weights=ws)), weights=ws)
    return 2.0 * cov / mu


def gini(x, w=None) -> float:
    return concentration_index(x, x, w)


def kakwani(tax, pre, w=None) -> float:
    """K = C_t − G_pre (paper eq. 2)."""
    return concentration_index(tax, pre, w) - gini(pre, w)


def suits(tax, pre, w=None) -> float:
    """Suits index: 1 − 2∫ L_t d(L_y): area-based against cumulative PRE-tax income
    share (not population share)."""
    tax = np.asarray(tax, float)
    pre = np.asarray(pre, float)
    w = np.ones_like(tax) if w is None else np.asarray(w, float)
    order = np.argsort(pre, kind="stable")
    t, y, ws = tax[order], pre[order], w[order]
    cy = np.cumsum(y * ws) / np.sum(y * ws)
    ct = np.cumsum(t * ws) / np.sum(t * ws)
    cy0 = np.concatenate([[0.0], cy])
    ct0 = np.concatenate([[0.0], ct])
    area = np.sum(0.5 * (ct0[1:] + ct0[:-1]) * np.diff(cy0))
    return 1.0 - 2.0 * area


def reynolds_smolensky(pre, post, w=None) -> float:
    """R–S = G_pre − G_post (paper eq. 1, ignoring re-ranking)."""
    return gini(pre, w) - gini(post, w)


def kakwani_identity_rs(tax, pre, w=None) -> float:
    """R–S via the decomposition t/(1−t)·K − D with D the re-ranking term omitted
    (the paper's Table A.4 reports D ≈ 0 for net wealth)."""
    tax = np.asarray(tax, float)
    pre = np.asarray(pre, float)
    ws = np.ones_like(tax) if w is None else np.asarray(w, float)
    t = np.average(tax, weights=ws) / np.average(pre, weights=ws)
    return t / (1.0 - t) * kakwani(tax, pre, w)
