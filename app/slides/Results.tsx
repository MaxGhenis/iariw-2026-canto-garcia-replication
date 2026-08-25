import React from 'react';
import Slide from '@/components/Slide';
import SlideTitle from '@/components/SlideTitle';
import SlideSubtitle from '@/components/SlideSubtitle';
import { assetPath } from '@/lib/assetPath';

export function AETRSlide() {
  return (
    <Slide>
      <SlideTitle>Result 1 · Who faces the tax, and at what rate</SlideTitle>
      <SlideSubtitle>
        Average effective tax rates by net-wealth percentile, 2022 — their
        Figure 3
      </SlideSubtitle>
      <div className="flex-1 flex flex-col justify-center pb-10">
        <div className="grid grid-cols-2 gap-8">
          <div className="text-center">
            <img
              src={assetPath('/figures/aetr-p67.png')}
              alt="AETRs from percentile 67"
              className="w-full h-auto border border-slate-200 rounded-lg"
            />
            <p className="text-sm text-slate-500 mt-1.5">From percentile 67</p>
          </div>
          <div className="text-center">
            <img
              src={assetPath('/figures/aetr-p985.png')}
              alt="AETRs from percentile 98.5"
              className="w-full h-auto border border-slate-200 rounded-lg"
            />
            <p className="text-sm text-slate-500 mt-1.5">From percentile 98.5</p>
          </div>
        </div>
        <div className="flex items-center justify-between mt-4">
          <img
            src={assetPath('/figures/aetr-legend.png')}
            alt="Legend"
            className="h-12 w-auto"
          />
          <div className="text-lg text-slate-700 leading-snug max-w-[52%]">
            <p>
              <span className="font-semibold text-slate-900">Current IP (red): flat zero until ~p99.3.</span>{' '}
              Norway starts near p80; Piketty and Sim. NO climb steepest at the
            top.
            </p>
          </div>
        </div>
      </div>
    </Slide>
  );
}

const HEADLINE = [
  ['IP (baseline)', '170,404', '1,126', '0.02%', '0.231', '0.806', '0.000%'],
  ['Sim. NO', '7,647,459', '15,456', '0.29%', '0.191', '0.522', '0.066%'],
  ['Sim. CH', '12,400,000', '4,843', '0.09%', '0.120', '0.276', '0.013%'],
  ['Sim. FR', '117,585', '1,444', '0.03%', '0.244', '0.893', '0.013%'],
  ['Sim. 1', '1,834,488', '3,709', '0.07%', '0.226', '0.752', '0.013%'],
  ['Sim. 2', '201,687', '2,405', '0.04%', '0.234', '0.849', '0.013%'],
  ['Sim. 3', '4,626,929', '12,673', '0.24%', '0.231', '0.779', '0.066%'],
  ['Sim. Piketty', '11,010,000', '15,861', '0.30%', '0.197', '0.570', '0.080%'],
];

export function HeadlineTableSlide() {
  return (
    <Slide>
      <SlideTitle>Result 2 · Base breadth, not rate steepness, drives everything</SlideTitle>
      <SlideSubtitle>
        Individual net wealth, 2022 — condensed from their Table 3 (p.21)
      </SlideSubtitle>
      <div className="flex-1 flex flex-col justify-center pb-10">
        <table className="w-full text-[17px] text-slate-700 border-collapse">
          <thead>
            <tr className="bg-slate-800 text-white">
              <th className="text-left px-4 py-2.5 font-semibold rounded-tl-lg">Design</th>
              <th className="text-right px-4 py-2.5 font-semibold">Taxpayers</th>
              <th className="text-right px-4 py-2.5 font-semibold">Revenue (€M)</th>
              <th className="text-right px-4 py-2.5 font-semibold">Avg. rate t</th>
              <th className="text-right px-4 py-2.5 font-semibold">Kakwani K</th>
              <th className="text-right px-4 py-2.5 font-semibold">Suits S</th>
              <th className="text-right px-4 py-2.5 font-semibold rounded-tr-lg">Wealth Gini cut</th>
            </tr>
          </thead>
          <tbody>
            {HEADLINE.map((row, i) => (
              <tr
                key={row[0]}
                className={
                  row[0] === 'IP (baseline)'
                    ? 'bg-teal-50 font-medium'
                    : i % 2 === 0
                      ? 'bg-white'
                      : 'bg-slate-50'
                }
              >
                <td className="px-4 py-1.5 font-semibold text-slate-900 whitespace-nowrap">{row[0]}</td>
                <td className="px-4 py-1.5 text-right tabular-nums">{row[1]}</td>
                <td className="px-4 py-1.5 text-right tabular-nums">{row[2]}</td>
                <td className="px-4 py-1.5 text-right tabular-nums">{row[3]}</td>
                <td className="px-4 py-1.5 text-right tabular-nums">{row[4]}</td>
                <td className="px-4 py-1.5 text-right tabular-nums">{row[5]}</td>
                <td className="px-4 py-1.5 text-right tabular-nums">{row[6]}</td>
              </tr>
            ))}
          </tbody>
        </table>
        <div className="grid grid-cols-3 gap-6 mt-4 text-base text-slate-700">
          <p>
            <span className="font-semibold text-slate-900">Revenue spans 14×</span>{' '}
            — €1.1bn (IP) to €15.9bn (Piketty).
          </p>
          <p>
            <span className="font-semibold text-slate-900">Formal progressivity falls</span>{' '}
            as bases broaden: K and S are highest for IP/FR/Sim. 2.
          </p>
          <p>
            <span className="font-semibold text-slate-900">Short-run Gini moves are tiny</span>{' '}
            for wealth — the action is in revenue and the long run.
          </p>
        </div>
      </div>
    </Slide>
  );
}

