"""Carousel cerita "Senja Hari Ini" (14 slide, 1080x1350): hook foto penuh + 12 slide cerita + penutup.
Run: python3 social/build_senja_cerita.py && node social/render_senja_cerita.js -> social/senja-cerita/"""
import pathlib
H = pathlib.Path(__file__).parent
LOGO = "../assets/logo-sunari-color.png"; LOGO_D = "../assets/logo-sunari-color-dark.png"; P = "../assets/photos/graded/senja__"
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
.fc .tm{position:absolute;left:84px;bottom:150px;color:#FBF4EC;text-shadow:0 2px 12px rgba(0,0,0,.5)}
.fc .tm b{font-family:'Playfair Display',serif;font-weight:400;font-size:120px;line-height:1}
.fc .tm span{font-weight:700;font-size:22px;letter-spacing:.3em;margin-left:14px}
.fc .fg{position:absolute;left:84px;bottom:76px;font-weight:600;font-size:20px;letter-spacing:.38em;text-transform:uppercase;color:#FBF4EC;opacity:.92}
.fc .fl{position:absolute;right:70px;bottom:56px;width:300px;filter:drop-shadow(0 2px 8px rgba(0,0,0,.45))}
"""
# (foto, posisi, tahap, judul, keterangan) — urut jalannya sore
SL = [("79-meja-kayak-golden-hour.jpg", "50% 60%", "Golden hour", 'Meja sudah <em>siap</em>', "Termos kopi di meja, kayak berjajar di pasir, laut masih tenang."),
      ("80-cahaya-masuk-resto.jpg", "50% 50%", "Golden hour", 'Cahaya masuk ke <em>resto</em>', "Tirai jingga mulai menyala, kursi pantai menunggu di depan."),
      ("81-resto-tirai-senja.jpg", "50% 55%", "Menjelang senja", 'Kursi mulai <em>terisi</em>', "Satu per satu tamu datang, minuman dingin, obrolan pelan."),
      ("82-dua-tamu-meja-senja.jpg", "50% 50%", "Menjelang senja", 'Cerita di meja <em>kayu</em>', "Di bawah pohon ketapang, matahari tepat di depan mata."),
      ("71-siluet-tirai-matahari.jpg", "45% 50%", "Menjelang senja", 'Duduk di balik <em>tirai</em>', "Minuman di tangan, jalur cahaya jatuh di depan meja."),
      ("83-fotografer-di-tepi-pantai.jpg", "50% 62%", "Menjelang senja", 'Lensa <em>siap</em>', "Kamera diarahkan ke laut, menunggu cahaya terbaik."),
      ("76-staf-bantu-ayunan.jpg", "50% 55%", "Matahari turun", 'Dibantu naik <em>ayunan</em>', "Tim SunaRi siap membantu, ayunan raksasa gratis untuk dicoba."),
      ("77-ayunan-siluet-dekat.jpg", "50% 45%", "Matahari turun", 'Lalu, <em>melayang</em>', "Sejenak di udara, langit jingga di sekeliling."),
      ("72-ayunan-di-antara-kelapa.jpg", "50% 60%", "Matahari turun", 'Berayun ke arah <em>matahari</em>', "Di antara pohon kelapa, matahari tepat di cakrawala."),
      ("70-perahu-nelayan-daun-kelapa.jpg", "50% 55%", "Matahari terbenam", 'Nelayan <em>pulang</em>', "Perahu melintas pelan di jalur cahaya."),
      ("73-kayak-pelampung-perahu.jpg", "50% 78%", "Matahari terbenam", 'Kayak <em>beristirahat</em>', "Pelampung digantung, kayak menunggu besok sore."),
      ("75-afterglow-dua-sahabat.jpg", "50% 55%", "Afterglow", 'Langit belum <em>selesai</em>', "Matahari sudah tenggelam, jingga dan merah muda masih bertahan.")]
N = len(SL) + 2
T = [f'''<div class="t fc" id="senja-01"><img class="bgf" src="{P}74-matahari-menyentuh-laut-kapal.jpg" style="object-position:55% 50%" alt="">
  <div class="vt"></div><div class="vb"></div>
  <div class="fk">Senja hari ini · Pantai Sunari</div>
  <div class="fh">Sore ini terlalu <em>indah</em><br>untuk dilewatkan.</div>
  <div class="tm"><b>17.57</b><span>WITA</span></div>
  <div class="fg">Geser untuk ceritanya &nbsp;→</div><img class="fl" src="{LOGO_D}" alt=""></div>''']
for k, (img, pos, kick, t, sub) in enumerate(SL, 2):
    T.append(f'''<div class="t" id="senja-{k:02d}"><div class="ph"><img src="{P}{img}" style="object-position:{pos}" alt=""><img class="lg" src="{LOGO_D}" alt=""></div>
  <div class="kick">{kick}</div><div class="ttl emb">{t}</div><div class="sub">{sub}</div>
  <div class="bt"><span>SunaRi · Selayar</span><span class="h">#sunarisunsetmoment</span><span>{k:02d} / {N:02d}</span></div></div>''')
TIPS = ["Datang 30 menit sebelum matahari terbenam", "Akhir Nov–Des: senja sekitar 18.00 WITA", "Ayunan raksasa gratis, kayak bisa disewa", "Ikuti jam senja harian di story kami"]
T.append(f'''<div class="t" id="senja-{N:02d}"><div style="position:absolute;inset:36px;border:1.5px solid rgba(138,95,72,.4)"></div>
  <img src="{LOGO}" style="position:absolute;left:50%;transform:translateX(-50%);top:130px;width:360px" alt="">
  <div style="position:absolute;left:100px;right:100px;top:430px;text-align:center;color:#45301F">
    <div style="font-weight:700;font-size:21px;letter-spacing:.32em;text-transform:uppercase;color:#7A5039">Sampai jumpa besok sore</div>
    <div class="emb" style="font-family:'Playfair Display',serif;font-size:80px;line-height:1.1;margin-top:14px">Senja <em style="color:#A0603E">berikutnya</em></div>
    <div style="margin-top:40px;border-top:1.5px solid rgba(138,95,72,.3)">{"".join(f'<div style="padding:20px 0;border-bottom:1.5px solid rgba(138,95,72,.3);font-size:28px">{x}</div>' for x in TIPS)}</div></div>
  <div style="position:absolute;left:0;right:0;bottom:150px;text-align:center">
    <div style="font-weight:700;font-size:20px;letter-spacing:.32em;text-transform:uppercase;color:#7A5039">Info &amp; reservasi</div>
    <div style="font-family:'Playfair Display',serif;font-size:58px;color:#45301F;margin-top:8px"><i style="color:#A0603E">WhatsApp</i> {WA}</div></div>
  <div style="position:absolute;left:0;right:0;bottom:96px;text-align:center;font-weight:600;font-size:19px;letter-spacing:.38em;text-transform:uppercase;color:#7A5039">Pantai Sunari · Selayar</div>
  <div style="position:absolute;left:0;right:0;bottom:62px;text-align:center;font-weight:700;font-size:17px;letter-spacing:.2em;color:#C0592C">#sunarisunsetmoment</div></div>''')
(H / "senja_cerita.html").write_text(f'<!doctype html><html lang="id"><head><meta charset="utf-8">{FONTS}<style>{CSS}</style></head><body>{"".join(T)}</body></html>')
print(len(T))
