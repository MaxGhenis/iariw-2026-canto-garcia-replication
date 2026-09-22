"""Focused contract tests for real Axiom compiled-artifact execution.

The temporary RuleSpec below is a test-only composition.  It is compiled and
executed by the local Rust engine; it is not a country-law artifact and is not
used by the replication calculators.
"""

from __future__ import annotations

import hashlib
import json
import os
import shutil
from dataclasses import dataclass
from decimal import Decimal
from pathlib import Path

import pytest

from wealth_tax_es.axiom import (
    AxiomArtifactError,
    AxiomInputCatalogError,
    AxiomInputValue,
    AxiomRuntime,
    AxiomRuntimeUnavailableError,
    CompiledArtifact,
    CompiledProgramBinding,
    tax_year_interval,
)

COMPOSITION = """\
format: rulespec/v1
module:
  kind: composition
  summary: Test-only exact-decimal wealth-tax composition.
rules:
  - name: test_wealth_tax
    kind: derived
    entity: TaxUnit
    dtype: Money
    period: Year
    unit: EUR
    source: Synthetic runtime integration fixture
    versions:
      - effective_from: '2022-01-01'
        formula: |-
          max(0, taxable_wealth - allowance) * rate + adjustment
"""

EXPECTED_CATALOG = {
    "taxable_wealth": "taxable_wealth",
    "allowance": "allowance",
    "rate": "rate",
    "adjustment": "adjustment",
}


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _local_engine_binary() -> Path:
    configured = os.environ.get("AXIOM_RULES_ENGINE_BIN")
    if configured:
        return Path(configured).expanduser().resolve()

    installed = shutil.which("axiom-rules-engine")
    if installed:
        return Path(installed).resolve()

    engine_root = (
        Path(__file__).resolve().parents[3] / "iariw-axiom-worktrees" / "axiom-rules-engine"
    )
    candidates = tuple(
        engine_root / "target" / profile / "axiom-rules-engine" for profile in ("release", "debug")
    )
    return next(
        (candidate.resolve() for candidate in candidates if candidate.is_file()), candidates[0]
    )


@pytest.fixture(scope="module")
def engine_binary() -> Path:
    binary = _local_engine_binary()
    assert binary.is_file(), f"real local Axiom engine is missing: {binary}"
    assert os.access(binary, os.X_OK), f"real local Axiom engine is not executable: {binary}"
    return binary


@dataclass(frozen=True)
class CompiledFixture:
    artifact_path: Path
    binding: CompiledProgramBinding


@pytest.fixture(scope="module")
def compiled_fixture(tmp_path_factory, engine_binary: Path) -> CompiledFixture:
    from axiom_rules_engine import AxiomRulesEngine

    temp_root = tmp_path_factory.mktemp("axiom-runtime")
    rulespec_root = (temp_root / "rulespec-us").resolve()
    (rulespec_root / "us" / "statutes").mkdir(parents=True)
    composition_path = (temp_root / "runtime-composition.yaml").resolve()
    composition_path.write_text(COMPOSITION, encoding="utf-8")
    artifact_path = (temp_root / "runtime.compiled.json").resolve()

    engine = AxiomRulesEngine(binary_path=engine_binary, timeout=30)
    engine.compile_composed(
        program_path=composition_path,
        rulespec_roots=(rulespec_root,),
        output_path=artifact_path,
    )
    binding = CompiledProgramBinding.load(
        artifact_path,
        expected_artifact_sha256=_sha256(artifact_path),
        output="test_wealth_tax",
        entity="TaxUnit",
        expected_input_catalog=EXPECTED_CATALOG,
    )
    return CompiledFixture(artifact_path=artifact_path, binding=binding)


def _inputs() -> dict[str, AxiomInputValue]:
    return {
        "taxable_wealth": AxiomInputValue.decimal(Decimal("1500000.10")),
        "allowance": AxiomInputValue.decimal(Decimal("700000.05")),
        "rate": AxiomInputValue.decimal(Decimal("0.002")),
        "adjustment": AxiomInputValue.decimal(Decimal("0.005")),
    }


def test_tax_year_interval_is_calendar_tax_year():
    interval = tax_year_interval(2022)
    assert interval.period_kind == "tax_year"
    assert interval.start.isoformat() == "2022-01-01"
    assert interval.end.isoformat() == "2022-12-31"


def test_compiled_input_catalog_is_exact_and_exposed(compiled_fixture: CompiledFixture):
    catalog = compiled_fixture.binding.artifact.input_catalog
    assert catalog.as_dict() == EXPECTED_CATALOG
    assert catalog.canonical_name("taxable_wealth") == "taxable_wealth"

    with pytest.raises(AxiomInputCatalogError, match="unacknowledged artifact slots"):
        catalog.assert_exact({"taxable_wealth": "taxable_wealth"})
    with pytest.raises(AxiomInputCatalogError, match="canonical request-name mismatches"):
        catalog.assert_exact({**EXPECTED_CATALOG, "rate": "invented#input.rate"})


