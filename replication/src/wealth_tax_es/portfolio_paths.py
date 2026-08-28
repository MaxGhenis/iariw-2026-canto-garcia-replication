"""Illustrative common-portfolio paths used in the discussant charts.

These functions are deliberately separate from the statutory calculators. They
hold one non-pension balance sheet fixed at 25% main residence and 75% other
assets, then apply each design's valuation rules. They are chart assumptions,
not estimates of the Spanish wealth distribution.
"""

from . import schedules as S
from .calculator import ifi_liability, ip_liability, norway_liability, zurich_liability

RESIDENCE_SHARE = 0.25
OTHER_ASSET_SHARE = 1.0 - RESIDENCE_SHARE

# ECB annual-average reference rate for 2022, series EXR.A.CHF.EUR.SP00.A:
# one euro = 1.0047093385214 Swiss francs.
CHF_PER_EUR_2022 = 1.0047093385214


def portfolio(net_wealth_eur: float) -> tuple[float, float]:
    """Return (main residence, other assets), both at market value in euros."""
    return RESIDENCE_SHARE * net_wealth_eur, OTHER_ASSET_SHARE * net_wealth_eur


def ip_path(net_wealth_eur: float, exemption: float) -> float:
    """Spanish state IP reference, including the main-residence relief."""
    residence_eur, _ = portfolio(net_wealth_eur)
    return ip_liability(
        net_wealth_eur,
        main_residence_value=residence_eur,
        exemption=exemption,
        apply_rebate=False,
    )


def norway_paper_path(net_wealth_eur: float) -> float:
    """Paper's flat-1% Norway variant along the common portfolio, in euros."""
    residence_eur, other_assets_eur = portfolio(net_wealth_eur)
    assessable_eur = (
        S.NORWAY_PRIMARY_RESIDENCE_DISCOUNT * residence_eur + other_assets_eur
    )
    return norway_liability(
        assessable_eur * S.NOK_PER_EUR_2022,
        params=S.NORWAY_PAPER_VARIANT,
    ) / S.NOK_PER_EUR_2022


def zurich_path(net_wealth_eur: float) -> float:
    """Illustrative Zurich City reference, converting the euro path to/from CHF."""
    residence_eur, other_assets_eur = portfolio(net_wealth_eur)
    assessable_chf = (
        S.ZURICH_REAL_ESTATE_FACTOR * residence_eur + other_assets_eur
    ) * CHF_PER_EUR_2022
    steuerfuss = S.ZURICH_STEUERFUSS_CANTON + S.ZURICH_STEUERFUSS_CITY
    liability_chf = zurich_liability(assessable_chf, steuerfuss=steuerfuss)
    return liability_chf / CHF_PER_EUR_2022


def france_path(net_wealth_eur: float) -> float:
    """French IFI with only the common portfolio's main residence in the base."""
    residence_eur, _ = portfolio(net_wealth_eur)
    assessable_real_estate_eur = (
        1.0 - S.IFI_MAIN_RESIDENCE_ABATEMENT
    ) * residence_eur
    return ifi_liability(assessable_real_estate_eur)
