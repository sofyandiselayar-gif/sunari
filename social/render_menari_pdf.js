// PDF HD seri "Menari di SunaRi" versi tamu: teks vektor + foto resolusi penuh.
// Usage: python3 social/build_menari_story.py && python3 social/build_menari_satu.py && node social/render_menari_pdf.js
// -> social/menari-story/Menari_di_SunaRi_Story.pdf (10 halaman) & Menari_di_SunaRi_1_Frame.pdf (1 halaman), 1080x1920 px per halaman
const { chromium } = require('playwright'); const path = require('path');
const PRINT = '@page{size:1080px 1920px;margin:0} html,body{background:none!important;margin:0} .s{margin:0!important;page-break-after:always;break-after:page} .s:last-child{page-break-after:auto;break-after:auto}';
(async () => {
  const b = await chromium.launch(); const p = await b.newPage();
  for (const [html, out] of [['menari_story.html', 'Menari_di_SunaRi_Story.pdf'], ['menari_satu.html', 'Menari_di_SunaRi_1_Frame.pdf']]) {
    await p.goto('file://' + path.join(__dirname, html)); await p.waitForLoadState('load');
    await p.addStyleTag({ content: PRINT }); await p.evaluate(() => document.fonts.ready);
    await p.pdf({ path: path.join(__dirname, 'menari-story', out), width: '1080px', height: '1920px', printBackground: true, preferCSSPageSize: true });
    console.log('saved', out);
  }
  await b.close();
})();
