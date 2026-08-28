"""Fail-closed execution of real Axiom compiled artifacts."""

from __future__ import annotations

import os
from collections.abc import Mapping
from dataclasses import dataclass
from datetime import date
from decimal import Decimal, InvalidOperation
from pathlib import Path
from typing import Any, Literal

from .artifact import CompiledProgramBinding
from .errors import (
    AxiomDependencyError,
    AxiomExecutionError,
    AxiomInputCatalogError,
    AxiomOutputError,
    AxiomRuntimeUnavailableError,
)

ExecutionMode = Literal["explain", "fast"]
ScalarKind = Literal["bool", "integer", "decimal", "text", "date"]


@dataclass(frozen=True, slots=True)
class TaxYearInterval:
    """Calendar tax-year interval used by the wealth-tax programs."""

    year: int
    start: date
    end: date
    period_kind: str = "tax_year"


def tax_year_interval(year: int) -> TaxYearInterval:
    if isinstance(year, bool) or not isinstance(year, int) or year < 1:
        raise ValueError("tax year must be a positive integer")
    return TaxYearInterval(year, date(year, 1, 1), date(year, 12, 31))


@dataclass(frozen=True, slots=True)
class AxiomInputValue:
    """One typed input value on the engine's JSON wire contract."""

    kind: ScalarKind
    value: Decimal | bool | int | str | date

    @classmethod
    def decimal(cls, value: Decimal | int | str) -> AxiomInputValue:
        """Build an exact decimal fact; binary floats are intentionally rejected."""

        if isinstance(value, (bool, float)):
            raise TypeError("Axiom decimal inputs require Decimal, int, or decimal text")
        try:
            decimal_value = value if isinstance(value, Decimal) else Decimal(value)
        except (InvalidOperation, ValueError) as exc:
            raise ValueError(f"invalid Axiom decimal input: {value!r}") from exc
        if not decimal_value.is_finite():
            raise ValueError("Axiom decimal inputs must be finite")
        return cls("decimal", decimal_value)

    @classmethod
    def integer(cls, value: int) -> AxiomInputValue:
        if isinstance(value, bool) or not isinstance(value, int):
            raise TypeError("Axiom integer inputs require int")
        return cls("integer", value)

    @classmethod
    def boolean(cls, value: bool) -> AxiomInputValue:
        if not isinstance(value, bool):
            raise TypeError("Axiom boolean inputs require bool")
        return cls("bool", value)

    @classmethod
    def text(cls, value: str) -> AxiomInputValue:
        if not isinstance(value, str):
            raise TypeError("Axiom text inputs require str")
        return cls("text", value)

    @classmethod
    def date(cls, value: date) -> AxiomInputValue:
        if not isinstance(value, date):
            raise TypeError("Axiom date inputs require datetime.date")
        return cls("date", value)

    def wire_value(self) -> bool | int | str:
        if self.kind == "decimal":
            return format(self.value, "f")
        if self.kind == "date":
            return self.value.isoformat()
        return self.value


@dataclass(frozen=True, slots=True)
class AxiomEvaluation:
    """Exact scalar result plus engine and period evidence."""

    value: Decimal
    entity_id: str
    output: str
    tax_year: TaxYearInterval
    requested_mode: str
    actual_mode: str
    fallback_reason: str | None
    artifact_sha256: str


def _load_python_binding() -> tuple[Any, Any, Any]:
    try:
        from axiom_rules_engine import AxiomRulesEngine, Dataset, ExecutionQuery
    except ImportError as exc:
        raise AxiomDependencyError(
            "axiom-rules-engine's Python package is required for compiled execution"
        ) from exc
    return AxiomRulesEngine, Dataset, ExecutionQuery


