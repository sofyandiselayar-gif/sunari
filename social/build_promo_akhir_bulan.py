"""Story Instagram "Promo Akhir Bulan" (1080x1920), 1 frame. Soft selling, diskon 15%.
Run: python3 social/build_promo_akhir_bulan.py && node social/render_promo_akhir_bulan.js -> social/promo-akhir-bulan/promo-story.png"""
import pathlib
H = pathlib.Path(__file__).parent
LOGO_D = "../assets/logo-sunari-color-dark.png"; P = "../assets/photos/graded/senja__74-matahari-menyentuh-laut-kapal.jpg"
FONTS = '<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;1,400;1,500&family=Montserrat:wght@500;600;700;800&display=swap" rel="stylesheet">'
CSS = """
*{margin:0;padding:0;box-sizing:border-box}body{background:#bbb;font-family:Montserrat,sans-serif}
.s{position:relative;overflow:hidden;width:1080px;height:1920px;margin:30px auto;background:#1d140e;color:#FBF4EC}
.bg{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:60% 50%}
.vt{position:absolute;left:0;right:0;top:0;height:900px;background:linear-gradient(180deg,rgba(20,12,6,.72),rgba(20,12,6,.35) 60%,rgba(20,12,6,0))}
.vb{position:absolute;left:0;right:0;bottom:0;height:900px;background:linear-gradient(0deg,rgba(20,12,6,.85),rgba(20,12,6,.5) 55%,rgba(20,12,6,0))}
.lg{position:absolute;left:76px;top:250px;width:240px;filter:drop-shadow(0 2px 8px rgba(0,0,0,.5))}
.tx{position:absolute;left:76px;right:76px;text-shadow:0 2px 14px rgba(0,0,0,.55)}
.kick{font-weight:700;font-size:24px;letter-spacing:.34em;text-transform:uppercase}
"""
html = f'''<div class="s" id="promo-story"><img class="bg" src="{P}" alt="">
  <div class="vt"></div><div class="vb"></div><img class="lg" src="{LOGO_D}" alt="">
  <div class="tx" style="top:430px">
    <div class="kick" style="color:#FDB15D">Sunari Beach Resort · Selayar</div>
    <div style="font-family:'Playfair Display',serif;font-size:118px;line-height:1.04;margin-top:20px">Promo<br>Akhir <em style="color:#FDB15D">Bulan</em></div>
    <div style="margin-top:36px;display:flex;align-items:baseline;gap:22px">
      <span style="font-family:'Playfair Display',serif;font-size:150px;line-height:1;color:#FDB15D">15%</span>
      <span style="font-weight:700;font-size:30px;letter-spacing:.2em;text-transform:uppercase;line-height:1.35">Diskon<br>semua tipe kamar</span></div></div>
  <div class="tx" style="bottom:262px">
    <div style="font-family:'Playfair Display',serif;font-style:italic;font-size:48px;line-height:1.28">Sebelum bulan ini berakhir, ada senja yang ingin menyambutmu lebih hangat.</div>
    <div style="margin-top:30px;border-top:1.5px solid rgba(251,244,236,.4)">
      <div style="padding:13px 0;border-bottom:1.5px solid rgba(251,244,236,.3);font-size:30px">🗓️ &nbsp;<b>Pesan</b> &nbsp;15 – 28 November 2026</div>
      <div style="padding:13px 0;border-bottom:1.5px solid rgba(251,244,236,.3);font-size:30px">🏝️ &nbsp;<b>Menginap</b> &nbsp;20 – 30 November 2026</div></div>
    <div style="margin-top:24px;font-weight:700;font-size:25px;letter-spacing:.2em;text-transform:uppercase;color:#FDB15D">Ketuk untuk pesan lewat WhatsApp</div>
    <div style="font-family:'Playfair Display',serif;font-size:48px;margin-top:6px">0821-8903-3044</div></div></div>'''
(H / "promo_akhir_bulan.html").write_text(f'<!doctype html><html lang="id"><head><meta charset="utf-8">{FONTS}<style>{CSS}</style></head><body>{html}</body></html>')
