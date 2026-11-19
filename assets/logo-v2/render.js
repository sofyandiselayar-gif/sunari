const { chromium } = require('playwright'); const path = require('path');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 2600, height: 2400 }, deviceScaleFactor: 2 });
  await p.goto('file://' + path.join(__dirname, 'build.html')); await p.waitForLoadState('networkidle'); await p.evaluate(() => document.fonts.ready);
  for (const id of ['tagline-driftwood','tagline-cream','badge-driftwood','badge-cream'])
    await p.locator('#' + id).screenshot({ path: path.join(__dirname, `logo-sunari-${id}.png`), omitBackground: true });
  const p1 = await b.newPage({ viewport: { width: 2600, height: 2400 }, deviceScaleFactor: 1 });
  await p1.goto('file://' + path.join(__dirname, 'build.html')); await p1.waitForLoadState('networkidle'); await p1.evaluate(() => document.fonts.ready);
  for (const id of ['pp-logo-a','pp-logo-b']) await p1.locator('#' + id).screenshot({ path: path.join(__dirname, `${id}.png`) });
  await p.locator('#sheet').screenshot({ path: path.join(__dirname, 'logo-sheet.png') });
  await b.close(); console.log('ok');
})();
