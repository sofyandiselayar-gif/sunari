// Render carousel "Menari di SunaRi" ke PNG HD 2160x2700 (4:5). Usage: python3 social/build_menari.py && node social/render_menari.js
const { chromium } = require('playwright'); const path = require('path'); const fs = require('fs');
(async () => {
  const b = await chromium.launch(); const out = path.join(__dirname, 'menari'); fs.mkdirSync(out, { recursive: true });
  const p = await b.newPage({ viewport: { width: 1200, height: 2000 }, deviceScaleFactor: 2 });
  await p.goto('file://' + path.join(__dirname, 'menari.html')); await p.waitForLoadState('load'); await p.evaluate(() => document.fonts.ready);
  for (const id of await p.$$eval('.t', ts => ts.map(t => t.id))) { await p.locator('#' + id).screenshot({ path: path.join(out, id + '.png') }); console.log('saved', id); }
  await b.close();
})();
