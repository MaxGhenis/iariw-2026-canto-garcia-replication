# Axiom RuleSpec migration progress

## State

- Externally blocked after exhausting supported local source, composition, and
  runtime paths without bypassing Axiom's signed-apply trust boundary.
- Constraint: all production calculations must execute real composed RuleSpec
  artifacts through the Axiom rules engine; no parallel hand-written evaluator.

## Done

- Confirmed the replication repository and the four country repositories are
  present locally.
- Recorded the standing requirement to preserve the 26 existing oracle tests,
  keep paper scenarios as overlays, and avoid all out-of-scope presentation and
  communication artifacts.
- Independently ran 34/34 replication tests: 26 byte-unchanged legal oracles and
  8 synthetic tests that execute the real Rust engine.
- Confirmed the current calculator still uses bespoke schedules and every
  country repository contains zero atomic RuleSpec modules and zero overlays.
- Confirmed terminal DNS, GitHub authentication, the agent secret store, and
  protected Axiom signer attachment are unavailable in this session.
- Added the verified historical Zürich StG § 47 source that governed tax year
  2022 to the corpus intake branch (`6cfb8231`), while retaining the 2026
  indexed ESTV table as a separate vintage.
- Confirmed two latent bespoke-oracle defects: jointly assessed Norwegian
  spouses have a doubled top-rate threshold, and Spanish IP bracket integration
  drifts one cent from the statute's mandatory quota anchors at two edges.
- Corrected both defects in the comparison path and added the verified 2022
  Zürich tariff without altering the original 26-test oracle file. The full
  suite now passes 37/37, including three new legal-correction regressions and
  eight synthetic real-engine contract tests.
- Expanded the source intake to 19 documents with the retroactive ITSGF
  exemption amendment and updated the Spain and Zurich source maps. This closes
  the legal-source gaps but not the signed corpus/apply prerequisite.
- Confirmed the only available local-dev signer produces nonpublishable output;
  a guarded dev release additionally requires isolated S3/Supabase services and
  root-owned supervisor provisioning unavailable in this sandbox. The required
  output report now contains the exact production resume sequence.
- Pushed the coordination, corpus, and engine branches. The country histories
  remain local pending authenticated creation of their organization repositories.

## Next

1. Finish the repository-creation/CI and source-value audits.
2. Attempt source extraction and supervised encoding only through supported
   Axiom paths; record any repeated hard blocker precisely.
3. Once country artifacts exist, replace the calculator path with composition
   plus Axiom execution and run the immutable oracle suite.
4. Add eight ProgramSpec scenarios and cent-parity comparison, update docs,
   push, and write the final report.
