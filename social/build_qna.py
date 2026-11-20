"""Story Q&A SunaRi (1080x1920): pertanyaan yang sering ditanyakan tamu sebelum menginap.
Run: python3 social/build_qna.py && node social/render_qna.js  -> social/story-qna/*.png"""
import pathlib
H = pathlib.Path(__file__).parent
WA = "0821-8903-3044"
IG = "@sunaribeachresortselayar"
LOGO = "../assets/logo-sunari-color.png"
P = "../assets/photos/"
FONTS = '<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;1,400;1,500&family=Montserrat:wght@400;500;600;700&display=swap" rel="stylesheet">'
CSS = """
*{margin:0;padding:0;box-sizing:border-box}
body{background:#ccc;font-family:Montserrat,sans-serif;color:#45301F}
.s{width:1080px;height:1920px;background:#FBF4EC;position:relative;overflow:hidden;margin:30px auto}
.top{position:absolute;left:72px;right:72px;top:118px;display:flex;align-items:center}
.top img{width:230px;filter:drop-shadow(0 1.5px 0 #fff) drop-shadow(1px 2px 2px rgba(60,40,30,.25))}
.caps{font-weight:600;text-transform:uppercase;letter-spacing:.24em;color:#8A5F48}
.top .caps{margin-left:auto;font-size:22px}
.body{position:absolute;left:72px;right:72px;top:260px}
.body.center{top:250px;bottom:330px;display:flex;flex-direction:column;justify-content:center}
.pf{font-family:'Playfair Display',serif;font-weight:500}
.it{font-style:italic;color:#A67C64}
.emb{text-shadow:0 1.5px 0 #fff,1px 2.5px 3px rgba(90,62,49,.22)}
.photo{width:100%;height:700px;object-fit:cover;border-radius:30px;display:block;box-shadow:0 2px 0 #fff,0 10px 30px rgba(90,62,49,.18)}
/* question sticker */
.q{position:relative;margin:0 34px;background:#FFFDF9;border-radius:36px;overflow:hidden;box-shadow:0 18px 40px rgba(90,62,49,.16),0 2px 6px rgba(90,62,49,.10)}
.photo+.q{margin-top:-110px}
.q .band{background:linear-gradient(90deg,#FDB15D,#FF8A5C);padding:22px 0;text-align:center;font-weight:700;font-size:23px;letter-spacing:.24em;text-transform:uppercase;color:#fff}
.q .txt{padding:40px 50px 46px;text-align:center;font-family:'Playfair Display',serif;font-weight:500;font-size:62px;line-height:1.15}
.a{margin-top:60px}
.a .lbl{display:flex;align-items:center;gap:20px;font-size:22px}
.a .lbl::after{content:"";flex:1;height:2px;border-top:1px solid rgba(138,95,72,.45);border-bottom:1px solid #fff}
.a .main{font-family:'Playfair Display',serif;font-weight:500;font-size:64px;line-height:1.15;margin-top:26px}
.a p{font-size:36px;line-height:1.5;margin-top:22px}
.a p b{font-weight:600}
.list{margin-top:26px;border-top:1px solid rgba(138,95,72,.35)}
.list div{display:flex;justify-content:space-between;gap:24px;padding:22px 0;border-bottom:1px solid rgba(138,95,72,.35);font-size:33px;line-height:1.35}
.list div span:last-child{text-align:right;color:#8A5F48;font-weight:600}
.list.one div{display:block}
.steps>div{display:flex;gap:30px;align-items:flex-start;margin-top:34px}
.steps .n{flex:none;width:76px;height:76px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-family:'Playfair Display',serif;font-size:38px;color:#fff;background:linear-gradient(180deg,#FDB15D,#FF8A5C);box-shadow:0 2px 0 #fff,0 4px 10px rgba(224,122,75,.3)}
.steps h4{font-family:'Playfair Display',serif;font-weight:500;font-size:44px}
.steps p{font-size:32px;line-height:1.45;margin-top:4px}
.ft{position:absolute;left:72px;right:72px;bottom:240px;display:flex;justify-content:space-between;font-size:20px;padding-top:22px}
.ft::before{content:"";position:absolute;left:0;right:0;top:0;height:2px;border-top:1px solid rgba(138,95,72,.45);border-bottom:1px solid #fff}
.sun{display:block;margin:0 auto}
"""
SUN = '''<svg class="sun" viewBox="0 0 200 200" width="{w}" height="{w}"><defs><linearGradient id="sg{u}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FDB15D"/><stop offset="1" stop-color="#FF8A5C"/></linearGradient>
<mask id="sm{u}"><rect width="200" height="200" fill="white"/><rect y="112" width="200" height="5"/><rect y="126" width="200" height="7"/><rect y="142" width="200" height="9"/><rect y="160" width="200" height="11"/><rect y="180" width="200" height="13"/></mask></defs>
<circle cx="100" cy="100" r="96" fill="url(#sg{u})" mask="url(#sm{u})"/></svg>'''
sun = lambda w, u: SUN.format(w=w, u=u)

