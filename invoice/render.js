// Render invoice.html & invoice_kosong.html → PDF + PNG preview. Usage: node invoice/render.js
const { chromium } = require('playwright'); const path = require('path');
(async () => {
  const b = await chromium.launch();
  for (const [src, out] of [['invoice.html', 'SunaRi_Invoice'], ['invoice_kosong.html', 'SunaRi_Invoice_Kosong']]) {
    const p = await b.newPage({ viewport: { width: 794, height: 1123 }, deviceScaleFactor: 2 });
    await p.goto('file://' + path.join(__dirname, src)); await p.waitForLoadState('networkidle'); await p.evaluate(() => document.fonts.ready);
    await p.locator('.page').screenshot({ path: path.join(__dirname, out + '.png') });
    await p.pdf({ path: path.join(__dirname, out + '.pdf'), width: '210mm', height: '297mm', printBackground: true });
  }
  await b.close();
})();
