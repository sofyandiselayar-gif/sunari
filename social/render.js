// Render every .tpl element in a template file to PNG (file name = element id).
// Usage: node social/render.js [file.html ...]   (default: all template files)
const { chromium } = require('playwright');
const path = require('path');
const files = process.argv.slice(2).length ? process.argv.slice(2)
  : ['social-kit.html', 'carousel-superior.html', 'carousel-standard.html', 'carousel-vip.html'];
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 2400, height: 2200 } });
  for (const f of files) {
    const outDir = path.join(__dirname, f.startsWith('carousel') ? 'carousel' : '.');
    await page.goto('file://' + path.join(__dirname, path.basename(f)));
    await page.evaluate(() => document.fonts.ready);
    await page.waitForLoadState('networkidle');
    for (const id of await page.$$eval('.tpl', els => els.map(e => e.id))) {
      await page.locator('#' + id).screenshot({ path: path.join(outDir, id + '.png') });
      console.log('saved', path.relative(__dirname, path.join(outDir, id + '.png')));
    }
  }
  await browser.close();
})();
