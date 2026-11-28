// Render 1 frame story "Menari di SunaRi" versi tamu ke PNG HD 2160x3840. Usage: python3 social/build_menari_satu.py && node social/render_menari_satu.js
const { chromium } = require('playwright'); const path = require('path');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1200, height: 2000 }, deviceScaleFactor: 2 });
  await p.goto('file://' + path.join(__dirname, 'menari_satu.html')); await p.waitForLoadState('load'); await p.evaluate(() => document.fonts.ready);
  await p.locator('#menari-satu-frame').screenshot({ path: path.join(__dirname, 'menari-story', 'menari-satu-frame.png') }); console.log('saved');
  await b.close();
})();
