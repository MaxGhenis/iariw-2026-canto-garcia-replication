# Axiom RuleSpec migration progress

## State

- Externally blocked after exhausting supported local source, composition, and
  runtime paths without bypassing Axiom's signed-apply trust boundary. France
  additionally needs an official DILA LEGI/PISTE ingestion adapter.
- Constraint: all production calculations must execute real composed RuleSpec
  artifacts through the Axiom rules engine; no parallel hand-written evaluator.

## Done

- Confirmed the replication repository and the four country repositories are
  present locally.
- Recorded the standing requirement to preserve the 26 existing oracle tests,
  keep paper scenarios as overlays, and avoid all out-of-scope presentation and
  communication artifacts.
- Independently ran 41/41 replication tests: 20 original schedule cases, 6
  original index/long-run cases, 3 legal-correction regressions, and 12
  synthetic contract tests that execute the real Rust engine.
- Confirmed the current calculator still uses bespoke schedules and every
  country repository contains zero atomic RuleSpec modules and zero overlays.
- Confirmed no protected Axiom signer is attached. A names-only credential
  inventory found the relevant Axiom key entries without reading them;
  production apply remains GitHub-Actions-only.
- Added the verified historical Zürich StG § 47 source that governed tax year
  2022 to the corpus intake branch (`6cfb8231`), while retaining the 2026
  indexed ESTV table as a separate vintage.
- Confirmed two latent bespoke-oracle defects: jointly assessed Norwegian
  spouses have a doubled top-rate threshold, and Spanish IP bracket integration
  drifts one cent from the statute's mandatory quota anchors at two edges.
- Corrected both defects in the comparison path and added the verified 2022
  Zürich tariff without altering either original test file. The full suite now
  passes 41/41, including three legal-correction regressions and 12 synthetic
  real-engine contract tests.
- Expanded the source intake to 11 manifests and 19 documents, added the
  retroactive ITSGF exemption amendment, split Zürich statute/guidance scopes,
  narrowed overbroad Swiss, Spanish, and Norwegian slices, and updated the Spain
  and Zürich source maps. The corpus branch is pushed through `574513cc`.
- Completed disposable live extraction with full coverage for 10 of 11
  manifests (18 of 19 documents). Légifrance challenges the historical French
  page; DILA's official bulk archive is reachable but needs a tar/XML importer,
  and no extracted outputs have been committed or signed.
- Pinned both the compiled artifact and engine executable to externally supplied
  SHA-256 digests and re-check both immediately before execution.
- Confirmed the only available local-dev signer produces nonpublishable output;
  a guarded dev release additionally requires isolated S3/Supabase services and
  root-owned supervisor provisioning unavailable in this sandbox. The required
  output report now contains the exact production resume sequence.
- Restored GitHub authentication, created the four public organization country
  repositories, and pushed each `main` history. Their initial workflow events
  fail before jobs start because signed-release and reusable-workflow pins are
  intentionally still `<pin-me>`.
- Opened corpus PR `TheAxiomFoundation/axiom-corpus#624`; it is
  mergeable/clean with all applicable CI green and is ready for maintainer
  review/merge. CHF/NOK engine PR
  `TheAxiomFoundation/axiom-rules-engine#165` passed full CI and merged to
  `main` as `bb4b568`; the latest published engine release remains `v0.2.2`.
- Confirmed no Actions workflow extracts or ingest-signs corpus documents. A
  protected key-holder must create those artifacts; same-repository PR CI then
  verifies their signatures. Publication and activation are not safe before
  those artifacts and canonical release selectors exist.
- Opened `TheAxiomFoundation/axiom-corpus#625` to track the official DILA LEGI
  historical-statute importer required by France.

## Next

1. Add the official French LEGI ingestion adapter.
2. Have the protected key-holder extract/sign the corpus artifacts, merge them
   through same-repository CI, publish immutable releases, and run supervised
   encoding only through supported Axiom paths.
3. Once country artifacts exist, replace the calculator path with composition
   plus Axiom execution and run the immutable oracle suite.
4. Add eight ProgramSpec scenarios and cent-parity comparison, update the
   canonical report, and push.
