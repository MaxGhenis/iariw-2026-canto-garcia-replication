# Axiom RuleSpec migration progress

## State

- Canonical Axiom-only branch: `axiom-rulespec-migration-clean`.
- Legacy mixed branch: `axiom-rulespec-migration` also contains three
  pre-existing presentation commits and is not the review branch for this work.
- Coordination repository: this replication package.
- Current phase: externally blocked after exhausting supported local paths.
  Source intake and the real-engine runtime foundation are committed, but there
  are still zero live country RuleSpec modules and zero paper-scenario
  ProgramSpecs. Production progress now requires network/authentication, signed
  corpus releases, and the protected apply signer.
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
- Added the replication package's fail-closed Axiom compiled-artifact runtime: exact input-catalog validation, `tax_year` intervals, Decimal-only inputs/outputs, artifact hashing, and explicit dependency/runtime errors. The focused suite compiles and executes a test composition through the real Rust engine; the full suite passes 34/34.
- Pinned and locked the official Axiom Python client to engine commit `2c0e1edac0dccc355297eb9663e0aa0c4e97e5b4`. The runtime foundation does not yet switch jurisdiction calculators or ship stand-in country artifacts.
- Prepared each country lane for the bounded wealth-tax scope without hand-authoring protected atomic modules: Spain `a7f3b539` (plus progress `b085cc99`), Norway `9ace7f16` (`7822a8e5`), Switzerland `08096273` (`7daf80c4`), and France `c38c40d0` (`6e52e154`).
- Cross-checked the four country source maps against all 10 corpus manifests and all 17 unique citation roots. Added `es-md`, `es-an`, `es-ga`, and `ch-zh` repository roots; retained the explicit Zürich 2022-vintage gap. Each country layout suite passes 7/7.
- Left country toolchains and reusable-workflow pins deliberately unresolved: no signed corpus release exists, the source-intake commit is not published, and the current encoder does not accept the workflow pin copied by older BE/NZ lanes. The dedicated binding/pin commits must follow release signing.
- Updated `replication/README.md` and `replication/NOTES.md` with the real-engine development contract, exact 2022/2023 primary-source URLs, the country-lane/source-intake state, the still-open Zürich 2022 tariff vintage, and the now-closed French IFI Article 977 bracket check.
- Created the committed handoff/output file `AXIOM_MIGRATION_REPORT.md` with the definition-of-done matrix, validation evidence, commit map, exact blockers, and resume sequence. It reports the migration as incomplete rather than overstating the scaffold/runtime work.
- Recorded the worker's external-access constraints: terminal GitHub DNS was
  intermittent, `gh` authentication was expired, and its credential lookup was
  unavailable at that stage. Local work could continue, but signed apply could
  not.
- Re-audited the actual branch after takeover: the full replication suite is
  34/34 (26 byte-unchanged legal oracles plus 8 synthetic real-engine tests),
  but `calculator.py` is byte-unchanged from `origin/master` and none of the 26
  oracle cases reaches Axiom. Each country lane has 0 atomic modules, 0
  companion RuleSpec tests, and 0 ProgramSpecs; its 7/7 tests are layout-only.
- Reconfirmed the protected trust boundary: current `axiom-encode` requires a
  signed corpus release and a supervisor-attached external signer for
  `encode --apply`. No protected trust-root config or signer socket is present;
  `gh auth status` reports an invalid token. A post-run names-only
  `agent-secret` search confirmed the relevant Axiom entries exist, without
  reading their values; that does not bypass the GitHub-Actions-only production
  apply signer.
- Confirmed terminal DNS still cannot resolve BOE. The Playwright CLI wrapper
  also could not establish a usable retrieval session, so no source snapshot
  was fabricated or copied through an untrusted path.
- Located and line-checked the official historical Zürich StG edition that was
  in force for tax year 2022. Added its § 47 PDF and historical-law landing page
  to the corpus intake branch at `6cfb8231`; the prior 2026 ESTV indexed table
  remains separately identified rather than being relabelled as 2022 law.
- Completed the ES/NO legal audit. It found that joint Norwegian assessment
  doubles both the allowance and the NOK 20m state-rate threshold, and that the
  Spanish IP computation must honor the statutory cuota anchors to avoid
  one-cent drift. These are defects in the bespoke comparison path that its
  current broad tolerances do not expose.
- Corrected those comparison-oracle defects without changing the 26 original
  tests: Spain now uses the statutory cumulative-quota anchors, jointly assessed
  Norwegian spouses use the NOK 40m top-rate threshold, and the official 2022
  Zürich tariff is available separately from the preserved 2026 paper oracle.
  Three focused regression tests bring the full replication suite to 37/37.
- Added the retroactive ITSGF exemption amendment to the corpus intake branch at
  `f00f7d4a`, bound it in the Spain source map at `4f8f338`, and closed the
  Zurich 2022-vintage source-map gap at `988ebd3`. The intake now covers 19
  official documents; it still has no extracted/signed release artifacts.
- Probed the complete guarded local path. The available local-dev signer creates
  explicitly nonpublishable manifests; a safe real dev release would also need
  isolated S3/Supabase services and a new root-owned supervisor tree, neither of
  which is available in this sandbox. The final report records the exact
  production resume sequence without weakening those controls.
- Reconstructed the migration commits on the Axiom-only
  `axiom-rulespec-migration-clean` branch from `origin/master`, excluding the
  three pre-existing deck/chart commits on the legacy mixed branch.
- Pushed the clean coordination branch, `wealth-tax-source-manifests`, and
  `wealth-tax-currency-seeds` during working network intervals. The four country
  histories remain local because their organization repositories do not exist
  and `gh` authentication is invalid.

## Next

- Restore operator-managed network/authentication and protected signing access.
- Extract and sign the 19 verified legal-source snapshots in `axiom-corpus`, then cut the jurisdiction bindings required by the current supervised workflow.
- Encode and validate sourced law through `axiom-encode`, including explicit unresolved-source notes without guessing.
- Replace the bespoke replication execution path with Axiom composition and engine execution.
- Run unchanged oracle tests and produce cent-level scenario comparisons.
- Update documentation, write the final report, and push all branches/commits.
