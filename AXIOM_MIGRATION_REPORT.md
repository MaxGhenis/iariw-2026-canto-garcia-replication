# Axiom wealth-tax migration final report

Status date: 2026-08-28

Canonical coordination branch: `axiom-rulespec-migration-clean`

The canonical branch is synchronized with current `origin/master`. Its Axiom
PR diff does not modify the presentation, deck, PDF, chart, or communication
artifacts inherited from that base.

Legacy mixed branch: `axiom-rulespec-migration` (contains pre-existing
presentation commits and is not the Axiom review branch)

Status: **incomplete; blocked by French source ingestion and Axiom's protected
corpus/apply boundary**

## Outcome

This session did not satisfy the requested definition of done. The four country
lanes remain source-first scaffolds with zero atomic RuleSpec modules, and the
replication calculators still use the bespoke comparison implementation. I did
not hand-author protected atomic files, manufacture proof atoms, weaken the
supervisor, or relabel a synthetic engine test as a country implementation.

The work did leave the migration in a more accurate and reproducible state:

- 11 corpus intake manifests now identify 19 official documents and 19 unique
  citation roots across Spain, Norway, Switzerland/Zürich, and France;
- the previously open 2022 Zürich tariff and French IFI mid-bracket checks are
  closed against primary sources;
- the retroactive ITSGF exemption amendment is explicitly sourced;
- disposable live extraction is coverage-complete for 10 of 11 manifests; the
  French historical chapter needs a DILA LEGI/PISTE ingestion adapter;
- the bespoke comparison path's Spanish cent-anchor and Norwegian
  joint-threshold defects are corrected behind new tests;
- CHF and NOK compile as Axiom currency units and are merged to engine
  `main`;
- all four country scaffold histories now have public organization repositories
  and pushed `main` branches;
- the replication package has a fail-closed, exact-decimal runtime for real
  Axiom compiled artifacts, exercised by 12 runtime contract tests around a
  synthetic composition compiled and executed through the real engine; and
- the exact publishable encode/compose/execute sequence and blockers are known.

## Definition-of-done status

| Requirement | Status | Evidence |
|---|---|---|
| Four country encodings validate and carry provision citations | **Not complete** | `axiom-encode inventory` reports 0 files and 0 rules in every country repo. Only source maps and intake manifests exist. |
| Axiom-backed calculator behind the existing signatures | **Not complete** | The real-engine runtime contract is implemented, but there are no country artifacts to bind; `calculator.py` remains the explicitly labelled comparator. |
| Original 26 oracle tests pass unchanged against Axiom | **Not complete** | The Axiom change set leaves the current-master baseline test files untouched. The 26 starting-point cases remain (20 schedule plus 6 index/long-run cases), and current master adds 4 schedule/portfolio-path cases, but all 30 baseline cases still reach the comparator/Python analysis path. Twelve additional runtime contract tests exercise a synthetic composition compiled and executed through the Rust engine. |
| Eight paper scenarios are ProgramSpec overlays | **Not complete** | No ProgramSpecs were committed because their atomic imports and exported identifiers do not exist. |
| Cent comparison table for all eight scenarios | **Not complete** | It cannot be generated without executable country artifacts and overlays. |
| README, NOTES, and progress ledger updated | **Complete for the actual state** | They distinguish source vintages, record implementation gaps, tests, commits, and blockers. |
| Commits pushed | **Complete for current work** | The clean coordination, corpus, engine, and all four country histories are pushed. Country validation still cannot start because the deliberately invalid `<pin-me>` workflow/toolchain placeholders require signed-release inputs. |

## Legal-source corrections

### Spain

- Ley 19/1991 Article 30's cumulative quota column is now represented directly
  in the comparator. Integrating only the printed rounded bounds produced
  €71,362.34 and €183,670.30 at the two highest edges, one cent above the
  statutory €71,362.33 and €183,670.29 anchors.
- ITSGF's own cumulative anchors are recorded as €39,915.97 and €152,223.93.
- The original Ley 38/2022 text limited the €700,000 reduction to
  personal-obligation taxpayers. Real Decreto-ley 8/2023 Article 17 removed that
  qualifier with effect from Ley 38/2022's entry into force. The amendment is a
  separate corpus source rather than being silently projected backward.
- Andalucía's 100% rebate was operative before the 31 December 2022 accrual;
  the explicit 1 January language in Decreto-ley 7/2022 applies to its IRPF
  provisions, not to the wealth-tax clause itself.
- A full Article 31 module still needs inputs absent from the three-argument
  comparator: personal-obligation scope, gains/dividend adjustments,
  non-income-producing assets, and joint-return allocation.

### Norway

