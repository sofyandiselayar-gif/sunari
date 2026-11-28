"""Carousel "Sunset Moment" (8 slide, 1080x1350): hook + 7 slide cerita sore + penutup. Foto baru senja/85-99.
Run: python3 social/build_sunset_moment.py && node social/render_sunset_moment.js -> social/sunset-moment/"""
import pathlib
H = pathlib.Path(__file__).parent
LOGO = "../assets/logo-sunari-color.png"; LOGO_D = "../assets/logo-sunari-color-dark.png"; P = "../assets/photos/senja/"
WA = "0821-8903-3044"
FONTS = '<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;1,400;1,500&family=Montserrat:wght@500;600;700&display=swap" rel="stylesheet">'
CSS = """
*{margin:0;padding:0;box-sizing:border-box}body{background:#bbb;font-family:Montserrat,sans-serif}
.t{position:relative;overflow:hidden;width:1080px;height:1350px;margin:30px auto;background:#FBF4EC}
.emb{text-shadow:0 1.5px 0 rgba(255,255,255,.85),0 2px 4px rgba(90,62,49,.22)}
.ph{position:absolute;left:60px;right:60px;top:60px;height:820px;border-radius:24px;overflow:hidden;box-shadow:0 14px 36px rgba(90,62,49,.18)}
.ph img{width:100%;height:100%;object-fit:cover}
.ph .lg{position:absolute;left:28px;top:26px;width:200px;height:auto;filter:drop-shadow(0 2px 8px rgba(0,0,0,.5))}
.kick{position:absolute;left:64px;top:930px;font-weight:700;font-size:21px;letter-spacing:.32em;text-transform:uppercase;color:#C0592C}
.ttl{position:absolute;left:64px;right:64px;top:975px;font-family:'Playfair Display',serif;font-size:76px;line-height:1.1;color:#45301F}
.ttl em{font-style:italic;color:#A0603E}
.sub{position:absolute;left:64px;right:64px;top:1080px;font-size:31px;line-height:1.5;color:#4A3426}
.bt{position:absolute;left:64px;right:64px;bottom:56px;display:flex;justify-content:space-between;font-weight:700;font-size:18px;letter-spacing:.26em;text-transform:uppercase;color:#7A5039;padding-top:18px;border-top:1.5px solid rgba(138,95,72,.3)}
.bt .h{color:#C0592C;letter-spacing:.12em;text-transform:none}
.fc .bgf{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.fc .vt{position:absolute;left:0;right:0;top:0;height:700px;background:linear-gradient(180deg,rgba(20,12,6,.6),rgba(20,12,6,0))}
.fc .vb{position:absolute;left:0;right:0;bottom:0;height:420px;background:linear-gradient(0deg,rgba(20,12,6,.65),rgba(20,12,6,0))}
.fc .fk{position:absolute;left:84px;top:110px;font-weight:600;font-size:22px;letter-spacing:.42em;text-transform:uppercase;color:#FBF4EC;text-shadow:0 2px 10px rgba(0,0,0,.5)}
.fc .fh{position:absolute;left:80px;right:80px;top:160px;font-family:'Playfair Display',serif;font-size:104px;line-height:1.06;color:#FBF4EC;text-shadow:0 3px 18px rgba(0,0,0,.45)}
.fc .fh em{color:#FDB15D}
.fc .fg{position:absolute;left:84px;bottom:76px;font-weight:600;font-size:20px;letter-spacing:.38em;text-transform:uppercase;color:#FBF4EC;opacity:.92}
.fc .fl{position:absolute;right:70px;bottom:56px;width:300px;filter:drop-shadow(0 2px 8px rgba(0,0,0,.45))}
"""
HOOK = "85-dua-tamu-bingkai-pohon-tirai.jpg"
# (foto, posisi, tahap, judul, keterangan)
SL = [("88-matahari-terbenam-langit-merah.jpg", "50% 55%", "Matahari terbenam", 'Matahari <em>menyentuh</em> laut', "Langit berubah jingga pekat, laut ikut diam sejenak."),
      ("97-gazebo-tirai-pantulan-matahari.jpg", "50% 50%", "Kita mulai dari awal sore", 'Sore mulai dari <em>cahaya</em>', "Tirai jingga, kursi kayu, dan pantulan matahari di laut."),
      ("96-kayak-pulau-awan.jpg", "50% 70%", "Golden hour", 'Kayak <em>meluncur</em> pelan', "Laut tenang, awan merona merah muda di atas pulau seberang."),
      ("91-tamu-memotret-matahari.jpg", "50% 60%", "Menjelang senja", 'Semua ingin <em>mengabadikan</em>', "Ponsel terangkat, jalur cahaya jatuh tepat di depan."),
      ("87-tamu-berhijab-tepi-pantai.jpg", "50% 60%", "Menjelang senja", 'Berdiri di tepi <em>air</em>', "Mengobrol, bermain air, menunggu matahari turun bersama."),
      ("98-kayak-langit-merah.jpg", "50% 70%", "Afterglow", 'Langit belum <em>selesai</em>', "Matahari sudah turun, jingga dan merah masih menemani kayak terakhir.")]
