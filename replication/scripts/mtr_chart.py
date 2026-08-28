"""Statutory wealth-tax schedules: marginal and average rates by net wealth,
for the five real tax systems in Cantó & García-Rodríguez (2026).

Two stacked panels sharing a log wealth axis (never a dual y-axis): top =
marginal rate on the next euro; bottom = average rate (total tax / net wealth).
Geometry and curves come from the tested calculators in wealth_tax_es; the
marginal steps are cross-checked against numeric derivatives at every bracket
midpoint before plotting.

Outputs: results/mtr_by_wealth.png (standalone, titled) and
results/mtr_by_wealth_slide.png (untitled, larger type, for the deck).

Assumptions: individual filer; Spain = state schedule with the €700k general
exemption and NO abatements (no regional rebates, no main-residence exemption,
no IRPF–IP cap; the ITSGF then adds nothing — the IP schedule weakly dominates
it); Norway 2022 single filer, NOK→EUR at 10.10; Zurich single Grundtarif
× 2.18 Steuerfuss (canton 99% + City of Zurich 119%), CHF≈EUR; France IFI on
real-estate wealth only, including the €1.3M entry cliff and 1.3–1.4M décote;
Piketty as the paper implements it.
"""
import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FixedLocator, FuncFormatter, NullFormatter

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from wealth_tax_es import schedules as S  # noqa: E402
from wealth_tax_es.calculator import (  # noqa: E402
    ifi_liability,
    ip_liability,
    norway_liability,
    piketty_liability,
    zurich_liability,
)

NOK = S.NOK_PER_EUR_2022  # 10.10
STEUERFUSS = S.ZURICH_STEUERFUSS_CANTON + S.ZURICH_STEUERFUSS_CITY  # 2.18
X_MIN, X_MAX = 1e5, 5e7


def steps_from_schedule(schedule, exemption=0.0):
    return [(lo + exemption, rate) for lo, rate in schedule]


IP = steps_from_schedule(S.IP_STATE_SCHEDULE, S.IP_GENERAL_EXEMPTION)
NORWAY = [(S.NORWAY_2022["threshold_single"] / NOK, 0.0095), (20_000_000 / NOK, 0.011)]
ZURICH = [(lo, rate * STEUERFUSS) for lo, rate in S.ZURICH_GRUNDTARIF_SINGLE]
IFI = [(S.IFI_TRIGGER, 0.007 + 0.0125), (1_400_000.0, 0.007),
       (2_570_000.0, 0.010), (5_000_000.0, 0.0125), (10_000_000.0, 0.015)]
PIKETTY = list(S.PIKETTY_PAPER)

SERIES = [
    ("Spain IP (no abatements)", "#2a78d6", IP,
     lambda w: ip_liability(w, apply_rebate=False)),
    ("Piketty (paper variant)", "#eb6834", PIKETTY, piketty_liability),
    ("France IFI (real estate)", "#1baf7a", IFI, ifi_liability),
    ("Norway 2022", "#eda100", NORWAY,
     lambda w: norway_liability(w * NOK) / NOK),
    ("Zurich ×2.18 Steuerfuss", "#e87ba4", ZURICH,
     lambda w: zurich_liability(w, steuerfuss=STEUERFUSS)),
]


def crosscheck(steps, fn, name, eps=1.0):
    edges = [lo for lo, _ in steps] + [X_MAX]
    for (lo, rate), hi in zip(steps, edges[1:]):
        mid = np.sqrt(max(lo, 1.0) * hi)
        if mid <= lo or mid >= hi:
            mid = (lo + hi) / 2
        num = (fn(mid + eps) - fn(mid - eps)) / (2 * eps)
        assert abs(num - rate) < 1e-6, f"{name} @ {mid:,.0f}: analytic {rate} vs numeric {num}"


for name, _, steps, fn in SERIES:
    crosscheck(steps, fn, name)
print("cross-checks passed: analytic steps == tested calculator marginals")

W_GRID = np.geomspace(X_MIN, X_MAX, 600)


