"""Validated metadata for Axiom compiled-program artifacts.

The rules engine publishes the accepted runtime names in
``metadata.input_catalog``.  Treating that catalog as an explicit contract is
important: a misspelled RuleSpec identifier otherwise becomes a new free
input, which can make an apparently successful integration execute the wrong
program.
"""

from __future__ import annotations

import hashlib
import json
from collections.abc import Mapping
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .errors import AxiomArtifactError, AxiomInputCatalogError

SUPPORTED_ARTIFACT_FORMAT_VERSION = 2


def _required_string(value: Any, label: str) -> str:
    if not isinstance(value, str) or not value:
        raise AxiomArtifactError(f"{label} must be a non-empty string")
    return value


@dataclass(frozen=True, slots=True)
class InputCatalogEntry:
    """One compiler input slot and every request name accepted for it."""

    slot: str
    canonical_request_name: str
    request_names: tuple[str, ...]


@dataclass(frozen=True, slots=True)
class CompiledInputCatalog:
    """Immutable, checked view of ``metadata.input_catalog``."""

    entries: tuple[InputCatalogEntry, ...]

    @classmethod
    def from_raw(cls, raw: Any) -> CompiledInputCatalog:
        if not isinstance(raw, list):
            raise AxiomArtifactError("metadata.input_catalog must be a list")

        entries: list[InputCatalogEntry] = []
        seen_slots: set[str] = set()
        for index, item in enumerate(raw):
            if not isinstance(item, Mapping):
                raise AxiomArtifactError(f"metadata.input_catalog[{index}] must be an object")
            slot = _required_string(item.get("slot"), f"input_catalog[{index}].slot")
            canonical = _required_string(
                item.get("canonical_request_name"),
                f"input_catalog[{index}].canonical_request_name",
            )
            request_names_raw = item.get("request_names")
            if not isinstance(request_names_raw, list) or not request_names_raw:
                raise AxiomArtifactError(
                    f"input_catalog[{index}].request_names must be a non-empty list"
                )
            request_names = tuple(
                _required_string(name, f"input_catalog[{index}].request_names[]")
                for name in request_names_raw
            )
            if canonical not in request_names:
                raise AxiomArtifactError(
                    f"canonical request name {canonical!r} is absent from request_names"
                )
            if slot in seen_slots:
                raise AxiomArtifactError(f"duplicate compiled input slot: {slot}")
            seen_slots.add(slot)
            entries.append(InputCatalogEntry(slot, canonical, request_names))

        return cls(tuple(entries))

    def as_dict(self) -> dict[str, str]:
        """Return ``slot -> canonical request name`` in compiler order."""

        return {entry.slot: entry.canonical_request_name for entry in self.entries}

    def canonical_name(self, slot: str) -> str:
        for entry in self.entries:
            if entry.slot == slot:
                return entry.canonical_request_name
        raise AxiomInputCatalogError(f"compiled artifact has no input slot {slot!r}")

    def assert_exact(self, expected: Mapping[str, str]) -> None:
        """Fail unless ``expected`` exactly matches the compiled catalog."""

        actual = self.as_dict()
        expected_dict = dict(expected)
        if actual == expected_dict:
            return

        missing = sorted(actual.keys() - expected_dict.keys())
        unexpected = sorted(expected_dict.keys() - actual.keys())
        mismatched = sorted(
            slot
            for slot in actual.keys() & expected_dict.keys()
            if actual[slot] != expected_dict[slot]
        )
        details = []
        if missing:
            details.append(f"unacknowledged artifact slots={missing}")
        if unexpected:
            details.append(f"expected slots absent from artifact={unexpected}")
        if mismatched:
            pairs = {
                slot: {"artifact": actual[slot], "expected": expected_dict[slot]}
                for slot in mismatched
            }
            details.append(f"canonical request-name mismatches={pairs}")
        raise AxiomInputCatalogError("; ".join(details))

    def assert_supplied(self, supplied_slots: set[str]) -> None:
        """Fail unless one value is supplied for every compiled input slot."""

        required = set(self.as_dict())
        missing = sorted(required - supplied_slots)
        unexpected = sorted(supplied_slots - required)
        if not missing and not unexpected:
            return
        details = []
        if missing:
            details.append(f"missing input slots={missing}")
        if unexpected:
            details.append(f"unknown input slots={unexpected}")
        raise AxiomInputCatalogError("; ".join(details))


