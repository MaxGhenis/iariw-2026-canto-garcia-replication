"""Index sanity checks plus the two demonstrations behind REVIEW.md's mechanical findings:
scale invariance of the Gini under uniform growth, and the upper bound on how far a
near-proportional tax can move it."""
import numpy as np
import pytest

from wealth_tax_es.indices import (
    concentration_index,
    gini,
    kakwani,
    kakwani_identity_rs,
    reynolds_smolensky,
    suits,
)
from wealth_tax_es.longrun import cumulative_effective_rate, project


def test_gini_known_values():
    assert gini([1, 1, 1, 1]) == pytest.approx(0.0, abs=1e-12)
    # One unit holds everything: G -> (n-1)/n with mid-rank formula
    assert gini([0, 0, 0, 100]) == pytest.approx(0.75)
    assert gini([1, 2, 3, 4]) == pytest.approx(0.25)


def test_weights_equal_replication():
    x = [10.0, 20.0, 70.0]
    assert gini(x, w=[2, 2, 2]) == pytest.approx(gini([10, 10, 20, 20, 70, 70]))


def test_kakwani_sign():
    pre = np.array([100.0, 200.0, 700.0])
    prog = np.array([0.0, 2.0, 28.0])   # burden concentrated on the rich
    flat = pre * 0.01
    assert kakwani(prog, pre) > 0
    assert kakwani(flat, pre) == pytest.approx(0.0, abs=1e-12)
    assert suits(prog, pre) > 0
    assert suits(flat, pre) == pytest.approx(0.0, abs=1e-9)


def test_rs_identity_close_without_reranking():
    rng = np.random.default_rng(7)
    pre = np.exp(rng.normal(11, 1.2, 20_000))
    tax = np.where(pre > np.quantile(pre, 0.99), (pre - np.quantile(pre, 0.99)) * 0.02, 0.0)
    direct = reynolds_smolensky(pre, pre - tax)
    via_identity = kakwani_identity_rs(tax, pre)
    # Tax preserves ranking -> D ~ 0 -> the two agree to first order
    assert direct == pytest.approx(via_identity, rel=0.05)


def test_uniform_growth_is_scale_invariant():
    """The no-tax Gini is IDENTICAL at any horizon under uniform g — the premise of
    REVIEW.md finding `equivalized-longrun-artefact` (Table 5's rising equivalized
    Gini cannot come from the stated framework)."""
    rng = np.random.default_rng(42)
    w0 = np.exp(rng.normal(11, 1.4, 50_000)) - 5_000  # includes negatives
    for T in (25, 50, 100):
        assert gini(project(w0, 0.0, 0.02, T)) == pytest.approx(gini(w0), abs=1e-12)


def test_ip_scale_tax_cannot_raise_gini_a_full_point():
    """An IP-like tax (levied only above a high threshold, i.e. concentration index
    near 1) at the paper's cumulative 0.50%-of-wealth scale moves the Gini DOWN and
    by far less than one point: |ΔG| <= t/(1-t) * (C_t - G) ≈ 0.17 points."""
    rng = np.random.default_rng(1)
    w0 = np.exp(rng.normal(11.0, 1.5, 200_000))
    thr = np.quantile(w0, 0.996)
    rate = 0.0002  # per-year, calibrated so cumulative T=25 burden ~0.5% of wealth
    t_i = np.where(w0 > thr, rate * (w0 - thr) / w0 * 40, 0.0)
    wT = project(w0, t_i, 0.02, 25)
    cum = cumulative_effective_rate(w0, t_i, 0.02, 25)
    g0, gT = gini(w0), gini(wT)
    assert gT < g0  # a top-concentrated tax cannot RAISE the Gini
    ct = concentration_index(np.where(w0 > thr, w0 - thr, 0.0), w0)
    bound = cum / (1 - cum) * (ct - g0)
    assert (g0 - gT) <= bound * 1.05  # Kakwani-style upper bound holds
    assert (g0 - gT) < 0.01  # far below one Gini point (0.01 on the 0-1 scale)
