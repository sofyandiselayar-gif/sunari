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
               ("04-kamar-tempat-tidur.jpg","50% 55%","King bed di bawah atap A-frame","Jendela segitiga, TV, mini bar/kulkas, dan tirai blackout."),
               ("05-kamar-dari-loteng.jpg","50% 50%","Lihat dari loteng","Pintu kaca terbuka langsung ke teras dan taman."),
               ("06-bathtub-semi-outdoor.jpg","50% 55%","Bathtub & air panas","Berendam air hangat di bawah atap kaca, dengan pohon kelapa di atas kepala.")],
       facts=["Untuk 2 orang, maks. 3 dengan extra bed","Kelas tertinggi, termasuk sarapan","Bathtub & air panas","King bed, TV, mini bar/kulkas","AC, Wi-Fi, kopi/teh & pemanas air","Teras kayu pribadi dengan kursi santai"]),
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
  dict(id="camp-4", photo="malam/05-a-frame-malam.jpg", pos="50% 60%", lines=["Saat senja usai,", "lampu-lampu", "<i>menyala.</i>"], where="top"),
  dict(id="camp-5", photo="malam/09-lilin-di-meja.jpg", pos="50% 70%", lines=["Malam yang", "pelan di", "<i>Selayar.</i>"], where="top"),
]
VALUES = [("wave","Tepi Pantai"),("sun","Menghadap Senja"),("leaf","Alami & Lokal"),("moon","Tenang & Pelan")]
PROMO = dict(kicker="Paket Akhir Pekan", title="Staycation", title_it="Senja", sub="Dua malam, dua kali senja",
             items=["Superior Bungalow kayu A-frame","Senja Dinner ikan bakar & seafood untuk dua orang","Teras pribadi untuk menunggu senja"])
QUOTE = dict(text="Setiap hari di Selayar<br>berakhir dengan <em>indah.</em>", en="Where every day ends beautifully")
# Feed order shown in grid-preview.png (newest first)
GRID = ["camp-1","feed-senja","carousel/vs-1","camp-4","carousel/vp-1","feed-quote","camp-3","feed-kayak","carousel/fs-1","camp-2","feed-promo","carousel/sb-1"]
# ---------------------------------------------------------------- END CONTENT

e = html.escape
LOGO = "../assets/logo-sunari-color.png"        # full-color logo (light backgrounds)
LOGO_C = "../assets/logo-sunari-color-dark.png" # full-color logo (photos / dark backgrounds)
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
.facts .mark{position:absolute;left:50%;transform:translateX(-50%);top:56px;width:380px}
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
  <img src="{LOGO}" style="position:absolute;left:50%;transform:translateX(-50%);top:70px;width:440px" alt="">
  <div class="center" style="position:absolute;left:72px;right:72px;top:330px">
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
    <img src="{LOGO}" style="width:300px;margin-bottom:24px" alt="">
  </div>
  <div class="hair" style="position:absolute;left:72px;right:72px;top:1190px"></div>
  {foot(e(SENJA["date"]), e(SENJA["place"]))}
