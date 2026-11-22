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
T.append(f'''<div class="t" id="quote-a-minimal" style="background:#F3E3CC">
  <div class="frame" style="border-color:rgba(138,95,72,.45)"></div>
  <img src="{LOGO}" style="position:absolute;left:50%;transform:translateX(-50%);top:250px;width:380px" alt="">
  <div style="position:absolute;left:80px;right:80px;top:580px;color:#45301F">
    <div class="q emb">{Q.replace('<em>', '<em style="color:#A0603E">')}</div>
    <div class="rule" style="background:linear-gradient(90deg,#FDB15D,#FF8A5C)"></div>
    <div class="en" style="color:#7A5039">{EN}</div></div>
  <div class="ft" style="color:#7A5039;bottom:96px">Pantai Sunari · Selayar</div>
  <div class="tag" style="color:#C0592C;bottom:62px">#sunarisunsetmoment</div></div>''')
# B · foto senja penuh
T.append(f'''<div class="t" id="quote-b-foto">
  <img src="{P}senja/29-dua-kursi-menghadap-senja.jpg" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:50% 30%" alt="">
  <div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(15,8,4,.55) 0%,rgba(15,8,4,.25) 40%,rgba(15,8,4,.15) 60%,rgba(15,8,4,.6) 100%)"></div>
  <div class="frame" style="border-color:rgba(251,244,236,.5)"></div>
  <img src="{LOGO_D}" style="position:absolute;left:50%;transform:translateX(-50%);bottom:150px;width:300px;filter:drop-shadow(0 2px 10px rgba(0,0,0,.5))" alt="">
  <div class="sh" style="position:absolute;left:80px;right:80px;top:330px;color:#FBF4EC">
    <div class="q">{Q.replace('<em>', '<em style="color:#FDB15D">')}</div>
    <div class="rule" style="background:#FDB15D"></div>
    <div class="en">{EN}</div></div>
  <div class="ft sh" style="color:#FBF4EC;bottom:96px">Pantai Sunari · Selayar</div>
  <div class="tag sh" style="color:#FDB15D;bottom:62px">#sunarisunsetmoment</div></div>''')
# C · foto atas + teks bawah
T.append(f'''<div class="t" id="quote-c-split" style="background:#FBF4EC">
  <img src="{P}senja/28-matahari-di-bawah-daun.jpg" style="position:absolute;left:0;top:0;width:1080px;height:640px;object-fit:cover;object-position:50% 55%" alt="">
  <img src="{LOGO_D}" style="position:absolute;left:60px;top:54px;width:240px;filter:drop-shadow(0 2px 8px rgba(0,0,0,.5))" alt="">
  <div style="position:absolute;left:70px;right:70px;top:760px;color:#45301F">
    <div class="q emb" style="font-size:76px">{Q.replace('<em>', '<em style="color:#A0603E">')}</div>
    <div class="rule" style="background:linear-gradient(90deg,#FDB15D,#FF8A5C);margin:34px auto"></div>
    <div class="en" style="color:#7A5039">{EN}</div></div>
  <div class="ft" style="color:#7A5039;bottom:96px">Pantai Sunari · Selayar</div>
  <div class="tag" style="color:#C0592C;bottom:62px">#sunarisunsetmoment</div></div>''')
(H / "quote.html").write_text(f'<!doctype html><html lang="id"><head><meta charset="utf-8">{FONTS}<style>{CSS}</style></head><body>{"".join(T)}</body></html>')
print(len(T))
