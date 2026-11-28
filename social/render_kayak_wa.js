// Render katalog WhatsApp sewa kayak. Usage: python3 social/build_kayak_wa.py && node social/render_kayak_wa.js
// Frame .hd (wa-kayak-lengkap) dirender 2x -> PNG HD 2160x2700.
const { chromium } = require('playwright'); const path = require('path'); const fs = require('fs');
(async () => {
  const b = await chromium.launch(); const out = path.join(__dirname, 'kayak-wa'); fs.mkdirSync(out, { recursive: true });
  for (const [sel, dsf] of [['.t:not(.hd)', 1], ['.t.hd', 2]]) {
    const p = await b.newPage({ viewport: { width: 1200, height: 2000 }, deviceScaleFactor: dsf });
    await p.goto('file://' + path.join(__dirname, 'kayak_wa.html')); await p.waitForLoadState('networkidle'); await p.evaluate(() => document.fonts.ready);
    for (const id of await p.$$eval(sel, ts => ts.map(t => t.id))) { await p.locator('#' + id).screenshot({ path: path.join(out, id + '.png') }); console.log('saved', id); }
    await p.close();
  }
  await b.close();
})();
