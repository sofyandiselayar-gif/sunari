"""Versi Story Instagram (1080x1920) dari carousel feed "Malam di SunaRi" (8 slide): teks sama, foto penuh, zona aman.
Run: python3 social/build_malam_carousel_story.py && node social/render_malam_carousel_story.js -> social/malam-carousel-story/"""
import pathlib
H = pathlib.Path(__file__).parent
LOGO = "../assets/logo-sunari-color.png"; LOGO_D = "../assets/logo-sunari-color-dark.png"; P = "../assets/photos/"; WA = "0821-8903-3044"
FONTS = '<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;1,400;1,500&family=Montserrat:wght@500;600;700&display=swap" rel="stylesheet">'
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
.sub{font-size:36px;line-height:1.45;margin-top:22px;opacity:.95}
"""
SL = [("senja/38-blue-hour-kayak-1815.jpg", "50% 50%", "Langit berganti biru", "Beberapa menit setelah matahari tenggelam, langit perlahan menjadi biru tua."),
      ("malam/02-bangunan-utama-malam.jpg", "50% 50%", "Hangat di antara pohon kelapa", "Bangunan kayu dan jembatan kecil yang menyala setiap malam."),
      ("malam/06-taman-malam-bougainvillea.jpg", "50% 50%", "Taman ikut menyala", "Lampu-lampu kecil di antara bunga dan pohon kelapa."),
      ("malam/07-jalan-setapak-gazebo.jpg", "50% 50%", "Jalan setapak berlampu", "Dari bungalow ke gazebo, ditemani suara ombak."),
      ("resto/03-resto-malam.jpg", "50% 50%", "Makan malam di Bajoy", "Ikan bakar &amp; seafood di bawah lampu gantung, buka sampai 21.00 WITA."),
      ("malam/09-lilin-di-meja.jpg", "50% 50%", "Malam yang pelan", "Tidak ada yang terburu-buru di Selayar.")]
N = 8
T = [f'''<div class="s" id="story-01"><img class="bg" src="{P}malam/05-a-frame-malam.jpg" style="object-position:50% 50%" alt="">
  <div class="vt" style="height:900px;background:linear-gradient(180deg,rgba(14,8,4,.75),rgba(14,8,4,.35) 65%,rgba(14,8,4,0))"></div>
  <div class="tx" style="top:300px;bottom:auto"><div class="kick">Malam di SunaRi</div>
    <div class="ttl" style="font-size:120px;line-height:1.04">Saat senja usai, lampu-lampu <em style="color:#FDB15D">menyala.</em></div></div>
  <div style="position:absolute;left:76px;bottom:300px;font-weight:600;font-size:22px;letter-spacing:.38em;text-transform:uppercase;color:#FBF4EC">Ketuk untuk lanjut &nbsp;→</div>
  <img src="{LOGO_D}" style="position:absolute;right:70px;bottom:270px;width:280px;filter:drop-shadow(0 2px 8px rgba(0,0,0,.5))" alt=""></div>''']
for k, (img, pos, t, sub) in enumerate(SL, 2):
    T.append(f'''<div class="s" id="story-{k:02d}"><img class="bg" src="{P}{img}" style="object-position:{pos}" alt="">
  <div class="vt"></div><div class="vb"></div><img class="lg" src="{LOGO_D}" alt=""><div class="no">{k:02d} — {N:02d}</div>
  <div class="tx"><div class="kick">Malam di SunaRi</div><div class="ttl">{t}</div><div class="sub">{sub}</div></div></div>''')
PTS = ["Bajoy Beach Resto buka sampai 21.00 WITA", "Senja Dinner, pesan H-1", "Taman berlampu di antara pohon kelapa", "Bungalow kayu dengan teras pribadi"]
T.append(f'''<div class="s" id="story-08" style="background:#FBF4EC;color:#45301F"><div style="position:absolute;left:40px;right:40px;top:200px;bottom:200px;border:1.5px solid rgba(138,95,72,.4)"></div>
  <img src="{LOGO}" style="position:absolute;left:50%;transform:translateX(-50%);top:300px;width:400px" alt="">
  <div style="position:absolute;left:100px;right:100px;top:640px;text-align:center">
    <div style="font-weight:600;font-size:24px;letter-spacing:.4em;text-transform:uppercase;color:#7A5039">Yang menantimu malam ini</div>
    <div style="font-family:'Playfair Display',serif;font-size:92px;line-height:1.08;margin-top:16px;text-shadow:0 1.5px 0 #fff">Malam di <em style="color:#A0603E">SunaRi</em></div>
    <div style="margin-top:44px;border-top:1.5px solid rgba(138,95,72,.3);text-align:left">{"".join(f'<div style="padding:24px 0;border-bottom:1.5px solid rgba(138,95,72,.3);font-size:32px"><span style="display:inline-block;width:11px;height:11px;border-radius:50%;background:linear-gradient(90deg,#FDB15D,#FF8A5C);margin-right:18px;vertical-align:middle"></span>{x}</div>' for x in PTS)}</div></div>
  <div style="position:absolute;left:0;right:0;bottom:330px;text-align:center">
    <div style="font-weight:600;font-size:22px;letter-spacing:.36em;text-transform:uppercase;color:#7A5039">Info &amp; reservasi</div>
    <div style="font-family:'Playfair Display',serif;font-size:64px;margin-top:10px"><i style="color:#A0603E">WhatsApp</i> {WA}</div>
    <div style="font-weight:700;font-size:20px;letter-spacing:.2em;color:#C0592C;margin-top:20px">#sunarisunsetmoment</div></div></div>''')
(H / "malam_carousel_story.html").write_text(f'<!doctype html><html lang="id"><head><meta charset="utf-8">{FONTS}<style>{CSS}</style></head><body>{"".join(T)}</body></html>')
print(len(T))