def render_mtr_only(out_path):
    base = 14
    fig, ax1 = plt.subplots(figsize=(12.8, 6.6), dpi=300)
    SURFACE = "#fcfcfb"
    fig.patch.set_facecolor(SURFACE)
    ax1.set_facecolor(SURFACE)
    ax1.grid(True, which="major", color="#e8e8e4", linewidth=0.8, zorder=0)
    for side in ("top", "right"):
        ax1.spines[side].set_visible(False)
    for side in ("left", "bottom"):
        ax1.spines[side].set_color("#c9c9c4")
    ax1.tick_params(colors="#6f6f6a", labelsize=base)
    ax1.yaxis.set_major_formatter(FuncFormatter(lambda v, _: f"{v:g}%"))
    ax1.set_xscale("log")
    ax1.set_xlim(X_MIN, X_MAX)
    for name, color, steps, _ in SERIES:
        xs, ys = [X_MIN], [0.0]
        for lo, rate in steps:
            if lo > X_MAX:
                continue
            xs += [max(lo, X_MIN), max(lo, X_MIN)]
            ys += [ys[-1], rate * 100]
        xs.append(X_MAX)
        ys.append(ys[-1])
        ax1.plot(xs, ys, color=color, linewidth=2.4, solid_joinstyle="miter", zorder=3)
    ax1.set_ylim(0, 3.7)
    ticks = [1e5, 3e5, 1e6, 3e6, 1e7, 3e7]
    ax1.xaxis.set_major_locator(FixedLocator(ticks))
    ax1.xaxis.set_major_formatter(FuncFormatter(
        lambda v, _: f"€{v/1e6:g}M" if v >= 1e6 else f"€{v/1e3:g}k"))
    ax1.xaxis.set_minor_formatter(NullFormatter())
    ends = {"Spain IP (no abatements)": 3.5, "Piketty (paper variant)": 2.0,
            "France IFI (real estate)": 1.5, "Norway 2022": 1.1,
            "Zurich ×2.18 Steuerfuss": 0.654}
    for name, color, *_ in SERIES:
        y = ends[name]
        ax1.annotate(name, xy=(X_MAX, y), xytext=(X_MAX * 1.07, y),
                     color="#3d3d3a", fontsize=base, va="center", annotation_clip=False)
        ax1.plot([X_MAX * 1.02], [y], marker="o", color=color, markersize=6,
                 clip_on=False, zorder=4)
    cliff = ifi_liability(S.IFI_TRIGGER + 1)
    ax1.annotate(f"IFI entry cliff: ≈€{cliff:,.0f} due at €1.3M",
                 xy=(1.32e6, 1.95), xytext=(2.3e5, 2.6),
                 fontsize=base - 2, color="#6f6f6a",
                 arrowprops=dict(arrowstyle="-", color="#b9b9b4", lw=1))
    fig.subplots_adjust(left=0.05, right=0.76, top=0.97, bottom=0.115)
    fig.text(0.05, 0.008,
             "Individual filer, 2022 statutes. Spain: €700k exemption only — no rebates, no residence exemption, no IRPF–IP cap. NOK→EUR 10.10; CHF≈EUR.",
             fontsize=11, color="#8a8a84", va="bottom")
    fig.savefig(out_path, facecolor=SURFACE)
    plt.close(fig)
    print(f"wrote {out_path}")


