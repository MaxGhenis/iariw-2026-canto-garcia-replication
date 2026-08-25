import React from 'react';
import Slide from '@/components/Slide';
import SlideTitle from '@/components/SlideTitle';
import SlideSubtitle from '@/components/SlideSubtitle';

export function Comment1Slide() {
  return (
    <Slide>
      <SlideTitle>1 · The baseline is pre-ITSGF law — Sim. 2 is partly the status quo</SlideTitle>
      <SlideSubtitle>
        Ley 38/2022 entered into force 29 Dec 2022 and accrues each 31 December —
        its first tax year is 2022 (your valuation date), not 2023 (fn. 2)
      </SlideSubtitle>
      <div className="flex-1 flex flex-col justify-center pb-10 space-y-5 max-w-6xl w-full mx-auto text-2xl text-slate-700 leading-relaxed">
        <div className="grid grid-cols-3 gap-6">
          <div className="bg-slate-800 text-white rounded-xl px-6 py-4">
            <p className="text-4xl font-bold text-teal-300">€623M</p>
            <p className="text-lg text-slate-200 mt-1">
              ITSGF collected on 2022 wealth (12,010 taxpayers; 89% Madrid) —
              ≈ half of Sim. 2&rsquo;s incremental €1,280M
            </p>
          </div>
          <div className="bg-slate-800 text-white rounded-xl px-6 py-4">
            <p className="text-4xl font-bold text-teal-300">€1,926M</p>
            <p className="text-lg text-slate-200 mt-1">
              actual IP receipts for 2023 (+€676M, 90.6% from Madrid ending its
              rebate under Ley 12/2023) — vs €1,126M simulated &ldquo;current
              law&rdquo;
            </p>
          </div>
          <div className="bg-slate-800 text-white rounded-xl px-6 py-4">
            <p className="text-4xl font-bold text-teal-300">−60%</p>
            <p className="text-lg text-slate-200 mt-1">
              ITSGF outturn vs its ~€1.5bn official forecast — a live lesson in
              static revenue scoring
            </p>
          </div>
        </div>
        <p>
          None of this invalidates the design comparison — but the baseline
          should be labeled a{' '}
          <span className="font-semibold text-slate-900">pre-ITSGF counterfactual</span>,
          and footnote 2&rsquo;s dating corrected.
        </p>
        <div className="border-l-4 border-pe-teal pl-5 py-2.5 bg-teal-50 rounded-r-lg text-xl">
          <p>
            <span className="font-semibold text-slate-900">The opportunity:</span>{' '}
            2023 is now observable — Madrid un-rebated plus a state surcharge is
            a partial dress rehearsal of Sim. 2. An out-of-sample validation
            against AEAT&rsquo;s 2023 statistics would be a genuinely novel
            contribution.
          </p>
        </div>
      </div>
    </Slide>
  );
}

