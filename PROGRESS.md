# Axiom RuleSpec migration progress

## State

- Active branch: `axiom-rulespec-migration`.
- Coordination repository: this replication package.
- Current phase: corpus ingestion and first supervised country encodings.
- Guardrails: use the real Axiom RuleSpec composition and rules-engine path; preserve the 26 existing oracle tests unchanged; keep paper scenarios as overlays; do not touch the slide app, staged OBBBA PDF, or Gmail drafts.

## Done

- Confirmed the replication worktree was clean at `ce37958` before starting.
- Started parallel audits of the replication API/tests, Axiom repo and CI conventions, and primary-source/corpus grounding.
- Selected clean Axiom worktrees at cached upstream refs: `axiom-encode` `deccdafd`, `axiom-rules-engine` `2c0e1ed`, `axiom-compose` `9a514ac`, `axiom-oracles` `d77dc7fd9`, and `axiom-corpus` `620527d7`.
- Used `axiom-encode new-jurisdiction` to generate all four canonical country scaffolds; their generated layout suites each pass 7/7 tests.
- Committed the scaffolds locally: `rulespec-es` `97d4a7c`, `rulespec-no` `d014f21`, `rulespec-ch` `afa3b37`, and `rulespec-fr` `915d946`.
- Recorded executable oracle plans for Spain and France (EUROMOD is available) and explicit no-oracle status for Norway and Switzerland.
- Confirmed Axiom engine v0.2.2 already registers EUR but needs the generated NOK and CHF currency seeds before those two country modules can validate.
- Recorded external-access constraints: terminal GitHub DNS is unavailable, `gh` authentication is expired, and the approved agent secret store is locked; local work can continue, but signed apply and push cannot complete until access is restored.

## Next

- Add NOK and CHF currency units to the real Axiom engine with tests.
- Ingest the verified legal sources into `axiom-corpus` and cut the jurisdiction bindings required by the current supervised workflow.
- Encode and validate sourced law through `axiom-encode`, including explicit unresolved-source notes without guessing.
- Replace the bespoke replication execution path with Axiom composition and engine execution.
- Run unchanged oracle tests and produce cent-level scenario comparisons.
- Update documentation, write the final report, and push all branches/commits.
