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
  ['IP (baseline)', 'Spanish wealth tax as legislated for 2022, all 17 regional regimes', '€700k general; ≤€300k home', '0.2–3.5% progressive'],
  ['Sim. NO', 'Norwegian design: broad base, residence at 25% of market value', '~€160k assessable; 2× married', 'flat 1% (0.3% + 0.7%)'],
  ['Sim. CH', 'Swiss design (Canton of Zurich): real estate at 70% of market value', 'cantonal allowance', 'progressive, low rates'],
  ['Sim. FR', 'French IFI: real-estate wealth only', '€1.3M property trigger', '0.5–1.5% progressive'],
  ['Sim. 1', 'Spanish IP with the general exemption cut to €300k', '€300k general; ≤€300k home', 'IP schedule'],
  ['Sim. 2', 'Spanish IP without regional deductions and rebates', '€700k general; ≤€300k home', 'IP schedule'],
  ['Sim. 3', 'Sim. 1 + Sim. 2 combined', '€300k general; ≤€300k home', 'IP schedule'],
  ['Sim. Piketty', 'Paper\'s Piketty-inspired variant; base details incomplete', '€200k threshold', '0.5% / 1% / 2%'],
];

export function DesignsSlide() {
  return (
    <Slide>
      <SlideTitle>The paper turns six schedule paths into eight designs</SlideTitle>
      <SlideSubtitle>
        Paper order: baseline → foreign designs → Spanish reforms → Piketty;
        same 2022 microdata, no behavioral response
      </SlideSubtitle>
      <div className="flex-1 flex flex-col justify-center pb-10">
        <table className="w-full text-xl text-slate-700 border-collapse">
          <thead>
            <tr className="bg-slate-800 text-white">
              <th className="text-left px-4 py-2.5 font-semibold rounded-tl-lg">Design</th>
              <th className="text-left px-4 py-2.5 font-semibold">What it is</th>
              <th className="text-left px-4 py-2.5 font-semibold">Threshold / relief</th>
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
          Tables 1 (p.11) and A.2 (p.40). The paper describes pensions as exempt
          under NO/CH but does not publish the asset-level implementation; its
          Piketty base is likewise incomplete. Foreign designs drop Spain&rsquo;s cap;
          IFI has its own 75% income plafonnement.
        </p>
      </div>
    </Slide>
  );
}