export function Comment2Slide() {
  return (
    <Slide>
      <SlideTitle>2 · Static revenue is a ceiling — and your own citations price the gap</SlideTitle>
      <SlideSubtitle>
        Behavioral erosion scales with the tax rate, so it is not
        ranking-neutral across the eight designs
      </SlideSubtitle>
      <div className="flex-1 flex flex-col justify-center pb-10 space-y-5 max-w-6xl w-full mx-auto text-xl text-slate-700 leading-relaxed">
        <div className="grid grid-cols-2 gap-8">
          <div className="bg-slate-50 border border-slate-200 rounded-xl px-6 py-4">
            <p className="font-semibold text-slate-900 mb-2">
              A transparent ready-reckoner (illustration, not an estimate)
            </p>
            <ul className="space-y-1.5 list-disc pl-5 text-lg">
              <li>
                Advani &amp; Tarrant (2021): base −7–17% per 1pp →{' '}
                <span className="font-semibold">Sim. NO €15.5bn → €12.8–14.4bn</span>
              </li>
              <li>
                Mas-Montserrat et al. (2025, your citation): −3.21% per 0.1pp
                ATR → ~8–10% off Sim. NO/3/Piketty
              </li>
              <li>
                Brülhart et al. (2022, your citation): ≥43% reported-wealth
                response per 1pp = the upper bound
              </li>
              <li>
                Saez–Zucman score with 15% (strong) / 50% (weak enforcement)
                erosion — zero is outside the published debate
              </li>
            </ul>
          </div>
          <div className="space-y-4">
            <div className="bg-slate-50 border border-slate-200 rounded-xl px-6 py-4">
              <p className="font-semibold text-slate-900 mb-1">The missing citation helps you</p>
              <p className="text-lg">
                Agrawal, Foremny &amp; Martínez-Toledano (AEJ: Applied 2025):
                Madrid&rsquo;s zero rate; mobility costs 6× more in income tax
                than it saves in wealth tax;{' '}
                <span className="font-semibold">
                  Madrid itself would gain from a harmonized positive rate
                </span>{' '}
                — your Sim. 2/3 case, made stronger.
              </p>
            </div>
            <div className="bg-slate-50 border border-slate-200 rounded-xl px-6 py-4">
              <p className="font-semibold text-slate-900 mb-1">Two anchors worth one sentence each</p>
              <p className="text-lg">
                Norway&rsquo;s own tax yields ~0.5% of GDP vs Sim. NO&rsquo;s
                1.13% of Spain&rsquo;s; and Sims 1–3 keep the 60% IRPF–IP cap —
                the channel carrying 92.6% of measured Spanish avoidance.
              </p>
            </div>
          </div>
        </div>
        <p>
          Because erosion rises with rates, adjusting for it{' '}
          <span className="font-semibold text-slate-900">
            strengthens your breadth-over-rates conclusion
          </span>{' '}
          while shrinking the headline euros — worth owning explicitly.
        </p>
      </div>
    </Slide>
  );
}

export function Comment3Slide() {
  return (
    <Slide>
      <SlideTitle>3 · Two mechanical results need a re-run</SlideTitle>
      <SlideSubtitle>
        Fixable before the journal version — neither threatens the qualitative ranking
      </SlideSubtitle>
      <div className="flex-1 flex flex-col justify-center pb-10 space-y-5 max-w-6xl w-full mx-auto text-xl text-slate-700 leading-relaxed">
        <div className="grid grid-cols-2 gap-8">
          <div className="bg-slate-50 border border-slate-200 rounded-xl px-6 py-4">
            <p className="font-semibold text-slate-900 mb-1.5">
              The equivalized long-run Gini cannot rise
            </p>
            <p className="text-lg">
              Under uniform growth the no-tax distribution is scale-invariant,
              and with your C<sub>t</sub> = 0.974 the cumulative IP levy
              (0.50% by T=25) can move the Gini at most{' '}
              <span className="font-semibold">~0.17pt, downward</span>. Table 5
              reports <span className="font-semibold">+1.04pt</span> — six
              times the bound, wrong sign; five designs stay above the
              starting Gini for a century. The projection code needs an audit.
            </p>
          </div>
          <div className="bg-slate-50 border border-slate-200 rounded-xl px-6 py-4">
            <p className="font-semibold text-slate-900 mb-1.5">
              Which total wealth? €5.3T vs €7.2T
            </p>
            <p className="text-lg">
              Every printed t and t<sub>s/r</sub> coheres on total net wealth
              ≈ €5.3T (the EFF-consistent figure), but Table A.1&rsquo;s
              mean × count implies €7.2T — a 35% gap. Since t<sub>s/r</sub>{' '}
              seeds the entire long-run analysis, A.1&rsquo;s descriptives
              need reconciling.
            </p>
          </div>
        </div>
        <div className="bg-slate-800 text-white rounded-xl px-6 py-4 text-lg">
          <p className="font-semibold text-slate-100 mb-1">Smaller items for the same consistency pass</p>
          <p className="text-slate-200">
            Table 3&rsquo;s net-wealth R–S column is silently ×1000 vs Table
            A.4 · overlap matrix has impossible cells (Piketty∩Sim.2 = 297,219
            &gt; Sim.2&rsquo;s 201,687) · ratio 3.0838 vs 3.1125 on one page ·
            seven vs eight vs nine scenarios · declared vs ×3.08 market values
            across scenarios (Zurich&rsquo;s housing base ≈ 2.2× the
            IP&rsquo;s) — state each design&rsquo;s valuation base explicitly.
          </p>
        </div>
      </div>
    </Slide>
  );
}

