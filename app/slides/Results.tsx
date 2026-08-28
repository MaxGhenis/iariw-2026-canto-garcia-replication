import React from 'react';
import Slide from '@/components/Slide';
import SlideTitle from '@/components/SlideTitle';
import SlideSubtitle from '@/components/SlideSubtitle';
import { assetPath } from '@/lib/assetPath';

function ResultContext({ children }: { children: React.ReactNode }) {
  return (
    <span className="inline-block rounded-md border border-slate-200 bg-slate-100 px-2.5 py-0.5 text-xl font-semibold text-slate-700 mr-2">
      {children}
    </span>
  );
}

export function AETRSlide() {
  return (
    <Slide>
      <SlideTitle>Result 1 · Who faces the tax, and at what rate</SlideTitle>
      <SlideSubtitle>
        <ResultContext>Level measure · no-IP line = 0</ResultContext>
        Average effective tax rates by net-wealth percentile, 2022 — their Figure 3
      </SlideSubtitle>
      <div className="flex-1 flex flex-col justify-center pb-10">
        <div className="grid grid-cols-2 gap-8">
          <div className="text-center">
            <img
              src={assetPath('/figures/aetr-p67.png')}
              alt="AETRs from percentile 67"
              className="w-full h-auto border border-slate-200 rounded-lg"
            />
            <p className="text-base text-slate-500 mt-1.5">From percentile 67</p>
          </div>
          <div className="text-center">
            <img
              src={assetPath('/figures/aetr-p985.png')}
              alt="AETRs from percentile 98.5"
              className="w-full h-auto border border-slate-200 rounded-lg"
            />
            <p className="text-base text-slate-500 mt-1.5">From percentile 98.5</p>
          </div>
        </div>
        <div className="flex items-center justify-between mt-4">
          <img
            src={assetPath('/figures/aetr-legend.png')}
            alt="Legend"
            className="h-12 w-auto"
          />
          <div className="text-xl text-slate-700 leading-snug max-w-[52%]">
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
        <ResultContext>Gini comparator · no IP</ResultContext>
        Individual net wealth, 2022 — condensed from their Table 3 (p.21)
      </SlideSubtitle>
      <div className="flex-1 flex flex-col justify-center pb-10">
        <table className="w-full text-xl text-slate-700 border-collapse">
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
        <div className="grid grid-cols-3 gap-6 mt-4 text-lg text-slate-700">
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
      <SlideTitle>Result 3 · Incidence dominates the redistribution gains</SlideTitle>
      <SlideSubtitle>
        <ResultContext>Comparator · current IP</ResultContext>
        Change in Reynolds–Smolensky, split using Díaz et al. (2010, 2011) — their Figure 4
      </SlideSubtitle>
      <div className="flex-1 flex items-center gap-12 pb-10">
        <div className="w-[44%] space-y-5 text-2xl text-slate-700 leading-relaxed">
          <p>
            Every alternative redistributes more than the current IP — and in
            every case the gain is{' '}
            <span className="font-semibold text-slate-900">
              dominated by the level effect
            </span>
            : the tax simply collects more.
          </p>
          <p>
            The distance contribution is{' '}
            <span className="font-semibold text-slate-900">negative</span> for
            Norway, Switzerland, and Piketty—even though all three taxes remain
            progressive in absolute terms.
          </p>
          <p className="text-xl text-slate-500">
            Mechanically: the mean net-of-tax change goes to &ldquo;level&rdquo;;
            the change in normalized pairwise wealth gaps goes to
            &ldquo;distance&rdquo;. This is an accounting split, not a behavioral one.
          </p>
          <p className="text-xl text-slate-700 border-l-4 border-slate-300 pl-5">
            Negative is relative, not regressive: Sim. CH has K = 0.120, versus
            0.231 for the current IP.
          </p>
          <div className="border-l-4 border-pe-teal pl-5 py-2 bg-teal-50 rounded-r-lg text-xl">
            <p>
              Their own words: improvements are &ldquo;driven primarily by the
              Level Effect&rdquo; (p.22).
            </p>
          </div>
        </div>
        <div className="flex-1 flex flex-col items-center">
          <img
            src={assetPath('/figures/rs-decomposition.png')}
            alt="Decomposition of the change in the R-S index, individual net wealth"
            className="max-h-[500px] w-auto border border-slate-200 rounded-lg"
          />
          <p className="text-base text-slate-500 mt-2">
            ΔR–S vs the Spanish IP, individual net wealth
          </p>
        </div>
      </div>
    </Slide>
  );
}

const CHILD = [
  { design: 'IP', perChild: 149, taxOnly: 0.21, combined: 0.48 },
  { design: 'Sim. NO', perChild: 2_049, taxOnly: 1.08, combined: 4.58 },
  { design: 'Sim. CH', perChild: 642, taxOnly: 0.24, combined: 1.40 },
  { design: 'Sim. FR', perChild: 191, taxOnly: 0.21, combined: 0.56 },
  { design: 'Sim. 1', perChild: 492, taxOnly: 0.29, combined: 1.19 },
  { design: 'Sim. 2', perChild: 319, taxOnly: 0.48, combined: 1.06 },
  { design: 'Sim. 3', perChild: 1_680, taxOnly: 1.32, combined: 4.21 },
  { design: 'Piketty', perChild: 2_103, taxOnly: 1.30, combined: 4.87 },
];

