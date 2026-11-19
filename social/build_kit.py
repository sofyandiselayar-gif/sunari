"""Generate kit.html (all Instagram templates, minimalist-elegant style).
Edit the CONTENT section below, then run:  python3 social/build_kit.py && node social/render.js
"""
import html, pathlib
HERE = pathlib.Path(__file__).parent
WA = "0821-8903-3044"
SENJA = dict(time="17.57", date="Kamis, 19 November 2026", place="Pantai Tile-Tile")

# ---------------------------------------------------------------- CONTENT
ROOMS = [
  dict(prefix="sb", name="Superior Bungalow", photos="superior-bungalow",
       tagline="Rumah kayu di antara pohon kelapa", cover="02-eksterior-depan.jpg", cover_pos="50% 30%",
       slides=[("03-teras.jpg","50% 50%","Teras kayu pribadi","Tempat terbaik untuk kopi pagi dan obrolan sore, dengan pohon kelapa sebagai pemandangannya."),
               ("04-kamar-loteng.jpg","50% 50%","Atap A-frame & loteng","Langit-langit kayu menjulang dengan loteng di atasnya. Lapang, sejuk, dan hangat."),
               ("05-kamar-tempat-tidur.jpg","50% 50%","Tidur nyenyak, bangun santai","Kasur besar, pintu kaca ke teras, dan cahaya pagi yang masuk pelan-pelan."),
               ("10-kamar-mandi-taman.jpg","50% 60%","Kamar mandi semi-outdoor","Mandi di bawah rain shower, ditemani taman hijau dan langit terbuka.")],
       facts=["Bungalow kayu A-frame dengan loteng","Teras pribadi dengan kursi santai","Kamar mandi semi-outdoor, rain shower","AC, TV, perlengkapan kopi & teh","Beberapa langkah ke pantai"]),
  dict(prefix="st", name="Standard Bungalow", photos="standard-bungalow",
       tagline="Pagi menghadap laut Selayar", cover="01-teras-view-laut.jpg", cover_pos="50% 55%",
       slides=[("03-kamar-depan.jpg","50% 60%","Hangatnya rumah kayu","Dinding kayu, atap tinggi, dan seprai segar. Sederhana, bersih, dan nyaman."),
               ("02-kamar-sudut.jpg","50% 55%","Sejuk sepanjang hari","Kamar ber-AC dengan jendela atas yang membiarkan cahaya alami masuk."),
               ("04-kamar-mandi-bambu.jpg","50% 50%","Kamar mandi nuansa bambu","Dinding anyaman bambu dan lantai batu alam, dengan shower dan toilet duduk.")],
       facts=["Bungalow kayu untuk dua orang","Teras pribadi luas menghadap laut","AC & tempat tidur double","Kamar mandi dalam, shower & toilet duduk"]),
  dict(prefix="vp", name="VIP Standard Bungalow", photos="vip-standard-bungalow",
       tagline="Turun tangga, langsung pasir", cover="02-teras-view-pantai.jpg", cover_pos="50% 55%",
       slides=[("01-eksterior-rumah-panggung.jpg","50% 45%","Rumah panggung beratap rumbia","Berdiri di tepi pantai, dinaungi pohon kelapa, dengan atap lengkung tradisional."),
               ("04-teras-view-laut.jpg","60% 50%","Teras pribadi menghadap senja","Perahu nelayan lewat di kejauhan, dan matahari terbenam tepat di depan mata."),
               ("07-kamar-samping.jpg","50% 50%","Kamar yang hangat","Kayu dari lantai sampai atap, lampu dinding temaram, dan kasur besar yang empuk."),
               ("10-kamar-mandi-shower.jpg","50% 40%","Kamar mandi dalam","Area wastafel dan gantungan baju, lalu kamar mandi luas dengan shower.")],
       facts=["Rumah panggung tepat di bibir pantai","Teras pribadi menghadap laut & senja","AC, tempat tidur double, lampu dinding","Perlengkapan kopi/teh & air mineral","Kamar mandi dalam, shower & toilet duduk"]),
]
PROMO = dict(kicker="Paket Akhir Pekan", title="Staycation", title_it="Senja", sub="Dua malam, dua kali senja",
             items=["Superior Bungalow kayu A-frame","Senja Dinner ikan bakar untuk dua orang","Kelapa muda setiap sore"])