</div>''')
# promo
items = "".join(f"<li>{e(i)}</li>" for i in PROMO["items"])
parts.append(f'''<div class="tpl facts" id="feed-promo">
  <img class="mark" src="{LOGO}" alt="">
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
    <img src="{LOGO}" style="width:420px" alt="">
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
</div>''')
# ---- 10-day story plan (20–29 Nov 2026)
STORIES = [
  ("sd-01","Jumat, 20 Nov","17.57","senja/13-tamu-bertopi-story.jpg","50% 50%","Senja hari ini","Kursi sudah<br>menunggu.","Matahari terbenam pukul 17.57 WITA di Pantai Sunari.","Stiker: Hitung mundur 17.57"),
  ("sd-02","Sabtu, 21 Nov","17.57","senja/19-pantai-di-bawah-daun.jpg","50% 60%","Pilih satu","Tim <i>pantai</i><br>atau tim gunung?","Akhir pekan ini, kamu mau ke mana?","Stiker: Polling Pantai / Gunung"),
  ("sd-03","Minggu, 22 Nov","17.58","vip-superior-bungalow/06-bathtub-semi-outdoor.jpg","50% 50%","Tebak kamarnya","Berendam di<br>bawah <i>atap kaca.</i>","Satu-satunya kamar kami dengan bathtub & air panas.","Stiker: Kuis 4 pilihan kamar"),
  ("sd-04","Senin, 23 Nov","17.58","senja/15-dua-kayak-oranye.jpg","50% 60%","Sewa kayak","Mendayung<br>menuju <i>senja.</i>","Single Rp 50.000 · Double Rp 100.000","Stiker: Tautan WhatsApp"),
  ("sd-05","Selasa, 24 Nov","17.58","resto/04-resto-malam-pohon-kelapa.jpg","50% 70%","Bajoy Beach Resto","Makan malam<br>di bawah <i>pohon kelapa.</i>","Ikan bakar &amp; seafood. Buka 07.00–21.00 WITA.","Stiker: Lokasi SunaRi"),
  ("sd-06","Rabu, 25 Nov","17.59","senja/08-meja-di-bawah-pohon.jpg","50% 55%","Tanya kami","Mau tahu apa<br>tentang <i>SunaRi?</i>","Kamar, sarapan, antar-jemput, kayak. Tanya saja.","Stiker: Kotak pertanyaan"),
  ("sd-07","Kamis, 26 Nov","17.59","family-superior-bungalow/01-eksterior-taman.jpg","55% 50%","Family Superior","Satu rumah,<br><i>semua bersama.</i>","Untuk 6 orang (maks. 8) · 2 lantai · termasuk sarapan","Stiker: Slider emoji keluarga"),
  ("sd-08","Jumat, 27 Nov","18.00","senja/16-perahu-nelayan.jpg","50% 60%","Antar-jemput","Dari bandara,<br>langsung ke <i>pantai.</i>","Antar-jemput bandara &amp; pelabuhan (biaya tambahan).","Stiker: Tautan WhatsApp"),
  ("sd-09","Sabtu, 28 Nov","18.00","resto/05-makan-malam-taman.jpg","50% 60%","Senja Dinner","Makan malam<br>saat <i>senja.</i>","Ikan bakar &amp; seafood. Pesan H-1 via WhatsApp.","Stiker: Tautan WhatsApp"),
  ("sd-10","Minggu, 29 Nov","18.00","senja/18-kayak-berdua-pelampung.jpg","50% 60%","Sampai jumpa","Setiap hari<br>berakhir <i>indah.</i>","Senja hari ini 18.00 WITA. Kapan kamu ke sini?","Stiker: Hitung mundur / Polling"),
]
for sid, day, t, photo, pos, kicker, head, body, sticker in STORIES:
    parts.append(f"""<div class="tpl story on-photo" id="{sid}">
  <img class="bleed" src="../assets/photos/{photo}" style="object-position:{pos}" alt="">
  <div class="veil-top" style="height:{'62%;background:linear-gradient(180deg,rgba(40,26,20,.82),rgba(40,26,20,.55) 55%,rgba(40,26,20,0))' if sid in ('sd-03','sd-07') else '52%'}"></div>
  <div class="veil-bot" style="height:40%;background:linear-gradient(0deg,rgba(40,26,20,.72),rgba(40,26,20,0))"></div>
  <img src="{LOGO_C}" style="position:absolute;left:50%;transform:translateX(-50%);top:120px;width:260px" alt="">
  <div style="position:absolute;left:90px;right:90px;top:360px;text-shadow:0 2px 20px rgba(30,18,12,.45)">
    <div class="caps" style="font-size:24px;color:var(--cream)">{kicker}</div>
    <div class="pf" style="font-size:104px;line-height:1.06;margin-top:22px;color:var(--cream)">{head}</div>
    <div style="font-size:32px;line-height:1.5;margin-top:30px;color:var(--cream);max-width:820px">{body}</div>
  </div>
  <div style="position:absolute;left:90px;right:90px;bottom:150px;display:flex;justify-content:space-between;color:var(--cream)">
    <span class="caps" style="font-size:20px;color:var(--cream)">{day}</span>
    <span class="caps" style="font-size:20px;color:var(--cream)">Senja {t} WITA</span>
  </div>
</div>""")
# ---- Highlight story content (1080x1920) + FAQ carousel (1080x1350)
P_ = "../assets/photos/"
def hs(sid, group, photo, pos, title, body, extra=""):
    """Highlight story: framed photo top, text below. Keeps clear of IG top/bottom UI (~250px)."""
    ph = f'<img src="{P_}{photo}" style="position:absolute;left:72px;top:250px;width:936px;height:860px;object-fit:cover;object-position:{pos}" alt="">' if photo else ""
    top = 1170 if photo else 470
    tsize = 70 if photo else 96
    return f"""<div class="tpl story" id="{sid}">
  <div style="position:absolute;left:72px;right:72px;top:118px;display:flex;align-items:center;gap:20px">
    <img src="{LOGO}" style="width:210px" alt=""><span class="caps" style="font-size:22px;margin-left:auto">{group}</span></div>
  {ph}
  <div style="position:absolute;left:72px;right:72px;top:{top}px">
    <div class="pf" style="font-size:{tsize}px;line-height:1.1">{title}</div>
    <div style="font-size:31px;line-height:1.6;margin-top:24px">{body}</div>
    {extra}
  </div>
  <div style="position:absolute;left:72px;right:72px;bottom:230px;display:flex;justify-content:space-between">
    <span class="caps" style="font-size:19px">SunaRi · Selayar</span><span class="caps" style="font-size:19px">WA {WA}</span></div>
</div>"""
def lst(items, size=31, pad=16):
    li = "".join(f'<div style="padding:{pad}px 0;border-bottom:1px solid rgba(166,124,100,.4)">{x}</div>' for x in items)
    return f'<div style="margin-top:26px;font-size:{size}px;line-height:1.35;border-top:1px solid rgba(166,124,100,.4)">{li}</div>'
def steps(items):
    out = ""
    for n, (h, t) in enumerate(items, 1):
        out += f'''<div style="display:flex;gap:34px;margin-top:70px;align-items:flex-start">
  <div class="pf" style="flex:none;width:100px;height:100px;border-radius:50%;border:1.5px solid var(--drift);display:flex;align-items:center;justify-content:center;font-size:48px;color:var(--drift)">{n}</div>
  <div><div class="pf" style="font-size:56px">{h}</div><div style="font-size:35px;line-height:1.5;margin-top:10px;opacity:.85">{t}</div></div></div>'''
    return out

HS = [
 # SunaRi
 hs("hs-sunari-1","SunaRi","malam/03-resort-malam-a-frame.jpg","50% 60%","Selamat datang di<br>tempat senja <i class='it'>pulang.</i>",
    "Resort tepi Pantai Sunari, Kepulauan Selayar. Setiap sore, matahari terbenam tepat di depan pantai kami."),
 hs("hs-sunari-2","SunaRi","senja/19-pantai-di-bawah-daun.jpg","50% 60%","Info <i class='it'>penting</i>",
    "", lst(["Check-in 14.00 · Check-out 12.00 WITA","Sarapan termasuk di semua kamar","AC &amp; Wi-Fi di semua kamar","Pantai landai &amp; aman untuk anak"])),
 hs("hs-sunari-3","SunaRi",None,"","Fasilitas <i class='it'>kami</i>","",
    lst(["5 tipe bungalow dengan teras pribadi","Bajoy Beach Resto · 07.00–21.00 WITA","Senja Dinner · pesan H-1","Sewa kayak · single Rp 50.000 · double Rp 100.000","Antar-jemput bandara &amp; pelabuhan (berbayar)","Wi-Fi · sarapan · pantai landai"], 38, 30)),
 # Senja
 hs("hs-senja-1","Senja","senja/17-kayak-berdua.jpg","50% 60%","Senja di <i class='it'>Pantai Sunari</i>",
    "Matahari terbenam sekitar pukul 17.50–18.00 WITA. Ikuti #SenjaHariIni setiap sore di story kami."),
 # Kamar
 hs("hs-kamar-1","Kamar","vip-superior-bungalow/06-bathtub-semi-outdoor.jpg","50% 55%","VIP Superior <i class='it'>Bungalow</i>",
    "Kelas tertinggi kami.", lst(["2 orang · maks. 3 dengan extra bed","King bed · TV · mini bar/kulkas","Bathtub &amp; air panas, satu-satunya tipe dengan air panas"],29)),
 hs("hs-kamar-2","Kamar","superior-bungalow/02-eksterior-depan.jpg","50% 30%","Superior <i class='it'>Bungalow</i>",
    "Rumah kayu A-frame di antara pohon kelapa.", lst(["2 orang · maks. 3 dengan extra bed","King bed · TV · lebih luas dari Standard","Kamar mandi semi-outdoor, rain shower"],29)),
 hs("hs-kamar-3","Kamar","family-superior-bungalow/01-eksterior-taman.jpg","55% 50%","Family Superior <i class='it'>Bungalow</i>",
    "Tipe terbesar, ideal untuk keluarga.", lst(["6 orang · maks. 8 dengan 2 extra bed","2 lantai · kamar mandi di kedua lantai","Teras pribadi dengan kursi santai"],29)),
 hs("hs-kamar-4","Kamar","vip-standard-bungalow/02-teras-view-pantai.jpg","50% 60%","VIP Standard <i class='it'>Bungalow</i>",
    "Rumah panggung di tepi pantai.", lst(["2 orang · maks. 3 dengan extra bed","King bed · lebih luas dari Standard","Teras pribadi menghadap laut"],29)),
 hs("hs-kamar-5","Kamar","standard-bungalow/01-teras-view-laut.jpg","50% 60%","Standard <i class='it'>Bungalow</i>",
    "Pagi menghadap laut Selayar.", lst(["2 orang · maks. 3 dengan extra bed","Queen bed · AC · Wi-Fi","Teras pribadi luas menghadap laut"],29)),
 # Resto
 hs("hs-resto-1","Resto","resto/03-resto-malam.jpg","50% 60%","Bajoy Beach <i class='it'>Resto</i>",
    "Ikan bakar &amp; seafood setiap hari.", lst(["Buka 07.00–21.00 WITA","Tamu tidak menginap: sampai 19.00 WITA","Senja Dinner tersedia (pesan H-1)"],29)),
 hs("hs-resto-2","Resto","resto/05-makan-malam-taman.jpg","50% 60%","Senja <i class='it'>Dinner</i>",
    "Makan malam ikan bakar &amp; seafood saat matahari terbenam. Pesan paling lambat H-1 via WhatsApp."),
 # Kayak
 hs("hs-kayak-1","Kayak","aktivitas/01-kayak-sore.jpg","50% 55%","Sewa <i class='it'>kayak</i>",
    "Air Pantai Sunari tenang dan landai, paling seru menjelang senja.",
    '<div style="display:flex;gap:60px;margin-top:34px"><div><div class="caps" style="font-size:20px">Single</div><div class="pf" style="font-size:60px;margin-top:6px">Rp 50.000</div></div><div><div class="caps" style="font-size:20px">Double</div><div class="pf" style="font-size:60px;margin-top:6px">Rp 100.000</div></div></div>'),
 # Lokasi
 hs("hs-lokasi-1","Lokasi","malam/02-bangunan-utama-malam.jpg","50% 60%","Lokasi <i class='it'>kami</i>",
    "Jl. Poros Benteng – Appatana KM 14, Dusun Tile-Tile Utara, Desa Patikarya, Kec. Bontosikuyu, Kepulauan Selayar.",
    '<div class="caps" style="margin-top:30px;font-size:20px">Ketuk stiker lokasi / link Google Maps</div>'),
 hs("hs-lokasi-2","Lokasi",None,"","Cara ke <i class='it'>Selayar</i>","Dari Makassar, ada dua pilihan:",
    steps([("Pesawat","ke Bandara H. Aroeppala, Selayar"),("Darat + feri","ke Pelabuhan Bira (Bulukumba), lanjut feri ke Pamatata"),("Antar-jemput","dari bandara/pelabuhan ke SunaRi (biaya tambahan, pesan via WA)")])),
 # Ulasan
 hs("hs-ulasan-1","Ulasan","senja/04-pasangan-tripod.jpg","50% 70%","Bagikan <i class='it'>ceritamu</i>",
    "Menginap di SunaRi? Tag <b>@sunaribeachresortselayar</b> dan pakai <b>#SunaRiSelayar</b>. Kami repost favorit setiap minggu."),
 # Booking
 hs("hs-booking-1","Booking",None,"","Cara <i class='it'>reservasi</i>","",
    steps([("Kirim data","tanggal check-in &amp; check-out, jumlah tamu, tipe kamar"),("Terima penawaran","kami kirim harga &amp; ketersediaan terbaru"),("Bayar &amp; konfirmasi","kirim bukti transfer, booking terkonfirmasi")])
    + f'<div style="margin-top:110px;text-align:center"><div class="caps">WhatsApp</div><div class="pf" style="font-size:76px;margin-top:10px">{WA}</div></div>'),
 hs("hs-booking-2","Booking",None,"","Pertanyaan <i class='it'>umum</i>","",
    lst(["Check-in 14.00 · Check-out 12.00 WITA","Sarapan termasuk di semua kamar","Air panas &amp; bathtub: VIP Superior","Extra bed tersedia (biaya tambahan)","Antar-jemput bandara/pelabuhan (berbayar)","Pantai landai &amp; aman untuk anak"],38,30)),
]
parts.extend(HS)

# FAQ carousel
FAQ = [("Jam check-in &amp; check-out?","Check-in mulai 14.00 WITA, check-out paling lambat 12.00 WITA."),
       ("Sudah termasuk sarapan?","Ya, sarapan termasuk di semua tipe kamar."),
       ("Ada Wi-Fi &amp; AC?","Ada, di semua kamar."),
       ("Kamar mana yang ada air panas?","VIP Superior Bungalow, dengan bathtub di kamar mandi semi-outdoor beratap kaca."),
       ("Cocok untuk keluarga?","Family Superior untuk 6 orang (maks. 8), 2 lantai, kamar mandi di kedua lantai. Pantainya landai &amp; aman untuk anak."),
       ("Bisa tambah extra bed?","Bisa, dengan biaya tambahan: 1 untuk tipe lain, 2 untuk Family Superior."),
       ("Ada antar-jemput?","Ada, dari Bandara H. Aroeppala &amp; pelabuhan, dengan biaya tambahan."),
       ("Tamu luar boleh ke resto?","Boleh. Bajoy Beach Resto buka 07.00–21.00, tamu tidak menginap sampai 19.00 WITA.")]
NF = len(FAQ)//2 + 2
parts.append(f'''<div class="tpl cover on-photo" id="faq-1">
  <img class="bleed" src="{P_}senja/08-meja-di-bawah-pohon.jpg" style="object-position:50% 60%" alt="">
  <div class="veil-top"></div><div class="veil-bot"></div>
  <div class="head"><div class="caps">Ditanya Kakak</div><h1>Pertanyaan yang<br>sering <i>ditanya.</i></h1><div class="it">Semua jawaban ada di sini</div></div>
  <img class="logo" src="{LOGO_C}" alt="">
  <div class="foot" style="right:auto"><span class="caps" style="color:var(--cream);opacity:.9">Geser &nbsp;→</span></div>