N = len(SL) + 2
T = [f'''<div class="t fc" id="sm-01"><img class="bgf" src="{P}{HOOK}" style="object-position:50% 50%" alt="">
  <div class="vt"></div><div class="vb"></div>
  <div class="fk">Sunset moment · Pantai Sunari</div>
  <div class="fh">Senja di Selayar <em>begini</em> rasanya.</div>
  <div class="fg">Geser pelan-pelan &nbsp;→</div><img class="fl" src="{LOGO_D}" alt=""></div>''']
for k, (img, pos, kick, t, sub) in enumerate(SL, 2):
    T.append(f'''<div class="t" id="sm-{k:02d}"><div class="ph"><img src="{P}{img}" style="object-position:{pos}" alt=""><img class="lg" src="{LOGO_D}" alt=""></div>
  <div class="kick">{kick}</div><div class="ttl emb">{t}</div><div class="sub">{sub}</div>
  <div class="bt"><span>SunaRi · Selayar</span><span class="h">#sunarisunsetmoment</span><span>{k:02d} / {N:02d}</span></div></div>''')
T.append(f'''<div class="t" id="sm-{N:02d}"><div style="position:absolute;inset:36px;border:1.5px solid rgba(138,95,72,.4)"></div>
  <img src="{LOGO}" style="position:absolute;left:50%;transform:translateX(-50%);top:130px;width:360px" alt="">
  <div style="position:absolute;left:100px;right:100px;top:440px;text-align:center;color:#45301F">
    <div style="font-weight:700;font-size:21px;letter-spacing:.32em;text-transform:uppercase;color:#7A5039">Senja ini menunggumu</div>
    <div class="emb" style="font-family:'Playfair Display',serif;font-size:80px;line-height:1.1;margin-top:14px">Simpan untuk <em style="color:#A0603E">liburanmu</em></div>
    <div style="margin-top:44px;font-size:30px;line-height:1.55">Tag orang yang ingin kamu ajak<br>menikmati sore seperti ini.</div></div>
  <div style="position:absolute;left:0;right:0;bottom:190px;text-align:center">
    <div style="font-weight:700;font-size:20px;letter-spacing:.32em;text-transform:uppercase;color:#7A5039">Biar kami bantu</div>
    <div style="font-family:'Playfair Display',serif;font-size:58px;color:#45301F;margin-top:8px"><i style="color:#A0603E">WhatsApp</i> {WA}</div></div>
  <div style="position:absolute;left:0;right:0;bottom:96px;text-align:center;font-weight:600;font-size:19px;letter-spacing:.38em;text-transform:uppercase;color:#7A5039">Pantai Sunari · Selayar</div>
  <div style="position:absolute;left:0;right:0;bottom:62px;text-align:center;font-weight:700;font-size:17px;letter-spacing:.2em;color:#C0592C">#sunarisunsetmoment</div></div>''')
(H / "sunset_moment.html").write_text(f'<!doctype html><html lang="id"><head><meta charset="utf-8">{FONTS}<style>{CSS}</style></head><body>{"".join(T)}</body></html>')
print(len(T))
