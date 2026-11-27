// Render story "Bungalow Mana yang Cocok Buat Kamu?" ke PNG HD (retina 2x = 2160x3840).
// Usage: python3 social/build_pilih_bungalow_story.py && node social/render_pilih_bungalow_story.js
const { chromium } = require('playwright'); const path = require('path'); const fs = require('fs');
(async () => {
  const b = await chromium.launch(); const out = path.join(__dirname, 'pilih-bungalow-story'); fs.mkdirSync(out, { recursive: true });
  const p = await b.newPage({ viewport: { width: 1200, height: 2100 }, deviceScaleFactor: 2 });
  await p.goto('file://' + path.join(__dirname, 'pilih_bungalow_story.html')); await p.waitForLoadState('networkidle'); await p.evaluate(() => document.fonts.ready);
  await p.evaluate(() => Promise.all([...document.images].map(i => i.complete ? 0 : new Promise(r => { i.onload = i.onerror = r; }))));
  for (const id of await p.$$eval('.s', ts => ts.map(t => t.id))) { await p.locator('#' + id).screenshot({ path: path.join(out, id + '.png') }); console.log('saved', id); }
  await b.close();
})();
