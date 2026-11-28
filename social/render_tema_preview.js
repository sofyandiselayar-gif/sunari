// Render preview 5 tema: slide contoh 2160x2700 & papan 1 frame 4320x5400. Usage: python3 social/build_tema_preview.py && node social/render_tema_preview.js
const { chromium } = require('playwright'); const path = require('path'); const fs = require('fs');
(async () => {
  const b = await chromium.launch(); const out = path.join(__dirname, 'tema-preview'); fs.mkdirSync(out, { recursive: true });
  let p = await b.newPage({ viewport: { width: 1200, height: 1500 }, deviceScaleFactor: 2 });
  await p.goto('file://' + path.join(__dirname, 'tema_preview.html')); await p.waitForLoadState('load'); await p.evaluate(() => document.fonts.ready);
  for (let i = 1; i <= 5; i++) { await p.locator('#tema-' + i).screenshot({ path: path.join(out, `tema-${i}.png`) }); console.log('saved tema', i); }
  p = await b.newPage({ viewport: { width: 1080, height: 1350 }, deviceScaleFactor: 4 });
  await p.goto('file://' + path.join(__dirname, 'tema_board.html')); await p.waitForLoadState('load'); await p.evaluate(() => document.fonts.ready);
  await p.locator('#board').screenshot({ path: path.join(out, '5-tema-carousel-1-frame.png') }); console.log('saved board');
  await b.close();
})();
