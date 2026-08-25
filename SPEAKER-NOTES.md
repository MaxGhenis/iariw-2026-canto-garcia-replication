# Speaker notes — discussant presentation of Cantó & García-Rodríguez (2026)

**Session:** Wealth and fiscal and monetary policy · Fri 28 Aug 2026, 4:00–5:30pm, Room A2 (NBB Auditorium, Brussels) · chair Rutger Kemels (NBB)
**Paper:** "Progressivity and Redistribution of Wealth Taxation in Spain: a Microsimulation Analysis using Tax Register Data" — Olga Cantó & Francisco García-Rodríguez (Universidad de Alcalá / EQUALITAS), EQUALITAS WP-95, April 2026, 47pp.
**Format:** IARIW flipped — discussant presents the paper (~15 min), then the authors respond.
**Slot caveat:** verified on the online program 23 Aug — this paper stayed at 4pm (the organizers moved #287 to 2pm instead of moving #195 as David Johnson first proposed). Max's own #364 response runs in parallel in Room A1 4:00–5:30; coordinate with both chairs on paper order before the session.
**Deck:** 20 slides. 1–14 = the paper; 15 divider; 16–19 discussion; 20 close.

Timing guide (15 min): setting 2.5 min (slides 2–4), data + design 3 min (5–7), results 5 min (8–14, lean on 9/11/12), discussion 4 min (16–19), close 0.5 (20).

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

## 7 · Methods
Kakwani K = C_t − G_pre (eq. 2 p.13); Suits (eq. 3); R–S = G_pre − G_post = t/(1−t)·K − D (eq. 1 p.12); level vs distance decomposition of ΔR–S (eq. 5–8 p.14, Díaz et al. 2010/2011); long-run: project wealth at constant g ∈ {1,2,3}% with/without the annual tax, T = 25/50/75/100 (p.15). Measured on individual and equivalized net wealth + equivalized market and disposable income.

## 8 · Result 1: AETR profiles (their Fig. 3 p.19)
IP: near zero until ~p99.3 (p.18) then rises modestly — only ~top 0.5% pay. NO: taxation from ~p80, smooth rise. CH: step ~p67, flat low. FR: lowest across most of the top (narrow base), crosses IP above p99.5. Piketty: steepest top gradient (to ~1.3% at p100); Sim. 3 next. Percentiles are over all 44.9M individuals.

## 9 · Result 2: headline table (their Table 3 p.21, net-wealth panel)
Read across IP → Piketty: taxpayers 170,404 → 11.0M; revenue €1,126M → €15,861M (14×); avg rate t 0.02% → 0.30%. Kakwani FALLS from 0.231 (IP) to 0.191 (NO) / 0.197 (Piketty); Suits 0.806 → 0.522/0.570. Only FR (K 0.244) and Sim. 2 (0.234) beat the IP on formal progressivity. Wealth Gini cuts are tiny in the short run (0.000%–0.080%). THE message: base breadth ↔ revenue; formal progressivity moves the other way.
(If asked about R–S units: Table 3's net-wealth R–S column is ×1000 vs Table A.4 — flagged in the review; I quote Gini-reduction % instead.)

## 10 · Result 3: decomposition (their Fig. 4 p.23)
All designs raise R–S vs IP; level effect (incidence) dominates everywhere; distance effect small and often negative for broad bases. Quote p.22: gains "driven primarily by the Level Effect". This is the paper's most honest self-diagnosis — the reforms redistribute by collecting more, not by being structurally more progressive.

## 11 · Result 4: child benefit (their Table 4 p.25)
Revenue recycled as universal per-child transfer: IP €149/child/yr; NO €2,049; CH €642; FR €191; Sim. 1 €492; Sim. 2 €319; Sim. 3 €1,680; Piketty €2,103. Disposable-income Gini falls 0.48% (IP) → 4.58/4.21/4.87% (NO/S3/Piketty) — in POINTS that's 0.3779 → 0.3620/0.3595, i.e. 1.6–1.8 Gini points. (Their own slide says "4–5 Gini points" — it's 4–5 percent; I use the correct units and flag gently in discussion if useful.)

## 12 · Result 5: long run (their Fig. 5 p.28, Tables 5/A.5–A.7)
Equivalized top-1% share 14.67% at T=0 (g=2%): IP → 13.45% at T=100 (−1.2pp); NO → 9.13%; Piketty → 7.96%; Sim. 3 → 6.58% (largest fall). Long-run effective rates t_l/r at T=100: IP 1.95% of wealth; NO 22.3%; Piketty 21.9%; Sim. 3 15.3% (Table 5 p.26). Robustness: g = 1% and 3% similar (Tables A.5–A.7). Their own caveat (p.25): "not intended to predict… but rather to illustrate a fundamental mechanism" — honor it in the framing. Note the equivalized-Gini wrinkle (Table 5 bottom): under IP/CH/FR/Sim.1/Sim.2 the equivalized Gini RISES for decades before the mechanics bite.

## 13 · Result 6: who pays (their Fig. 6 p.29, Fig. 7 p.32, Table 6 p.31)
IP payers: predominantly 65+; FR similar (take-off after ~65 in Fig. 7). Broad bases shift the age curve left (CH/Piketty steepest around 50–60). Women less likely to pay under every design (Table 6: marginal effects −0.00005 FR to −0.0048 CH, all significant) — consistent with the gender wealth gap (they cite UK: ~68% of potential payers male, Advani et al. 2021). Household: multi-adult households less likely at same age.

## 14 · Their conclusions (p.33–34 + their deck)
Current IP: high formal progressivity, minimal effect; regional rebates create horizontal inequity. Reforms: broaden base + harmonize → 4.6–11M taxpayers, €12.7–15.9bn, real disposable-income redistribution once recycled, cumulative long-run concentration decline. Their policy line: gains come from base + incidence, not marginal-rate steepening.

## 15 · Divider
One breath. "Four comments — all offered in the spirit of making a genuinely valuable exercise sharper."

## 16–19 · Discussion comments
See REVIEW.md — filled after the adversarial review.

## 20 · Close
Floor questions + hand to Olga and Francisco.

---

## Numbers most likely to be challenged (all sourced)
- 170,404 effective taxpayers vs 170,408 filers (Table 3 p.21 vs Table A.1 p.38 — different concepts: positive-liability vs filed).
- €1,125.58M baseline revenue (Table 3 p.21).
- 14× revenue span: 1,126 → 15,861 (Table 3).
- Kakwani falls under broad bases: 0.2313 → 0.1912 (NO) / 0.1969 (Piketty) (Table 3).
- Child benefit €149 vs €2,103 (Table 4 p.25); Gini cut 4–5 PERCENT = 1.6–1.8 points (0.3779→0.3595).
- Top-1% equivalized share 14.67% → 6.58% (Sim. 3, T=100, g=2%) (Table A.7 p.46 / Fig. 5).
- AETR ≈ 0 until p99.3 (p.18; their slide says p99.5).
- ×3.08 cadastral→market (eq. A.1 p.39; 3.0838 vs 3.1125 inconsistency).
- (Post-review: add verified AEAT/ITSGF/Norway official statistics here.)
