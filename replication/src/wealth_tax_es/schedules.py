"""Statutory wealth-tax schedules for the eight designs in Cantó & García-Rodríguez (2026).

Every parameter here carries its primary source. Where the paper under-specifies a design
(Zurich multipliers, per-scenario valuation bases, Sim. 2 semantics), the ambiguity is
encoded as explicit variants rather than silently resolved — see replication/NOTES.md.

A "schedule" is a list of (lower_bound, marginal_rate) pairs over the taxable base after
exemptions, in ascending order; ``progressive_tax`` in calculator.py integrates it.
"""

# ---------------------------------------------------------------------------
# Spain — Impuesto sobre el Patrimonio, state default schedule
# Source: Ley 19/1991, art. 30.2 (consolidated), BOE-A-1991-14392.
# Each row is (lower bound, cuota at the lower bound, marginal rate).  The
# published cuota column is legally operative: deriving it by integrating the
# rounded bounds drifts by one cent at the two highest edges.
# ---------------------------------------------------------------------------
IP_STATE_SCHEDULE = [
    (0.0, 0.0, 0.002),
    (167_129.45, 334.26, 0.003),
    (334_252.88, 835.63, 0.005),
    (668_499.75, 2_506.86, 0.009),
    (1_336_999.51, 8_523.36, 0.013),
    (2_673_999.01, 25_904.35, 0.017),
    (5_347_998.03, 71_362.33, 0.021),
    (10_695_996.06, 183_670.29, 0.035),
]
IP_GENERAL_EXEMPTION = 700_000.0  # art. 28 (state default; regions may vary)
IP_MAIN_RESIDENCE_EXEMPTION = 300_000.0  # art. 4.Nueve
# Joint IRPF–IP limit, art. 31: IP + IRPF quotas capped at 60% of the sum of IRPF
# taxable bases; the reduction of the IP quota cannot exceed 80% (=> 20% minimum).
IP_JOINT_LIMIT_SHARE = 0.60
IP_JOINT_LIMIT_MAX_REDUCTION = 0.80

# 2022 regional 100%/partial rebates on the IP quota (bonificaciones).
# Madrid: standing 100% rebate (Decreto Legislativo 1/2010 tradition; suspended from
#   2023 by Ley 12/2023 while the ITSGF stands — outside the 2022 baseline).
# Andalusia: 100% from tax year 2022 (Decreto-ley 7/2022, BOJA 20 Sept 2022,
#   effects 1 Jan 2022). Galicia: 25% for 2022 (Ley 18/2021; 50% only from 2023).
REGIONAL_REBATES_2022 = {"madrid": 1.00, "andalucia": 1.00, "galicia": 0.25}

# ---------------------------------------------------------------------------
# Spain — ITSGF (Impuesto Temporal de Solidaridad de las Grandes Fortunas)
# Source: Ley 38/2022 art. 3 (BOE-A-2022-22684, consolidated). In force 29 Dec
# 2022; accrues each 31 December => first tax year 2022; extended by RDL 8/2023.
# IP quota actually paid is credited.
# ---------------------------------------------------------------------------
ITSGF_SCHEDULE = [
    (0.0, 0.0, 0.0),
    (3_000_000.0, 0.0, 0.017),
    (5_347_998.03, 39_915.97, 0.021),
    (10_695_996.06, 152_223.93, 0.035),
]
ITSGF_EXEMPTION = 700_000.0

# ---------------------------------------------------------------------------
# Norway — formuesskatt. Sources: Skatteetaten rate pages for 2022 and 2023.
# 2022: municipal 0.7% + state 0.25% (0.4% above NOK 20M) => 0.95% / 1.10%.
# 2023: municipal 0.7% + state 0.3% (0.4% above NOK 20M) => 1.00% / 1.10%.
# Threshold NOK 1.7M, doubled for jointly assessed couples.
# The paper's Sim. NO is a flat 1% (the 2023 combined sub-20M rate) with no top
# bracket — encoded as PAPER_VARIANT for comparability runs.
# ---------------------------------------------------------------------------
NOK_PER_EUR_2022 = 10.10  # ECB average 2022; used only for rough EUR conversions
NORWAY_2022 = {
    "threshold_single": 1_700_000.0,
    "threshold_couple": 3_400_000.0,
    "schedule": [(0.0, 0.0095), (20_000_000.0, 0.011)],
    "schedule_couple": [(0.0, 0.0095), (40_000_000.0, 0.011)],
    "municipal_rate_default": 0.007,
    "state_schedule": [(0.0, 0.0025), (20_000_000.0, 0.004)],
    "state_schedule_couple": [(0.0, 0.0025), (40_000_000.0, 0.004)],
}
NORWAY_2023 = {
    "threshold_single": 1_700_000.0,
    "threshold_couple": 3_400_000.0,
    "schedule": [(0.0, 0.010), (20_000_000.0, 0.011)],
    "schedule_couple": [(0.0, 0.010), (40_000_000.0, 0.011)],
    "municipal_rate_default": 0.007,
    "state_schedule": [(0.0, 0.003), (20_000_000.0, 0.004)],
    "state_schedule_couple": [(0.0, 0.003), (40_000_000.0, 0.004)],
}
NORWAY_PAPER_VARIANT = {
    "threshold_single": 1_700_000.0,
    "threshold_couple": 3_400_000.0,
    "schedule": [(0.0, 0.010)],
}
# Housing valuation (Skatteetaten): primary dwelling at 25% of market value up to
# NOK 10M, excess at 50% (2022) / 70% (2023+); secondary dwellings 95% (2022) /
# 100% (2023). The paper values ALL housing at 25%.
NORWAY_PRIMARY_RESIDENCE_DISCOUNT = 0.25
NORWAY_PRIMARY_RESIDENCE_KINK_NOK = 10_000_000.0
NORWAY_PRIMARY_RESIDENCE_EXCESS_RATE_2022 = 0.50
NORWAY_PRIMARY_RESIDENCE_EXCESS_RATE_2023 = 0.70
NORWAY_SECONDARY_RESIDENCE_RATE_2022 = 0.95
NORWAY_SECONDARY_RESIDENCE_RATE_2023 = 1.00
NORWAY_SHARE_RATE_2022 = 0.75
NORWAY_SHARE_RATE_2023 = 0.80


