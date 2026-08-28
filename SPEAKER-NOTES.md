# Speaker notes — discussant presentation of Cantó & García-Rodríguez (2026)

**Session:** Wealth and fiscal and monetary policy · Fri 28 Aug 2026, 4:00–5:30pm, Room A2 (NBB Auditorium, Brussels) · chair Rutger Kemels (NBB)
**Paper:** "Progressivity and Redistribution of Wealth Taxation in Spain: a Microsimulation Analysis using Tax Register Data" — Olga Cantó & Francisco García-Rodríguez (Universidad de Alcalá / EQUALITAS), EQUALITAS WP-95, April 2026, 47pp.
**Format:** IARIW flipped — discussant presents the paper (~15 min), then the authors respond.
**Slot caveat:** verified on the online program 23 Aug — this paper stayed at 4pm (the organizers moved #287 to 2pm instead of moving #195 as David Johnson first proposed). Max's own #364 response runs in parallel in Room A1 4:00–5:30; coordinate with both chairs on paper order before the session.
**Deck:** 27 slides. 1–21 = the paper (6–12 = discussant-added design-path sequence; 13 = paper-order design table); 22 divider; 23–26 discussion; 27 close.

Timing guide (15 min): setting 2 min (slides 2–4), data 0.75 min (5), design paths 3.25 min (6–12), design synthesis + methods 1.25 min (13–14), results 3.25 min (15–21, lean on 16/18/19), discussion 4 min (23–26), close 0.5 (27).

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

## 6–11 · Six design paths in the paper's order (discussant-added)
Own it at slide 6: "The next six charts are mine. I hold one transparent single-filer balance sheet fixed — 25% main residence, 75% other assets, pension rights outside plotted wealth — and apply each design's valuation and exemption rules. This is not a representative household; it isolates the rules." Top = tax on the next euro of total non-pension wealth; bottom = tax divided by that wealth. Prior paths fade in place. ~30–35s each.
- **6 IP baseline (paper row 1)**: apply the €300k main-residence relief and €700k general exemption to the 25/75 portfolio, then the state 0.2→3.5% schedule. Regional scales/rebates and the income cap stay outside the illustration, so this is not the 17-region baseline; the same solid state path is later the reference for Sim. 2. Land: "late but fierce — Spain's state line has the highest top rate, while the paper is about what survives the other layers."
- **7 Sim. NO (paper row 2)**: Table A.2 is unambiguous: ~€160k individual threshold, double for married couples, then a true flat 1%. The paper values all housing at 25%. With residence = 25% of our portfolio, 75% other assets, the assessable share is 25%×25% + 75% = 81.25%; hence the chart's post-entry MTR is 0.8125% of the next total-wealth euro. Distinguish this paper variant from actual 2022 law (0.95% / 1.10%, residence 25% then 50%).
- **8 Sim. CH (paper row 3)**: Zurich values the 25% residence share at 70% and other assets fully, so 92.5% of the common path enters before allowances. Pensions are described as exempt (paper p.5). The explicit reference is §47's 2026-indexed tariff 0–3‰ ×2.18 for canton 99% + City of Zurich 119% using 2022–23 factors and the ECB 2022 average (€1 = CHF 1.0047). That gives a top path MTR of ≈0.60%; it is a mixed-vintage reference, not a recovered paper parameter. Spouses are jointly taxed and minors attributed.
- **9 Sim. FR (paper row 4)**: only the 25% residence share enters; apply the 30% main-home abatement, so 17.5% of total wealth is assessable. The €1.3M IFI trigger therefore arrives at ~€7.43M total wealth on this deliberately property-light path; ≈€1,250 falls due just above entry, then the 0.5–1.5% barème applies. Real households with other property can enter earlier. France also has its own 75% income plafonnement.
- **10 Sims 1–3 (paper rows 5–7)**: narrate in table order. Sim. 1 = €300k general exemption, regional deductions retained; Sim. 2 = €700k, deductions/rebates removed; Sim. 3 = both changes. The dashed €300k state path references Sims 1/3; the earlier solid €700k path references Sim. 2. Exact regional scales remain unpublished. Effective taxpayers: 1.8M / 201,687 / 4.6M.
- **11 Sim. Piketty (paper row 8)**: 0.5% / 1% / 2% above €200k / €1M / €5M, not enacted law. The text calls it a full net-wealth base, but neither Table A.2 nor the methods publish the asset-level or pension treatment or whether an income cap carries over. Our path assumes full non-pension net wealth and labels that choice.

## 12 · One portfolio makes valuation choices visible (recap)
One breath over the combined MTR chart: the ordering now matches Tables 1/A.2. Norway's true 1% becomes 0.8125% per next total-wealth euro because its 25% housing valuation operates on a portfolio with 25% housing. Zurich reaches ~0.60%; France enters only near €7.4M because this path has just 25% main residence; Spain's state schedule reaches 3.5%. Bridge: "six visible paths, but eight simulations — the table next decodes the Spanish reforms." Calculators retain statute-anchored schedule tests and numeric-derivative checks.

## 13 · Eight designs, in the paper's table order
Their Tables 1 (p.11) + A.2 (p.40): IP, NO, CH, FR, Sim. 1, Sim. 2, Sim. 3, Piketty. IP baseline replicates all regional schedules for 2022 (footnote 6 says 2022; p.9 text says benchmark legislation 2023 — small internal wobble, don't raise unless asked). Repeat only what the charts could not resolve: the paper says NO/CH pension rights are exempt but never documents the asset-level implementation; business assets are observed only for IP filers; liabilities are not decomposed; Piketty's base is called full net wealth without an asset map. Foreign designs drop Spain's cap, although France has its own 75% plafonnement. This is the setup for the reproducibility ask on slide 26.

## 14 · Methods
Kakwani K = C_t − G_pre (eq. 2 p.13); Suits (eq. 3); R–S = G_pre − G_post = t/(1−t)·K − D (eq. 1 p.12); level vs distance decomposition of ΔR–S (eq. 5–8 p.14, Díaz et al. 2010/2011); long-run: project wealth at constant g ∈ {1,2,3}% with/without the annual tax, T = 25/50/75/100 (p.15). Measured on individual and equivalized net wealth + equivalized market and disposable income.

## 15 · Result 1: AETR profiles (their Fig. 3 p.19)
IP: near zero until ~p99.3 (p.18) then rises modestly — only ~top 0.5% pay. NO: taxation from ~p80, smooth rise. CH: step ~p67, flat low. FR: lowest across most of the top (narrow base), crosses IP above p99.5. Piketty: steepest top gradient (to ~1.3% at p100); Sim. 3 next. Percentiles are over all 44.9M individuals.

## 16 · Result 2: headline table (their Table 3 p.21, net-wealth panel)
Read across IP → Piketty: taxpayers 170,404 → 11.0M; revenue €1,126M → €15,861M (14×); avg rate t 0.02% → 0.30%. Kakwani FALLS from 0.231 (IP) to 0.191 (NO) / 0.197 (Piketty); Suits 0.806 → 0.522/0.570. Only FR (K 0.244) and Sim. 2 (0.234) beat the IP on formal progressivity. Wealth Gini cuts are tiny in the short run (0.000%–0.080%). THE message: base breadth ↔ revenue; formal progressivity moves the other way.
(If asked about R–S units: Table 3's net-wealth R–S column is ×1000 vs Table A.4 — flagged in the review; I quote Gini-reduction % instead.)

## 17 · Result 3: decomposition (their Fig. 4 p.23)
All designs raise R–S vs IP; level effect (incidence) dominates everywhere; the distance contribution is negative for NO, CH, and Piketty. Negative does **not** mean those taxes are regressive. It is a change relative to the current IP after separating the incidence channel: CH remains progressive in absolute terms (Kakwani K = 0.1202 > 0), but less progressive than IP (K = 0.2313); its much broader, low-rate base spreads liability farther down the Spanish wealth distribution. Mechanics from eqs. 5–8 (p.14): compare current IP (0) with reform (1), writing ΔR–S = LE + DE. LE assigns the change in average tax incidence t — hence the change in mean net-of-tax wealth — to the level channel. DE uses the change in the sum of pairwise wealth distances, normalized by population, mean wealth, and post-reform retention, as the structural-progressivity/re-ranking channel. This is an accounting decomposition, not a causal or behavioral one; it does not itself distinguish base breadth from rate design. The authors did not invent it: they explicitly follow Díaz, Garcimartín, and Ruiz-Huerta (2010, 2011), especially “Progresividad y redistribución en reformas fiscales. Los efectos nivel y distancia” (Revista de Economía Aplicada 19(57):97–116). Equation 8 has a sign inconsistency as printed: its first numerator, (1−t¹)−(1−t⁰), equals t⁰−t¹, while the displayed final expression is t¹−t⁰. The intended positive-incidence convention is inferable from the final expression and prose, but ask the authors to correct it. Quote p.22: gains are "driven primarily by the Level Effect". This is the paper's most honest self-diagnosis — the reforms redistribute mainly because they collect more; the distance channel is secondary, not zero.

## 18 · Result 4: child benefit (their Table 4 p.25)
Revenue recycled as universal per-child transfer: IP €149/child/yr; NO €2,049; CH €642; FR €191; Sim. 1 €492; Sim. 2 €319; Sim. 3 €1,680; Piketty €2,103. Table 3 gives tax-only disposable-income Gini reductions; Table 4 gives tax + benefit. Comparing their rounded R–S values implies that recycling adds 0.10 Gini point under IP, 1.32 under Norway, 0.44 under CH, 0.13 under FR, 0.34 under Sim. 1, 0.22 under Sim. 2, 1.09 under Sim. 3, and 1.35 under Piketty. The combined effect is 2.2–5.9× the tax-only effect; for NO/Sim. 3/Piketty, the benefit accounts for 69–76% of the combined reduction. Be precise: this is an inferred difference, not a transfer-only counterfactual or formal decomposition reported by the paper. Combined disposable-income Gini falls 4.58/4.21/4.87% under NO/S3/Piketty — 1.6–1.8 Gini points, not the authors' slide claim of "4–5 Gini points."

## 19 · Result 5: long run (their Fig. 5 p.28, Tables 5/A.5–A.7)
Equivalized top-1% share 14.67% at T=0 (g=2%): IP → 13.45% at T=100 (−1.2pp); NO → 9.13%; Piketty → 7.96%; Sim. 3 → 6.58% (largest fall). Long-run effective rates t_l/r at T=100: IP 1.95% of wealth; NO 22.3%; Piketty 21.9%; Sim. 3 15.3% (Table 5 p.26). Robustness: g = 1% and 3% similar (Tables A.5–A.7). Their own caveat (p.25): "not intended to predict… but rather to illustrate a fundamental mechanism" — honor it in the framing. Note the equivalized-Gini wrinkle (Table 5 bottom): under IP/CH/FR/Sim.1/Sim.2 the equivalized Gini RISES for decades before the mechanics bite.

## 20 · Result 6: who pays (their Fig. 6 p.29, Fig. 7 p.32, Table 6 p.31)
IP payers: predominantly 65+; FR similar (take-off after ~65 in Fig. 7). Broad bases shift the age curve left (CH/Piketty steepest around 50–60). Women less likely to pay under every design (Table 6: marginal effects −0.00005 FR to −0.0048 CH, all significant) — consistent with the gender wealth gap (they cite UK: ~68% of potential payers male, Advani et al. 2021). Household: multi-adult households less likely at same age.

## 21 · Their conclusions (p.33–34 + their deck)
Current IP: high formal progressivity, minimal effect; regional rebates create horizontal inequity. Reforms: broaden base + harmonize → 4.6–11M taxpayers, €12.7–15.9bn, real disposable-income redistribution once recycled, cumulative long-run concentration decline. Their policy line: gains come from base + incidence, not marginal-rate steepening.

## 22 · Divider
One breath. "Four comments — all offered in the spirit of making a genuinely valuable exercise sharper. Everything I'll say is documented, with sources, in a public repo I'll share at the end."

## 23 · Comment 1: the pre-ITSGF baseline

**Opening line:** “I think the pre-ITSGF benchmark is a defensible way to compare designs. My suggestion is to label it more explicitly and turn the subsequent policy change into a validation exercise.”

**Walk-through:**

1. **What the benchmark is.** The simulations hold 2022 wealth fixed and model the ordinary IP without the new solidarity tax. That is a useful counterfactual, but it is not the full statutory environment applying on 31 December 2022.
2. **The date to correct.** Ley 38/2022 entered into force on 29 December 2022 and the tax accrues on 31 December, so its first tax year is 2022—the paper's valuation date. RDL 8/2023 later extended it indefinitely. Footnote 2's “2023–2024” description should therefore be corrected.
3. **Why the distinction has scale.** The 2022 ITSGF raised €623M from 12,010 taxpayers; €555M, or 89%, came from Madrid. That is about 49% of Sim. 2's incremental €1,279.6M, so Sim. 2 partly overlaps an institutional change already under way.
4. **The constructive opportunity.** In 2023 Madrid suspended its IP rebate under Ley 12/2023. AEAT then reports €1,926.3M of IP receipts (+€676.3M, 90.6% from Madrid), while ITSGF receipts fell to roughly €35M. This is a partial out-of-sample realization of the mechanism behind Sim. 2.
5. **The ask.** Rename the benchmark “2022 pre-ITSGF counterfactual,” correct the date, and compare the model's prediction with the 2023 outturn. The first-year ITSGF yield—roughly 40% of its ~€1.5bn official forecast—also offers a useful calibration point for static scoring.

**Tone cue:** concede immediately that the exclusion was deliberate and disclosed. The point is not that the design comparison is invalid; it is that labeling and validation would make it stronger.

*Likely response (advocate-verified): exclusion was deliberate for comparability; the dating can be fixed; Sim. 2 covers the whole schedule whereas ITSGF begins only at very high wealth. All are fair responses and consistent with the proposed revision.*

## 24 · Comment 2: behavioral sensitivity ranges

**Opening line:** “The static exercise answers a useful mechanical question. A small sensitivity table would help readers understand how much of the revenue ranking survives plausible behavioral responses.”

**Walk-through:**

1. **What the current numbers mean.** Holding reported wealth and residence fixed isolates policy design cleanly. The resulting receipts are best read as a static benchmark, not a forecast of collected revenue after avoidance, migration, portfolio shifts, or capitalization.
2. **Why one common haircut is not enough.** Responses generally rise with the effective or marginal rate. That means the adjustment is unlikely to be ranking-neutral: Sim. 3's 3.5% top rate and Piketty's steep schedule may lose more base than Norway's broad flat 1% design.
3. **Illustrative anchors—not transplanted point estimates.** Advani and Tarrant summarize 7–17% base loss per one percentage point, mapping Sim. NO's €15.5bn static score to roughly €12.8–14.4bn. Mas-Montserrat et al.'s −3.21% per 0.1pp ATR implies about 8–10% off NO/Sim. 3/Piketty. Brülhart et al.'s estimate of at least 43% after six years per point is a high-response anchor, while Saez–Zucman use 15% and 50% erosion scenarios under stronger and weaker enforcement.
4. **Why this may reinforce the paper.** Differential erosion could reduce the headline euros while strengthening the paper's breadth-over-rate-steepness result. That is a reason to show the range, not a reason to abandon the static comparison.
5. **Two context checks.** Norway's actual wealth tax yields roughly 0.5% of GDP, compared with Sim. NO's 1.13% of Spanish GDP. Sims 1–3 also retain the 60% IRPF–IP cap, the channel associated with 92.6% of measured Spanish avoidance in Mas-Montserrat.
6. **Recent supportive evidence.** Agrawal, Foremny, and Martínez-Toledano (AEJ: Applied 2025) find that mobility induced by Madrid's zero rate costs about six times more in income-tax revenue than it saves in wealth tax, and that Madrid could gain from a harmonized positive rate—consistent with the logic of Sims. 2 and 3.
7. **The ask.** Add low/central/high behavioral-response columns beside the static estimate, explicitly labeled as sensitivity bounds rather than forecasts.

**Tone cue:** do not claim that any foreign elasticity transfers directly to Spain. The methodological request is simply to show whether the ordering is robust across reasonable bounds.

*Likely response: the paper is intentionally static and some avoidance channels disappear when exemptions or regional arbitrage are removed. Agree; then explain that a compact bounds column would preserve that scope while making the revenue claims easier to interpret.*

## 25 · Comment 3: long-run consistency checks

**Opening line:** “I found three long-run mechanics that would benefit from a schedule-based rerun or a short reconciliation. The main static comparison remains valuable; this asks how much of the long-run ranking survives.”

**Walk-through:**

1. **Uniform growth plus a frozen tax rate.** Everyone receives the same constant percentage growth rate g. The model then holds each person's year-0 average tax rate t_s/r fixed rather than reapplying the statutory schedule each year. At g = 2%, no-tax wealth is 7.24× larger after a century, yet an initial nonpayer never enters, an existing payer never exits, and nobody moves brackets.
2. **Why band entry can be material.** With thresholds held fixed in the simulation's units, many households would cross exemptions and higher brackets as wealth compounds; those whose post-tax wealth falls could move the other way. This extensive- and intensive-margin adjustment should matter most for progressive schedules with sizable exemptions, including Spain and Piketty. If thresholds rose at the same rate as wealth, the difference would be much smaller. The direction of each design's change is predictable; the effect on their ranking is an empirical question.
3. **The actual threshold rules differ.** Spain's state IP fixes the €300k home exemption, €700k fallback minimum, and state bands in nominal law until amended; autonomous communities may vary the general minimum, schedule, deductions, and rebates, but not that state-law home exemption (Ley 19/1991 arts. 4, 28, 30 and final provision 2; Ley 22/2009 art. 47). Norway's Storting annually sets the state thresholds/rates and the municipal deduction and maximum rate; municipalities may choose a lower rate, and there is no automatic CPI formula (Tax Act §§15-1–15-2). Zurich StG §48 automatically CPI-adjusts the zero-rate band and §47 bracket amounts at the start of each two-year tax-coefficient (Steuerfuss) period. A single frozen or fully indexed path is therefore inappropriate for all three.
4. **Long-run Gini logic.** Without tax, multiplying everyone's wealth by the same g leaves the Gini unchanged. Under the current IP, the paper reports tax concentration C_t = 0.9744 and a cumulative burden of only 0.50% by year 25. Using those printed quantities, our accounting bounds the Gini movement at about 0.17 point downward.
5. **The number to reconcile.** Table 5 instead moves the equivalized Gini from 0.6402 to 0.6506, or 1.04 points upward. Five designs remain above the starting Gini for decades. This may reflect a definition, population, or equivalization step not visible in the text; a code-and-input check should identify it.
6. **Total-wealth denominator.** Revenue divided by every printed t or t_s/r implies total net wealth around €5.3T. Table A.1's mean multiplied by its count implies €7.2T, a 35% difference. The EFF 2022 household mean (~€309k; Banco de España DO 2413) is closer to €5.3T. Ask which vintage and valuation concept feeds the long-run denominator.
7. **Comparator labeling.** Most outcome tables compare each design with no wealth tax, but Figure 4 compares each alternative with the current IP. This is why Switzerland can have a negative distance contribution while remaining progressive in absolute terms. Put “comparator: no IP” or “comparator: current IP” in every caption and, ideally, report both deltas in an appendix.
8. **Other items for the same pass.** Table 3's net-wealth R–S changes scale relative to Table A.4; some overlap cells exceed row totals (297,219 in Piketty∩Sim. 2 versus 201,687 total Sim. 2 taxpayers); one ratio appears as both 3.0838 and 3.1125; the text alternates among seven, eight, and nine scenarios; and valuation bases move between declared and market values. A short consistency appendix could settle these without distracting from the main paper.
9. **The ask.** Reapply each statutory schedule annually under its actual or explicitly assumed threshold path, rerun the equivalized Gini, reconcile the wealth aggregate, and add a comparator/units line to every result.

**Tone cue:** present these as reconciliation questions, not proof of a coding error. Give the authors room to identify a definition that is absent from the draft.

*Likely responses: the fixed-rate projection is intentionally illustrative; the R–S column is displayed in thousandths; A.1 may use an earlier cadastral-adjustment vintage; overlap cells may be transcription errors; valuation follows each statute. Those explanations are plausible—request a schedule-reapplication sensitivity and documentation in the journal version.*

## 26 · Comment 4: framing and reproducibility

**Opening line:** “My final comment is mostly an invitation to make the paper's strongest result easier to see and easier to reproduce.”

**Walk-through:**

1. **Separate progressivity from redistribution.** The abstract emphasizes reforms that “increase tax progressivity,” but the paper's own measures show a subtler pattern. Kakwani falls from 0.2313 under the current IP to 0.1912 under Norway and 0.1969 under Piketty; Suits falls from 0.8055 to 0.5221 and 0.5701. Only France and Sim. 2 exceed the IP's Kakwani value.
2. **Why that is a stronger finding.** Norway, Sim. 3, and Piketty redistribute more despite lower formal progressivity because they tax a much broader base and raise average incidence. Figure 4's level effect and the child-benefit comparison both point in the same direction. The paper can say: broad coverage and revenue capacity matter more here than the steepness of the schedule.
3. **Add the positive aggregate check—with limits.** The simulated baseline is about 8% low on positive payers and 10% low on revenue relative to AEAT's official 2022 figures (185,101 payers and €1,250M), reasonably close on those two aggregates. This is not full validation: total declarants are about 26% low and the zero-liability-filer gap remains unresolved. Report both the match and its limits.
4. **What is already accessible.** The Panel de Hogares is a joint INE–AEAT–IEF product that researchers can request free under the IEF protocol. The confidentiality constraint therefore does not prevent methodological replication by approved researchers.
5. **What still needs publication.** The author-controlled pieces are: (a) the 17-region, three-foreign-design, and Piketty parameter tables; (b) an asset-by-asset base map covering property values, pension rights, business assets, liabilities, exemptions, and caps; and (c) the calculator code. The Zurich case illustrates why this matters: the statutory top tariff of 0.3% becomes roughly 0.65% only after canton and city multipliers, which the draft does not specify.
6. **How to frame our repo.** We have independently re-encoded all eight designs with 30 schedule and portfolio-path tests at github.com/MaxGhenis/iariw-2026-canto-garcia-replication. It is a transparent foundation, not a full replication. With their parameter disclosures and an approved PH extract, it could become one.
7. **The ask.** Commit to releasing the appendix and calculator with the journal version. That would turn a useful comparison into a reusable benchmark for European wealth-tax research.

**Tone cue:** lead with the paper's strengths—the inverse breadth/progressivity result and the baseline validation—before asking for disclosure. Treat the open package as a way to extend the paper's impact.

*Likely response: this is still a working paper; the parameters come from public statutes; a package has not yet been assembled. A constructive outcome is a commitment to publish an implementation appendix and code with the journal version.*

## 27 · Close

Three invitations rather than challenges: (1) clarify which property values, pension rights, business assets, and liabilities enter each scenario, and what Piketty raises on one common asset base; (2) consider the 2023 out-of-sample test; and (3) explain how the 60% cap operates in Sims 1–3/Piketty, including Table A.8's 3,577 IP payers outside Piketty. Hand to Olga and Francisco. Repo URL on screen.

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
