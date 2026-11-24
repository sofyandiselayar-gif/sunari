"""Story Instagram "Malam di SunaRi" (8 frame, 1080x1920), cerita suasana malam yang tenang.
Run: python3 social/build_malam_story.py && node social/render_malam_story.js -> social/malam-story/"""
import pathlib
H = pathlib.Path(__file__).parent
LOGO_D = "../assets/logo-sunari-color-dark.png"; P = "../assets/photos/graded/malam__"
FONTS = '<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;1,400;1,500&family=Montserrat:wght@500;600;700&display=swap" rel="stylesheet">'
CSS = """
*{margin:0;padding:0;box-sizing:border-box}body{background:#bbb;font-family:Montserrat,sans-serif}
.s{position:relative;overflow:hidden;width:1080px;height:1920px;margin:30px auto;background:#0b0d14;color:#FBF4EC}
.bg{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.vt{position:absolute;left:0;right:0;top:0;height:560px;background:linear-gradient(180deg,rgba(6,8,14,.65),rgba(6,8,14,0))}
.vb{position:absolute;left:0;right:0;bottom:0;height:900px;background:linear-gradient(0deg,rgba(6,8,14,.88),rgba(6,8,14,.55) 55%,rgba(6,8,14,0))}
.lg{position:absolute;left:50%;transform:translateX(-50%);top:236px;width:200px;filter:drop-shadow(0 2px 8px rgba(0,0,0,.6))}
.tx{position:absolute;left:96px;right:96px;bottom:330px;text-align:center;text-shadow:0 2px 16px rgba(0,0,0,.65)}
.l1{font-family:'Playfair Display',serif;font-weight:400;font-size:62px;line-height:1.2;color:#FBF4EC}
.l2{font-family:'Playfair Display',serif;font-style:italic;font-size:52px;line-height:1.25;color:#FDB15D;margin-top:14px}
.orn{display:flex;align-items:center;justify-content:center;gap:18px;margin-bottom:34px}
.orn i{display:block;width:90px;height:1px;background:linear-gradient(90deg,rgba(253,177,93,0),#FDB15D)}
.orn i:last-child{transform:scaleX(-1)}
.orn b{width:7px;height:7px;transform:rotate(45deg);border:1px solid #FDB15D}
"""
# (foto, posisi, baris1, baris2, baris1 miring?)
F = [("23-jalan-setapak-taman-senja.jpg", "50% 50%", "Ketika senja pamit,", "SunaRi mulai berbisik pelan.", True),
     ("20-gazebo-berlampu-kelapa.jpg", "34% 50%", "Satu per satu lampu menyala,", "seperti bintang yang turun lebih dulu.", False),
     ("22-jalan-setapak-ke-pantai.jpg", "42% 50%", "Langkah jadi lebih pelan.", "Yang terdengar hanya ombak.", False),
     ("15-teras-view-gazebo-berlampu.jpg", "30% 50%", "Dari teras, cahaya di tepi pantai", "terasa begitu dekat.", False),
     ("14-teras-kayu-sofa.jpg", "52% 50%", "Tidak ada yang perlu dikejar malam ini.", "Cukup duduk, dan bernapas.", False),
     ("18-kelapa-dan-bintang.jpg", "40% 50%", "Di Selayar, langitnya masih", "mau menunjukkan bintang.", False),
     ("24-family-superior-bulan.jpg", "56% 50%", "Lalu bulan naik,", "menjaga rumah-rumah kayu yang tertidur.", False)]
T = []
for k, (img, pos, a, b, swap) in enumerate(F, 1):
    l1 = f'<div class="l2" style="margin:0 0 10px">{a}</div><div class="l1">{b}</div>' if swap else f'<div class="l1">{a}</div><div class="l2">{b}</div>'
    T.append(f'''<div class="s" id="malam-{k:02d}"><img class="bg" src="{P}{img}" style="object-position:{pos}" alt="">
  <div class="vt"></div><div class="vb"></div><img class="lg" src="{LOGO_D}" alt="">
  <div class="tx"><div class="orn"><i></i><b></b><i></i></div>{l1}</div></div>''')
T.append(f'''<div class="s" id="malam-08"><img class="bg" src="{P}19-taman-bulan-jembatan.jpg" style="object-position:55% 50%" alt="">
  <div class="vt"></div><div class="vb" style="height:1000px"></div><img class="lg" src="{LOGO_D}" alt="">
  <div class="tx" style="bottom:300px"><div class="orn"><i></i><b></b><i></i></div>
    <div class="l1" style="font-size:70px">Selamat malam dari SunaRi. 🌙</div>
    <div class="l2">Besok sore, senja menunggumu lagi.</div>
    <div style="margin-top:40px;font-weight:600;font-size:20px;letter-spacing:.36em;text-transform:uppercase;color:#FDB15D">WhatsApp</div>
    <div style="font-family:'Playfair Display',serif;font-size:48px;margin-top:4px">0821-8903-3044</div>
    <div style="margin-top:14px;font-weight:700;font-size:19px;letter-spacing:.16em;color:#FF8A5C">#sunarisunsetmoment</div></div></div>''')
(H / "malam_story.html").write_text(f'<!doctype html><html lang="id"><head><meta charset="utf-8">{FONTS}<style>{CSS}</style></head><body>{"".join(T)}</body></html>')
print(len(T))
