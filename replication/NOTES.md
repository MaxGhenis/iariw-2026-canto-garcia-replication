# Parameter sources and open questions

Every schedule in `schedules.py` cites its source inline. This file registers the
primary sources actually consulted (all fetched during the adversarial review,
23–25 Aug 2026) and the open questions only the authors can resolve.

## Primary sources
- Ley 19/1991 (IP), consolidated: https://www.boe.es/buscar/act.php?id=BOE-A-1991-14392 — art. 30.2 state schedule (anchor-tested), art. 28 €700k, art. 4.Nueve €300k, art. 31 límite conjunto (60%, 80% max reduction).
- Ley 38/2022 (ITSGF), consolidated: https://www.boe.es/buscar/act.php?id=BOE-A-2022-22684 — brackets, €700k mínimo exento, devengo 31 December, in force 29-12-2022, IP credit; prorogued by RDL 8/2023.
- Andalusia Decreto-ley 7/2022 (100% rebate, effects from 1 Jan 2022): https://www.juntadeandalucia.es/boja/2022/182/1
- Catalonia (500k threshold, 0.21–3.48% own scale, 2022–2025): https://atc.gencat.cat/es/tributs/impost-patrimoni/
- ITSGF outturn: https://www.lamoncloa.gob.es/serviciosdeprensa/notasprensa/hacienda/paginas/2023/200923-impuesto-solidaridad-grandes-fortunas.aspx (€623M, 12,010 taxpayers, Madrid €555M)
- AEAT IP 2022 statistics: 230,365 declarants / 185,101 with positive cuota / €1,250.0M (sede.agenciatributaria.gob.es, Estadística de los declarantes del IP 2022); 2023: 228,575 declarants, €1,926.3M.
- Norway: https://www.skatteetaten.no/en/rates/wealth-tax/?year=2022 and ?year=2023; residence valuation: skatteetaten.no "Taxable value of residential properties"; Forskuddsmeldingen 2022 (0.95%/1.10%, 25%-to-NOK-10M-then-50%, secondary 95%, shares 75%).
- Zurich: ESTV Kantonsblatt ZH, https://www.estv2.admin.ch/stp/kb/zh-de.pdf — § 47 Grundtarif tables (single/married) as encoded; Steuerfuss: canton 99% (2022–23), City of Zurich 119%; ESTV "Vermögenssteuer natürlicher Personen" dossier — family taxation (Art. 3(3) StHG).
- France: https://www.service-public.gouv.fr/particuliers/vosdroits/F563 (trigger €1.3M, 30% abatement); impots.gouv.fr "Calcul de l'IFI" (barème from €800k, décote 1.3–1.4M, 75% plafonnement).
- Panel de Hogares access: https://www.ief.es/investigacion/Est_panelHogares.vbhtml and IEF DT 5/2024 (https://www.ief.es/docs/destacados/publicaciones/documentos_trabajo/2024_05.pdf) — joint INE–AEAT–IEF product, waves 2016–2023, M714 wealth-tax file, free under the petition protocol; covers the common fiscal territory only (excludes Basque Country and Navarre).
- EFF 2022: Banco de España, mean €309k / median €142.7k per household (Documento Ocasional 2413).

## Vintage caveats (encoded honestly, flagged here)
- The Zurich Grundtarif tables are the Kantonsblatt's published edition marked
  "gültig ab Steuerperiode 2026" (post-indexation). The 2022-vintage brackets were
  slightly lower (allowances ~CHF 77k/154k). If the authors state their vintage, swap
  the table — bracket structure is identical.
- The IFI mid-bracket edges (2.57M / 5M / 10M at 0.7/1/1.25%) follow the published
  barème as summarized by impots.gouv.fr; verify line-by-line against CGI art. 977
  before quantitative use.
- `NOK_PER_EUR_2022 = 10.10` is a rough annual average for narrative conversions only.

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