QUOTE = dict(text="Setiap hari di Selayar<br>berakhir dengan <em>indah.</em>", en="Where every day ends beautifully")
# ---------------------------------------------------------------- END CONTENT

e = html.escape
LOGO = "../assets/logo-sunari-driftwood.png"
CSS = """
:root{--ink:#5A3E31;--cream:#FBF4EC;--sand:#E6C89B;--drift:#A67C64;--coral:#FF8A5C;--gold:#FDB15D;--pink:#F7A7A1;--ocean:#7BA7B6}
*{box-sizing:border-box;margin:0;padding:0}
body{background:#ddd6cc;font-family:Montserrat,sans-serif;padding:40px;display:flex;flex-wrap:wrap;gap:40px;align-items:flex-start}
.tpl{position:relative;width:1080px;height:1350px;overflow:hidden;flex:none;background:var(--cream);color:var(--ink);font-variant-numeric:lining-nums}
.tpl.story{height:1920px}
.serif{font-family:'Cormorant Garamond',serif;font-weight:500}
.it{font-family:'Cormorant Garamond',serif;font-style:italic;font-weight:400;color:var(--drift)}
.caps{font-weight:500;font-size:22px;letter-spacing:.42em;text-transform:uppercase;color:var(--drift)}
.center{text-align:center}
.hair{height:1px;background:var(--drift);opacity:.45}
.foot{position:absolute;left:72px;right:72px;bottom:54px;display:flex;justify-content:space-between;align-items:center}
.foot .caps{font-size:18px;letter-spacing:.36em}
.logo{display:block}
.dot{display:inline-block;width:14px;height:14px;border-radius:50%;background:var(--coral)}
/* photo slides */
.ph{position:absolute;left:72px;top:72px;width:936px;height:830px;object-fit:cover}
.txt{position:absolute;left:72px;right:72px;top:950px}
.txt h2{font-family:'Cormorant Garamond',serif;font-weight:500;font-size:66px;line-height:1.05;margin-top:16px}
.txt p{font-size:28px;line-height:1.6;margin-top:16px;max-width:860px;opacity:.85}
/* cover */
.cover .logo{position:absolute;left:50%;transform:translateX(-50%);top:40px;width:240px}
.cover .ph{top:190px;height:800px}
.cover .txt{top:1030px}
.cover h1{font-family:'Cormorant Garamond',serif;font-weight:500;font-size:92px;line-height:1;margin-top:14px}
.cover .it{font-size:38px;margin-top:10px}
/* facts / CTA */
.facts .logo{position:absolute;left:50%;transform:translateX(-50%);top:90px;width:260px}
.facts .head{position:absolute;left:72px;right:72px;top:300px}
.facts h2{font-family:'Cormorant Garamond',serif;font-weight:500;font-size:82px;line-height:1;margin-top:18px}
.facts ul{position:absolute;left:150px;right:150px;top:470px;list-style:none;border-top:1px solid rgba(166,124,100,.4)}
.facts li{font-size:30px;line-height:1.3;padding:25px 0;border-bottom:1px solid rgba(166,124,100,.4);text-align:center}
.cta{position:absolute;left:72px;right:72px;bottom:150px;text-align:center}
.cta .wa{font-family:'Cormorant Garamond',serif;font-weight:500;font-size:58px;margin-top:14px}
.cta .wa span{color:var(--drift);font-style:italic;font-weight:400}
/* senja */
.sun-wrap{position:absolute;left:0;right:0;height:200px;overflow:hidden}
.sun{position:absolute;left:50%;transform:translateX(-50%);border-radius:50%;background:linear-gradient(180deg,var(--gold),var(--coral))}
.horizon{position:absolute;left:180px;right:180px;height:1px;background:var(--drift);opacity:.6}
.refl{position:absolute;left:50%;transform:translateX(-50%);height:2px;border-radius:2px;background:var(--ocean)}
.time{font-family:'Cormorant Garamond',serif;font-weight:500;line-height:1;letter-spacing:-.01em;font-variant-numeric:lining-nums}
"""
FONTS = '<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500&family=Montserrat:wght@400;500;600&display=swap" rel="stylesheet">'

