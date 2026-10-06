'use client';

import React, { useEffect, useState } from 'react';
import { CoverSlide, DiscussionDividerSlide } from './slides/Cover';
import {
  MotivationSlide,
  SpanishIPSlide,
  ThisPaperSlide,
} from './slides/Background';
import {
  DataSlide,
  DesignsSlide,
  ScheduleBuild1Slide,
  ScheduleBuild2Slide,
  ScheduleBuild3Slide,
  ScheduleBuild4Slide,
  ScheduleBuild5Slide,
  ScheduleBuild6Slide,
  SchedulesChartSlide,
  MethodsSlide,
} from './slides/Approach';
import {
  AETRSlide,
  HeadlineTableSlide,
  DecompositionSlide,
  ChildBenefitSlide,
  LongRunSlide,
  WhoPaysSlide,
  TheirConclusionsSlide,
} from './slides/Results';
import {
  Comment1Slide,
  Comment2Slide,
  Comment3Slide,
  Comment4Slide,
  CloseSlide,
} from './slides/Discussion';

const slides = [
  CoverSlide,
  MotivationSlide,
  SpanishIPSlide,
  ThisPaperSlide,
  DataSlide,
  DesignsSlide,
  ScheduleBuild1Slide,
  ScheduleBuild2Slide,
  ScheduleBuild3Slide,
  ScheduleBuild4Slide,
  ScheduleBuild5Slide,
  ScheduleBuild6Slide,
  SchedulesChartSlide,
  MethodsSlide,
  AETRSlide,
  HeadlineTableSlide,
  DecompositionSlide,
  ChildBenefitSlide,
  LongRunSlide,
  WhoPaysSlide,
  TheirConclusionsSlide,
  DiscussionDividerSlide,
  Comment1Slide,
  Comment2Slide,
  Comment3Slide,
  Comment4Slide,
  CloseSlide,
];

export default function Home() {
  const [currentSlide, setCurrentSlide] = useState(0);

  useEffect(() => {
    const params = new URLSearchParams(window.location.search);
    const s = params.get('slide');
    if (s !== null) {
      const idx = parseInt(s, 10);
      if (!isNaN(idx) && idx >= 0 && idx < slides.length) {
        setCurrentSlide(idx);
      }
    }
  }, []);

  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.key === 'ArrowRight' || e.key === 'ArrowDown' || e.key === ' ') {
        e.preventDefault();
        setCurrentSlide((prev) => Math.min(prev + 1, slides.length - 1));
      } else if (e.key === 'ArrowLeft' || e.key === 'ArrowUp') {
        e.preventDefault();
        setCurrentSlide((prev) => Math.max(prev - 1, 0));
      } else if (e.key === 'Home') {
        e.preventDefault();
        setCurrentSlide(0);
      } else if (e.key === 'End') {
        e.preventDefault();
        setCurrentSlide(slides.length - 1);
      }
    };

    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, []);

  const CurrentSlideComponent = slides[currentSlide];

  return (
    <main className="relative">
      <CurrentSlideComponent />

      {/* Slide counter */}
      <div className="fixed bottom-14 right-4 text-xs text-slate-400 bg-white/80 px-2 py-1 rounded">
        {currentSlide + 1} / {slides.length}
      </div>
    </main>
  );
}
