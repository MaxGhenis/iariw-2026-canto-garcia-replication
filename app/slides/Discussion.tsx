import React from 'react';
import Slide from '@/components/Slide';
import SlideTitle from '@/components/SlideTitle';
import SlideSubtitle from '@/components/SlideSubtitle';

export function Comment1Slide() {
  return (
    <Slide>
      <SlideTitle>1 · Clarify the policy baseline — and use 2023 as validation</SlideTitle>
      <SlideSubtitle>
        The pre-ITSGF benchmark is analytically useful; a clearer label and
        corrected date would sharpen the comparison
      </SlideSubtitle>
      <div className="flex-1 flex flex-col justify-center pb-10 space-y-5 max-w-6xl w-full mx-auto text-2xl text-slate-700 leading-relaxed">
        <div className="grid grid-cols-3 gap-6">
          <div className="bg-slate-800 text-white rounded-xl px-6 py-4">
            <p className="text-4xl font-bold text-teal-300">€623M</p>
            <p className="text-2xl text-slate-200 mt-1">
              ITSGF collected on 2022 wealth (12,010 taxpayers; 89% Madrid) —
              ≈ half of Sim. 2&rsquo;s incremental €1,280M
            </p>
          </div>
          <div className="bg-slate-800 text-white rounded-xl px-6 py-4">
            <p className="text-4xl font-bold text-teal-300">€1,926M</p>
            <p className="text-2xl text-slate-200 mt-1">
              actual IP receipts for 2023 (+€676M, 90.6% from Madrid ending its
              rebate under Ley 12/2023) — vs €1,126M in the simulated
              pre-ITSGF benchmark
            </p>
          </div>
          <div className="bg-slate-800 text-white rounded-xl px-6 py-4">
            <p className="text-4xl font-bold text-teal-300">~40%</p>
            <p className="text-2xl text-slate-200 mt-1">
              of the ~€1.5bn official ITSGF forecast was collected in its first
              year — useful evidence for calibrating static scores
            </p>
          </div>
        </div>
        <p>
          The design comparison remains informative. Labeling the benchmark a{' '}
          <span className="font-semibold text-slate-900">pre-ITSGF counterfactual</span>,
          and correcting footnote 2&rsquo;s date, would prevent readers from
          mistaking it for the full law applying at the 2022 valuation date.
        </p>
        <div className="border-l-4 border-pe-teal pl-5 py-2.5 bg-teal-50 rounded-r-lg text-2xl">
          <p>
            <span className="font-semibold text-slate-900">A useful extension:</span>{' '}
            2023 is now observable — Madrid un-rebated plus a state surcharge is
            a partial dress rehearsal of Sim. 2. An out-of-sample validation
            against AEAT&rsquo;s 2023 statistics could be a genuinely novel
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
      <SlideTitle>2 · Add behavioral sensitivity ranges to the static estimates</SlideTitle>
      <SlideSubtitle>
        Static scores are a useful benchmark; a modest bounds exercise would
        show how robust the ranking is
      </SlideSubtitle>
      <div className="flex-1 flex flex-col justify-center pb-10 space-y-5 max-w-6xl w-full mx-auto text-2xl text-slate-700 leading-relaxed">
        <div className="grid grid-cols-2 gap-8">
          <div className="bg-slate-50 border border-slate-200 rounded-xl px-6 py-4">
            <p className="font-semibold text-slate-900 mb-2">
              An illustrative sensitivity range (not a point estimate)
            </p>
            <ul className="space-y-2 list-disc pl-5 text-2xl">
              <li>
                Advani &amp; Tarrant: base −7–17% per 1pp →{' '}
                <span className="font-semibold">Sim. NO €15.5bn → €12.8–14.4bn</span>
              </li>
              <li>
                Mas-Montserrat: −3.21% per 0.1pp ATR → ~8–10% lower
              </li>
              <li>
                Brülhart: ≥43% reported-wealth response per 1pp (high-response anchor)
              </li>
              <li>
                Saez–Zucman: 15% / 50% erosion scenarios
              </li>
            </ul>
          </div>
          <div className="space-y-4">
            <div className="bg-slate-50 border border-slate-200 rounded-xl px-6 py-4">
              <p className="font-semibold text-slate-900 mb-1">Recent evidence reinforces the harmonization case</p>
              <p className="text-2xl">
                Agrawal, Foremny &amp; Martínez-Toledano: mobility induced by
                Madrid&rsquo;s zero rate costs 6× more in income tax than it saves
                in wealth tax;{' '}
                <span className="font-semibold">
                  Madrid itself would gain from a harmonized positive rate
                </span>{' '}
                — evidence consistent with your Sim. 2/3 case.
              </p>
            </div>
            <div className="bg-slate-50 border border-slate-200 rounded-xl px-6 py-4">
              <p className="font-semibold text-slate-900 mb-1">Two external anchors for context</p>
              <p className="text-2xl">
                Norway raises ~0.5% of GDP vs Sim. NO&rsquo;s 1.13% of Spain&rsquo;s.
                Sims 1–3 also retain the 60% IRPF–IP cap.
              </p>
            </div>
          </div>
        </div>
        <p>
          Because behavioral responses likely rise with rates, these ranges may{' '}
          <span className="font-semibold text-slate-900">
            strengthen your breadth-over-rates conclusion
          </span>{' '}
          while lowering the headline euros. Showing both figures would make
          the conclusion more robust.
        </p>
      </div>
    </Slide>
  );
}

