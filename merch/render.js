// Render artworks (transparent, 3x), product mockups, overview sheet and PDF catalog.
// Usage: python3 merch/build_art.py && python3 merch/build_mockups.py && node merch/render.js
const { chromium } = require('playwright'); const path = require('path'); const fs = require('fs');
const open = async (b, file, scale) => {
  const p = await b.newPage({ viewport: { width: 2600, height: 2400 }, deviceScaleFactor: scale });
  await p.goto('file://' + path.join(__dirname, file)); await p.waitForLoadState('networkidle'); await p.evaluate(() => document.fonts.ready);
  return p;
};
(async () => {
  const b = await chromium.launch();
  const a = await open(b, 'art.html', 3);
  for (const id of await a.$$eval('.art', e => e.map(x => x.id)))
    await a.locator('#' + id).screenshot({ path: path.join(__dirname, 'artwork', id + '.png'), omitBackground: true });
  if (fs.existsSync(path.join(__dirname, 'mockups.html'))) {
    fs.rmSync(path.join(__dirname, 'mockup'), { recursive: true, force: true }); fs.mkdirSync(path.join(__dirname, 'mockup'));
    const m = await open(b, 'mockups.html', 1);
    for (const id of await m.$$eval('.mk', e => e.map(x => x.id)))
      await m.locator('#' + id).screenshot({ path: path.join(__dirname, 'mockup', id + '.png') });
    fs.rmSync(path.join(__dirname, 'mockup-clean'), { recursive: true, force: true }); fs.mkdirSync(path.join(__dirname, 'mockup-clean'));
    await m.addStyleTag({ content: '.mk .lab,.mk .code{display:none!important}' });
    for (const id of await m.$$eval('.mk', e => e.map(x => x.id)))
      await m.locator('#' + id).screenshot({ path: path.join(__dirname, 'mockup-clean', id + '.png') });
    const o = await open(b, 'overview.html', 1);
    await o.locator('#sheet').screenshot({ path: path.join(__dirname, 'merch-overview.png') });
    const c = await open(b, 'catalog.html', 1);
    await c.pdf({ path: path.join(__dirname, 'SunaRi_Katalog_Souvenir.pdf'), width: '297mm', height: '210mm', printBackground: true });
  }
  await b.close(); console.log('ok');
})();
