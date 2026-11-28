"""Carousel cerita "Menari di SunaRi" (10 slide, 1080x1350): satu hari seorang tamu, dari bungalow sampai ayunan.
Run: python3 social/grade_menari.py && python3 social/build_menari.py && node social/render_menari.js -> social/menari/"""
import pathlib
H = pathlib.Path(__file__).parent
LOGO = "../assets/logo-sunari-color.png"; LOGO_D = "../assets/logo-sunari-color-dark.png"; P = "../assets/photos/graded/menari__"
WA = "0821-8903-3044"; N = 10
FONTS = '<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;1,400;1,500&family=Montserrat:wght@500;600;700&display=swap" rel="stylesheet">'
CSS = """
*{margin:0;padding:0;box-sizing:border-box}body{background:#bbb;font-family:Montserrat,sans-serif}
.t{position:relative;overflow:hidden;width:1080px;height:1350px;margin:30px auto;background:#FBF4EC;color:#45301F}
.bgf{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
em{font-style:italic;color:#A0603E}
.kick{font-weight:700;font-size:20px;letter-spacing:.34em;text-transform:uppercase;color:#C0592C}
.ttl{font-family:'Playfair Display',serif;font-size:62px;line-height:1.16}
.bt{position:absolute;left:64px;right:64px;bottom:50px;display:flex;justify-content:space-between;font-weight:700;font-size:17px;letter-spacing:.26em;text-transform:uppercase;color:#7A5039;padding-top:16px;border-top:1.5px solid rgba(138,95,72,.3)}
.bt.lt{color:rgba(251,244,236,.9);border-color:rgba(251,244,236,.35)}
.fr{position:absolute;overflow:hidden;box-shadow:0 16px 40px rgba(90,62,49,.2)}
.fr img{width:100%;height:100%;object-fit:cover;display:block}
.arch{border-radius:480px 480px 22px 22px}
.rd{border-radius:22px}
.orn{display:flex;align-items:center;gap:16px;margin-bottom:26px}
.orn i{display:block;width:80px;height:1px;background:#C0592C}
.orn b{width:7px;height:7px;transform:rotate(45deg);border:1.2px solid #C0592C}
.lt-t{color:#FBF4EC;text-shadow:0 2px 16px rgba(0,0,0,.5)}
.lt-t em{color:#FDB15D}
.pol{position:absolute;background:#fff;padding:22px 22px 90px;box-shadow:0 18px 40px rgba(90,62,49,.25)}
.pol img{width:100%;height:100%;object-fit:cover;display:block}
.pol span{position:absolute;left:0;right:0;bottom:26px;text-align:center;font-family:'Playfair Display',serif;font-style:italic;font-size:30px;color:#7A5039}
"""
def bt(k, lt=False):
    return f'<div class="bt{" lt" if lt else ""}"><span>Menari di SunaRi</span><span>{k:02d} / {N:02d}</span></div>'
def img(name, pos):
    return f'<img src="{P}{name}.jpg" style="object-position:{pos}" alt="">'
T = []
# 1. Hook: ayunan lebar
T.append(f'''<div class="t" id="menari-01"><img class="bgf" src="{P}12-ayunan-lebar-laut.jpg" style="object-position:46% 50%" alt="">
  <div style="position:absolute;inset:0 0 auto 0;height:640px;background:linear-gradient(180deg,rgba(30,20,14,.62),rgba(30,20,14,0))"></div>
  <div style="position:absolute;inset:auto 0 0 0;height:380px;background:linear-gradient(0deg,rgba(30,20,14,.6),rgba(30,20,14,0))"></div>
  <div class="lt-t" style="position:absolute;left:80px;right:80px;top:110px">
    <div class="kick" style="color:#FDB15D">Sebuah cerita · Pantai Sunari</div>
    <div style="font-family:'Playfair Display',serif;font-size:92px;line-height:1.06;margin-top:22px">Hari ketika aku belajar <em>menari</em> bersama waktu.</div></div>
  <div class="lt-t" style="position:absolute;left:84px;bottom:84px;font-weight:600;font-size:20px;letter-spacing:.36em;text-transform:uppercase">Geser pelan-pelan &nbsp;→</div>
  <img src="{LOGO_D}" style="position:absolute;right:70px;bottom:52px;width:260px;filter:drop-shadow(0 2px 8px rgba(0,0,0,.45))" alt=""></div>''')
