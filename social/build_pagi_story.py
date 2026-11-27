"""Story Instagram (1080x1920) "Tentang SunaRi: Pagi di SunaRi" (7 frame, morning vibe).
Run: python3 social/build_pagi_story.py && node social/render_pagi_story.js -> social/pagi-story/"""
import pathlib
H = pathlib.Path(__file__).parent
LOGO = "../assets/logo-sunari-color.png"; LOGO_D = "../assets/logo-sunari-color-dark.png"; P = "../assets/photos/"; WA = "0821-8903-3044"
FONTS = '<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;1,400;1,500&family=Montserrat:wght@500;600;700&display=swap" rel="stylesheet">'
CSS = """
*{margin:0;padding:0;box-sizing:border-box}body{background:#bbb;font-family:Montserrat,sans-serif}
.s{position:relative;overflow:hidden;width:1080px;height:1920px;margin:30px auto;background:#FBF4EC;color:#FBF4EC}
.bg{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;filter:brightness(1.06) saturate(1.06) sepia(.12)}
.vt{position:absolute;left:0;right:0;top:0;height:640px;background:linear-gradient(180deg,rgba(90,62,49,.55),rgba(90,62,49,0))}
.vb{position:absolute;left:0;right:0;bottom:0;height:1100px;background:linear-gradient(0deg,rgba(80,52,40,.92),rgba(90,58,42,.72) 45%,rgba(110,72,52,0))}
.glow{position:absolute;left:0;right:0;top:0;height:700px;background:radial-gradient(ellipse at 85% 0%,rgba(253,177,93,.45),rgba(253,177,93,0) 65%)}
.lg{position:absolute;left:76px;top:250px;width:220px;filter:drop-shadow(0 2px 8px rgba(0,0,0,.45))}
.no{position:absolute;right:76px;top:268px;font-weight:600;font-size:20px;letter-spacing:.3em;color:#FBF4EC;opacity:.9}
.tx{position:absolute;left:76px;right:76px;bottom:300px;text-shadow:0 2px 14px rgba(60,35,22,.55)}
.kick{font-weight:600;font-size:22px;letter-spacing:.42em;text-transform:uppercase;color:#FDB15D}
.kick:before{content:"";display:inline-block;width:14px;height:14px;border-radius:50%;background:linear-gradient(90deg,#FDB15D,#FF8A5C);margin-right:18px;vertical-align:middle;position:relative;top:-2px}
.ttl{font-family:'Playfair Display',serif;font-size:92px;line-height:1.06;margin-top:20px}
.sub{font-size:36px;line-height:1.45;margin-top:22px;opacity:.97}
"""
K = "Pagi di SunaRi"
SL = [("pantai/03-pulau-di-seberang.jpg", "50% 50%", "Tempat senja pulang", "Tentang SunaRi", "Resort tepi pantai di Pantai Sunari, pesisir barat Kepulauan Selayar, Sulawesi Selatan."),
      ("pantai/02-perahu-nelayan-biru.jpg", "50% 50%", "Matahari yang menari", "Arti nama", "Sun + Nari: matahari yang menari turun ke laut Selayar. Pagi tenang, sore ditutup senja."),
      ("superior-bungalow/01-eksterior-samping.jpg", "50% 50%", "Bangun di bungalow kayu", "Tempat menginap", "5 tipe bungalow dengan teras pribadi, ber-AC dan Wi-Fi, sudah termasuk sarapan."),
      ("standard-bungalow/01-teras-view-laut.jpg", "50% 50%", "Kopi di teras, laut di depan mata", "Teras pribadi", "Duduk santai sebelum hari dimulai. Pilih pemandangan laut atau taman."),
      ("taman/05-meja-taman-view-laut-gazebo.jpg", "38% 50%", "Sarapan di antara bougenvil", "Bajoy Beach Resto", "Buka 07.00–21.00 WITA. Ikan bakar &amp; seafood, sarapan termasuk untuk tamu menginap.")]
