"""E-book "Panduan Lengkap SunaRi Beach Resort Selayar": A4, gaya SunaRi.
Run: python3 ebook/build_ebook.py && node ebook/render.js
Semua isi berasal dari data yang sudah dikonfirmasi (brand guide, OTA, menu, dokumen tur & transfer, peta rute)."""
import pathlib
H = pathlib.Path(__file__).parent
WA = "0821-8903-3044"
IG = "@sunaribeachresortselayar"
I = "img/"
def ph(path): return I + path.replace("/", "__")
def rp(v): return "Rp " + f"{v:,}".replace(",", ".")

FONTS = '<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;1,400;1,500&family=Montserrat:wght@400;500;600;700&display=swap" rel="stylesheet">'
CSS = """
*{margin:0;padding:0;box-sizing:border-box}
body{background:#d9d2c8;font-family:Montserrat,sans-serif;color:#3B2819;font-variant-numeric:lining-nums;-webkit-font-smoothing:antialiased}
.page{width:794px;height:1123px;background:#FBF4EC;position:relative;overflow:hidden;margin:20px auto;padding:58px 60px 86px;page-break-after:always}
.run{position:absolute;left:60px;right:60px;bottom:34px;display:flex;justify-content:space-between;align-items:center;padding-top:12px;border-top:1px solid rgba(138,95,72,.35);
  font-size:10px;font-weight:600;letter-spacing:.22em;text-transform:uppercase;color:#8A5F48}
.run b{font-family:'Playfair Display',serif;font-size:15px;letter-spacing:0;color:#45301F;font-weight:500}
.sec{font-size:11px;font-weight:700;letter-spacing:.26em;text-transform:uppercase;color:#7A5039;display:flex;align-items:center;gap:12px}
.sec .n{color:#E07A4B}
.sec::after{content:"";flex:1;height:1px;background:rgba(138,95,72,.35)}
h1{font-family:'Playfair Display',serif;font-weight:500;font-size:40px;line-height:1.1;margin-top:12px}
h1 i,h2 i,h3 i{color:#9A6A4F;font-style:italic}
h2{font-family:'Playfair Display',serif;font-weight:500;font-size:25px;line-height:1.2;margin-top:22px}
h3{font-family:'Playfair Display',serif;font-weight:500;font-size:19px;line-height:1.25}
.lead{font-size:15px;line-height:1.6;margin-top:12px;color:#3B2819}
p.t{font-size:13.5px;line-height:1.6;margin-top:8px;color:#3B2819}
.caps{font-size:10.5px;font-weight:700;letter-spacing:.2em;text-transform:uppercase;color:#7A5039}
.img{width:100%;object-fit:cover;border-radius:16px;display:block}
.grid2{display:grid;grid-template-columns:1fr 1fr;gap:14px}
.grid3{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}
.chips{display:flex;flex-wrap:wrap;gap:8px;margin-top:12px}
.chip{font-size:12px;font-weight:600;padding:6px 12px;border-radius:20px;background:rgba(230,200,155,.32);color:#45301F}
.chip b{color:#E07A4B;font-weight:700}
table{width:100%;border-collapse:collapse;font-size:13px;margin-top:10px}
th{font-size:9.5px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:#7A5039;text-align:left;padding:7px 6px;border-bottom:1px solid rgba(138,95,72,.55)}
td{padding:6.5px 6px;border-bottom:1px solid rgba(138,95,72,.25);vertical-align:top;line-height:1.4}
td.r,th.r{text-align:right;white-space:nowrap} td.b{font-weight:600} td.hi{font-weight:700;color:#C0592C} td.t{white-space:nowrap;font-weight:700;color:#7A5039;width:104px}
ul.l{list-style:none;font-size:13px;line-height:1.45;margin-top:6px}
ul.l li{padding:2.5px 0 2.5px 16px;position:relative}
ul.l li::before{content:"";position:absolute;left:2px;top:9px;width:6px;height:6px;border-radius:50%;background:#E07A4B}
ul.l.no li::before{background:none;content:"–";top:2px;color:#8A5F48;font-weight:700}
ul.l.cols{columns:2;column-gap:22px} ul.l.cols3{columns:3;column-gap:18px} ul.l li{break-inside:avoid}
.card{border-radius:16px;background:#FFFDF9;padding:16px 18px;box-shadow:0 1px 0 rgba(255,255,255,.8),0 6px 18px rgba(90,62,49,.07)}
.note{border-left:3px solid #FDB15D;padding:9px 14px;font-size:13px;line-height:1.55;margin-top:12px;background:rgba(253,177,93,.08);border-radius:0 10px 10px 0}
.note b{color:#45301F}
.kv{display:grid;grid-template-columns:160px 1fr;font-size:13.5px;line-height:1.5}
.kv div{padding:9px 0;border-bottom:1px solid rgba(138,95,72,.2)}
.kv div:nth-child(odd){font-weight:700;font-size:10.5px;letter-spacing:.14em;text-transform:uppercase;color:#7A5039;padding-top:11px}
.num{display:inline-flex;width:24px;height:24px;border-radius:50%;color:#fff;align-items:center;justify-content:center;font-family:'Playfair Display',serif;font-size:13px;flex:none}
.step{display:flex;gap:12px;align-items:flex-start;padding:8px 0;border-bottom:1px solid rgba(138,95,72,.25);font-size:12.5px;line-height:1.45}
.step:last-child{border-bottom:none}
.step .d{margin-left:auto;font-weight:700;color:#C0592C;white-space:nowrap;padding-left:10px}
.toc a{display:flex;align-items:baseline;gap:10px;padding:11px 0;border-bottom:1px solid rgba(138,95,72,.22);text-decoration:none;color:#45301F}
.toc .no{font-size:10px;font-weight:700;letter-spacing:.2em;color:#E07A4B;width:30px}
.toc .ti{font-family:'Playfair Display',serif;font-size:17px}
.toc .ds{font-size:12px;color:#5A3E31;margin-left:8px}
.toc .dots{flex:1;border-bottom:1px dotted rgba(138,95,72,.5);transform:translateY(-4px)}
.toc .pg{font-family:'Playfair Display',serif;font-size:15px}
.tp td{padding:4.5px 6px} .tp h2{margin-top:12px !important} .tp ul.l li{padding:1.5px 0 1.5px 16px} .tp .lead{margin-top:6px}
a.lnk{color:#C0592C;font-weight:700;text-decoration:none;border-bottom:1px solid rgba(192,89,44,.4)}
.vcard .pr{font-family:'Playfair Display',serif;font-size:24px;color:#C0592C;margin-top:6px}
.menu-col h3{margin-top:14px} .menu-col table{font-size:12.5px} .menu-col td{padding:5px 4px}
.cover > div{text-shadow:0 2px 14px rgba(0,0,0,.65),0 1px 3px rgba(0,0,0,.5)}
.cover > img[src*='logo']{filter:drop-shadow(0 2px 10px rgba(0,0,0,.45))}
@page{size:210mm 297mm;margin:0} @media print{body{background:none}.page{margin:0}}
"""
SUN = '''<svg viewBox="0 0 200 200" width="{w}" height="{w}" style="display:block;{st}"><defs><linearGradient id="sg{u}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FDB15D"/><stop offset="1" stop-color="#FF8A5C"/></linearGradient>
<mask id="sm{u}"><rect width="200" height="200" fill="white"/><rect y="112" width="200" height="5"/><rect y="126" width="200" height="7"/><rect y="142" width="200" height="9"/><rect y="160" width="200" height="11"/><rect y="180" width="200" height="13"/></mask></defs>
<circle cx="100" cy="100" r="96" fill="url(#sg{u})" mask="url(#sm{u})"/></svg>'''
_u = [0]
def sun(w, st=""):
    _u[0] += 1; return SUN.format(w=w, st=st, u=_u[0])