- Joint assessment doubles both the allowance and the upper state-rate
  threshold. The correct 2022 upper threshold is NOK 20m single and NOK 40m
  joint. The former comparator taxed a NOK 25m joint case at NOK 212,700 instead
  of NOK 205,200.
- State and municipal components must remain separately composable: the 0.70%
  municipal component is the statutory maximum/default, not a universal enacted
  local rate.
- The verified asset factors are 25% through NOK 10m and 50%/70% above for a
  primary residence in 2022/2023, 95%/100% for secondary housing, and 75%/80%
  for shares.
- A complete taxable-net-wealth base still needs proportional debt reduction for
  discounted assets under skatteloven § 4-19.

### Zürich

- Official historical StG Nachtrag 115, § 47 closes the 2022 source gap. Its
  single widths are CHF 77k, 231k, 386k, 616k, 925k, and 923k before the top
  band; married/reduced widths are CHF 154k, 231k, 385k, 616k, 925k, and 924k.
- The ESTV table used by the original oracle is explicitly a separate 2026
  indexed vintage (CHF 81k/161k initial widths). The unchanged oracle continues
  to test that historical choice, while `zurich_liability_2022` tests the law
  applicable to 2022.
- Canton 99% and City of Zürich 119% factors remain separate composable inputs.

### France

- The archived 2022 CGI verifies the €1.3m trigger, scale beginning at €800k,
  0.7%/1%/1.25% intermediate rates at €2.57m/€5m/€10m, the €1.3m–€1.4m
  décote, 30% main-residence abatement, and 75% plafonnement.
- The simple comparator's optional cap is not a substitute for encoding every
  Article 979 income/tax component definition in the eventual RuleSpec.

## Committed work

### Coordination and replication repository

Clean branch commit chain:

- `322bb68`, `e7b1e4c`, `193df5a`, `3cefdcf`, `61d55a2`, `961ee77`,
  `b66e18f`, and `58a42ac` — establish the migration ledger, country
  scaffolds, source intake, runtime foundation, and initial handoff;
- `fd554bc`, `8437585`, `beab157`, `6131bbc`, and `ab8be34` — record the
  audit, close the historical Zürich gap, correct the Spanish and Norwegian
  comparison oracles, and update source documentation;
- `c8ab0e7`, `35bd133`, and `787a8f1` — finalize the blocker report and
  publish the clean handoff; and
- `87b42b4` — pin compiled artifacts and the exact Axiom engine binary by
  independently supplied SHA-256 digests; and
- `d8b19f1` — update the report and handoff with the final repository, PR, CI,
  corpus-workflow, and blocker state before the current-master synchronization.

The Axiom runtime validates artifact format and an externally supplied artifact
SHA-256, enforces the compiler's exact input catalog, rejects missing or unknown
slots, uses exact `Decimal` values, issues annual queries, and requires an
externally supplied SHA-256 for the executable engine binary. It re-hashes both
files immediately before each engine call and fails closed for drift, missing
dependencies, artifacts, inputs, outputs, or engine execution. Those expected
digests must come from a trusted signed release or lock; this runtime does not
itself validate release signatures.

### `axiom-corpus`

Branch `wealth-tax-source-manifests`:

- `65abb900` — add 10 official-document intake manifests (17 documents);
- `6cfb8231` — add the official historical 2022 Zürich § 47 source;
- `f00f7d4a` — add the retroactive ITSGF exemption amendment source;
- `e8a89787` — replace blocked Zürich attachment links and restrict the
  Zürich/retroactive Spanish extraction slices; and
- `574513cc` — split mixed Zürich scopes, narrow the remaining Swiss and
  Spanish sources, and stop Norwegian guidance before unrelated sections.

Current intake total: 11 manifests, 19 documents, 19 unique citation roots.
There are still no extracted `sources/`, `inventory/`, `provisions/`, or
`coverage/` artifacts for these scopes and no signed named release.
The branch is pushed to `TheAxiomFoundation/axiom-corpus`. PR #624 is open,
mergeable/clean, and has all applicable CI green; production release coverage
is skipped by design on pull requests. It is ready for maintainer review and
merge.

### `axiom-rules-engine`

Feature commit `9d61eea`, merged through
`TheAxiomFoundation/axiom-rules-engine#165` as `bb4b568`:

- registers CHF and NOK as two-minor-unit currencies; and
- adds RuleSpec compile tests for each.

PR #165 and the resulting `main` merge commit passed Linux/macOS Rust tests,
PyO3, WASM, and Python package checks. CHF/NOK are therefore on the default
branch and satisfy the country workflow ancestry prerequisite. The latest
published engine release is still `v0.2.2`/`2c0e1ed`, so the replication
client lock should move only after a CHF/NOK-capable release is cut and
verified.

