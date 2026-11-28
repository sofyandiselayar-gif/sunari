// Render story "Satu Hari di SunaRi" ke PNG 1080x1920. Usage: python3 social/build_satu_hari.py && node social/render_satu_hari.js
const { chromium } = require('playwright'); const path = require('path'); const fs = require('fs');
(async () => {
  const b = await chromium.launch(); const out = path.join(__dirname, 'satu-hari'); fs.mkdirSync(out, { recursive: true });
  const p = await b.newPage({ viewport: { width: 1200, height: 2000 } });
  await p.goto('file://' + path.join(__dirname, 'satu_hari.html')); await p.waitForLoadState('load'); await p.evaluate(() => document.fonts.ready);
  for (const id of await p.$$eval('.s', ts => ts.map(t => t.id))) { await p.locator('#' + id).screenshot({ path: path.join(out, id + '.png') }); console.log('saved', id); }
  await b.close();
})();
