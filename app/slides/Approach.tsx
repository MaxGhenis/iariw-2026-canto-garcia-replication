import React from 'react';
import Slide from '@/components/Slide';
import SlideTitle from '@/components/SlideTitle';
import SlideSubtitle from '@/components/SlideSubtitle';
import { assetPath } from '@/lib/assetPath';

export function DataSlide() {
  return (
    <Slide>
      <SlideTitle>Data: the tax agency&rsquo;s Household Panel</SlideTitle>
      <SlideSubtitle>
        Administrative records for filers and non-filers, compiled by AEAT and
        provided through the Instituto de Estudios Fiscales
      </SlideSubtitle>
      <div className="flex-1 grid grid-cols-2 gap-10 pb-10 content-center text-xl text-slate-700 leading-relaxed">
        <div className="space-y-4">
          <div className="bg-slate-50 border border-slate-200 rounded-xl px-6 py-4">
            <p className="font-semibold text-slate-900 mb-1">Panel de Hogares (PH), 2022 wave</p>
            <ul className="space-y-1.5 list-disc pl-5">
              <li>
                <span className="font-semibold">~950,000 households · 2.7M individuals</span>{' '}
                sampled; weighted to 17.7M households / 44.9M individuals
              </li>
              <li>
                Links income-tax returns, wealth-tax declarations, and
                third-party reports (employers, banks) — covers{' '}
                <span className="font-semibold">non-filers</span> too
              </li>
              <li>Panel structure from 2016; used here as a 2022 cross-section</li>
            </ul>
          </div>
          <div className="bg-teal-50 border border-teal-200 rounded-xl px-6 py-4">
            <p className="font-semibold text-slate-900 mb-1">The valuation fix</p>
            <p>
              Real estate is recorded at cadastral value → rescaled to market
              value with an EFF-based ratio of{' '}
              <span className="font-semibold">×3.08</span> (uniform across
              properties).
            </p>
          </div>
        </div>
        <div className="space-y-4">
          <div className="bg-slate-800 text-white rounded-xl px-6 py-4">
            <p className="font-semibold mb-2 text-slate-100">2022 headline statistics (their Table A.1)</p>
            <table className="w-full text-lg">
              <tbody>
                <tr className="border-b border-slate-600">
                  <td className="py-1.5 pr-3">Mean / median net wealth, all individuals</td>
                  <td className="py-1.5 text-right font-semibold text-teal-300">€160,540 / €60,372</td>
                </tr>
                <tr className="border-b border-slate-600">
                  <td className="py-1.5 pr-3">Wealth-tax filers (weighted)</td>
                  <td className="py-1.5 text-right font-semibold text-teal-300">170,408</td>
                </tr>
                <tr>
                  <td className="py-1.5 pr-3">Mean / median net wealth among filers</td>
                  <td className="py-1.5 text-right font-semibold text-teal-300">€2.05M / €1.43M</td>
                </tr>
              </tbody>
            </table>
          </div>
          <div className="bg-slate-50 border border-slate-200 rounded-xl px-6 py-4">
            <p className="font-semibold text-slate-900 mb-1">Limits the authors flag</p>
            <ul className="space-y-1.5 list-disc pl-5 text-lg">
              <li>Business assets recorded only for wealth-tax filers</li>
              <li>Liabilities not decomposed (EFF used as complement)</li>
              <li>Cadastral values lag markets, unevenly across areas</li>
            </ul>
          </div>
        </div>
      </div>
    </Slide>
  );
}

