"""Hand-computed anchor tests for every encoded schedule.

The Spanish IP anchors are the cuota íntegra column of Ley 19/1991 art. 30.2 as
published in the BOE consolidated text — if these pass, the bracket encoding is
exactly the statutory table.
"""
import pytest

from wealth_tax_es import schedules as S
from wealth_tax_es.calculator import (
    ifi_liability,
    ip_liability,
    itsgf_liability,
    joint_limit,
    norway_liability,
    norway_primary_residence_taxable,
    piketty_liability,
    progressive_tax,
    zurich_liability,
)
from wealth_tax_es.portfolio_paths import (
    CHF_PER_EUR_2022,
    france_path,
    ip_path,
    norway_paper_path,
    portfolio,
    zurich_path,
)

# BOE art. 30.2 anchor points: (base liquidable, cuota íntegra)
IP_ANCHORS = [
    (167_129.45, 334.26),
    (334_252.88, 835.63),
    (668_499.75, 2_506.86),
    (1_336_999.51, 8_523.36),
    (2_673_999.01, 25_904.35),
    (5_347_998.03, 71_362.33),
    (10_695_996.06, 183_670.29),
]


@pytest.mark.parametrize("base,cuota", IP_ANCHORS)
def test_ip_state_schedule_matches_boe_anchors(base, cuota):
    assert progressive_tax(base, S.IP_STATE_SCHEDULE) == pytest.approx(cuota, abs=0.02)


def test_ip_liability_with_exemptions():
    # Net wealth 1.5M, residence worth 400k (capped at 300k), 700k general exemption
    # -> base 500k -> 835.63 + (500,000-334,252.88)*0.005 = 1,664.37
    assert ip_liability(1_500_000, main_residence_value=400_000) == pytest.approx(1_664.37, abs=0.02)


def test_ip_madrid_rebate_zeroes_quota():
    assert ip_liability(5_000_000, region="madrid") == 0.0
    assert ip_liability(5_000_000, region="madrid", apply_rebate=False) > 0


def test_joint_limit_60_with_20_floor():
    # IP 100k, IRPF 50k, IRPF base 100k: cap = 60k; excess = 90k; max reduction 80k
    assert joint_limit(100_000, 50_000, 100_000) == pytest.approx(20_000)
    # Non-binding case unchanged
    assert joint_limit(1_000, 10_000, 1_000_000) == 1_000


def test_itsgf_hand_computed():
    # Net 5M, no residence: base 4.3M -> 1.7% on 1.3M above the 3M zero band = 22,100
    assert itsgf_liability(5_000_000) == pytest.approx(22_100, abs=0.01)
    # IP paid is credited
    assert itsgf_liability(5_000_000, ip_quota_paid=22_100) == 0.0
    # Effective floor ~3.7M: nothing due at 3.6M net
    assert itsgf_liability(3_600_000) == 0.0


def test_itsgf_top_bracket_edges_match_ip():
    assert S.ITSGF_SCHEDULE[2][0] == S.IP_STATE_SCHEDULE[6][0]
    assert S.ITSGF_SCHEDULE[3][0] == S.IP_STATE_SCHEDULE[7][0]


def test_norway_2022_two_brackets():
    # Single, 25M NOK taxable: 0.95% on (20M-1.7M) + 1.1% on 5M = 173,850 + 55,000
    assert norway_liability(25_000_000) == pytest.approx(228_850)
    # Below threshold: zero
    assert norway_liability(1_600_000) == 0.0
    # Couples: doubled threshold
    assert norway_liability(3_000_000, couple=True) == 0.0


def test_norway_paper_variant_flat_1pct():
    assert norway_liability(2_700_000, params=S.NORWAY_PAPER_VARIANT) == pytest.approx(10_000)
    # Unlike 2022 law, the paper keeps the same 1% rate above NOK 20M.
    assert norway_liability(25_000_000, params=S.NORWAY_PAPER_VARIANT) == pytest.approx(233_000)


def test_norway_residence_valuation_kink():
    assert norway_primary_residence_taxable(8_000_000) == pytest.approx(2_000_000)
    # 15M home: 25% of 10M + 50% of 5M = 5.0M (Skatteetaten worked example: taxable 5M)
    assert norway_primary_residence_taxable(15_000_000) == pytest.approx(5_000_000)


