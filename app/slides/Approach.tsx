import React from 'react';
import Slide from '@/components/Slide';
import SlideTitle from '@/components/SlideTitle';
import SlideSubtitle from '@/components/SlideSubtitle';

export function DataSlide() {
  return (
    <Slide>
      <SlideTitle>Data: the tax agency&rsquo;s Household Panel</SlideTitle>
      <SlideSubtitle>
        Administrative records for filers and non-filers, compiled by AEAT and
        provided through the Instituto de Estudios Fiscales
      </SlideSubtitle>
      <div className="flex-1 grid grid-cols-2 gap-10 pb-10 content-center text-lg text-slate-700 leading-relaxed">
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
            <table className="w-full text-base">
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
            <ul className="space-y-1.5 list-disc pl-5 text-base">
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
  ['Sim. FR', 'French IFI: real-estate wealth only', '€1.3M', '0.5–1.5% progressive'],
  ['Sim. 1', 'Spanish IP with the general exemption cut to €300k', '€300k', 'IP schedule'],
  ['Sim. 2', 'Spanish IP without regional deductions and rebates', '€700k', 'IP schedule'],
  ['Sim. 3', 'Sim. 1 + Sim. 2 combined', '€300k', 'IP schedule'],
  ['Sim. Piketty', 'Piketty (2014) normative schedule on all net wealth', '€200k', '0.5% / 1% / 2%'],
];

export function DesignsSlide() {
  return (
    <Slide>
      <SlideTitle>Eight designs, one fixed population</SlideTitle>
      <SlideSubtitle>
        Same 2022 microdata under each law; no behavioral response — design
        effects only
      </SlideSubtitle>
      <div className="flex-1 flex flex-col justify-center pb-10">
        <table className="w-full text-[17px] text-slate-700 border-collapse">
          <thead>
            <tr className="bg-slate-800 text-white">
              <th className="text-left px-4 py-2.5 font-semibold rounded-tl-lg">Design</th>
              <th className="text-left px-4 py-2.5 font-semibold">What it is</th>
              <th className="text-left px-4 py-2.5 font-semibold">Exemption</th>
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
        <p className="text-sm text-slate-500 mt-3">
          Foreign designs drop Spain&rsquo;s joint IRPF–IP cap (no analogue
          abroad). Sources: their Table 1 (p.11) and Table A.2 (p.40).
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
      <div className="flex-1 grid grid-cols-3 gap-8 pb-10 text-lg text-slate-700 leading-relaxed">
        <div className="bg-slate-50 border border-slate-200 rounded-xl px-6 py-5">
          <p className="font-semibold text-slate-900 mb-2">Progressivity &amp; redistribution</p>
          <ul className="space-y-2 list-disc pl-5 text-base">
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
          <p className="text-base">
            Changes in R–S across designs split into a{' '}
            <span className="font-semibold">level effect</span> (more incidence
            — the tax simply collects more) and a{' '}
            <span className="font-semibold">distance effect</span> (more
            structural progressivity), following Díaz et al. (2010, 2011).
          </p>
        </div>
        <div className="bg-slate-50 border border-slate-200 rounded-xl px-6 py-5">
          <p className="font-semibold text-slate-900 mb-2">Long run</p>
          <p className="text-base">
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