const DESIGNS = [
  ['IP (baseline)', 'Spanish wealth tax as legislated for 2022, all 17 regional regimes', '€700k + €300k residence', '0.2–3.5% progressive'],
  ['Sim. NO', 'Norwegian design: broad base, residence at 25% of market value', '~€160k', 'flat 1% (0.3% + 0.7%)'],
  ['Sim. CH', 'Swiss design (Canton of Zurich): real estate at 70% of market value', 'cantonal thresholds', 'progressive, low rates'],
  ['Sim. FR', 'French IFI: real-estate wealth only', '€1.3M trigger', '0.5–1.5% progressive'],
  ['Sim. 1', 'Spanish IP with the general exemption cut to €300k', '€300k', 'IP schedule'],
  ['Sim. 2', 'Spanish IP without regional deductions and rebates', '€700k', 'IP schedule'],
  ['Sim. 3', 'Sim. 1 + Sim. 2 combined', '€300k', 'IP schedule'],
  ['Sim. Piketty', 'Paper\'s Piketty-inspired variant; base details incomplete', '€200k', '0.5% / 1% / 2%'],
];

export function DesignsSlide() {
  return (
    <Slide>
      <SlideTitle>Eight designs, one fixed population</SlideTitle>
      <SlideSubtitle>
        Same 2022 microdata under each design; no behavioral response — design
        effects only
      </SlideSubtitle>
      <div className="flex-1 flex flex-col justify-center pb-10">
        <table className="w-full text-xl text-slate-700 border-collapse">
          <thead>
            <tr className="bg-slate-800 text-white">
              <th className="text-left px-4 py-2.5 font-semibold rounded-tl-lg">Design</th>
              <th className="text-left px-4 py-2.5 font-semibold">What it is</th>
              <th className="text-left px-4 py-2.5 font-semibold">Entry point</th>
              <th className="text-left px-4 py-2.5 font-semibold rounded-tr-lg">Rates</th>
            </tr>
          </thead>
          <tbody>
            {DESIGNS.map((row, i) => (
              <tr key={row[0]} className={i % 2 === 0 ? 'bg-white' : 'bg-slate-50'}>
                <td className="px-4 py-2 font-semibold text-slate-900 whitespace-nowrap">{row[0]}</td>
                <td className="px-4 py-2">{row[1]}</td>
                <td className="px-4 py-2 whitespace-nowrap">{row[2]}</td>
                <td className="px-4 py-2 whitespace-nowrap">{row[3]}</td>
              </tr>
            ))}
          </tbody>
        </table>
        <p className="text-base text-slate-500 mt-3">
          The paper drops Spain&rsquo;s joint IRPF–IP cap in the foreign designs;
          France&rsquo;s IFI has its own 75% income plafonnement. Sources: their
          Table 1 (p.11) and Table A.2 (p.40).
        </p>
      </div>
    </Slide>
  );
}

export function ScheduleBuild1Slide() {
  return (
    <Slide>
      <SlideTitle>Spain IP first: the steepest schedule on paper</SlideTitle>
      <SlideSubtitle>
        Schedule 1 of 6 — discussant&rsquo;s reference; links to the paper&rsquo;s
        variants are stated explicitly
      </SlideSubtitle>
      <div className="flex-1 flex items-center gap-10 pb-8">
        <div className="w-[36%] space-y-4">
          <div>
            <p className="font-semibold text-slate-900">Base and unit</p>
            <p className="text-lg text-slate-700 leading-snug">State IP schedule on net wealth above €700k. This comparison strips the €300k residence relief, regional rules, and the income cap.</p>
          </div>
          <div>
            <p className="font-semibold text-slate-900">Rates</p>
            <p className="text-lg text-slate-700 leading-snug">0.2% → 3.5% over eight brackets — the steepest top rate of the designs you are about to see.</p>
          </div>
          <div>
            <p className="font-semibold text-slate-900">Link to the paper</p>
            <p className="text-lg text-slate-700 leading-snug">This is the state-default reference for Sim. 2; the paper leaves its treatment of regional scales and thresholds unresolved. Baseline IP varies across regions.</p>
          </div>
          <div>
            <p className="font-semibold text-slate-900">Shape</p>
            <p className="text-lg text-slate-700 leading-snug">Late but fierce: on paper Spain out-taxes everyone at the top. The paper is about how little of this survives exemptions, rebates, and the cap.</p>
          </div>
        </div>
        <div className="flex-1 flex justify-center">
          <img
            src={assetPath('/figures/schedule_build_1.png')}
            alt="Marginal and average rate schedules with Spain IP highlighted"
            className="max-h-[700px] w-auto"
          />
        </div>
      </div>
    </Slide>
  );
}

