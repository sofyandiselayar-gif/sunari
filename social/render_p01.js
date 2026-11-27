// Render ulang hanya carousel p01 "Lebih dari Menginap" (sampul camp-1 + p01-2..10) dari kit.html.
// Usage: python3 social/build_kit.py && node social/render_p01.js && python3 social/assemble_feed12.py
const { chromium } = require('playwright'); const path = require('path');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 2400, height: 2200 } });
  await p.goto('file://' + path.join(__dirname, 'kit.html')); await p.waitForLoadState('networkidle'); await p.evaluate(() => document.fonts.ready);
  for (const id of await p.$$eval('.tpl', els => els.map(e => e.id).filter(i => /^p01-/.test(i)))) {
    await p.locator('#' + id).screenshot({ path: path.join(__dirname, 'feed12', id + '.png') }); console.log('saved', id);
  }
  await b.close();
})();
