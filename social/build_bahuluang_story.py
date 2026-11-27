"""Versi Story Instagram (1080x1920) dari feed "Dari SunaRi ke Bahuluang" (10 frame): teks sama, foto penuh, zona aman.
Run: python3 social/build_bahuluang_story.py && node social/render_bahuluang_story.js -> social/bahuluang-story/"""
import pathlib
H = pathlib.Path(__file__).parent
ns = {"__file__": str(H / "build_bahuluang_feed.py")}
exec((H / "build_bahuluang_feed.py").read_text().split("(H / \"bahuluang_feed.html\")")[0], ns)
SL, TL, WA, LOGO, LOGO_D, FONTS, KICK, P = (ns[k] for k in ["SL", "TL", "WA", "LOGO", "LOGO_D", "FONTS", "KICK", "P"])
N = 10
CSS = """
*{margin:0;padding:0;box-sizing:border-box}body{background:#bbb;font-family:Montserrat,sans-serif}
.s{position:relative;overflow:hidden;width:1080px;height:1920px;margin:30px auto;background:#120c08;color:#FBF4EC}
.bg{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.vt{position:absolute;left:0;right:0;top:0;height:620px;background:linear-gradient(180deg,rgba(14,8,4,.7),rgba(14,8,4,0))}
.vb{position:absolute;left:0;right:0;bottom:0;height:980px;background:linear-gradient(0deg,rgba(14,8,4,.9),rgba(14,8,4,.6) 55%,rgba(14,8,4,0))}
.lg{position:absolute;left:76px;top:250px;width:220px;filter:drop-shadow(0 2px 8px rgba(0,0,0,.55))}
.no{position:absolute;right:76px;top:268px;font-weight:600;font-size:20px;letter-spacing:.3em;opacity:.85}
.tx{position:absolute;left:76px;right:76px;bottom:300px;text-shadow:0 2px 14px rgba(0,0,0,.55)}
.kick{font-weight:600;font-size:22px;letter-spacing:.42em;text-transform:uppercase;color:#FDB15D}
.chip{display:inline-block;margin-left:14px;padding:6px 14px;border-radius:30px;background:linear-gradient(90deg,#FDB15D,#FF8A5C);color:#fff;font-size:18px;letter-spacing:.14em;text-shadow:none;vertical-align:2px}
.ttl{font-family:'Playfair Display',serif;font-size:92px;line-height:1.06;margin-top:20px}
.ttl em{font-style:italic;color:#FDB15D}
.sub{font-size:36px;line-height:1.45;margin-top:22px;opacity:.95}
"""
POS = {1: "62% 50%", 2: "40% 50%", 3: "50% 50%", 4: "50% 50%", 5: "48% 50%", 6: "40% 50%", 7: "50% 50%", 8: "48% 50%", 9: "45% 50%"}
T = []
_, _, t, sub, _ = SL[0]
T.append(f'''<div class="s" id="story-01"><img class="bg" src="{P}bahuluang/13-berdiri-di-air-dangkal.jpg" style="object-position:50% 50%" alt="">
  <div class="vb" style="height:700px;background:linear-gradient(0deg,rgba(14,8,4,.65),rgba(14,8,4,0))"></div>
  <div class="vt" style="height:900px;background:linear-gradient(180deg,rgba(14,8,4,.75),rgba(14,8,4,.35) 65%,rgba(14,8,4,0))"></div>
  <div class="tx" style="top:300px;bottom:auto"><div class="kick">{KICK}</div>
    <div class="ttl" style="font-size:130px;line-height:1.04">{t}</div>
    <div style="font-family:'Playfair Display',serif;font-style:italic;font-size:50px;line-height:1.3;margin-top:26px">{sub}</div></div>
  <div style="position:absolute;left:76px;bottom:300px;font-weight:600;font-size:22px;letter-spacing:.38em;text-transform:uppercase;text-shadow:0 2px 10px rgba(0,0,0,.6)">Ketuk untuk lanjut &nbsp;→</div>
  <img src="{LOGO_D}" style="position:absolute;right:70px;bottom:270px;width:280px;filter:drop-shadow(0 2px 8px rgba(0,0,0,.5))" alt=""></div>''')
for k, (img, _, t, sub, jam) in enumerate(SL[1:], 2):
    T.append(f'''<div class="s" id="story-{k:02d}"><img class="bg" src="{P}{img}" style="object-position:{POS[k]}" alt="">
  <div class="vt"></div><div class="vb"></div><img class="lg" src="{LOGO_D}" alt=""><div class="no">{k:02d} — {N:02d}</div>
  <div class="tx"><div class="kick">{KICK}{f'<span class="chip">± {jam}</span>' if jam else ""}</div><div class="ttl">{t}</div><div class="sub">{sub}</div></div></div>''')
rows = "".join(f'<div style="display:flex;gap:28px;padding:22px 0;border-bottom:1.5px solid rgba(138,95,72,.3);font-size:31px"><b style="flex:0 0 120px;color:#C0592C">{a}</b>{b}</div>' for a, b in TL)
T.append(f'''<div class="s" id="story-10" style="background:#FBF4EC;color:#45301F"><div style="position:absolute;left:40px;right:40px;top:200px;bottom:200px;border:1.5px solid rgba(138,95,72,.4)"></div>
  <img src="{LOGO}" style="position:absolute;left:50%;transform:translateX(-50%);top:260px;width:340px" alt="">
  <div style="position:absolute;left:100px;right:100px;top:530px;text-align:center">
    <div style="font-weight:600;font-size:24px;letter-spacing:.4em;text-transform:uppercase;color:#7A5039">Simpan alurnya</div>
    <div style="font-family:'Playfair Display',serif;font-size:84px;line-height:1.08;margin-top:14px;text-shadow:0 1.5px 0 #fff">Satu hari, <em style="color:#A0603E">satu pulau</em></div>
    <div style="margin-top:34px;border-top:1.5px solid rgba(138,95,72,.3);text-align:left">{rows}</div>
    <div style="font-family:'Playfair Display',serif;font-style:italic;font-size:34px;color:#7A5039;margin-top:30px">Ingin ke Bahuluang saat menginap?<br>Biar kami bantu atur.</div></div>
  <div style="position:absolute;left:0;right:0;bottom:290px;text-align:center">
    <div style="font-weight:600;font-size:22px;letter-spacing:.3em;text-transform:uppercase;color:#7A5039">Info &amp; reservasi</div>
    <div style="font-family:'Playfair Display',serif;font-size:60px;margin-top:10px"><i style="color:#A0603E">WhatsApp</i> {WA}</div>
    <div style="font-weight:700;font-size:20px;letter-spacing:.2em;color:#C0592C;margin-top:16px">#sunarisunsetmoment</div></div></div>''')
(H / "bahuluang_story.html").write_text(f'<!doctype html><html lang="id"><head><meta charset="utf-8">{FONTS}<style>{CSS}</style></head><body>{"".join(T)}</body></html>')
print(len(T))
