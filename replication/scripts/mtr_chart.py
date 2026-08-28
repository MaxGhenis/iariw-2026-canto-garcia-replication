"""Marginal wealth-tax rate by net wealth, for the five real tax systems in
Cantó & García-Rodríguez (2026).

Geometry is derived from the schedule constants in wealth_tax_es.schedules and
cross-checked numerically against the calculator functions at every bracket
midpoint before plotting — the chart cannot drift from the tested engine.

Assumptions (printed on the chart): individual filer; Spain = state schedule
with the €700k general exemption and NO abatements (no regional rebates, no
main-residence exemption, no IRPF–IP cap; the ITSGF then adds nothing — the IP
schedule weakly dominates it); Norway 2022 single filer, NOK→EUR at 10.10;
Zurich single Grundtarif × 2.18 Steuerfuss (canton 99% + city 119%), CHF≈EUR;
France IFI on real-estate wealth only, including the €1.3M entry cliff and the
1.3–1.4M décote band; Piketty as the paper implements it.
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
X_MAX = 5e7


def steps_from_schedule(schedule, exemption=0.0):
    """[(wealth_edge, marginal_rate), ...] for a base schedule shifted by an exemption."""
    return [(lo + exemption, rate) for lo, rate in schedule]


# --- exact step geometry per tax (wealth domain, EUR) ---
IP = steps_from_schedule(S.IP_STATE_SCHEDULE, S.IP_GENERAL_EXEMPTION)
NORWAY = [(S.NORWAY_2022["threshold_single"] / NOK, 0.0095), (20_000_000 / NOK, 0.011)]
ZURICH = [(lo, rate * STEUERFUSS) for lo, rate in S.ZURICH_GRUNDTARIF_SINGLE]
# IFI true marginal: zero below the trigger; décote adds 1.25pp in 1.3–1.4M.
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
    """Assert analytic marginal == numeric derivative of the tested calculator
    at every bracket midpoint (skipping the sub-exemption zero segment)."""
    edges = [lo for lo, _ in steps] + [X_MAX]
    for (lo, rate), hi in zip(steps, edges[1:]):
        mid = np.sqrt(max(lo, 1.0) * hi)  # geometric midpoint of the bracket
        if mid <= lo or mid >= hi:
            mid = (lo + hi) / 2
        num = (fn(mid + eps) - fn(mid - eps)) / (2 * eps)
        assert abs(num - rate) < 1e-6, f"{name} @ {mid:,.0f}: analytic {rate} vs numeric {num}"


for name, _, steps, fn in SERIES:
    crosscheck(steps, fn, name)
print("cross-checks passed: analytic steps == tested calculator marginals")

# --- draw ---
fig, ax = plt.subplots(figsize=(12.5, 7.0), dpi=300)
SURFACE = "#fcfcfb"
fig.patch.set_facecolor(SURFACE)
ax.set_facecolor(SURFACE)

for name, color, steps, _ in SERIES:
    xs, ys = [1e5], [0.0]
    for lo, rate in steps:
        if lo > X_MAX:
            continue
        xs += [max(lo, 1e5), max(lo, 1e5)]
        ys += [ys[-1], rate * 100]
    xs.append(X_MAX)
    ys.append(ys[-1])
    ax.plot(xs, ys, color=color, linewidth=2, solid_joinstyle="miter", zorder=3)

# direct labels at the right edge (nudged apart)
END_LABELS = {"Spain IP (no abatements)": (3.5, 0), "Piketty (paper variant)": (2.0, 0),
              "France IFI (real estate)": (1.5, 0.06), "Norway 2022": (1.1, -0.06),
              "Zurich ×2.18 Steuerfuss": (0.654, 0)}
for name, color, *_ in SERIES:
    y, dy = END_LABELS[name]
    ax.annotate(name, xy=(X_MAX, y), xytext=(X_MAX * 1.06, y + dy),
                color="#3d3d3a", fontsize=10.5, va="center",
                annotation_clip=False)
    ax.plot([X_MAX * 1.01], [y], marker="o", color=color, markersize=5,
            clip_on=False, zorder=4)

# IFI entry cliff annotation (exact jump from the tested calculator)
cliff = ifi_liability(S.IFI_TRIGGER + 1)
ax.annotate(f"IFI entry cliff: ≈€{cliff:,.0f} due\nat €1.3M (then décote to €1.4M)",
            xy=(1.3e6, 1.95), xytext=(2.6e5, 2.6),
            fontsize=9.5, color="#6f6f6a",
            arrowprops=dict(arrowstyle="-", color="#b9b9b4", lw=1))

ax.set_xscale("log")
ax.set_xlim(1e5, X_MAX)
ax.set_ylim(0, 3.7)
ticks = [1e5, 3e5, 1e6, 3e6, 1e7, 3e7]
ax.xaxis.set_major_locator(FixedLocator(ticks))
ax.xaxis.set_major_formatter(FuncFormatter(
    lambda v, _: f"€{v/1e6:g}M" if v >= 1e6 else f"€{v/1e3:g}k"))
ax.xaxis.set_minor_formatter(NullFormatter())
ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: f"{v:g}%"))
ax.grid(True, which="major", color="#e8e8e4", linewidth=0.8, zorder=0)
for side in ("top", "right"):
    ax.spines[side].set_visible(False)
for side in ("left", "bottom"):
    ax.spines[side].set_color("#c9c9c4")
ax.tick_params(colors="#6f6f6a", labelsize=10.5)

fig.text(0.045, 0.955, "Marginal wealth-tax rates by net wealth",
         fontsize=16, fontweight="bold", color="#1e1e1c")
fig.text(0.045, 0.915, "Statutory marginal rate on the next euro of net wealth — "
         "individual filer, 2022 law, log wealth scale", fontsize=11, color="#6f6f6a")
fig.text(0.045, 0.012,
         "Spain: state IP schedule, €700k general exemption, no regional rebates, no main-residence exemption, no IRPF–IP cap\n"
         "(the ITSGF then adds nothing: the IP schedule weakly dominates it). Norway: 2022 single filer, NOK→EUR at 10.10. Zurich: single\n"
         "Grundtarif × 2.18 Steuerfuss (canton 99% + City of Zurich 119%), CHF≈EUR. France: IFI, real-estate wealth only. Piketty: 0/0.5/1/2%\n"
         "schedule as implemented by the paper. Source: statutes cited in replication/NOTES.md.",
         fontsize=8.5, color="#8a8a84", va="bottom")

ax.legend(handles=[plt.Line2D([], [], color=c, lw=2, label=n) for n, c, *_ in SERIES],
          loc="upper left", frameon=False, fontsize=10)

fig.subplots_adjust(left=0.06, right=0.82, top=0.87, bottom=0.16)
out = Path(__file__).resolve().parents[1] / "results" / "mtr_by_wealth.png"
fig.savefig(out, facecolor=SURFACE)
print(f"wrote {out}")