PAGES = []   # (section_title_for_toc or None, html, cls)
def add(html, toc=None, cls=""): PAGES.append((toc, html, cls))
def head(no, label, title, lead=""):
    return f'<div class="sec"><span class="n">{no}</span>{label}</div><h1>{title}</h1>' + (f'<p class="lead">{lead}</p>' if lead else "")
def tbl(head_, rows, right_from=1, hi_last=False):
    th = "".join(f'<th class="{"r" if i >= right_from else ""}">{h}</th>' for i, h in enumerate(head_))
    tr = "".join("<tr>" + "".join(f'<td class="{("b " if i == 0 else "") + ("r " if i >= right_from else "") + ("hi" if hi_last and i == len(r) - 1 else "")}">{c}</td>' for i, c in enumerate(r)) + "</tr>" for r in rows)
    return f"<table><tr>{th}</tr>{tr}</table>"
def ul(items, cls=""): return f'<ul class="l {cls}">' + "".join(f"<li>{x}</li>" for x in items) + "</ul>"
def img(path, h, pos="50% 50%", extra=""): return f'<img class="img" src="{ph(path)}" style="height:{h}px;object-position:{pos};{extra}" alt="">'

# =============================================================== COVER
add(f'''<img src="{I}cover__kayak-senja.jpg" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:50% 42%" alt="">
<img src="../assets/logo-sunari-color-dark.png" style="position:absolute;left:50%;transform:translateX(-50%);top:64px;width:270px" alt="">
<div style="position:absolute;left:64px;right:64px;bottom:96px;color:#FBF4EC;text-align:center">
  <div style="font-size:11px;font-weight:700;letter-spacing:.34em;text-transform:uppercase;color:#FDB15D">Panduan Lengkap Tamu · Edisi 2026</div>
  <div style="font-family:'Playfair Display',serif;font-size:58px;line-height:1.05;margin-top:16px;text-shadow:0 4px 20px rgba(0,0,0,.35)">Tempat senja <i style="color:#FDB15D">pulang.</i></div>
  <div style="font-size:14px;line-height:1.6;margin-top:16px;opacity:.95">Semua yang perlu Anda tahu sebelum menginap di SunaRi Beach Resort Selayar:<br>kamar, fasilitas, aktivitas, tur pulau, rute perjalanan &amp; cara reservasi.</div>
  <div style="display:flex;justify-content:center;gap:26px;margin-top:26px;font-size:10px;font-weight:700;letter-spacing:.24em;text-transform:uppercase;opacity:.9"><span>Pantai Sunari</span><span>·</span><span>Kepulauan Selayar</span><span>·</span><span>Sulawesi Selatan</span></div>
</div>''', cls="cover")

# =============================================================== TOC (filled later)
add("__TOC__")

# =============================================================== 1 SELAMAT DATANG
add(f'''{head("01", "Selamat datang", "Selamat datang di <i>SunaRi</i>")}
<div class="grid2" style="margin-top:18px;grid-template-columns:1.15fr 1fr;align-items:start">
  <div>
    <p class="lead" style="margin-top:0">SunaRi Beach Resort Selayar adalah resort tepi pantai di <b>Pantai Sunari</b>, pesisir barat Kepulauan Selayar, Sulawesi Selatan. Setiap sore, matahari terbenam tepat di depan pantai kami, di atas laut yang tenang.</p>
    <p class="t">Kami memiliki lima tipe bungalow kayu dengan teras pribadi, mulai dari rumah panggung di bibir pantai, bungalow A-frame dengan kamar mandi semi-outdoor, hingga bungalow dua lantai untuk keluarga hingga 8 orang. Semua kamar dilengkapi AC dan Wi-Fi, dan sudah termasuk sarapan.</p>
    <p class="t">Pantai kami landai dan aman untuk anak-anak. Sore hari, mendayunglah dengan kayak menyongsong senja, berayun di ayunan raksasa, lalu tutup hari dengan ikan bakar di Bajoy Beach Resto.</p>
    <div class="card" style="margin-top:18px;text-align:center">{sun(46, "margin:0 auto")}
      <div style="font-family:'Playfair Display',serif;font-size:20px;margin-top:10px">“Datanglah untuk senjanya,<br><i style="color:#A67C64">tinggallah untuk ketenangannya.”</i></div></div>
  </div>
  <div>{img("senja/24-pohon-tepi-pantai-senja.jpg", 300)}<div style="height:12px"></div>{img("pantai/04-kursi-santai-bawah-pohon.jpg", 250, "50% 60%")}</div>
</div>
<h2>SunaRi dalam <i>angka</i></h2>
<div class="grid3" style="margin-top:12px;grid-template-columns:repeat(4,1fr)">
  {"".join(f'<div class="card" style="text-align:center;padding:14px 8px"><div style="font-family:Playfair Display,serif;font-size:30px;color:#E07A4B">{a}</div><div class="caps" style="margin-top:4px;font-size:8.5px">{b}</div></div>' for a, b in [("5", "Tipe bungalow"), ("8", "Tamu maks. / Family"), ("4", "Pilihan tur pulau"), ("3", "Rute menuju Selayar")])}
</div>''', toc=("Selamat datang", "Tentang SunaRi & Pantai Sunari"))

# =============================================================== 2 INFO PENTING
add(f'''{head("02", "Info penting", "Informasi <i>sekilas</i>", "Simpan halaman ini. Semua yang paling sering ditanyakan tamu ada di sini.")}
<div class="kv" style="margin-top:16px">
  <div>Alamat</div><div>Jl. Poros Benteng – Appatana KM 14, Dusun Tile-Tile Utara, Desa Patikarya, Kec. Bontosikuyu, Kab. Kepulauan Selayar, Sulawesi Selatan</div>
  <div>Pantai</div><div><b>Pantai Sunari</b>, pesisir barat Pulau Selayar. Landai &amp; aman untuk anak-anak</div>
  <div>Check-in / out</div><div>Check-in mulai <b>14.00 WITA</b> · Check-out paling lambat <b>12.00 WITA</b></div>
  <div>Harga kamar</div><div>Mulai <b>Rp 900.000 /malam</b>, sudah termasuk sarapan. Daftar lengkap di Bab 03</div>
  <div>Sudah termasuk</div><div>Sarapan untuk semua tipe kamar · AC · Wi-Fi · teras pribadi</div>
  <div>Restoran</div><div><b>Bajoy Beach Resto</b>: 07.00–21.00 WITA (tamu menginap) · 07.00–19.00 WITA (tamu tidak menginap)</div>
  <div>Senja Dinner</div><div>Ikan bakar &amp; seafood saat matahari terbenam, <b>pesan paling lambat H-1</b></div>
  <div>Matahari terbenam</div><div>Tepat di depan Pantai Sunari, sekitar <b>17.50–18.00 WITA</b>, paling cantik April–Desember</div>
  <div>Dari bandara</div><div>Bandara H. Aroeppala → SunaRi ±10–15 menit dengan mobil</div>
  <div>Antar-jemput</div><div>Tersedia (berbayar): bandara, Pelabuhan Benteng &amp; Pamatata, hingga dari Makassar. Lihat Bab 08</div>
  <div>Reservasi</div><div>WhatsApp <b>{WA}</b> · Instagram <b>{IG}</b></div>
  <div>Google Maps</div><div>maps.app.goo.gl/iUWWHNCT7Vyu4i537</div>
</div>
<div class="note"><b>Ketersediaan kamar</b> menyesuaikan tanggal. Hubungi admin kami lewat WhatsApp untuk cek kamar kosong &amp; konfirmasi harga terbaru.</div>''', toc=("Informasi sekilas", "Alamat, jam, kontak & hal penting"))

