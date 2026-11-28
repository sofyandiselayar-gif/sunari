// Render 1 frame rekomendasi color grading ke PNG HD 2160x2700. Usage: python3 social/build_rekomendasi_grading.py && node social/render_rekomendasi_grading.js
const { chromium } = require('playwright'); const path = require('path');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1200, height: 1500 }, deviceScaleFactor: 2 });
  await p.goto('file://' + path.join(__dirname, 'rekomendasi_grading.html')); await p.waitForLoadState('load'); await p.evaluate(() => document.fonts.ready);
  await p.locator('#rekomendasi').screenshot({ path: path.join(__dirname, 'variasi-grading', 'rekomendasi-6-color-grading.png') }); console.log('saved');
  await b.close();
})();
