// Render each template in social-kit.html to PNG.
// Usage: node social/render.js   (requires Playwright)
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 2400, height: 2200 } });
  await page.goto('file://' + path.join(__dirname, 'social-kit.html'));
  await page.evaluate(() => document.fonts.ready);
  await page.waitForTimeout(500);
  for (const id of ['feed-senja', 'feed-promo', 'feed-quote', 'story-senja']) {
    await page.locator('#' + id).screenshot({ path: path.join(__dirname, id + '.png') });
    console.log('saved', id + '.png');
  }
  await browser.close();
})();