# =============================================================== 3 KAMAR OVERVIEW
ROOMS = [
 ("Standard Bungalow", "2 orang (maks. 3)", "Queen", "Teras luas menghadap laut, kamar mandi bambu", 900000),
 ("VIP Standard Bungalow", "2 orang (maks. 3)", "King", "Rumah panggung di tepi pantai, teras ke arah senja", 1000000),
 ("Superior Bungalow", "2 orang (maks. 3)", "King", "A-frame berloteng, TV, kamar mandi semi-outdoor", 1500000),
 ("VIP Superior Bungalow", "2 orang (maks. 3)", "King", "Kelas tertinggi: bathtub, air panas, TV, mini bar", 2500000),
 ("Family Superior Bungalow", "6 orang (maks. 8)", "Besar + 4 kasur", "2 lantai, kamar mandi di kedua lantai", 2500000),
]
add(f'''{head("03", "Kamar", "Lima tipe <i>bungalow</i>", "Setiap bungalow terbuat dari kayu dengan teras pribadi. Semua tipe sudah termasuk sarapan, AC dan Wi-Fi.")}
{tbl(["Tipe kamar", "Kapasitas", "Tempat tidur", "Keistimewaan", "Harga / malam"], [(a, b, c, d, rp(e)) for a, b, c, d, e in ROOMS], right_from=4, hi_last=True)}
<p class="t" style="font-size:12px;margin-top:6px">Harga per kamar per malam, sudah termasuk sarapan. Extra bed dikenakan biaya tambahan.</p>
<h2>Fasilitas di <i>semua kamar</i></h2>
{ul(["Sarapan", "AC", "Wi-Fi", "Teras pribadi dengan kursi santai", "Kopi/teh &amp; pemanas air (kettle)", "Meja kerja/rias", "Tirai blackout", "Bantal &amp; selimut tambahan", "Kamar mandi dalam, toilet duduk", "Perlengkapan mandi &amp; handuk", "Setrika (atas permintaan)", "Extra bed (berbayar)"], "cols3")}
<div class="grid3" style="margin-top:18px">{img("vip-standard-bungalow/02-teras-view-pantai.jpg", 170)}{img("superior-bungalow/02-eksterior-depan.jpg", 170, "50% 35%")}{img("family-superior-bungalow/01-eksterior-taman.jpg", 170)}</div>
<div class="note"><b>Extra bed:</b> 1 extra bed untuk Standard, VIP Standard, Superior &amp; VIP Superior (maks. 3 orang). 2 extra bed untuk Family Superior (maks. 8 orang). Biaya extra bed dikonfirmasi admin saat reservasi.</div>''',
    toc=("Kamar", "Perbandingan 5 tipe bungalow"))

def room(no, name, sub, spec, desc, fac, photos, price=0):
    big, s1, s2 = photos
    add(f'''{head(no, "Kamar", name)}
<div class="chips"><span class="chip" style="background:#FDE3CF">Harga <b>{rp(price)} /malam</b></span>{"".join(f'<span class="chip">{k} <b>{v}</b></span>' for k, v in spec)}</div>
<div style="margin-top:14px">{img(big[0], 300, big[1])}</div>
<div class="grid2" style="margin-top:12px">{img(s1[0], 175, s1[1])}{img(s2[0], 175, s2[1])}</div>
<p class="lead" style="margin-top:16px"><i style="font-family:'Playfair Display',serif;font-size:16px;color:#A67C64">{sub}</i></p>
<p class="t">{desc}</p>
<h2 style="font-size:18px;margin-top:14px">Fasilitas kamar</h2>
{ul(fac, "cols3")}''', toc=None)

room("03 · a", "Standard <i>Bungalow</i>", "Pagi menghadap laut Selayar.",
     [("Kapasitas", "2 dewasa (maks. 3)"), ("Tempat tidur", "Queen"), ("Pemandangan", "Laut &amp; taman")],
     "Bungalow kayu yang sejuk dan bersih dengan atap tinggi dan teras pribadi yang luas menghadap laut. Nikmati kopi pagi sambil melihat ombak dari kursi santai, lalu berjalan ke pantai untuk menunggu senja. Kamar mandi dalam bernuansa bambu dengan lantai batu alam.",
     ["Sarapan", "Queen bed", "AC", "Wi-Fi", "Kopi/teh &amp; kettle", "Meja kerja/rias", "Tirai blackout", "Bantal &amp; selimut tambahan", "Shower", "Toilet duduk", "Perlengkapan mandi &amp; handuk", "Teras pribadi &amp; kursi santai", "Setrika (atas permintaan)", "Extra bed (maks. 1)"],
     [("standard-bungalow/01-teras-view-laut.jpg", "50% 60%"), ("standard-bungalow/03-kamar-depan.jpg", "50% 50%"), ("standard-bungalow/04-kamar-mandi-bambu.jpg", "50% 50%")], price=900000)
room("03 · b", "VIP Standard <i>Bungalow</i>", "Rumah panggung di bibir Pantai Sunari.",
     [("Kapasitas", "2 dewasa (maks. 3)"), ("Tempat tidur", "King"), ("Pemandangan", "Laut atau taman")],
     "Rumah panggung beratap rumbia di tepi Pantai Sunari, dengan kamar yang lebih luas dibanding Standard Bungalow. Teras pribadi menghadap ke arah matahari terbenam. Pada unit tepi pantai, senja tepat di depan mata. Kamar bernuansa kayu dengan lampu dinding temaram dan area wastafel dengan gantungan baju.",
     ["Sarapan", "King bed", "AC", "Wi-Fi", "Kopi/teh &amp; kettle", "Meja kerja/rias", "Tirai blackout", "Bantal &amp; selimut tambahan", "Shower", "Toilet duduk", "Perlengkapan mandi &amp; handuk", "Teras pribadi &amp; kursi santai", "Setrika (atas permintaan)", "Extra bed (maks. 1)"],
     [("vip-standard-bungalow/02-teras-view-pantai.jpg", "50% 60%"), ("vip-standard-bungalow/01-eksterior-rumah-panggung.jpg", "50% 50%"), ("vip-standard-bungalow/06-kamar-depan.jpg", "50% 50%")], price=1000000)
room("03 · c", "Superior <i>Bungalow</i>", "Rumah kayu A-frame di antara pohon kelapa.",
     [("Kapasitas", "2 dewasa (maks. 3)"), ("Tempat tidur", "King"), ("Ekstra", "TV · loteng")],
     "Bungalow kayu beratap A-frame dengan loteng di bawah langit-langit kayu yang menjulang, lebih luas dibanding Standard dan VIP Standard. Keistimewaannya adalah kamar mandi semi-outdoor dengan rain shower, dikelilingi taman hijau dan langit terbuka. Teras kayu pribadi menghadap laut atau taman.",
     ["Sarapan", "King bed", "TV", "Loteng", "AC", "Wi-Fi", "Kopi/teh &amp; kettle", "Meja kerja/rias", "Tirai blackout", "Kamar mandi semi-outdoor", "Rain shower", "Perlengkapan mandi &amp; handuk", "Teras pribadi &amp; kursi santai", "Setrika (atas permintaan)", "Extra bed (maks. 1)"],
     [("superior-bungalow/02-eksterior-depan.jpg", "50% 35%"), ("superior-bungalow/05-kamar-tempat-tidur.jpg", "50% 50%"), ("superior-bungalow/10-kamar-mandi-taman.jpg", "50% 50%")], price=1500000)