SL = []
def shell(sid, inner, n=None, center=False):
    tag = f"Tanya SunaRi · {n:02d}" if n else "Tanya SunaRi"
    SL.append(f'''<div class="s" id="{sid}"><div class="top"><img src="{LOGO}" alt=""><span class="caps">{tag}</span></div>
  <div class="body{" center" if center else ""}">{inner}</div>
  <div class="ft"><span class="caps">WA {WA}</span><span class="caps">{IG}</span></div></div>''')
def qa(q, answer, photo=None, pos="50% 50%"):
    ph = f'<img class="photo" src="{P}{photo}" style="object-position:{pos}" alt="">' if photo else ""
    n = len(SL)
    shell(f"qna-{n:02d}", f'''{ph}<div class="q"><div class="band">Tanya SunaRi</div><div class="txt">{q}</div></div>
  <div class="a"><div class="lbl caps">Jawab</div>{answer}</div>''', n, center=not photo)
def lst(rows, one=False):
    if one: return f'<div class="list one">' + "".join(f"<div>{r}</div>" for r in rows) + "</div>"
    return '<div class="list">' + "".join(f"<div><span>{a}</span><span>{b}</span></div>" for a, b in rows) + "</div>"
def steps(rows):
    return '<div class="steps">' + "".join(f'<div><div class="n">{i}</div><div><h4>{h}</h4><p>{t}</p></div></div>' for i, (h, t) in enumerate(rows, 1)) + "</div>"

# 01 cover
SL.append(f'''<div class="s" id="qna-00-sampul"><img src="{P}senja/12-kayak-matahari-merah-story.jpg" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover" alt="">
  <div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(40,26,18,.55) 0%,rgba(40,26,18,0) 30%,rgba(40,26,18,0) 45%,rgba(40,26,18,.75) 100%)"></div>
  <img src="../assets/logo-sunari-color-dark.png" style="position:absolute;left:50%;transform:translateX(-50%);top:150px;width:340px" alt="">
  <div style="position:absolute;left:72px;right:72px;bottom:300px;text-align:center;color:#FBF4EC">
    <div class="caps" style="color:#FDB15D;font-size:24px">Sebelum menginap</div>
    <div class="pf" style="font-size:112px;line-height:1.05;margin-top:24px;text-shadow:0 4px 20px rgba(0,0,0,.35)">Tanya <i style="color:#FDB15D">SunaRi</i></div>
    <div style="font-size:36px;line-height:1.5;margin-top:28px">Jawaban untuk pertanyaan yang paling sering ditanyakan tamu</div>
    <div class="caps" style="color:#FBF4EC;font-size:22px;margin-top:50px">Ketuk untuk lanjut &nbsp;→</div></div></div>''')

qa("Jam berapa check-in &amp; check-out?",
   '<div class="main emb">Check-in <span class="it">14.00</span><br>Check-out <span class="it">12.00</span> WITA</div><p>Ingin datang lebih awal atau pulang lebih sore? Tanyakan dulu lewat WhatsApp sebelum tiba.</p>',
   "vip-standard-bungalow/01-eksterior-rumah-panggung.jpg", "50% 55%")
qa("Apakah sudah termasuk sarapan?",
   '<div class="main emb">Ya, <span class="it">semua kamar</span> sudah termasuk sarapan.</div><p>Disajikan di <b>Bajoy Beach Resto</b>, menghadap Pantai Sunari.</p>',
   "resto/01-tamu-makan-siang.jpg", "50% 55%")
qa("Ada Wi-Fi dan AC di kamar?",
   '<div class="main emb">Ada, di <span class="it">semua</span> tipe bungalow.</div><p>Tetap terhubung, tetapi kami sarankan sesekali simpan ponsel saat senja datang.</p>',
   "standard-bungalow/03-kamar-depan.jpg", "50% 55%")
qa("Tipe kamar apa saja &amp; untuk berapa orang?",
   lst([("Standard Bungalow", "2 org · queen"), ("VIP Standard Bungalow", "2 org · king"), ("Superior Bungalow", "2 org · king · TV"),
        ("VIP Superior Bungalow", "2 org · king · bathtub"), ("Family Superior Bungalow", "6 org · 2 lantai")])
   + '<p>Semua bungalow punya <b>teras pribadi</b>. Tipe 2 orang bisa sampai 3 orang dengan extra bed, Family Superior sampai 8 orang.</p>')
