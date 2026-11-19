// Render brand-board.html to brand-board.png (run after social/render.js so campaign tiles exist).
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1600, height: 1200 }, deviceScaleFactor: 2 });
  await p.goto('file://' + path.join(__dirname, 'brand-board.html'));
  await p.waitForLoadState('networkidle');
  await p.evaluate(() => document.fonts.ready);
  await p.locator('#board').screenshot({ path: path.join(__dirname, 'brand-board.png') });
  console.log('saved brand-board.png');
  await b.close();
})();
