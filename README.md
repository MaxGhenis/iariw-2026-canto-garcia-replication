# IARIW 2026 discussant slides — Cantó & García-Rodríguez, Spanish wealth taxation

Discussant presentation (flipped format: discussant presents, authors respond) for
Cantó & García-Rodríguez (2026), *Progressivity and Redistribution of Wealth
Taxation in Spain: a Microsimulation Analysis using Tax Register Data* (EQUALITAS
WP-95), IARIW General Conference, Brussels, **Fri 28 Aug 2026 4:00–5:30pm, Room A2**,
session "Wealth and fiscal and monetary policy" (slot verified on the online program
23 Aug 2026 — the organizers resolved Max's 4pm double-booking by moving paper #287
to 2pm, keeping this paper at 4pm). Discussant: Max Ghenis (PolicyEngine). Author
response: Olga Cantó & Francisco García-Rodríguez.

- `app/slides/*.tsx` — 26 slides (Next.js + Tailwind): 14 present the paper plus a
  6-slide discussant-added statutory-schedules build (policy-by-policy reveal + recap),
  divider + 4 discussion comments + close
- `public/figures/` — figures cropped from the authors' PDFs (`source/`)
- `REVIEW.md` — adversarial review findings (CONFIRMED/PLAUSIBLE/REFUTED) behind
  the discussion slides; full evidence in `REVIEW-APPENDIX.md`
- `SPEAKER-NOTES.md` — talk track with every number sourced to a paper table
- `export/discussant-slides.pdf` — PDF for the Oxford Abstracts upload
  (upload mechanics: only the submitter uploads, so the PDF goes to Olga Cantó)

```bash
bun install
bun run dev          # http://localhost:3000  (arrow keys; ?slide=N deep-links)
bun run export       # Playwright → export/slide-NN.png
uv run --with pillow python make_pdf.py   # PNGs → export/discussant-slides.pdf
```
