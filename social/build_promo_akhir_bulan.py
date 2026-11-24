"""Story Instagram "Promo Akhir Bulan" (1080x1920), 1 frame, versi elegan. Soft selling, diskon 15%.
Run: python3 social/build_promo_akhir_bulan.py && node social/render_promo_akhir_bulan.js -> social/promo-akhir-bulan/promo-story.png"""
import pathlib
H = pathlib.Path(__file__).parent
LOGO_D = "../assets/logo-sunari-color-dark.png"; P = "../assets/photos/senja/42-teras-bingkai-daun-1744.jpg"
FONTS = '<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;1,400;1,500&family=Playfair+Display:ital,wght@0,400;1,400&family=Montserrat:wght@500;600;700&display=swap" rel="stylesheet">'
GOLD = "#E9C48A"
CSS = f"""
*{{margin:0;padding:0;box-sizing:border-box}}body{{background:#bbb;font-family:Montserrat,sans-serif}}
.s{{position:relative;overflow:hidden;width:1080px;height:1920px;margin:30px auto;background:#120b06;color:#FBF4EC;text-align:center}}
.bg{{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:50% 50%;filter:saturate(1.05) contrast(1.04)}}
.vt{{position:absolute;left:0;right:0;top:0;height:640px;background:linear-gradient(180deg,rgba(14,8,4,.7),rgba(14,8,4,.3) 75%,rgba(14,8,4,0))}}
.vb{{position:absolute;left:0;right:0;bottom:0;height:960px;background:linear-gradient(0deg,rgba(14,8,4,.9),rgba(14,8,4,.72) 62%,rgba(14,8,4,0))}}
.fr{{position:absolute;inset:46px;border:1px solid rgba(233,196,138,.55)}}
.fr2{{position:absolute;inset:58px;border:1px solid rgba(233,196,138,.22)}}
.lg{{position:absolute;left:50%;transform:translateX(-50%);top:250px;width:220px;filter:drop-shadow(0 2px 8px rgba(0,0,0,.5))}}
.cap{{font-weight:600;font-size:20px;letter-spacing:.5em;text-transform:uppercase;color:{GOLD}}}
.orn{{display:flex;align-items:center;justify-content:center;gap:22px;color:{GOLD}}}
.orn i{{display:block;width:120px;height:1px;background:linear-gradient(90deg,rgba(233,196,138,0),{GOLD})}}
.orn i:last-child{{transform:scaleX(-1)}}
.orn b{{width:9px;height:9px;transform:rotate(45deg);border:1px solid {GOLD}}}
.sh{{text-shadow:0 2px 16px rgba(0,0,0,.55)}}
"""
html = f'''<div class="s" id="promo-story"><img class="bg" src="{P}" alt="">
  <div class="vt"></div><div class="vb"></div><div class="fr"></div><div class="fr2"></div>
  <img class="lg" src="{LOGO_D}" alt="">
  <div class="sh" style="position:absolute;left:90px;right:90px;top:370px">
    <div style="font-family:'Cormorant Garamond',serif;font-weight:500;font-size:116px;line-height:.98">Promo<br><i style="color:{GOLD};font-weight:400">Akhir Bulan</i></div></div>
  <div class="sh" style="position:absolute;left:90px;right:90px;top:985px">
    <div class="orn"><i></i><b></b><i></i></div>
    <div class="cap" style="margin-top:26px;color:#FBF4EC">Diskon</div>
    <div style="font-family:'Cormorant Garamond',serif;font-weight:500;font-size:166px;line-height:.9;color:{GOLD};margin-top:6px">15%</div>
    <div style="font-family:'Cormorant Garamond',serif;font-style:italic;font-size:44px;margin-top:6px">untuk semua tipe kamar</div>
    <div style="font-family:'Cormorant Garamond',serif;font-style:italic;font-size:42px;line-height:1.28;margin:24px 30px 0;color:#F3E3CC">“Sebelum bulan ini berakhir, ada senja yang ingin menyambutmu lebih hangat.”</div>
    <div style="display:flex;justify-content:center;margin-top:26px;border-top:1px solid rgba(233,196,138,.45);border-bottom:1px solid rgba(233,196,138,.45)">
      <div style="flex:1;padding:16px 0"><div class="cap" style="font-size:17px">Pesan</div><div style="font-family:'Cormorant Garamond',serif;font-size:40px;margin-top:6px">15 – 28 Nov 2026</div></div>
      <div style="width:1px;background:rgba(233,196,138,.45)"></div>
      <div style="flex:1;padding:16px 0"><div class="cap" style="font-size:17px">Menginap</div><div style="font-family:'Cormorant Garamond',serif;font-size:40px;margin-top:6px">20 – 30 Nov 2026</div></div></div>
    <div class="cap" style="margin-top:28px;font-size:18px;letter-spacing:.4em">Reservasi via WhatsApp</div>
    <div style="font-family:'Cormorant Garamond',serif;font-size:56px;margin-top:4px">0821-8903-3044</div></div></div>'''
(H / "promo_akhir_bulan.html").write_text(f'<!doctype html><html lang="id"><head><meta charset="utf-8">{FONTS}<style>{CSS}</style></head><body>{html}</body></html>')

# ---- versi feed 3:4 (1080x1440)
CSSF = CSS.replace("height:1920px", "height:1440px").replace("object-position:50% 50%", "object-position:50% 44%") \
          .replace("height:640px;background:linear-gradient(180deg", "height:520px;background:linear-gradient(180deg") \
          .replace("height:960px;background:linear-gradient(0deg", "height:760px;background:linear-gradient(0deg") \
          .replace("inset:46px", "inset:34px").replace("inset:58px", "inset:46px") \
          .replace("top:250px;width:220px;", "top:88px;width:200px;")
feed = html.replace('id="promo-story"', 'id="promo-feed"') \
           .replace('top:370px">', 'top:196px">').replace("font-size:116px;line-height:.98", "font-size:104px;line-height:.98") \
           .replace('top:985px">', 'top:742px">').replace("font-size:166px;line-height:.9", "font-size:150px;line-height:.9") \
           .replace("font-size:42px;line-height:1.28;margin:24px 30px 0", "font-size:38px;line-height:1.25;margin:18px 40px 0") \
           .replace("margin-top:26px;border-top:1px", "margin-top:22px;border-top:1px").replace("flex:1;padding:16px 0", "flex:1;padding:12px 0") \
           .replace("margin-top:28px;font-size:18px;letter-spacing:.4em", "margin-top:20px;font-size:18px;letter-spacing:.4em")
(H / "promo_akhir_bulan_feed.html").write_text(f'<!doctype html><html lang="id"><head><meta charset="utf-8">{FONTS}<style>{CSSF}</style></head><body>{feed}</body></html>')
