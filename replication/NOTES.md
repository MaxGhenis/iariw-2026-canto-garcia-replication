# Parameter sources and open questions

Every schedule in `schedules.py` cites its source inline. This file registers the
primary sources reviewed from 23–28 Aug 2026 and the open questions only the
authors can resolve.

## Primary sources
- Ley 19/1991 (IP), BOE historical consolidation at 28 Dec 2022: https://www.boe.es/buscar/act.php?id=BOE-A-1991-14392&p=20221228&tn=1 — art. 30.2 state schedule (anchor-tested), art. 28 €700k, art. 4.Nueve €300k, art. 31 límite conjunto (60%, 80% max reduction).
- Ley 38/2022 (ITSGF), BOE historical consolidation at 28 Dec 2022: https://www.boe.es/buscar/act.php?id=BOE-A-2022-22684&p=20221228&tn=1 — brackets, original personal-obligation €700k mínimo exento, devengo 31 December, in force 29-12-2022, and IP credit. Real Decreto-ley 8/2023 art. 17: https://www.boe.es/buscar/act.php?id=BOE-A-2023-26452&p=20231228&tn=1 — removed the personal-obligation qualifier with retroactive effect from Ley 38/2022's entry into force.
- Madrid Decreto Legislativo 1/2010, art. 20 (100% rebate): https://www.boe.es/buscar/act.php?id=BOCM-m-2010-90068&p=20221222&tn=1
- Andalusia Decreto-ley 7/2022 (100% rebate operative for the 31 Dec 2022 accrual): https://www.juntadeandalucia.es/boja/2022/182/1
- Galicia Ley 18/2021 (25% from 2022): https://www.boe.es/eli/es-ga/l/2021/12/27/18; Ley 7/2022 (50% from 2023): https://www.xunta.gal/dog/Publicados/2022/20221230/AnuncioC3B0-271222-3_es.html
- Catalonia (500k threshold, 0.21–3.48% own scale, 2022–2025): https://atc.gencat.cat/es/tributs/impost-patrimoni/
- ITSGF outturn: https://www.lamoncloa.gob.es/serviciosdeprensa/notasprensa/hacienda/paginas/2023/200923-impuesto-solidaridad-grandes-fortunas.aspx (€623M, 12,010 taxpayers, Madrid €555M)
- AEAT IP 2022 statistics: 230,365 declarants / 185,101 with positive cuota / €1,250.0M (sede.agenciatributaria.gob.es, Estadística de los declarantes del IP 2022); 2023: 228,575 declarants, €1,926.3M.
- Norway: operative Storting tax decisions for 2022 (https://lovdata.no/dokument/LTI/forskrift/2021-12-14-3571) and 2023 (https://lovdata.no/dokument/LTI/forskrift/2022-12-13-2199); Skatteetaten Forskuddsmeldingen 2022 (https://www.skatteetaten.no/rettskilder/type/skattedirektoratets-meldinger/forskuddsmeldingen-2022/) and 2023 (https://www.skatteetaten.no/rettskilder/type/skattedirektoratets-meldinger/forskuddsmeldingen-2023/), plus the historical housing-rate page (https://www.skatteetaten.no/satser/formuesverdi-bolig/?year=2022 and `year=2023`) for allowances and asset valuation.
- Zurich: official historical StG ZH Nachtrag 115, https://www.zh.ch/de/politik-staat/gesetze-beschluesse/gesetzessammlung/zhlex-ls/erlass-631_1-1997_06_08-1999_01_01-115.html — the § 47 single/married tariff in force for 2022; ESTV Kantonsblatt ZH, https://www.estv2.admin.ch/stp/kb/zh-de.pdf — the distinct 2026-indexed § 47 tables used by the original paper oracle; formal cantonal 99% factor resolution: https://www.zh.ch/de/politik-staat/gesetze-beschluesse/gesetzessammlung/zhlex-ls/erlass-631_21-2021_12_14-2022_01_26-116.html; City of Zurich 119% factor in the official 2023 accounts: https://www.stadt-zuerich.ch/content/dam/web/de/aktuell/publikationen/2024/rechnung/20240326-rechnung-23-medienkonferenz.pdf; family unit: Art. 3(3) StHG on Fedlex (https://www.fedlex.admin.ch/eli/cc/1991/1256_1256_1256/de).
- France: archived 2022 CGI IFI chapter, Articles 964–983: https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069577/LEGISCTA000036384995/2022-03-02/ — €1.3M trigger, exact Article 977 scale and décote, 30% main-residence abatement, and 75% plafonnement.
- Panel de Hogares access: https://www.ief.es/investigacion/Est_panelHogares.vbhtml and IEF DT 5/2024 (https://www.ief.es/docs/destacados/publicaciones/documentos_trabajo/2024_05.pdf) — joint INE–AEAT–IEF product, waves 2016–2023, M714 wealth-tax file, free under the petition protocol; covers the common fiscal territory only (excludes Basque Country and Navarre).
- EFF 2022: Banco de España, mean €309k / median €142.7k per household (Documento Ocasional 2413).

## Vintage caveats (encoded honestly, flagged here)
- The Zurich 2022 source gap is closed. The replication keeps the historical
  2022 StG table (allowances CHF 77k/154k) distinct from the Kantonsblatt edition
  marked "gültig ab Steuerperiode 2026" (CHF 81k/161k). The unchanged original
  oracle expects the latter; the legal 2022 comparison uses the former.
- The IFI mid-bracket edges (2.57M / 5M / 10M at 0.7/1/1.25%) were verified
  line-by-line against the archived 2022 text of CGI art. 977. This former gap is
  closed.
- `NOK_PER_EUR_2022 = 10.10` is a rough annual average for narrative conversions only.

## Axiom migration status

- Eleven official-document intake manifests covering 19 source documents are
  committed and pushed in `axiom-corpus` through `574513cc`. The four country
  repositories map every intended citation root and include the `es-md`,
  `es-an`, `es-ga`, and `ch-zh` namespaces.
- The replication package pins the official Axiom Python client and has a fail-closed
  real-engine runtime contract. Callers must supply independent artifact and
  executable SHA-256 pins, and the runtime rechecks both files immediately before
  execution. Its 12 focused runtime contract tests use a synthetic composition
  compiled and executed through the Rust engine; no bespoke fallback is
  available on that path.
- Atomic country modules are not yet present. Disposable live extraction is
  coverage-complete for 10 of 11 manifests; France needs an official DILA LEGI
  tar/XML or credentialed PISTE adapter because Légifrance challenges direct
  retrieval. No extracted output is committed or signed. Axiom also requires a
  protected key-holder to create signed ingest manifests, then a signed corpus
  release plus the protected supervisor/signing broker before supervised apply.
  No GitHub Action performs the extraction or ingest signing. The empty
  toolchains and workflow placeholders are therefore deliberate, not validation
  claims.

## Source-audit implementation gaps

- The current three-argument Spanish joint-limit comparator covers the headline
  60% cap and 80% maximum reduction only. Full Article 31 encoding must also model
  personal-obligation scope, the specified gains/dividend adjustments,
  non-income-producing assets, and joint-return allocation.
- A complete Norwegian taxable-net-wealth base must apply the proportional debt
  reduction associated with discounted assets under skatteloven § 4-19. The
  existing valuation helpers do not yet accept the debt composition needed to do so.

## Open questions for the authors (each blocks exact replication)
1. Which real-estate value enters each scenario's taxable base — declared/cadastral
   or ×3.08 EFF-market? (Paper p.9 vs slides contradict; Zurich's 70% and Norway's
   25% are defined on market values.)
2. Which ratio was applied, 3.0838 or 3.1125 (both printed on p.39)?
3. Sim. 2: are regional *scales and thresholds* retained (as Table A.8's overlap
   matrix implies) or harmonized to the state €700k (as Table A.2 says)?
4. Is the 60% IRPF–IP limit active in Sims 1–3 and Piketty, and with what revenue
   effect? (Table A.8's 3,577 IP payers with zero Piketty liability suggest it is.)
5. Zurich: statutory tariff only, or × Steuerfuss (≈2.18)? Which allowance vintage?
6. The 17 regional schedules "replicated in full detail" (fn. 6): please publish the
   parameter tables — this package has slots ready for them.
