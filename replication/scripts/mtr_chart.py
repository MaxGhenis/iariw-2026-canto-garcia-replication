"""Statutory wealth-tax schedules for ALL EIGHT designs in Cantó &
García-Rodríguez (2026), drawn as six lines with the coincidences named:

- Spain IP, €700k exemption  ≡ Sim. 2 in this un-abated view (Sim. 2 removes
  regional rebates, which this rendering already strips).
- Spain IP, €300k exemption  ≡ Sims 1 & 3 (they differ only in rebates).
- Zurich (Sim. CH), Norway (Sim. NO; true 2022 statute — the paper uses a flat
  1% variant), France IFI (Sim. FR), Piketty.

Marginal steps are cross-checked against numeric derivatives of the tested
calculators at every bracket midpoint before plotting. Outputs:
  results/mtr_by_wealth.png        standalone two-panel (MTR + ATR), titled
  results/mtr_by_wealth_slide.png  recap slide chart (MTR only, untitled)
  results/schedule_build_{1..6}.png  reveal slides (MTR+ATR stacked, fade-in)
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

NOK = S.NOK_PER_EUR_2022
STEUERFUSS = S.ZURICH_STEUERFUSS_CANTON + S.ZURICH_STEUERFUSS_CITY
X_MIN, X_MAX = 1e5, 5e7
SURFACE = "#fcfcfb"


def steps_from_schedule(schedule, exemption=0.0):
    return [(lo + exemption, rate) for lo, rate in schedule]


IP700 = steps_from_schedule(S.IP_STATE_SCHEDULE, S.IP_GENERAL_EXEMPTION)
IP300 = steps_from_schedule(S.IP_STATE_SCHEDULE, S.SIM1_EXEMPTION)
NORWAY = [(S.NORWAY_2022["threshold_single"] / NOK, 0.0095), (20_000_000 / NOK, 0.011)]
ZURICH = [(lo, rate * STEUERFUSS) for lo, rate in S.ZURICH_GRUNDTARIF_SINGLE]
IFI = [(S.IFI_TRIGGER, 0.007 + 0.0125), (1_400_000.0, 0.007),
       (2_570_000.0, 0.010), (5_000_000.0, 0.0125), (10_000_000.0, 0.015)]
PIKETTY = list(S.PIKETTY_PAPER)

# (name, short, color, linestyle, steps, liability_fn)
SERIES = [
    ("Spain IP €700k (≡ Sim. 2)", "Spain IP €700k", "#2a78d6", "solid", IP700,
     lambda w: ip_liability(w, apply_rebate=False)),
    ("Spain €300k (Sims 1 & 3)", "Spain €300k", "#2a78d6", (0, (5, 3)), IP300,
     lambda w: ip_liability(w, exemption=S.SIM1_EXEMPTION, apply_rebate=False)),
    ("Piketty (paper variant)", "Piketty", "#eb6834", "solid", PIKETTY, piketty_liability),
    ("France IFI (Sim. FR)", "France IFI", "#1baf7a", "solid", IFI, ifi_liability),
    ("Norway 2022 (Sim. NO)", "Norway", "#eda100", "solid", NORWAY,
     lambda w: norway_liability(w * NOK) / NOK),
    ("Zurich ×2.18 (Sim. CH)", "Zurich", "#e87ba4", "solid", ZURICH,
     lambda w: zurich_liability(w, steuerfuss=STEUERFUSS)),
]
BY_NAME = {r[0]: r for r in SERIES}
BUILD_ORDER = ["Spain IP €700k (≡ Sim. 2)", "Spain €300k (Sims 1 & 3)",
               "Zurich ×2.18 (Sim. CH)", "Norway 2022 (Sim. NO)",
               "France IFI (Sim. FR)", "Piketty (paper variant)"]
W_GRID = np.geomspace(X_MIN, X_MAX, 600)


def crosscheck(steps, fn, name, eps=1.0):
    edges = [lo for lo, _ in steps] + [X_MAX]
    for (lo, rate), hi in zip(steps, edges[1:]):
        mid = np.sqrt(max(lo, 1.0) * hi)
        if mid <= lo or mid >= hi:
            mid = (lo + hi) / 2
        num = (fn(mid + eps) - fn(mid - eps)) / (2 * eps)
        assert abs(num - rate) < 1e-6, f"{name} @ {mid:,.0f}: analytic {rate} vs numeric {num}"


for name, _, _, _, steps, fn in SERIES:
    crosscheck(steps, fn, name)
print("cross-checks passed: analytic steps == tested calculator marginals (6 series)")


def style_axis(ax, base):
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


def euro_ticks(ax, ticks):
    ax.xaxis.set_major_locator(FixedLocator(ticks))
    ax.xaxis.set_major_formatter(FuncFormatter(
        lambda v, _: f"€{v/1e6:g}M" if v >= 1e6 else f"€{v/1e3:g}k"))
    ax.xaxis.set_minor_formatter(NullFormatter())


def mtr_line(ax, steps, color, ls, lw, alpha, z):
    xs, ys = [X_MIN], [0.0]
    for lo, rate in steps:
        if lo > X_MAX:
            continue
        xs += [max(lo, X_MIN), max(lo, X_MIN)]
        ys += [ys[-1], rate * 100]
    xs.append(X_MAX)
    ys.append(ys[-1])
    ax.plot(xs, ys, color=color, linestyle=ls, linewidth=lw, alpha=alpha,
            solid_joinstyle="miter", zorder=z)


def right_labels(ax, entries, base, min_gap=0.16):
    """entries: [(text, color, y)] — nudge collisions downward, draw dot+text."""
    placed = []
    for text, color, y in sorted(entries, key=lambda e: -e[2]):
        yy = y
        for u in placed:
            if abs(yy - u) < min_gap:
                yy = u - min_gap
        placed.append(yy)
        ax.annotate(text, xy=(X_MAX, y), xytext=(X_MAX * 1.07, yy),
                    color="#3d3d3a", fontsize=base, va="center", annotation_clip=False)
        ax.plot([X_MAX * 1.02], [y], marker="o", color=color, markersize=5,
                clip_on=False, zorder=5)


def render_standalone(out_path):
    base = 10.5
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12.5, 8.6), dpi=300,
                                   sharex=True, height_ratios=[1, 1])
    fig.patch.set_facecolor(SURFACE)
    for ax in (ax1, ax2):
        style_axis(ax, base)
    for name, short, color, ls, steps, fn in SERIES:
        mtr_line(ax1, steps, color, ls, 2, 1.0, 3)
        atr = np.array([fn(w) / w for w in W_GRID]) * 100
        ax2.plot(W_GRID, atr, color=color, linestyle=ls, linewidth=2, zorder=3)
    ax1.set_ylim(0, 3.7)
    ax2.set_ylim(0, 3.4)
    for ax, panel in ((ax1, "Marginal rate (next euro)"),
                      (ax2, "Average rate (total tax ÷ net wealth)")):
        ax.text(0.005, 0.96, panel, transform=ax.transAxes, fontsize=base + 1.5,
                fontweight="bold", color="#3d3d3a", va="top")
    euro_ticks(ax2, [1e5, 3e5, 1e6, 3e6, 1e7, 3e7])
    right_labels(ax1, [(n, c, s[-1][1] * 100) for n, _, c, _, s, _ in SERIES], base)
    right_labels(ax2, [(sh, c, fn(X_MAX) / X_MAX * 100) for _, sh, c, _, _, fn in SERIES], base)
    cliff = ifi_liability(S.IFI_TRIGGER + 1)
    ax1.annotate(f"IFI entry cliff: ≈€{cliff:,.0f} due at €1.3M",
                 xy=(1.32e6, 1.95), xytext=(2.3e5, 2.6), fontsize=base - 1,
                 color="#6f6f6a", arrowprops=dict(arrowstyle="-", color="#b9b9b4", lw=1))
    fig.text(0.045, 0.965, "Statutory wealth-tax schedules: all eight designs, six lines",
             fontsize=16, fontweight="bold", color="#1e1e1c")
    fig.text(0.045, 0.935, "By net wealth — individual filer, 2022 law, log scale. "
             "Spain un-abated: €700k line ≡ Sim. 2; €300k line ≡ Sims 1 & 3.",
             fontsize=11, color="#6f6f6a")
    fig.text(0.045, 0.008,
             "Spain: state IP schedule, no regional rebates, no main-residence exemption, no IRPF–IP cap (the ITSGF then adds nothing).\n"
             "Norway: true 2022 statute (0.95%/1.10%; the paper's Sim. NO uses flat 1%), NOK→EUR 10.10. Zurich: single Grundtarif × 2.18\n"
             "Steuerfuss (canton 99% + City of Zurich 119%), CHF≈EUR. France: IFI, real-estate wealth only. Piketty: 0/0.5/1/2% as in the paper.\n"
             "Source: statutes cited in replication/NOTES.md.",
             fontsize=8.5, color="#8a8a84", va="bottom")
    fig.subplots_adjust(left=0.05, right=0.77, top=0.905, bottom=0.115, hspace=0.12)
    fig.savefig(out_path, facecolor=SURFACE)
    plt.close(fig)
    print(f"wrote {out_path}")


def render_recap_slide(out_path):
    base = 14
    fig, ax1 = plt.subplots(figsize=(12.8, 6.6), dpi=300)
    fig.patch.set_facecolor(SURFACE)
    style_axis(ax1, base)
    for name, short, color, ls, steps, fn in SERIES:
        mtr_line(ax1, steps, color, ls, 2.4, 1.0, 3)
    ax1.set_ylim(0, 3.7)
    euro_ticks(ax1, [1e5, 3e5, 1e6, 3e6, 1e7, 3e7])
    right_labels(ax1, [(n, c, s[-1][1] * 100) for n, _, c, _, s, _ in SERIES], base, min_gap=0.2)
    cliff = ifi_liability(S.IFI_TRIGGER + 1)
    ax1.annotate(f"IFI entry cliff: ≈€{cliff:,.0f} due at €1.3M",
                 xy=(1.32e6, 1.95), xytext=(2.3e5, 2.6), fontsize=base - 2,
                 color="#6f6f6a", arrowprops=dict(arrowstyle="-", color="#b9b9b4", lw=1))
    fig.subplots_adjust(left=0.05, right=0.72, top=0.97, bottom=0.115)
    fig.text(0.05, 0.008,
             "Individual filer, 2022 statutes; marginal rate on the next euro. Spain un-abated: solid ≡ Sim. 2, dashed ≡ Sims 1 & 3. NOK→EUR 10.10; CHF≈EUR.",
             fontsize=11, color="#8a8a84", va="bottom")
    fig.savefig(out_path, facecolor=SURFACE)
    plt.close(fig)
    print(f"wrote {out_path}")


def render_buildup(out_path, upto):
    base = 13
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(9.6, 8.2), dpi=300,
                                   sharex=True, height_ratios=[1, 1])
    fig.patch.set_facecolor(SURFACE)
    for ax in (ax1, ax2):
        style_axis(ax, base)
    shown = BUILD_ORDER[:upto]
    current = shown[-1]
    for name in shown:
        _, short, color, ls, steps, fn = BY_NAME[name]
        hot = name == current
        alpha, lw = (1.0, 2.8) if hot else (0.22, 2.0)
        mtr_line(ax1, steps, color, ls, lw, alpha, 4 if hot else 2)
        atr = np.array([fn(w) / w for w in W_GRID]) * 100
        ax2.plot(W_GRID, atr, color=color, linestyle=ls, linewidth=lw, alpha=alpha,
                 zorder=4 if hot else 2)
        if hot:
            y1 = steps[-1][1] * 100
            ax1.annotate(short, xy=(X_MAX, y1), xytext=(X_MAX * 1.07, y1),
                         color="#3d3d3a", fontsize=base + 1, fontweight="bold",
                         va="center", annotation_clip=False)
            ax1.plot([X_MAX * 1.02], [y1], marker="o", color=color, markersize=6,
                     clip_on=False, zorder=5)
            ax2.plot([X_MAX * 1.02], [fn(X_MAX) / X_MAX * 100], marker="o",
                     color=color, markersize=6, clip_on=False, zorder=5)
    ax1.set_ylim(0, 3.7)
    ax2.set_ylim(0, 3.4)
    for ax, panel in ((ax1, "Marginal rate (next euro)"),
                      (ax2, "Average rate (total tax ÷ net wealth)")):
        ax.text(0.008, 0.95, panel, transform=ax.transAxes, fontsize=base + 1,
                fontweight="bold", color="#3d3d3a", va="top")
    euro_ticks(ax2, [1e5, 1e6, 1e7])
    fig.subplots_adjust(left=0.075, right=0.83, top=0.985, bottom=0.06, hspace=0.10)
    fig.savefig(out_path, facecolor=SURFACE)
    plt.close(fig)
    print(f"wrote {out_path}")


results = Path(__file__).resolve().parents[1] / "results"
render_standalone(results / "mtr_by_wealth.png")
render_recap_slide(results / "mtr_by_wealth_slide.png")
for k in range(1, 7):
    render_buildup(results / f"schedule_build_{k}.png", k)