export function DecompositionSlide() {
  return (
    <Slide>
      <SlideTitle>Result 3 · Redistribution comes from incidence, not rate design</SlideTitle>
      <SlideSubtitle>
        Change in Reynolds–Smolensky vs the current IP, split into level and
        distance effects — their Figure 4
      </SlideSubtitle>
      <div className="flex-1 flex items-center gap-12 pb-10">
        <div className="w-[44%] space-y-5 text-xl text-slate-700 leading-relaxed">
          <p>
            Every alternative redistributes more than the current IP — and in
            every case the gain is{' '}
            <span className="font-semibold text-slate-900">
              dominated by the level effect
            </span>
            : the tax simply collects more.
          </p>
          <p>
            The distance (structural-progressivity) effect is small and often{' '}
            <span className="font-semibold text-slate-900">negative</span> for
            the broad-base designs.
          </p>
          <div className="border-l-4 border-pe-teal pl-5 py-2 bg-teal-50 rounded-r-lg text-lg">
            <p>
              Their own words: improvements are &ldquo;driven primarily by the
              Level Effect&rdquo; — incidence, not progressivity (p.22).
            </p>
          </div>
        </div>
        <div className="flex-1 flex flex-col items-center">
          <img
            src={assetPath('/figures/rs-decomposition.png')}
            alt="Decomposition of the change in the R-S index, individual net wealth"
            className="max-h-[500px] w-auto border border-slate-200 rounded-lg"
          />
          <p className="text-sm text-slate-500 mt-2">
            ΔR–S vs the Spanish IP, individual net wealth
          </p>
        </div>
      </div>
    </Slide>
  );
}

const CHILD = [
  ['IP (baseline)', '149', '0.48%'],
  ['Sim. NO', '2,049', '4.58%'],
  ['Sim. CH', '642', '1.40%'],
  ['Sim. FR', '191', '0.56%'],
  ['Sim. 1', '492', '1.19%'],
  ['Sim. 2', '319', '1.06%'],
  ['Sim. 3', '1,680', '4.21%'],
  ['Sim. Piketty', '2,103', '4.87%'],
];