</div>''')
for k in range(0, len(FAQ), 2):
    i = k//2 + 2
    qa = "".join(f'''<div style="padding:70px 0;border-bottom:1px solid rgba(166,124,100,.4)">
      <div class="caps" style="font-size:21px">Tanya</div><div class="pf" style="font-size:66px;line-height:1.1;margin-top:16px">{q}</div>
      <div style="font-size:36px;line-height:1.55;margin-top:24px;opacity:.88">{a}</div></div>''' for q, a in FAQ[k:k+2])
    parts.append(f'''<div class="tpl" id="faq-{i}">
  <img src="{LOGO}" style="position:absolute;left:62px;top:56px;width:280px" alt="">
  <div style="position:absolute;left:72px;right:72px;top:250px;border-top:1px solid rgba(166,124,100,.4)">{qa}</div>
  {foot("SunaRi · Selayar", f"{i:02d} — {NF:02d}")}
</div>''')
parts.append(f'''<div class="tpl facts" id="faq-{NF}">
  <img class="mark" src="{LOGO}" alt="">
  <div class="head center"><div class="caps">Masih ada pertanyaan?</div><h2>Tanya <span class="it">langsung</span> saja</h2></div>
  <ul><li>Harga &amp; ketersediaan kamar</li><li>Senja Dinner (pesan H-1)</li><li>Sewa kayak · Rp 50.000 / Rp 100.000</li><li>Antar-jemput bandara &amp; pelabuhan</li></ul>
  <div class="cta"><div class="caps">Info &amp; Reservasi</div><div class="wa"><span>WhatsApp</span> {WA}</div></div>
  {foot("SunaRi · Selayar", f"{NF:02d} — {NF:02d}")}
