const { chromium } = require('playwright'); const path = require('path'); const fs = require('fs');
(async () => {
  const b = await chromium.launch(); const out = path.join(__dirname, 'wa-cover'); fs.mkdirSync(out, { recursive: true });
  const p = await b.newPage({ viewport: { width: 1300, height: 800 }, deviceScaleFactor: 2 });
  await p.goto('file://' + path.join(__dirname, 'wa_cover.html')); await p.waitForLoadState('networkidle'); await p.evaluate(() => document.fonts.ready);
  await p.locator('#wa-cover').screenshot({ path: path.join(out, 'sampul-whatsapp-business.png') }); await b.close(); console.log('saved');
})();
