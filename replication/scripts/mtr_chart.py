"""Six wealth-tax design paths related to the eight designs in Cantó &
García-Rodríguez (2026), ordered as in the paper's Tables 1 and A.2:

- Spanish IP baseline / the state-schedule reference later reused by Sim. 2.
- Sim. NO: the paper's flat 1% Norway variant after its ~EUR 160k threshold.
- Sim. CH: an illustrative Zurich City reference because the paper omits the
  tariff vintage and Steuerfuss.
- Sim. FR: France's real-estate-only IFI.
- Sims 1-3: the EUR 300k Spanish threshold line, alongside the baseline line.
- Sim. Piketty: the paper's normative schedule.

The x-axis is non-pension net wealth along one transparent illustrative
portfolio: 25% main residence and 75% other assets at every wealth level.
Each design's valuation rules are then applied to that same portfolio. This
is not an estimate of a representative Spanish household.

Underlying statutory schedules remain cross-checked against numeric
derivatives of the tested calculators at every bracket midpoint. Outputs:
  results/mtr_by_wealth.png        standalone two-panel (MTR + ATR), titled
  results/mtr_by_wealth_slide.png  recap slide chart (MTR only, untitled)
  results/schedule_build_{1..6}.png  reveal slides (MTR+ATR stacked, fade-in)
"""
import shutil
import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FixedLocator, FuncFormatter, NullFormatter, NullLocator

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from wealth_tax_es import schedules as S
from wealth_tax_es.calculator import (
    ifi_liability,
    ip_liability,
    norway_liability,
    piketty_liability,
    zurich_liability,
)
from wealth_tax_es.portfolio_paths import (
    CHF_PER_EUR_2022,
    RESIDENCE_SHARE,
    france_path,
    ip_path,
    norway_paper_path,
    portfolio,
    zurich_path,
)

NOK = S.NOK_PER_EUR_2022
STEUERFUSS = S.ZURICH_STEUERFUSS_CANTON + S.ZURICH_STEUERFUSS_CITY
X_MIN, X_MAX = 1e4, 1e8
SURFACE = "#fcfcfb"


def steps_from_schedule(schedule, exemption=0.0):
    return [(lo + exemption, rate) for lo, rate in schedule]


IP700 = steps_from_schedule(S.IP_STATE_SCHEDULE, S.IP_GENERAL_EXEMPTION)
IP300 = steps_from_schedule(S.IP_STATE_SCHEDULE, S.SIM1_EXEMPTION)
NORWAY_PAPER = [(S.NORWAY_PAPER_VARIANT["threshold_single"] / NOK, 0.010)]
ZURICH = [(lo, rate * STEUERFUSS) for lo, rate in S.ZURICH_GRUNDTARIF_SINGLE]
IFI = [(S.IFI_TRIGGER, 0.007 + 0.0125), (1_400_000.0, 0.007),
       (2_570_000.0, 0.010), (5_000_000.0, 0.0125), (10_000_000.0, 0.015)]
PIKETTY = list(S.PIKETTY_PAPER)

# (name, short, color, linestyle, liability along the common total-wealth path)
SERIES = [
    ("IP baseline / Sim. 2 ref.", "IP / Sim. 2", "#2a78d6", "solid",
     lambda w: ip_path(w, S.IP_GENERAL_EXEMPTION)),
    ("Sim. NO (paper)", "Sim. NO", "#eda100", "solid", norway_paper_path),
    ("Sim. CH (Zurich ref.)", "Sim. CH", "#e87ba4", "solid", zurich_path),
    ("Sim. FR (IFI)", "Sim. FR", "#1baf7a", "solid", france_path),
    ("Sims 1/3 (€300k ref.)", "Sims 1/3", "#2a78d6", (0, (5, 3)),
     lambda w: ip_path(w, S.SIM1_EXEMPTION)),
    ("Sim. Piketty", "Piketty", "#eb6834", "solid", piketty_liability),
]
BY_NAME = {r[0]: r for r in SERIES}
BUILD_ORDER = [r[0] for r in SERIES]
W_GRID = np.geomspace(X_MIN, X_MAX, 1_600)


def crosscheck(steps, fn, name, eps=1.0):
    edges = [lo for lo, _ in steps] + [X_MAX]
    for (lo, rate), hi in zip(steps, edges[1:]):
        mid = np.sqrt(max(lo, 1.0) * hi)
        if mid <= lo or mid >= hi:
            mid = (lo + hi) / 2
        num = (fn(mid + eps) - fn(mid - eps)) / (2 * eps)
        assert abs(num - rate) < 1e-6, f"{name} @ {mid:,.0f}: analytic {rate} vs numeric {num}"


