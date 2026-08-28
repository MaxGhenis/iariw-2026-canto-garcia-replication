# Axiom wealth-tax migration final report

Status date: 2026-08-28

Canonical coordination branch: `axiom-rulespec-migration-clean`

Legacy mixed branch: `axiom-rulespec-migration` (contains pre-existing
presentation commits and is not the Axiom review branch)

Status: **incomplete; blocked at Axiom's protected corpus/apply boundary**

## Outcome

This session did not satisfy the requested definition of done. The four country
lanes remain source-first scaffolds with zero atomic RuleSpec modules, and the
replication calculators still use the bespoke comparison implementation. I did
not hand-author protected atomic files, manufacture proof atoms, weaken the
supervisor, or relabel a synthetic engine test as a country implementation.

The work did leave the migration in a more accurate and reproducible state:

- 10 corpus intake manifests now identify 19 official documents and 19 unique
  citation roots across Spain, Norway, Switzerland/Zürich, and France;
- the previously open 2022 Zürich tariff and French IFI mid-bracket checks are
  closed against primary sources;
- the retroactive ITSGF exemption amendment is explicitly sourced;
- the bespoke comparison path's Spanish cent-anchor and Norwegian
  joint-threshold defects are corrected behind new tests;
- CHF and NOK compile as Axiom currency units on the local engine branch;
- the replication package has a fail-closed, exact-decimal runtime for real
  Axiom compiled artifacts, exercised by eight synthetic integration tests; and
- the exact publishable encode/compose/execute sequence and blockers are known.

## Definition-of-done status

| Requirement | Status | Evidence |
|---|---|---|
| Four country encodings validate and carry provision citations | **Not complete** | `axiom-encode inventory` reports 0 files and 0 rules in every country repo. Only source maps and intake manifests exist. |
| Axiom-backed calculator behind the existing signatures | **Not complete** | The real-engine runtime contract is implemented, but there are no country artifacts to bind; `calculator.py` remains the explicitly labelled comparator. |
| Original 26 oracle tests pass unchanged against Axiom | **Not complete** | The original test file is byte-unchanged and passes, but still reaches the comparator. Eight additional tests execute a synthetic composition through the Rust engine. |
| Eight paper scenarios are ProgramSpec overlays | **Not complete** | No ProgramSpecs were committed because their atomic imports and exported identifiers do not exist. |
| Cent comparison table for all eight scenarios | **Not complete** | It cannot be generated without executable country artifacts and overlays. |
| README, NOTES, and progress ledger updated | **Complete for the actual state** | They distinguish source vintages, record implementation gaps, tests, commits, and blockers. |
| Commits pushed | **Partly complete** | The clean coordination, corpus, and engine branches are pushed. `gh` authentication is invalid and the four country repos do not exist/have remotes, so those histories remain local. |

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

- Existing foundation commits: `c440d90`, `dfdd42a`, `d9ef6b8`, `45d3af2`,
  `8b529b9`, `270066a`, `a7ac97d`, and `7e41ba9`.
- `968d9c9` — create the replication progress ledger.
- `886b796` — record the independent migration audit.
- `05d5694` — record the verified 2022 Zürich source.
- `30e5773` — correct Spanish statutory anchors and the Norwegian joint
  threshold; add distinct 2022 Zürich law and regression tests.
- `6d4c134` — update the replication source register and documentation.

The Axiom runtime validates artifact format and SHA-256, enforces the compiler's
exact input catalog, rejects missing or unknown slots, uses exact `Decimal`
values, issues annual queries, and fails closed for missing dependencies,
artifacts, inputs, outputs, or engine execution.

### `axiom-corpus`

Branch `wealth-tax-source-manifests`:

- `65abb900` — add 10 official-document intake manifests (17 documents);
- `6cfb8231` — add the official historical 2022 Zürich § 47 source; and
- `f00f7d4a` — add the retroactive ITSGF exemption amendment source.

Current intake total: 10 manifests, 19 documents, 19 unique citation roots.
There are still no extracted `sources/`, `inventory/`, `provisions/`, or
`coverage/` artifacts for these scopes and no signed named release.
The branch is pushed to `TheAxiomFoundation/axiom-corpus`.

### `axiom-rules-engine`

Branch `wealth-tax-currency-seeds`, commit `9d61eea`:

- registers CHF and NOK as two-minor-unit currencies; and
- adds RuleSpec compile tests for each.

The replication lock remains on upstream engine `v0.2.2`/`2c0e1ed` because the
CHF/NOK feature commit is not reviewed, merged, or released. Pinning production
replication code to the feature branch would get ahead of that admission step.

The engine branch is now pushed to `TheAxiomFoundation/axiom-rules-engine`; the
replication lock should move only after the engine change is reviewed and lands
on a stable reachable revision.

### Country repositories

