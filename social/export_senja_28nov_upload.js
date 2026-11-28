// Ekspor feed & story "Senja Hari Ini · 28 Nov" kualitas upload: render 2x (2160 px) lalu diperkecil ke 1080 px oleh
// export_senja_28nov_upload.py. Run: python3 social/build_senja_28nov.py && python3 social/build_senja_28nov_story.py
//      && node social/export_senja_28nov_upload.js && python3 social/export_senja_28nov_upload.py
const { chromium } = require('playwright'); const path = require('path'); const fs = require('fs');
const JOBS = [['senja_28nov.html', '.t', 'feed'], ['senja_28nov_story.html', '.s', 'story']];
(async () => {
  const b = await chromium.launch();
  for (const [html, sel, name] of JOBS) {
    const out = path.join(__dirname, 'upload-28nov', '_2x', name); fs.mkdirSync(out, { recursive: true });
    const p = await b.newPage({ viewport: { width: 1200, height: 2000 }, deviceScaleFactor: 2 });
    await p.goto('file://' + path.join(__dirname, html)); await p.waitForLoadState('networkidle'); await p.evaluate(() => document.fonts.ready);
    for (const id of await p.$$eval(sel, ts => ts.map(t => t.id))) { await p.locator('#' + id).screenshot({ path: path.join(out, id + '.png') }); }
    console.log('rendered', name); await p.close();
  }
  await b.close();
})();