room("03 · d", "VIP Superior <i>Bungalow</i>", "Kelas tertinggi di SunaRi.",
     [("Kapasitas", "2 dewasa (maks. 3)"), ("Tempat tidur", "King"), ("Ekstra", "Bathtub · air panas")],
     "Bungalow A-frame beratap rumbia dengan loteng dan jendela segitiga yang membiarkan cahaya pagi masuk. Kamar mandi semi-outdoor beratap kaca dengan <b>bathtub, rain shower dan air panas</b>, satu-satunya tipe kamar dengan air panas, untuk berendam air hangat dengan pohon kelapa tepat di atas kepala.",
     ["Sarapan", "King bed", "TV", "Mini bar/kulkas", "Bathtub", "Air panas &amp; dingin", "Rain shower", "Loteng", "AC", "Wi-Fi", "Kopi/teh &amp; kettle", "Tirai blackout", "Perlengkapan mandi &amp; handuk", "Teras pribadi &amp; kursi santai", "Extra bed (maks. 1)"],
     [("vip-superior-bungalow/01-eksterior-a-frame.jpg", "50% 45%"), ("vip-superior-bungalow/04-kamar-tempat-tidur.jpg", "50% 50%"), ("vip-superior-bungalow/06-bathtub-semi-outdoor.jpg", "50% 55%")], price=2500000)
room("03 · e", "Family Superior <i>Bungalow</i>", "Satu rumah, dua lantai, semua bersama.",
     [("Kapasitas", "6 orang (maks. 8)"), ("Lantai 1", "2–3 orang"), ("Lantai 2", "4–5 orang")],
     "Tipe bungalow terbesar di SunaRi, ideal untuk keluarga besar. Lantai 1 untuk 2–3 orang dengan tempat tidur besar, lantai 2 untuk 4–5 orang dengan empat kasur di bawah atap kayu yang tinggi. Toilet dan kamar mandi tersedia di kedua lantai. Teras pribadi dengan kursi santai, pas untuk berkumpul sebelum senja.",
     ["Sarapan", "2 lantai", "Kamar mandi di kedua lantai", "AC", "Wi-Fi", "Kopi/teh &amp; kettle", "Meja kerja/rias", "Tirai blackout", "Bantal &amp; selimut tambahan", "Perlengkapan mandi &amp; handuk", "Teras pribadi &amp; kursi santai", "Setrika (atas permintaan)", "Extra bed (maks. 2)"],
     [("family-superior-bungalow/01-eksterior-taman.jpg", "55% 50%"), ("family-superior-bungalow/05-kamar-bawah-depan.jpg", "50% 50%"), ("family-superior-bungalow/09-lantai-atas-4-kasur.jpg", "50% 50%")], price=2500000)

# =============================================================== 4 RESTO
MENU = {
 "Makanan": [("Nasi Goreng Sunari", 45000), ("Nasi Goreng Seafood", 45000), ("Nasi Goreng Egois", 45000), ("Nasi Goreng Kampung", 45000), ("Ayam Lalapan", 50000), ("Ayam Bakar", 50000),
             ("Beef Sandwich", 30000), ("Beef Sandwich D.", 40000), ("Egg Sandwich", 25000), ("Egg Sandwich D.", 35000), ("Indomie Goreng", 20000), ("Indomie Kuah", 20000)],
 "Snack": [("French Fries", 25000), ("Toast", 25000), ("Banana Roll", 25000), ("Fried Cassava", 25000), ("Fried Banana", 25000)],
 "Drinks": [("Chocolate M.S", 25000), ("Oreo M.S", 25000), ("Orange Punch", 25000), ("Watermelon L.M", 25000), ("Green Tea", 25000), ("Hot Tea", 10000), ("Ice Tea", 20000),
            ("Black Coffee", 20000), ("Coffee Milk", 20000), ("Milk Tea", 25000), ("Original Coconut", 25000), ("Saronso", 25000)],
 "Juice": [("Avocado", 25000), ("Watermelon", 25000), ("Melon", 25000), ("Mango", 25000), ("Dragon Fruit", 25000), ("Soursop Fruit", 25000), ("Apple", 25000), ("Orange", 25000)],
 "Soft Drink": [("Coke", 15000), ("Fanta", 15000), ("Sprite", 15000), ("Fresh Tea", 15000), ("Pulpy", 15000), ("Mineral Water", 10000)],
}
mt = lambda k: f'<h3>{k}</h3><table>' + "".join(f'<tr><td>{n}</td><td class="r">{rp(v)}</td></tr>' for n, v in MENU[k]) + "</table>"
add(f'''{head("04", "Restoran", "Bajoy <i>Beach Resto</i>", "Restoran tepi pantai SunaRi dengan ikan bakar &amp; seafood setiap hari. Sarapan tamu menginap disajikan di sini.")}
<div class="grid2" style="margin-top:16px">{img("resto/03-resto-malam.jpg", 210)}{img("resto/05-makan-malam-taman.jpg", 210)}</div>
<div class="grid2" style="margin-top:16px;align-items:start">
  <div class="card"><div class="caps">Jam buka</div>
    <table style="margin-top:6px"><tr><td class="b">Tamu menginap</td><td class="r">07.00 – 21.00 WITA</td></tr><tr><td class="b">Tamu tidak menginap</td><td class="r">07.00 – 19.00 WITA</td></tr></table></div>
  <div class="card"><div class="caps">Senja Dinner</div>
    <p class="t" style="margin-top:6px">Makan malam <b>ikan bakar &amp; seafood</b> di tepi pantai saat matahari terbenam. <b>Pesan paling lambat H-1</b> lewat WhatsApp {WA}.</p></div>
</div>
<h2>Menu <i>harian</i></h2>
<div class="grid2 menu-col" style="align-items:start;gap:26px">
  <div>{mt("Makanan")}</div>
  <div>{mt("Drinks")}</div>
</div>''', toc=("Restoran", "Bajoy Beach Resto, Senja Dinner & menu"))
add(f'''{head("04", "Restoran", "Menu <i>snack</i>, jus &amp; minuman")}
<div class="grid2 menu-col" style="align-items:start;gap:26px;margin-top:6px">
  <div>{mt("Snack")}{mt("Soft Drink")}</div><div>{mt("Juice")}</div>
</div>
<div class="grid3" style="margin-top:22px">{img("resto/02-bakar-cumi-ayam.jpg", 200)}{img("malam/09-lilin-di-meja.jpg", 200)}{img("resto/01-tamu-makan-siang.jpg", 200, "50% 40%")}</div>
<div class="note">Harga dapat berubah sewaktu-waktu. Menu ikan bakar &amp; seafood untuk Senja Dinner dikonfirmasi admin saat pemesanan.</div>''')

