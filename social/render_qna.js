// Render Q&A stories to PNG + overflow check. Usage: python3 social/build_qna.py && node social/render_qna.js
const { chromium } = require('playwright'); const path = require('path'); const fs = require('fs');
(async () => {
  const b = await chromium.launch(); const out = path.join(__dirname, 'story-qna'); fs.mkdirSync(out, { recursive: true });
  const p = await b.newPage({ viewport: { width: 1200, height: 2000 } });
  await p.goto('file://' + path.join(__dirname, 'qna.html')); await p.waitForLoadState('networkidle'); await p.evaluate(() => document.fonts.ready);
  const info = await p.$$eval('.s', ss => ss.map(s => { const ft = s.querySelector('.ft'); const body = s.querySelector('.body'); if (!ft || !body) return [s.id, null];
    let m = 0; body.querySelectorAll('*').forEach(e => { const r = e.getBoundingClientRect(); if (r.height && r.bottom > m) m = r.bottom; });
    return [s.id, Math.round(m - ft.getBoundingClientRect().top)]; }));
  for (const [id, over] of info) { await p.locator('#' + id).screenshot({ path: path.join(out, id + '.png') }); console.log(id, over === null ? '' : 'gap ' + over); }
  await b.close();
})();
