"""Feed kutipan "Setiap hari di Selayar berakhir dengan indah." (dibuat ulang, 1080x1350, 3 variasi).
Run: python3 social/build_quote.py && node social/render_quote.js -> social/quote/*.png"""
import pathlib
H = pathlib.Path(__file__).parent
LOGO = "../assets/logo-sunari-color.png"; LOGO_D = "../assets/logo-sunari-color-dark.png"; P = "../assets/photos/"
FONTS = '<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;1,400;1,500&family=Montserrat:wght@500;600;700&display=swap" rel="stylesheet">'
CSS = """
*{margin:0;padding:0;box-sizing:border-box}
body{background:#bbb;font-family:Montserrat,sans-serif}
.t{position:relative;overflow:hidden;width:1080px;height:1350px;margin:30px auto}
.q{font-family:'Playfair Display',serif;font-weight:400;font-size:84px;line-height:1.14;text-align:center}
.q em{font-style:italic}
.en{font-weight:600;font-size:22px;letter-spacing:.42em;text-transform:uppercase;text-align:center}
.rule{width:90px;height:2px;margin:40px auto}
.ft{position:absolute;left:0;right:0;bottom:70px;text-align:center;font-weight:600;font-size:19px;letter-spacing:.38em;text-transform:uppercase}
.tag{position:absolute;left:0;right:0;bottom:36px;text-align:center;font-weight:700;font-size:17px;letter-spacing:.2em}
.frame{position:absolute;inset:36px;border:1.5px solid}
.sh{text-shadow:0 3px 16px rgba(0,0,0,.55),0 1px 3px rgba(0,0,0,.5)}
.emb{text-shadow:0 1.5px 0 rgba(255,255,255,.85),0 2px 4px rgba(90,62,49,.22)}
"""
Q = 'Setiap hari di Selayar<br>berakhir dengan <em>indah.</em>'
EN = "Where every day ends beautifully"
T = []
# A · krem minimalis + logo berwarna
T.append(f'''<div class="t" id="carousel-01" style="background:#F3E3CC">
  <div class="frame" style="border-color:rgba(138,95,72,.45)"></div>
  <img src="{LOGO}" style="position:absolute;left:50%;transform:translateX(-50%);top:250px;width:380px" alt="">
  <div style="position:absolute;left:80px;right:80px;top:580px;color:#45301F">
    <div class="q emb">{Q.replace('<em>', '<em style="color:#A0603E">')}</div>
    <div class="rule" style="background:linear-gradient(90deg,#FDB15D,#FF8A5C)"></div>
    <div class="en" style="color:#7A5039">{EN}</div></div>
  <div class="ft" style="color:#7A5039;bottom:96px">Pantai Sunari · Selayar</div>
  <div class="tag" style="color:#C0592C;bottom:62px">#sunarisunsetmoment</div></div>''')
(H / "quote.html").write_text(f'<!doctype html><html lang="id"><head><meta charset="utf-8">{FONTS}<style>{CSS}</style></head><body>{"".join(T)}</body></html>')
print(len(T))

