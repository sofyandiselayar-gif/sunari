"""1 frame (feed 4:5, render HD 2x = 2160x2700): 6 rekomendasi color grading untuk carousel Menari di SunaRi, contoh foto 1.
Run: python3 social/grade_menari.py && python3 social/grade_variasi.py && python3 social/build_rekomendasi_grading.py
     && node social/render_rekomendasi_grading.js -> social/variasi-grading/rekomendasi-6-color-grading.png"""
import pathlib
H = pathlib.Path(__file__).parent
N = "01-duduk-meja-pantai-surut"; G = "../assets/photos/graded/"
FONTS = '<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;1,400;1,500&family=Montserrat:wght@500;600;700&display=swap" rel="stylesheet">'
CSS = """
*{margin:0;padding:0;box-sizing:border-box}body{background:#bbb;font-family:Montserrat,sans-serif}
.s{position:relative;overflow:hidden;width:1080px;height:1350px;margin:30px auto;background:#FBF4EC;color:#45301F}
em{font-style:italic;color:#A0603E}
.g{position:absolute;left:48px;right:48px;top:160px;display:grid;grid-template-columns:1fr 1fr;gap:26px 30px}
.c{position:relative}
.c img{width:100%;height:262px;object-fit:cover;object-position:40% 55%;display:block;border-radius:14px;box-shadow:0 10px 24px rgba(90,62,49,.18)}
.c .no{position:absolute;left:14px;top:12px;width:44px;height:44px;border-radius:50%;background:rgba(251,244,236,.92);display:flex;align-items:center;justify-content:center;font-family:'Playfair Display',serif;font-size:24px;color:#45301F}
.c .bd{position:absolute;right:12px;top:12px;background:#C0592C;color:#FBF4EC;font-weight:700;font-size:13px;letter-spacing:.14em;text-transform:uppercase;padding:8px 12px;border-radius:30px}
.c h3{font-family:'Playfair Display',serif;font-weight:500;font-size:29px;margin-top:10px}
.c p{font-size:16px;line-height:1.42;color:#5A3E31;margin-top:4px}
.c p b{font-weight:600;color:#A0603E}
"""
S = [("menari__" + N, "Sinematik Soft", "Kontras lembut, bayangan teal, glow halus.", "cerita memorial (dipakai kini)", "Paling cocok"),
     ("variasi/" + N + "__earthy", "Earthy Beige", "Warna krem, selaras dengan hijab &amp; outfit.", "feed estetik yang seragam", ""),
     ("variasi/" + N + "__film", "Warm Film", "Hangat keemasan, hitam matte, hijau zaitun.", "nuansa nostalgia &amp; liburan", ""),
     ("variasi/" + N + "__cerah", "Bright &amp; Airy", "Terang, pastel, putih bersih.", "pagi segar &amp; ceria", ""),
     ("variasi/" + N + "__tealorange", "Teal &amp; Orange", "Laut teal, kulit &amp; kayu oranye, tegas.", "kesan film &amp; dramatis", ""),
     ("variasi/" + N + "__dark", "Dark Moody", "Gelap, warna tenang, vignette.", "suasana tenang &amp; dalam", "")]
cells = "".join(f'''<div class="c"><img src="{G}{f}.jpg" alt=""><div class="no">{k}</div>{f'<div class="bd">{b}</div>' if b else ""}
  <h3>{t}</h3><p>{d}<br><b>Cocok untuk:</b> {u}</p></div>''' for k, (f, t, d, u, b) in enumerate(S, 1))
HTML = f'''<div class="s" id="rekomendasi"><div style="position:absolute;left:48px;right:48px;top:44px">
  <div style="font-weight:700;font-size:16px;letter-spacing:.34em;text-transform:uppercase;color:#C0592C">Carousel · Menari di SunaRi</div>
  <div style="font-family:'Playfair Display',serif;font-size:52px;line-height:1.1;margin-top:10px">6 rekomendasi <em>color grading</em></div></div>
  <div class="g">{cells}</div></div>'''
(H / "rekomendasi_grading.html").write_text(f'<!doctype html><html lang="id"><head><meta charset="utf-8">{FONTS}<style>{CSS}</style></head><body>{HTML}</body></html>')
print(len(S))