# =============================================================== 5 AKTIVITAS
add(f'''{head("05", "Aktivitas", "Aktivitas di <i>Pantai Sunari</i>", "Tidak perlu jauh-jauh: banyak hal bisa dinikmati tanpa meninggalkan resort.")}
<div class="grid2" style="margin-top:16px;align-items:start">
  <div class="card">{img("aktivitas/01-kayak-sore.jpg", 170)}<h3 style="margin-top:12px">Sewa <i>kayak</i></h3>
    <p class="t">Air Pantai Sunari tenang dan landai, paling seru menjelang senja.</p>
    <table><tr><td class="b">Kayak single</td><td class="r hi">{rp(50000)}</td></tr><tr><td class="b">Kayak double</td><td class="r hi">{rp(100000)}</td></tr></table></div>
  <div class="card">{img("aktivitas/05-ayunan-raksasa-senja.jpg", 170, "40% 55%")}<h3 style="margin-top:12px">Ayunan <i>raksasa</i></h3>
    <p class="t">Spot foto favorit di tepi pantai, berayun dengan matahari terbenam di depan mata. <b>Gratis.</b></p></div>
  <div class="card">{img("senja/07-payung-kursi-pantai.jpg", 150)}<h3 style="margin-top:12px">Menunggu <i>senja</i></h3>
    <p class="t">Matahari terbenam tepat di depan pantai, sekitar 17.50–18.00 WITA. Paling cantik April–Desember.</p></div>
  <div class="card">{img("pantai/04-kursi-santai-bawah-pohon.jpg", 150, "50% 55%")}<h3 style="margin-top:12px">Bersantai &amp; <i>bermain air</i></h3>
    <p class="t">Pantai landai dan aman untuk anak-anak. Kursi santai di bawah pohon ketapang dengan Pulau Gusung di seberang.</p></div>
</div>''', toc=("Aktivitas", "Kayak, ayunan raksasa, snorkeling, senja & pantai"))
add(f'''{head("05", "Aktivitas", "Sewa alat <i>snorkeling</i>", "Nikmati keindahan bawah laut Selayar dengan alat snorkeling berkualitas, bersih, dan terawat.")}
<div class="grid2" style="margin-top:16px;align-items:start">
  <div>{img("bahuluang/14-snorkeling-makam-karang.jpg", 250)}</div>
  <div class="card"><div class="caps">Spesifikasi alat</div>
    <table style="margin-top:6px"><tr><td class="b">Snorkel</td><td>TUSA Hyperdry Snorkel</td></tr><tr><td class="b">Masker</td><td>TUSA Splash</td></tr><tr><td class="b">Fins</td><td>Cowfish / Alba</td></tr><tr><td class="b">Pelampung</td><td>Life jacket</td></tr></table></div>
</div>
<div class="grid2" style="margin-top:6px;gap:22px;align-items:start">
  <div><h2 style="font-size:20px">Paket <i>sewa</i></h2>
    {tbl(["Paket", "Harga"], [("Paket lengkap<br><span style='font-weight:400;font-size:12px'>Snorkel + masker + fins + life jacket</span>", rp(50000) + " /set /hari"), ("Paket tanpa life jacket<br><span style='font-weight:400;font-size:12px'>Snorkel + masker + fins</span>", rp(40000) + " /set /hari")], hi_last=True)}</div>
  <div><h2 style="font-size:20px">Sewa <i>satuan</i></h2>
    {tbl(["Alat", "Harga"], [("Snorkel", rp(15000) + " /hari"), ("Masker", rp(15000) + " /hari"), ("Fins", rp(15000) + " /hari"), ("Life jacket", rp(15000) + " /hari")], hi_last=True)}</div>
</div>
<h2 style="font-size:20px">Syarat &amp; <i>ketentuan</i></h2>
{ul(["Pembayaran dilakukan di awal sebelum alat digunakan.", "Kerusakan atau kehilangan alat menjadi tanggung jawab penyewa dan dikenakan biaya penggantian.", "Life jacket wajib digunakan bagi tamu yang belum mahir berenang.", "Sewa mengikuti ketersediaan stok alat di lokasi."])}
<div class="note">Alat snorkeling <b>sudah termasuk</b> dalam semua paket tur pulau (Bab 07). Pesan lewat katalog WhatsApp: <a class="lnk" href="https://wa.me/p/28508148958779838/6282189033044">wa.me/p/28508148958779838</a></div>''')

# =============================================================== 6 ACARA / VENUE
VENUES = [("Wantilan", 2500000, "60–80 orang", "Area utama yang tenang dan tertata, ideal untuk dinner semi formal, meeting, maupun presentasi."),
          ("Beach Club", 2000000, "40–60 orang", "Suasana santai di tepi pantai, ideal untuk lunch atau dinner santai, perayaan ulang tahun, dan acara sejenis."),
          ("Lapangan &amp; Panggung", 2000000, "100 orang", "Ruang terbuka yang luas, ideal untuk games, gathering, dan berbagai acara outdoor.")]
add(f'''{head("06", "Acara", "Sewa tempat <i>untuk acara</i>", "Meeting, gathering kantor, perayaan, hingga dinner semi formal di tepi Pantai Sunari.")}
<div class="grid3" style="margin-top:16px">{img("malam/02-bangunan-utama-malam.jpg", 165)}{img("taman/01-meja-di-taman.jpg", 165)}{img("malam/07-jalan-setapak-gazebo.jpg", 165)}</div>
<h2>Pilihan <i>venue</i></h2>
<p class="t" style="margin-top:2px">Waktu pemakaian <b>08.00–17.00 WITA</b></p>
<div class="grid3" style="margin-top:10px;align-items:stretch">
  {"".join(f'<div class="card vcard"><div class="caps">Kapasitas {c}</div><h3 style="margin-top:6px">{n}</h3><div class="pr">{rp(p)}</div><p class="t">{d}</p></div>' for n, p, c, d in VENUES)}
</div>
<p class="t" style="font-style:italic">Ketiga area dapat disewa sekaligus dalam satu acara, dengan harga sesuai tarif masing-masing.</p>
<h2 style="font-size:20px">Fasilitas <i>termasuk</i></h2>
{ul(["Venue, meja &amp; kursi", "Proyektor, LCD &amp; speaker", "Listrik", "Kebersihan area"], "cols")}''', toc=("Acara & venue", "Sewa tempat, fasilitas & ketentuan"))
add(f'''{head("06", "Acara", "Ketentuan <i>acara</i>")}
<div class="grid2" style="margin-top:14px;gap:16px;align-items:stretch">
  <div class="card"><h3>Konsumsi</h3>{ul(["Tamu dipersilakan membawa makanan &amp; peralatan makan sendiri", "Makanan wajib dalam kondisi <b>siap saji</b>"])}</div>
  <div class="card"><h3>Sewa peralatan makan</h3>{ul(["Mulai <b>Rp 1.500.000</b>, sudah termasuk service", "Piring saji, piring makan, sendok, garpu &amp; perlengkapan lain", "Harga menyesuaikan jumlah tamu"])}</div>
  <div class="card"><h3>Dekorasi</h3>{ul(["Diperbolehkan, termasuk dari vendor luar", "Pembersihan setelah acara dapat dilakukan oleh pihak tamu"])}</div>
  <div class="card"><h3>Penambahan waktu</h3>{ul(["Melewati pukul 17.00 dikenakan biaya <b>Rp 500.000</b>, atau sesuai kesepakatan"])}</div>
  <div class="card"><h3>Sound system</h3>{ul(["Penggunaan maksimal hingga <b>pukul 22.00</b>, demi kenyamanan tamu yang menginap"])}</div>
  <div class="card"><h3>Akomodasi</h3>{ul(["Peserta acara memperoleh <b>harga corporate</b> untuk kamar", "Tanpa minimum jumlah pemesanan"])}</div>
</div>
<h2 style="font-size:20px">Booking &amp; <i>pembayaran</i></h2>
{ul(["Pemesanan minimal <b>3 hari sebelum acara</b>", "<b>DP 50%</b> saat booking", "Pelunasan setelah acara selesai", "Reschedule dapat dilakukan dalam <b>6 bulan</b>; dana <b>tidak dapat dikembalikan</b>"], "cols")}
<div class="note">Kami dengan senang hati menyesuaikan paket sesuai kebutuhan acara Anda. Hubungi WhatsApp <b>{WA}</b> atau lihat katalog: <a class="lnk" href="https://wa.me/p/28083493487968437/6282189033044">wa.me/p/28083493487968437</a></div>''')