def render(out_path, slide=False):
    base = 13 if slide else 10.5
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12.5, 8.6), dpi=300,
                                   sharex=True, height_ratios=[1, 1])
    SURFACE = "#fcfcfb"
    fig.patch.set_facecolor(SURFACE)

    for ax in (ax1, ax2):
        ax.set_facecolor(SURFACE)
        ax.grid(True, which="major", color="#e8e8e4", linewidth=0.8, zorder=0)
        for side in ("top", "right"):
            ax.spines[side].set_visible(False)
        for side in ("left", "bottom"):
            ax.spines[side].set_color("#c9c9c4")
        ax.tick_params(colors="#6f6f6a", labelsize=base)
        ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: f"{v:g}%"))
        ax.set_xscale("log")
        ax.set_xlim(X_MIN, X_MAX)

    # top: marginal steps
    for name, color, steps, _ in SERIES:
        xs, ys = [X_MIN], [0.0]
        for lo, rate in steps:
            if lo > X_MAX:
                continue
            xs += [max(lo, X_MIN), max(lo, X_MIN)]
            ys += [ys[-1], rate * 100]
        xs.append(X_MAX)
        ys.append(ys[-1])
        ax1.plot(xs, ys, color=color, linewidth=2, solid_joinstyle="miter", zorder=3)
    ax1.set_ylim(0, 3.7)

    # bottom: average rate curves from the tested calculators
    for name, color, _, fn in SERIES:
        atr = np.array([fn(w) / w for w in W_GRID]) * 100
        ax2.plot(W_GRID, atr, color=color, linewidth=2, zorder=3)
    ax2.set_ylim(0, 3.2)

    for ax, panel in ((ax1, "Marginal rate (next euro)"), (ax2, "Average rate (total tax ÷ net wealth)")):
        ax.text(0.005, 0.96, panel, transform=ax.transAxes, fontsize=base + 1.5,
                fontweight="bold", color="#3d3d3a", va="top")

    ticks = [1e5, 3e5, 1e6, 3e6, 1e7, 3e7]
    ax2.xaxis.set_major_locator(FixedLocator(ticks))
    ax2.xaxis.set_major_formatter(FuncFormatter(
        lambda v, _: f"€{v/1e6:g}M" if v >= 1e6 else f"€{v/1e3:g}k"))
    ax2.xaxis.set_minor_formatter(NullFormatter())

    # direct labels: top panel = terminal marginals; bottom = terminal ATRs
    for ax, get_end in ((ax1, lambda nm, fn: dict((n, s[-1][1] * 100) for n, _, s, _ in SERIES)[nm]),
                        (ax2, lambda nm, fn: fn(X_MAX) / X_MAX * 100)):
        used = []
        for name, color, _, fn in SERIES:
            y = get_end(name, fn)
            for u in used:  # nudge collisions apart
                if abs(y - u) < 0.14:
                    y = u - 0.15
            used.append(y)
            ax.annotate(name, xy=(X_MAX, y), xytext=(X_MAX * 1.07, y),
                        color="#3d3d3a", fontsize=base, va="center",
                        annotation_clip=False)
            ax.plot([X_MAX * 1.02], [y], marker="o", color=color, markersize=5,
                    clip_on=False, zorder=4)

    cliff = ifi_liability(S.IFI_TRIGGER + 1)
    ax1.annotate(f"IFI entry cliff: ≈€{cliff:,.0f} due at €1.3M",
                 xy=(1.32e6, 1.95), xytext=(2.4e5, 2.55),
                 fontsize=base - 1, color="#6f6f6a",
                 arrowprops=dict(arrowstyle="-", color="#b9b9b4", lw=1))

    if slide:
        fig.subplots_adjust(left=0.055, right=0.775, top=0.975, bottom=0.075, hspace=0.12)
        fig.text(0.055, 0.008,
                 "Individual filer, 2022 statutes. Spain: €700k exemption only — no rebates, no residence exemption, no IRPF–IP cap. NOK→EUR 10.10; CHF≈EUR.",
                 fontsize=10, color="#8a8a84", va="bottom")
    else:
        fig.text(0.045, 0.965, "Statutory wealth-tax schedules: marginal and average rates",
                 fontsize=16, fontweight="bold", color="#1e1e1c")
        fig.text(0.045, 0.935, "By net wealth — individual filer, 2022 law, log wealth scale",
                 fontsize=11, color="#6f6f6a")
        fig.text(0.045, 0.008,
                 "Spain: state IP schedule, €700k general exemption, no regional rebates, no main-residence exemption, no IRPF–IP cap\n"
                 "(the ITSGF then adds nothing: the IP schedule weakly dominates it). Norway: 2022 single filer, NOK→EUR at 10.10. Zurich: single\n"
                 "Grundtarif × 2.18 Steuerfuss (canton 99% + City of Zurich 119%), CHF≈EUR. France: IFI, real-estate wealth only. Piketty: 0/0.5/1/2%\n"
                 "schedule as implemented by the paper. Source: statutes cited in replication/NOTES.md.",
                 fontsize=8.5, color="#8a8a84", va="bottom")
        fig.subplots_adjust(left=0.05, right=0.79, top=0.91, bottom=0.115, hspace=0.12)

    fig.savefig(out_path, facecolor=SURFACE)
    plt.close(fig)
    print(f"wrote {out_path}")




BUILD_ORDER = ["Zurich ×2.18 Steuerfuss", "Norway 2022", "France IFI (real estate)",
               "Piketty (paper variant)", "Spain IP (no abatements)"]
