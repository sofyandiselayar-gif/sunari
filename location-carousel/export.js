/**
 * Export the 7 "Location & Rute Akses" slides to PNG.
 * Output: ./output/carousel-slide-1.png … carousel-slide-7.png
 * Each slide is 1080x1350 CSS px rendered at deviceScaleFactor 2 (2160x2700 px, retina).
 *
 * Usage:  node export.js
 */
const path = require('path');
const fs = require('fs');
const { chromium } = require('playwright');

const ROOT = __dirname;
const OUT = path.join(ROOT, 'output');
const SLIDES = 7;

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
    // Layout check: the info card must sit fully inside the slide; report where it starts
    // (map labels live above it, so a low card top means the map stays readable).
    const card = await slide.evaluate(s => {
      const r = s.getBoundingClientRect(), c = s.querySelector('.card').getBoundingClientRect();
      return { top: Math.round(c.top - r.top), bottom: Math.round(r.bottom - c.bottom) };
    });
    if (card.top < 0 || card.bottom < 0) throw new Error(`slide-${i}: card overflows the slide`);
    const file = path.join(OUT, `carousel-slide-${i}.png`);
    await slide.screenshot({ path: file });
    console.log("✔", path.relative(ROOT, file), `(card starts at y=${card.top}px)`);
  }

  await browser.close();
})().catch(err => { console.error(err); process.exit(1); });
