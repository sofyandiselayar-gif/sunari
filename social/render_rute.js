// Render story "Rute ke SunaRi" ke PNG. Usage: python3 social/build_rute.py && node social/render_rute.js
const { chromium } = require('playwright'); const path = require('path'); const fs = require('fs');
(async () => {
  const b = await chromium.launch(); const out = path.join(__dirname, 'story-rute'); fs.mkdirSync(out, { recursive: true });
  const p = await b.newPage({ viewport: { width: 1200, height: 2000 } });
  await p.goto('file://' + path.join(__dirname, 'rute.html')); await p.waitForLoadState('networkidle'); await p.evaluate(() => document.fonts.ready);
  const info = await p.$$eval('.s', ss => ss.map(s => { const r = s.getBoundingClientRect(), c = s.querySelector('.card').getBoundingClientRect();
    return [s.id, Math.round(c.top - r.top), Math.round(r.bottom - c.bottom)]; }));
  for (const [id, top, bot] of info) { await p.locator('#' + id).screenshot({ path: path.join(out, id + '.png') }); console.log(id, 'card top', top, 'bottom gap', bot); }
  await b.close();
})();
