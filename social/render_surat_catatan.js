// Render carousel "Surat untuk Diriku" & "Catatan Satu Hari" ke PNG HD 2160x2700 (+ JPG HD q95 lewat Python).
// Usage: python3 social/build_surat_catatan.py && node social/render_surat_catatan.js
const { chromium } = require('playwright'); const path = require('path'); const fs = require('fs');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1200, height: 1500 }, deviceScaleFactor: 2 });
  for (const name of ['surat', 'catatan']) {
    const out = path.join(__dirname, name); fs.mkdirSync(out, { recursive: true });
    await p.goto('file://' + path.join(__dirname, name + '.html')); await p.waitForLoadState('load'); await p.evaluate(() => document.fonts.ready);
    for (const id of await p.$$eval('.t', ts => ts.map(t => t.id))) await p.locator('#' + id).screenshot({ path: path.join(out, id + '.png') });
    console.log('saved', name);
  }
  await b.close();
})();
