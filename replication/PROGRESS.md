# Axiom RuleSpec migration progress

## State

- Active: auditing the existing migration branch, country RuleSpec repositories,
  Axiom corpus/toolchain, and immutable replication oracle tests.
- Constraint: all production calculations must execute real composed RuleSpec
  artifacts through the Axiom rules engine; no parallel hand-written evaluator.

## Done

- Confirmed the replication repository and the four country repositories are
  present locally.
- Recorded the standing requirement to preserve the 26 existing oracle tests,
  keep paper scenarios as overlays, and avoid all out-of-scope presentation and
  communication artifacts.

## Next

1. Inventory existing commits and uncommitted work without disturbing user edits.
2. Verify repository-creation/CI conventions, RuleSpec format, composition, and
   engine bindings against the checked-out Axiom sources.
3. Validate and complete ES, NO, CH/ZH, and FR legal encodings with citations.
4. Replace the replication calculator path with composition plus Axiom execution.
5. Add and run eight-scenario cent-parity comparison, update documentation, push,
   and write the final report.
