"""Gambar katalog WhatsApp Business: VIP Standard Bungalow (1080x1080, maks. 10 gambar per produk).
Run: python3 social/build_vipstd_wa.py && node social/render_vipstd_wa.js -> social/vip-standard-wa/*.png"""
import pathlib
H = pathlib.Path(__file__).parent
LOGO = "../assets/logo-sunari-color.png"; LOGO_D = "../assets/logo-sunari-color-dark.png"; P = "../assets/photos/vip-standard-bungalow/"
FONTS = '<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;1,400;1,500&family=Montserrat:wght@500;600;700&display=swap" rel="stylesheet">'
CSS = """
*{margin:0;padding:0;box-sizing:border-box}body{background:#bbb;font-family:Montserrat,sans-serif}
.t{position:relative;overflow:hidden;width:1080px;height:1080px;margin:30px auto;background:#FBF4EC}
.t img.bg{width:100%;height:100%;object-fit:cover}
.lg{position:absolute;left:40px;top:36px;width:230px;filter:drop-shadow(0 2px 8px rgba(0,0,0,.5))}
.lb{position:absolute;left:40px;bottom:40px;background:rgba(251,244,236,.94);border-radius:16px;padding:16px 26px;font-weight:700;font-size:24px;letter-spacing:.18em;text-transform:uppercase;color:#45301F;box-shadow:0 6px 20px rgba(0,0,0,.18)}
.emb{text-shadow:0 1.5px 0 rgba(255,255,255,.85),0 2px 4px rgba(90,62,49,.22)}
.fx{display:grid;grid-template-columns:1fr 1fr;column-gap:40px;border-top:1.5px solid rgba(138,95,72,.3)}
.fx div{padding:17px 0;border-bottom:1.5px solid rgba(138,95,72,.3);font-size:27px;color:#45301F}
.fx div::before{content:"";display:inline-block;width:10px;height:10px;border-radius:50%;background:linear-gradient(90deg,#FDB15D,#FF8A5C);margin-right:14px;vertical-align:middle}
"""
T = []
# 01 sampul
T.append(f'''<div class="t" id="wa-vip-standard-01">
  <div style="position:absolute;left:0;right:0;top:0;height:760px;overflow:hidden"><img class="bg" src="{P}04-teras-view-laut.jpg" style="object-position:50% 50%" alt=""></div>
  <img class="lg" src="{LOGO_D}" alt="">
  <div style="position:absolute;left:60px;right:60px;top:800px">
    <div style="font-weight:700;font-size:21px;letter-spacing:.32em;text-transform:uppercase;color:#7A5039">SunaRi Beach Resort · Selayar</div>
    <div class="emb" style="font-family:'Playfair Display',serif;font-size:84px;line-height:1.1;color:#45301F;margin-top:10px">VIP Standard <em style="color:#A0603E">Bungalow</em></div>
    <div style="font-size:28px;color:#4A3426;margin-top:12px">Rumah panggung tepi pantai · King bed · Termasuk sarapan</div></div></div>''')
PH = [("01-eksterior-rumah-panggung.jpg", "50% 55%", "Rumah panggung"), ("02-teras-view-pantai.jpg", "50% 60%", "Teras menghadap pantai"),
      ("03-teras-samping.jpg", "45% 55%", "Teras pribadi"), ("06-kamar-depan.jpg", "50% 55%", "King bed"),
      ("07-kamar-samping.jpg", "50% 55%", "Kamar"), ("08-wastafel-gantungan.jpg", "60% 50%", "Area wastafel"),
      ("10-kamar-mandi-shower.jpg", "50% 60%", "Kamar mandi dalam")]
for k, (img, pos, lb) in enumerate(PH, 2):
    T.append(f'''<div class="t" id="wa-vip-standard-{k:02d}"><img class="bg" src="{P}{img}" style="object-position:{pos}" alt=""><img class="lg" src="{LOGO_D}" alt=""><div class="lb">{lb}</div></div>''')
FX = ["King bed", "Termasuk sarapan", "AC &amp; Wi-Fi", "Teras kayu pribadi", "Set kopi/teh", "Pemanas air", "Tirai blackout", "Meja rias", "Shower &amp; toilet duduk", "Perlengkapan mandi"]
T.append(f'''<div class="t" id="wa-vip-standard-09"><div style="position:absolute;inset:32px;border:1.5px solid rgba(138,95,72,.4)"></div>
  <img src="{LOGO}" style="position:absolute;left:50%;transform:translateX(-50%);top:80px;width:300px" alt="">
  <div style="position:absolute;left:90px;right:90px;top:330px;text-align:center">
    <div style="font-weight:700;font-size:21px;letter-spacing:.32em;text-transform:uppercase;color:#7A5039">Fasilitas kamar</div>
    <div class="emb" style="font-family:'Playfair Display',serif;font-size:66px;color:#45301F;margin:8px 0 30px">VIP Standard <em style="color:#A0603E">Bungalow</em></div>
    <div class="fx" style="text-align:left">{"".join(f"<div>{x}</div>" for x in FX)}</div>
    <div style="margin-top:30px;font-size:26px;color:#4A3426">Untuk 2 tamu · maks. 3 dengan extra bed</div></div>
  <div style="position:absolute;left:0;right:0;bottom:62px;text-align:center;font-weight:700;font-size:19px;letter-spacing:.32em;text-transform:uppercase;color:#7A5039">Pantai Sunari · Selayar</div></div>''')
(H / "vipstd_wa.html").write_text(f'<!doctype html><html lang="id"><head><meta charset="utf-8">{FONTS}<style>{CSS}</style></head><body>{"".join(T)}</body></html>')
print(len(T))