qa("Kamar mana yang ada air panas?",
   '<div class="main emb">Hanya <span class="it">VIP Superior</span> Bungalow.</div><p>Kelas tertinggi kami: air panas, <b>bathtub</b> di kamar mandi semi-outdoor, king bed, TV dan mini bar.</p>',
   "vip-superior-bungalow/06-bathtub-semi-outdoor.jpg", "50% 55%")
qa("Bisa tambah extra bed?",
   '<div class="main emb">Bisa, dengan <span class="it">biaya tambahan</span>.</div>'
   + lst(["Standard, VIP Standard, Superior &amp; VIP Superior: <b>1 extra bed</b> (maks. 3 orang)", "Family Superior: <b>2 extra bed</b> (maks. 8 orang)"], one=True),
   "family-superior-bungalow/09-lantai-atas-4-kasur.jpg", "50% 55%")
qa("Aman untuk anak-anak?",
   '<div class="main emb">Pantai Sunari <span class="it">landai</span> &amp; aman untuk anak.</div><p>Untuk keluarga besar, <b>Family Superior Bungalow</b>: 2 lantai, kamar mandi di kedua lantai, untuk 6 orang (maks. 8).</p>',
   "family-superior-bungalow/01-eksterior-taman.jpg", "55% 50%")
qa("Bisa lihat sunset dari resort?",
   '<div class="main emb">Matahari terbenam <span class="it">tepat di depan</span> Pantai Sunari.</div><p>Sekitar pukul <b>17.50–18.00 WITA</b>, paling cantik di bulan <b>April–Desember</b>. Teras <b>VIP Standard</b> menghadap langsung ke arah matahari terbenam.</p>',
   "senja/07-payung-kursi-pantai.jpg", "50% 60%")
qa("Ada restoran di resort?",
   '<div class="main emb">Ada, <span class="it">Bajoy Beach Resto</span>.</div>'
   + lst([("Tamu menginap", "07.00–21.00"), ("Tamu tidak menginap", "07.00–19.00")])
   + '<p>Menu harian, ikan bakar &amp; seafood.</p>',
   "resto/04-resto-malam-pohon-kelapa.jpg", "50% 65%")
qa("Bisa makan malam saat senja?",
   '<div class="main emb">Bisa, <span class="it">Senja Dinner</span>.</div><p>Ikan bakar &amp; seafood di tepi pantai saat matahari terbenam. <b>Pesan paling lambat H-1</b> lewat WhatsApp.</p>',
   "resto/05-makan-malam-taman.jpg", "50% 60%")
qa("Bagaimana cara ke Selayar?",
   steps([("Pesawat", "Makassar ke Bandara H. Aroeppala, Selayar."),
          ("Darat + kapal feri", "Makassar ke Pelabuhan Bira (Bulukumba), lalu feri ke Pelabuhan Pamatata."),
          ("Lanjut ke SunaRi", "Jl. Poros Benteng–Appatana KM 14, Bontosikuyu. Bisa kami jemput.")]))
qa("Ada layanan antar-jemput?",
   '<div class="main emb">Ada, <span class="it">berbayar</span>, kendaraan privat.</div>'
   + lst(["Bandara H. Aroeppala ↔ SunaRi", "Pelabuhan Benteng ↔ SunaRi", "Pelabuhan Pamatata ↔ SunaRi", "Transfer dari Makassar (mobil privat atau bus + shuttle)"], one=True)
   + '<p>Daftar tarif lengkap kami kirim lewat WhatsApp. Konfirmasi jadwal paling lambat <b>H-1</b>.</p>')
qa("Ada aktivitas apa saja?",
   lst([("Sewa kayak single", "Rp 50.000"), ("Sewa kayak double", "Rp 100.000"), ("Ayunan raksasa", "gratis"), ("Tur pulau &amp; snorkeling", "info via WA")]),
   "aktivitas/03-ayunan-senja.jpg", "50% 55%")
qa("Bisa ikut tur ke pulau-pulau sekitar?",
   '<div class="main emb">Bisa, berangkat <span class="it">dari SunaRi</span>.</div>'
   + lst([("Pulau Gusung", "tur privat"), ("Pulau Bahuluang", "tur privat"), ("Polassi &amp; Tambolongan", "tur privat"), ("Jelajah Selayar", "open trip 2 hari")])
   + '<p><b>Pulau Gusung</b> terlihat langsung dari Pantai Sunari. Sudah termasuk kapal, alat snorkeling &amp; lunchbox. Detail paket kami kirim lewat WhatsApp.</p>')
