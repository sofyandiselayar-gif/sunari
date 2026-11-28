// Render story "Menari di SunaRi" versi tamu ke PNG HD 2160x3840 (9:16). Usage: python3 social/build_menari_story.py && node social/render_menari_story.js
const { chromium } = require('playwright'); const path = require('path'); const fs = require('fs');
(async () => {
  const b = await chromium.launch(); const out = path.join(__dirname, 'menari-story'); fs.mkdirSync(out, { recursive: true });
  const p = await b.newPage({ viewport: { width: 1200, height: 2000 }, deviceScaleFactor: 2 });
  await p.goto('file://' + path.join(__dirname, 'menari_story.html')); await p.waitForLoadState('load'); await p.evaluate(() => document.fonts.ready);
  for (const id of await p.$$eval('.s', ts => ts.map(t => t.id))) { await p.locator('#' + id).screenshot({ path: path.join(out, id + '.png') }); console.log('saved', id); }
  await b.close();
})();
