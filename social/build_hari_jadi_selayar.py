"""Story Instagram (1080x1920) ucapan Hari Jadi ke-421 Kabupaten Kepulauan Selayar (29 November 2026), gaya SunaRi.
# Foto latar: hasil color grading tema SunaRi (resep social/grade_photos.py, kekuatan 0.5) -> assets/photos/graded/senja__85-siluet-tirai-senja-persegi-lurus.jpg
Run: python3 social/build_hari_jadi_selayar.py && node social/render_hari_jadi_selayar.js -> social/hari-jadi-selayar/story-hari-jadi-421.png"""
import pathlib
H = pathlib.Path(__file__).parent
P = "../assets/photos/"; LOGO_D = "../assets/logo-sunari-color-dark.png"; LOGO = "../assets/logo-sunari-color.png"
FONTS = '<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;1,400;1,500&family=Montserrat:wght@500;600;700&display=swap" rel="stylesheet">'
CSS = """
*{margin:0;padding:0;box-sizing:border-box}body{background:#bbb;font-family:Montserrat,sans-serif}
.s{position:relative;overflow:hidden;width:1080px;height:1920px;margin:30px auto;background:#120c08;color:#FBF4EC}
.bg{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.vt{position:absolute;left:0;right:0;top:0;height:900px;background:linear-gradient(180deg,rgba(40,20,8,.72),rgba(40,20,8,.38) 70%,rgba(40,20,8,0))}
.head{position:absolute;left:70px;right:70px;top:210px;text-align:center;text-shadow:0 3px 18px rgba(40,18,6,.75),0 1px 3px rgba(40,18,6,.6)}
.kick{font-weight:700;font-size:28px;letter-spacing:.34em;text-transform:uppercase;color:#FFF3E2}
.ttl{font-family:'Playfair Display',serif;font-weight:500;font-size:80px;line-height:1.08;color:#FFFFFF}
.big{font-family:'Playfair Display',serif;font-weight:500;font-size:220px;line-height:.92;color:#FFFFFF}
.vb{position:absolute;left:0;right:0;bottom:0;height:820px;background:linear-gradient(0deg,rgba(30,14,6,.9),rgba(30,14,6,.7) 55%,rgba(30,14,6,0))}
.card{position:absolute;left:70px;right:70px;bottom:250px;text-align:center;color:#FFFFFF;text-shadow:0 2px 12px rgba(20,8,2,.7)}
.lbl{font-weight:700;font-size:24px;letter-spacing:.36em;text-transform:uppercase;color:#FDB15D}
.tema{font-family:'Playfair Display',serif;font-weight:500;font-size:50px;line-height:1.26;margin-top:12px}
.sub{font-size:31px;line-height:1.5;color:#FFF3E2;margin-top:24px}
.tag{font-weight:700;font-size:20px;letter-spacing:.14em;color:#FDB15D;margin-top:12px}
"""
T = f'''<div class="s" id="story-hari-jadi-421"><img class="bg" src="{P}graded/senja__85-siluet-tirai-senja-persegi-lurus.jpg" style="object-position:15% 50%" alt="">
  <div class="vt"></div><div class="vb"></div>
  <div class="head">
    <div class="kick">29 November 1605 — 2026</div>
    <div class="ttl" style="margin-top:30px">Selamat Hari Jadi</div>
    <div class="big">ke-421</div>
    <div class="ttl" style="font-size:62px">Kabupaten Kepulauan Selayar</div>
  </div>
  <div class="card">
    <div class="lbl">Tema</div>
    <div class="tema">“Pangan Lokal Mendukung<br>Ketahanan Pangan Nasional”</div>
    <div class="sub">Dari tepi Pantai Sunari, kami turut merayakan 421 tahun Selayar. Semoga laut dan tanahnya terus memberi berkah untuk kita semua.</div>
    <img src="{LOGO_D}" style="width:250px;margin-top:26px;filter:drop-shadow(0 2px 8px rgba(0,0,0,.5))" alt="">
    <div class="tag">#sunarisunsetmoment · #HariJadiSelayar421</div>
  </div></div>'''
(H / "hari_jadi_selayar.html").write_text(f'<!doctype html><html lang="id"><head><meta charset="utf-8">{FONTS}<style>{CSS}</style></head><body>{T}</body></html>')
print("ok")
