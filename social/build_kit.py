"""Generate kit.html (all Instagram templates) and grid.html (profile preview).
Style: minimalist-elegant brand board look (Playfair Display + Montserrat, Sunset Beach palette).
Edit the CONTENT section, then run:  python3 social/build_kit.py && node social/render.js
"""
import html, pathlib
HERE = pathlib.Path(__file__).parent
WA = "0821-8903-3044"
SENJA = dict(time="17.57", date="Kamis, 19 November 2026", place="Pantai Sunari",
             photo="senja/19-pantai-di-bawah-daun.jpg", story_photo="senja/12-kayak-matahari-merah-story.jpg")

# ---------------------------------------------------------------- CONTENT
ROOMS = [
  dict(prefix="sb", name="Superior Bungalow", photos="superior-bungalow",
       tagline="Rumah kayu di antara pohon kelapa", cover="02-eksterior-depan.jpg", cover_pos="50% 30%",
       slides=[("03-teras.jpg","50% 50%","Teras kayu pribadi","Tempat terbaik untuk kopi pagi dan obrolan sore, dengan pohon kelapa sebagai pemandangannya."),
               ("04-kamar-loteng.jpg","50% 50%","Atap A-frame & loteng","Langit-langit kayu menjulang dengan loteng di atasnya. Lapang, sejuk, dan hangat."),
               ("05-kamar-tempat-tidur.jpg","50% 50%","King bed & kamar lebih luas","Lebih lapang dari Standard dan VIP Standard, dengan TV dan tirai blackout."),
               ("10-kamar-mandi-taman.jpg","50% 60%","Kamar mandi semi-outdoor","Mandi di bawah rain shower, ditemani taman hijau dan langit terbuka.")],
       facts=["Untuk 2 orang, maks. 3 dengan extra bed","Termasuk sarapan","King bed, TV, kamar lebih luas","Kamar mandi semi-outdoor, rain shower","AC, Wi-Fi, kopi/teh & pemanas air","Teras pribadi dengan kursi santai"]),
  dict(prefix="st", name="Standard Bungalow", photos="standard-bungalow",
       tagline="Pagi menghadap laut Selayar", cover="01-teras-view-laut.jpg", cover_pos="50% 60%",
       slides=[("03-kamar-depan.jpg","50% 60%","Queen bed di rumah kayu","Dinding kayu, atap tinggi, tirai blackout, serta bantal dan selimut tambahan."),
               ("02-kamar-sudut.jpg","50% 55%","Sejuk sepanjang hari","Kamar ber-AC dan Wi-Fi, dengan set kopi/teh dan pemanas air."),
               ("04-kamar-mandi-bambu.jpg","50% 50%","Kamar mandi nuansa bambu","Shower dan toilet duduk, lengkap dengan perlengkapan mandi dan handuk.")],
       facts=["Untuk 2 orang, maks. 3 dengan extra bed","Termasuk sarapan","Queen bed, AC & Wi-Fi","Teras pribadi menghadap laut","Kopi/teh, perlengkapan mandi & handuk"]),
  dict(prefix="vs", name="VIP Superior Bungalow", photos="vip-superior-bungalow",
       tagline="Berendam di bawah langit terbuka", cover="01-eksterior-a-frame.jpg", cover_pos="40% 50%",
       slides=[("02-teras.jpg","50% 60%","Teras kayu yang teduh","Dua kursi, satu meja, dan rimbun tanaman tropis. Tempat pas untuk kopi sore."),
               ("04-kamar-tempat-tidur.jpg","50% 55%","Atap A-frame yang lapang","Langit-langit tinggi dengan jendela segitiga yang membiarkan cahaya pagi masuk."),
               ("05-kamar-dari-loteng.jpg","50% 50%","Lihat dari loteng","Pintu kaca terbuka langsung ke teras dan taman."),
               ("06-bathtub-semi-outdoor.jpg","50% 55%","Bathtub semi-outdoor","Berendam atau mandi rain shower di bawah atap kaca, dengan pohon kelapa di atas kepala.")],
       facts=["Untuk 2 orang, maks. 3 dengan extra bed","Bungalow A-frame dengan loteng","Teras kayu pribadi","Bathtub & rain shower semi-outdoor","AC, TV, Wi-Fi, kulkas mini, kopi & teh"]),
  dict(prefix="fs", name="Family Superior Bungalow", photos="family-superior-bungalow",
       tagline="Satu rumah, dua lantai, semua bersama", cover="01-eksterior-taman.jpg", cover_pos="55% 50%",
       slides=[("03-teras-sofa.jpg","50% 55%","Teras pribadi untuk berkumpul","Sofa kayu yang lega di antara pohon kelapa. Tempat ngobrol sambil menunggu senja."),
               ("06-kamar-bawah-sudut.jpg","50% 50%","Lantai 1 untuk 2–3 orang","Tempat tidur besar, tirai blackout, meja rias, dan set kopi/teh dengan pemanas air."),
               ("09-lantai-atas-4-kasur.jpg","50% 50%","Lantai 2 untuk 4–5 orang","Ruang luas di bawah atap kayu tinggi, dengan empat kasur berjajar."),
               ("12-kamar-mandi-shower.jpg","50% 50%","Kamar mandi di kedua lantai","Perlengkapan mandi lengkap dan handuk bersih untuk setiap tamu.")],
       facts=["Untuk 6 orang, maks. 8 dengan 2 extra bed","Tipe bungalow terbesar, 2 lantai","Kamar mandi di lantai 1 & lantai 2","Termasuk sarapan","AC, Wi-Fi, kopi & teh, tirai blackout","Teras pribadi dengan kursi santai"]),
  dict(prefix="vp", name="VIP Standard Bungalow", photos="vip-standard-bungalow",
       tagline="Turun tangga, langsung pasir", cover="02-teras-view-pantai.jpg", cover_pos="50% 60%",
       slides=[("01-eksterior-rumah-panggung.jpg","50% 45%","Rumah panggung beratap rumbia","Berdiri di tepi pantai, dinaungi pohon kelapa, dengan atap lengkung tradisional."),
               ("04-teras-view-laut.jpg","60% 50%","Teras pribadi menghadap senja","Perahu nelayan lewat di kejauhan, dan matahari terbenam tepat di depan mata."),
               ("07-kamar-samping.jpg","50% 50%","King bed, kamar lebih luas","Kayu dari lantai sampai atap, lampu dinding temaram, dan tirai blackout."),
               ("10-kamar-mandi-shower.jpg","50% 40%","Kamar mandi dalam","Kamar mandi luas dengan shower, perlengkapan mandi, dan handuk bersih.")],
       facts=["Untuk 2 orang, maks. 3 dengan extra bed","Termasuk sarapan","King bed, lebih luas dari Standard","Rumah panggung di tepi pantai","AC, Wi-Fi, kopi/teh & pemanas air","Perlengkapan mandi & handuk"]),
]
# Campaign tiles: full-bleed photo + stacked serif phrase (lines), position of text: "top" or "bottom"
CAMPAIGN = [
  dict(id="camp-1", photo="senja/08-meja-di-bawah-pohon.jpg", pos="50% 60%", lines=["Lebih dari", "Menginap.", "<i>Sebuah Rasa.</i>"], where="top"),
  dict(id="camp-2", photo="senja/15-dua-kayak-oranye.jpg", pos="50% 70%", lines=["Menginap.", "Menjelajah.", "Melambat.", "<i>Pulang.</i>"], where="top"),
  dict(id="camp-3", photo="senja/04-pasangan-tripod.jpg", pos="50% 70%", lines=["Pantai Sepi.", "Senja Hangat.", "<i>Hati Tenang.</i>"], where="top"),
]
VALUES = [("wave","Tepi Pantai"),("sun","Menghadap Senja"),("leaf","Alami & Lokal"),("moon","Tenang & Pelan")]
PROMO = dict(kicker="Paket Akhir Pekan", title="Staycation", title_it="Senja", sub="Dua malam, dua kali senja",
             items=["Superior Bungalow kayu A-frame","Senja Dinner ikan bakar & seafood untuk dua orang","Teras pribadi untuk menunggu senja"])
