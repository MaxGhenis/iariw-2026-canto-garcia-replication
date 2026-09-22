"""Regression tests for defects found while source-auditing the oracle path."""

from wealth_tax_es import schedules as S
from wealth_tax_es.calculator import (
    norway_liability,
    progressive_tax,
    zurich_liability,
    zurich_liability_2022,
)


def test_spanish_ip_uses_statutory_quota_anchors_exactly():
    for lower_bound, statutory_quota, _rate in S.IP_STATE_SCHEDULE:
        assert progressive_tax(lower_bound, S.IP_STATE_SCHEDULE) == statutory_quota


def test_norway_joint_assessment_doubles_top_rate_threshold():
    assert norway_liability(25_000_000, couple=True) == 205_200


def test_zurich_2022_and_2026_vintages_remain_distinct():
    assert zurich_liability_2022(500_000) == 307.5
    assert zurich_liability(500_000) == 298.5