@dataclass(frozen=True, slots=True)
class CompiledArtifact:
    """A compiled artifact whose format, inputs, and outputs are validated."""

    path: Path
    sha256: str
    artifact_format_version: int
    engine_version: str | None
    input_catalog: CompiledInputCatalog
    output_request_names: frozenset[str]

    @classmethod
    def load(cls, path: str | Path) -> CompiledArtifact:
        artifact_path = Path(path).expanduser()
        try:
            artifact_path = artifact_path.resolve(strict=True)
            source = artifact_path.read_bytes()
        except (OSError, RuntimeError) as exc:
            raise AxiomArtifactError(
                f"cannot read compiled Axiom artifact {artifact_path}"
            ) from exc
        if not artifact_path.is_file():
            raise AxiomArtifactError(f"compiled Axiom artifact is not a file: {artifact_path}")

        try:
            raw = json.loads(source)
        except (UnicodeDecodeError, json.JSONDecodeError) as exc:
            raise AxiomArtifactError(
                f"compiled Axiom artifact is not valid JSON: {artifact_path}"
            ) from exc
        if not isinstance(raw, Mapping):
            raise AxiomArtifactError("compiled Axiom artifact root must be an object")

        version = raw.get("artifact_format_version")
        if version != SUPPORTED_ARTIFACT_FORMAT_VERSION:
            raise AxiomArtifactError(
                "unsupported compiled artifact format: "
                f"expected {SUPPORTED_ARTIFACT_FORMAT_VERSION}, got {version!r}"
            )

        metadata = raw.get("metadata")
        if not isinstance(metadata, Mapping):
            raise AxiomArtifactError("compiled artifact metadata must be an object")
        catalog = CompiledInputCatalog.from_raw(metadata.get("input_catalog"))

        program = raw.get("program")
        if not isinstance(program, Mapping):
            raise AxiomArtifactError("compiled artifact program must be an object")
        derived = program.get("derived")
        if not isinstance(derived, list):
            raise AxiomArtifactError("compiled artifact program.derived must be a list")
        output_names: set[str] = set()
        for index, rule in enumerate(derived):
            if not isinstance(rule, Mapping):
                raise AxiomArtifactError(f"program.derived[{index}] must be an object")
            name = rule.get("name")
            rule_id = rule.get("id")
            if isinstance(name, str) and name:
                output_names.add(name)
            if isinstance(rule_id, str) and rule_id:
                output_names.add(rule_id)

        engine_version = raw.get("engine_version")
        if engine_version is not None and not isinstance(engine_version, str):
            raise AxiomArtifactError("compiled artifact engine_version must be text or null")

        return cls(
            path=artifact_path,
            sha256=hashlib.sha256(source).hexdigest(),
            artifact_format_version=version,
            engine_version=engine_version,
            input_catalog=catalog,
            output_request_names=frozenset(output_names),
        )

    def assert_output(self, output: str) -> None:
        if output not in self.output_request_names:
            raise AxiomArtifactError(
                f"compiled artifact does not publish output {output!r}; "
                f"available={sorted(self.output_request_names)}"
            )


@dataclass(frozen=True, slots=True)
class CompiledProgramBinding:
    """Pinned execution contract for one output in a compiled artifact."""

    artifact: CompiledArtifact
    output: str
    entity: str
    expected_input_catalog: tuple[tuple[str, str], ...]

    @classmethod
    def load(
        cls,
        artifact_path: str | Path,
        *,
        output: str,
        entity: str,
        expected_input_catalog: Mapping[str, str],
    ) -> CompiledProgramBinding:
        if not output:
            raise AxiomArtifactError("compiled output name must be non-empty")
        if not entity:
            raise AxiomArtifactError("compiled output entity must be non-empty")
        artifact = CompiledArtifact.load(artifact_path)
        artifact.assert_output(output)
        artifact.input_catalog.assert_exact(expected_input_catalog)
        return cls(
            artifact=artifact,
            output=output,
            entity=entity,
            expected_input_catalog=tuple(expected_input_catalog.items()),
        )