### Country repositories

| Repository | Current commit | Scope | Remote |
|---|---:|---|---|
| `rulespec-es` | `4f8f338` | `es`, `es-md`, `es-an`, `es-ga`; includes RDL 8/2023 authority | `TheAxiomFoundation/rulespec-es` |
| `rulespec-no` | `9ace7f1` | `no`; 2022/2023 statute and guidance maps | `TheAxiomFoundation/rulespec-no` |
| `rulespec-ch` | `642a3e5` | `ch`, `ch-zh`; distinct 2022/2026 tariff sources and split statute/guidance manifests | `TheAxiomFoundation/rulespec-ch` |
| `rulespec-fr` | `c38c40d` | `fr`; archived 2022 CGI IFI source | `TheAxiomFoundation/rulespec-fr` |

Each country README explicitly requires supervised encoding and says not to
hand-author RuleSpec. Each `.axiom/toolchain.toml` is an intentional
`NON-VALIDATING PLACEHOLDER`; workflow dependencies still contain `<pin-me>`.
The layout tests therefore prove only repository shape, not legal coverage.
The first push-triggered workflow in each new repository created zero jobs and
reported the expected invalid reusable-workflow reference at `@<pin-me>`.
Existing green BE/NZ lanes currently pin reviewed shared workflow
`842c69d6aa62a0d75a4da850fabc3d0df20701d7`, but copying that reference and
dependency SHAs before these four signed releases exist would only advance the
failure to the three-key toolchain gate.

## Validation evidence

- Replication: **45 passed** — 26 starting-point tests, 4 schedule/portfolio-path
  tests inherited from current master, 3 legal-correction regressions, and 12
  runtime contract tests around a synthetic composition compiled and executed
  through the real Rust engine.
- Coordination PR #1 is open and mergeable/clean, but this repository has no PR
  validation workflow or reported status checks. The replication, Ruff, and
  formatting evidence here is local; GitHub's `CLEAN` state confirms only that
  the branch is conflict-free.
- Axiom Compose core/spec/transformation suite: **18 passed**.
- Country layout suites: **7 passed in each repo** (28 total).
- Country encoder inventory: **0 files / 0 rules / 0 source-provision files / 0
  compositions in each repo**.
- Corpus intake validation: **11 manifests / 19 documents / 19 unique citation
  roots**; focused scope suite **11 passed**. Live extraction completed with
  full coverage for 10 of 11 manifests (18 of 19 documents); the historical
  French Légifrance source remains access-blocked.
- Corpus repository, local macOS: **4,260 passed / 80 skipped / 208
  deselected**. PR #624 Linux/Python 3.14 CI: **4,263 passed / 77 skipped / 208
  deselected**. Ruff, mypy, Towncrier, artifact guard, PostgreSQL, workflow,
  citation-grammar, and named-release selector checks passed.
- GitNexus staged checks for the corpus fixes: **low risk, 0 affected
  processes**.
- Engine PR #165: CHF test **1 passed**; NOK test **1 passed**; full Linux/macOS
  Rust, PyO3, WASM, and Python package CI passed on both the PR and merged
  `main`; `cargo fmt --check` passed locally.
- Documentation and staged diffs: `git diff --check` passed for every committed
  step.

## Why production encoding is blocked

The supported country-lane sequence is source extraction, immutable signed
corpus release, real three-key toolchain binding, then supervised
`axiom-encode encode ... --apply`. This environment cannot complete that chain:

1. Ten of the 11 manifests now extract successfully from official sources. The
   historical French Légifrance chapter is legally correct but returns a
   Cloudflare challenge to the supported HTTP and browser-impersonation
   fetches. DILA's official LEGI bulk archive is reachable, but the current
   extractor cannot stream its tar/XML format or select the historical article
   versions. France therefore needs a narrow LEGI archive importer or
   credentialed PISTE adapter; BOFiP guidance is not a statute substitute.
   The implementation is tracked in `axiom-corpus#625`.
2. GitHub authentication recovered, the four organization repositories were
   created, and their local histories were pushed. Their first `main` workflow
   events fail before any job starts because the committed reusable-workflow
   reference and dependency inputs are deliberately `<pin-me>`. Replacing
   those placeholders before a signed corpus release would invent the required
   three-key binding rather than validate it.
