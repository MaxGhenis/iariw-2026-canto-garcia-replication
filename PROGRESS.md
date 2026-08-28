# Axiom RuleSpec migration progress

## State

- Canonical Axiom-only branch: `axiom-rulespec-migration-clean`.
- Legacy mixed branch: `axiom-rulespec-migration` also contains three
  pre-existing presentation commits and is not the review branch for this work.
- Coordination repository: this replication package.
- Current phase: externally blocked after exhausting supported local paths.
  Source intake and the real-engine runtime foundation are committed, but there
  are still zero live country RuleSpec modules and zero paper-scenario
  ProgramSpecs. Production progress now requires a French LEGI ingestion
  adapter, signed corpus releases, and the protected apply signer.
- Guardrails: use the real Axiom RuleSpec composition and rules-engine path; preserve the 26 existing oracle tests unchanged; keep paper scenarios as overlays; do not touch the slide app, staged OBBBA PDF, or Gmail drafts.

## Done

- Confirmed the replication worktree was clean at `ce37958` before starting.
- Started parallel audits of the replication API/tests, Axiom repo and CI conventions, and primary-source/corpus grounding.
- Selected clean Axiom worktrees at cached upstream refs: `axiom-encode` `deccdafd`, `axiom-rules-engine` `2c0e1ed`, `axiom-compose` `9a514ac`, `axiom-oracles` `d77dc7fd9`, and `axiom-corpus` `620527d7`.
- Used `axiom-encode new-jurisdiction` to generate all four canonical country scaffolds; their generated layout suites each pass 7/7 tests.
- Committed the scaffolds locally: `rulespec-es` `97d4a7c`, `rulespec-no` `d014f21`, `rulespec-ch` `afa3b37`, and `rulespec-fr` `915d946`.
- Recorded executable oracle plans for Spain and France (EUROMOD is available) and explicit no-oracle status for Norway and Switzerland.
- Confirmed Axiom engine v0.2.2 already registers EUR but needs the generated NOK and CHF currency seeds before those two country modules can validate.
- Added and tested the missing CHF/NOK currency registrations in engine feature
  commit `9d61eea` (both RuleSpec compile tests and `cargo fmt --check` pass).
  Engine PR #165 passed full CI and merged to `main` as `bb4b568`.
- Added 10 official-document intake manifests covering 17 unique Spanish, Norwegian, Swiss, and French sources on `axiom-corpus` branch `wealth-tax-source-manifests`, commit `65abb900`.
- Validated every intake manifest with the current corpus loader, unique source/citation-path checks, compiled extraction regexes, `git diff --check`, and the focused corpus suite (102/102 tests passing). GitNexus reports low impact and no affected processes.
- Kept the Zürich tariff source explicitly dated to its verified 2026 indexed edition; the manifest does not misstate it as a 2022 table. Verified the City of Zürich 119% factor for 2022 and 2023 from the official 2023 accounts.
- Closed the previously flagged French IFI bracket gap against the archived 2022 CGI text; the source manifest covers the exact Article 977 scale and décote together with Articles 964, 973, and 979.
- Added the replication package's fail-closed Axiom compiled-artifact runtime:
  exact input-catalog validation, `tax_year` intervals, Decimal-only
  inputs/outputs, externally pinned artifact and executable hashes, and explicit
  dependency/runtime errors. The current full suite passes 41/41.
- Pinned and locked the official Axiom Python client to engine commit `2c0e1edac0dccc355297eb9663e0aa0c4e97e5b4`. The runtime foundation does not yet switch jurisdiction calculators or ship stand-in country artifacts.
- Prepared each country lane for the bounded wealth-tax scope without hand-authoring protected atomic modules: Spain `a7f3b539` (plus progress `b085cc99`), Norway `9ace7f16` (`7822a8e5`), Switzerland `08096273` (`7daf80c4`), and France `c38c40d0` (`6e52e154`).
- Cross-checked the four country source maps against all 11 corpus manifests and
  all 19 unique citation roots. Added `es-md`, `es-an`, `es-ga`, and `ch-zh`
  repository roots and closed the Zürich 2022-vintage gap. Each country layout
  suite passes 7/7.
- Left country toolchains and reusable-workflow pins deliberately unresolved:
  the source-intake branch is published, but no signed corpus release exists,
  and the current encoder does not accept the workflow pin copied by older
  BE/NZ lanes. The dedicated binding/pin commits must follow release signing.
- Updated `replication/README.md` and `replication/NOTES.md` with the
  real-engine development contract, exact 2022/2023 primary-source URLs, the
  country-lane/source-intake state, the now-closed Zürich 2022 tariff gap, and
  the closed French IFI Article 977 bracket check.
- Created the committed handoff/output file `AXIOM_MIGRATION_REPORT.md` with the definition-of-done matrix, validation evidence, commit map, exact blockers, and resume sequence. It reports the migration as incomplete rather than overstating the scaffold/runtime work.
- Recorded the worker's external-access constraints: terminal GitHub DNS was
  intermittent, `gh` authentication was expired, and its credential lookup was
  unavailable at that stage. Local work could continue, but signed apply could
  not.
