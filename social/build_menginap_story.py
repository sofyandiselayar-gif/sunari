"""Story Instagram (1080x1920) dari feed "Lebih dari Menginap" 10 slide: teks & foto sama dengan feed (dibaca dari build_kit.py), foto penuh, zona aman.
Run: python3 social/build_menginap_story.py && node social/render_menginap_story.js -> social/menginap-story/"""
import pathlib, re, ast
H = pathlib.Path(__file__).parent
src = (H / "build_kit.py").read_text()
blk = src[src.index('("p01", "Lebih dari Menginap"'):src.index(' ("p02",')].strip().rstrip(',')
_, NAME, _, SL, (ENDT, ENDL) = ast.literal_eval(blk)
P = "../assets/photos/"; WA = "0821-8903-3044"; N = 10
LOGO = "../assets/logo-sunari-color.png"; LOGO_D = "../assets/logo-sunari-color-dark.png"
FONTS = '<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;1,400;1,500&family=Montserrat:wght@500;600;700&display=swap" rel="stylesheet">'
CSS = """
*{margin:0;padding:0;box-sizing:border-box}body{background:#bbb;font-family:Montserrat,sans-serif}
.s{position:relative;overflow:hidden;width:1080px;height:1920px;margin:30px auto;background:#120c08;color:#FBF4EC}
.bg{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.vt{position:absolute;left:0;right:0;top:0;height:620px;background:linear-gradient(180deg,rgba(14,8,4,.7),rgba(14,8,4,0))}
.vb{position:absolute;left:0;right:0;bottom:0;height:1000px;background:linear-gradient(0deg,rgba(14,8,4,.9),rgba(14,8,4,.6) 55%,rgba(14,8,4,0))}
.lg{position:absolute;left:76px;top:250px;width:220px;filter:drop-shadow(0 2px 8px rgba(0,0,0,.55))}
.no{position:absolute;right:76px;top:268px;font-weight:600;font-size:20px;letter-spacing:.3em;opacity:.85}
.tx{position:absolute;left:76px;right:76px;bottom:300px;text-shadow:0 2px 14px rgba(0,0,0,.55)}
.kick{font-weight:600;font-size:22px;letter-spacing:.42em;text-transform:uppercase;color:#FDB15D}
.ttl{font-family:'Playfair Display',serif;font-size:88px;line-height:1.06;margin-top:20px}
.sub{font-size:36px;line-height:1.45;margin-top:22px;opacity:.95}
"""
POS = {}   # crop khusus 9:16 bila perlu (nomor frame -> object-position)
EXTRA = {2: "height:2200px"}
TOPTEXT = {2}   # objek foto di bawah -> teks di atas   # foto nelayan: diperbesar agar watermark di bawah terpotong
T = [f'''<div class="s" id="story-01"><img class="bg" src="{P}senja/08-meja-di-bawah-pohon.jpg" style="object-position:50% 60%" alt="">
  <div class="vt" style="height:900px;background:linear-gradient(180deg,rgba(14,8,4,.75),rgba(14,8,4,.35) 65%,rgba(14,8,4,0))"></div>
  <div class="vb" style="height:620px;background:linear-gradient(0deg,rgba(14,8,4,.6),rgba(14,8,4,0))"></div>
  <div class="tx" style="top:300px;bottom:auto"><div class="ttl" style="font-size:136px;line-height:1.04;margin-top:0">Lebih dari<br>Menginap.<br><i>Sebuah Rasa.</i></div></div>
  <div style="position:absolute;left:76px;bottom:300px;font-weight:600;font-size:22px;letter-spacing:.38em;text-transform:uppercase;text-shadow:0 2px 10px rgba(0,0,0,.6)">Ketuk untuk lanjut &nbsp;→</div>
  <img src="{LOGO_D}" style="position:absolute;right:70px;bottom:270px;width:280px;filter:drop-shadow(0 2px 8px rgba(0,0,0,.5))" alt=""></div>''']
for k, (img, pos, t, sub) in enumerate(SL, 2):
    T.append(f'''<div class="s" id="story-{k:02d}"><img class="bg" src="{P}{img}" style="object-position:{POS.get(k, pos)};{EXTRA.get(k, '')}" alt="">
  {'<div class="vt" style="height:1150px;background:linear-gradient(180deg,rgba(14,8,4,.8),rgba(14,8,4,.5) 60%,rgba(14,8,4,0))"></div>' if k in TOPTEXT else '<div class="vt"></div><div class="vb"></div>'}<img class="lg" src="{LOGO_D}" alt=""><div class="no">{k:02d} — {N:02d}</div>
  <div class="tx"{' style="top:420px;bottom:auto"' if k in TOPTEXT else ''}><div class="kick">{NAME}</div><div class="ttl">{t}</div><div class="sub">{sub}</div></div></div>''')
rows = "".join(f'<div style="padding:26px 0;border-bottom:1.5px solid rgba(138,95,72,.3);font-size:34px">{x}</div>' for x in ENDL)
a, b = ENDT.split(" ", 1)
T.append(f'''<div class="s" id="story-10" style="background:#FBF4EC;color:#45301F"><div style="position:absolute;left:40px;right:40px;top:200px;bottom:200px;border:1.5px solid rgba(138,95,72,.4)"></div>
  <img src="{LOGO}" style="position:absolute;left:50%;transform:translateX(-50%);top:300px;width:380px" alt="">
  <div style="position:absolute;left:110px;right:110px;top:640px;text-align:center">
    <div style="font-weight:600;font-size:24px;letter-spacing:.4em;text-transform:uppercase;color:#7A5039">{NAME}</div>
    <div style="font-family:'Playfair Display',serif;font-size:92px;line-height:1.08;margin-top:16px;text-shadow:0 1.5px 0 #fff">{a} <em style="color:#A0603E">{b}</em></div>
    <div style="margin-top:44px;border-top:1.5px solid rgba(138,95,72,.3)">{rows}</div></div>
  <div style="position:absolute;left:0;right:0;bottom:330px;text-align:center">
    <div style="font-weight:600;font-size:22px;letter-spacing:.36em;text-transform:uppercase;color:#7A5039">Info &amp; reservasi</div>
    <div style="font-family:'Playfair Display',serif;font-size:64px;margin-top:10px"><i style="color:#A0603E">WhatsApp</i> {WA}</div>
    <div style="font-weight:700;font-size:20px;letter-spacing:.2em;color:#C0592C;margin-top:20px">#sunarisunsetmoment</div></div></div>''')
(H / "menginap_story.html").write_text(f'<!doctype html><html lang="id"><head><meta charset="utf-8">{FONTS}<style>{CSS}</style></head><body>{"".join(T)}</body></html>')
print(len(T))
