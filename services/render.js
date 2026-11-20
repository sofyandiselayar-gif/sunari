// Render each document to PDF + PNG pages. Usage: python3 services/build_docs.py && node services/render.js
const { chromium } = require('playwright'); const path = require('path'); const fs = require('fs');
(async () => {
  const b = await chromium.launch();
  fs.mkdirSync(path.join(__dirname, 'png'), { recursive: true });
  for (const f of fs.readdirSync(__dirname).filter(f => /^\d\d_.*\.html$/.test(f))) {
    const key = f.replace('.html', '');
    const p = await b.newPage({ viewport: { width: 900, height: 1200 }, deviceScaleFactor: 2 });
    await p.goto('file://' + path.join(__dirname, f)); await p.waitForLoadState('networkidle'); await p.evaluate(() => document.fonts.ready);
    const pages = await p.$$('.page');
    for (let i = 0; i < pages.length; i++) await pages[i].screenshot({ path: path.join(__dirname, 'png', `${key}_p${i + 1}.png`) });
    const over = await p.$$eval('.page', ps => ps.map(pg => {
      const ft = pg.querySelector('.ft').getBoundingClientRect().top; let m = 0;
      pg.querySelectorAll(':scope > *:not(.ft):not(.frame):not(.frame2):not(.paper):not(.grain), :scope > *:not(.ft):not(.frame):not(.frame2):not(.paper):not(.grain) *').forEach(e => { const r = e.getBoundingClientRect(); if (r.height && r.bottom > m) m = r.bottom; });
      return Math.round(m - ft); }));
    console.log(key, 'pages', pages.length, 'overlap px', over.join(','));
    await p.pdf({ path: path.join(__dirname, `SunaRi_${key}.pdf`), width: '210mm', height: '297mm', printBackground: true });
  }
  await b.close();
})();