def foot(left, right):
    return f'<div class="foot"><span class="caps">{left}</span><span class="caps">{right}</span></div>'

def sun_block(top, d, story=False):
    h = d//2
    s = f'<div class="sun-wrap" style="top:{top}px;height:{h}px"><div class="sun" style="width:{d}px;height:{d}px;top:0"></div></div>'
    s += f'<div class="horizon" style="top:{top+h}px"></div>'
    for i,(w,o) in enumerate([(int(d*.62),.9),(int(d*.4),.65),(int(d*.2),.45)]):
        s += f'<div class="refl" style="top:{top+h+26+i*24}px;width:{w}px;opacity:{o}"></div>'
    return s

parts = []
# 1. #SenjaHariIni
parts.append(f'''<div class="tpl" id="feed-senja">
  <div class="caps center" style="position:absolute;left:0;right:0;top:120px">#SenjaHariIni</div>
  {sun_block(250, 330)}
  <div class="center" style="position:absolute;left:0;right:0;top:530px">
    <div class="time" style="font-size:210px">{SENJA["time"]}</div>
    <div class="caps" style="margin-top:22px">W I T A</div>
    <div class="it" style="font-size:50px;margin-top:40px">Tempat senja pulang</div>
    <div class="hair" style="width:80px;margin:44px auto 0"></div>
    <div class="caps" style="margin-top:34px;font-size:20px">{e(SENJA["date"])} · {e(SENJA["place"])}</div>
  </div>
  <img class="logo" src="{LOGO}" style="position:absolute;left:50%;transform:translateX(-50%);bottom:70px;width:230px" alt="">
</div>''')
# 2. promo
items = "".join(f"<li>{e(i)}</li>" for i in PROMO["items"])
parts.append(f'''<div class="tpl facts" id="feed-promo">
  <img class="logo" src="{LOGO}" alt="">
  <div class="head center"><span class="dot"></span>
    <div class="caps" style="margin-top:22px">{e(PROMO["kicker"])}</div>
    <h2 style="font-size:104px">{e(PROMO["title"])} <span class="it" style="font-size:104px">{e(PROMO["title_it"])}</span></h2>
    <div class="it" style="font-size:38px;margin-top:14px">{e(PROMO["sub"])}</div>
  </div>
  <ul style="top:600px">{items}</ul>
  <div class="cta"><div class="caps">Info &amp; Reservasi</div><div class="wa"><span>WhatsApp</span> {WA}</div></div>
  {foot("SunaRi · Selayar","Beach Resort")}
</div>''')
# 3. quote
parts.append(f'''<div class="tpl" id="feed-quote">
  <div style="position:absolute;inset:48px;border:1px solid rgba(166,124,100,.45)"></div>
  <div class="center" style="position:absolute;left:110px;right:110px;top:380px">
    <span class="dot"></span>
    <div class="serif" style="font-size:84px;line-height:1.12;margin-top:56px">{QUOTE["text"].replace("<em>","<em class='it' style='font-size:84px'>")}</div>
    <div class="hair" style="width:80px;margin:56px auto 0"></div>
    <div class="caps" style="margin-top:36px">{e(QUOTE["en"])}</div>
  </div>
  <img class="logo" src="{LOGO}" style="position:absolute;left:50%;transform:translateX(-50%);bottom:110px;width:250px" alt="">
</div>''')
# 4. story
parts.append(f'''<div class="tpl story" id="story-senja">
  <img class="logo" src="{LOGO}" style="position:absolute;left:50%;transform:translateX(-50%);top:150px;width:300px" alt="">
  <div class="caps center" style="position:absolute;left:0;right:0;top:470px;font-size:28px">Senja hari ini</div>
  {sun_block(590, 420)}
  <div class="center" style="position:absolute;left:0;right:0;top:960px">
    <div class="time" style="font-size:280px">{SENJA["time"]}</div>
    <div class="caps" style="margin-top:26px;font-size:28px">W I T A</div>
    <div class="it" style="font-size:58px;margin-top:46px">Sampai jumpa di tepi pantai</div>
  </div>
  <div class="caps center" style="position:absolute;left:50%;transform:translateX(-50%);bottom:200px;border:1px dashed rgba(166,124,100,.6);padding:28px 56px;font-size:20px;white-space:nowrap">Tempel stiker / link di sini</div>
</div>''')
# carousels
for r in ROOMS:
    n = len(r["slides"]) + 2
    p = f'../assets/photos/{r["photos"]}/'
    parts.append(f'''<div class="tpl cover" id="{r["prefix"]}-1">
  <img class="logo" src="{LOGO}" alt="">
  <img class="ph" src="{p}{r["cover"]}" style="object-position:{r["cover_pos"]}" alt="">
  <div class="txt"><div class="caps">Room Tour</div><h1>{e(r["name"])}</h1><div class="it">{e(r["tagline"])}</div></div>
  {foot("SunaRi · Selayar","Geser &nbsp;→")}
</div>''')
    for i,(img,pos,h,t) in enumerate(r["slides"], start=2):
        parts.append(f'''<div class="tpl" id="{r["prefix"]}-{i}">
  <img class="ph" src="{p}{img}" style="object-position:{pos}" alt="">
  <div class="txt"><div class="caps">{e(r["name"])}</div><h2>{e(h)}</h2><p>{e(t)}</p></div>
  {foot("SunaRi · Selayar", f"{i:02d} — {n:02d}")}
</div>''')
    facts = "".join(f"<li>{e(f)}</li>" for f in r["facts"])
    parts.append(f'''<div class="tpl facts" id="{r["prefix"]}-{n}">
  <img class="logo" src="{LOGO}" alt="">
  <div class="head center"><div class="caps">{e(r["name"])}</div><h2>Yang kamu <span class="it" style="font-size:82px">dapatkan</span></h2></div>
  <ul>{facts}</ul>
  <div class="cta"><div class="caps">Info &amp; Reservasi</div><div class="wa"><span>WhatsApp</span> {WA}</div></div>
  {foot("SunaRi · Selayar", f"{n:02d} — {n:02d}")}
</div>''')

