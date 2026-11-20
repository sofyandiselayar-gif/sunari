const { chromium } = require('playwright'); const path = require('path');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 2400, height: 2400 } });
  await p.goto('file://' + path.join(__dirname, 'build.html')); await p.waitForLoadState('networkidle');
  for (const id of ['pp-a','pp-b','pp-c','pp-d','pp-e']) await p.locator('#' + id).screenshot({ path: path.join(__dirname, id + '.png') });
  await p.reload(); await p.waitForLoadState('networkidle');
  await p.locator('#prev').screenshot({ path: path.join(__dirname, 'preview.png') });
  await b.close(); console.log('ok');
})();