export function Comment3Slide() {
  return (
    <Slide>
      <SlideTitle>3 · The long-run mechanics merit a consistency check</SlideTitle>
      <SlideSubtitle>
        Reapply each schedule under an actual or explicitly assumed threshold
        path, then test whether the long-run ranking survives
      </SlideSubtitle>
      <div className="flex-1 flex flex-col justify-center pb-10 space-y-5 max-w-6xl w-full mx-auto text-2xl text-slate-700 leading-relaxed">
        <div className="grid grid-cols-3 gap-5">
          <div className="bg-slate-50 border border-slate-200 rounded-xl px-5 py-4">
            <p className="font-semibold text-slate-900 mb-1.5">
              Reapply the schedule as wealth grows
            </p>
            <p className="text-2xl">
              At g = 2%, no-tax wealth grows <span className="font-semibold">7.24×</span>{' '}
              by T=100. But each year-0 average rate stays fixed: nobody enters,
              exits, or changes bands. A schedule-based rerun could materially
              change the paths.
            </p>
          </div>
          <div className="bg-slate-50 border border-slate-200 rounded-xl px-5 py-4">
            <p className="font-semibold text-slate-900 mb-1.5">
              The equivalized long-run Gini
            </p>
            <p className="text-2xl">
              Uniform growth leaves the no-tax Gini unchanged. The printed
              inputs imply at most <span className="font-semibold">~0.17pt down</span>{' '}
              by T=25; Table 5 reports <span className="font-semibold">+1.04pt</span>.
              Could definitions or equivalization explain it?
            </p>
          </div>
          <div className="bg-slate-50 border border-slate-200 rounded-xl px-5 py-4">
            <p className="font-semibold text-slate-900 mb-1.5">
              Reconcile total net wealth: €5.3T vs €7.2T
            </p>
            <p className="text-2xl">
              The reported t and t<sub>s/r</sub> imply{' '}
              <span className="font-semibold">≈ €5.3T</span>, while Table
              A.1&rsquo;s mean × count implies <span className="font-semibold">€7.2T</span>.
              Which aggregate seeds the projection?
            </p>
          </div>
        </div>
        <div className="bg-slate-800 text-white rounded-xl px-6 py-4 text-2xl">
          <p className="font-semibold text-slate-100 mb-1">Threshold paths and comparators differ by design</p>
          <p className="text-slate-200">
            Spain: nominal until amended · Norway: annual Storting decision ·
            Zurich: bracket amounts CPI-adjusted every two years. State each
            path—and label Tables 3–4 vs no IP, Figure 4 vs current IP.
          </p>
        </div>
      </div>
    </Slide>
  );
}

export function Comment4Slide() {
  return (
    <Slide>
      <SlideTitle>4 · Lead with the strongest finding — and make it reproducible</SlideTitle>
      <SlideSubtitle>
        The breadth–progressivity trade-off is the paper&rsquo;s most interesting
        result; replication is one disclosure package away
      </SlideSubtitle>
      <div className="flex-1 flex flex-col justify-center pb-10 space-y-5 max-w-6xl w-full mx-auto text-2xl text-slate-700 leading-relaxed">
        <div className="grid grid-cols-2 gap-8">
          <div className="bg-slate-50 border border-slate-200 rounded-xl px-6 py-4">
            <p className="font-semibold text-slate-900 mb-1.5">Framing</p>
            <p className="text-2xl">
              The broad-base designs redistribute more even as Kakwani falls:
              0.231 → 0.191 (Norway) and 0.197 (Piketty). The level effect
              dominates. That breadth–incidence trade-off is a sharper finding.
              The baseline is also 8% low on payers and 10% low on revenue
              versus AEAT&rsquo;s 2022 totals — a useful two-moment check.
            </p>
          </div>
          <div className="bg-slate-50 border border-slate-200 rounded-xl px-6 py-4">
            <p className="font-semibold text-slate-900 mb-1.5">Replicability</p>
            <p className="text-2xl">
              Researchers can request the Panel de Hogares free under the IEF
              protocol. The remaining author-controlled inputs are code,
              implementation-ready parameters, and the asset-base map. Zurich
              shows why: its 0.3% statutory top tariff becomes ~0.65% only after
              canton and city multipliers.
            </p>
          </div>
        </div>
        <div className="border-l-4 border-pe-teal pl-5 py-2.5 bg-teal-50 rounded-r-lg">
          <p>
            <span className="font-semibold text-slate-900">A practical package:</span>{' '}
            publish the 17-region + 3-foreign-design + Piketty parameters, the
            asset-by-asset base map, and calculator code.{' '}
            <span className="font-semibold text-slate-900">
              We&rsquo;ve started an open re-encoding of all eight designs
            </span>{' '}
            — with those disclosures and a PH extract, it could become a full
            replication.
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
        <h1 className="text-6xl font-bold text-center">Questions for discussion</h1>
        <div className="space-y-5 text-3xl text-slate-200 leading-relaxed max-w-5xl mx-auto">
          <p>
            <span className="text-teal-300 font-semibold">Could you clarify the base?</span>{' '}
            Which property values, pension rights, business assets, and
            liabilities enter each scenario? What does Piketty raise on one
            common asset base?
          </p>
          <p>
            <span className="text-teal-300 font-semibold">Could 2023 be an out-of-sample test?</span>{' '}
            Madrid un-rebated + ITSGF is a partial dress rehearsal of Sim. 2 —
            does the combined ~€1.96bn outturn match what your model
            predicts?
          </p>
          <p>
            <span className="text-teal-300 font-semibold">How is the cap applied?</span>{' '}
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
