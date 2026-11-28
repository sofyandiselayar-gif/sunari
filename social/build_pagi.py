"""Story Instagram "Pagi di SunaRi" (5 frame, 1080x1920), 1 frame per hari, diunggah pagi hari.
Run: python3 social/build_pagi.py && node social/render_pagi.js -> social/pagi/"""
import pathlib
H = pathlib.Path(__file__).parent
LOGO_D = "../assets/logo-sunari-color-dark.png"; PH = "../assets/photos/"
FONTS = '<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;1,400;1,500&family=Montserrat:wght@500;600;700&display=swap" rel="stylesheet">'
CSS = """
*{margin:0;padding:0;box-sizing:border-box}body{background:#bbb;font-family:Montserrat,sans-serif}
.s{position:relative;overflow:hidden;width:1080px;height:1920px;margin:30px auto;background:#2a1e18;color:#FBF4EC}
.bg{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.vt{position:absolute;left:0;right:0;top:0;height:760px;background:linear-gradient(180deg,rgba(40,26,20,.85),rgba(40,26,20,.55) 55%,rgba(40,26,20,0))}
.vb{position:absolute;left:0;right:0;bottom:0;height:980px;background:linear-gradient(0deg,rgba(34,22,17,.94),rgba(34,22,17,.7) 55%,rgba(34,22,17,0))}
.lg{position:absolute;left:50%;transform:translateX(-50%);top:236px;width:200px;filter:drop-shadow(0 2px 8px rgba(0,0,0,.55))}
.day{position:absolute;left:0;right:0;top:470px;text-align:center;font-weight:700;font-size:22px;letter-spacing:.34em;text-transform:uppercase;color:#FDB15D;text-shadow:0 2px 12px rgba(0,0,0,.8)}
.dots{display:flex;justify-content:center;gap:12px;margin-top:20px}
.dots i{width:10px;height:10px;border-radius:50%;border:1.5px solid #FDB15D}
.dots i.on{background:#FDB15D}
.tx{position:absolute;left:96px;right:96px;bottom:430px;text-align:center;text-shadow:0 2px 16px rgba(0,0,0,.65)}
.l1{font-family:'Playfair Display',serif;font-weight:400;font-size:68px;line-height:1.18;color:#FBF4EC}
.l2{font-family:'Playfair Display',serif;font-style:italic;font-size:52px;line-height:1.25;color:#FDB15D;margin-top:16px}
.orn{display:flex;align-items:center;justify-content:center;gap:18px;margin-bottom:34px}
.orn i{display:block;width:90px;height:1px;background:linear-gradient(90deg,rgba(253,177,93,0),#FDB15D)}
.orn i:last-child{transform:scaleX(-1)}
.orn b{width:7px;height:7px;transform:rotate(45deg);border:1px solid #FDB15D}
.nx{position:absolute;left:0;right:0;bottom:350px;text-align:center;font-weight:600;font-size:20px;letter-spacing:.3em;text-transform:uppercase;color:rgba(251,244,236,.85);text-shadow:0 2px 10px rgba(0,0,0,.6)}
"""
# (id, foto, posisi, zoom (sembunyikan watermark), baris1, baris2, teaser besok)
F = [("nelayan", "graded/pantai__01-nelayan-pagi.jpg", "50% 40%", 1.12,
      "07.34, nelayan sudah melaut.", "Pagi di Selayar selalu dimulai pelan.", "Besok pagi: dari teras"),
     ("teras", "taman/03-taman-dari-teras-bungalow.jpg", "38% 50%", 1.0,
      "Buka pintu bungalow,", "dan taman menyapa selamat pagi.", "Besok pagi: jalan setapak"),
     ("kamboja", "taman/06-jalan-setapak-kamboja.jpg", "42% 50%", 1.0,
      "Bunga kamboja jatuh pelan,", "seolah tahu kamu sedang liburan.", "Besok pagi: sarapan"),
     ("sarapan", "taman/12-meja-taman-portrait.jpg", "50% 60%", 1.0,
      "Sarapan sudah termasuk.", "Tinggal pilih meja yang paling teduh.", "Besok pagi: giliranmu"),
     ("ajakan", "taman/05-meja-taman-view-laut-gazebo.jpg", "40% 50%", 1.0,
      "Pagi seperti ini", "bisa jadi milikmu minggu depan.", "")]
T = []
for k, (hid, img, pos, z, a, b, nxt) in enumerate(F, 1):
    dots = "".join(f'<i class="{"on" if j == k else ""}"></i>' for j in range(1, 6))
    cta = ""
    if hid == "ajakan":
        cta = '''<div style="margin-top:44px;font-weight:600;font-size:20px;letter-spacing:.36em;text-transform:uppercase;color:#FDB15D">Reservasi via WhatsApp</div>
    <div style="font-family:'Playfair Display',serif;font-size:50px;margin-top:6px">0821-8903-3044</div>
    <div style="margin-top:14px;font-weight:700;font-size:19px;letter-spacing:.16em;color:#FF8A5C">#sunarisunsetmoment</div>'''
    nx = f'<div class="nx">{nxt} ›</div>' if nxt else ""
    zs = f";transform:scale({z});transform-origin:50% 0" if z != 1 else ""
    txs = ' style="top:640px;bottom:auto"' if hid == "nelayan" else ""
    vts = ' style="height:1150px;background:linear-gradient(180deg,rgba(40,26,20,.85),rgba(40,26,20,.7) 60%,rgba(40,26,20,0))"' if hid == "nelayan" else ""
    T.append(f'''<div class="s" id="pagi-{k:02d}-{hid}"><img class="bg" src="{PH}{img}" style="object-position:{pos}{zs}" alt="">
  <div class="vt"{vts}></div><div class="vb"></div><img class="lg" src="{LOGO_D}" alt="">
  <div class="day">Pagi di SunaRi · {k}/5<div class="dots">{dots}</div></div>
  <div class="tx"{txs}><div class="orn"><i></i><b></b><i></i></div><div class="l1">{a}</div><div class="l2">{b}</div>{cta}</div>{nx}</div>''')
(H / "pagi.html").write_text(f'<!doctype html><html lang="id"><head><meta charset="utf-8">{FONTS}<style>{CSS}</style></head><body>{"".join(T)}</body></html>')
print(len(T))
