# Speaker notes — discussant presentation of Cantó & García-Rodríguez (2026)

**Session:** Wealth and fiscal and monetary policy · Fri 28 Aug 2026, 4:00–5:30pm, Room A2 (NBB Auditorium, Brussels) · chair Rutger Kemels (NBB)
**Paper:** "Progressivity and Redistribution of Wealth Taxation in Spain: a Microsimulation Analysis using Tax Register Data" — Olga Cantó & Francisco García-Rodríguez (Universidad de Alcalá / EQUALITAS), EQUALITAS WP-95, April 2026, 47pp.
**Format:** IARIW flipped — discussant presents the paper (~15 min), then the authors respond.
**Slot caveat:** verified on the online program 23 Aug — this paper stayed at 4pm (the organizers moved #287 to 2pm instead of moving #195 as David Johnson first proposed). Max's own #364 response runs in parallel in Room A1 4:00–5:30; coordinate with both chairs on paper order before the session.
**Deck:** 26 slides. 1–20 = the paper (7–12 = discussant-added schedules build); 21 divider; 22–25 discussion; 26 close.

Timing guide (15 min): setting 2 min (slides 2–4), data + designs 1.5 min (5–6), schedule build 3.5 min (7–12), results 3.5 min (13–20, lean on 15/17/18), discussion 4 min (22–25), close 0.5 (26).

---

## 1 · Cover
Who's who; flipped format for anyone unfamiliar. Olga and Francisco respond after. One line on my seat: I build open-source tax-benefit microsimulation at PolicyEngine, so this is a paper after my own heart.

## 2 · Wealth concentration in Spain has been rising
EFF trend (their Fig. 1, p.17, and intro p.1): top 1% share 13.3% (2002) → just over 21% (2022); next 9% 29.1% → 32.6%; p51–90 44.8% → ~39%; bottom 50% 12.8% → 7.1%. Wealth taxes retreating: 12 OECD countries in 1990 → Spain, Norway, Switzerland by 2023 (p.3); France ISF → IFI real-estate-only in 2018 (p.3, p.5). Spain = natural laboratory (p.2): progressive rates + regional autonomy.

## 3 · The Spanish wealth tax (IP)
History (p.3): introduced 1977 (monitoring tool for the new income tax), permanent 1991, suspended 2008, back 2011, "temporary" renewed annually. Design (p.3–4): €700k general exemption + €300k main residence; state schedule 0.2–3.5%; joint IRPF–IP cap at 60% of the income-tax base with a 20% minimum wealth-tax payment. Regions since 2011 set rates/thresholds/rebates: Madrid and Andalusia 100% rebate in 2022 (p.4, footnote 9 p.20); Catalonia/Extremadura/Valencia keep high burdens → horizontal inequity + fiscal competition (p.4). Punchline from their data (Table 3 p.21): 170,404 effective taxpayers (0.38% of 44.9M individuals), €1,125.58M, wealth Gini reduction 0.0000%.
Scope note to say out loud (their footnote 2, p.5): the ITSGF "solidarity" surcharge is deliberately excluded from the baseline — I come back to it in the discussion.

## 4 · This paper
Questions (p.2): progressivity + revenue; redistribution of the revenue; long-run concentration; who pays. Contributions (p.2): administrative-data design comparison; level/distance decomposition; long-run framework (Durán-Cabré & Esteller-Moré); taxpayer profiles.

## 5 · Data
PH (Sec. 4.1 p.7–8): compiled by AEAT, provided by IEF; 2022 wave ~950k households / 2.7M individuals sampled; weighted 17.67M households / 44.86M individuals (Table A.1 p.38). Links IRPF returns, IP (wealth-tax) declarations, third-party reports; covers non-filers. Real estate at cadastral values → market via EFF ratio ×3.08 (eq. A.1 p.39 — note the paper prints both 3.0838 and 3.1125; slides say ×3.08). Key stats (Table A.1): mean €160,540 / median €60,372 all individuals; filers 170,408 weighted (28,329 sample), mean €2.05M / median €1.43M. Limits they flag (p.8): business assets only for IP filers; dependents info gaps; liabilities not decomposed.

## 6 · Eight designs
Their Table 1 (p.11) + A.2 (p.40). IP baseline replicates all regional schedules for 2022 (footnote 6 says fiscal year 2022; p.9 text says benchmark legislation 2023 — small internal wobble, don't raise unless asked). NO: flat 1% (0.3% state + 0.7% municipal), threshold ~€160k, residence at 25% of market value, married double threshold. CH: Canton of Zurich schedule, real estate 70%. FR: IFI, real estate only, €1.3M threshold, 0.5–1.5%. Sim. 1: exemption €300k. Sim. 2: no regional deductions/rebates. Sim. 3: both. Piketty: 0/0.5/1/2% above 200k/1M/5M. Foreign designs drop the IRPF–IP cap (p.10).

## 7–11 · Schedule build, one policy at a time (discussant-added)
Own it out loud once, at slide 7: "the next five charts are mine, drawn from the statutes — because you can't feel the paper's results without knowing each schedule's shape." Each slide: text panel left, MTR (top) + ATR (bottom) stacked right, prior systems faded in place. ~35–40 seconds each; don't rush — this IS the setup for everything after.
- **7 Zurich**: family unit; Grundtarif 0–3‰ ×2.18 Steuerfuss → top ≈0.65%; bites from ~CHF 81k. Gentlest, broadest; Swiss wealth taxes ≈1% of GDP (OECD 2018, 2016 figure).
- **8 Norway**: NOK 1.7M threshold (~€168k), 0.95%/1.10% above NOK 20M; residence at 25% of market value. Near-flat wall; ≈0.48% of GDP in 2022.
- **9 France**: IFI real-estate only; €1.3M trigger with ≈€1,250 entry cliff (schedule counts from €800k), décote to €1.4M, 0.5–1.5%. Nothing → cliff → modest.
- **10 Piketty**: 0.5/1/2% above 200k/1M/5M on everything (paper variant; book adds 0.1% bottom, 5–10% top).
- **11 Spain (punchline)**: €700k exemption then 0.2→3.5% — the STEEPEST top schedule of the five. Land the line: "on paper, Spain out-taxes everyone at the top — the whole paper is about why so little of this line survives."

## 12 · All five together (recap)
One breath over the combined MTR chart: steepest-on-paper Spain vs earliest-and-flattest Norway. Bridge to methods/results: "their Figure 3 will show what's LEFT of these lines after exemptions, rebates, and the cap — that gap is the paper." Charts generated from the replication package's statute-anchored calculators (bracket-edge cross-checks); two-panel MTR+ATR standalone in the repo. NOK→EUR 10.10; CHF≈EUR.

## 13 · Methods
Kakwani K = C_t − G_pre (eq. 2 p.13); Suits (eq. 3); R–S = G_pre − G_post = t/(1−t)·K − D (eq. 1 p.12); level vs distance decomposition of ΔR–S (eq. 5–8 p.14, Díaz et al. 2010/2011); long-run: project wealth at constant g ∈ {1,2,3}% with/without the annual tax, T = 25/50/75/100 (p.15). Measured on individual and equivalized net wealth + equivalized market and disposable income.

## 14 · Result 1: AETR profiles (their Fig. 3 p.19)
IP: near zero until ~p99.3 (p.18) then rises modestly — only ~top 0.5% pay. NO: taxation from ~p80, smooth rise. CH: step ~p67, flat low. FR: lowest across most of the top (narrow base), crosses IP above p99.5. Piketty: steepest top gradient (to ~1.3% at p100); Sim. 3 next. Percentiles are over all 44.9M individuals.

## 15 · Result 2: headline table (their Table 3 p.21, net-wealth panel)
Read across IP → Piketty: taxpayers 170,404 → 11.0M; revenue €1,126M → €15,861M (14×); avg rate t 0.02% → 0.30%. Kakwani FALLS from 0.231 (IP) to 0.191 (NO) / 0.197 (Piketty); Suits 0.806 → 0.522/0.570. Only FR (K 0.244) and Sim. 2 (0.234) beat the IP on formal progressivity. Wealth Gini cuts are tiny in the short run (0.000%–0.080%). THE message: base breadth ↔ revenue; formal progressivity moves the other way.
(If asked about R–S units: Table 3's net-wealth R–S column is ×1000 vs Table A.4 — flagged in the review; I quote Gini-reduction % instead.)

## 16 · Result 3: decomposition (their Fig. 4 p.23)
All designs raise R–S vs IP; level effect (incidence) dominates everywhere; distance effect small and often negative for broad bases. Quote p.22: gains "driven primarily by the Level Effect". This is the paper's most honest self-diagnosis — the reforms redistribute by collecting more, not by being structurally more progressive.

## 17 · Result 4: child benefit (their Table 4 p.25)
Revenue recycled as universal per-child transfer: IP €149/child/yr; NO €2,049; CH €642; FR €191; Sim. 1 €492; Sim. 2 €319; Sim. 3 €1,680; Piketty €2,103. Disposable-income Gini falls 0.48% (IP) → 4.58/4.21/4.87% (NO/S3/Piketty) — in POINTS that's 0.3779 → 0.3620/0.3595, i.e. 1.6–1.8 Gini points. (Their own slide says "4–5 Gini points" — it's 4–5 percent; I use the correct units and flag gently in discussion if useful.)

## 18 · Result 5: long run (their Fig. 5 p.28, Tables 5/A.5–A.7)
Equivalized top-1% share 14.67% at T=0 (g=2%): IP → 13.45% at T=100 (−1.2pp); NO → 9.13%; Piketty → 7.96%; Sim. 3 → 6.58% (largest fall). Long-run effective rates t_l/r at T=100: IP 1.95% of wealth; NO 22.3%; Piketty 21.9%; Sim. 3 15.3% (Table 5 p.26). Robustness: g = 1% and 3% similar (Tables A.5–A.7). Their own caveat (p.25): "not intended to predict… but rather to illustrate a fundamental mechanism" — honor it in the framing. Note the equivalized-Gini wrinkle (Table 5 bottom): under IP/CH/FR/Sim.1/Sim.2 the equivalized Gini RISES for decades before the mechanics bite.

## 19 · Result 6: who pays (their Fig. 6 p.29, Fig. 7 p.32, Table 6 p.31)
IP payers: predominantly 65+; FR similar (take-off after ~65 in Fig. 7). Broad bases shift the age curve left (CH/Piketty steepest around 50–60). Women less likely to pay under every design (Table 6: marginal effects −0.00005 FR to −0.0048 CH, all significant) — consistent with the gender wealth gap (they cite UK: ~68% of potential payers male, Advani et al. 2021). Household: multi-adult households less likely at same age.

## 20 · Their conclusions (p.33–34 + their deck)
Current IP: high formal progressivity, minimal effect; regional rebates create horizontal inequity. Reforms: broaden base + harmonize → 4.6–11M taxpayers, €12.7–15.9bn, real disposable-income redistribution once recycled, cumulative long-run concentration decline. Their policy line: gains come from base + incidence, not marginal-rate steepening.

## 21 · Divider
One breath. "Four comments — all offered in the spirit of making a genuinely valuable exercise sharper. Everything I'll say is documented, with sources, in a public repo I'll share at the end."

## 22 · Comment 1: the pre-ITSGF baseline
Lead gently: "the paper's institutional timing needs one correction with real consequences." Ley 38/2022 (BOE): in force 29 Dec 2022, devengo each 31 December → first tax year 2022 = their valuation date; extended indefinitely by RDL 8/2023 (paper's fn.2 says "2023–2024" — wrong). Ejercicio 2022: €623M from 12,010 taxpayers, €555M (89%) Madrid ≈ 49% of Sim. 2's incremental €1,279.6M. Then 2023 reality: Madrid suspended its rebate (Ley 12/2023) → AEAT 2023: €1,926.3M IP (+€676.3M, 90.6% from Madrid), ITSGF collapses to ~€35M. So "current law" raises ~€1.96bn, not €1.13bn — and the ITSGF's 60% shortfall vs its ~€1.5bn forecast is a live static-scoring lesson. The gift framing: 2023 = out-of-sample validation of Sim. 2, a novel contribution nobody else can do as easily as they can.
*Expected response (advocate-verified): exclusion was deliberate and disclosed (p.5, fn.2) for comparability; will fix the dating; Sim. 2 answers a broader question than the ITSGF (whole schedule vs >€3.7M). All true — my point is labeling and the validation opportunity, not the design choice.*

## 23 · Comment 2: static ceilings, priced by their own citations
Ready-reckoner (labeled illustration): Advani-Tarrant 7–17% base loss per 1pp → Sim. NO €15.5bn → €12.8–14.4bn; Mas-Montserrat (their citation) −3.21% per 0.1pp ATR → ~8–10% off the three broad designs; Brülhart (their citation) ≥43% per 1pp = upper bound; Saez-Zucman themselves score with 15%/50% erosion — zero is outside the entire published range. Key twist: erosion scales with rates → hits Sim. 3 (top 3.5%) and Piketty harder than Norway's flat 1% → behavioral adjustment STRENGTHENS breadth-over-rates. Agrawal/Foremny/Martínez-Toledano (AEJ: Applied 2025, uncited): Madrid's PIT losses 6× wealth-tax losses; Madrid gains from harmonization — their Sim. 2/3 case, stronger. One-liners: Norway's own yield ~0.5% GDP vs Sim. NO's 1.13% of Spain's; Sims 1–3 keep the 60% cap = 92.6% of measured Spanish avoidance (Mas-Montserrat).
*Expected response: static-by-design (p.2, p.11, p.34); transplanted elasticities overstate because avoidance runs through features the reforms remove. Concede partially — then ask for the bounds column anyway.*

## 24 · Comment 3: two mechanical re-runs
(a) Equivalized long-run Gini: under uniform g the no-tax distribution is scale-invariant (our test verifies to 1e-12); with their C_t = 0.9744 and cumulative 0.50% at T=25 the max Gini move is ~0.17pt DOWN; Table 5 prints +1.04pt UP — 6× the bound, wrong sign; five designs stay above the starting Gini for a century; their p.27 "natural growth of wealth at the top" explanation is unavailable under their own uniform-g assumption (advocate verifier conceded this needs an audit). (b) Total wealth: every t and t_s/r implies ~€5.3T; Table A.1's mean×count = €7.2T (35% gap); EFF 2022 (€309k mean/household, BdE DO 2413) sides with €5.3T → A.1's descriptives look mis-vintaged, and t_s/r seeds the long-run tables. Smaller: R–S ×1000 units (Table 3 vs A.4); overlap matrix impossibilities (297,219 > 201,687; 72,186 < forced 170,404); 3.0838 vs 3.1125; 7/8/9 scenarios; declared-vs-market valuation base per scenario (Zurich housing base ≈ 2.16× the IP's legal base).
*Expected responses: R–S = thousandths for readability (concede note); A.1 audit ("earlier vintage of the cadastral adjustment"); overlap matrix "transposition errors, purely descriptive"; valuation = "statutory rules are part of design" — my ask: then report the revaluation/design split.*

Extra probe if the long-run discussion opens up (accrual mechanics): the projection pins each person's average rate at its year-0 value forever — the schedule is never re-applied to the growing stock. At g=2% wealth multiplies 7.2× over the century, yet nobody ever crosses the €700k threshold and no existing payer climbs a bracket. For progressive designs with fixed nominal thresholds that freezes the extensive margin and understates the long-run bite — differentially across designs (Norway's low flat threshold is least affected). Paper basis: p.15 "wealth is reduced each year by a constant ts/r"; Table 5 note.

## 25 · Comment 4: say the real finding + open the engine
Framing: abstract says reforms "increase tax progressivity"; Table 3: K 0.2313 → 0.1912 (NO), 0.1969 (Piketty), Suits 0.806 → 0.522/0.570; only FR and Sim. 2 raise K. Their own decomposition + conclusions credit incidence. The inverse trade-off IS the paper — own it. Also report the AEAT validation (they land −8%/−10% vs official 185,101/€1,250M — a strength they never claim). Replicability: PH is free to researchers under the IEF protocol (joint INE-AEAT-IEF product) — the data are open-ish; the CODE and parameters aren't (Zurich never states its tariff or Steuerfuss — statutory 0.3% vs ~0.65% top rate; EUROMOD can't simulate the IP at all: "lack of data on wealth impedes simulation," JRC country report). The ask: parameter appendix + code with the journal version. Then the reveal: we've already re-encoded all eight designs with 26 statute-anchored tests — github.com/MaxGhenis/iariw-2026-canto-garcia-replication — their parameters would complete it.
*Expected response: "working paper, no package yet; parameters come from public statutes; happy to commit to an appendix + code release." That's the win condition — get it said on the record.*

## 26 · Close
Three floor questions (valuation base + Piketty-on-declared-values decomposition; the 2023 out-of-sample test; the cap in Sims 1–3/Piketty and Table A.8's 3,577 IP payers escaping Piketty). Hand to Olga and Francisco. Repo URL on screen.

---

## Numbers most likely to be challenged (all sourced; URLs in REVIEW-APPENDIX.md)
- 170,404 payers / €1,125.58M baseline (Table 3 p.21) vs AEAT official 2022: 230,365 declarants, 185,101 with positive cuota, €1,250.0M (−7.9% / −10.0%). AEAT 2023: 228,575 declarants, €1,926.3M (+€676.3M, 90.6% Madrid).
- ITSGF: Ley 38/2022 in force 29-12-2022, devengo 31-12 → first ejercicio 2022; €623M / 12,010 taxpayers / Madrid €555M (Moncloa 20-9-2023); forecast ~€1.5bn; ~€35M by the 2024 campaign; Madrid rebate suspended by Ley 12/2023.
- Sim. 2 incremental revenue €1,279.59M (2,405.17 − 1,125.58); ITSGF share 623/1,279.59 = 48.7%.
- Kakwani falls: 0.2313 → 0.1912 (NO) / 0.1969 (Piketty); Suits 0.8055 → 0.5221/0.5701 (Table 3).
- Child benefit €149 → €2,103/child (Table 4); Gini cut 4.2–4.9 PERCENT = 1.6–1.8 points (0.3779 → 0.3595). Divisor = 7.543M minors in every row (recomputed); common-territory under-18s ≈ 7.7M (INE), national 8.2M.
- Equivalized long-run: 0.6402 → 0.6506 at T=25 under IP (+1.04pt) vs Kakwani bound ~0.17pt down; top-1% 14.67% → 9.13% (NO, −5.5pp, NOT >7pp), 7.96% (Piketty, −6.7pp), 6.58% (Sim. 3, −8.1pp) at T=100 g=2% (Table A.7).
- Wealth totals: t-implied ~€5.28–5.38T vs Table A.1's €7.20T (44,857,347 × €160,539.8); EFF 2022 household mean €309k → ~€5.46T.
- Behavioral anchors: Brülhart ≥43%/1pp (6y; mobility 24%, housing 21%); Jakobsen 19%/31% @8y, 30%/65% @30y, elasticity 1.15; Mas-Montserrat −3.21%/0.1pp, cap = 92.6% of avoidance, losses 2.75× 2011 revenue; Seim 0.09–0.27; Advani-Tarrant 7–17%/1pp, estimates "vary by a factor of 800"; Agrawal PIT losses 6× direct; S-Z 15%/50% evasion scenarios.
- Norway: 2022 rates 0.95%/1.10% (>NOK 20M), threshold NOK 1.7M/3.4M, residence 25% to NOK 10M then 50%, secondary 95%, shares 75%; formuesskatt NOK 26.5bn (2022) ≈ 0.48% GDP; Sim. NO = 1.13% of Spain's GDP (€1,373,629M INE 2022).
- Zurich: Grundtarif 0–3‰; allowances CHF 81k/161k (2026 tables; 2022 vintage lower); Steuerfuss 99% + 119%; ESTV: spouses taxed jointly, minors attributed → the paper's 12.4M individual taxpayers ≠ Swiss family unit.
- IFI: trigger €1.3M, barème from €800k, 30% residence abatement, 75% income plafonnement (vs paper's "no analogue" for the Spanish cap).
- Foral: weighted 44.86M = common territory (Spain 47.43M − Basque 2.18M − Navarre 0.66M, INE); "Basque/Navarre/foral" appear nowhere in the paper.
- Citations: DCE-M long-run framework = IEB WP 2019/09 (cited "2021/04" is a COVID exams paper); Kleven et al. 2011 (cited for Danish wealth data) is a tax-audit RCT; DCE-M 2014 concluded "el impuesto sobre el patrimonio debe eliminarse."
- Paper status: under review at International Tax and Public Finance (Research Square rs-9834492, 27 May 2026).
