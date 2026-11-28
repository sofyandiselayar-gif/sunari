"""Satu frame story "Menari di SunaRi" versi tamu: seluruh cerita dalam 1 kolase (1080x1920, render HD 2x = 2160x3840).
Tanpa logo SunaRi & nomor WhatsApp.
Run: python3 social/grade_menari.py && python3 social/build_menari_satu.py && node social/render_menari_satu.js -> social/menari-satu-frame.png"""
import pathlib
H = pathlib.Path(__file__).parent
P = "../assets/photos/graded/menari__"
FONTS = '<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;1,400;1,500&family=Montserrat:wght@500;600;700&display=swap" rel="stylesheet">'
CSS = """
*{margin:0;padding:0;box-sizing:border-box}body{background:#bbb;font-family:Montserrat,sans-serif}
.s{position:relative;overflow:hidden;width:1080px;height:1920px;margin:30px auto;background:#FBF4EC;color:#45301F}
em{font-style:italic;color:#A0603E}
.kick{font-weight:700;font-size:20px;letter-spacing:.34em;text-transform:uppercase;color:#C0592C}
.orn{display:flex;align-items:center;justify-content:center;gap:16px;margin-bottom:22px}
.orn i{display:block;width:80px;height:1px;background:linear-gradient(90deg,rgba(192,89,44,0),#C0592C)}
.orn i:last-child{transform:scaleX(-1)}
.orn b{width:7px;height:7px;transform:rotate(45deg);border:1px solid #C0592C}
.g{position:absolute;left:60px;right:60px;top:560px;display:grid;grid-template-columns:repeat(3,1fr);gap:26px 18px}
.c img{width:100%;height:236px;object-fit:cover;display:block;border-radius:16px;box-shadow:0 10px 24px rgba(90,62,49,.18)}
.c .cap{display:flex;gap:10px;align-items:baseline;margin-top:12px}
.c .n{font-weight:700;font-size:15px;letter-spacing:.12em;color:#C0592C}
.c .t{font-family:'Playfair Display',serif;font-style:italic;font-size:23px;line-height:1.2;color:#5A3E31}
"""
C = [("04-depan-bungalow-tersenyum", "50% 30%", "pagi, tanpa rencana"),
     ("09-profil-kerudung-palem", "40% 40%", "angin mengajak berdansa"),
     ("08-bougenvil-tersenyum", "70% 35%", "tersenyum tanpa alasan"),
     ("10-berjalan-pantai-surut", "66% 50%", "karang jadi lantai dansa"),
     ("01-duduk-meja-pantai-surut", "34% 55%", "laut yang bercerita"),
     ("03-nasi-goreng-teh-dingin", "62% 55%", "teh dingin &amp; kerupuk"),
     ("06-ponsel-di-meja", "40% 60%", "kupotret sekali saja"),
     ("11-ayunan-dekat-langit", "30% 35%", "lalu aku ikut menari"),
     ("12-ayunan-lebar-laut", "46% 55%", "bersama angin Selayar")]
cells = "".join(f'<div class="c"><img src="{P}{f}.jpg" style="object-position:{pos}" alt=""><div class="cap"><span class="n">{k:02d}</span><span class="t">{t}</span></div></div>'
                for k, (f, pos, t) in enumerate(C, 1))
HTML = f'''<div class="s" id="menari-satu-frame"><div style="position:absolute;inset:30px;border:1.5px solid rgba(138,95,72,.35)"></div>
  <div style="position:absolute;left:90px;right:90px;top:230px;text-align:center"><div class="orn"><i></i><b></b><i></i></div>
    <div class="kick">Sebuah cerita · Pantai Sunari</div>
    <div style="font-family:'Playfair Display',serif;font-size:66px;line-height:1.14;margin-top:20px">Hari ketika aku belajar<br><em>menari</em> bersama waktu.</div></div>
  <div class="g">{cells}</div>
  <div style="position:absolute;left:80px;right:80px;top:1530px;text-align:center">
    <div style="font-family:'Playfair Display',serif;font-size:44px;line-height:1.2">Beberapa tempat hanya dikunjungi.</div>
    <div style="font-family:'Playfair Display',serif;font-style:italic;font-size:44px;line-height:1.2;color:#A0603E;margin-top:6px">Sebagian lagi, dikenang.</div>
    <div style="margin-top:30px;font-weight:600;font-size:19px;letter-spacing:.38em;text-transform:uppercase;color:#7A5039">Pantai Sunari · Selayar</div></div></div>'''
(H / "menari_satu.html").write_text(f'<!doctype html><html lang="id"><head><meta charset="utf-8">{FONTS}<style>{CSS}</style></head><body>{HTML}</body></html>')
print(len(C))
