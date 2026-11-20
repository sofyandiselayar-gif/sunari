// Render artworks (transparent, 3x) then mockups.
const { chromium } = require('playwright'); const path = require('path');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 2600, height: 2400 }, deviceScaleFactor: 3 });
  await p.goto('file://' + path.join(__dirname, 'art.html')); await p.waitForLoadState('networkidle'); await p.evaluate(() => document.fonts.ready);
  for (const id of await p.$$eval('.art', e => e.map(x => x.id)))
    await p.locator('#' + id).screenshot({ path: path.join(__dirname, 'artwork', id + '.png'), omitBackground: true });
  const fs = require('fs');
  if (fs.existsSync(path.join(__dirname, 'mockups.html'))) {
    const m = await b.newPage({ viewport: { width: 2600, height: 2400 }, deviceScaleFactor: 1 });
    await m.goto('file://' + path.join(__dirname, 'mockups.html')); await m.waitForLoadState('networkidle'); await m.evaluate(() => document.fonts.ready);
    for (const id of await m.$$eval('.mk', e => e.map(x => x.id)))
      await m.locator('#' + id).screenshot({ path: path.join(__dirname, 'mockup', id + '.png') });
    if (await m.$('#sheet')) await m.locator('#sheet').screenshot({ path: path.join(__dirname, 'merch-overview.png') });
  }
  await b.close(); console.log('ok');
})();