# =============================================================== 6 TUR
add(f'''{head("07", "Tur pulau", "Jelajah pulau <i>dari SunaRi</i>", "Pulau-pulau eksotis Selayar bisa dijelajahi langsung dari resort. Semua tur privat sudah termasuk kapal, alat snorkeling, lunchbox &amp; tiket masuk.")}
<div class="grid2" style="margin-top:16px">{img("pantai/03-pulau-di-seberang.jpg", 210, "50% 60%")}{img("bahuluang/10-air-dangkal-toska.jpg", 210, "50% 50%")}</div>
<p class="t" style="margin-top:8px;font-style:italic">Kiri: Pulau Gusung, terlihat langsung dari Pantai Sunari. Kanan: air toska Pulau Bahuluang.</p>
{tbl(["Paket", "Jenis", "Durasi", "Mulai dari"], [
  ("Tur Eksotis Pulau Gusung", "Privat · kapal", "1 hari (07.00–15.00)", rp(333750) + " /orang*"),
  ("Tur Eksotis Pulau Bahuluang", "Privat · mobil + kapal", "1 hari (07.00–16.00)", rp(652500) + " /orang*"),
  ("Tur Eksotis Polassi &amp; Tambolongan", "Privat · mobil + kapal", "1 hari (07.00–16.30)", rp(847500) + " /orang*"),
  ("Open Trip Jelajah Pulau Selayar", "Gabungan · min. 8 orang", "2 hari", rp(3000000) + " /orang")], right_from=3, hi_last=True)}
<p class="t" style="font-size:12px">*Harga per orang untuk rombongan 8 orang tanpa pemandu. Harga lengkap per jumlah tamu ada di halaman berikutnya.</p>
<div class="note"><b>Sebelum berangkat:</b> sarapan di SunaRi tersedia mulai 07.00. Jadwal dapat disesuaikan oleh kapten &amp; pemandu mengikuti cuaca, kondisi laut dan pasang-surut.</div>
<div class="grid3" style="margin-top:16px">{img("bahuluang/11-berjalan-ke-laut-dan-kapal.jpg", 190, "50% 50%")}{img("bahuluang/03-masuk-gua-lipang.jpg", 190, "50% 50%")}{img("bahuluang/05-kapal-menuju-pulau.jpg", 190, "50% 60%")}</div>''',
    toc=("Tur pulau", "Gusung, Bahuluang, Polassi & Tambolongan, Open Trip"))

def tour(title, sub, hl, rows, prices, incl, excl, car=False, photos=None):
    gl = lambda n: f"{n} orang"
    add(f'''<div class="tp">{head("07", "Tur pulau", title, sub)}
<div class="chips">{"".join(f'<span class="chip">{k} <b>{v}</b></span>' for k, v in hl)}</div>
<h2 style="font-size:18px;margin-top:14px">Jadwal <i>tur</i></h2>
<table>{"".join(f'<tr><td class="t">{t}</td><td>{a}</td></tr>' for t, a in rows)}</table>
<div class="grid2" style="margin-top:6px;gap:22px;align-items:start">
  <div><h2 style="font-size:18px;margin-top:10px">Harga <i>per orang</i></h2>
    {tbl(["Jumlah", "Tanpa pemandu", "Dgn pemandu"], [(gl(n), rp(x), rp(y)) for n, x, y in prices], hi_last=True)}{'<p class="t" style="font-size:12px;margin-top:6px">Armada: 1–4 orang 1 mobil · 5–8 orang 2 mobil.</p>' if car else ''}</div>
  <div><h2 style="font-size:18px;margin-top:10px">Termasuk</h2>{ul(incl)}<h2 style="font-size:18px;margin-top:10px">Tidak termasuk</h2>{ul(excl, "no")}</div>
</div>''' + ((f'<div class="grid3" style="margin-top:12px">{"".join(img(a, 140, b) for a, b in photos)}</div>' if len(photos) > 1 else f'<div style="margin-top:12px">{img(photos[0][0], 150, photos[0][1])}</div>') if photos else "") + "</div>")

EX = ["Pengeluaran pribadi &amp; belanja", "Dokumentasi foto/video tambahan"]
tour('Tur Eksotis <i>Pulau Gusung</i>', "Tur privat satu hari: hopping pulau &amp; snorkeling, langsung dengan kapal dari SunaRi.",
     [("Snorkeling", "Liang Kareta &amp; Jekneia"), ("Pantai", "Liang Kareta · Bone Malea"), ("Gua", "Balojaha")],
     [("07.00–08.00", "Persiapan &amp; sarapan di SunaRi."), ("08.00–08.30", "Berangkat dengan kapal sewa privat."), ("08.30–09.30", "<b>Snorkeling Liang Kareta:</b> terumbu karang &amp; biota laut."),
      ("09.30–10.30", "Pantai Liang Kareta, lanjut ke Pantai Bone Malea."), ("10.30–11.30", "<b>Pantai &amp; Gua Balojaha:</b> gua laut, foto &amp; berenang."), ("11.30–12.30", "Makan siang (lunchbox di lokasi)."),
      ("12.30–13.30", "<b>Snorkeling Jekneia:</b> taman karang bawah laut."), ("13.30–14.30", "Waktu bebas &amp; berenang (opsional: kayak)."), ("15.00", "Kembali ke SunaRi. Tur selesai.")],
     [(1,990000,1740000),(2,615000,990000),(3,490000,740000),(4,427500,615000),(5,390000,540000),(6,365000,490000),(7,347143,454286),(8,333750,427500)],
     ["Sewa kapal privat", "Alat snorkeling + pelampung", "Lunchbox + air mineral", "Tiket masuk destinasi", "Kapten &amp; kru berpengalaman", "Pemandu lokal (paket dgn pemandu)"],
     EX + ["Sewa kano/kayak opsional", "Tip kapten/kru/pemandu (sukarela)"],
     photos=[("gusung/04-udara-teluk-dan-terumbu.jpg", "50% 50%"), ("gusung/05-udara-pantai-dan-kapal.jpg", "50% 60%"), ("gusung/06-udara-dua-pantai.jpg", "50% 60%")])
tour('Tur Eksotis <i>Pulau Bahuluang</i>', "Jelajah pulau lewat jalur darat ke Desa Turungan, lalu kapal privat.",
     [("Snorkeling", "Makam Karang"), ("Pantai", "Pasir Timbul &amp; Pantai Bahuluang"), ("Gua", "Gua Lipang")],
     [("07.00–08.00", "Sarapan di SunaRi &amp; persiapan."), ("08.00–09.00", "Mobil privat ke Desa Turungan."), ("09.00–10.00", "Bertemu kapten, menyeberang ke Pulau Bahuluang."),
      ("10.00–11.00", "<b>Snorkeling Makam Karang:</b> formasi karang unik."), ("11.00–12.00", "<b>Pasir Timbul Bahuluang</b> (tergantung pasang-surut)."), ("12.00–13.00", "<b>Pantai Bahuluang</b> &amp; makan siang (lunchbox)."),
      ("13.00–14.00", "<b>Jelajah Gua Lipang</b> &amp; lanskap eksotis."), ("15.00–16.00", "Kembali ke SunaRi. Tur selesai.")],
     [(1,2640000,3540000),(2,1440000,1890000),(3,1040000,1340000),(4,840000,1065000),(5,900000,1080000),(6,790000,940000),(7,711429,840000),(8,652500,765000)],
     ["Mobil privat (resort ⇄ Turungan)", "Sewa kapal privat", "Alat snorkeling + pelampung", "Lunchbox + air mineral", "Tiket masuk destinasi", "Sopir &amp; BBM", "Pemandu lokal (paket dgn pemandu)"],
     EX + ["Aktivitas tambahan opsional", "Tip sopir/kapten/pemandu (sukarela)"], car=True,
     photos=[("bahuluang/07-gua-lipang-dalam.jpg", "50% 50%"), ("bahuluang/12-berjalan-di-pasir-timbul.jpg", "50% 55%"), ("bahuluang/14-snorkeling-makam-karang.jpg", "50% 50%")])
