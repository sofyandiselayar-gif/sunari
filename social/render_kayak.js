// Render tips kayak: feed (kayak.html -> kayak-tips/) & story (kayak_story.html -> kayak-tips-story/).
// Usage: python3 social/build_kayak.py && node social/render_kayak.js
const { chromium } = require('playwright'); const path = require('path'); const fs = require('fs');
(async () => {
  const b = await chromium.launch();
  for (const [html, dir] of [['kayak.html', 'kayak-tips'], ['kayak_story.html', 'kayak-tips-story']]) {
    const out = path.join(__dirname, dir); fs.mkdirSync(out, { recursive: true });
    const p = await b.newPage({ viewport: { width: 1200, height: 2100 } });
    await p.goto('file://' + path.join(__dirname, html)); await p.waitForLoadState('networkidle'); await p.evaluate(() => document.fonts.ready);
    for (const id of await p.$$eval('.t', ts => ts.map(t => t.id))) { await p.locator('#' + id).screenshot({ path: path.join(out, id + '.png') }); }
    console.log(dir, 'ok'); await p.close();
  }
  await b.close();
})();
