"""Gambar katalog WhatsApp Business: Family Superior Bungalow (1080x1080, maks. 10 gambar per produk).
Run: python3 social/build_family_wa.py && node social/render_family_wa.js -> social/family-wa/*.png"""
import pathlib
H = pathlib.Path(__file__).parent
LOGO = "../assets/logo-sunari-color.png"; LOGO_D = "../assets/logo-sunari-color-dark.png"; P = "../assets/photos/family-superior-bungalow/"
FONTS = '<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;1,400;1,500&family=Montserrat:wght@500;600;700&display=swap" rel="stylesheet">'
CSS = """
*{margin:0;padding:0;box-sizing:border-box}body{background:#bbb;font-family:Montserrat,sans-serif}
.t{position:relative;overflow:hidden;width:1080px;height:1080px;margin:30px auto;background:#FBF4EC}
.t img.bg{width:100%;height:100%;object-fit:cover}
.lg{position:absolute;left:40px;top:36px;width:230px;filter:drop-shadow(0 2px 8px rgba(0,0,0,.5))}
.lb{position:absolute;left:40px;bottom:40px;background:rgba(251,244,236,.94);border-radius:16px;padding:16px 26px;font-weight:700;font-size:24px;letter-spacing:.18em;text-transform:uppercase;color:#45301F;box-shadow:0 6px 20px rgba(0,0,0,.18)}
.emb{text-shadow:0 1.5px 0 rgba(255,255,255,.85),0 2px 4px rgba(90,62,49,.22)}
.fx{display:grid;grid-template-columns:1fr 1fr;column-gap:40px;border-top:1.5px solid rgba(138,95,72,.3)}
.fx div{padding:11px 0;border-bottom:1.5px solid rgba(138,95,72,.3);font-size:23px;color:#45301F}
.fx div::before{content:"";display:inline-block;width:10px;height:10px;border-radius:50%;background:linear-gradient(90deg,#FDB15D,#FF8A5C);margin-right:14px;vertical-align:middle}
"""
T = []
# 01 sampul
T.append(f'''<div class="t" id="wa-family-01">
  <div style="position:absolute;left:0;right:0;top:0;height:760px;overflow:hidden"><img class="bg" src="{P}01-eksterior-taman.jpg" style="object-position:50% 50%" alt=""></div>
  <img class="lg" src="{LOGO_D}" alt="">
  <div style="position:absolute;left:60px;right:60px;top:800px">
    <div style="font-weight:700;font-size:21px;letter-spacing:.32em;text-transform:uppercase;color:#7A5039">SunaRi Beach Resort · Selayar</div>
    <div class="emb" style="font-family:'Playfair Display',serif;font-size:76px;line-height:1.1;color:#45301F;margin-top:10px">Family Superior <em style="color:#A0603E">Bungalow</em></div>
    <div style="font-size:28px;color:#4A3426;margin-top:12px">Satu rumah, dua lantai, semua bersama · 6 orang (maks. 8)</div></div></div>''')
PH = [("02-teras-samping.jpg", "50% 55%", "Teras pribadi"), ("03-teras-sofa.jpg", "40% 55%", "Bersantai di teras"),
      ("05-kamar-bawah-depan.jpg", "50% 55%", "Lantai 1 · tempat tidur besar"), ("06-kamar-bawah-sudut.jpg", "50% 55%", "Lantai 1 · untuk 2–3 tamu"),
      ("09-lantai-atas-4-kasur.jpg", "50% 55%", "Lantai 2 · empat kasur"), ("10-lantai-atas-kasur-kettle.jpg", "45% 55%", "Lantai 2 · set kopi/teh"),
      ("12-kamar-mandi-shower.jpg", "50% 55%", "Kamar mandi di kedua lantai"), ("11-wastafel.jpg", "45% 55%", "Wastafel &amp; cermin")]
for k, (img, pos, lb) in enumerate(PH, 2):
    T.append(f'''<div class="t" id="wa-family-{k:02d}"><img class="bg" src="{P}{img}" style="object-position:{pos}" alt=""><img class="lg" src="{LOGO_D}" alt=""><div class="lb">{lb}</div></div>''')
FL = [("Lantai 1", "2 orang", ["+1 extra bed = 3 orang", "Tempat tidur besar", "Toilet &amp; kamar mandi"]),
      ("Lantai 2", "4 orang", ["+1 extra bed = 5 orang", "Empat kasur", "Toilet &amp; kamar mandi"])]
FX = ["Termasuk sarapan", "AC &amp; Wi-Fi", "Teras/balkon pribadi", "Set kopi/teh &amp; pemanas air", "Tirai blackout", "Meja kerja/rias", "Handuk untuk setiap tamu", "Perlengkapan mandi lengkap", "Bantal &amp; selimut tambahan", "Setrika atas permintaan"]
fl = "".join(f'''<div style="flex:1;background:#fff;border-radius:18px;padding:22px 24px;box-shadow:0 8px 22px rgba(90,62,49,.1);text-align:left;border-top:6px solid #C0592C">
  <div style="display:flex;justify-content:space-between;align-items:baseline"><span style="font-family:'Playfair Display',serif;font-size:40px;color:#45301F">{n}</span><span style="font-weight:700;font-size:18px;letter-spacing:.14em;text-transform:uppercase;color:#C0592C">{c}</span></div>
  {"".join(f'<div style="font-size:23px;color:#4A3426;padding:9px 0;border-bottom:1.5px solid rgba(138,95,72,.2)">{x}</div>' for x in items)}</div>''' for n, c, items in FL)
T.append(f'''<div class="t" id="wa-family-10"><div style="position:absolute;inset:32px;border:1.5px solid rgba(138,95,72,.4)"></div>
  <img src="{LOGO}" style="position:absolute;left:50%;transform:translateX(-50%);top:60px;width:240px" alt="">
  <div style="position:absolute;left:80px;right:80px;top:250px;text-align:center">
    <div style="font-weight:700;font-size:20px;letter-spacing:.32em;text-transform:uppercase;color:#7A5039">Satu rumah, dua lantai</div>
    <div class="emb" style="font-family:'Playfair Display',serif;font-size:56px;color:#45301F;margin:6px 0 22px">Family Superior <em style="color:#A0603E">Bungalow</em></div>
    <div style="display:flex;gap:22px">{fl}</div>
    <div class="fx" style="text-align:left;margin-top:22px">{"".join(f"<div>{x}</div>" for x in FX)}</div>
    <div style="margin-top:18px;font-size:24px;color:#4A3426">Kapasitas normal 6 orang · maksimal 8 orang dengan 2 extra bed</div></div></div>''')
(H / "family_wa.html").write_text(f'<!doctype html><html lang="id"><head><meta charset="utf-8">{FONTS}<style>{CSS}</style></head><body>{"".join(T)}</body></html>')
print(len(T))