# 2. Bungalow, bingkai lengkung
T.append(f'''<div class="t" id="menari-02"><div class="fr arch" style="left:90px;right:90px;top:70px;height:840px">{img("04-depan-bungalow-tersenyum", "50% 50%")}</div>
  <div style="position:absolute;left:90px;right:90px;top:960px"><div class="kick">Pagi · Bungalow kayu</div>
    <div class="ttl" style="margin-top:16px">Pagi itu aku melangkah keluar, <em>tanpa rencana apa pun.</em></div></div>{bt(2)}</div>''')
# 3. Profil kerudung
T.append(f'''<div class="t" id="menari-03"><div class="fr rd" style="left:0;right:400px;top:0;height:1350px;border-radius:0">{img("09-profil-kerudung-palem", "42% 50%")}</div>
  <div style="position:absolute;left:730px;right:60px;top:300px"><div class="orn"><i style="width:60px"></i><b></b></div>
    <div style="font-family:'Playfair Display',serif;font-size:46px;line-height:1.22">Angin laut menyentuh kerudungku,</div>
    <div style="font-family:'Playfair Display',serif;font-style:italic;font-size:46px;line-height:1.22;color:#A0603E;margin-top:18px">pelan, seperti mengajak berdansa.</div></div>
  <div style="position:absolute;left:730px;right:60px;bottom:50px;font-weight:700;font-size:17px;letter-spacing:.26em;color:#7A5039;padding-top:16px;border-top:1.5px solid rgba(138,95,72,.3)">03 / {N:02d}</div></div>''')
# 4. Dua foto bougenvil bertingkat
T.append(f'''<div class="t" id="menari-04">
  <div class="fr rd" style="left:64px;top:70px;width:470px;height:760px">{img("07-bougenvil-menengadah", "28% 50%")}</div>
  <div class="fr rd" style="left:560px;top:250px;width:456px;height:760px">{img("08-bougenvil-tersenyum", "72% 50%")}</div>
  <div style="position:absolute;left:64px;right:64px;top:1050px"><div class="kick">Taman bougenvil</div>
    <div class="ttl" style="margin-top:14px;font-size:54px">Aku menengadah lebih lama, <em>lalu tersenyum tanpa alasan.</em></div></div>{bt(4)}</div>''')
# 5. Berjalan di pantai surut, foto penuh
T.append(f'''<div class="t" id="menari-05"><img class="bgf" src="{P}10-berjalan-pantai-surut.jpg" style="object-position:68% 50%" alt="">
  <div style="position:absolute;inset:0 0 auto 0;height:620px;background:linear-gradient(180deg,rgba(30,20,14,.6),rgba(30,20,14,0))"></div>
  <div style="position:absolute;inset:auto 0 0 0;height:200px;background:linear-gradient(0deg,rgba(30,20,14,.5),rgba(30,20,14,0))"></div>
  <div class="lt-t" style="position:absolute;left:80px;right:80px;top:110px"><div class="kick" style="color:#FDB15D">Laut sedang surut</div>
    <div class="ttl" style="margin-top:18px;font-size:64px">Karang-karang muncul, seperti <em>lantai dansa</em> yang disiapkan alam.</div></div>{bt(5, True)}</div>''')
# 6. Duduk di meja pantai
T.append(f'''<div class="t" id="menari-06"><div class="fr rd" style="left:64px;right:64px;top:70px;height:840px">{img("01-duduk-meja-pantai-surut", "34% 50%")}</div>
  <div style="position:absolute;left:64px;right:64px;top:960px"><div class="kick">Siang · Di bawah ketapang</div>
    <div class="ttl" style="margin-top:16px">Aku duduk, memesan teh dingin, <em>dan membiarkan laut bercerita.</em></div></div>{bt(6)}</div>''')
