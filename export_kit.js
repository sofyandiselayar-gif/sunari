// Build the full deliverable package: PNG + PDF (editable text) + Canva-ready multi-page PDFs + ZIP.
// No compression anywhere: original PNGs, full-resolution photos in PDFs, ZIP in store mode.
// Usage: python3 social/build_kit.py && node social/render.js && node brand/render_board.js && node export_kit.js
const { chromium } = require('playwright');
const path = require('path'), fs = require('fs'), { execSync } = require('child_process');
const ROOT = __dirname, OUT = path.join(ROOT, 'export', 'SunaRi_Konten_Instagram');
const GROUPS = {
  '01_Feed': ['feed-senja','feed-kayak','camp-1','camp-2','camp-3','camp-4','camp-5','feed-values','feed-promo','feed-quote'],
  '02_Story': ['story-senja'],
  '10_Story_10_Hari': ['sd-01','sd-02','sd-03','sd-04','sd-05','sd-06','sd-07','sd-08','sd-09','sd-10'],
  '03_Carousel_Superior': ['sb-1','sb-2','sb-3','sb-4','sb-5','sb-6'],
  '04_Carousel_VIP_Superior': ['vs-1','vs-2','vs-3','vs-4','vs-5','vs-6'],
  '05_Carousel_Family_Superior': ['fs-1','fs-2','fs-3','fs-4','fs-5','fs-6'],
  '06_Carousel_Standard': ['st-1','st-2','st-3','st-4','st-5'],
  '07_Carousel_VIP_Standard': ['vp-1','vp-2','vp-3','vp-4','vp-5','vp-6'],
};
(async () => {
  fs.rmSync(path.join(ROOT, 'export'), { recursive: true, force: true });
  const b = await chromium.launch();
  const page = await b.newPage({ viewport: { width: 1200, height: 2000 } });
  await page.goto('file://' + path.join(ROOT, 'social', 'kit.html'));
  await page.waitForLoadState('networkidle');
  await page.evaluate(() => document.fonts.ready);
  const show = async (ids, h) => page.evaluate(([ids, h]) => {
    let st = document.getElementById('xp'); if (!st) { st = document.createElement('style'); st.id = 'xp'; document.head.appendChild(st); }
    st.textContent = `@page{size:1080px ${h}px;margin:0} html,body{margin:0!important;padding:0!important;background:none!important;display:block!important}
      .tpl{display:none!important} ${ids.map(i => '#' + i).join(',')}{display:block!important;break-after:page;page-break-after:always}`;
  }, [ids, h]);
  for (const [g, ids] of Object.entries(GROUPS)) {
    for (const d of ['PNG', 'PDF']) fs.mkdirSync(path.join(OUT, d, g), { recursive: true });
    for (const id of ids) {
      const src = /^(sb|st|vp|vs|fs)-/.test(id) ? `social/carousel/${id}.png` : /^sd-/.test(id) ? `social/stories/${id}.png` : `social/${id}.png`;
      fs.copyFileSync(path.join(ROOT, src), path.join(OUT, 'PNG', g, `${id}.png`));
      const h = (id.startsWith('story') || id.startsWith('sd-')) ? 1920 : 1350;
      await show([id], h);
      await page.pdf({ path: path.join(OUT, 'PDF', g, `${id}.pdf`), width: '1080px', height: h + 'px', printBackground: true, pageRanges: '1' });
    }
    // one multi-page PDF per group -> import once into Canva
    fs.mkdirSync(path.join(OUT, 'CANVA_Import'), { recursive: true });
    const h = g.includes('Story') ? 1920 : 1350;
    await show(ids, h);
    await page.pdf({ path: path.join(OUT, 'CANVA_Import', `${g}.pdf`), width: '1080px', height: h + 'px', printBackground: true });
    console.log('done', g);
  }
  await b.close();
  // extras
  const ex = path.join(OUT, '08_Brand');
  fs.mkdirSync(path.join(ex, 'Logo'), { recursive: true }); 
  for (const f of ['logo-sunari-driftwood.png','logo-sunari-cream.png','mark-sunari-driftwood.svg','mark-sunari-cream.svg'])
    fs.copyFileSync(path.join(ROOT, 'assets', f), path.join(ex, 'Logo', f));
  fs.cpSync(path.join(ROOT, 'assets/photos'), path.join(ex, 'Foto'), { recursive: true });
  fs.copyFileSync(path.join(ROOT, 'brand/brand-board.png'), path.join(ex, 'brand-board.png'));
  fs.copyFileSync(path.join(ROOT, 'brand/BRAND_GUIDE.md'), path.join(ex, 'BRAND_GUIDE.md'));
  fs.copyFileSync(path.join(ROOT, 'social/INSTAGRAM_BULAN_1.md'), path.join(OUT, 'CAPTION_30_HARI.md'));
  fs.copyFileSync(path.join(ROOT, 'ota/DESKRIPSI_OTA_GOOGLE.md'), path.join(OUT, 'DESKRIPSI_OTA_GOOGLE.md'));
  fs.copyFileSync(path.join(ROOT, 'social/TIKTOK_REELS.md'), path.join(OUT, 'CAPTION_REELS_TIKTOK.md'));
  fs.copyFileSync(path.join(ROOT, 'social/STORY_10_HARI.md'), path.join(OUT, 'RENCANA_STORY_10_HARI.md'));
  fs.copyFileSync(path.join(ROOT, 'social/grid-preview.png'), path.join(OUT, 'preview-feed-instagram.png'));
  const hl = path.join(OUT, '09_Highlight_Cover'); fs.mkdirSync(hl, { recursive: true });
  for (const f of fs.readdirSync(path.join(ROOT, 'social/highlights'))) fs.copyFileSync(path.join(ROOT, 'social/highlights', f), path.join(hl, f));
  fs.copyFileSync(path.join(ROOT, 'export_README.md'), path.join(OUT, 'BACA_DULU.md'));
    execSync('cd export && zip -0 -qr SunaRi_Konten_Instagram.zip SunaRi_Konten_Instagram');
  console.log('zip ready');
})();