QUOTE = dict(text="Setiap hari di Selayar<br>berakhir dengan <em>indah.</em>", en="Where every day ends beautifully")
# Feed order shown in grid-preview.png (newest first)
GRID = ["camp-1","feed-senja","carousel/vs-1","camp-3","carousel/vp-1","feed-quote","camp-2","feed-promo","carousel/fs-1"]
# ---------------------------------------------------------------- END CONTENT

e = html.escape
LOGO = "../assets/logo-sunari-driftwood.png"
LOGO_C = "../assets/logo-sunari-cream.png"
MARK = "../assets/mark-sunari-driftwood.svg"
ICONS = {
 "wave": '<path d="M8 30 q8 -7 16 0 t16 0 t16 0"/><path d="M8 42 q8 -7 16 0 t16 0 t16 0"/>',
 "sun":  '<path d="M16 38 a16 16 0 0 1 32 0"/><line x1="8" y1="38" x2="56" y2="38"/><line x1="32" y1="12" x2="32" y2="16"/><line x1="14" y1="20" x2="17" y2="23"/><line x1="50" y1="20" x2="47" y2="23"/><line x1="20" y1="46" x2="44" y2="46"/>',
 "leaf": '<path d="M16 48 C16 26 30 14 50 14 C50 34 38 48 16 48 Z"/><path d="M16 48 L40 24"/>',
 "moon": '<path d="M40 14 a18 18 0 1 0 10 30 a14 14 0 1 1 -10 -30 Z"/>',
}
def icon(k, color="currentColor", size=64):
    return f'<svg viewBox="0 0 64 64" width="{size}" height="{size}" fill="none" stroke="{color}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">{ICONS[k]}</svg>'