export function ScheduleBuild2Slide() {
  return (
    <Slide>
      <SlideTitle>The paper's own reform: pull the threshold to €300k</SlideTitle>
      <SlideSubtitle>
        Schedule 2 of 6 — the shared Spanish rate-and-threshold skeleton
      </SlideSubtitle>
      <div className="flex-1 flex items-center gap-10 pb-8">
        <div className="w-[36%] space-y-4">
          <div>
            <p className="font-semibold text-slate-900">Base and unit</p>
            <p className="text-lg text-slate-700 leading-snug">Same state schedule with a €300k exemption: a reference skeleton for Sims 1 and 3, whose design-specific regional parameters are not fully published.</p>
          </div>
          <div>
            <p className="font-semibold text-slate-900">Rates</p>
            <p className="text-lg text-slate-700 leading-snug">Same 0.2% → 3.5% brackets; every step arrives €400k of wealth earlier.</p>
          </div>
          <div>
            <p className="font-semibold text-slate-900">Shape</p>
            <p className="text-lg text-slate-700 leading-snug">The dashed twin, shifted left. Effective taxpayers rise from 170,404 to 1.8M (Sim. 1) or 4.6M (Sim. 3), but this chart is not an exact recovery of either design.</p>
          </div>
        </div>
        <div className="flex-1 flex justify-center">
          <img
            src={assetPath('/figures/schedule_build_2.png')}
            alt="Marginal and average rate schedules with Spain €300k highlighted"
            className="max-h-[700px] w-auto"
          />
        </div>
      </div>
    </Slide>
  );
}

export function ScheduleBuild3Slide() {
  return (
    <Slide>
      <SlideTitle>Canton of Zurich: the broad, gentle reference</SlideTitle>
      <SlideSubtitle>
        Schedule 3 of 6 — illustrative Zurich-city benchmark; paper omits vintage and multiplier
      </SlideSubtitle>
      <div className="flex-1 flex items-center gap-10 pb-8">
        <div className="w-[36%] space-y-4">
          <div>
            <p className="font-semibold text-slate-900">Base and unit</p>
            <p className="text-lg text-slate-700 leading-snug">Zurich §47 single tariff on net wealth; spouses are jointly taxed and minors attributed. Shown allowance: CHF 81k (2026-indexed table).</p>
          </div>
          <div>
            <p className="font-semibold text-slate-900">Rates</p>
            <p className="text-lg text-slate-700 leading-snug">2026-indexed tariff 0–3‰ ×2.18 using canton (99%) + City of Zurich (119%) factors documented for 2022–23 → top ≈0.65%. This is a mixed-vintage illustration.</p>
          </div>
          <div>
            <p className="font-semibold text-slate-900">Shape</p>
            <p className="text-lg text-slate-700 leading-snug">Bites almost immediately, climbs slowly, never gets steep — a transparent Zurich-city reference, not a recovered paper parameter.</p>
          </div>
        </div>
        <div className="flex-1 flex justify-center">
          <img
            src={assetPath('/figures/schedule_build_3.png')}
            alt="Marginal and average rate schedules with Zurich highlighted"
            className="max-h-[700px] w-auto"
          />
        </div>
      </div>
    </Slide>
  );
}