CALCULATOR_CHECKS = [
    (IP700, lambda w: ip_liability(w, apply_rebate=False), "Spain EUR 700k"),
    (IP300,
     lambda w: ip_liability(w, exemption=S.SIM1_EXEMPTION, apply_rebate=False),
     "Spain EUR 300k"),
    (NORWAY_PAPER,
     lambda w: norway_liability(w * NOK, params=S.NORWAY_PAPER_VARIANT) / NOK,
     "Norway paper variant"),
    (ZURICH, lambda w: zurich_liability(w, steuerfuss=STEUERFUSS), "Zurich City"),
    (IFI, ifi_liability, "France IFI"),
    (PIKETTY, piketty_liability, "Piketty"),
]
for steps, fn, name in CALCULATOR_CHECKS:
    crosscheck(steps, fn, name)

assert sum(portfolio(1_000_000.0)) == 1_000_000.0
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
    ax.xaxis.set_minor_locator(NullLocator())
    ax.xaxis.set_minor_formatter(NullFormatter())


def marginal_rate(fn, wealth):
    """Central-difference MTR along the common total-wealth portfolio path."""
    eps = max(1.0, wealth * 1e-7)
    lo = max(0.0, wealth - eps)
    rate = (fn(wealth + eps) - fn(lo)) / (wealth + eps - lo) * 100
    # IFI has a discrete entry liability. Leave that discontinuity to the
    # annotation rather than drawing a meaningless near-infinite derivative.
    return np.nan if abs(rate) > 4.0 else max(0.0, rate)


def mtr_values(fn):
    return np.array([marginal_rate(fn, w) for w in W_GRID])


def line(ax, ys, color, ls, lw, alpha, z):
    ax.plot(W_GRID, ys, color=color, linestyle=ls, linewidth=lw, alpha=alpha,
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


def mtr_endpoint_labels():
    """Merge the coincident Spanish 3.5% endpoints into one truthful label."""
    ip_rate = marginal_rate(BY_NAME["IP baseline / Sim. 2 ref."][-1], X_MAX)
    entries = [(
        "IP baseline / Sim. 2 ref.\nSims 1/3 (€300k ref.)",
        "#2a78d6",
        ip_rate,
    )]
    entries.extend(
        (name, color, marginal_rate(fn, X_MAX))
        for name, _, color, _, fn in SERIES
        if name not in {"IP baseline / Sim. 2 ref.", "Sims 1/3 (€300k ref.)"}
    )
    return entries


def render_standalone(out_path):
    base = 10.5
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12.5, 8.6), dpi=300,
                                   sharex=True, height_ratios=[1, 1])
    fig.patch.set_facecolor(SURFACE)
    for ax in (ax1, ax2):
        style_axis(ax, base)
    for name, short, color, ls, fn in SERIES:
        line(ax1, mtr_values(fn), color, ls, 2, 1.0, 3)
        atr = np.array([fn(w) / w for w in W_GRID]) * 100
        line(ax2, atr, color, ls, 2, 1.0, 3)
    ax1.set_ylim(0, 3.7)
    ax2.set_ylim(0, 3.4)
    for ax, panel in ((ax1, "Marginal tax on next euro of net wealth"),
                      (ax2, "Average tax ÷ non-pension net wealth")):
        ax.text(0.005, 0.96, panel, transform=ax.transAxes, fontsize=base + 1.5,
                fontweight="bold", color="#3d3d3a", va="top")
    euro_ticks(ax2, [1e4, 1e5, 1e6, 1e7, 1e8])
    ax2.set_xlabel("Illustrative non-pension net wealth (log scale)",
                   fontsize=base, color="#6f6f6a")
    right_labels(ax1, mtr_endpoint_labels(), base)
    right_labels(ax2, [(sh, c, fn(X_MAX) / X_MAX * 100)
                       for _, sh, c, _, fn in SERIES], base)
    cliff = ifi_liability(S.IFI_TRIGGER + 1)
    ifi_trigger_wealth = S.IFI_TRIGGER / (
        (1.0 - S.IFI_MAIN_RESIDENCE_ABATEMENT) * RESIDENCE_SHARE
    )
    ax1.annotate(f"IFI entry: ≈€{cliff:,.0f} once 17.5% of wealth exceeds €1.3M",
                 xy=(ifi_trigger_wealth * 1.02, 0.34),
                 xytext=(1.1e6, 2.75), fontsize=base - 1,
                 color="#6f6f6a",
                 arrowprops={"arrowstyle": "-", "color": "#b9b9b4", "lw": 1})
    fig.text(0.045, 0.965, "Six design paths in the paper's order",
             fontsize=16, fontweight="bold", color="#1e1e1c")
    fig.text(0.045, 0.935, "Single filer; 25% main residence + 75% other assets; pension rights excluded.",
             fontsize=11, color="#6f6f6a")
    fig.text(0.045, 0.008,
             "Illustrative portfolio, not a representative household. Norway paper variant: housing valued at 25%, then flat 1% after ~€160k (double threshold for couples).\n"
             f"Zurich: housing at 70%; mixed-vintage 2026 tariff ×2.18 (2022–23 factors); ECB 2022 average €1=CHF{CHF_PER_EUR_2022:.4f}. France: residence only, 30% abatement.\n"
             "Spain: €300k residence relief; state schedules, no regional rebate or income cap. Piketty: full non-pension net wealth assumed; paper leaves its valuation base unresolved.\n"
             "Sources: Tables 1/A.2 + replication/NOTES.md.",
             fontsize=8.5, color="#8a8a84", va="bottom")
    fig.subplots_adjust(left=0.05, right=0.77, top=0.905, bottom=0.13, hspace=0.12)
    fig.savefig(out_path, facecolor=SURFACE)
    plt.close(fig)
    print(f"wrote {out_path}")


