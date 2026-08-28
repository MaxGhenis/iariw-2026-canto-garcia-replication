# Axiom RuleSpec migration progress

## State

- Active branch: `axiom-rulespec-migration`.
- Coordination repository: this replication package.
- Current phase: repository, runtime, source, and oracle-test reconnaissance.
- Guardrails: use the real Axiom RuleSpec composition and rules-engine path; preserve the 26 existing oracle tests unchanged; keep paper scenarios as overlays; do not touch the slide app, staged OBBBA PDF, or Gmail drafts.

## Done

- Confirmed the replication worktree was clean at `ce37958` before starting.
- Started parallel audits of the replication API/tests, Axiom repo and CI conventions, and primary-source/corpus grounding.

## Next

- Record the exact implementation and validation plan from the audits.
- Seed the four country RuleSpec repositories using the current Axiom organization runbook.
- Encode and validate sourced law, including explicit ratchets for unresolved primary-source gaps.
- Replace the bespoke replication execution path with Axiom composition and engine execution.
- Run unchanged oracle tests and produce cent-level scenario comparisons.
- Update documentation, write the final report, and push all branches/commits.