</div>''')


# ---- 12 carousels following the feed preview (covers reuse feed tiles; slides 2..n here)
FEED12 = [
 ("p01", "Lebih dari Menginap", "camp-1", [
   ("senja/05-tamu-di-meja.jpg","50% 55%","Duduk, diam, menikmati","Tidak perlu rencana. Cukup meja kayu, angin laut, dan langit yang pelan-pelan berubah warna."),
   ("resto/04-resto-malam-pohon-kelapa.jpg","50% 70%","Makan malam di bawah pohon kelapa","Ikan bakar &amp; seafood di Bajoy Beach Resto. Senja Dinner bisa dipesan H-1."),
   ("malam/03-resort-malam-a-frame.jpg","50% 60%","Lalu malam datang","Lampu-lampu bungalow menyala di antara pohon kelapa.")],
   ("Lebih dari menginap", ["5 tipe bungalow dengan teras pribadi","Sarapan, AC &amp; Wi-Fi di semua kamar","Senja tepat di depan Pantai Sunari"])),
 ("p02", "#SenjaHariIni", "feed-senja", [
   ("senja/70-perahu-nelayan-daun-kelapa.jpg","50% 50%","Perahu pulang saat senja","Nelayan melintas pelan, di bawah matahari yang mulai turun."),
   ("senja/71-siluet-tirai-matahari.jpg","45% 50%","Duduk di balik tirai","Minuman di tangan, jalur cahaya tepat di depan meja."),
   ("senja/72-ayunan-di-antara-kelapa.jpg","50% 55%","Berayun di antara kelapa","Ayunan raksasa menghadap laut, matahari tepat di cakrawala."),
   ("senja/73-kayak-pelampung-perahu.jpg","50% 78%","Kayak menunggu di pasir","Dayung sudah selesai, sekarang waktunya menikmati langit."),
   ("senja/74-matahari-menyentuh-laut-kapal.jpg","50% 60%","Saat matahari menyentuh laut","Hanya beberapa menit, lalu langit berubah warna."),
   ("senja/75-afterglow-dua-sahabat.jpg","50% 55%","Langit belum selesai","Setelah matahari tenggelam, jingga dan merah muda masih bertahan.")],
   ("Tips menikmati senja", ["Datang 30 menit sebelum matahari terbenam","Akhir Nov–Des: senja sekitar 18.00 WITA","Ikuti jam senja harian di story kami","Simpan postingan ini untuk liburanmu"])),
 ("p04", "Malam di SunaRi", "camp-4", [
   ("senja/38-blue-hour-kayak-1815.jpg","50% 55%","Langit berganti biru","Beberapa menit setelah matahari tenggelam, langit perlahan menjadi biru tua."),
   ("malam/02-bangunan-utama-malam.jpg","50% 60%","Hangat di antara pohon kelapa","Bangunan kayu dan jembatan kecil yang menyala setiap malam."),
   ("malam/06-taman-malam-bougainvillea.jpg","50% 45%","Taman ikut menyala","Lampu-lampu kecil di antara bunga dan pohon kelapa."),
   ("malam/07-jalan-setapak-gazebo.jpg","50% 60%","Jalan setapak berlampu","Dari bungalow ke gazebo, ditemani suara ombak."),
   ("resto/03-resto-malam.jpg","50% 58%","Makan malam di Bajoy","Ikan bakar &amp; seafood di bawah lampu gantung, buka sampai 21.00 WITA."),
   ("malam/09-lilin-di-meja.jpg","50% 70%","Malam yang pelan","Tidak ada yang terburu-buru di Selayar.")],
   ("Malam di SunaRi", ["Bajoy Beach Resto buka sampai 21.00 WITA","Senja Dinner, pesan H-1","Taman berlampu di antara pohon kelapa","Bungalow kayu dengan teras pribadi"])),
 ("p06", "Setiap hari berakhir indah", "feed-quote", [
   ("senja/10-kayak-pantulan.jpg","50% 60%","Matahari yang menari","SunaRi: sun dan nari. Matahari yang menari turun ke laut Selayar."),
   ("senja/16-perahu-nelayan.jpg","50% 60%","Perahu pulang ke darat","Saat langit oranye, nelayan pun pulang."),
   ("senja/18-kayak-berdua-pelampung.jpg","50% 60%","Tempat senja pulang","Dan setiap senja, kamu juga pulang ke sini.")],
   ("Tempat senja pulang", ["Resort tepi Pantai Sunari","Kepulauan Selayar, Sulawesi Selatan","Where every day ends beautifully"])),
 ("p07", "Pantai Sepi", "camp-3", [
   ("graded/pantai__05-kursi-santai-dan-kayak.jpg","50% 62%","Pantai yang masih sepi","Kursi santai, kayak di pasir, dan laut yang tenang, tanpa keramaian."),
   ("graded/pantai__01-nelayan-pagi.jpg","50% 55%","Pagi yang tenang","Hanya perahu nelayan yang lewat di laut yang datar."),
   ("graded/aktivitas__06-ayunan-gaun-merah-senja.jpg","50% 40%","Ayunan raksasa saat senja","Spot foto favorit di tepi Pantai Sunari, gratis."),
   ("graded/senja__59-makan-senja-payung-1810.jpg","50% 50%","Pantai landai &amp; aman","Air tenang, cocok untuk anak-anak dan keluarga."),
   ("graded/senja__25-pohon-senja-dekat.jpg","50% 72%","Senja di depan mata","Matahari turun ke laut, tepat di depan Pantai Sunari."),
   ("graded/senja__56-drone-kelapa-payung-1749.jpg","50% 68%","Duduk sampai langit gelap","Meja di tepi pantai, sambil menunggu matahari tenggelam.")],
   ("Pantai Sunari", ["Pantai landai &amp; aman untuk anak","Senja tepat di depan pantai","Ayunan raksasa, gratis","Sewa kayak · single Rp 50.000 · double Rp 100.000"])),
 ("p08", "Sewa Kayak", "feed-kayak", [
   ("aktivitas/01-kayak-sore.jpg","50% 55%","Mendayung menjelang senja","Waktu terbaik: 1 jam sebelum matahari terbenam."),
   ("senja/09-kayak-pasangan.jpg","50% 60%","Sendiri atau berdua","Pilih kayak single atau double."),
   ("senja/17-kayak-berdua.jpg","50% 60%","Air tenang &amp; landai","Pantai Sunari aman untuk pemula.")],
   ("Sewa kayak", ["Single · Rp 50.000","Double · Rp 100.000","Tersedia di Pantai Sunari"])),
 ("p10", "Menginap. Menjelajah. Melambat. Pulang.", "camp-2", [
   ("vip-superior-bungalow/01-eksterior-a-frame.jpg","40% 50%","Menginap.","Bungalow kayu dengan teras pribadi, sarapan, AC &amp; Wi-Fi."),
   ("senja/11-kayak-dan-pulau.jpg","50% 60%","Menjelajah.","Kayak di Pantai Sunari, laut tenang, pulau di kejauhan."),
   ("taman/01-meja-di-taman.jpg","50% 35%","Melambat.","Duduk di taman di bawah pohon palem dan bunga bougainvillea."),
   ("senja/12-kayak-matahari-merah-story.jpg","50% 55%","Pulang.","Dan setiap sore, senja menunggumu di tepi pantai.")],
   ("Mulai liburanmu", ["5 tipe bungalow untuk 2–8 orang","Antar-jemput bandara &amp; pelabuhan","Senja tepat di depan pantai"])),
 ("p11", "Staycation Senja", "feed-promo", [
   ("superior-bungalow/02-eksterior-depan.jpg","50% 30%","Superior Bungalow","Rumah kayu A-frame dengan king bed, TV &amp; kamar mandi semi-outdoor."),
   ("resto/05-makan-malam-taman.jpg","50% 60%","Senja Dinner","Ikan bakar &amp; seafood saat matahari terbenam."),
   ("superior-bungalow/03-teras.jpg","50% 50%","Teras pribadi","Tempat menunggu senja, dua sore berturut-turut.")],
   ("Staycation Senja", ["Superior Bungalow kayu A-frame","Senja Dinner untuk dua orang","Info paket &amp; harga via WhatsApp"])),
]
for pre, name, cover, slides, (endt, endl) in FEED12:
    n = len(slides) + 2
    for i, (img, pos, h, t) in enumerate(slides, start=2):
        parts.append(f"""<div class="tpl" id="{pre}-{i}">
  <img class="ph" src="../assets/photos/{img}" style="object-position:{pos}" alt="">
  <div class="txt"><div class="caps">{name}</div><h2>{h}</h2><p>{t}</p></div>
  {foot("SunaRi · Selayar", f"{i:02d} — {n:02d}")}
</div>""")
    li = "".join(f"<li>{x}</li>" for x in endl)
    parts.append(f"""<div class="tpl facts" id="{pre}-{n}">
  <img class="mark" src="{LOGO}" alt="">
  <div class="head center"><div class="caps">{name}</div><h2>{endt.split(' ',1)[0]} <span class="it">{endt.split(' ',1)[1] if ' ' in endt else ''}</span></h2></div>
  <ul>{li}</ul>
  <div class="cta"><div class="caps">Info &amp; Reservasi</div><div class="wa"><span>WhatsApp</span> {WA}</div></div>
  {foot("SunaRi · Selayar", f"{n:02d} — {n:02d}")}
</div>""")
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
  <img class="mark" src="{LOGO}" alt="">
  <div class="head center"><div class="caps">{e(r["name"])}</div><h2>Yang kamu <span class="it">dapatkan</span></h2></div>
  <ul>{facts}</ul>
  <div class="cta"><div class="caps">Info &amp; Reservasi</div><div class="wa"><span>WhatsApp</span> {WA}</div></div>
  {foot("SunaRi · Selayar", f"{n:02d} — {n:02d}")}
</div>''')