tour('Tur Eksotis <i>Polassi &amp; Tambolongan</i>', "Trekking Bukit Nane, hopping pulau &amp; snorkeling.",
     [("Trekking", "Bukit Nane ±15 menit"), ("Snorkeling", "Tambolongan"), ("Ikonik", "Pasir Timbul Tambolongan")],
     [("07.00–08.00", "Sarapan di SunaRi &amp; persiapan."), ("08.00–09.00", "Mobil privat ke Desa Turungan."), ("09.00–10.30", "Menyeberang ke Pulau Polassi."),
      ("10.30–11.45", "<b>Trekking Bukit Nane:</b> panorama laut &amp; foto."), ("11.45–13.00", "Pantai Bukit Nane, makan siang &amp; istirahat."), ("13.00–14.00", "<b>Pantai &amp; snorkeling Tambolongan.</b>"),
      ("14.00–15.00", "<b>Pasir Timbul Tambolongan</b> &amp; waktu bebas."), ("15.00–16.30", "Kembali ke SunaRi. Tur selesai.")],
     [(1,4147500,5047500),(2,2197500,2647500),(3,1547500,1847500),(4,1222500,1447500),(5,1207500,1387500),(6,1047500,1197500),(7,933214,1061786),(8,847500,960000)],
     ["Mobil privat (resort ⇄ Turungan)", "Sewa kapal privat", "Alat snorkeling + pelampung", "Lunchbox + air mineral", "Tiket Bukit Nane &amp; atraksi", "Sopir &amp; BBM", "Pemandu lokal (paket dgn pemandu)"],
     EX + ["Aktivitas tambahan opsional", "Tip sopir/kapten/pemandu (sukarela)"], car=True,
     photos=[("polassi-tambolongan/07-punggung-bukit-nane-dan-teluk.jpg", "50% 55%")])

add(f'''{head("07", "Tur pulau", "Open Trip <i>Jelajah Pulau Selayar</i>", "Wisata bahari 2 hari bersama peserta lain: temukan surga tersembunyi Sulawesi Selatan.")}
<div class="chips"><span class="chip">Harga <b>{rp(3000000)} /orang</b></span><span class="chip">Durasi <b>2 hari</b></span><span class="chip">Kuota min. <b>8 orang</b></span><span class="chip">Titik temu <b>penjemputan area/pelabuhan Selayar</b></span></div>
<div class="grid2" style="margin-top:12px;gap:22px;align-items:start">
  <div><h2 style="font-size:18px;margin-top:6px">Hari 1 · <i>Pulau Gusung</i></h2>{ul(["Penjemputan, briefing keselamatan &amp; pembagian alat snorkeling", "Pantai Balojaha: pasir putih &amp; air toska", "Pantai Liang Tarrusu: tebing kapur ikonik", "Pantai Bone Malea: makan siang lunchbox", "Pantai Liang Kareta: berenang &amp; snorkeling", "Kembali ke pelabuhan / resort"])}
    <h2 style="font-size:18px;margin-top:12px">Hari 2 · <i>Bahuluang &amp; Polassi</i></h2>{ul(["Penjemputan &amp; menuju pelabuhan", "Bukit Nane (Pulau Polassi): panorama 360°", "Pasi Timbul Polassi (tergantung pasang-surut)", "Makan siang di tepi pantai pulau", "Liang Lipang (Pulau Bahuluang): gua pesisir", "Snorkeling di Makam Karang", "Serah terima dokumentasi &amp; perpisahan"])}</div>
  <div><h2 style="font-size:18px;margin-top:6px">Termasuk</h2>{ul(["Antar-jemput titik temu/pelabuhan di Selayar", "Kapal hopping pulau bersama 2 hari", "Masker, snorkel &amp; pelampung", "Tiket &amp; izin semua destinasi", "Lunchbox &amp; air mineral 2 hari", "Pemandu lokal berlisensi", "Dokumentasi foto &amp; video bawah laut"])}
    <h2 style="font-size:18px;margin-top:12px">Tidak termasuk</h2>{ul(["Tiket pesawat/feri ke Selayar", "Penginapan (menginaplah di SunaRi)", "Pengeluaran pribadi", "Tip sukarela untuk kru &amp; pemandu"], "no")}
    <h2 style="font-size:18px;margin-top:12px">Yang perlu dibawa</h2>{ul(["Baju renang &amp; baju ganti", "Tabir surya ramah karang", "Kacamata hitam &amp; topi", "Dry bag untuk ponsel/kamera", "Sepatu air / sandal anti-selip"])}</div>
</div>
<div class="note"><b>Ketentuan:</b> minimal 8 orang per keberangkatan (jika tidak terpenuhi: penyesuaian harga, jadwal ulang atau refund penuh sesuai kesepakatan). Rute dapat berubah karena cuaca/gelombang. Sinyal di pulau terluar terbatas. Bukit Nane butuh kebugaran sedang.</div>''')

# =============================================================== 7 RUTE
add(f'''{head("08", "Rute &amp; akses", "Tiga jalan <i>menuju SunaRi</i>", "Dari Makassar, Selayar bisa dicapai lewat udara, darat + feri, atau kapal langsung.")}
<img class="img" src="{I}map__03_tiga_rute.jpg" style="height:330px;margin-top:14px;object-position:50% 50%" alt="Peta 3 rute">
<div class="grid3" style="margin-top:14px;align-items:start">
  <div class="card"><div class="caps" style="display:flex;gap:8px;align-items:center"><span class="num" style="background:#E8674A">1</span>Udara · tercepat</div>
    <div class="step"><span>Makassar (Sultan Hasanuddin) → Bandara H. Aroeppala</span><span class="d">±45 mnt</span></div>
    <div class="step"><span>Bandara → SunaRi (mobil)</span><span class="d">±10–15 mnt</span></div>
    <p class="t" style="font-size:12px">Cek jadwal maskapai H-7.</p></div>
  <div class="card"><div class="caps" style="display:flex;gap:8px;align-items:center"><span class="num" style="background:#2B8289">2</span>Darat &amp; feri</div>
    <div class="step"><span>Terminal Malengkeri → Pelabuhan Bira</span><span class="d">±4–5 jam</span></div>
    <div class="step"><span>Feri Bira → Pamatata (ASDP)</span><span class="d">±2 jam</span></div>
    <div class="step"><span>Pamatata → SunaRi</span><span class="d">±1–1,5 jam</span></div>
    <p class="t" style="font-size:12px">Penyeberangan pagi &amp; siang.</p></div>
  <div class="card"><div class="caps" style="display:flex;gap:8px;align-items:center"><span class="num" style="background:#D8932D">3</span>Kapal langsung</div>
    <div class="step"><span>KM Dharma Kartika III: Makassar → Benteng</span><span class="d">±10–11 jam</span></div>
    <div class="step"><span>Benteng → SunaRi (mobil)</span><span class="d">±20–30 mnt</span></div>
    <p class="t" style="font-size:12px">Berangkat malam, tiba pagi. Tidak setiap hari.</p></div>
</div>''', toc=("Rute & akses", "Peta, 3 rute & tarif antar-jemput"))

