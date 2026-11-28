"""1 frame bersih: 6 gaya color grading gambar 1 (feed 4:5, render 4x = 4320x5400 PNG). Hanya foto + nama gaya.
Run: python3 social/export_grading_png.py && python3 social/build_grading_1frame.py && node social/render_grading_1frame.js
-> social/variasi-grading/6-color-grading-1-frame.png"""
import pathlib
H = pathlib.Path(__file__).parent
FONTS = '<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;1,400&family=Montserrat:wght@600;700&display=swap" rel="stylesheet">'
CSS = """
*{margin:0;padding:0;box-sizing:border-box}body{background:#bbb;font-family:Montserrat,sans-serif}
.s{position:relative;overflow:hidden;width:1080px;height:1350px;margin:0 auto;background:#FBF4EC;color:#45301F}
.g{position:absolute;left:36px;right:36px;top:118px;display:grid;grid-template-columns:1fr 1fr;gap:16px 20px}
.c img{width:100%;height:344px;object-fit:cover;display:block;border-radius:12px}
.c div{display:flex;align-items:baseline;gap:10px;margin-top:8px}
.c b{font-weight:700;font-size:14px;letter-spacing:.14em;color:#C0592C}
.c span{font-family:'Playfair Display',serif;font-size:26px}
"""
S = [("1-sinematik-soft", "Sinematik Soft"), ("2-earthy-beige", "Earthy Beige"), ("3-warm-film", "Warm Film"),
     ("4-bright-airy", "Bright &amp; Airy"), ("5-teal-orange", "Teal &amp; Orange"), ("6-dark-moody", "Dark Moody")]
cells = "".join(f'<div class="c"><img src="variasi-grading/png/{f}.png" alt=""><div><b>{k:02d}</b><span>{t}</span></div></div>' for k, (f, t) in enumerate(S, 1))
HTML = f'''<div class="s" id="g1"><div style="position:absolute;left:36px;right:36px;top:34px;display:flex;justify-content:space-between;align-items:baseline">
  <div style="font-family:'Playfair Display',serif;font-size:46px">6 gaya <i style="color:#A0603E">color grading</i></div>
  <div style="font-weight:700;font-size:14px;letter-spacing:.3em;text-transform:uppercase;color:#7A5039">Pantai Sunari · Selayar</div></div>
  <div class="g">{cells}</div></div>'''
(H / "grading_1frame.html").write_text(f'<!doctype html><html lang="id"><head><meta charset="utf-8">{FONTS}<style>{CSS}</style></head><body>{HTML}</body></html>')