head = f'<!doctype html><html lang="id"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>SunaRi Instagram Kit</title>{FONTS}<style>{CSS}</style></head><body>\n'
(HERE / "kit.html").write_text(head + "\n".join(parts) + "\n</body></html>\n")

tiles = "".join(f'<div class="t"><img src="{g}.png" alt=""></div>' for g in GRID)
HL = [("hl2-02-reservasi","Reservasi Kamar"),("hl2-07f-promo","Promo"),("hl2-07e-qna","Q&amp;A"),("hl2-06-ayunan","Ayunan Raksasa"),("hl2-08-kayak","Kano / Kayak")]
hls = "".join(f'<div class="h"><div class="hc"><img src="highlights-v2/{f}.png" alt=""></div><span>{n}</span></div>' for f, n in HL)
grid = f'''<!doctype html><html lang="id"><head><meta charset="utf-8"><title>SunaRi Feed Preview</title>{FONTS}<style>
*{{box-sizing:border-box;margin:0;padding:0}} body{{background:#ddd6cc;padding:40px;font-family:-apple-system,"Segoe UI",Roboto,Arial,sans-serif}}
#grid-preview{{width:1080px;background:#fff;color:#000}}
.bar{{height:110px;display:flex;align-items:center;padding:0 40px;font-size:38px;font-weight:700;border-bottom:1px solid #efefef}}
.top{{display:flex;align-items:center;gap:60px;padding:44px 40px 0}}
.av{{width:220px;height:220px;border-radius:50%;overflow:hidden;flex:none;border:1px solid #dbdbdb}} .av img{{width:100%;height:100%;display:block}}
.nm{{font-size:34px;font-weight:600}} .cat{{font-size:28px;color:#737373;margin-top:6px}}
.bio{{padding:28px 40px 0;font-size:29px;line-height:1.45;white-space:pre-line}} .bio a{{color:#00376b;font-weight:600}}
.btns{{display:flex;gap:14px;padding:30px 40px 0}} .btns div{{flex:1;background:#efefef;border-radius:16px;text-align:center;font-size:28px;font-weight:600;padding:20px 0}}
.btns .pri{{background:#0095f6;color:#fff}}
.hls{{display:flex;gap:34px;padding:40px 40px 34px;overflow:hidden}} .h{{width:160px;text-align:center;flex:none}}
.hc{{width:150px;height:150px;border-radius:50%;border:2px solid #dbdbdb;padding:6px;margin:0 auto}} .hc img{{width:100%;height:100%;border-radius:50%;object-fit:cover;display:block}}
.h span{{display:block;font-size:24px;margin-top:12px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}}
.tabs{{display:flex;border-top:1px solid #dbdbdb}} .tabs div{{flex:1;height:90px;display:flex;align-items:center;justify-content:center}}
.tabs .on{{border-top:2px solid #000;margin-top:-1px}} .tabs i{{width:40px;height:40px;border:3px solid #000;border-radius:4px;display:block;background:repeating-linear-gradient(90deg,transparent 0 9px,#000 9px 12px)}}
.g{{display:grid;grid-template-columns:repeat(3,1fr);gap:3px}} .t{{aspect-ratio:3/4;overflow:hidden}} .t img{{width:100%;height:100%;object-fit:cover;display:block}}
</style></head><body><div id="grid-preview">
<div class="bar">sunaribeachresortselayar</div>
<div class="top"><div class="av"><img src="profile/pp-e.png" alt=""></div>
<div><div class="nm">SunaRi Beach Resort Selayar</div><div class="cat">Resort</div></div></div>
<div class="bio">🌅 Tempat senja pulang
🌴 Resort tepi pantai di Kepulauan Selayar
🍽️ Senja Dinner ikan bakar &amp; seafood
📩 WA {WA} ⬇️
<a>wa.me/6282189033044</a></div>
<div class="btns"><div class="pri">Ikuti</div><div>Kirim pesan</div><div>WhatsApp</div></div>
<div class="hls">{hls}</div>
<div class="tabs"><div class="on"><i></i></div><div></div><div></div></div>
<div class="g">{tiles}</div></div></body></html>'''
(HERE / "grid.html").write_text(grid)
print("wrote kit.html (%d templates) and grid.html" % len(parts))