class AxiomRuntime:
    """Execute a pinned compiled program through the official Python client."""

    def __init__(self, binary_path: str | Path, *, timeout: float = 30.0) -> None:
        binary = Path(binary_path).expanduser()
        try:
            binary = binary.resolve(strict=True)
        except (OSError, RuntimeError) as exc:
            raise AxiomRuntimeUnavailableError(
                f"Axiom rules-engine binary does not exist: {binary}"
            ) from exc
        if not binary.is_file() or not os.access(binary, os.X_OK):
            raise AxiomRuntimeUnavailableError(
                f"Axiom rules-engine binary is not executable: {binary}"
            )
        if timeout <= 0:
            raise ValueError("Axiom runtime timeout must be positive")

        engine_type, dataset_type, query_type = _load_python_binding()
        self.binary_path = binary
        self.timeout = timeout
        self._engine = engine_type(binary_path=binary, timeout=timeout)
        self._dataset_type = dataset_type
        self._query_type = query_type

    def evaluate_decimal(
        self,
        binding: CompiledProgramBinding,
        inputs: Mapping[str, AxiomInputValue],
        *,
        tax_year: int,
        entity_id: str = "tax-unit:1",
        mode: ExecutionMode = "explain",
    ) -> AxiomEvaluation:
        """Execute one entity and return an exact scalar Decimal output."""

        if not entity_id:
            raise ValueError("Axiom entity_id must be non-empty")
        if mode not in ("explain", "fast"):
            raise ValueError(f"unsupported Axiom execution mode: {mode!r}")
        if not all(isinstance(value, AxiomInputValue) for value in inputs.values()):
            raise TypeError("all Axiom runtime inputs must be AxiomInputValue instances")

        supplied_slots = set(inputs)
        binding.artifact.input_catalog.assert_supplied(supplied_slots)
        expected = dict(binding.expected_input_catalog)
        binding.artifact.input_catalog.assert_exact(expected)

        interval = tax_year_interval(tax_year)
        records = []
        for slot in sorted(inputs):
            input_value = inputs[slot]
            records.append(
                {
                    "name": binding.artifact.input_catalog.canonical_name(slot),
                    "entity": binding.entity,
                    "entity_id": entity_id,
                    "interval": {
                        "start": interval.start.isoformat(),
                        "end": interval.end.isoformat(),
                    },
                    "value": {
                        "kind": input_value.kind,
                        "value": input_value.wire_value(),
                    },
                }
            )

        dataset = self._dataset_type.model_validate({"inputs": records, "relations": []})
        query = self._query_type.model_validate(
            {
                "entity_id": entity_id,
                "period": {
                    "period_kind": interval.period_kind,
                    "start": interval.start.isoformat(),
                    "end": interval.end.isoformat(),
                },
                "outputs": [binding.output],
            }
        )
        try:
            response = self._engine.run_compiled(
                mode=mode,
                artifact_path=binding.artifact.path,
                dataset=dataset,
                queries=[query],
            )
        except Exception as exc:
            raise AxiomExecutionError(
                f"Axiom rules engine failed for output {binding.output!r}"
            ) from exc

        if len(response.results) != 1:
            raise AxiomOutputError(f"expected one Axiom query result, got {len(response.results)}")
        result = response.results[0]
        if result.entity_id != entity_id:
            raise AxiomOutputError(
                f"Axiom response entity mismatch: expected {entity_id!r}, got {result.entity_id!r}"
            )
        output = result.outputs.get(binding.output)
        if output is None:
            raise AxiomOutputError(f"Axiom response omitted requested output {binding.output!r}")
        if output.kind != "scalar" or output.value.kind not in ("decimal", "integer"):
            raise AxiomOutputError(f"Axiom output {binding.output!r} is not a numeric scalar")
        try:
            value = Decimal(str(output.value.value))
        except InvalidOperation as exc:
            raise AxiomOutputError(
                f"Axiom output {binding.output!r} is not a valid decimal"
            ) from exc

        response_period = result.period
        if (
            response_period.period_kind != interval.period_kind
            or response_period.start != interval.start
            or response_period.end != interval.end
        ):
            raise AxiomOutputError("Axiom response did not preserve the requested tax year")

        return AxiomEvaluation(
            value=value,
            entity_id=entity_id,
            output=binding.output,
            tax_year=interval,
            requested_mode=response.metadata.requested_mode,
            actual_mode=response.metadata.actual_mode,
            fallback_reason=response.metadata.fallback_reason,
            artifact_sha256=binding.artifact.sha256,
        )


def require_input_value(value: Any) -> AxiomInputValue:
    """Narrow an untyped value with a catalog-focused error for adapters."""

    if not isinstance(value, AxiomInputValue):
        raise AxiomInputCatalogError(
            "compiled inputs must be explicitly typed AxiomInputValue instances"
        )
    return value
