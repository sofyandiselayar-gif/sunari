"""Versi Story Instagram (1080x1920) dari carousel feed VIP Superior Bungalow (10 slide): teks sama, foto penuh, zona aman.
Run: python3 social/build_vipsuperior_story.py && node social/render_vipsuperior_story.js -> social/vip-superior-story/"""
import pathlib, re
H = pathlib.Path(__file__).parent
src = (H / "build_vipsuperior.py").read_text()
# ambil konten (SL, FX, WA) dari build feed agar teks selalu sama
ns = {"__file__": str(H / "build_vipsuperior.py")}
exec(src.split("T = []")[0], ns)
SL, FX, WA, LOGO, LOGO_D, KICK = ns["SL"], None, ns["WA"], ns["LOGO"], ns["LOGO_D"], ns["KICK"]
FX = ["King bed", "Termasuk sarapan", "AC &amp; Wi-Fi", "TV", "Mini bar/kulkas", "Set kopi/teh", "Bathtub", "Air panas &amp; dingin", "Rain shower", "Tirai blackout", "Meja kerja/rias", "Teras kayu pribadi"]
P = "../assets/photos/vip-superior-bungalow/"; N = 10
FONTS = ns["FONTS"]
CSS = """
*{margin:0;padding:0;box-sizing:border-box}body{background:#bbb;font-family:Montserrat,sans-serif}
.s{position:relative;overflow:hidden;width:1080px;height:1920px;margin:30px auto;background:#120c08;color:#FBF4EC}
.bg{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.vt{position:absolute;left:0;right:0;top:0;height:620px;background:linear-gradient(180deg,rgba(14,8,4,.7),rgba(14,8,4,0))}
.vb{position:absolute;left:0;right:0;bottom:0;height:960px;background:linear-gradient(0deg,rgba(14,8,4,.9),rgba(14,8,4,.6) 55%,rgba(14,8,4,0))}
.lg{position:absolute;left:76px;top:250px;width:220px;filter:drop-shadow(0 2px 8px rgba(0,0,0,.55))}
.no{position:absolute;right:76px;top:268px;font-weight:600;font-size:20px;letter-spacing:.3em;color:#FBF4EC;opacity:.85}
.tx{position:absolute;left:76px;right:76px;bottom:300px;text-shadow:0 2px 14px rgba(0,0,0,.55)}
.kick{font-weight:600;font-size:22px;letter-spacing:.42em;text-transform:uppercase;color:#FDB15D}
.ttl{font-family:'Playfair Display',serif;font-size:92px;line-height:1.06;margin-top:20px}
.ttl em{font-style:italic;color:#FDB15D}
.sub{font-size:36px;line-height:1.45;margin-top:22px;opacity:.95}
"""
T = []
img, pos, t, sub, kick = SL[0]
T.append(f'''<div class="s" id="story-01"><img class="bg" src="{P}{img}" style="object-position:{pos}" alt="">
  <div class="vt" style="height:900px;background:linear-gradient(180deg,rgba(14,8,4,.75),rgba(14,8,4,.35) 65%,rgba(14,8,4,0))"></div>
  <div class="tx" style="top:300px;bottom:auto"><div class="kick">{kick}</div>
    <div class="ttl" style="font-size:130px;line-height:1.04">{t}</div>
    <div style="font-family:'Playfair Display',serif;font-style:italic;font-size:52px;margin-top:26px">{sub}</div></div>
  <div style="position:absolute;left:76px;bottom:300px;font-weight:600;font-size:22px;letter-spacing:.38em;text-transform:uppercase">Ketuk untuk lanjut &nbsp;→</div>
  <img src="{LOGO_D}" style="position:absolute;right:70px;bottom:270px;width:280px;filter:drop-shadow(0 2px 8px rgba(0,0,0,.5))" alt=""></div>''')
for k, (img, pos, t, sub, kick) in enumerate(SL[1:], 2):
    T.append(f'''<div class="s" id="story-{k:02d}"><img class="bg" src="{P}{img}" style="object-position:{pos}" alt="">
  <div class="vt"></div><div class="vb"></div><img class="lg" src="{LOGO_D}" alt=""><div class="no">{k:02d} — {N:02d}</div>
  <div class="tx"><div class="kick">{kick}</div><div class="ttl">{t}</div><div class="sub">{sub}</div></div></div>''')
rows = "".join(f'<div style="padding:22px 0;border-bottom:1.5px solid rgba(138,95,72,.3);font-size:32px"><span style="display:inline-block;width:11px;height:11px;border-radius:50%;background:linear-gradient(90deg,#FDB15D,#FF8A5C);margin-right:18px;vertical-align:middle"></span>{x}</div>' for x in FX)
T.append(f'''<div class="s" id="story-10" style="background:#FBF4EC;color:#45301F"><div style="position:absolute;left:40px;right:40px;top:200px;bottom:200px;border:1.5px solid rgba(138,95,72,.4)"></div>
  <img src="{LOGO}" style="position:absolute;left:50%;transform:translateX(-50%);top:270px;width:380px" alt="">
  <div style="position:absolute;left:100px;right:100px;top:560px;text-align:center">
    <div style="font-weight:600;font-size:24px;letter-spacing:.4em;text-transform:uppercase;color:#7A5039">Fasilitas kamar</div>
    <div style="font-family:'Playfair Display',serif;font-size:84px;line-height:1.08;margin-top:16px;text-shadow:0 1.5px 0 #fff">VIP Superior <em style="color:#A0603E">Bungalow</em></div>
    <div style="margin-top:36px;border-top:1.5px solid rgba(138,95,72,.3);text-align:left;display:grid;grid-template-columns:1fr 1fr;column-gap:40px">{rows}</div></div>
  <div style="position:absolute;left:0;right:0;bottom:330px;text-align:center">
    <div style="font-weight:600;font-size:22px;letter-spacing:.36em;text-transform:uppercase;color:#7A5039">Info &amp; reservasi</div>
    <div style="font-family:'Playfair Display',serif;font-size:60px;margin-top:10px"><i style="color:#A0603E">WhatsApp</i> {WA}</div>
    <div style="font-weight:700;font-size:20px;letter-spacing:.2em;color:#C0592C;margin-top:20px">#sunarisunsetmoment</div></div></div>''')
(H / "vipsuperior_story.html").write_text(f'<!doctype html><html lang="id"><head><meta charset="utf-8">{FONTS}<style>{CSS}</style></head><body>{"".join(T)}</body></html>')
print(len(T))
