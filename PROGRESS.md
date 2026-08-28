# Axiom RuleSpec migration progress

## State

- Active branch: `axiom-rulespec-migration`.
- Coordination repository: this replication package.
- Current phase: source intake committed; corpus extraction/signing and first supervised country encodings are next.
- Guardrails: use the real Axiom RuleSpec composition and rules-engine path; preserve the 26 existing oracle tests unchanged; keep paper scenarios as overlays; do not touch the slide app, staged OBBBA PDF, or Gmail drafts.

## Done

- Confirmed the replication worktree was clean at `ce37958` before starting.
- Started parallel audits of the replication API/tests, Axiom repo and CI conventions, and primary-source/corpus grounding.
- Selected clean Axiom worktrees at cached upstream refs: `axiom-encode` `deccdafd`, `axiom-rules-engine` `2c0e1ed`, `axiom-compose` `9a514ac`, `axiom-oracles` `d77dc7fd9`, and `axiom-corpus` `620527d7`.
- Used `axiom-encode new-jurisdiction` to generate all four canonical country scaffolds; their generated layout suites each pass 7/7 tests.
- Committed the scaffolds locally: `rulespec-es` `97d4a7c`, `rulespec-no` `d014f21`, `rulespec-ch` `afa3b37`, and `rulespec-fr` `915d946`.
- Recorded executable oracle plans for Spain and France (EUROMOD is available) and explicit no-oracle status for Norway and Switzerland.
- Confirmed Axiom engine v0.2.2 already registers EUR but needs the generated NOK and CHF currency seeds before those two country modules can validate.
- Added and tested the missing CHF/NOK currency registrations on Axiom engine branch `wealth-tax-currency-seeds`, commit `9d61eea` (both RuleSpec compile tests pass; `cargo fmt --check` passes).
- Added 10 official-document intake manifests covering 17 unique Spanish, Norwegian, Swiss, and French sources on `axiom-corpus` branch `wealth-tax-source-manifests`, commit `65abb900`.
- Validated every intake manifest with the current corpus loader, unique source/citation-path checks, compiled extraction regexes, `git diff --check`, and the focused corpus suite (102/102 tests passing). GitNexus reports low impact and no affected processes.
- Kept the Zürich tariff source explicitly dated to its verified 2026 indexed edition; the manifest does not misstate it as a 2022 table. Verified the City of Zürich 119% factor for 2022 and 2023 from the official 2023 accounts.
- Closed the previously flagged French IFI bracket gap against the archived 2022 CGI text; the source manifest covers the exact Article 977 scale and décote together with Articles 964, 973, and 979.
- Recorded external-access constraints: terminal GitHub DNS is unavailable, `gh` authentication is expired, and the approved agent secret store is locked; local work can continue, but signed apply and push cannot complete until access is restored.

## Next

- Extract and sign the 17 verified legal-source snapshots in `axiom-corpus`, then cut the jurisdiction bindings required by the current supervised workflow. The intake manifests are ready; terminal DNS and signing access currently block this step.
- Encode and validate sourced law through `axiom-encode`, including explicit unresolved-source notes without guessing.
- Replace the bespoke replication execution path with Axiom composition and engine execution.
- Run unchanged oracle tests and produce cent-level scenario comparisons.
- Update documentation, write the final report, and push all branches/commits.