def test_real_compiled_execution_returns_exact_decimal_and_tax_year(
    compiled_fixture: CompiledFixture, engine_binary: Path
):
    runtime = AxiomRuntime(
        engine_binary,
        expected_binary_sha256=_sha256(engine_binary),
    )
    result = runtime.evaluate_decimal(
        compiled_fixture.binding,
        _inputs(),
        tax_year=2022,
        entity_id="tax-unit:oracle",
        mode="explain",
    )

    assert isinstance(result.value, Decimal)
    assert result.value == Decimal("1600.00510")
    assert result.entity_id == "tax-unit:oracle"
    assert result.output == "test_wealth_tax"
    assert result.tax_year == tax_year_interval(2022)
    assert result.requested_mode == "explain"
    assert result.actual_mode == "explain"
    assert len(result.artifact_sha256) == 64
    assert result.engine_binary_sha256 == _sha256(engine_binary)


def test_runtime_rejects_missing_and_unknown_inputs_before_execution(
    compiled_fixture: CompiledFixture, engine_binary: Path
):
    runtime = AxiomRuntime(
        engine_binary,
        expected_binary_sha256=_sha256(engine_binary),
    )
    missing = _inputs()
    missing.pop("rate")
    with pytest.raises(AxiomInputCatalogError, match=r"missing input slots=\['rate'\]"):
        runtime.evaluate_decimal(compiled_fixture.binding, missing, tax_year=2022)

    unexpected = {**_inputs(), "typo_rate": AxiomInputValue.decimal("0.002")}
    with pytest.raises(AxiomInputCatalogError, match=r"unknown input slots=\['typo_rate'\]"):
        runtime.evaluate_decimal(compiled_fixture.binding, unexpected, tax_year=2022)


def test_decimal_inputs_reject_binary_floats():
    with pytest.raises(TypeError, match="require Decimal"):
        AxiomInputValue.decimal(0.1)


def test_runtime_fails_closed_when_engine_is_missing(tmp_path):
    with pytest.raises(AxiomRuntimeUnavailableError, match="does not exist"):
        AxiomRuntime(
            tmp_path / "missing-axiom-rules-engine",
            expected_binary_sha256="0" * 64,
        )


def test_runtime_rejects_unpinned_engine_binary(engine_binary: Path):
    with pytest.raises(AxiomRuntimeUnavailableError, match="binary SHA-256 mismatch"):
        AxiomRuntime(engine_binary, expected_binary_sha256="0" * 64)


def test_runtime_rejects_engine_binary_changed_after_initialization(
    compiled_fixture: CompiledFixture,
    engine_binary: Path,
    tmp_path: Path,
):
    mutable_binary = tmp_path / "axiom-rules-engine"
    shutil.copy2(engine_binary, mutable_binary)
    runtime = AxiomRuntime(
        mutable_binary,
        expected_binary_sha256=_sha256(mutable_binary),
    )
    with mutable_binary.open("r+b") as stream:
        stream.write(b"changed")

    with pytest.raises(AxiomRuntimeUnavailableError, match="changed after"):
        runtime.evaluate_decimal(compiled_fixture.binding, _inputs(), tax_year=2022)


def test_artifact_rejects_unsupported_format(compiled_fixture: CompiledFixture, tmp_path):
    raw = json.loads(compiled_fixture.artifact_path.read_text(encoding="utf-8"))
    raw["artifact_format_version"] = 999
    incompatible = tmp_path / "incompatible.compiled.json"
    incompatible.write_text(json.dumps(raw), encoding="utf-8")

    with pytest.raises(AxiomArtifactError, match="unsupported compiled artifact format"):
        CompiledArtifact.load(incompatible, expected_sha256=_sha256(incompatible))


def test_binding_requires_expected_artifact_digest(compiled_fixture: CompiledFixture):
    with pytest.raises(AxiomArtifactError, match="artifact SHA-256 mismatch"):
        CompiledProgramBinding.load(
            compiled_fixture.artifact_path,
            expected_artifact_sha256="0" * 64,
            output="test_wealth_tax",
            entity="TaxUnit",
            expected_input_catalog=EXPECTED_CATALOG,
        )


def test_runtime_rejects_artifact_changed_after_binding(
    compiled_fixture: CompiledFixture,
    engine_binary: Path,
    tmp_path: Path,
):
    artifact_path = tmp_path / "mutable.compiled.json"
    shutil.copyfile(compiled_fixture.artifact_path, artifact_path)
    binding = CompiledProgramBinding.load(
        artifact_path,
        expected_artifact_sha256=_sha256(artifact_path),
        output="test_wealth_tax",
        entity="TaxUnit",
        expected_input_catalog=EXPECTED_CATALOG,
    )
    artifact_path.write_text("{}", encoding="utf-8")
    runtime = AxiomRuntime(
        engine_binary,
        expected_binary_sha256=_sha256(engine_binary),
    )

    with pytest.raises(AxiomArtifactError, match="changed after binding"):
        runtime.evaluate_decimal(binding, _inputs(), tax_year=2022)


def test_binding_rejects_output_absent_from_artifact(compiled_fixture: CompiledFixture):
    with pytest.raises(AxiomArtifactError, match="does not publish output"):
        CompiledProgramBinding.load(
            compiled_fixture.artifact_path,
            expected_artifact_sha256=_sha256(compiled_fixture.artifact_path),
            output="invented_tax",
            entity="TaxUnit",
            expected_input_catalog=EXPECTED_CATALOG,
        )
