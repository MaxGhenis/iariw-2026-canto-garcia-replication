# Axiom wealth-tax migration report

Status date: 2026-08-28

Coordination branch: `axiom-rulespec-migration`

Status: blocked before protected source ingestion and supervised atomic encoding

## Outcome

The source-first and runtime prerequisites are committed, but the requested migration
is not complete. No unsigned or hand-authored atomic RuleSpec was substituted for the
protected Axiom workflow, and the bespoke calculator has not been relabeled as an
Axiom implementation.

The remaining critical path requires external state unavailable in this session:

1. terminal DNS/outbound access to official publishers and GitHub;
2. valid GitHub authentication and creation of the four organization repositories;
3. a signed corpus release for each country lane;
4. the current protected Axiom signing broker, supervised encoder, and apply signer.

## Definition-of-done status

| Requirement | Status | Evidence |
|---|---|---|
| Spain, Norway, Switzerland/Zürich, and France atomic RuleSpec with provision citations | **Not complete** | Four clean local scaffolds and source maps exist; Axiom inventory correctly reports zero atomic files/rules. |
| Validation with money proof atoms | **Not complete** | Ten intake manifests are parser-valid, but source snapshots, provisions, releases, and proof atoms cannot exist until extraction/signing runs. |
| Replication calculator defaults execute compose + engine under the same signatures | **Not complete** | A real-engine, fail-closed compiled-artifact runtime is committed and tested; `calculator.py` remains the explicit bespoke oracle pending country artifacts. |
| All 26 unchanged legal oracle tests pass against the Axiom-backed defaults | **Not complete** | The 26 tests still pass, but against the existing calculator. Eight additional runtime tests execute the actual Rust engine. |
| Eight paper scenarios are ProgramSpec overlays | **Not complete** | ProgramSpecs depend on the durable rule paths and exported symbols created by supervised country encoding; they were not guessed in advance. |
| Cent-level eight-scenario comparison table | **Not complete** | Cannot be produced honestly without the composed country artifacts and overlays. |
| README and NOTES updated | **Complete for current state** | Both document the exact source set, runtime contract, verified IFI brackets, Zürich vintage gap, and blockers. |
| Commits pushed | **Not complete** | Terminal cannot resolve GitHub, `gh` reports an invalid token, four new country repos have no remotes, and the approved secret helper is locked. |

## Committed work

### Coordination and replication repository

- `c440d90` — start committed migration progress ledger.
- `dfdd42a` — record four generated country scaffolds.
- `d9ef6b8` — record CHF/NOK engine prerequisite.
- `45d3af2` — record official-source intake.
- `8b529b9` — add the fail-closed real Axiom runtime foundation and locked client.
- `270066a` — record country source-intake layouts.
- `a7ac97d` — update the replication README and primary-source/open-gap notes.

The runtime validates compiled artifact format and SHA-256, asserts the compiler's
exact input catalog, rejects unknown or missing slots, uses exact `Decimal` values,
issues annual queries with `period_kind: tax_year`, and fails closed when the official
client, binary, artifact, input, or output is unavailable.

### `axiom-corpus`

Branch `wealth-tax-source-manifests`, commit `65abb900`:

- 10 official-document intake manifests;
- 17 unique source IDs and citation roots;
- national Spain plus Madrid, Andalucía, and Galicia;
- Norway statutes and guidance for 2022/2023;
- Swiss family rule plus Zürich tariff and tax-factor sources;
- archived 2022 French CGI IFI chapter.

The Zürich tariff manifest explicitly identifies the verified indexed table as the
2026 edition and does not claim it is the unavailable 2022 vintage. The archived CGI
source closes the former Article 977 mid-bracket verification gap.

### `axiom-rules-engine`

Branch `wealth-tax-currency-seeds`, commit `9d61eea`:

- registers CHF and NOK with two minor units;
- adds compile coverage for both currencies;
- passes the targeted tests and `cargo fmt --check`.

Country modules should still declare their currencies inline so their validity does
not depend on this unmerged engine patch alone.

### Country repositories