CSS = """
:root{--ink:#5A3E31;--cream:#FBF4EC;--sand:#E6C89B;--drift:#A67C64;--coral:#FF8A5C;--gold:#FDB15D;--pink:#F7A7A1;--ocean:#7BA7B6}
*{box-sizing:border-box;margin:0;padding:0}
body{background:#ddd6cc;font-family:Montserrat,sans-serif;padding:40px;display:flex;flex-wrap:wrap;gap:40px;align-items:flex-start}
.tpl{position:relative;width:1080px;height:1350px;overflow:hidden;flex:none;background:var(--cream);color:var(--ink);font-variant-numeric:lining-nums}
.tpl.story{height:1920px}
.pf{font-family:'Playfair Display',serif;font-weight:400}
.it{font-family:'Playfair Display',serif;font-style:italic;font-weight:400;color:var(--drift)}
.caps{font-weight:500;font-size:22px;letter-spacing:.38em;text-transform:uppercase;color:var(--drift)}
.center{text-align:center}
.hair{height:1px;background:var(--drift);opacity:.45}
.foot{position:absolute;left:72px;right:72px;bottom:54px;display:flex;justify-content:space-between;align-items:center}
.foot .caps{font-size:18px;letter-spacing:.34em}
.dot{display:inline-block;width:14px;height:14px;border-radius:50%;background:var(--coral)}
/* full-bleed photo tiles */
.bleed{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.veil-top{position:absolute;left:0;right:0;top:0;height:62%;background:linear-gradient(180deg,rgba(40,26,20,.62),rgba(40,26,20,0))}
.veil-bot{position:absolute;left:0;right:0;bottom:0;height:34%;background:linear-gradient(0deg,rgba(40,26,20,.5),rgba(40,26,20,0))}
.on-photo{color:var(--cream)} .on-photo .caps{color:var(--cream);opacity:.9} .on-photo .it{color:var(--cream)}
.stack{position:absolute;left:84px;top:96px;font-family:'Playfair Display',serif;font-size:96px;line-height:1.08;color:var(--cream);text-shadow:0 2px 24px rgba(30,18,12,.45)}
.stack i{font-style:italic}
/* framed photo slides */
.ph{position:absolute;left:72px;top:72px;width:936px;height:830px;object-fit:cover}
.txt{position:absolute;left:72px;right:72px;top:950px}
.txt h2{font-family:'Playfair Display',serif;font-weight:400;font-size:58px;line-height:1.1;margin-top:16px}
.txt p{font-size:28px;line-height:1.6;margin-top:16px;max-width:880px;opacity:.85}
/* cover (full-bleed) */
.cover .head{position:absolute;left:84px;right:84px;top:96px;text-shadow:0 2px 20px rgba(30,18,12,.45)}
.cover h1{font-family:'Playfair Display',serif;font-weight:400;font-size:88px;line-height:1.02;margin-top:18px}
.cover .it{font-size:40px;margin-top:16px}
.cover .logo{position:absolute;right:72px;bottom:44px;width:250px}
/* facts / CTA */
.facts .mark{position:absolute;left:50%;transform:translateX(-50%);top:90px;width:120px}
.facts .head{position:absolute;left:72px;right:72px;top:270px}
.facts h2{font-family:'Playfair Display',serif;font-weight:400;font-size:70px;line-height:1.05;margin-top:18px}
.facts ul{position:absolute;left:150px;right:150px;top:450px;list-style:none;border-top:1px solid rgba(166,124,100,.4)}
.facts li{font-size:30px;line-height:1.3;padding:25px 0;border-bottom:1px solid rgba(166,124,100,.4);text-align:center}
.cta{position:absolute;left:72px;right:72px;bottom:150px;text-align:center}
.cta .wa{font-family:'Playfair Display',serif;font-size:52px;margin-top:14px}
.cta .wa span{color:var(--drift);font-style:italic}
/* senja */
.sun-wrap{position:absolute;left:0;right:0;overflow:hidden}
.sun{position:absolute;left:50%;transform:translateX(-50%);border-radius:50%;background:linear-gradient(180deg,var(--gold),var(--coral))}
.horizon{position:absolute;left:180px;right:180px;height:1px;background:var(--drift);opacity:.6}
.refl{position:absolute;left:50%;transform:translateX(-50%);height:2px;border-radius:2px;background:var(--ocean)}
.time{font-family:'Playfair Display',serif;font-weight:400;line-height:1}
/* values */
.vals{position:absolute;left:72px;right:72px;top:640px;display:grid;grid-template-columns:repeat(2,1fr);gap:70px 40px}
.val{text-align:center;color:var(--drift)}
.val .ring{width:150px;height:150px;border:1.5px solid var(--drift);border-radius:50%;margin:0 auto;display:flex;align-items:center;justify-content:center}
.val .caps{margin-top:26px;font-size:20px}
"""
FONTS = '<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;1,400&family=Montserrat:wght@400;500;600&display=swap" rel="stylesheet">'