- Re-audited the actual branch after takeover: the current full replication
  suite is 41/41 (20 original schedule cases, 6 original index/long-run cases,
  3 correction regressions, and 12 synthetic real-engine contract tests),
  but `calculator.py` is byte-unchanged from `origin/master` and none of the 26
  oracle cases reaches Axiom. Each country lane has 0 atomic modules, 0
  companion RuleSpec tests, and 0 ProgramSpecs; its 7/7 tests are layout-only.
- Reconfirmed the protected trust boundary: current `axiom-encode` requires a
  signed corpus release and a supervisor-attached external signer for
  `encode --apply`. No protected trust-root config or signer socket is present.
  At that checkpoint, `gh auth status` reported an invalid token. A names-only
  `agent-secret` search confirmed the relevant Axiom entries exist, without
  reading their values; that does not bypass the GitHub-Actions-only production
  apply signer.
- The earlier worker encountered transient BOE DNS failures and correctly
  declined to fabricate a source snapshot. Later terminal access recovered and
  disposable live extraction succeeded for every manifest except France.
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
  Three focused regression tests and the expanded runtime contract suite bring
  the current full replication suite to 41/41.
- Added the retroactive ITSGF exemption amendment to the corpus intake branch at
  `f00f7d4a`, bound it in the Spain source map at `4f8f338`, and closed the
  Zurich 2022-vintage source-map gap. The subsequent corpus scope fixes land at
  `574513cc` and the current Swiss source-map commit is `642a3e5`. The intake
  covers 19 official documents; it still has no extracted/signed release
  artifacts.
- Probed the complete guarded local path. The available local-dev signer creates
  explicitly nonpublishable manifests; a safe real dev release would also need
  isolated S3/Supabase services and a new root-owned supervisor tree, neither of
  which is available in this sandbox. The final report records the exact
  production resume sequence without weakening those controls.
- Reconstructed the migration commits on the Axiom-only
  `axiom-rulespec-migration-clean` branch from `origin/master`, excluding the
  three pre-existing deck/chart commits on the legacy mixed branch.
- Pushed the clean coordination branch, `wealth-tax-source-manifests`, and
  `wealth-tax-currency-seeds`.
- GitHub authentication later recovered. Created public
  `TheAxiomFoundation/rulespec-es`, `rulespec-no`, `rulespec-ch`, and
  `rulespec-fr` repositories and pushed each `main` history. Their initial
  workflow events fail before jobs start because the signed-release and
  reusable-workflow values deliberately remain `<pin-me>`.
- Hardened the runtime in `87b42b4`: callers must supply independent
  compiled-artifact and engine-binary SHA-256 pins, and both paths are rehashed
  immediately before execution. Twelve runtime contract tests pass.
- Corrected the remaining corpus extraction scopes in `e8a89787` and
  `574513cc`. The intake now has 11 single-scope manifests, 19 documents, and
  19 unique citation roots. Ten manifests (18 documents) pass live extraction
  with complete coverage; the historical French source needs a DILA LEGI
  tar/XML or credentialed PISTE adapter. The local macOS corpus suite passes
  4,260 tests, with 80 skipped and 208 deselected; PR Linux/Python 3.14 CI
  passes 4,263, with 77 skipped and 208 deselected.
- Updated the local Swiss source map at `642a3e5` for the separate Zürich
  statute and guidance manifests.
- Opened corpus PR `TheAxiomFoundation/axiom-corpus#624`; it is open,
  mergeable/clean, and all applicable CI is green (production release coverage
  skips by design on PRs). It is ready for maintainer review and merge. Engine PR
  `TheAxiomFoundation/axiom-rules-engine#165` passed full CI and merged as
  `bb4b568`.
- Confirmed the new country workflows create zero jobs at their deliberate
  `@<pin-me>` reusable-workflow reference. Existing green BE/NZ lanes use
  immutable shared-workflow snapshot `842c69d6aa62a0d75a4da850fabc3d0df20701d7`,
  but the new lanes cannot bind it honestly until signed releases and
  default-branch dependency ancestry exist.
- Audited the protected corpus workflow. No Action extracts official documents
  or signs ingest manifests, and no ingest-private-key Actions secret exists.
  A protected key-holder/local wrapper must create and sign artifacts before
  same-repository CI can verify them. No publish or activation dispatch is safe
  without those files and a canonical release selector. The live
  `release-activation` environment also lacks the required-reviewer rule
  described by workflow comments, so its policy must be confirmed before use.
  The two Zürich statute manifests also share the `ch-zh/statute` scope, so
  extraction must use distinct immutable source versions; a combined scope, if
  needed, must compose them into a third distinct target version.
- Opened `TheAxiomFoundation/axiom-corpus#625` with the bounded DILA LEGI
  streaming importer design and historical article-selection acceptance tests.

## Next

- Add the official French LEGI ingestion adapter and obtain protected signing
  access.
- Have the protected key-holder extract and sign the 19 legal-source snapshots
  in `axiom-corpus`, merge them through same-repository CI, publish immutable
  releases, then cut the jurisdiction bindings required by the supervised
  workflow.
- Encode and validate sourced law through `axiom-encode`, including explicit unresolved-source notes without guessing.
- Replace the bespoke replication execution path with Axiom composition and engine execution.
- Run unchanged oracle tests and produce cent-level scenario comparisons.
- Keep the canonical report current as the protected release work advances.