export function ScheduleBuild1Slide() {
  return (
    <Slide>
      <SlideTitle>Baseline IP: Spain&rsquo;s steep state schedule</SlideTitle>
      <SlideSubtitle>
        Design 1 in paper order — common illustrative portfolio, single filer
      </SlideSubtitle>
      <div className="flex-1 flex items-center gap-10 pb-8">
        <div className="w-[36%] space-y-4">
          <div>
            <p className="font-semibold text-slate-900">Base and unit</p>
            <p className="text-lg text-slate-700 leading-snug">Non-pension net wealth: 25% main residence, 75% other assets. Apply the €300k residence relief plus €700k general exemption; regional rules and the income cap remain outside this chart.</p>
          </div>
          <div>
            <p className="font-semibold text-slate-900">Rates</p>
            <p className="text-lg text-slate-700 leading-snug">0.2% → 3.5% over eight brackets — the steepest top rate of the designs you are about to see.</p>
          </div>
          <div>
            <p className="font-semibold text-slate-900">Link to the paper</p>
            <p className="text-lg text-slate-700 leading-snug">The baseline actually models 17 regional regimes. This state line is also the later reference for Sim. 2; the paper does not publish its full regional parameter map.</p>
          </div>
          <div>
            <p className="font-semibold text-slate-900">Shape</p>
            <p className="text-lg text-slate-700 leading-snug">Late but fierce: the state schedule reaches the highest top rate. The paper explains why far less survives once regions, rebates, and the cap apply.</p>
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
      <SlideTitle>Norway: a true flat 1% after a low threshold</SlideTitle>
      <SlideSubtitle>
        Design 2 in paper order — the paper&rsquo;s Sim. NO, not Norway&rsquo;s two-rate 2022 statute
      </SlideSubtitle>
      <div className="flex-1 flex items-center gap-10 pb-8">
        <div className="w-[36%] space-y-4">
          <div>
            <p className="font-semibold text-slate-900">Base and unit</p>
            <p className="text-lg text-slate-700 leading-snug">About €160k of assessable wealth exempt for an individual; double for married couples. Residence is 25% of our portfolio and the paper values that residence at 25%; pensions are outside the path.</p>
          </div>
          <div>
            <p className="font-semibold text-slate-900">Rates</p>
            <p className="text-lg text-slate-700 leading-snug">A true flat 1% on the modeled base. Along this portfolio, 81.25¢ of each extra wealth euro is assessable, so the charted marginal burden is 0.8125% after entry.</p>
          </div>
          <div>
            <p className="font-semibold text-slate-900">Shape</p>
            <p className="text-lg text-slate-700 leading-snug">Broad and proportional. Actual 2022 law used 0.95% / 1.10%; the paper deliberately stylizes it as flat 1% with housing kept at 25%.</p>
          </div>
        </div>
        <div className="flex-1 flex justify-center">
          <img
            src={assetPath('/figures/schedule_build_2.png')}
            alt="Marginal and average effective rates with the paper's flat-rate Norway design highlighted"
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
        Design 3 in paper order — illustrative Zurich-city benchmark; paper omits vintage and multiplier
      </SlideSubtitle>
      <div className="flex-1 flex items-center gap-10 pb-8">
        <div className="w-[36%] space-y-4">
          <div>
            <p className="font-semibold text-slate-900">Base and unit</p>
            <p className="text-lg text-slate-700 leading-snug">Zurich values the 25% residence share at 70% and other assets in full: 92.5% of this non-pension wealth path before its allowance. Shown allowance: CHF 81k; ECB 2022 average €1 = CHF 1.0047.</p>
          </div>
          <div>
            <p className="font-semibold text-slate-900">Rates</p>
            <p className="text-lg text-slate-700 leading-snug">2026-indexed tariff 0–3‰ ×2.18 using canton (99%) + City of Zurich (119%) factors documented for 2022–23 → top ≈0.65%. This is a mixed-vintage illustration.</p>
          </div>
          <div>
            <p className="font-semibold text-slate-900">Shape</p>
            <p className="text-lg text-slate-700 leading-snug">Bites almost immediately, climbs slowly, never gets steep — a transparent Zurich-city reference, not a recovered paper parameter. Spouses are jointly taxed.</p>
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
      <SlideTitle>France: a narrow base delays the tax</SlideTitle>
      <SlideSubtitle>
        Design 4 in paper order — the paper&rsquo;s real-estate-only Sim. FR
      </SlideSubtitle>
      <div className="flex-1 flex items-center gap-10 pb-8">
        <div className="w-[36%] space-y-4">
          <div>
            <p className="font-semibold text-slate-900">Base and unit</p>
            <p className="text-lg text-slate-700 leading-snug">Only the 25% residence share enters IFI; its 30% main-home abatement leaves 17.5% of total non-pension wealth assessable. Other assets are excluded.</p>
          </div>
          <div>
            <p className="font-semibold text-slate-900">Rates</p>
            <p className="text-lg text-slate-700 leading-snug">IFI triggers when assessable property exceeds €1.3M — about €7.4M total wealth on this path. The 0.5–1.5% schedule then counts from €800k.</p>
          </div>
          <div>
            <p className="font-semibold text-slate-900">Shape</p>
            <p className="text-lg text-slate-700 leading-snug">Nothing for most of the range, then an ≈€1,250 entry liability, then modest progression — the paper&rsquo;s narrowest base.</p>
          </div>
        </div>
        <div className="flex-1 flex justify-center">
          <img
            src={assetPath('/figures/schedule_build_4.png')}
            alt="Marginal and average effective rates with France IFI highlighted"
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
      <SlideTitle>Three Spanish reforms reuse two schedule paths</SlideTitle>
      <SlideSubtitle>
        Designs 5–7 in paper order — Sim. 1, Sim. 2, then Sim. 3
      </SlideSubtitle>
      <div className="flex-1 flex items-center gap-10 pb-8">
        <div className="w-[36%] space-y-4">
          <div>
            <p className="font-semibold text-slate-900">Map the rows</p>
            <p className="text-lg text-slate-700 leading-snug">Sim. 1 cuts the general exemption to €300k. Sim. 2 keeps €700k but removes regional deductions and rebates. Sim. 3 combines both.</p>
          </div>
          <div>
            <p className="font-semibold text-slate-900">Two visible paths</p>
            <p className="text-lg text-slate-700 leading-snug">The dashed €300k line references Sims 1 and 3; the earlier solid €700k line references Sim. 2. These plotted references use the state 0.2%–3.5% brackets and €300k residence relief; the paper does not publish the exact regional schedule map.</p>
          </div>
          <div>
            <p className="font-semibold text-slate-900">What the paper finds</p>
            <p className="text-lg text-slate-700 leading-snug">Effective taxpayers: 1.8M under Sim. 1, 201,687 under Sim. 2, and 4.6M under Sim. 3.</p>
          </div>
        </div>
        <div className="flex-1 flex justify-center">
          <img
            src={assetPath('/figures/schedule_build_5.png')}
            alt="Marginal and average effective rates with the Spanish 300k exemption reference highlighted"
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
        Design 8 in paper order — the paper&rsquo;s normative benchmark, not enacted law
      </SlideSubtitle>
      <div className="flex-1 flex items-center gap-10 pb-8">
        <div className="w-[36%] space-y-4">
          <div>
            <p className="font-semibold text-slate-900">Base and unit</p>
            <p className="text-lg text-slate-700 leading-snug">The paper calls this a full net-wealth base beginning at €200k, but does not publish its asset-level or pension treatment or whether an income cap carries over. The chart assumes full non-pension wealth.</p>
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
      <SlideTitle>One portfolio makes valuation choices visible</SlideTitle>
      <SlideSubtitle>
        Paper order; 25% main residence + 75% other assets; pension rights excluded
      </SlideSubtitle>
      <div className="flex-1 flex flex-col justify-center pb-8">
        <img
          src={assetPath('/figures/mtr-schedules.png')}
          alt="Marginal wealth-tax burdens for six design paths applied to one illustrative non-pension portfolio"
          className="max-h-[620px] w-auto mx-auto"
        />
        <p className="text-xl text-slate-700 mt-2 max-w-6xl">
          <span className="font-semibold text-slate-900">
            Norway&rsquo;s flat 1% becomes 0.8125% per next wealth euro after its
            25% housing valuation; France does not enter until about €7.4M on
            this property-light path.
          </span>{' '}
          Spain still reaches the steepest top rate. The table next maps these
          six paths back to all eight simulations.
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
