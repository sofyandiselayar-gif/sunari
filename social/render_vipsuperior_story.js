// Render seri "Jeda" ke PNG. Usage: python3 social/build_slow.py && node social/render_slow.js
const { chromium } = require('playwright'); const path = require('path'); const fs = require('fs');
(async () => {
  const b = await chromium.launch(); const out = path.join(__dirname, 'vip-superior-story'); fs.mkdirSync(out, { recursive: true });
  const p = await b.newPage({ viewport: { width: 1200, height: 2000 } });
  await p.goto('file://' + path.join(__dirname, 'vipsuperior_story.html')); await p.waitForLoadState('networkidle'); await p.evaluate(() => document.fonts.ready);
  for (const id of await p.$$eval('.s', ts => ts.map(t => t.id))) { await p.locator('#' + id).screenshot({ path: path.join(out, id + '.png') }); console.log('saved', id); }
  await b.close();
})();