function ChildBenefitComparisonChart() {
  const left = 135;
  const top = 54;
  const plotWidth = 650;
  const rowHeight = 59;
  const plotBottom = top + CHILD.length * rowHeight;
  const x = (value: number) => left + (value / 5) * plotWidth;

  return (
    <svg
      viewBox="0 0 915 570"
      role="img"
      aria-label="Paired horizontal bars compare the percentage cut in the disposable-income Gini from the wealth tax alone and from the tax plus a universal child benefit for eight designs."
      className="w-full h-auto"
    >
      {[0, 1, 2, 3, 4, 5].map((tick) => (
        <g key={tick}>
          <line
            x1={x(tick)}
            x2={x(tick)}
            y1={top - 5}
            y2={plotBottom - 6}
            stroke="#E2E8F0"
            strokeWidth="1"
          />
          <text
            x={x(tick)}
            y={plotBottom + 17}
            textAnchor="middle"
            fill="#64748B"
            fontSize="14"
          >
            {tick}%
          </text>
        </g>
      ))}

      <rect x={left} y="8" width="16" height="12" fill="#64748B" />
      <text x={left + 23} y="19" fill="#334155" fontSize="15">Tax only</text>
      <rect x={left + 122} y="8" width="16" height="12" fill="#2EA3A3" />
      <text x={left + 145} y="19" fill="#334155" fontSize="15">Tax + child benefit</text>

      {CHILD.map((row, index) => {
        const y = top + index * rowHeight;
        return (
          <g key={row.design}>
            <text
              x={left - 13}
              y={y + 27}
              textAnchor="end"
              fill="#0F172A"
              fontSize="17"
              fontWeight="600"
            >
              {row.design}
            </text>
            <rect
              x={left}
              y={y + 6}
              width={x(row.taxOnly) - left}
              height="14"
              fill="#64748B"
            />
            <text
              x={x(row.taxOnly) + 7}
              y={y + 18}
              fill="#334155"
              fontSize="14"
              fontWeight="600"
            >
              {row.taxOnly.toFixed(2)}%
            </text>
            <rect
              x={left}
              y={y + 30}
              width={x(row.combined) - left}
              height="14"
              fill="#2EA3A3"
            />
            <text
              x={x(row.combined) + 7}
              y={y + 42}
              fill="#334155"
              fontSize="14"
              fontWeight="600"
            >
              {row.combined.toFixed(2)}% · €{row.perChild.toLocaleString('en-US')}/yr
            </text>
          </g>
        );
      })}

      <text
        x={left + plotWidth / 2}
        y="566"
        textAnchor="middle"
        fill="#64748B"
        fontSize="15"
      >
        Reduction in disposable-income Gini (%)
      </text>
    </svg>
  );
}

export function ChildBenefitSlide() {
  return (
    <Slide>
      <SlideTitle>Result 4 · Most of the immediate income effect comes from recycling</SlideTitle>
      <SlideSubtitle>
        <ResultContext>Comparator · no IP / no transfer</ResultContext>
        Tax only (Table 3, p.21) versus tax + equal annual per-child transfer (Table 4, p.25)
      </SlideSubtitle>
      <div className="flex-1 flex items-center gap-10 pb-10">
        <div className="w-[64%]">
          <ChildBenefitComparisonChart />
        </div>
        <div className="flex-1 space-y-5 text-2xl text-slate-700 leading-relaxed">
          <p>
            Comparing their tables, tax + benefit cuts the Gini{' '}
            <span className="font-semibold text-slate-900">2.2–5.9×</span>{' '}
            as much as the tax alone.
          </p>
          <p>
            For Norway, Sim. 3, and Piketty, the child benefit supplies{' '}
            <span className="font-semibold text-slate-900">
              69–76% of the combined one-year reduction
            </span>.
          </p>
          <p className="text-xl text-slate-500">
            Derived from rounded R–S values; the paper reports no transfer-only
            counterfactual.
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
        <ResultContext>Reference · common T = 0 wealth</ResultContext>
        Top 1% share under repeated annual taxation, g = 2% — their Figure 5
      </SlideSubtitle>
      <div className="flex-1 flex items-center gap-12 pb-10">
        <div className="w-[44%] space-y-5 text-2xl text-slate-700 leading-relaxed">
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
          <p className="text-xl text-slate-500">
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
          <p className="text-base text-slate-500 mt-2">
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
        <ResultContext>Level measure · not Δ vs IP</ResultContext>
        Taxpayer profiles across designs — their Figures 6–7 and Table 6
      </SlideSubtitle>
      <div className="flex-1 flex items-center gap-10 pb-10">
        <div className="flex-1 flex flex-col items-center">
          <img
            src={assetPath('/figures/fig7-age-probability.png')}
            alt="Predicted probability of being a taxpayer by age under each design"
            className="max-h-[440px] w-auto border border-slate-200 rounded-lg"
          />
          <p className="text-base text-slate-500 mt-2">
            Predicted probability of paying, by age (logit with region and
            household controls)
          </p>
        </div>
        <div className="w-[42%] space-y-5 text-2xl text-slate-700 leading-relaxed">
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
      <div className="flex-1 flex flex-col justify-center pb-10 space-y-5 max-w-5xl w-full mx-auto text-2xl text-slate-700 leading-relaxed">
        <div className="grid grid-cols-2 gap-8">
          <div className="bg-slate-50 border border-slate-200 rounded-xl px-7 py-5">
            <p className="font-semibold text-slate-900 mb-2">Current design (IP)</p>
            <p className="text-xl">
              High formal progressivity, minimal effect: 0.4% of individuals
              pay, €1.1bn raised, no measurable inequality reduction; regional
              rebates create horizontal inequity.
            </p>
          </div>
          <div className="bg-teal-50 border border-teal-200 rounded-xl px-7 py-5">
            <p className="font-semibold text-slate-900 mb-2">Reformed designs (Sim. 3, Piketty, NO)</p>
            <p className="text-xl">
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
