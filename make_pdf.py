"""Assemble export/slide-NN.png into export/discussant-slides.pdf (run after `bun run export`).

Playwright captures at deviceScaleFactor 2 (3840x2160); pages are downscaled to 1920x1080
so the PDF stays email-sized (~4 MB) while remaining crisp on a projector.
"""
from pathlib import Path

from PIL import Image

SLIDE_COUNT = 27
export_dir = Path("export")
pngs = sorted(export_dir.glob("slide-*.png"))
expected = [export_dir / f"slide-{i:02d}.png" for i in range(1, SLIDE_COUNT + 1)]
assert pngs == expected, (
    f"expected exactly {SLIDE_COUNT} contiguous slide PNGs; "
    "run `bun run export` again"
)
frames = []
for p in pngs:
    im = Image.open(p).convert("RGB")
    if im.size != (1920, 1080):
        im = im.resize((1920, 1080), Image.LANCZOS)
    frames.append(im)
out = export_dir / "discussant-slides.pdf"
frames[0].save(out, save_all=True, append_images=frames[1:], resolution=72.0)
print(f"wrote {out} ({len(frames)} pages)")
