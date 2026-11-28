// Render 1 frame 6 gaya color grading ke PNG 4320x5400 (4x). Usage: python3 social/build_grading_1frame.py && node social/render_grading_1frame.js
const { chromium } = require('playwright'); const path = require('path');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1080, height: 1350 }, deviceScaleFactor: 4 });
  await p.goto('file://' + path.join(__dirname, 'grading_1frame.html')); await p.waitForLoadState('load'); await p.evaluate(() => document.fonts.ready);
  await p.locator('#g1').screenshot({ path: path.join(__dirname, 'variasi-grading', '6-color-grading-1-frame.png') }); console.log('saved');
  await b.close();
})();