out = f'<!doctype html><html lang="id"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>SunaRi Instagram Kit</title>{FONTS}<style>{CSS}</style></head><body>\n' + "\n".join(parts) + "\n</body></html>\n"
(HERE / "kit.html").write_text(out)

GRID = ["carousel/vp-1","feed-senja","carousel/sb-1","feed-quote","carousel/vp-3","feed-promo","carousel/st-1","carousel/sb-6","carousel/sb-3"]
tiles = "".join(f'<img src="{g}.png" alt="">' for g in GRID)
grid = f'''<!doctype html><html lang="id"><head><meta charset="utf-8"><title>SunaRi Grid Preview</title>{FONTS}<style>
*{{box-sizing:border-box;margin:0;padding:0}} body{{background:#ddd6cc;padding:40px;font-family:Montserrat,sans-serif}}
#grid-preview{{width:1080px;background:#fff;color:#262626;padding:56px 0 0}}
.prof{{display:flex;gap:56px;align-items:center;padding:0 56px 44px}}
.av{{width:200px;height:200px;border-radius:50%;background:#FBF4EC;border:2px solid #E6C89B;display:flex;align-items:center;justify-content:center;flex:none}}
.av img{{width:170px}}
.user{{font-size:34px;font-weight:600}} .name{{font-size:26px;font-weight:600;margin-top:18px}}
.bio{{font-size:25px;line-height:1.5;margin-top:6px;white-space:pre-line}}
.bio a{{color:#00376b;font-weight:500}}
.tabs{{border-top:1px solid #dbdbdb;height:70px}}
.g{{display:grid;grid-template-columns:repeat(3,1fr);gap:4px}} .g img{{width:100%;aspect-ratio:4/5;object-fit:cover;display:block}}
</style></head><body><div id="grid-preview">
<div class="prof"><div class="av"><img src="../assets/logo-sunari-driftwood.png" alt=""></div>
<div><div class="user">sunari.selayar</div><div class="name">SunaRi Beach Resort Selayar</div>
<div class="bio">🌅 Tempat senja pulang
🌴 Resort tepi pantai di Kepulauan Selayar
🥥 Kelapa muda setiap sore
📩 WA {WA} ⬇️
<a>wa.me/6282189033044</a></div></div></div>
<div class="tabs"></div><div class="g">{tiles}</div></div></body></html>'''
(HERE / "grid.html").write_text(grid)
print("wrote", HERE / "kit.html", len(parts), "templates")
