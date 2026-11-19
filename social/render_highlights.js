const { chromium } = require('playwright'); const path = require('path'); const fs = require('fs');
(async () => {
  fs.mkdirSync(path.join(__dirname, 'highlights'), { recursive: true });
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 2400, height: 2200 } });
  await p.goto('file://' + path.join(__dirname, 'highlights.html')); await p.waitForLoadState('networkidle');
  for (const id of await p.$$eval('.hl', e => e.map(x => x.id)))
    await p.locator('#' + id).screenshot({ path: path.join(__dirname, 'highlights', id + '.png') });
  await p.reload(); await p.waitForLoadState('networkidle'); await p.evaluate(() => document.fonts.ready);
  await p.locator('#preview').screenshot({ path: path.join(__dirname, 'highlights', 'preview-highlights.png') });
  await b.close(); console.log('ok');
})();
