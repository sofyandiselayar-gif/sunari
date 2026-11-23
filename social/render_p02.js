// Render hanya carousel 02 Senja Hari Ini (p02-*) dari kit.html ke feed12/. Usage: python3 social/build_kit.py && node social/render_p02.js
const { chromium } = require('playwright'); const path = require('path');
(async () => {
  const b = await chromium.launch(); const page = await b.newPage({ viewport: { width: 2400, height: 2200 } });
  await page.goto('file://' + path.join(__dirname, 'kit.html')); await page.waitForLoadState('networkidle'); await page.evaluate(() => document.fonts.ready);
  for (const id of await page.$$eval('.tpl', els => els.map(e => e.id).filter(i => /^p02-/.test(i)))) {
    await page.locator('#' + id).screenshot({ path: path.join(__dirname, 'feed12', id + '.png') }); console.log('saved', id); }
  await b.close();
})();