SHORT_NAMES = {"Zurich ×2.18 Steuerfuss": "Zurich", "Norway 2022": "Norway",
               "France IFI (real estate)": "France IFI", "Piketty (paper variant)": "Piketty",
               "Spain IP (no abatements)": "Spain IP"}


def render_buildup(out_path, upto):
    """Reveal slide k (1-based): series BUILD_ORDER[:upto], last one highlighted,
    earlier ones faded in place. Stacked MTR (top) and ATR (bottom), shared x."""
    base = 13
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(9.6, 8.2), dpi=300,
                                   sharex=True, height_ratios=[1, 1])
    SURFACE = "#fcfcfb"
    fig.patch.set_facecolor(SURFACE)
    shown = BUILD_ORDER[:upto]
    current = shown[-1]
    by_name = {name: (color, steps, fn) for name, color, steps, fn in SERIES}

    for ax in (ax1, ax2):
        ax.set_facecolor(SURFACE)
        ax.grid(True, which="major", color="#e8e8e4", linewidth=0.8, zorder=0)
        for side in ("top", "right"):
            ax.spines[side].set_visible(False)
        for side in ("left", "bottom"):
            ax.spines[side].set_color("#c9c9c4")
        ax.tick_params(colors="#6f6f6a", labelsize=base)
        ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: f"{v:g}%"))
        ax.set_xscale("log")
        ax.set_xlim(X_MIN, X_MAX)

    for name in shown:
        color, steps, fn = by_name[name]
        hot = name == current
        alpha, lw = (1.0, 2.8) if hot else (0.22, 2.0)
        xs, ys = [X_MIN], [0.0]
        for lo, rate in steps:
            if lo > X_MAX:
                continue
            xs += [max(lo, X_MIN), max(lo, X_MIN)]
            ys += [ys[-1], rate * 100]
        xs.append(X_MAX)
        ys.append(ys[-1])
        ax1.plot(xs, ys, color=color, linewidth=lw, alpha=alpha,
                 solid_joinstyle="miter", zorder=4 if hot else 2)
        atr = np.array([fn(w) / w for w in W_GRID]) * 100
        ax2.plot(W_GRID, atr, color=color, linewidth=lw, alpha=alpha,
                 zorder=4 if hot else 2)
        if hot:
            y1 = steps[-1][1] * 100
            ax1.annotate(SHORT_NAMES[name], xy=(X_MAX, y1), xytext=(X_MAX * 1.07, y1),
                         color="#3d3d3a", fontsize=base + 1, fontweight="bold",
                         va="center", annotation_clip=False)
            ax1.plot([X_MAX * 1.02], [y1], marker="o", color=color, markersize=6,
                     clip_on=False, zorder=5)
            y2 = fn(X_MAX) / X_MAX * 100
            ax2.plot([X_MAX * 1.02], [y2], marker="o", color=color, markersize=6,
                     clip_on=False, zorder=5)
    ax1.set_ylim(0, 3.7)
    ax2.set_ylim(0, 3.2)
    for ax, panel in ((ax1, "Marginal rate (next euro)"),
                      (ax2, "Average rate (total tax ÷ net wealth)")):
        ax.text(0.008, 0.95, panel, transform=ax.transAxes, fontsize=base + 1,
                fontweight="bold", color="#3d3d3a", va="top")
    ticks = [1e5, 1e6, 1e7]
    ax2.xaxis.set_major_locator(FixedLocator(ticks))
    ax2.xaxis.set_major_formatter(FuncFormatter(
        lambda v, _: f"€{v/1e6:g}M" if v >= 1e6 else f"€{v/1e3:g}k"))
    ax2.xaxis.set_minor_formatter(NullFormatter())
    fig.subplots_adjust(left=0.075, right=0.80, top=0.985, bottom=0.06, hspace=0.10)
    fig.savefig(out_path, facecolor=SURFACE)
    plt.close(fig)
    print(f"wrote {out_path}")


results = Path(__file__).resolve().parents[1] / "results"
render(results / "mtr_by_wealth.png", slide=False)
render_mtr_only(results / "mtr_by_wealth_slide.png")
for k in range(1, 6):
    render_buildup(results / f"schedule_build_{k}.png", k)
