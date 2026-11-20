const { chromium } = require('playwright'); const path = require('path');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 2400, height: 2200 }, deviceScaleFactor: 3 });
  await p.goto('file://' + path.join(__dirname, 'menu.html')); await p.waitForLoadState('networkidle'); await p.evaluate(() => document.fonts.ready);
  await p.locator('#menu-a4').screenshot({ path: path.join(__dirname, 'Menu_Bajoy_A4.png') });
  const s = await b.newPage({ viewport: { width: 2400, height: 2200 }, deviceScaleFactor: 1 });
  await s.goto('file://' + path.join(__dirname, 'menu.html')); await s.waitForLoadState('networkidle'); await s.evaluate(() => document.fonts.ready);
  for (const id of ['menu-story-1-makanan', 'menu-story-2-minuman']) await s.locator('#' + id).screenshot({ path: path.join(__dirname, id + '.png') });
  const q = await b.newPage();
  await q.goto('file://' + path.join(__dirname, 'menu-print.html')); await q.waitForLoadState('networkidle'); await q.evaluate(() => document.fonts.ready);
  await q.pdf({ path: path.join(__dirname, 'Menu_Bajoy_A4.pdf'), width: '210mm', height: '297mm', printBackground: true });
  await b.close(); console.log('ok');
})();