export function Comment4Slide() {
  return (
    <Slide>
      <SlideTitle>4 · Say the finding your tables prove — and open the engine</SlideTitle>
      <SlideSubtitle>
        Redistribution and measured progressivity move in opposite directions;
        replication is one artifact away
      </SlideSubtitle>
      <div className="flex-1 flex flex-col justify-center pb-10 space-y-5 max-w-6xl w-full mx-auto text-xl text-slate-700 leading-relaxed">
        <div className="grid grid-cols-2 gap-8">
          <div className="bg-slate-50 border border-slate-200 rounded-xl px-6 py-4">
            <p className="font-semibold text-slate-900 mb-1.5">Framing</p>
            <p className="text-lg">
              The abstract promises designs that &ldquo;increase tax
              progressivity&rdquo; — but Kakwani falls under every broad-base
              design you champion (0.231 → 0.191 Norway, 0.197 Piketty), and
              your own decomposition credits the level effect. The inverse
              trade-off <em>is</em> the interesting result: own it in the
              abstract. (Also: your baseline validates within 8–10% of
              AEAT&rsquo;s €1,250M — report that; it&rsquo;s a strength.)
            </p>
          </div>
          <div className="bg-slate-50 border border-slate-200 rounded-xl px-6 py-4">
            <p className="font-semibold text-slate-900 mb-1.5">Replicability</p>
            <p className="text-lg">
              The Panel de Hogares is a joint INE–AEAT–IEF product any
              researcher can request free under the IEF protocol — unusually
              open for register data. What&rsquo;s missing is yours, not
              theirs: no code, no parameter tables (the Zurich design never
              states its schedule — statutory 0.3% top rate vs ~0.65% with
              multipliers). EUROMOD cannot simulate the IP at all
              (&ldquo;lack of data on wealth&rdquo;).
            </p>
          </div>
        </div>
        <div className="border-l-4 border-pe-teal pl-5 py-2.5 bg-teal-50 rounded-r-lg">
          <p>
            <span className="font-semibold text-slate-900">The ask:</span>{' '}
            publish the 17-region + 4-foreign-design parameter tables and the
            calculator code with the journal version.{' '}
            <span className="font-semibold text-slate-900">
              We&rsquo;ve started an open re-encoding of all eight designs
            </span>{' '}
            (github.com/MaxGhenis/iariw-2026-canto-garcia-replication) — with
            your parameters it becomes a full replication on any PH or EFF
            extract.
          </p>
        </div>
      </div>
    </Slide>
  );
}

export function CloseSlide() {
  return (
    <Slide isEnd>
      <div className="space-y-10">
        <h1 className="text-6xl font-bold text-center">Questions to open the floor</h1>
        <div className="space-y-5 text-3xl text-slate-200 leading-relaxed max-w-5xl mx-auto">
          <p>
            <span className="text-teal-300 font-semibold">Valuation base.</span>{' '}
            Which real-estate value enters each scenario&rsquo;s taxable base —
            declared or ×3.08 market? What does Piketty raise on the
            IP&rsquo;s own base?
          </p>
          <p>
            <span className="text-teal-300 font-semibold">The 2023 test.</span>{' '}
            Madrid un-rebated + ITSGF is a partial dress rehearsal of Sim. 2 —
            does AEAT&rsquo;s 2023 outturn (€1.93bn) match what your model
            predicts?
          </p>
          <p>
            <span className="text-teal-300 font-semibold">The cap.</span>{' '}
            Is the 60% IRPF–IP limit active in Sims 1–3 and Piketty, and how
            much revenue does it remove from each?
          </p>
        </div>
        <div className="text-center pt-6 border-t border-slate-600">
          <p className="text-3xl">
            Thank you — and over to{' '}
            <span className="font-semibold">Olga Cantó</span> and{' '}
            <span className="font-semibold">Francisco García-Rodríguez</span>
          </p>
          <p className="text-xl text-slate-400 mt-2">
            Max Ghenis · max@policyengine.org · review + open re-encoding:
            github.com/MaxGhenis/iariw-2026-canto-garcia-replication
          </p>
        </div>
      </div>
    </Slide>
  );
}
