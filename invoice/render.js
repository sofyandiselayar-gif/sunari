// Render invoice.html → PDF + PNG preview. Usage: node invoice/render.js
const { chromium } = require('playwright'); const path = require('path');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 794, height: 1123 }, deviceScaleFactor: 2 });
  await p.goto('file://' + path.join(__dirname, 'invoice.html')); await p.waitForLoadState('networkidle'); await p.evaluate(() => document.fonts.ready);
  await p.locator('.page').screenshot({ path: path.join(__dirname, 'SunaRi_Invoice.png') });
  await p.pdf({ path: path.join(__dirname, 'SunaRi_Invoice.pdf'), width: '210mm', height: '297mm', printBackground: true });
  await b.close();
})();
