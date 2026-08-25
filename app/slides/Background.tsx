import React from 'react';
import Slide from '@/components/Slide';
import SlideTitle from '@/components/SlideTitle';
import SlideSubtitle from '@/components/SlideSubtitle';
import { assetPath } from '@/lib/assetPath';

export function MotivationSlide() {
  return (
    <Slide>
      <SlideTitle>Wealth concentration in Spain has been rising</SlideTitle>
      <SlideSubtitle>
        And most countries have walked away from the tax that targets it
      </SlideSubtitle>
      <div className="flex-1 flex items-center gap-12 pb-10">
        <div className="w-[46%] space-y-5 text-xl text-slate-700 leading-relaxed">
          <p>
            Survey of Household Finances (EFF): the{' '}
            <span className="font-semibold text-slate-900">top 1% share</span>{' '}
            of net wealth rose from{' '}
            <span className="font-semibold text-slate-900">13.3% (2002) to ~21% (2022)</span>;
            the bottom 50% fell from 12.8% to 7.1%.
          </p>
          <p>
            Meanwhile the annual net wealth tax has nearly vanished:{' '}
            <span className="font-semibold text-slate-900">12 OECD countries in 1990 → 3 by 2023</span>{' '}
            (Spain, Norway, Switzerland). France retreated to real estate only
            (ISF → IFI, 2018).
          </p>
          <p>
            Spain is the natural laboratory: progressive rates, broad legal
            base, and <span className="font-semibold text-slate-900">17 regional regimes</span>{' '}
            that can — and do — hollow the tax out.
          </p>
        </div>
        <div className="flex-1 flex flex-col items-center justify-center">
          <img
            src={assetPath('/figures/lorenz-eff.png')}
            alt="Lorenz curves of equivalized net wealth in Spain, 2002-2022"
            className="max-h-[520px] w-auto"
          />
          <p className="text-sm text-slate-500 mt-2">
            Lorenz curves of equivalized net wealth (EFF, 2002–2022) — their Figure 1
          </p>
        </div>
      </div>
    </Slide>
  );
}

export function SpanishIPSlide() {
  return (
    <Slide>
      <SlideTitle>The Spanish wealth tax: progressive on paper, hollowed out in practice</SlideTitle>
      <SlideSubtitle>
        Impuesto sobre el Patrimonio (IP) — state schedule, regional control
      </SlideSubtitle>
      <div className="flex-1 grid grid-cols-2 gap-10 pb-10 content-center text-lg text-slate-700 leading-relaxed">
        <div className="space-y-4">
          <div className="bg-slate-50 border border-slate-200 rounded-xl px-6 py-4">
            <p className="font-semibold text-slate-900 mb-1">Statutory design (2022 baseline)</p>
            <ul className="space-y-1.5 list-disc pl-5">
              <li>
                Net wealth above a{' '}
                <span className="font-semibold">€700,000 general exemption</span>{' '}
                + €300,000 for the main residence
              </li>
              <li>
                Progressive state schedule,{' '}
                <span className="font-semibold">0.2% → 3.5%</span>
              </li>
              <li>
                Joint IRPF–IP cap: combined liability ≤ 60% of the income-tax
                base, with a 20% minimum wealth-tax payment
              </li>
            </ul>
          </div>
          <div className="bg-slate-50 border border-slate-200 rounded-xl px-6 py-4">
            <p className="font-semibold text-slate-900 mb-1">A tax with a strange life</p>
            <p>
              Introduced 1977 as &ldquo;temporary&rdquo;; permanent 1991;
              suspended 2008; reinstated 2011 — formally temporary, renewed
              every year since.
            </p>
          </div>
        </div>
        <div className="space-y-4">
          <div className="bg-teal-50 border border-teal-200 rounded-xl px-6 py-4">
            <p className="font-semibold text-slate-900 mb-1">Regional autonomy is the story</p>
            <ul className="space-y-1.5 list-disc pl-5">
              <li>
                Since 2011 regions set rates, thresholds, and rebates —{' '}
                <span className="font-semibold">
                  Madrid and Andalusia: 100% rebate in 2022
                </span>
              </li>
              <li>
                Catalonia, Extremadura, Valencia keep high effective burdens →
                horizontal inequity and fiscal competition
              </li>
            </ul>
          </div>
          <div className="bg-slate-800 text-white rounded-xl px-6 py-4">
            <p className="text-lg text-slate-200">The result, in their 2022 data:</p>
            <p className="text-3xl font-bold text-teal-300 mt-1">
              170,404 effective taxpayers
            </p>
            <p className="text-lg text-slate-200">
              of 44.9M individuals (0.4%) · €1.13bn revenue · zero measurable
              Gini reduction
            </p>
          </div>
          <p className="text-base text-slate-500">
            Scope note: the 2022 state &ldquo;solidarity&rdquo; surcharge on
            large fortunes (ITSGF) is deliberately excluded from the baseline
            (their footnote 2) — it returns in the discussion.
          </p>
        </div>
      </div>
    </Slide>
  );
}

export function ThisPaperSlide() {
  return (
    <Slide>
      <SlideTitle>This paper: what would a different design deliver?</SlideTitle>
      <SlideSubtitle>
        Hold the 2022 population and wealth fixed; swap the tax law; compare
      </SlideSubtitle>
      <div className="flex-1 flex flex-col justify-center pb-10 space-y-6 max-w-5xl w-full mx-auto text-xl text-slate-700 leading-relaxed">
        <div className="grid grid-cols-2 gap-8">
          <div className="bg-slate-50 border border-slate-200 rounded-xl px-7 py-5">
            <p className="font-semibold text-slate-900 mb-2">Questions</p>
            <ul className="space-y-2 list-disc pl-5 text-lg">
              <li>How would alternative designs change progressivity and revenue?</li>
              <li>How much redistribution could the revenue buy?</li>
              <li>Which designs bend long-run wealth concentration?</li>
              <li>Who would actually pay, under each?</li>
            </ul>
          </div>
          <div className="bg-slate-50 border border-slate-200 rounded-xl px-7 py-5">
            <p className="font-semibold text-slate-900 mb-2">Contributions</p>
            <ul className="space-y-2 list-disc pl-5 text-lg">
              <li>
                First wealth-tax design comparison on Spanish{' '}
                <span className="font-semibold">administrative register data</span>
              </li>
              <li>
                Decomposition of redistributive change:{' '}
                <span className="font-semibold">level (incidence) vs distance (progressivity)</span>
              </li>
              <li>Long-run (25–100 year) cumulative framework</li>
              <li>Taxpayer profiles under each design (logit)</li>
            </ul>
          </div>
        </div>
        <p>
          The comparison set is unusually rich: three real foreign systems
          (Norway, Switzerland, France), three internal reforms, and
          Piketty&rsquo;s (2014) normative schedule — all run on the same
          microdata.
        </p>
      </div>
    </Slide>
  );
}
