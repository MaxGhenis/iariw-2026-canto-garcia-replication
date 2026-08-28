import { expect, test } from '@playwright/test';
import * as fs from 'fs';

const SLIDE_COUNT = Number(process.env.SLIDE_COUNT || 27);
const port = process.env.PORT || '3000';

test('export all slides as PNGs', async ({ page }) => {
  test.setTimeout(300000);
  fs.mkdirSync('export', { recursive: true });
  for (const file of fs.readdirSync('export')) {
    if (/^slide-\d+\.png$/.test(file)) fs.rmSync(`export/${file}`);
  }

  const pageErrors: string[] = [];
  const responseErrors: string[] = [];
  page.on('pageerror', (error) => pageErrors.push(error.message));
  page.on('response', (response) => {
    if (response.status() >= 400) {
      responseErrors.push(`${response.status()} ${response.url()}`);
    }
  });

  for (let i = 0; i < SLIDE_COUNT; i++) {
    pageErrors.length = 0;
    responseErrors.length = 0;
    const response = await page.goto(`http://localhost:${port}/?slide=${i}`);
    expect(response?.ok(), `slide ${i + 1} navigation`).toBe(true);
    await page.waitForLoadState('networkidle');
    await expect(page.getByTestId('slide-counter')).toHaveText(
      `${i + 1} / ${SLIDE_COUNT}`,
    );
    await page.evaluate(async () => {
      await document.fonts.ready;
      const images = Array.from(document.images);
      await Promise.all(images.map((img) => img.decode()));
      for (const img of images) {
        if (img.naturalWidth === 0 || img.naturalHeight === 0) {
          throw new Error(`Broken image: ${img.currentSrc || img.src}`);
        }
      }
    });
    expect(pageErrors, `slide ${i + 1} page errors`).toEqual([]);
    expect(responseErrors, `slide ${i + 1} HTTP errors`).toEqual([]);
    const n = String(i + 1).padStart(2, '0');
    await page.screenshot({ path: `export/slide-${n}.png` });
  }
});