# ---------------------------------------------------------------------------
# Zurich — Vermögenssteuer Grundtarif, § 47 StG ZH.
# Source for 2022: official historical StG ZH, Nachtrag 115, § 47.  Source for
# 2026: ESTV Kantonsblatt Zürich (estv2.admin.ch/stp/kb/zh-de.pdf), indexed
# edition ("Gültig ab Steuerperiode 2026").  Both tables print bracket widths.
# The immutable paper-replication oracle used the 2026 table, so that vintage is
# retained under the historical public names; the 2022 law has explicit names.
# ---------------------------------------------------------------------------
def _widths_to_schedule(widths):
    """[(width, rate), ...] -> [(lower_bound, rate), ...]"""
    out, lo = [], 0.0
    for width, rate in widths:
        out.append((lo, rate))
        lo += width
    return out


ZURICH_GRUNDTARIF_SINGLE_2022 = _widths_to_schedule(
    [
        (77_000.0, 0.0000),
        (231_000.0, 0.0005),
        (386_000.0, 0.0010),
        (616_000.0, 0.0015),
        (925_000.0, 0.0020),
        (923_000.0, 0.0025),
    ]
) + [(3_158_000.0, 0.0030)]
ZURICH_GRUNDTARIF_MARRIED_2022 = _widths_to_schedule(
    [
        (154_000.0, 0.0000),
        (231_000.0, 0.0005),
        (385_000.0, 0.0010),
        (616_000.0, 0.0015),
        (925_000.0, 0.0020),
        (924_000.0, 0.0025),
    ]
) + [(3_235_000.0, 0.0030)]
ZURICH_GRUNDTARIF_SINGLE_2026 = _widths_to_schedule(
    [
        (81_000.0, 0.0000),
        (241_000.0, 0.0005),
        (404_000.0, 0.0010),
        (645_000.0, 0.0015),
        (968_000.0, 0.0020),
        (965_000.0, 0.0025),
    ]
) + [(3_304_000.0, 0.0030)]
ZURICH_GRUNDTARIF_MARRIED_2026 = _widths_to_schedule(
    [
        (161_000.0, 0.0000),
        (242_000.0, 0.0005),
        (402_000.0, 0.0010),
        (646_000.0, 0.0015),
        (967_000.0, 0.0020),
        (967_000.0, 0.0025),
    ]
) + [(3_385_000.0, 0.0030)]
# Backwards-compatible names used by the unchanged 2026-vintage paper oracle.
ZURICH_GRUNDTARIF_SINGLE = ZURICH_GRUNDTARIF_SINGLE_2026
ZURICH_GRUNDTARIF_MARRIED = ZURICH_GRUNDTARIF_MARRIED_2026
ZURICH_STEUERFUSS_CANTON = 0.99  # zh.ch, 2022-23
ZURICH_STEUERFUSS_CITY = 1.19  # City of Zurich
ZURICH_REAL_ESTATE_FACTOR = 0.70  # paper p.10: real estate at 70% of market value

# ---------------------------------------------------------------------------
# France — IFI. Sources: service-public.fr fiche F563 (trigger EUR 1.3M; 30%
# main-residence abatement); impots.gouv.fr barème (schedule from EUR 800k;
# décote for 1.3–1.4M; 75% income cap). Mid-bracket edges below follow the
# published CGI art. 977 barème; flagged in NOTES.md for a line-by-line check.
# ---------------------------------------------------------------------------
IFI_TRIGGER = 1_300_000.0
IFI_SCHEDULE = [
    (0.0, 0.0),
    (800_000.0, 0.005),
    (1_300_000.0, 0.007),
    (2_570_000.0, 0.010),
    (5_000_000.0, 0.0125),
    (10_000_000.0, 0.015),
]
IFI_MAIN_RESIDENCE_ABATEMENT = 0.30
IFI_INCOME_CAP_SHARE = 0.75  # plafonnement: IFI + income taxes <= 75% of income

# ---------------------------------------------------------------------------
# Piketty schedule as implemented by the paper (Table 2 / A.2): 0% below 200k,
# 0.5% to 1M, 1% to 5M, 2% above. Piketty (2014, ch. 15) variants also include
# 0.1% below 200k and 5–10% on the largest fortunes — paper drops both ends.
# ---------------------------------------------------------------------------
PIKETTY_PAPER = [(0.0, 0.0), (200_000.0, 0.005), (1_000_000.0, 0.01), (5_000_000.0, 0.02)]
PIKETTY_BOOK_VARIANT = [(0.0, 0.001), (200_000.0, 0.005), (1_000_000.0, 0.01), (5_000_000.0, 0.02)]

# Paper reform scenarios (Sec. 4.2): threshold changes on the IP.
SIM1_EXEMPTION = 300_000.0  # Sim. 1: general exemption cut to EUR 300k
SIM2_REMOVE_REBATES = True  # Sim. 2: regional bonificaciones removed (per the
# authors' overlap matrix, thresholds/scales stay regional)