| Repository | Progress commit | Source-layout commit | Added scope |
|---|---:|---:|---|
| `rulespec-es` | `b085cc99` | `a7f3b539` | `es`, `es-md`, `es-an`, `es-ga` |
| `rulespec-no` | `7822a8e5` | `9ace7f16` | `no` |
| `rulespec-ch` | `7daf80c4` | `08096273` | `ch`, `ch-zh` |
| `rulespec-fr` | `6e52e154` | `c38c40d0` | `fr` |

Each repository keeps an empty three-key toolchain and `<pin-me>` workflow inputs on
purpose. A valid toolchain must bind a signed immutable corpus release; inventing
those hashes would create a false validation claim. The current encoder also rejects
the older BE/NZ reusable-workflow pin `842c69…`, so workflow pins must be selected in
the dedicated post-release dependency commit.

## Validation evidence

- Corpus loader/schema checks: 10 manifests, 17 unique source IDs, 17 unique citation
  paths, one jurisdiction/document-class scope per manifest, every extraction regular
  expression compiled.
- Corpus focused suite: 102 passed, 5 pre-existing dependency warnings.
- GitNexus staged impact check: low risk, no affected processes.
- Country layout suites: 7/7 passed in each of ES, NO, CH, and FR.
- Country inventory: zero atomic files and zero rules in every scaffold, as expected.
- Country oracle-pending ratchets: valid and empty in every scaffold.
- Replication suite: 34 passed (26 unchanged legal anchors plus 8 real-engine runtime
  tests).
- Runtime lint/format: all five new runtime/test files pass Ruff check and format.
- Dependency lock: `uv lock --check --offline` passes; the official Python client is
  pinned to engine commit `2c0e1edac0dccc355297eb9663e0aa0c4e97e5b4`.

## Exact blockers observed

- Official-source extraction raises `NameResolutionError` for `www.boe.es`; raw-IP
  outbound access is also unavailable.
- Git operations fail with `Could not resolve host: github.com`.
- `gh auth status` reports the active `MaxGhenis` token as invalid.
- `agent-secret search github` reports that the approved secret store needs to be
  unlocked/initialized; no secret value was requested or exposed.
- `axiom-encode encode` and formal validation correctly reject the placeholder
  toolchains before generation.
- Even with a valid toolchain, the current workflow requires the protected corpus
  release keyring/signing broker. Apply additionally requires the protected supervisor
  and `apply_ed25519` signer FD. The installed verification-only supervisor is older
  (`0.2.1298`) than the selected encoder (`0.2.1738`) and no production apply signer is
  provisioned to this session.

## Resume sequence

1. Restore terminal DNS/outbound connectivity. Re-authenticate `gh` for Max's account
   and unlock the approved `agent-secret` helper without pasting credentials into the
   session.
2. Publish `axiom-corpus` commit `65abb900`, run all 10 official-document extractions,
   inspect coverage, sign the ingest manifests, and cut immutable signed country
   releases.
3. Create `TheAxiomFoundation/rulespec-es`, `rulespec-no`, `rulespec-ch`, and
   `rulespec-fr`; add remotes and push the existing clean histories.
4. Land dedicated three-key toolchain and compatible reusable-workflow pin commits.
5. Run supervised `axiom-encode encode ... --apply` for every national and
   subjurisdiction source unit, then run compile, companion tests, proof validation,
   money-atom validation, manifest census, inventory, and full CI.
6. Encode only the verified 2026 Zürich tariff and record the missing 2022 tariff as a
   typed gap; do not guess. Encode the now-verified 2022 CGI Article 977 brackets.
7. Lock the exported rule/input contract, add all eight ProgramSpec scenario overlays,
   compose and compile their artifacts, switch the existing calculator signatures to
   the fail-closed runtime, and preserve explicit bespoke access only as the comparison
   oracle/custom-schedule extension.
8. Run the unchanged 26 tests through the Axiom defaults, generate the eight-scenario
   cent comparison table, rebuild package artifacts reproducibly, update this report,
   and push every branch.

## Scope integrity

No deck slide source, staged OBBBA deliverable, or Gmail draft was included in any
migration commit. Concurrent user-owned deck/chart edits remain outside these commits.