def foot(left, right, photo=False):
    c = ' style="color:var(--cream);opacity:.9"' if photo else ''
    return f'<div class="foot"><span class="caps"{c}>{left}</span><span class="caps"{c}>{right}</span></div>'

def sun_block(top, d):
    h = d//2
    s = f'<div class="sun-wrap" style="top:{top}px;height:{h}px"><div class="sun" style="width:{d}px;height:{d}px;top:0"></div></div>'
    s += f'<div class="horizon" style="top:{top+h}px"></div>'
    for i,(w,o) in enumerate([(int(d*.62),.9),(int(d*.4),.65),(int(d*.2),.45)]):
        s += f'<div class="refl" style="top:{top+h+26+i*24}px;width:{w}px;opacity:{o}"></div>'
    return s

parts = []
# campaign tiles
for c in CAMPAIGN:
    lines = "<br>".join(c["lines"])
    parts.append(f'''<div class="tpl" id="{c["id"]}">
  <img class="bleed" src="../assets/photos/{c["photo"]}" style="object-position:{c["pos"]}" alt="">
  <div class="veil-top"></div><div class="veil-bot"></div>
  <div class="stack">{lines}</div>
  <img src="{LOGO_C}" style="position:absolute;right:66px;bottom:44px;width:250px" alt="">
  <div class="foot" style="right:auto"><span class="caps" style="color:var(--cream);opacity:.9">SunaRi · Selayar</span></div>
</div>''')
# kayak tile (prices allowed)
parts.append(f'''<div class="tpl on-photo" id="feed-kayak">
  <img class="bleed" src="../assets/photos/senja/03-kayak-matahari-merah.jpg" style="object-position:50% 40%" alt="">
  <div class="veil-top"></div>
  <div class="veil-bot" style="height:46%;background:linear-gradient(0deg,rgba(40,26,20,.78),rgba(40,26,20,0))"></div>
  <div class="stack" style="top:330px">Mendayung<br>menuju <i>senja.</i></div>
  <div style="position:absolute;left:84px;right:84px;bottom:150px;color:var(--cream)">
    <div class="caps" style="color:var(--cream)">Sewa Kayak · Pantai Sunari</div>
    <div style="display:flex;gap:70px;margin-top:22px;font-family:'Playfair Display',serif;font-size:50px">
      <div>Single <span style="color:var(--gold)">Rp 50.000</span></div>
      <div>Double <span style="color:var(--gold)">Rp 100.000</span></div>
    </div>
  </div>
  <img src="{LOGO_C}" style="position:absolute;right:66px;bottom:44px;width:230px" alt="">
  <div class="foot" style="right:auto"><span class="caps" style="color:var(--cream);opacity:.9">WA {WA}</span></div>
</div>''')
# values tile
vals = "".join(f'<div class="val"><div class="ring">{icon(k,"#A67C64",72)}</div><div class="caps">{e(l)}</div></div>' for k,l in VALUES)
parts.append(f'''<div class="tpl" id="feed-values">
  <img src="{MARK}" style="position:absolute;left:50%;transform:translateX(-50%);top:110px;width:130px" alt="">
  <div class="center" style="position:absolute;left:72px;right:72px;top:300px">
    <div class="caps">SunaRi Beach Resort</div>
    <div class="pf" style="font-size:72px;line-height:1.1;margin-top:20px">Tempat senja <span class="it">pulang.</span></div>
  </div>
  <div class="hair" style="position:absolute;left:470px;width:140px;top:560px"></div>
  <div class="vals">{vals}</div>
  {foot("SunaRi · Selayar","Kepulauan Selayar")}
</div>''')
# #SenjaHariIni (real photo, framed)
parts.append(f'''<div class="tpl" id="feed-senja">
  <img class="ph" src="../assets/photos/{SENJA["photo"]}" style="height:820px;object-position:50% 62%" alt="">
  <div style="position:absolute;left:72px;right:72px;top:940px;display:flex;justify-content:space-between;align-items:flex-end">
    <div><div class="caps">#SenjaHariIni</div>
      <div class="time" style="font-size:150px;margin-top:10px">{SENJA["time"]}<span class="caps" style="font-size:24px;margin-left:18px">WITA</span></div></div>
    <img src="{MARK}" style="width:110px;margin-bottom:20px" alt="">
  </div>
  <div class="hair" style="position:absolute;left:72px;right:72px;top:1190px"></div>
  {foot(e(SENJA["date"]), e(SENJA["place"]))}
</div>''')
# promo
items = "".join(f"<li>{e(i)}</li>" for i in PROMO["items"])
parts.append(f'''<div class="tpl facts" id="feed-promo">
  <img class="mark" src="{MARK}" alt="">
  <div class="head center"><div class="caps">{e(PROMO["kicker"])}</div>
    <h2 style="font-size:92px">{e(PROMO["title"])} <span class="it">{e(PROMO["title_it"])}</span></h2>
    <div class="it" style="font-size:36px;margin-top:14px">{e(PROMO["sub"])}</div>
  </div>
  <ul style="top:580px">{items}</ul>
  <div class="cta"><div class="caps">Info &amp; Reservasi</div><div class="wa"><span>WhatsApp</span> {WA}</div></div>
  {foot("SunaRi · Selayar","Beach Resort")}
</div>''')
# quote
parts.append(f'''<div class="tpl" id="feed-quote" style="background:var(--sand)">
  <div style="position:absolute;inset:48px;border:1px solid rgba(90,62,49,.35)"></div>
  <div class="center" style="position:absolute;left:110px;right:110px;top:360px">
    <img src="{MARK}" style="width:110px" alt="">
    <div class="pf" style="font-size:72px;line-height:1.18;margin-top:50px">{QUOTE["text"].replace("<em>","<em class='it' style='color:var(--ink)'>")}</div>
    <div class="hair" style="width:80px;margin:56px auto 0;background:var(--ink);opacity:.4"></div>
    <div class="caps" style="margin-top:36px;color:var(--ink)">{e(QUOTE["en"])}</div>
  </div>
  <div class="caps center" style="position:absolute;left:0;right:0;bottom:110px;color:var(--ink);font-size:18px">SunaRi Beach Resort · Selayar</div>
</div>''')
# story (real photo, full-bleed)
parts.append(f'''<div class="tpl story on-photo" id="story-senja">
  <img class="bleed" src="../assets/photos/{SENJA["story_photo"]}" alt="">
  <div class="veil-top" style="height:45%"></div><div class="veil-bot"></div>
  <img src="{LOGO_C}" style="position:absolute;left:50%;transform:translateX(-50%);top:110px;width:300px" alt="">
  <div class="center" style="position:absolute;left:0;right:0;top:330px;text-shadow:0 2px 20px rgba(30,18,12,.45)">
    <div class="caps" style="font-size:26px;color:var(--cream)">Senja hari ini</div>
    <div class="time" style="font-size:190px;margin-top:10px;color:var(--cream)">{SENJA["time"]}</div>
    <div class="caps" style="font-size:26px;color:var(--cream)">W I T A</div>
  </div>
  <div class="caps center" style="position:absolute;left:50%;transform:translateX(-50%);bottom:200px;border:1px dashed rgba(251,244,236,.7);padding:28px 56px;font-size:20px;white-space:nowrap;color:var(--cream)">Tempel stiker / link di sini</div>
</div>''')
# carousels
for r in ROOMS:
    n = len(r["slides"]) + 2
    p = f'../assets/photos/{r["photos"]}/'
    parts.append(f'''<div class="tpl cover on-photo" id="{r["prefix"]}-1">
  <img class="bleed" src="{p}{r["cover"]}" style="object-position:{r["cover_pos"]}" alt="">
  <div class="veil-top"></div><div class="veil-bot"></div>
  <div class="head"><div class="caps">Room Tour</div><h1>{e(r["name"])}</h1><div class="it">{e(r["tagline"])}</div></div>
  <img class="logo" src="{LOGO_C}" alt="">
  <div class="foot" style="right:auto"><span class="caps" style="color:var(--cream);opacity:.9">Geser &nbsp;→</span></div>
</div>''')
    for i,(img,pos,h,t) in enumerate(r["slides"], start=2):
        parts.append(f'''<div class="tpl" id="{r["prefix"]}-{i}">
  <img class="ph" src="{p}{img}" style="object-position:{pos}" alt="">
  <div class="txt"><div class="caps">{e(r["name"])}</div><h2>{e(h)}</h2><p>{e(t)}</p></div>
  {foot("SunaRi · Selayar", f"{i:02d} — {n:02d}")}
</div>''')
    facts = "".join(f"<li>{e(f)}</li>" for f in r["facts"])
    parts.append(f'''<div class="tpl facts" id="{r["prefix"]}-{n}">
  <img class="mark" src="{MARK}" alt="">
  <div class="head center"><div class="caps">{e(r["name"])}</div><h2>Yang kamu <span class="it">dapatkan</span></h2></div>
  <ul>{facts}</ul>
  <div class="cta"><div class="caps">Info &amp; Reservasi</div><div class="wa"><span>WhatsApp</span> {WA}</div></div>
  {foot("SunaRi · Selayar", f"{n:02d} — {n:02d}")}
</div>''')

