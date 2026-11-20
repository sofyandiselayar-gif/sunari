// Render e-book: PDF A4 + PNG per halaman + cek konten tidak menabrak footer.
// Usage: python3 ebook/build_ebook.py && node ebook/render.js
const { chromium } = require('playwright'); const path = require('path'); const fs = require('fs');
(async () => {
  const b = await chromium.launch(); const out = path.join(__dirname, 'png'); fs.mkdirSync(out, { recursive: true });
  const p = await b.newPage({ viewport: { width: 900, height: 1200 }, deviceScaleFactor: 2 });
  await p.goto('file://' + path.join(__dirname, 'ebook.html')); await p.waitForLoadState('networkidle'); await p.evaluate(() => document.fonts.ready);
  const over = await p.$$eval('.page', ps => ps.map(pg => { const run = pg.querySelector('.run'); if (!run) return null;
    const ft = run.getBoundingClientRect().top; let m = 0;
    pg.querySelectorAll(':scope > *:not(.run), :scope > *:not(.run) *').forEach(e => { const r = e.getBoundingClientRect(); if (r.height && r.bottom > m) m = r.bottom; });
    return Math.round(ft - m); }));
  over.forEach((g, i) => { if (g !== null && g < 8) console.log(`⚠ halaman ${i + 1}: konten ${g}px dari footer`); });
  console.log('jarak ke footer:', over.map((g, i) => `${i + 1}:${g === null ? '-' : g}`).join(' '));
  const pages = await p.$$('.page');
  for (let i = 0; i < pages.length; i++) await pages[i].screenshot({ path: path.join(out, `halaman-${String(i + 1).padStart(2, '0')}.png`) });
  await p.pdf({ path: path.join(__dirname, 'SunaRi_Ebook_Panduan_Lengkap.pdf'), width: '210mm', height: '297mm', printBackground: true });
  await b.close(); console.log(pages.length, 'halaman dirender');
})();