| Repository | Current commit | Scope | Remote |
|---|---:|---|---|
| `rulespec-es` | `4f8f338` | `es`, `es-md`, `es-an`, `es-ga`; includes RDL 8/2023 authority | none |
| `rulespec-no` | `9ace7f1` | `no`; 2022/2023 statute and guidance maps | none |
| `rulespec-ch` | `988ebd3` | `ch`, `ch-zh`; distinct 2022/2026 tariff sources | none |
| `rulespec-fr` | `c38c40d` | `fr`; archived 2022 CGI IFI source | none |

Each country README explicitly requires supervised encoding and says not to
hand-author RuleSpec. Each `.axiom/toolchain.toml` is an intentional
`NON-VALIDATING PLACEHOLDER`; workflow dependencies still contain `<pin-me>`.
The layout tests therefore prove only repository shape, not legal coverage.

## Validation evidence

- Replication: **37 passed** — 26 unchanged anchors, 3 legal-correction
  regressions, and 8 tests that compile/execute a synthetic composition through
  the real Rust engine.
- Axiom Compose core/spec/transformation suite: **18 passed**.
- Country layout suites: **7 passed in each repo** (28 total).
- Country encoder inventory: **0 files / 0 rules / 0 source-provision files / 0
  compositions in each repo**.
- Corpus intake validation: **10 manifests / 19 documents / 19 unique citation
  roots**; focused manifest/page-window suite **4 passed**.
- GitNexus staged checks for both new corpus commits: **low risk, 0 affected
  processes**.
- Engine CHF test: **1 passed**; NOK test: **1 passed**; `cargo fmt --check`
  passed.
- Documentation and staged diffs: `git diff --check` passed for every committed
  step.

## Why production encoding is blocked

The supported country-lane sequence is source extraction, immutable signed
corpus release, real three-key toolchain binding, then supervised
`axiom-encode encode ... --apply`. This environment cannot complete that chain:

1. Terminal DNS and raw outbound connections are intermittent and normally
   fail. A brief working interval allowed the three existing branches to push,
   but subsequent GitHub resolution failed again. Browser-accessible primary
   sources cannot be converted into authenticated corpus snapshots by copying
   rendered text.
2. `gh auth status` reports an invalid token. A post-run names-only
   `agent-secret` search confirmed that the relevant Axiom corpus/apply key
   entries exist; no credential value was read or exposed. This does not
   unblock the production apply path, which is deliberately bound to the
   protected GitHub Actions workflow.
3. The corpus worktree contains manifests only. The normal publisher needs an
   isolated S3-compatible bucket, migrated Supabase/PostgREST, a corpus signing
   key, and a clean tracked release selector. None is present locally.
4. The protected `/opt/axiom-verification` installation has fixed production
   trust roots and no apply signer. The current supervisor requires an external
   `apply_ed25519` signer file descriptor.
5. The encoder's `--allow-local-dev` option exists only on the leaf signer. It
   creates a throwaway key and nonpublishable manifests that Foundation CI does
   not trust. A safe dev chain would additionally require a newly root-owned
   supervisor tree plus isolated S3/Supabase services; this sandbox cannot write
   `/opt` and approvals are disabled.

Using the test supervisor fixture, inventing release evidence, or committing a
dev-signed manifest would weaken the required controls and would not satisfy the
request.

## Exact resume sequence

1. Restore stable terminal network/DNS and GitHub CLI authentication. Create the
   four `TheAxiomFoundation/rulespec-*` repositories, add remotes, and push the
   clean local histories. The coordination, corpus, and engine branches are
   already pushed.
2. Run all 10 corpus manifests through the normal extraction pipeline; inspect
   official snapshots and the resulting source inventory, provisions, and
   coverage. Commit them, create complete-expression-date release selectors,
   and publish immutable signed country releases.
3. Land dedicated country commits binding the real release name/content digest,
   waiver-set digest, full dependency SHAs, and reviewed reusable workflow SHA.
4. Through the production supervisor and apply signer, run commands of the form:

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
5. Add scenario ProgramSpecs only after the exported identifiers are fixed.
   Axiom Compose does not support replacing an imported derived rule with the
   same name: overlays must produce unique scenario outputs, or import atomic
   components while omitting the baseline liability producer and synthesize a
   common output in separate artifacts.
6. Compose each scenario with explicit country roots and the pinned corpus SHA,
   compile with `compile-composed`, execute with `run-compiled`, and bind each
   artifact to the existing replication signatures. Add `axiom-compose` and the
   pushed CHF/NOK-capable engine revision to the reproducible dependency lock.
7. Run the unchanged 26 tests through those country artifacts, generate the
   eight-design cent comparison table, update this report, and push all commits.

## Scope integrity

No deck slide source, staged OBBBA deliverable, or Gmail draft is included in
the canonical `axiom-rulespec-migration-clean` history. The earlier
`axiom-rulespec-migration` publication includes pre-existing presentation
commits `b797752`, `42ac3df`, and `2daa58e`; it is preserved rather than
force-rewritten, but should not be used as the Axiom review branch. Dirty
deck/chart/export files in the original worktree remain untouched.