export function ScheduleBuild4Slide() {
  return (
    <Slide>
      <SlideTitle>Norway: broad, nearly flat — and not quite the paper&rsquo;s line</SlideTitle>
      <SlideSubtitle>
        Schedule 4 of 6 — 2022 statute; the paper&rsquo;s Sim. NO is flat 1%
      </SlideSubtitle>
      <div className="flex-1 flex items-center gap-10 pb-8">
        <div className="w-[36%] space-y-4">
          <div>
            <p className="font-semibold text-slate-900">Base and unit</p>
            <p className="text-lg text-slate-700 leading-snug">All net wealth above NOK 1.7M (≈€168k; doubled for couples). Primary residence is valued at 25% through NOK 10M, then 50%; the paper&rsquo;s Sim. NO keeps 25% throughout.</p>
          </div>
          <div>
            <p className="font-semibold text-slate-900">Rates</p>
            <p className="text-lg text-slate-700 leading-snug">0.95% flat in 2022, 1.10% above NOK 20M (≈€2M) — barely progressive by design (the paper's Sim. NO stylizes this as flat 1%).</p>
          </div>
          <div>
            <p className="font-semibold text-slate-900">Shape</p>
            <p className="text-lg text-slate-700 leading-snug">A near-flat wall from ~€170k up: mass participation, low rates. Raised ≈0.5% of GDP in 2022.</p>
          </div>
        </div>
        <div className="flex-1 flex justify-center">
          <img
            src={assetPath('/figures/schedule_build_4.png')}
            alt="Marginal and average rate schedules with Norway highlighted"
            className="max-h-[700px] w-auto"
          />
        </div>
      </div>
    </Slide>
  );
}

export function ScheduleBuild5Slide() {
  return (
    <Slide>
      <SlideTitle>France: narrow base, sharp entry</SlideTitle>
      <SlideSubtitle>
        Schedule 5 of 6 — statutory IFI reference used by the paper&rsquo;s Sim. FR
      </SlideSubtitle>
      <div className="flex-1 flex items-center gap-10 pb-8">
        <div className="w-[36%] space-y-4">
          <div>
            <p className="font-semibold text-slate-900">Base and unit</p>
            <p className="text-lg text-slate-700 leading-snug">Real-estate wealth only (the IFI, successor to the ISF since 2018) — financial assets exempt. Trigger at €1.3M.</p>
          </div>
          <div>
            <p className="font-semibold text-slate-900">Rates</p>
            <p className="text-lg text-slate-700 leading-snug">0.5–1.5% schedule counted from €800k once over the trigger — so ≈€1,250 falls due just above €1.3M, smoothed by a décote to €1.4M.</p>
          </div>
          <div>
            <p className="font-semibold text-slate-900">Shape</p>
            <p className="text-lg text-slate-700 leading-snug">Nothing, then a cliff, then modest progression — and only on property.</p>
          </div>
        </div>
        <div className="flex-1 flex justify-center">
          <img
            src={assetPath('/figures/schedule_build_5.png')}
            alt="Marginal and average rate schedules with France IFI highlighted"
            className="max-h-[700px] w-auto"
          />
        </div>
      </div>
    </Slide>
  );
}

export function ScheduleBuild6Slide() {
  return (
    <Slide>
      <SlideTitle>Piketty: the normative benchmark</SlideTitle>
      <SlideSubtitle>
        Schedule 6 of 6 — the paper&rsquo;s normative benchmark, not enacted law
      </SlideSubtitle>
      <div className="flex-1 flex items-center gap-10 pb-8">
        <div className="w-[36%] space-y-4">
          <div>
            <p className="font-semibold text-slate-900">Base and unit</p>
            <p className="text-lg text-slate-700 leading-snug">The paper&rsquo;s benchmark begins at €200k. Its published parameter table does not specify the valuation base or whether an income cap carries over.</p>
          </div>
          <div>
            <p className="font-semibold text-slate-900">Rates</p>
            <p className="text-lg text-slate-700 leading-snug">0.5% / 1% / 2% above €200k / €1M / €5M (the book also floats 0.1% below €200k and 5–10% at the very top).</p>
          </div>
          <div>
            <p className="font-semibold text-slate-900">Shape</p>
            <p className="text-lg text-slate-700 leading-snug">Smoothly progressive from modest wealth up. Note how it shadows the dashed €300k Spanish line through the middle of the distribution.</p>
          </div>
        </div>
        <div className="flex-1 flex justify-center">
          <img
            src={assetPath('/figures/schedule_build_6.png')}
            alt="Marginal and average rate schedules with Piketty highlighted"
            className="max-h-[700px] w-auto"
          />
        </div>
      </div>
    </Slide>
  );
}

export function SchedulesChartSlide() {
  return (
    <Slide>
      <SlideTitle>Six reference schedules behind eight designs</SlideTitle>
      <SlideSubtitle>
        Statute/paper benchmarks; Spain stripped of abatements; assumptions labeled
      </SlideSubtitle>
      <div className="flex-1 flex flex-col justify-center pb-8">
        <img
          src={assetPath('/figures/mtr-schedules.png')}
          alt="Marginal wealth-tax rates for six reference schedules related to the paper's eight designs"
          className="max-h-[620px] w-auto mx-auto"
        />
        <p className="text-xl text-slate-700 mt-2 max-w-6xl">
          <span className="font-semibold text-slate-900">
            Zurich enters first; Norway follows with a low, nearly flat
            schedule; un-abated Spanish state IP reaches the steepest top rate
            (3.5%).
          </span>{' '}
          Valuation, exemptions, regional rules, and caps turn these schedule
          shapes into the paper&rsquo;s very different effective liabilities.
        </p>
      </div>
    </Slide>
  );
}

export function MethodsSlide() {
  return (
    <Slide>
      <SlideTitle>How they measure it</SlideTitle>
      <SlideSubtitle>
        Standard fiscal-incidence toolkit, plus a decomposition and a long-run
        extension
      </SlideSubtitle>
      <div className="flex-1 grid grid-cols-3 gap-8 pb-10 content-center text-xl text-slate-700 leading-relaxed">
        <div className="bg-slate-50 border border-slate-200 rounded-xl px-6 py-5">
          <p className="font-semibold text-slate-900 mb-2">Progressivity &amp; redistribution</p>
          <ul className="space-y-2 list-disc pl-5 text-xl">
            <li>
              <span className="font-semibold">Kakwani</span> K = C<sub>t</sub> −
              G<sub>pre</sub>: is the burden more concentrated than wealth?
            </li>
            <li>
              <span className="font-semibold">Suits</span> index (inequality-level-free
              cousin)
            </li>
            <li>
              <span className="font-semibold">Reynolds–Smolensky</span>{' '}
              R–S = G<sub>pre</sub> − G<sub>post</sub> = t/(1−t)·K − D
            </li>
            <li>
              Measured on net wealth <em>and</em> equivalized market /
              disposable income
            </li>
          </ul>
        </div>
        <div className="bg-slate-50 border border-slate-200 rounded-xl px-6 py-5">
          <p className="font-semibold text-slate-900 mb-2">Level vs distance</p>
          <p className="text-xl">
            Changes in R–S across designs split into a{' '}
            <span className="font-semibold">level effect</span> (more incidence
            — the tax simply collects more) and a{' '}
            <span className="font-semibold">distance effect</span> (more
            structural progressivity), following Díaz et al. (2010, 2011).
          </p>
        </div>
        <div className="bg-slate-50 border border-slate-200 rounded-xl px-6 py-5">
          <p className="font-semibold text-slate-900 mb-2">Long run</p>
          <p className="text-xl">
            Wealth is a stock: project each person&rsquo;s wealth forward at a
            constant growth rate g ∈ {'{1%, 2%, 3%}'} with and without the
            annual tax, for T = 25–100 years (Durán-Cabré &amp; Esteller-Moré
            framework). Compounding turns tiny annual rates into large
            cumulative wedges.
          </p>
        </div>
      </div>
    </Slide>
  );
}