head = f'<!doctype html><html lang="id"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>SunaRi Instagram Kit</title>{FONTS}<style>{CSS}</style></head><body>\n'
(HERE / "kit.html").write_text(head + "\n".join(parts) + "\n</body></html>\n")

tiles = "".join(f'<img src="{g}.png" alt="">' for g in GRID)
grid = f'''<!doctype html><html lang="id"><head><meta charset="utf-8"><title>SunaRi Grid Preview</title>{FONTS}<style>
*{{box-sizing:border-box;margin:0;padding:0}} body{{background:#ddd6cc;padding:40px;font-family:Montserrat,sans-serif}}
#grid-preview{{width:1080px;background:#fff;color:#262626;padding:56px 0 0}}
.prof{{display:flex;gap:56px;align-items:center;padding:0 56px 44px}}
.av{{width:200px;height:200px;border-radius:50%;background:#FBF4EC;border:2px solid #E6C89B;display:flex;align-items:center;justify-content:center;flex:none}}
.av img{{width:130px}}
.user{{font-size:34px;font-weight:600}} .name{{font-size:26px;font-weight:600;margin-top:18px}}
.bio{{font-size:25px;line-height:1.5;margin-top:6px;white-space:pre-line}} .bio a{{color:#00376b;font-weight:500}}
.tabs{{border-top:1px solid #dbdbdb;height:70px}}
.g{{display:grid;grid-template-columns:repeat(3,1fr);gap:4px}} .g img{{width:100%;aspect-ratio:4/5;object-fit:cover;display:block}}
</style></head><body><div id="grid-preview">
<div class="prof"><div class="av"><img src="../assets/mark-sunari-driftwood.svg" alt=""></div>
<div><div class="user">sunaribeachresortselayar</div><div class="name">SunaRi Beach Resort Selayar</div>
<div class="bio">🌅 Tempat senja pulang
🌴 Resort tepi pantai di Kepulauan Selayar
🍽️ Senja Dinner ikan bakar & seafood
📩 WA {WA} ⬇️
<a>wa.me/6282189033044</a></div></div></div>
<div class="tabs"></div><div class="g">{tiles}</div></div></body></html>'''
(HERE / "grid.html").write_text(grid)
print("wrote kit.html (%d templates) and grid.html" % len(parts))
