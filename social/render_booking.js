// Render story "Cara Reservasi" ke PNG + cek ruang. Usage: python3 social/build_booking.py && node social/render_booking.js
const { chromium } = require('playwright'); const path = require('path'); const fs = require('fs');
(async () => {
  const b = await chromium.launch(); const out = path.join(__dirname, 'story-booking'); fs.mkdirSync(out, { recursive: true });
  const p = await b.newPage({ viewport: { width: 1200, height: 2000 } });
  await p.goto('file://' + path.join(__dirname, 'booking.html')); await p.waitForLoadState('networkidle'); await p.evaluate(() => document.fonts.ready);
  const info = await p.$$eval('.s', ss => ss.map(s => { const body = s.querySelector('.body'); if (!body) return [s.id, ''];
    const br = body.getBoundingClientRect(); let top = 1e9, bot = 0;
    body.querySelectorAll('*').forEach(e => { const r = e.getBoundingClientRect(); if (r.height) { top = Math.min(top, r.top); bot = Math.max(bot, r.bottom); } });
    return [s.id, `top ${Math.round(top - br.top)} bottom ${Math.round(br.bottom - bot)}`]; }));
  for (const [id, m] of info) { await p.locator('#' + id).screenshot({ path: path.join(out, id + '.png') }); console.log(id, m); }
  await b.close();
})();