# 7. Makanan + ponsel bertingkat
T.append(f'''<div class="t" id="menari-07">
  <div class="fr rd" style="left:64px;right:300px;top:70px;height:560px">{img("03-nasi-goreng-teh-dingin", "60% 50%")}</div>
  <div class="fr rd" style="left:300px;right:64px;top:600px;height:440px;border:10px solid #FBF4EC">{img("06-ponsel-di-meja", "40% 60%")}</div>
  <div style="position:absolute;left:64px;right:64px;top:1080px"><div class="ttl" style="font-size:50px">Sempat kupotret sekali,<br><em>lalu ponselnya kusimpan.</em></div></div>{bt(7)}</div>''')
# 8. Ayunan dekat, puncak cerita
T.append(f'''<div class="t" id="menari-08"><img class="bgf" src="{P}11-ayunan-dekat-langit.jpg" style="object-position:28% 50%" alt="">
  <div style="position:absolute;inset:auto 0 0 0;height:640px;background:linear-gradient(0deg,rgba(30,20,14,.72),rgba(30,20,14,.35) 60%,rgba(30,20,14,0))"></div>
  <div class="lt-t" style="position:absolute;left:80px;right:80px;bottom:150px"><div class="kick" style="color:#FDB15D">Ayunan tepi pantai</div>
    <div class="ttl" style="margin-top:18px;font-size:72px">Dan di sini, aku akhirnya <em>ikut menari</em> bersama angin.</div></div>{bt(8, True)}</div>''')
# 9. Polaroid kenangan
T.append(f'''<div class="t" id="menari-09">
  <div class="pol" style="left:90px;top:120px;width:500px;height:600px;transform:rotate(-5deg)">{img("05-depan-bungalow-tangga", "52% 50%")}<span>pagi yang pelan</span></div>
  <div class="pol" style="left:500px;top:330px;width:500px;height:600px;transform:rotate(4deg)">{img("02-duduk-meja-dekat", "30% 50%")}<span>teh dingin, laut surut</span></div>
  <div style="position:absolute;left:80px;right:80px;top:1010px;text-align:center"><div class="ttl" style="font-size:56px">Beberapa tempat hanya dikunjungi.</div>
    <div class="ttl" style="font-size:56px;margin-top:6px"><em>Sebagian lagi, dikenang.</em></div></div>{bt(9)}</div>''')
# 10. Penutup CTA
T.append(f'''<div class="t" id="menari-10"><div style="position:absolute;inset:36px;border:1.5px solid rgba(138,95,72,.4)"></div>
  <img src="{LOGO}" style="position:absolute;left:50%;transform:translateX(-50%);top:140px;width:360px" alt="">
  <div style="position:absolute;left:100px;right:100px;top:440px;text-align:center">
    <div class="kick" style="color:#7A5039">SunaRi · matahari yang menari</div>
    <div class="ttl" style="font-size:76px;margin-top:18px">Kini <em>giliranmu</em><br>menari di sini.</div>
    <div style="margin-top:44px;border-top:1.5px solid rgba(138,95,72,.3)">
      <div style="padding:22px 0;border-bottom:1.5px solid rgba(138,95,72,.3);font-size:29px">🔖 Simpan untuk liburanmu nanti</div>
      <div style="padding:22px 0;border-bottom:1.5px solid rgba(138,95,72,.3);font-size:29px">💌 Tag orang yang ingin kamu ajak menari</div></div></div>
  <div style="position:absolute;left:0;right:0;bottom:170px;text-align:center">
    <div style="font-weight:700;font-size:20px;letter-spacing:.32em;text-transform:uppercase;color:#7A5039">Info &amp; reservasi</div>
    <div style="font-family:'Playfair Display',serif;font-size:58px;margin-top:8px"><em>WhatsApp</em> {WA}</div></div>
  <div style="position:absolute;left:0;right:0;bottom:104px;text-align:center;font-weight:600;font-size:19px;letter-spacing:.38em;text-transform:uppercase;color:#7A5039">Pantai Sunari · Selayar</div>
  <div style="position:absolute;left:0;right:0;bottom:68px;text-align:center;font-weight:700;font-size:17px;letter-spacing:.2em;color:#C0592C">#sunarisunsetmoment</div></div>''')
(H / "menari.html").write_text(f'<!doctype html><html lang="id"><head><meta charset="utf-8">{FONTS}<style>{CSS}</style></head><body>{"".join(T)}</body></html>')
print(len(T))
