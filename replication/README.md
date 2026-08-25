# Open re-encoding of the eight wealth-tax designs

Replication scaffold for Cantó & García-Rodríguez (2026), *Progressivity and
Redistribution of Wealth Taxation in Spain* (EQUALITAS WP-95), built for the IARIW
2026 discussant presentation. The paper releases no code and no parameter tables;
this package re-encodes every statutory schedule from primary legal sources and
implements the paper's indices and long-run framework, so that the full study
becomes re-runnable the moment microdata are attached.

```bash
uv sync
uv run pytest      # 26 hand-computed anchor tests, all against primary sources
```

## What is encoded (all parameters sourced in `src/wealth_tax_es/schedules.py`)
- **Spanish IP**: state schedule (Ley 19/1991 art. 30.2, anchor-tested against the
  BOE cuota íntegra table), €700k/€300k exemptions, the 60% IRPF–IP joint limit with
  its 80%-reduction floor, and the 2022 regional 100%/25% rebates (Madrid, Andalusia,
  Galicia).
- **ITSGF** (Ley 38/2022): €3M zero band over a €700k exemption, 1.7/2.1/3.5%
  brackets (edges shared with the IP top brackets), IP-quota credit — the tax the
  paper's "2022 baseline" excludes despite its first accrual falling on the paper's
  valuation date.
- **Norway**: true 2022 rules (0.95%/1.10% above NOK 20M, NOK 1.7M/3.4M thresholds,
  primary-residence 25%-then-50% valuation kink) *and* the paper's stylized flat-1%
  variant, so the fidelity gap is computable.
- **Zurich**: § 47 StG Grundtarif (single and married), with the Steuerfuss
  (canton 99% + city 119%) as an explicit choice the paper never discloses.
- **French IFI**: €1.3M trigger, schedule from €800k, 1.3–1.4M décote, 30%
  main-residence abatement, 75%-of-income plafonnement (the cap the paper says has
  "no analogue" abroad).
- **Piketty**: the paper's 0/0.5/1/2% variant and the book's 0.1%-bottom variant.
- **Indices**: weighted Gini, concentration, Kakwani, Suits, Reynolds–Smolensky and
  the t/(1−t)·K identity.
- **Long-run projector**: the paper's constant-g constant-t framework — including
  the tests demonstrating that under it the no-tax Gini is exactly scale-invariant,
  so Table 5's rising equivalized Gini cannot be produced by the stated method
  (REVIEW.md, finding `equivalized-longrun-artefact`).

## What still needs data or author input
| Layer | Status |
|---|---|
| EFF 2022 microdata (Banco de España) | Public after registration → reproduces Figure 1, the ×3.08 ratio, and a survey-based analogue of Table 3. Not yet fetched. |
| Panel de Hogares 2022 (INE–AEAT–IEF) | Free to researchers under the IEF data-request protocol (`ief.es → Est_peticion`) → near-exact replication. Request not yet filed. |
| 17 regional IP schedules beyond the rebates | Only the state schedule + rebates are encoded; the regional scales/thresholds (Catalonia 500k & 0.21–3.48%, etc.) belong in the parameter appendix we ask the authors to publish. |
| Per-scenario valuation base | The paper is ambiguous (declared vs ×3.08 market values by design); `calculator.py` deliberately leaves valuation to the caller. |
| Díaz et al. level/distance decomposition | Not implemented — the paper's eq. (5) as printed has a typo, and we do not implement formulas we have not read in the original source. |

## Structure
- `src/wealth_tax_es/schedules.py` — statutory parameters with per-line sources
- `src/wealth_tax_es/calculator.py` — liability functions (valuation-agnostic)
- `src/wealth_tax_es/indices.py` — Gini/Kakwani/Suits/R–S (weighted)
- `src/wealth_tax_es/longrun.py` — constant-g projection + cumulative rates
- `tests/` — 26 anchor tests, every number hand-computed from the cited statute
- `NOTES.md` — primary-source register and open questions for the authors
- `data/` — gitignored; put EFF/PH extracts here
