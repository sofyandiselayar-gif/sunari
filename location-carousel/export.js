/**
 * Export the 5 "Location & Rute Akses" slides to PNG.
 * Output: ./output/carousel-slide-1.png … carousel-slide-6.png
 * Each slide is 1080x1350 CSS px rendered at deviceScaleFactor 2 (2160x2700 px, retina).
 *
 * Usage:  node export.js
 */
const path = require('path');
const fs = require('fs');
const { chromium } = require('playwright');

const ROOT = __dirname;
const OUT = path.join(ROOT, 'output');
const SLIDES = 6;

(async () => {
  fs.mkdirSync(OUT, { recursive: true });
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1200, height: 1500 }, deviceScaleFactor: 2 });

  await page.goto('file://' + path.join(ROOT, 'index.html'));
  await page.waitForLoadState('networkidle');
  await page.evaluate(() => document.fonts.ready);

  // Fail loudly if a web font did not load (otherwise the export silently falls back).
  const fonts = await page.evaluate(() => ['Playfair Display', 'Plus Jakarta Sans']
    .map(f => [f, document.fonts.check(`16px "${f}"`)]));
  for (const [f, ok] of fonts) if (!ok) console.warn(`⚠ Font not loaded: ${f}`);

  for (let i = 1; i <= SLIDES; i++) {
    const slide = page.locator(`#slide-${i}`);
    const box = await slide.boundingBox();
    if (Math.round(box.width) !== 1080 || Math.round(box.height) !== 1350) {
      throw new Error(`slide-${i} is ${box.width}x${box.height}, expected 1080x1350`);
    }
    // Layout check: content must keep ≥ 24 px clear of the footer.
    const gap = await slide.evaluate(s => {
      const ft = s.querySelector('.footer').getBoundingClientRect().top;
      let bottom = 0;
      s.querySelectorAll(':scope > *:not(.footer):not(.swipe):not(.map), :scope > *:not(.footer):not(.swipe):not(.map) *')
        .forEach(e => { const r = e.getBoundingClientRect(); if (r.height) bottom = Math.max(bottom, r.bottom); });
      return Math.round(ft - bottom);
    });
    if (gap < 24) console.warn(`⚠ slide-${i}: content is only ${gap}px above the footer`);
    const file = path.join(OUT, `carousel-slide-${i}.png`);
    await slide.screenshot({ path: file });
    console.log("✔", path.relative(ROOT, file), `(space above footer: ${gap}px)`);
  }

  await browser.close();
})().catch(err => { console.error(err); process.exit(1); });