# ================================================================== LANJUTAN CAROUSEL (slide 2–5), gaya baru
WA = "0821-8903-3044"
CSS2 = """
.cs{background:#FBF4EC}
.cs .ph{position:absolute;left:60px;right:60px;top:60px;height:820px;border-radius:24px;overflow:hidden;box-shadow:0 14px 36px rgba(90,62,49,.18)}
.cs .ph img{width:100%;height:100%;object-fit:cover}
.cs .ph .lg{position:absolute;left:28px;top:26px;width:200px;height:auto;filter:drop-shadow(0 2px 8px rgba(0,0,0,.5))}
.cs .kick{position:absolute;left:64px;top:930px;font-weight:700;font-size:21px;letter-spacing:.32em;text-transform:uppercase;color:#7A5039}
.cs .ttl{position:absolute;left:64px;right:64px;top:975px;font-family:'Playfair Display',serif;font-size:76px;line-height:1.1;color:#45301F}
.cs .ttl em{font-style:italic;color:#A0603E}
.cs .sub{position:absolute;left:64px;right:64px;top:1080px;font-size:31px;line-height:1.5;color:#4A3426}
.cs .bt{position:absolute;left:64px;right:64px;bottom:56px;display:flex;justify-content:space-between;font-weight:700;font-size:18px;letter-spacing:.26em;text-transform:uppercase;color:#7A5039;padding-top:18px;border-top:1.5px solid rgba(138,95,72,.3)}
.cs .bt .h{color:#C0592C;letter-spacing:.12em;text-transform:none}
"""
SL = [("senja/44-dua-kayak-emas-1743.jpg", "50% 55%", 'Laut berubah <em>keemasan</em>', "Menjelang pukul lima sore, cahaya mulai melembut di Pantai Sunari."),
      ("senja/16-perahu-nelayan.jpg", "50% 60%", 'Perahu pulang <em>ke darat</em>', "Saat langit oranye, nelayan pun pulang."),
      ("senja/10-kayak-pantulan.jpg", "50% 55%", 'Matahari yang <em>menari</em>', "SunaRi: <b>sun</b> dan <b>nari</b>. Matahari yang menari turun ke laut Selayar."),
      ("aktivitas/05-ayunan-raksasa-senja.jpg", "40% 55%", 'Berayun <em>menyambut senja</em>', "Sejenak melayang, sebelum matahari menyentuh laut."),
      ("senja/18-kayak-berdua-pelampung.jpg", "50% 60%", 'Tempat senja <em>pulang</em>', "Dan setiap senja, kamu juga pulang ke sini."),
      ("senja/37-afterglow-kayak-pelampung-1814.jpg", "50% 50%", 'Langit belum <em>ingin pulang</em>', "Matahari tenggelam, tapi langit masih bercerita, jingga, merah muda, lalu ungu.")]
for k, (img, pos, t, sub) in enumerate(SL, 2):
    T.append(f'''<div class="t cs" id="carousel-{k:02d}"><div class="ph"><img src="{P}{img}" style="object-position:{pos}" alt=""><img class="lg" src="{LOGO_D}" alt=""></div>
  <div class="kick">Setiap hari berakhir indah</div><div class="ttl emb">{t}</div><div class="sub">{sub}</div>
  <div class="bt"><span>SunaRi · Selayar</span><span class="h">#sunarisunsetmoment</span><span>0{k} / 08</span></div></div>''')
T.append(f'''<div class="t cs" id="carousel-08"><div class="frame" style="border-color:rgba(138,95,72,.4)"></div>
  <img src="{LOGO}" style="position:absolute;left:50%;transform:translateX(-50%);top:150px;width:400px" alt="">
  <div style="position:absolute;left:100px;right:100px;top:470px;text-align:center;color:#45301F">
    <div style="font-weight:700;font-size:21px;letter-spacing:.32em;text-transform:uppercase;color:#7A5039">Setiap hari berakhir indah</div>
    <div class="q emb" style="font-size:88px;margin-top:16px">Tempat <em style="color:#A0603E">senja pulang</em></div>
    <div style="margin-top:44px;border-top:1.5px solid rgba(138,95,72,.3)">
      {"".join(f'<div style="padding:22px 0;border-bottom:1.5px solid rgba(138,95,72,.3);font-size:30px">{x}</div>' for x in ["Resort tepi Pantai Sunari", "Kepulauan Selayar, Sulawesi Selatan", "<i>Where every day ends beautifully</i>"])}</div></div>
  <div style="position:absolute;left:0;right:0;bottom:150px;text-align:center">
    <div style="font-weight:700;font-size:20px;letter-spacing:.32em;text-transform:uppercase;color:#7A5039">Info &amp; reservasi</div>
    <div style="font-family:'Playfair Display',serif;font-size:58px;color:#45301F;margin-top:8px"><i style="color:#A0603E">WhatsApp</i> {WA}</div></div>
  <div class="ft" style="color:#7A5039;bottom:96px">Pantai Sunari · Selayar</div>
  <div class="tag" style="color:#C0592C;bottom:62px">#sunarisunsetmoment</div></div>''')
(H / "quote.html").write_text(f'<!doctype html><html lang="id"><head><meta charset="utf-8">{FONTS}<style>{CSS}{CSS2}</style></head><body>{"".join(T)}</body></html>')
print(len(T))