def test_zurich_single_hand_computed():
    # 500k CHF: 0 on 81k + 0.5 permille on 241k (120.50) + 1 permille on 178k (178.00)
    assert zurich_liability(500_000) == pytest.approx(298.50)
    # Steuerfuss multiplies the simple tax
    assert zurich_liability(500_000, steuerfuss=2.18) == pytest.approx(298.50 * 2.18)


def test_zurich_married_allowance():
    assert zurich_liability(150_000, married=True) == 0.0
    assert zurich_liability(150_000, married=False) > 0


def test_ifi_trigger_and_decote():
    # Below the 1.3M trigger: no tax even though the schedule starts at 800k
    assert ifi_liability(1_200_000) == 0.0
    # 1.35M: gross = 0.5% on 500k + 0.7% on 50k = 2,850; décote = 17,500 - 1.25%*1.35M
    # = 625 -> 2,225
    assert ifi_liability(1_350_000) == pytest.approx(2_225.0)
    # 2.5M: 0.5% on 500k + 0.7% on 1.2M = 2,500 + 8,400 = 10,900
    assert ifi_liability(2_500_000) == pytest.approx(10_900.0)


def test_ifi_income_cap():
    # Plafonnement: IFI + other income taxes capped at 75% of income
    assert ifi_liability(20_000_000, income=100_000, other_income_taxes=50_000) == pytest.approx(25_000)


def test_piketty_paper_variant():
    assert piketty_liability(150_000) == 0.0
    assert piketty_liability(800_000) == pytest.approx(3_000)  # 0.5% on 600k
    # 6M: 0.5% on 0.8M + 1% on 4M + 2% on 1M = 4,000 + 40,000 + 20,000
    assert piketty_liability(6_000_000) == pytest.approx(64_000)
    # Book variant adds 0.1% below 200k
    assert piketty_liability(150_000, schedule=S.PIKETTY_BOOK_VARIANT) == pytest.approx(150)


def test_common_portfolio_and_spanish_residence_cap_kinks():
    assert portfolio(1_000_000) == pytest.approx((250_000, 750_000))
    entry = S.IP_GENERAL_EXEMPTION / 0.75
    assert ip_path(entry, S.IP_GENERAL_EXEMPTION) == pytest.approx(0.0, abs=1e-9)
    assert ip_path(entry + 1, S.IP_GENERAL_EXEMPTION) == pytest.approx(0.0015)
    # Below €1.2M, each extra euro adds 75 cents to the base; above it, the
    # €300k home relief is capped and the full euro enters.
    assert ip_path(1_190_001, S.IP_GENERAL_EXEMPTION) - ip_path(
        1_190_000, S.IP_GENERAL_EXEMPTION
    ) == pytest.approx(0.00225)
    assert ip_path(1_210_001, S.IP_GENERAL_EXEMPTION) - ip_path(
        1_210_000, S.IP_GENERAL_EXEMPTION
    ) == pytest.approx(0.003)


def test_norway_paper_path_entry_and_portfolio_marginal_rate():
    assessable_share = 0.25 * 0.25 + 0.75
    entry_eur = (
        S.NORWAY_PAPER_VARIANT["threshold_single"]
        / S.NOK_PER_EUR_2022
        / assessable_share
    )
    assert entry_eur == pytest.approx(207_159.2, abs=0.1)
    assert norway_paper_path(entry_eur) == pytest.approx(0.0, abs=1e-9)
    assert norway_paper_path(1_000_001) - norway_paper_path(1_000_000) == pytest.approx(
        0.008125
    )


def test_zurich_path_converts_euros_to_and_from_chf():
    assert CHF_PER_EUR_2022 == pytest.approx(1.0047093385214)
    assessable_share = 0.70 * 0.25 + 0.75
    entry_eur = 81_000 / (assessable_share * CHF_PER_EUR_2022)
    assert zurich_path(entry_eur - 1) == 0.0
    assert zurich_path(entry_eur + 1) > 0.0
    expected_marginal = assessable_share * 0.0005 * (0.99 + 1.19)
    assert zurich_path(100_001) - zurich_path(100_000) == pytest.approx(expected_marginal)


def test_france_path_property_light_trigger_and_entry_liability():
    assessable_share = (1.0 - S.IFI_MAIN_RESIDENCE_ABATEMENT) * 0.25
    entry_eur = S.IFI_TRIGGER / assessable_share
    assert entry_eur == pytest.approx(7_428_571.43, abs=0.01)
    assert france_path(entry_eur) == 0.0
    assert france_path(entry_eur + 1) == pytest.approx(1_250.0, abs=0.01)
