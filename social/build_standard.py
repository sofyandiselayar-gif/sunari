"""Feed carousel Standard Bungalow (7 slide, 1080x1350, gaya seri "Setiap hari berakhir indah").
Run: python3 social/build_standard.py && node social/render_standard.js -> social/standard/*.png"""
import pathlib
H = pathlib.Path(__file__).parent
LOGO = "../assets/logo-sunari-color.png"; LOGO_D = "../assets/logo-sunari-color-dark.png"; P = "../assets/photos/standard-bungalow/"
WA = "0821-8903-3044"; N = 7
FONTS = '<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;1,400;1,500&family=Montserrat:wght@500;600;700&display=swap" rel="stylesheet">'
CSS = """
*{margin:0;padding:0;box-sizing:border-box}
body{background:#bbb;font-family:Montserrat,sans-serif}
.t{position:relative;overflow:hidden;width:1080px;height:1350px;margin:30px auto;background:#FBF4EC}
.emb{text-shadow:0 1.5px 0 rgba(255,255,255,.85),0 2px 4px rgba(90,62,49,.22)}
.frame{position:absolute;inset:36px;border:1.5px solid rgba(138,95,72,.4)}
.ph{position:absolute;left:60px;right:60px;top:60px;height:820px;border-radius:24px;overflow:hidden;box-shadow:0 14px 36px rgba(90,62,49,.18)}
.ph img{width:100%;height:100%;object-fit:cover}
.ph .lg{position:absolute;left:28px;top:26px;width:200px;height:auto;filter:drop-shadow(0 2px 8px rgba(0,0,0,.5))}
.kick{position:absolute;left:64px;top:930px;font-weight:700;font-size:21px;letter-spacing:.32em;text-transform:uppercase;color:#7A5039}
.ttl{position:absolute;left:64px;right:64px;top:975px;font-family:'Playfair Display',serif;font-size:76px;line-height:1.1;color:#45301F}
.ttl em{font-style:italic;color:#A0603E}
.sub{position:absolute;left:64px;right:64px;top:1080px;font-size:31px;line-height:1.5;color:#4A3426}
.bt{position:absolute;left:64px;right:64px;bottom:56px;display:flex;justify-content:space-between;font-weight:700;font-size:18px;letter-spacing:.26em;text-transform:uppercase;color:#7A5039;padding-top:18px;border-top:1.5px solid rgba(138,95,72,.3)}
.bt .h{color:#C0592C;letter-spacing:.12em;text-transform:none}
.cv .ttl{top:960px;font-size:92px}
.cv .sub{top:1080px}
.fx{display:grid;grid-template-columns:1fr 1fr;column-gap:40px;margin-top:40px;border-top:1.5px solid rgba(138,95,72,.3)}
.fx div{padding:19px 0;border-bottom:1.5px solid rgba(138,95,72,.3);font-size:28px;color:#45301F;text-align:left}
.fx div::before{content:"";display:inline-block;width:10px;height:10px;border-radius:50%;background:linear-gradient(90deg,#FDB15D,#FF8A5C);margin-right:16px;vertical-align:middle}
"""
KICK = "Standard Bungalow"
SL = [("01-teras-view-laut.jpg", "50% 55%", 'Standard <em>Bungalow</em>', "Bungalow kayu beratap tinggi, pagi menghadap laut Selayar.", "Room tour · SunaRi"),
      ("01-teras-view-laut.jpg", "0% 50%;transform:scale(1.5);transform-origin:0% 62%", 'Pagi menghadap <em>laut</em>', "Teras pribadi yang luas dengan kursi santai, laut dan taman di depan mata.", KICK),
      ("03-kamar-depan.jpg", "50% 60%", 'Queen bed, <em>atap tinggi</em>', "Kamar kayu dengan atap tinggi, AC dan tirai blackout.", KICK),
      ("02-kamar-sudut.jpg", "50% 60%", 'Nyaman untuk <em>berdua</em>', "Untuk 2 tamu, maks. 3 dengan extra bed. Ada meja kerja/rias dan set kopi/teh.", KICK),
      ("04-kamar-mandi-bambu.jpg", "50% 55%", 'Cermin &amp; <em>meja kayu</em>', "Area bersiap dengan cermin besar di kamar mandi dalam.", KICK),
      ("05-kamar-mandi-toilet.jpg", "50% 60%", 'Kamar mandi <em>di dalam</em>', "Shower, wastafel dan toilet duduk di dalam kamar.", KICK)]
T = []
for k, (img, pos, t, sub, kick) in enumerate(SL, 1):
    T.append(f'''<div class="t{' cv' if k == 1 else ''}" id="standard-{k:02d}"><div class="ph"><img src="{P}{img}" style="object-position:{pos}" alt=""><img class="lg" src="{LOGO_D}" alt=""></div>
  <div class="kick">{kick}</div><div class="ttl emb">{t}</div><div class="sub">{sub}</div>
  <div class="bt"><span>SunaRi · Selayar</span><span class="h">#sunarisunsetmoment</span><span>{k:02d} / {N:02d}</span></div></div>''')
FX = ["Queen bed", "Termasuk sarapan", "AC &amp; Wi-Fi", "Set kopi/teh", "Pemanas air", "Tirai blackout", "Meja kerja/rias", "Kamar mandi dalam", "Shower &amp; toilet duduk", "Teras pribadi luas"]
T.append(f'''<div class="t" id="standard-07"><div class="frame"></div>
  <img src="{LOGO}" style="position:absolute;left:50%;transform:translateX(-50%);top:120px;width:360px" alt="">
  <div style="position:absolute;left:100px;right:100px;top:420px;text-align:center;color:#45301F">
    <div style="font-weight:700;font-size:21px;letter-spacing:.32em;text-transform:uppercase;color:#7A5039">Fasilitas kamar</div>
    <div class="emb" style="font-family:'Playfair Display',serif;font-size:80px;line-height:1.1;margin-top:14px">Standard <em style="color:#A0603E">Bungalow</em></div>
    <div class="fx">{"".join(f"<div>{x}</div>" for x in FX)}</div></div>
  <div style="position:absolute;left:0;right:0;bottom:150px;text-align:center">
    <div style="font-weight:700;font-size:20px;letter-spacing:.32em;text-transform:uppercase;color:#7A5039">Info &amp; reservasi</div>
    <div style="font-family:'Playfair Display',serif;font-size:58px;color:#45301F;margin-top:8px"><i style="color:#A0603E">WhatsApp</i> {WA}</div></div>
  <div style="position:absolute;left:0;right:0;bottom:96px;text-align:center;font-weight:600;font-size:19px;letter-spacing:.38em;text-transform:uppercase;color:#7A5039">Pantai Sunari · Selayar</div>
  <div style="position:absolute;left:0;right:0;bottom:62px;text-align:center;font-weight:700;font-size:17px;letter-spacing:.2em;color:#C0592C">#sunarisunsetmoment</div></div>''')
(H / "standard.html").write_text(f'<!doctype html><html lang="id"><head><meta charset="utf-8">{FONTS}<style>{CSS}</style></head><body>{"".join(T)}</body></html>')
print(len(T))