def render_recap_slide(out_path):
    base = 14
    fig, ax1 = plt.subplots(figsize=(12.8, 6.6), dpi=300)
    fig.patch.set_facecolor(SURFACE)
    style_axis(ax1, base)
    for name, short, color, ls, fn in SERIES:
        line(ax1, mtr_values(fn), color, ls, 2.4, 1.0, 3)
    ax1.set_ylim(0, 3.7)
    euro_ticks(ax1, [1e4, 1e5, 1e6, 1e7, 1e8])
    ax1.set_xlabel("Illustrative non-pension net wealth (log scale)",
                   fontsize=base, color="#6f6f6a")
    right_labels(ax1, mtr_endpoint_labels(), base, min_gap=0.2)
    fig.subplots_adjust(left=0.05, right=0.72, top=0.97, bottom=0.16)
    fig.text(0.05, 0.008,
             "Single filer; illustrative 25% main residence + 75% other assets; pensions excluded. Norway: paper's flat 1% after ~€160k, housing valued at 25%.\n"
             f"Zurich City: housing 70%, mixed-vintage ×2.18 reference; ECB 2022 average €1=CHF{CHF_PER_EUR_2022:.4f}. France: residence only with 30% abatement.\n"
             "Spain: residence relief shown; regional rules/cap omitted.",
             fontsize=9.5, color="#8a8a84", va="bottom")
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
        _, short, color, ls, fn = BY_NAME[name]
        hot = name == current
        alpha, lw = (1.0, 2.8) if hot else (0.22, 2.0)
        line(ax1, mtr_values(fn), color, ls, lw, alpha, 4 if hot else 2)
        atr = np.array([fn(w) / w for w in W_GRID]) * 100
        line(ax2, atr, color, ls, lw, alpha, 4 if hot else 2)
        if hot:
            y1 = marginal_rate(fn, X_MAX)
            ax1.annotate(short, xy=(X_MAX, y1), xytext=(X_MAX * 1.07, y1),
                         color="#3d3d3a", fontsize=base + 1, fontweight="bold",
                         va="center", annotation_clip=False)
            ax1.plot([X_MAX * 1.02], [y1], marker="o", color=color, markersize=6,
                     clip_on=False, zorder=5)
            ax2.plot([X_MAX * 1.02], [fn(X_MAX) / X_MAX * 100], marker="o",
                     color=color, markersize=6, clip_on=False, zorder=5)
    ax1.set_ylim(0, 3.7)
    ax2.set_ylim(0, 3.4)
    for ax, panel in ((ax1, "Marginal tax on next euro"),
                      (ax2, "Tax ÷ non-pension net wealth")):
        ax.text(0.008, 0.95, panel, transform=ax.transAxes, fontsize=base + 1,
                fontweight="bold", color="#3d3d3a", va="top")
    euro_ticks(ax2, [1e4, 1e5, 1e6, 1e7, 1e8])
    ax2.set_xlabel("Illustrative non-pension net wealth (log scale)",
                   fontsize=base, color="#6f6f6a")
    fig.subplots_adjust(left=0.075, right=0.83, top=0.985, bottom=0.085, hspace=0.10)
    fig.savefig(out_path, facecolor=SURFACE)
    plt.close(fig)
    print(f"wrote {out_path}")


results = Path(__file__).resolve().parents[1] / "results"
render_standalone(results / "mtr_by_wealth.png")
render_recap_slide(results / "mtr_by_wealth_slide.png")
for k in range(1, 7):
    render_buildup(results / f"schedule_build_{k}.png", k)

public = Path(__file__).resolve().parents[2] / "public" / "figures"
public.mkdir(parents=True, exist_ok=True)
assets = {results / "mtr_by_wealth_slide.png": public / "mtr-schedules.png"}
assets.update({
    results / f"schedule_build_{k}.png": public / f"schedule_build_{k}.png"
    for k in range(1, 7)
})
for source, target in assets.items():
    temporary = target.with_name(f".{target.name}.tmp")
    shutil.copy2(source, temporary)
    temporary.replace(target)
print(f"synced {len(assets)} slide assets to {public}")
