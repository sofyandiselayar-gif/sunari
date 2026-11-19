// Render every .tpl in kit.html to PNG. Room-tour slides (sb-/st-/vp-) go to carousel/.
// Usage: python3 social/build_kit.py && node social/render.js
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 2400, height: 2200 } });
  await page.goto('file://' + path.join(__dirname, 'kit.html'));
  await page.waitForLoadState('networkidle');
  await page.evaluate(() => document.fonts.ready);
  for (const id of await page.$$eval('.tpl', els => els.map(e => e.id))) {
    const dir = /^(sb|st|vp|vs|fs|faq)-/.test(id) ? path.join(__dirname, 'carousel') : /^sd-/.test(id) ? path.join(__dirname, 'stories') : /^hs-/.test(id) ? path.join(__dirname, 'highlight-stories') : /^p\d\d-/.test(id) ? path.join(__dirname, 'feed12') : __dirname;
    await page.locator('#' + id).screenshot({ path: path.join(dir, id + '.png') });
    console.log('saved', path.relative(__dirname, path.join(dir, id + '.png')));
  }
  await page.goto('file://' + path.join(__dirname, 'grid.html'));
  await page.waitForLoadState('networkidle');
  await page.evaluate(() => document.fonts.ready);
  await page.locator('#grid-preview').screenshot({ path: path.join(__dirname, 'grid-preview.png') });
  console.log('saved grid-preview.png');
  await browser.close();
})();
