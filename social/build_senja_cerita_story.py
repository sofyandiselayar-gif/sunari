"""Versi Story Instagram (1080x1920) dari carousel "Senja Hari Ini": 14 frame, foto penuh, zona aman atas/bawah ±250 px.
Run: python3 social/build_senja_cerita_story.py && node social/render_senja_cerita_story.js -> social/senja-cerita-story/"""
import pathlib, re
H = pathlib.Path(__file__).parent
src = (H / "build_senja_cerita.py").read_text()
ns = {}; exec(src[src.index("LOGO ="):src.index("N = len(SL)")], ns)   # ambil LOGO, P, WA, FONTS, SL dari versi feed
LOGO, LOGO_D, P, WA, FONTS, SL = ns["LOGO"], ns["LOGO_D"], ns["P"], ns["WA"], ns["FONTS"], ns["SL"]
SL = [(i, p, k, t, "Kayak berjajar di pasir, menunggu besok sore." if i.startswith("73") else s) for i, p, k, t, s in SL]
# posisi crop horizontal khusus 9:16 (foto aslinya persegi)
XPOS = {"79": "60%", "80": "28%", "81": "55%", "82": "58%", "71": "30%", "83": "74%", "76": "50%", "77": "42%",
        "72": "48%", "70": "48%", "73": "100%", "75": "55%"}
N = len(SL) + 2
TOP = {"70", "73"}  # subjek di bawah: teks dipindah ke atas
CSS = """
*{margin:0;padding:0;box-sizing:border-box}body{background:#bbb;font-family:Montserrat,sans-serif}
.s{position:relative;overflow:hidden;width:1080px;height:1920px;margin:30px auto;background:#1d140e}
.bg{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.vt{position:absolute;left:0;right:0;top:0;height:560px;background:linear-gradient(180deg,rgba(20,12,6,.55),rgba(20,12,6,0))}
.vb{position:absolute;left:0;right:0;bottom:0;height:980px;background:linear-gradient(0deg,rgba(20,12,6,.82) 0%,rgba(20,12,6,.55) 45%,rgba(20,12,6,0))}
.lg{position:absolute;left:72px;top:250px;width:230px;filter:drop-shadow(0 2px 8px rgba(0,0,0,.5))}
.no{position:absolute;right:72px;top:268px;font-weight:700;font-size:22px;letter-spacing:.24em;color:#FBF4EC;background:rgba(15,8,4,.4);border:1px solid rgba(251,244,236,.35);padding:10px 18px;border-radius:999px}
.tx{position:absolute;left:76px;right:76px;bottom:300px;color:#FBF4EC;text-shadow:0 2px 14px rgba(0,0,0,.55)}
.kick{font-weight:700;font-size:24px;letter-spacing:.34em;text-transform:uppercase;color:#FDB15D}
.ttl{font-family:'Playfair Display',serif;font-size:96px;line-height:1.06;margin-top:18px}
.ttl em{font-style:italic;color:#FDB15D}
.sub{font-size:36px;line-height:1.45;margin-top:22px;opacity:.95}
.tag{position:absolute;left:76px;bottom:250px;font-weight:700;font-size:20px;letter-spacing:.16em;color:#FBF4EC;opacity:.85}
"""
T = [f'''<div class="s" id="story-01"><img class="bg" src="{P}74-matahari-menyentuh-laut-kapal.jpg" style="object-position:57% 50%" alt="">
  <div class="vt"></div><div class="vb"></div><img class="lg" src="{LOGO_D}" alt="">
  <div class="tx" style="top:420px;bottom:auto"><div class="kick" style="color:#FBF4EC">Senja hari ini · Pantai Sunari</div>
    <div class="ttl" style="font-size:116px">Sore ini terlalu <em>indah</em> untuk dilewatkan.</div></div>
  <div class="tx"><div style="font-family:'Playfair Display',serif;font-size:170px;line-height:1">17.57<span style="font-family:Montserrat;font-weight:700;font-size:30px;letter-spacing:.3em;margin-left:18px">WITA</span></div>
    <div class="kick" style="color:#FBF4EC;margin-top:26px">Ketuk untuk ceritanya &nbsp;→</div></div></div>''']
for k, (img, pos, kick, t, sub) in enumerate(SL, 2):
    x = XPOS[img[:2]]
    T.append(f'''<div class="s" id="story-{k:02d}"><img class="bg" src="{P}{img}" style="object-position:{x} 50%" alt="">
  {'<div class="vt" style="height:1000px;background:linear-gradient(180deg,rgba(20,12,6,.75),rgba(20,12,6,.45) 50%,rgba(20,12,6,0))"></div>' if img[:2] in TOP else '<div class="vt"></div><div class="vb"></div>'}<img class="lg" src="{LOGO_D}" alt=""><div class="no">{k:02d} / {N:02d}</div>
  <div class="tx"{' style="top:400px;bottom:auto"' if img[:2] in TOP else ''}><div class="kick">{kick}</div><div class="ttl">{t}</div><div class="sub">{sub}</div></div></div>''')
TIPS = ["Datang 30 menit sebelum matahari terbenam", "Akhir Nov–Des: senja sekitar 18.00 WITA", "Ayunan raksasa gratis, kayak bisa disewa", "Ikuti jam senja harian di story kami"]
T.append(f'''<div class="s" id="story-{N:02d}" style="background:#FBF4EC"><div style="position:absolute;left:40px;right:40px;top:200px;bottom:200px;border:1.5px solid rgba(138,95,72,.4)"></div>
  <img src="{LOGO}" style="position:absolute;left:50%;transform:translateX(-50%);top:300px;width:400px" alt="">
  <div style="position:absolute;left:100px;right:100px;top:640px;text-align:center;color:#45301F">
    <div style="font-weight:700;font-size:24px;letter-spacing:.32em;text-transform:uppercase;color:#7A5039">Sampai jumpa besok sore</div>
    <div style="font-family:'Playfair Display',serif;font-size:96px;line-height:1.1;margin-top:16px;text-shadow:0 1.5px 0 #fff">Senja <em style="color:#A0603E">berikutnya</em></div>
    <div style="margin-top:44px;border-top:1.5px solid rgba(138,95,72,.3)">{"".join(f'<div style="padding:24px 0;border-bottom:1.5px solid rgba(138,95,72,.3);font-size:32px">{x}</div>' for x in TIPS)}</div></div>
  <div style="position:absolute;left:0;right:0;bottom:330px;text-align:center">
    <div style="font-weight:700;font-size:22px;letter-spacing:.32em;text-transform:uppercase;color:#7A5039">Info &amp; reservasi</div>
    <div style="font-family:'Playfair Display',serif;font-size:66px;color:#45301F;margin-top:10px"><i style="color:#A0603E">WhatsApp</i> {WA}</div>
    <div style="font-weight:700;font-size:20px;letter-spacing:.2em;color:#C0592C;margin-top:20px">#sunarisunsetmoment</div></div></div>''')
(H / "senja_cerita_story.html").write_text(f'<!doctype html><html lang="id"><head><meta charset="utf-8">{FONTS}<style>{CSS}</style></head><body>{"".join(T)}</body></html>')
print(len(T))