N = 7
T = [f'''<div class="s" id="story-01"><img class="bg" src="{P}pantai/04-kursi-santai-bawah-pohon.jpg" style="object-position:50% 60%" alt="">
  <div class="vt" style="height:1000px;background:linear-gradient(180deg,rgba(80,52,40,.72),rgba(90,62,49,.38) 65%,rgba(90,62,49,0))"></div><div class="glow"></div>
  <div class="tx" style="top:300px;bottom:auto"><div class="kick">Tentang SunaRi</div>
    <div class="ttl" style="font-size:124px;line-height:1.03">Selamat pagi dari <em style="color:#FDB15D">Pantai Sunari.</em></div></div>
  <div style="position:absolute;left:76px;bottom:300px;font-weight:600;font-size:22px;letter-spacing:.38em;text-transform:uppercase;color:#FBF4EC;text-shadow:0 2px 10px rgba(60,35,22,.6)">Ketuk untuk lanjut &nbsp;→</div>
  <img src="{LOGO_D}" style="position:absolute;right:70px;bottom:270px;width:280px;filter:drop-shadow(0 2px 8px rgba(0,0,0,.45))" alt=""></div>''']
for k, (img, pos, t, kick, sub) in enumerate(SL, 2):
    T.append(f'''<div class="s" id="story-{k:02d}"><img class="bg" src="{P}{img}" style="object-position:{pos}" alt="">
  <div class="vt"></div><div class="glow"></div><div class="vb"></div><img class="lg" src="{LOGO_D}" alt=""><div class="no">{k:02d} — {N:02d}</div>
  <div class="tx"><div class="kick">{kick}</div><div class="ttl">{t}</div><div class="sub">{sub}</div></div></div>''')
PTS = ["Bungalow kayu dengan teras pribadi", "Sarapan termasuk, Wi-Fi &amp; AC", "Bajoy Beach Resto, 07.00–21.00 WITA", "Sewa kayak &amp; antar-jemput bandara/pelabuhan"]
T.append(f'''<div class="s" id="story-07" style="color:#45301F"><div style="position:absolute;inset:0;background:linear-gradient(180deg,#FFF1DC,#FBF4EC 55%)"></div>
  <div style="position:absolute;left:40px;right:40px;top:200px;bottom:200px;border:1.5px solid rgba(138,95,72,.4)"></div>
  <img src="{LOGO}" style="position:absolute;left:50%;transform:translateX(-50%);top:300px;width:400px" alt="">
  <div style="position:absolute;left:100px;right:100px;top:640px;text-align:center">
    <div style="font-weight:600;font-size:24px;letter-spacing:.4em;text-transform:uppercase;color:#7A5039">Tentang SunaRi</div>
    <div style="font-family:'Playfair Display',serif;font-size:92px;line-height:1.08;margin-top:16px;text-shadow:0 1.5px 0 #fff">Pagi yang pelan, <em style="color:#A0603E">senja yang dikenang.</em></div>
    <div style="margin-top:44px;border-top:1.5px solid rgba(138,95,72,.3);text-align:left">{"".join(f'<div style="padding:24px 0;border-bottom:1.5px solid rgba(138,95,72,.3);font-size:32px"><span style="display:inline-block;width:11px;height:11px;border-radius:50%;background:linear-gradient(90deg,#FDB15D,#FF8A5C);margin-right:18px;vertical-align:middle"></span>{x}</div>' for x in PTS)}</div></div>
  <div style="position:absolute;left:0;right:0;bottom:330px;text-align:center">
    <div style="font-weight:600;font-size:22px;letter-spacing:.36em;text-transform:uppercase;color:#7A5039">Info &amp; reservasi</div>
    <div style="font-family:'Playfair Display',serif;font-size:64px;margin-top:10px"><i style="color:#A0603E">WhatsApp</i> {WA}</div>
    <div style="font-weight:700;font-size:20px;letter-spacing:.2em;color:#C0592C;margin-top:20px">#SunaRiSelayar</div></div></div>''')
(H / "pagi_story.html").write_text(f'<!doctype html><html lang="id"><head><meta charset="utf-8">{FONTS}<style>{CSS}</style></head><body>{"".join(T)}</body></html>')
print(len(T))
