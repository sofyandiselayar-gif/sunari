// Render invoice HTML files → PDF + PNG preview per page. Usage: node invoice/render.js
const { chromium } = require('playwright'); const path = require('path'); const fs = require('fs');
(async () => {
  const b = await chromium.launch();
  for (const [src, out] of [['invoice.html', 'SunaRi_Invoice'], ['invoice_kosong.html', 'SunaRi_Invoice_Kosong'], ['invoice_kamar_resto.html', 'SunaRi_Invoice_Kamar_Resto'], ['invoice_dennish.html', 'SunaRi_Invoice_Mr_Dennish'], ['invoice_wonderful_selayar.html', 'SunaRi_Invoice_Wonderful_Selayar'], ['invoice_arya.html', 'SunaRi_Invoice_Arya'], ['invoice_proforma_wonderful_selayar.html', 'SunaRi_Proforma_Wonderful_Selayar_Batch1'], ['invoice_proforma_wonderful_selayar_b2.html', 'SunaRi_Proforma_Wonderful_Selayar_Batch2']]) {
    if (!fs.existsSync(path.join(__dirname, src))) continue; // guest invoices are kept local only
    const p = await b.newPage({ viewport: { width: 794, height: 1123 }, deviceScaleFactor: 2 });
    await p.goto('file://' + path.join(__dirname, src)); await p.waitForLoadState('networkidle'); await p.evaluate(() => document.fonts.ready);
    const pages = p.locator('.page'); const n = await pages.count();
    for (let i = 0; i < n; i++) await pages.nth(i).screenshot({ path: path.join(__dirname, n > 1 ? `${out}_p${i + 1}.png` : out + '.png') });
    await p.pdf({ path: path.join(__dirname, out + '.pdf'), width: '210mm', height: '297mm', printBackground: true });
  }
  await b.close();
})();