export function ChildBenefitSlide() {
  return (
    <Slide>
      <SlideTitle>Result 4 · What the revenue could buy: a universal child benefit</SlideTitle>
      <SlideSubtitle>
        Each design&rsquo;s revenue recycled as an equal per-child transfer —
        their Table 4 (p.25)
      </SlideSubtitle>
      <div className="flex-1 flex items-center gap-12 pb-10">
        <div className="w-[48%]">
          <table className="w-full text-lg text-slate-700 border-collapse">
            <thead>
              <tr className="bg-slate-800 text-white">
                <th className="text-left px-4 py-2 font-semibold rounded-tl-lg">Design</th>
                <th className="text-right px-4 py-2 font-semibold">€ / child / year</th>
                <th className="text-right px-4 py-2 font-semibold rounded-tr-lg">
                  Disposable-income Gini cut
                </th>
              </tr>
            </thead>
            <tbody>
              {CHILD.map((row, i) => (
                <tr
                  key={row[0]}
                  className={
                    row[0] === 'IP (baseline)'
                      ? 'bg-teal-50 font-medium'
                      : i % 2 === 0
                        ? 'bg-white'
                        : 'bg-slate-50'
                  }
                >
                  <td className="px-4 py-1.5 font-semibold text-slate-900">{row[0]}</td>
                  <td className="px-4 py-1.5 text-right tabular-nums">{row[1]}</td>
                  <td className="px-4 py-1.5 text-right tabular-nums">{row[2]}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
        <div className="flex-1 space-y-5 text-xl text-slate-700 leading-relaxed">
          <p>
            The current IP finances{' '}
            <span className="font-semibold text-slate-900">€149 per child per year</span>.
            Broad-base designs finance{' '}
            <span className="font-semibold text-slate-900">€1,680–2,103</span>.
          </p>
          <p>
            Recycling the revenue cuts the disposable-income Gini by{' '}
            <span className="font-semibold text-slate-900">
              4.2–4.9% (1.6–1.8 Gini points)
            </span>{' '}
            under Sim. 3 / Piketty — versus 0.5% under the current tax.
          </p>
          <p className="text-lg text-slate-500">
            Redistribution tracks revenue capacity, not the shape of the rate
            schedule.
          </p>
        </div>
      </div>
    </Slide>
  );
}

export function LongRunSlide() {
  return (
    <Slide>
      <SlideTitle>Result 5 · Compounding turns small rates into large long-run wedges</SlideTitle>
      <SlideSubtitle>
        Top 1% share of equivalized net wealth under repeated annual taxation,
        g = 2% — their Figure 5
      </SlideSubtitle>
      <div className="flex-1 flex items-center gap-12 pb-10">
        <div className="w-[44%] space-y-5 text-xl text-slate-700 leading-relaxed">
          <p>
            Current IP: top 1% share drifts from 14.7% to{' '}
            <span className="font-semibold text-slate-900">13.5% after 100 years</span>{' '}
            (−1.2pp).
          </p>
          <p>
            Norway-style and Piketty schedules:{' '}
            <span className="font-semibold text-slate-900">below 8–9% by T=100</span>{' '}
            (−5.5 to −6.7pp); Sim. 3 falls furthest among Spanish options
            (to 6.6%, −8.1pp).
          </p>
          <p className="text-lg text-slate-500">
            Mechanical projection, not a forecast — the authors present it as
            illustrating how annual stock taxation cumulates (p.25). Effective
            long-run rates reach ~22% of wealth for the broad designs
            (Table 5).
          </p>
        </div>
        <div className="flex-1 flex flex-col items-center">
          <img
            src={assetPath('/figures/top1-longrun.png')}
            alt="Top 1% share of equivalized net wealth over 100 years by design"
            className="max-h-[500px] w-auto border border-slate-200 rounded-lg"
          />
          <p className="text-sm text-slate-500 mt-2">
            Top 1% share of equivalized net wealth, T = 0 → 100 years
          </p>
        </div>
      </div>
    </Slide>
  );
}

export function WhoPaysSlide() {
  return (
    <Slide>
      <SlideTitle>Result 6 · Design choices reshape who pays</SlideTitle>
      <SlideSubtitle>
        Taxpayer profiles across designs — their Figures 6–7 and Table 6
      </SlideSubtitle>
      <div className="flex-1 flex items-center gap-10 pb-10">
        <div className="flex-1 flex flex-col items-center">
          <img
            src={assetPath('/figures/fig7-age-probability.png')}
            alt="Predicted probability of being a taxpayer by age under each design"
            className="max-h-[440px] w-auto border border-slate-200 rounded-lg"
          />
          <p className="text-sm text-slate-500 mt-2">
            Predicted probability of paying, by age (logit with region and
            household controls)
          </p>
        </div>
        <div className="w-[42%] space-y-5 text-xl text-slate-700 leading-relaxed">
          <p>
            Under the current IP and the French design, payment is an{' '}
            <span className="font-semibold text-slate-900">old-age phenomenon</span>{' '}
            — probabilities take off only after ~65.
          </p>
          <p>
            Broad bases (Norway, Switzerland, Sim. 1/3, Piketty) pull the
            curve left:{' '}
            <span className="font-semibold text-slate-900">
              younger and more diverse payers
            </span>{' '}
            enter the base.
          </p>
          <p>
            Women are less likely to pay under every design — the
            administrative footprint of the gender wealth gap.
          </p>
        </div>
      </div>
    </Slide>
  );
}

export function TheirConclusionsSlide() {
  return (
    <Slide>
      <SlideTitle>Their conclusions</SlideTitle>
      <SlideSubtitle>As stated in the paper (p.33–34) and their own deck</SlideSubtitle>
      <div className="flex-1 flex flex-col justify-center pb-10 space-y-5 max-w-5xl w-full mx-auto text-xl text-slate-700 leading-relaxed">
        <div className="grid grid-cols-2 gap-8">
          <div className="bg-slate-50 border border-slate-200 rounded-xl px-7 py-5">
            <p className="font-semibold text-slate-900 mb-2">Current design (IP)</p>
            <p className="text-lg">
              High formal progressivity, minimal effect: 0.4% of individuals
              pay, €1.1bn raised, no measurable inequality reduction; regional
              rebates create horizontal inequity.
            </p>
          </div>
          <div className="bg-teal-50 border border-teal-200 rounded-xl px-7 py-5">
            <p className="font-semibold text-slate-900 mb-2">Reformed designs (Sim. 3, Piketty, NO)</p>
            <p className="text-lg">
              Broader bases and harmonized rules multiply taxpayers (4.6–11M)
              and revenue (€12.7–15.9bn), cut disposable-income inequality
              once recycled, and bend long-run wealth concentration.
            </p>
          </div>
        </div>
        <div className="border-l-4 border-pe-teal pl-6 py-3 bg-slate-50 rounded-r-lg">
          <p>
            The policy claim:{' '}
            <span className="font-semibold text-slate-900">
              redistributive gains come from broadening the base and raising
              effective incidence — not from steepening marginal rates.
            </span>
          </p>
        </div>
      </div>
    </Slide>
  );
}