3. The corpus branch contains only intake manifests/tests: it has no protected
   corpus artifacts, signed `.axiom/ingest-manifests`, or immutable
   `manifests/releases/*.json` selector. There is no Actions workflow that
   extracts official documents or signs ingest manifests, and no repository,
   organization, or environment Actions secret named
   `AXIOM_CORPUS_INGEST_PRIVATE_KEY`. A protected key-holder/local wrapper must
   create and sign those files before same-repository PR CI can verify them.
   The two Zürich statute manifests share the `ch-zh/statute` scope, so the
   extraction controller must assign distinct immutable source versions to
   avoid overwriting either extraction. If one combined scope is needed, compose
   those versions into a third distinct target version.
4. The protected `/opt/axiom-verification` installation has fixed production
   trust roots and no apply signer. The current supervisor requires an external
   `apply_ed25519` signer file descriptor.
5. The production publish workflow can stage, verify, and sign a complete
   release after a canonical selector reaches `main`, but no valid selector or
   artifacts exist yet. Live environment configuration also shows
   `release-activation` restricted to `main` without the required-reviewer
   rule described by its comments; activation must not be requested until that
   policy is confirmed or repaired.
6. The encoder's `--allow-local-dev` option exists only on the leaf signer. It
   creates a throwaway key and nonpublishable manifests that Foundation CI does
   not trust. A safe dev chain would additionally require a newly root-owned
   supervisor tree plus isolated S3/Supabase services; this sandbox cannot write
   `/opt` and approvals are disabled.

Using the test supervisor fixture, inventing release evidence, or committing a
dev-signed manifest would weaken the required controls and would not satisfy the
request.

## Exact resume sequence

1. Add a narrow official DILA LEGI tar/XML importer (or provision a
   credentialed PISTE adapter), pin the source archive, and extract the
   historical 2022 CGI Articles 964–983 without substituting guidance
   (`axiom-corpus#625`).
2. After manifest PR `axiom-corpus#624` passes review, have the protected
   key-holder use the supported local wrapper to run all 11 manifests through
   the normal extraction pipeline, inspect the official
   snapshots/inventory/provisions/coverage, and sign the ingest manifests. Ten
   manifests have passed disposable live extraction, but none of those outputs
   is committed or signed. Use distinct immutable source versions for the two
   `ch-zh/statute` manifests; if one combined scope is needed, compose them
   into a third distinct target version.
3. Submit those protected artifacts and ingest manifests through a
   same-repository PR. After they merge, add canonical complete expression-date
   release selectors on a dedicated PR, let `publish.yml` produce the signed
   immutable release objects, and confirm the activation environment policy
   before any activation.
4. Land dedicated country commits binding the real release name/content digest,
   waiver-set digest, full dependency SHAs, and a reviewed immutable reusable
   workflow SHA. The BE/NZ snapshot observed during this session was
   `842c69d6aa62a0d75a4da850fabc3d0df20701d7`; re-confirm it rather than
   assuming it remains the reviewed choice.
5. Through the production supervisor and apply signer, run commands of the form:

   ```bash
   axiom-encode encode \
     es/statute/ley-19-1991/impuesto-sobre-el-patrimonio/articulo-30 \
     --corpus-path /abs/axiom-corpus \
     --policy-repo-path /abs/rulespec-es \
     --axiom-rules-engine-path /abs/axiom-rules-engine \
     --output /tmp/es-encode \
     --apply
   ```

   Repeat for every national and subjurisdiction provision, then run companion
   tests, proof/money-atom validation, inventory, oracle disposition, and full
   `axiom-encode ci`.
6. Add scenario ProgramSpecs only after the exported identifiers are fixed.
   Axiom Compose does not support replacing an imported derived rule with the
   same name: overlays must produce unique scenario outputs, or import atomic
   components while omitting the baseline liability producer and synthesize a
   common output in separate artifacts.
7. Compose each scenario with explicit country roots and the pinned corpus SHA,
   compile with `compile-composed`, execute with `run-compiled`, and bind each
   artifact to the existing replication signatures. Add `axiom-compose` and the
   merged CHF/NOK-capable engine revision to the reproducible dependency lock
   after its release is verified.
8. Run the 26 starting-point oracle cases and the current-master baseline tests
   through those country artifacts, generate the eight-design cent comparison
   table, update this report, and push all commits.

## Scope integrity

The Axiom PR diff does not modify any slide/deck source, staged OBBBA
deliverable, PDF, chart artifact, or Gmail draft. The canonical
`axiom-rulespec-migration-clean` branch is synchronized with current master and
therefore inherits master's pre-existing presentation commits and files
unchanged. The earlier `axiom-rulespec-migration` publication also includes
presentation commits `b797752`, `42ac3df`, and `2daa58e`; it is preserved rather
than force-rewritten, but should not be used as the Axiom review branch. Dirty
deck/chart/export files in the original worktree remain untouched.