LOCAL = [("Bandara H. Aroeppala ↔ SunaRi", 150000, 300000), ("Pelabuhan Benteng ↔ SunaRi", 200000, 400000), ("Pelabuhan Pamatata ↔ SunaRi", 400000, 800000)]
A = [1950000, 2000000, 2050000, 2100000, 4050000, 4100000, 4150000, 4200000]
B = [1100000, 1550000, 2000000, 2450000, 3550000, 4000000, 4450000, 4900000]
add(f'''{head("08", "Rute &amp; akses", "Antar-jemput <i>&amp; transfer</i>", "Kendaraan privat khusus rombongan Anda, sudah termasuk sopir, BBM &amp; parkir.")}
<h2 style="font-size:18px;margin-top:14px">Shuttle lokal Selayar <i>(sekali jalan)</i></h2>
{tbl(["Rute", "1–4 tamu (1 mobil)", "5–8 tamu (2 mobil)"], [(r, rp(a), rp(b)) for r, a, b in LOCAL])}
<h2 style="font-size:18px;margin-top:18px">Transfer Makassar ↔ SunaRi <i>(total per rombongan)</i></h2>
<div class="grid2" style="gap:22px;align-items:start">
  <div><div class="caps" style="margin-top:6px">Opsi A · Mobil privat penuh</div><p class="t" style="font-size:12px">Mobil privat langsung termasuk penyeberangan feri. Paling nyaman.</p>
    {tbl(["Tamu", "Armada", "Total"], [(f"{n} tamu", "1 mobil" if n <= 4 else "2 mobil", rp(v)) for n, v in zip(range(1, 9), A)], right_from=2, hi_last=True)}</div>
  <div><div class="caps" style="margin-top:6px">Opsi B · Bus premium + shuttle</div><p class="t" style="font-size:12px">Bus sleeper/eksekutif Makassar–Pamatata + shuttle privat. Lebih hemat.</p>
    {tbl(["Tamu", "Layanan", "Total"], [(f"{n} tamu", "1 mobil + bus" if n <= 4 else "2 mobil + bus", rp(v)) for n, v in zip(range(1, 9), B)], right_from=2, hi_last=True)}</div>
</div>
<div class="note"><b>Ketentuan:</b> 1 mobil maks. 4 tamu + 4 koper sedang. Tiket feri &amp; bus dihitung per orang sesuai tarif resmi operator. Konfirmasi jadwal kedatangan &amp; data penumpang paling lambat H-1 via WhatsApp {WA}.</div>''')

# =============================================================== 8 RESERVASI + FAQ
FAQ = [("Jam check-in &amp; check-out?", "Check-in mulai 14.00 WITA, check-out paling lambat 12.00 WITA."),
       ("Sudah termasuk sarapan?", "Ya, semua tipe kamar."),
       ("Kamar mana yang ada air panas?", "Hanya VIP Superior Bungalow (bathtub &amp; air panas)."),
       ("Bisa tambah extra bed?", "Bisa, berbayar: 1 untuk tipe 2 orang, 2 untuk Family Superior."),
       ("Aman untuk anak-anak?", "Pantai Sunari landai &amp; aman untuk anak."),
       ("Tamu luar boleh ke resto?", "Boleh, Bajoy Beach Resto buka 07.00–19.00 untuk tamu tidak menginap."),
       ("Ayunan raksasa berbayar?", "Tidak, ayunan raksasa gratis."),
       ("Bisa dijemput di bandara?", "Bisa, berbayar. Lihat tarif di Bab 08.")]
add(f'''{head("09", "Reservasi", "Cara <i>reservasi</i>", "Cukup 3 langkah lewat WhatsApp, tanpa aplikasi lain.")}
<div class="grid3" style="margin-top:16px;align-items:stretch">
  {"".join(f'<div class="card"><span class="num" style="width:34px;height:34px;font-size:18px;background:linear-gradient(180deg,#FDB15D,#FF8A5C)">{i}</span><h3 style="margin-top:10px">{h}</h3><p class="t">{t}</p></div>' for i, (h, t) in enumerate([("Chat admin", f"Hubungi WhatsApp <b>{WA}</b>."), ("Kirim data", "Tanggal check-in &amp; check-out, jumlah tamu (dewasa &amp; anak), tipe kamar, perlu antar-jemput atau tidak."), ("Bayar &amp; selesai", "Admin kirim harga &amp; ketersediaan → transfer &amp; kirim bukti → booking terkonfirmasi.")], 1))}
</div>
<div class="note">Mau sekalian <b>Senja Dinner</b>, <b>tur pulau</b> atau <b>antar-jemput</b>? Tulis di chat yang sama, admin akan mengatur semuanya.</div>
<h2>Pertanyaan yang <i>sering ditanyakan</i></h2>
<div class="grid2" style="margin-top:10px;gap:10px 22px">
  {"".join(f'<div style="padding:9px 0;border-bottom:1px solid rgba(138,95,72,.22)"><div style="font-family:Playfair Display,serif;font-size:14.5px">{q}</div><div class="t" style="font-size:11.5px;margin-top:3px;color:rgba(69,48,31,.85)">{a}</div></div>' for q, a in FAQ)}
</div>''', toc=("Reservasi & FAQ", "3 langkah reservasi & tanya-jawab"))

# =============================================================== BACK COVER
add(f'''<img src="{I}cover__belakang-senja.jpg" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:50% 45%" alt="">
<img src="../assets/logo-sunari-color-dark.png" style="position:absolute;left:50%;transform:translateX(-50%);top:70px;width:270px" alt="">
<div style="position:absolute;left:70px;right:70px;bottom:60px;text-align:center;color:#FBF4EC">
  <div style="font-family:'Playfair Display',serif;font-size:42px;line-height:1.15;margin-top:26px">Sampai jumpa<br>di <i style="color:#FDB15D">Pantai Sunari.</i></div>
  <div style="margin-top:34px;padding:22px 26px;border-radius:20px;background:rgba(251,244,236,.95);color:#45301F;text-align:left;font-size:12.5px;line-height:1.7;text-shadow:none">
    <div class="caps">Reservasi &amp; informasi</div>
    <div style="font-family:'Playfair Display',serif;font-size:26px;margin-top:4px">WhatsApp {WA}</div>
    <div>Instagram <b>{IG}</b></div>
    <div>Jl. Poros Benteng – Appatana KM 14, Dusun Tile-Tile Utara, Desa Patikarya, Kec. Bontosikuyu, Kab. Kepulauan Selayar, Sulawesi Selatan</div>
    <div>Google Maps: maps.app.goo.gl/iUWWHNCT7Vyu4i537</div>
  </div>
  <div style="font-size:9.5px;letter-spacing:.2em;text-transform:uppercase;margin-top:22px;opacity:.85">Informasi &amp; harga dapat berubah sewaktu-waktu · Edisi 2026</div>
</div>''', cls="cover")

# =============================================================== assemble (page numbers + TOC)
total = len(PAGES)
toc_rows = ""
for idx, (toc, _, _) in enumerate(PAGES, 1):
    if toc:
        no = sum(1 for t, _, _ in PAGES[:idx] if t)
        toc_rows += f'<a><span class="no">{no:02d}</span><span class="ti">{toc[0]}</span><span class="ds">{toc[1]}</span><span class="dots"></span><span class="pg">{idx}</span></a>'
toc_html = f'''{head("", "Daftar isi", "Isi <i>panduan</i>", "Panduan ini disusun untuk membantu Anda merencanakan perjalanan ke SunaRi, dari memilih kamar hingga tiba di Pantai Sunari.")}
<div class="toc" style="margin-top:22px">{toc_rows}</div>
<div class="grid3" style="margin-top:30px">{img("senja/17-kayak-berdua.jpg", 160)}{img("aktivitas/05-ayunan-raksasa-senja.jpg", 160, "40% 55%")}{img("malam/03-resort-malam-a-frame.jpg", 160)}</div>'''
html = ""
for idx, (toc, body, cls) in enumerate(PAGES, 1):
    if body == "__TOC__": body = toc_html
    run = "" if cls == "cover" else f'<div class="run"><span>SunaRi Beach Resort Selayar · Panduan Tamu</span><b>{idx}</b></div>'
    pad = ' style="padding:0"' if cls == "cover" else ""
    html += f'<div class="page {cls}"{pad}>{body}{run}</div>\n'
(H / "ebook.html").write_text(f'<!doctype html><html lang="id"><head><meta charset="utf-8"><title>Panduan Lengkap SunaRi Beach Resort Selayar</title>{FONTS}<style>{CSS}</style></head><body>{html}</body></html>')
print(total, "halaman")