qa("Berapa harga kamar &amp; cara pesannya?",
   '<p style="margin-top:0">Harga &amp; ketersediaan kami kirim <b>langsung lewat WhatsApp</b>, sesuai tanggal &amp; tipe kamar.</p>'
   + steps([("Kirim data", "tanggal check-in &amp; check-out, jumlah tamu, tipe kamar"), ("Terima penawaran", "harga &amp; ketersediaan terbaru"), ("Bayar &amp; konfirmasi", "kirim bukti transfer, booking terkonfirmasi")]))
qa("Di mana lokasi SunaRi?",
   '<div class="main emb" style="font-size:52px">Pantai Sunari, <span class="it">Selayar</span></div><p>Jl. Poros Benteng – Appatana KM 14, Dusun Tile-Tile Utara, Desa Patikarya, Kec. Bontosikuyu, Kab. Kepulauan Selayar, Sulawesi Selatan.</p><p class="caps" style="font-size:22px;margin-top:30px">Ketuk stiker lokasi / link Google Maps</p>',
   "malam/02-bangunan-utama-malam.jpg", "50% 60%")

# closing CTA
SL.append(f'''<div class="s" id="qna-{len(SL):02d}-penutup"><div class="top"><img src="{LOGO}" alt=""><span class="caps">Tanya SunaRi</span></div>
  <div class="body" style="top:420px;text-align:center">{sun(120, "c")}
    <div class="caps" style="font-size:24px;margin-top:40px">Masih ada pertanyaan?</div>
    <div class="pf emb" style="font-size:96px;line-height:1.08;margin-top:24px">Tanya <span class="it">langsung</span><br>saja, Kak</div>
    <p style="font-size:36px;line-height:1.5;margin-top:34px">Kami balas secepatnya, termasuk harga kamar, Senja Dinner, antar-jemput &amp; tur pulau.</p>
    <div style="margin-top:80px;padding:44px 0;border-radius:36px;background:#FFFDF9;box-shadow:0 18px 40px rgba(90,62,49,.14)">
      <div class="caps" style="font-size:22px">WhatsApp</div><div class="pf" style="font-size:80px;margin-top:10px">{WA}</div></div>
    <div class="caps" style="font-size:22px;margin-top:50px">Atau kirim lewat stiker pertanyaan di story kami</div></div>
  <div class="ft"><span class="caps">SunaRi · Selayar</span><span class="caps">{IG}</span></div></div>''')

# templates for real question-sticker replies (IG sticker is pasted in the empty area)
SL.append(f'''<div class="s" id="qna-template-ajukan"><div class="top"><img src="{LOGO}" alt=""><span class="caps">Tanya SunaRi</span></div>
  <div class="body" style="top:380px;text-align:center">{sun(110, "t1")}
    <div class="pf emb" style="font-size:96px;line-height:1.08;margin-top:36px">Mau tanya apa<br>tentang <span class="it">SunaRi?</span></div>
    <p style="font-size:34px;line-height:1.5;margin-top:30px">Kamar, sarapan, senja, aktivitas, cara ke Selayar, tanya saja.</p>
    <div style="margin:70px auto 0;width:760px;height:420px;border-radius:36px;border:3px dashed rgba(138,95,72,.45);display:flex;align-items:center;justify-content:center">
      <span class="caps" style="font-size:22px;opacity:.7">Tempel stiker "Pertanyaan" di sini</span></div></div>
  <div class="ft"><span class="caps">WA {WA}</span><span class="caps">{IG}</span></div></div>''')
SL.append(f'''<div class="s" id="qna-template-jawab"><div class="top"><img src="{LOGO}" alt=""><span class="caps">Tanya SunaRi</span></div>
  <div class="body">
    <div style="width:100%;height:520px;border-radius:36px;border:3px dashed rgba(138,95,72,.45);display:flex;align-items:center;justify-content:center">
      <span class="caps" style="font-size:22px;opacity:.7">Tempel balasan stiker pertanyaan di sini</span></div>
    <div class="a"><div class="lbl caps">Jawab</div><div class="main emb" style="color:rgba(69,48,31,.35)">Tulis jawaban singkat di sini</div>
    <p style="color:rgba(69,48,31,.35)">Tambahkan detail di baris ini. Gunakan teks Instagram dengan font serif &amp; warna Driftwood Deep.</p></div></div>
  <div class="ft"><span class="caps">WA {WA}</span><span class="caps">{IG}</span></div></div>''')

(H / "qna.html").write_text(f'<!doctype html><html lang="id"><head><meta charset="utf-8">{FONTS}<style>{CSS}</style></head><body>{"".join(SL)}</body></html>')
print(len(SL), "story")
