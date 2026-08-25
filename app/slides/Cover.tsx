import React from 'react';
import Slide from '@/components/Slide';

export function CoverSlide() {
  return (
    <Slide isCover>
      <div className="text-center space-y-10">
        <div>
          <h1 className="text-5xl font-bold leading-tight mb-4">
            Progressivity and redistribution of wealth taxation in Spain
          </h1>
          <h2 className="text-3xl font-medium text-slate-200 leading-snug">
            A microsimulation analysis using tax register data
          </h2>
        </div>

        <div className="text-xl text-slate-200 leading-relaxed">
          <p className="font-semibold">Olga Cantó¹² · Francisco García-Rodríguez¹²</p>
          <p className="text-lg text-slate-400 mt-2">
            ¹Universidad de Alcalá · ²EQUALITAS
          </p>
        </div>

        <div className="space-y-2">
          <p className="text-xl text-slate-100">
            IARIW General Conference · Brussels · 28 August 2026 · 4:00–5:30pm · Room A2
          </p>
          <p className="text-lg text-slate-400">
            Session: Wealth and fiscal and monetary policy
          </p>
        </div>

        <div className="pt-4 border-t border-slate-600 inline-block px-12">
          <p className="text-xl">
            Presented by the discussant:{' '}
            <span className="font-semibold text-teal-300">Max Ghenis</span>{' '}
            (PolicyEngine)
          </p>
          <p className="text-base text-slate-400 mt-1">
            Author response: Olga Cantó &amp; Francisco García-Rodríguez
          </p>
        </div>
      </div>
    </Slide>
  );
}

export function DiscussionDividerSlide() {
  return (
    <Slide isSection>
      <div className="text-center space-y-6">
        <h1 className="text-6xl font-bold">Discussion</h1>
        <p className="text-2xl text-slate-300">
          Four comments and some minor notes — from a tax-microsimulation seat
        </p>
      </div>
    </Slide>
  );
}
