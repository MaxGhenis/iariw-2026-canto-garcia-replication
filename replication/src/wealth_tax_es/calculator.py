"""Liability calculators for the eight wealth-tax designs.

All functions take individual-level inputs in the tax's own currency and return the
annual liability. Valuation of the base (declared vs market values) is the caller's
choice — deliberately, because the paper leaves it ambiguous per scenario (REVIEW.md,
finding `valuation-base`).
"""

from . import schedules as S


def progressive_tax(base: float, schedule) -> float:
    """Tax from a marginal or statutory-anchor schedule on a nonnegative base.

    Rows may be ``(lower_bound, marginal_rate)`` or
    ``(lower_bound, quota_at_lower_bound, marginal_rate)``.  The latter mirrors
    statutes that publish a rounded cumulative-quota column.
    """
    if base <= 0:
        return 0.0
    if schedule and len(schedule[0]) == 3:
        for lo, quota, rate in reversed(schedule):
            if base >= lo:
                return quota + (base - lo) * rate
        return 0.0
    tax = 0.0
    for i, (lo, rate) in enumerate(schedule):
        hi = schedule[i + 1][0] if i + 1 < len(schedule) else float("inf")
        if base > lo:
            tax += (min(base, hi) - lo) * rate
        else:
            break
    return tax


# --- Spain ------------------------------------------------------------------


def ip_liability(
    net_wealth: float,
    main_residence_value: float = 0.0,
    exemption: float = S.IP_GENERAL_EXEMPTION,
    region: str | None = None,
    apply_rebate: bool = True,
    schedule=None,
) -> float:
    """Spanish IP under the state schedule with a regional bonificación if any.

    Regional own schedules/thresholds (Catalonia 500k & own scale, etc.) are not yet
    encoded — that is exactly the parameter appendix the paper should publish.
    """
    residence_exempt = min(main_residence_value, S.IP_MAIN_RESIDENCE_EXEMPTION)
    base = net_wealth - residence_exempt - exemption
    quota = progressive_tax(base, schedule or S.IP_STATE_SCHEDULE)
    if apply_rebate and region:
        quota *= 1.0 - S.REGIONAL_REBATES_2022.get(region.lower(), 0.0)
    return quota


def joint_limit(ip_quota: float, irpf_quota: float, irpf_taxable_base: float) -> float:
    """Art. 31 límite conjunto: reduce the IP quota so IP+IRPF <= 60% of the IRPF
    base, but never below 20% of the original IP quota."""
    excess = (ip_quota + irpf_quota) - S.IP_JOINT_LIMIT_SHARE * irpf_taxable_base
    if excess <= 0:
        return ip_quota
    reduction = min(excess, S.IP_JOINT_LIMIT_MAX_REDUCTION * ip_quota)
    return ip_quota - reduction


def itsgf_liability(
    net_wealth: float, ip_quota_paid: float = 0.0, main_residence_value: float = 0.0
) -> float:
    """Ley 38/2022 solidarity surcharge; credits the IP quota actually paid."""
    residence_exempt = min(main_residence_value, S.IP_MAIN_RESIDENCE_EXEMPTION)
    base = net_wealth - residence_exempt - S.ITSGF_EXEMPTION
    gross = progressive_tax(base, S.ITSGF_SCHEDULE)
    return max(0.0, gross - ip_quota_paid)


# --- Foreign designs --------------------------------------------------------


def norway_liability(
    taxable_wealth_nok: float, couple: bool = False, params=S.NORWAY_2022
) -> float:
    thr = params["threshold_couple"] if couple else params["threshold_single"]
    base = taxable_wealth_nok - thr
    if base <= 0:
        return 0.0
    # Norwegian brackets apply to wealth ABOVE the threshold at the rate of the
    # band the total wealth falls in (state component kinks at NOK 20M of wealth).
    sched = params.get("schedule_couple", params["schedule"]) if couple else params["schedule"]
    tax = 0.0
    for i, (lo, rate) in enumerate(sched):
        band_lo = max(lo, thr)
        band_hi = sched[i + 1][0] if i + 1 < len(sched) else float("inf")
        if taxable_wealth_nok > band_lo:
            tax += (min(taxable_wealth_nok, band_hi) - band_lo) * rate
    return tax


def norway_primary_residence_taxable(market_value_nok: float, year: int = 2022) -> float:
    """Skatteetaten valuation: 25% up to NOK 10M, excess at 50% (2022)."""
    kink = S.NORWAY_PRIMARY_RESIDENCE_KINK_NOK
    if market_value_nok <= kink:
        return market_value_nok * S.NORWAY_PRIMARY_RESIDENCE_DISCOUNT
    excess_rate = (
        S.NORWAY_PRIMARY_RESIDENCE_EXCESS_RATE_2022
        if year == 2022
        else S.NORWAY_PRIMARY_RESIDENCE_EXCESS_RATE_2023
    )
    return kink * S.NORWAY_PRIMARY_RESIDENCE_DISCOUNT + (market_value_nok - kink) * excess_rate


def zurich_liability(
    taxable_wealth_chf: float, married: bool = False, steuerfuss: float | None = None
) -> float:
    """2026-vintage Zurich comparator retained for the immutable paper oracle.

    ``steuerfuss=None`` returns the einfache Staatssteuer; pass e.g.
    ``0.99 + 1.19 = 2.18`` for canton plus City of Zurich.  Use
    :func:`zurich_liability_2022` for the law applicable to tax year 2022.
    """
    sched = S.ZURICH_GRUNDTARIF_MARRIED if married else S.ZURICH_GRUNDTARIF_SINGLE
    simple = progressive_tax(taxable_wealth_chf, sched)
    return simple * (steuerfuss if steuerfuss is not None else 1.0)


def zurich_liability_2022(
    taxable_wealth_chf: float, married: bool = False, steuerfuss: float | None = None
) -> float:
    """Zurich wealth tax under the § 47 tariff in force for tax year 2022."""
    sched = S.ZURICH_GRUNDTARIF_MARRIED_2022 if married else S.ZURICH_GRUNDTARIF_SINGLE_2022
    simple = progressive_tax(taxable_wealth_chf, sched)
    return simple * (steuerfuss if steuerfuss is not None else 1.0)


def ifi_liability(
    taxable_real_estate: float, income: float | None = None, other_income_taxes: float = 0.0
) -> float:
    """French IFI: liability only if taxable real estate > EUR 1.3M; schedule from
    EUR 800k; décote for 1.3–1.4M; optional 75%-of-income plafonnement."""
    if taxable_real_estate <= S.IFI_TRIGGER:
        return 0.0
    gross = progressive_tax(taxable_real_estate, S.IFI_SCHEDULE)
    if S.IFI_TRIGGER < taxable_real_estate < 1_400_000.0:
        gross -= max(0.0, 17_500.0 - 0.0125 * taxable_real_estate)
    if income is not None:
        cap = S.IFI_INCOME_CAP_SHARE * income
        excess = (gross + other_income_taxes) - cap
        if excess > 0:
            gross = max(0.0, gross - excess)
    return gross


def piketty_liability(net_wealth: float, schedule=S.PIKETTY_PAPER) -> float:
    return progressive_tax(net_wealth, schedule)
