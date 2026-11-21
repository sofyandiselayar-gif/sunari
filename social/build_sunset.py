"""Seri "Panduan Senja": tips sunset & foto sunset di SunaRi. Carousel feed 1080x1350 + story 1080x1920.
Run: python3 social/build_sunset.py && node social/render_sunset.js  -> social/sunset-guide/*.png"""
import pathlib
H = pathlib.Path(__file__).parent
WA = "0821-8903-3044"; IG = "@sunaribeachresortselayar"
LOGO = "../assets/logo-sunari-color.png"; LOGO_D = "../assets/logo-sunari-color-dark.png"; P = "../assets/photos/"
FONTS = '<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;1,400;1,500&family=Montserrat:wght@400;500;600;700&display=swap" rel="stylesheet">'
CSS = """
*{margin:0;padding:0;box-sizing:border-box}
body{background:#bbb;font-family:Montserrat,sans-serif;color:#3B2819}
.t{position:relative;overflow:hidden;margin:30px auto;background:#FBF4EC}
.f{width:1080px;height:1350px}.s{width:1080px;height:1920px}
.bg{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.sh{text-shadow:0 2px 14px rgba(0,0,0,.6),0 1px 3px rgba(0,0,0,.45)}
.pf{font-family:'Playfair Display',serif;font-weight:500}
.it{font-style:italic;color:#9A6A4F}
.gold{color:#FDB15D}
.caps{font-weight:700;text-transform:uppercase;letter-spacing:.24em;color:#7A5039}
.top{position:absolute;left:72px;right:72px;top:64px;display:flex;align-items:center;justify-content:space-between}
.top img{width:230px}.top .caps{font-size:20px}
.ft{position:absolute;left:72px;right:72px;bottom:60px;display:flex;justify-content:space-between;font-weight:700;font-size:18px;letter-spacing:.22em;text-transform:uppercase;color:#7A5039;padding-top:20px;border-top:1.5px solid rgba(138,95,72,.35)}
.ft.l{color:#FBF4EC;border-top-color:rgba(251,244,236,.45)}
.time{font-family:'Playfair Display',serif;font-weight:500;line-height:1;letter-spacing:-.01em}
.row{display:flex;align-items:baseline;gap:34px;padding:22px 0;border-bottom:1.5px solid rgba(138,95,72,.22)}
.row:last-child{border-bottom:none}
.row .time{font-size:64px;color:#E07A4B;width:200px;flex:none}
.row .tx b{display:block;font-family:'Playfair Display',serif;font-weight:500;font-size:38px;color:#3B2819}
.row .tx span{font-size:25px;color:#5A3E31;line-height:1.4}
.photo{border-radius:30px;object-fit:cover;display:block;width:100%}
.tag{display:inline-block;font-weight:700;font-size:20px;letter-spacing:.2em;text-transform:uppercase;color:#fff;background:linear-gradient(90deg,#FDB15D,#FF8A5C);padding:12px 22px;border-radius:999px}
ul.tips{list-style:none;margin-top:18px}
ul.tips li{display:flex;gap:22px;padding:20px 0;border-bottom:1.5px solid rgba(138,95,72,.22);font-size:28px;line-height:1.4;color:#3B2819}
ul.tips li:last-child{border-bottom:none}
ul.tips li i{flex:none;font-style:normal;font-family:'Playfair Display',serif;font-size:34px;color:#E07A4B;width:44px}
ul.tips li b{font-weight:700}
.mid{position:absolute;left:72px;right:72px;top:150px;bottom:140px;display:flex;flex-direction:column;justify-content:center}
.card{background:#FFFDF9;border-radius:32px;padding:40px 44px;box-shadow:0 18px 44px rgba(90,62,49,.12)}
"""
T = []
def foot(n, light=False, total=20):
    return f'<div class="ft{" l" if light else ""}"><span>SunaRi · Selayar</span><span>{n:02d} / {total:02d}</span></div>'

# ================================================================== CAROUSEL (20)
# 1 cover
T.append(f'''<div class="t f" id="sunset-01"><img class="bg" src="{P}senja/31-kayak-siluet-matahari-merah-story.jpg" style="object-position:50% 30%" alt="">
  <div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,.5) 0%,rgba(0,0,0,.15) 40%,rgba(0,0,0,0) 55%,rgba(0,0,0,.35) 100%)"></div>
  <img src="{LOGO_D}" style="position:absolute;left:72px;top:60px;width:240px;filter:drop-shadow(0 2px 8px rgba(0,0,0,.45))" alt="">
  <div class="sh" style="position:absolute;left:72px;right:72px;top:220px;color:#FBF4EC">
    <div style="font-weight:700;font-size:22px;letter-spacing:.28em;text-transform:uppercase;color:#FDB15D">Panduan senja · Pantai Sunari</div>
    <div class="time" style="font-size:210px;margin-top:8px">17.50</div>
    <div class="pf" style="font-size:60px;line-height:1.1;margin-top:4px">Jam paling ditunggu <i class="gold">di Selayar.</i></div></div>
  <div class="sh" style="position:absolute;left:72px;right:72px;bottom:130px;color:#FBF4EC;font-size:28px">Waktu terbaik, spot foto &amp; tips memotret senja. Simpan postingan&nbsp;ini&nbsp;↓</div>
  {foot(1, True)}</div>''')


def head_slide(n, label, title):
    return f'<div class="top"><img src="{LOGO}" alt=""><span class="caps">{label}</span></div>'
def text_slide(n, label, title, body):
    T.append(f'''<div class="t f" id="sunset-{n:02d}">{head_slide(n, label, title)}
  <div class="mid"><div class="pf" style="font-size:64px;line-height:1.06">{title}</div>{body}</div>{foot(n)}</div>''')
def tips(items, size=28):
    return '<ul class="tips">' + "".join(f'<li><i>{i}</i><span style="font-size:{size}px">{t}</span></li>' for i, t in enumerate(items, 1)) + '</ul>'
def photo_slide(n, img, pos, kicker, big, text, grad=True, size=112):
    g = '<div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,.35) 0%,rgba(0,0,0,0) 30%,rgba(0,0,0,0) 45%,rgba(0,0,0,.65) 100%)"></div>' if grad else ''
    T.append(f'''<div class="t f" id="sunset-{n:02d}"><img class="bg" src="{P}{img}" style="object-position:{pos}" alt="">{g}
  <img src="{LOGO_D}" style="position:absolute;left:72px;top:60px;width:230px" alt="">
  <div class="sh" style="position:absolute;left:72px;right:72px;bottom:150px;color:#FBF4EC">
    <div style="font-weight:700;font-size:22px;letter-spacing:.28em;text-transform:uppercase;color:#FDB15D">{kicker}</div>
    <div class="pf" style="font-size:{size}px;line-height:1.04;margin-top:10px">{big}</div>
    <div style="font-size:29px;line-height:1.5;margin-top:20px">{text}</div></div>{foot(n, True)}</div>''')

# 2 why
photo_slide(2, "pantai/03-pulau-di-seberang.jpg", "50% 60%", "Kenapa Pantai Sunari?", "Senja tepat <i class='gold'>di depan mata.</i>",
  "Pantai Sunari ada di pesisir <b>barat</b> Pulau Selayar. Matahari turun lurus ke laut lepas, tanpa terhalang daratan. Laut tenang, pantai landai, dan Pulau Gusung di seberang.")

# 3 timeline
text_slide(3, "Jadwal sore ideal", 'Satu sore, <span class="it">tanpa&nbsp;terburu&#8209;buru</span>',
  '<div style="margin-top:20px">' + "".join(f'<div class="row" style="padding:17px 0"><div class="time" style="font-size:58px">{t}</div><div class="tx"><b style="font-size:34px">{a}</b><span style="font-size:23px">{b}</span></div></div>' for t, a, b in [
    ("14.00", "Check-in", "Simpan koper, istirahat sejenak di teras."),
    ("15.00", "Paling lambat tiba", "Hari pertama? Ini batas aman agar senja tidak terlewat."),
    ("16.00", "Turun ke pantai", "Pilih spot, sewa kayak, siapkan kamera."),
    ("16.50", "Golden hour", "Cahaya hangat &amp; lembut, terbaik untuk foto potret."),
    ("17.50", "Matahari terbenam", "Menyentuh cakrawala, tepat di depan pantai."),
    ("18.10", "Afterglow", "Langit jingga-ungu. Jangan buru-buru pulang!"),
    ("18.30", "Senja Dinner", "Ikan bakar &amp; seafood di tepi pantai (pesan H-1).")]) + '</div>')

# 4 arrival
T.append(f'''<div class="t f" id="sunset-04"><div class="top"><img src="{LOGO}" alt=""><span class="caps">Kapan harus tiba?</span></div>
  <div class="mid">
    <div class="caps" style="font-size:22px">Tiba di resort paling lambat</div>
    <div class="time" style="font-size:250px;color:#E07A4B;margin-top:10px">15.00</div>
    <div class="pf" style="font-size:54px;line-height:1.15;margin-top:10px">Supaya senja pertamamu <span class="it">tidak terlewat.</span></div>
    <div class="card" style="margin-top:40px">{tips(["Check-in mulai <b>14.00 WITA</b>, check-out <b>12.00 WITA</b>.", "<b>Pesawat:</b> Bandara H. Aroeppala → SunaRi hanya <b>±10–15 menit</b>.", "<b>Feri Bira–Pamatata:</b> masih <b>±1–1,5 jam</b> ke resort, pilih penyeberangan pagi.", "<b>KM Dharma Kartika:</b> tiba pagi di Benteng, punya sepanjang hari sebelum senja."], 26)}</div></div>
  {foot(4)}</div>''')

# 5 best months
# 5 kalender senja (menggantikan slide "bulan terbaik"; KAL/kcell didefinisikan di bawah)
SLIDE5_AT = len(T); T.append(None)

# 6 light phases
text_slide(6, "Fase cahaya senja", 'Empat fase, <span class="it">empat warna</span>',
  '<div style="margin-top:24px">' + "".join(f'<div class="row"><div class="time" style="font-size:50px;width:270px">{t}</div><div class="tx"><b>{a}</b><span>{b}</span></div></div>' for t, a, b in [
    ("16.50–17.40", "Golden hour", "Cahaya keemasan &amp; bayangan panjang. Ideal untuk foto wajah &amp; pasangan."),
    ("17.40–17.55", "Sunset", "Matahari bulat merah menyentuh laut. Waktunya siluet &amp; jalur cahaya di air."),
    ("17.55–18.15", "Afterglow", "Matahari hilang, langit justru menyala jingga, merah muda &amp; ungu."),
    ("18.15–18.30", "Blue hour", "Langit biru tua, lampu resort mulai menyala. Foto suasana malam yang tenang.")]) + '</div>')

# 7 signs
text_slide(7, "Pertanda senja cantik", 'Akan <span class="it">secantik apa</span> senja hari ini?',
  tips(["<b>Awan tipis &amp; tinggi</b> di langit barat = warna paling dramatis, langit memantulkan jingga &amp; merah muda.",
        "<b>Langit bersih tanpa awan</b> = matahari bulat sempurna, cocok untuk siluet &amp; foto jalur cahaya.",
        "<b>Awan tebal di cakrawala</b> = matahari bisa hilang lebih awal. Datang lebih cepat, nikmati golden hour.",
        "<b>Habis hujan sore?</b> Udara bersih sering memberi afterglow terbaik. Tetap keluar!",
        "Ikuti story <b>#SenjaHariIni</b> kami setiap sore untuk melihat kondisi langit terkini."], 27))

# 8-13 spots
def spot(n, img, pos, no, name, when, desc, tip):
    T.append(f'''<div class="t f" id="sunset-{n:02d}"><div class="top"><img src="{LOGO}" alt=""><span class="caps">Spot foto {no} / 06</span></div>
  <img class="photo" src="{P}{img}" style="position:absolute;left:72px;right:72px;width:936px;top:170px;height:640px;object-position:{pos}" alt="">
  <div style="position:absolute;left:72px;right:72px;top:850px">
    <div style="display:flex;align-items:center;justify-content:space-between"><div class="pf" style="font-size:60px">{name}</div><span class="tag">{when}</span></div>
    <div style="font-size:27px;line-height:1.5;margin-top:14px">{desc}</div>
    <div style="font-size:25px;line-height:1.5;margin-top:14px;color:#7A5039"><b>Tips:</b> {tip}</div></div>
  {foot(n)}</div>''')
spot(8, "senja/35-matahari-cakrawala-1751.jpg", "50% 52%", "01", "Bibir <span class='it'>pantai</span>", "17.30–18.00", "Tepat di depan resort, matahari turun lurus di atas laut. Jalur cahaya di air paling cantik dari sini.", "letakkan garis cakrawala di sepertiga bawah layar.")
spot(9, "aktivitas/07-ayunan-gaun-merah-tengah.jpg", "50% 52%", "02", "Ayunan <span class='it'>raksasa</span>", "17.20–17.50", "Siluet berayun dengan matahari di cakrawala. Gratis untuk tamu.", "pakai mode burst saat ayunan di titik tertinggi.")
spot(10, "senja/42-teras-bingkai-daun-1744.jpg", "50% 35%", "03", "Teras <span class='it'>VIP Standard</span>", "17.00–17.50", "Teras rumah panggung menghadap langsung ke arah matahari terbenam. Senja dari 'rumah sendiri'.", "foto dari dalam teras, jadikan tiang &amp; atap sebagai bingkai.")
spot(11, "senja/51-kayak-double-jalur-cahaya-1751.jpg", "50% 55%", "04", "Di atas <span class='it'>kayak</span>", "17.00–17.40", "Mendayung di air tenang menyongsong senja. Sewa kayak single Rp 50.000, double Rp 100.000.", "minta teman memotret dari bibir pantai agar kayak jadi siluet.")
spot(12, "senja/23-pohon-meranggas-senja.jpg", "50% 55%", "05", "Pohon <span class='it'>tepi pantai</span>", "17.35–17.55", "Ranting pohon meranggas di tepi pantai membingkai matahari. Favorit untuk foto artistik.", "posisikan matahari di sela ranting, lalu ketuk langit untuk exposure.")
spot(13, "senja/32-payung-lampu-senja-1751.jpg", "50% 55%", "06", "Payung <span class='it'>&amp; lampu gantung</span>", "16.30–18.00", "Kursi kayu, payung &amp; lampu gantung di tepi pantai. Pada 3 September, foto ini diambil pukul <b>17.51</b>, matahari masih di atas laut.", "foto dari belakang kursi agar kursi &amp; laut masuk satu bingkai.")

# 14 phone exposure
text_slide(14, "Tips foto · Pengaturan ponsel", 'Atur ponselmu <span class="it">sebelum 17.30</span>',
  tips(["<b>Ketuk langit, bukan matahari.</b> Lalu geser ikon ☀ ke bawah. Warna lebih pekat, siluet lebih tajam.",
        "<b>Kunci fokus &amp; exposure</b> (tekan lama di layar: AE/AF Lock) agar tidak berubah saat memotret.",
        "<b>Matikan flash.</b> Flash membuat wajah pucat &amp; merusak warna senja.",
        "<b>Jangan zoom digital.</b> Pakai lensa 2x/3x bawaan atau mendekatlah.",
        "<b>HDR otomatis</b> boleh menyala untuk pemandangan, matikan jika ingin siluet hitam pekat.",
        "<b>Bersihkan lensa</b> dengan kain halus, udara pantai mudah membuatnya berkabut."], 26))

# 15 composition
text_slide(15, "Tips foto · Komposisi", 'Bingkai senja yang <span class="it">bercerita</span>',
  tips(["<b>Aturan sepertiga:</b> nyalakan grid kamera, letakkan cakrawala di garis bawah agar langit dominan.",
        "<b>Cakrawala harus lurus.</b> Gunakan grid atau level bawaan ponsel.",
        "<b>Bingkai alami:</b> daun ketapang, ranting, tiang teras atau pohon kelapa.",
        "<b>Beri skala:</b> perahu nelayan, kayak atau siluet orang membuat laut terasa luas.",
        "<b>Jalur cahaya:</b> sejajarkan diri dengan pantulan matahari di air untuk garis emas di tengah foto."], 27))

# 16 people
photo_slide(16, "senja/27-tamu-dan-pohon-kelapa.jpg", "50% 45%", "Tips foto · Pasangan &amp; keluarga", "Siluet lebih <i class='gold'>bercerita</i> dari wajah.",
  "Berdiri membelakangi matahari, beri jarak antar orang agar bentuk tubuh terpisah. Coba pose bergandengan, melompat, atau saling menunjuk matahari. Foto wajah? Lakukan saat <b>golden hour 16.50–17.40</b>, menghadap cahaya.", size=78)

# 17 video
text_slide(17, "Tips video · Reels &amp; TikTok", 'Rekam senja <span class="it">dalam 15 detik</span>',
  tips(["<b>Timelapse:</b> letakkan ponsel di tripod atau di atas meja mulai <b>17.20</b>, biarkan merekam sampai 18.00.",
        "<b>Slow motion</b> untuk ayunan, cipratan kayak atau ombak kecil di bibir pantai.",
        "<b>Rekam vertikal 9:16</b>, 4K jika ada, dan jangan banyak menggeser ponsel.",
        "<b>Ambil 3 sudut:</b> lebar (laut &amp; langit), sedang (orang), detail (kaki di pasir, gelas minuman).",
        "Unggah dengan <b>#SenjaHariIni</b> &amp; tag <b>@sunaribeachresortselayar</b>. Kami repost favorit setiap minggu."], 27))

# 18 what to bring
text_slide(18, "Yang perlu dibawa", 'Bekal <span class="it">menunggu senja</span>',
  '<div class="grid2" style="display:grid;grid-template-columns:1fr 1fr;gap:0 40px;margin-top:10px">' + tips(["Ponsel terisi penuh / power bank", "Tripod kecil atau penyangga ponsel", "Kain lap lensa"], 28) + tips(["Sandal &amp; baju yang boleh basah", "Topi &amp; kacamata hitam untuk sore", "Losion anti-nyamuk setelah gelap"], 28).replace('<i>1</i>', '<i>4</i>').replace('<i>2</i>', '<i>5</i>').replace('<i>3</i>', '<i>6</i>') + '</div>'
  + '<div class="card" style="margin-top:30px;font-size:27px;line-height:1.5">Sewa kayak: single <b>Rp 50.000</b> · double <b>Rp 100.000</b>. Alat snorkeling mulai <b>Rp 40.000</b>/set/hari. Ayunan raksasa <b>gratis</b>.</div>')

# 19 after sunset
photo_slide(19, "senja/37-afterglow-kayak-pelampung-1814.jpg", "50% 50%", "Setelah matahari terbenam", "Malam <i class='gold'>belum selesai.</i>",
  "<b>18.10</b> afterglow di bibir pantai · <b>18.30</b> Senja Dinner ikan bakar &amp; seafood (pesan H-1) · <b>sampai 21.00</b> Bajoy Beach Resto buka untuk tamu menginap · lampu-lampu bungalow menyala di antara pohon kelapa.")

# 10 CTA
T.append(f'''<div class="t f" id="sunset-20"><img class="bg" src="{P}senja/21-siluet-tamu-tepi-pantai.jpg" style="object-position:50% 60%" alt="">
  <div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,.3) 0%,rgba(0,0,0,0) 30%,rgba(0,0,0,.05) 50%,rgba(0,0,0,.7) 100%)"></div>
  <img src="{LOGO_D}" style="position:absolute;left:50%;transform:translateX(-50%);top:70px;width:280px" alt="">
  <div class="sh" style="position:absolute;left:72px;right:72px;bottom:150px;text-align:center;color:#FBF4EC">
    <div class="pf" style="font-size:76px;line-height:1.08">Senja berikutnya, <i class="gold">giliranmu.</i></div>
    <div style="font-size:28px;line-height:1.5;margin-top:20px">Tutup hari dengan <b>Senja Dinner</b> di tepi pantai, pesan paling lambat H-1.<br>Tag <b>{IG}</b> &amp; <b>#SenjaHariIni</b> di foto senjamu.</div>
    <div style="display:inline-block;margin-top:34px;padding:20px 40px;border-radius:999px;background:linear-gradient(90deg,#FDB15D,#FF8A5C);font-weight:700;font-size:28px;text-shadow:none">Reservasi · WA {WA}</div></div>
  {foot(20, True)}</div>''')

# ================================================================== STORIES (6)
def sfoot(light=True):
    return f'<div class="ft{" l" if light else ""}" style="bottom:240px"><span>WA {WA}</span><span>{IG}</span></div>'
T.append(f'''<div class="t s" id="story-sunset-1"><img class="bg" src="{P}senja/12-kayak-matahari-merah-story.jpg" style="object-position:50% 50%" alt="">
  <img src="{LOGO_D}" style="position:absolute;left:50%;transform:translateX(-50%);top:150px;width:300px;filter:drop-shadow(0 2px 8px rgba(0,0,0,.45))" alt="">
  <div class="sh" style="position:absolute;left:72px;right:72px;bottom:400px;text-align:center;color:#FBF4EC">
    <div style="font-weight:700;font-size:24px;letter-spacing:.28em;text-transform:uppercase;color:#FDB15D">Senja di Pantai Sunari</div>
    <div class="time" style="font-size:260px;margin-top:10px">17.50</div>
    <div class="pf" style="font-size:58px;margin-top:10px">Catat jamnya. <i class="gold">Jangan terlambat.</i></div>
    <div style="font-weight:700;font-size:22px;letter-spacing:.24em;text-transform:uppercase;margin-top:40px">Ketuk untuk tips →</div></div></div>''')
T.append(f'''<div class="t s" id="story-sunset-2"><div class="top" style="top:120px"><img src="{LOGO}" alt=""><span class="caps">Jadwal sore</span></div>
  <div style="position:absolute;left:72px;right:72px;top:300px">
    <div class="pf" style="font-size:76px;line-height:1.05">Hitung mundur <span class="it">menuju senja</span></div>
    <div style="margin-top:30px">
      {"".join(f'<div class="row"><div class="time" style="font-size:78px;width:230px">{t}</div><div class="tx"><b style="font-size:42px">{a}</b><span style="font-size:27px">{b}</span></div></div>' for t, a, b in [
        ("15.00", "Tiba di resort", "Check-in mulai 14.00"), ("16.00", "Ke pantai", "Pilih spot &amp; sewa kayak"), ("16.50", "Golden hour", "Cahaya paling hangat"),
        ("17.50", "Matahari terbenam", "Tepat di depan pantai"), ("18.10", "Afterglow", "Tetap di tempat!")])}
    </div></div>{sfoot(False)}</div>''')
T.append(f'''<div class="t s" id="story-sunset-3"><img class="bg" src="{P}aktivitas/08-ayunan-gaun-merah-kelapa.jpg" style="object-position:50% 30%" alt="">
  <img src="{LOGO_D}" style="position:absolute;left:72px;top:130px;width:240px" alt="">
  <div style="position:absolute;left:56px;right:56px;bottom:250px;background:rgba(251,244,236,.96);border-radius:40px;padding:30px 44px">
    <div class="caps" style="font-size:22px">4 spot foto senja</div>
    {"".join(f'<div class="row" style="padding:10px 0"><div class="time" style="font-size:42px;width:290px">{t}</div><div class="tx"><b style="font-size:32px">{a}</b></div></div>' for t, a in [("17.30–18.00", "Bibir pantai"), ("17.20–17.50", "Ayunan raksasa"), ("17.00–17.50", "Teras VIP Standard"), ("17.00–17.40", "Di atas kayak")])}
  </div></div>''')
T.append(f'''<div class="t s" id="story-sunset-4"><div class="top" style="top:120px"><img src="{LOGO}" alt=""><span class="caps">Tips foto</span></div>
  <div style="position:absolute;left:72px;right:72px;top:300px">
    <div class="pf" style="font-size:76px;line-height:1.05">3 trik foto senja <span class="it">pakai ponsel</span></div>
    <ul class="tips" style="margin-top:30px">
      <li><i>1</i><span style="font-size:34px"><b>Ketuk langit</b>, turunkan exposure. Siluet jadi tajam, warna pekat.</span></li>
      <li><i>2</i><span style="font-size:34px"><b>Bingkai alami</b>: daun, ranting atau tiang teras.</span></li>
      <li><i>3</i><span style="font-size:34px"><b>Tunggu 15 menit</b> setelah terbenam untuk afterglow.</span></li>
    </ul>
    <img class="photo" src="{P}senja/27-tamu-dan-pohon-kelapa.jpg" style="height:420px;margin-top:40px;object-position:50% 45%" alt=""></div>{sfoot(False)}</div>''')
T.append(f'''<div class="t s" id="story-sunset-5"><img class="bg" src="{P}senja/14-daun-matahari-story.jpg" style="object-position:50% 50%" alt="">
  <img src="{LOGO_D}" style="position:absolute;left:72px;top:130px;width:240px" alt="">
  <div class="sh" style="position:absolute;left:72px;right:72px;top:520px;text-align:center;color:#FBF4EC">
    <div class="pf" style="font-size:80px;line-height:1.1">Kamu tim <i class="gold">golden hour</i><br>atau tim <i class="gold">afterglow?</i></div>
    <div style="margin:70px auto 0;width:760px;height:340px;border-radius:36px;border:3px dashed rgba(251,244,236,.75);display:flex;align-items:center;justify-content:center;text-shadow:none">
      <span style="font-weight:700;font-size:22px;letter-spacing:.24em;text-transform:uppercase">Tempel stiker polling di sini</span></div></div></div>''')
T.append(f'''<div class="t s" id="story-sunset-6"><img class="bg" src="{P}senja/29-dua-kursi-menghadap-senja.jpg" style="object-position:50% 55%" alt="">
  <img src="{LOGO_D}" style="position:absolute;left:50%;transform:translateX(-50%);top:150px;width:300px" alt="">
  <div style="position:absolute;left:56px;right:56px;bottom:300px;background:rgba(251,244,236,.96);border-radius:40px;padding:46px 48px;text-align:center">
    <div class="caps" style="font-size:22px">Pesan senjamu</div>
    <div class="pf" style="font-size:64px;line-height:1.1;margin-top:12px">Kamar + <span class="it">Senja Dinner</span></div>
    <div style="font-size:28px;line-height:1.5;margin-top:14px">Senja Dinner dipesan paling lambat <b>H-1</b>.</div>
    <div style="margin-top:28px;height:150px;border-radius:30px;border:3px dashed rgba(224,122,75,.75);display:flex;align-items:center;justify-content:center;font-weight:700;font-size:20px;letter-spacing:.22em;text-transform:uppercase;color:#C0592C">Tempel stiker tautan WhatsApp</div>
    <div class="pf" style="font-size:46px;margin-top:22px">WA {WA}</div></div></div>''')

# ================================================================== KALENDER SENJA
# Jam terbenam astronomis untuk Pantai Sunari (6.13°LS, 120.47°BT, WITA), dibulatkan; awal–akhir bulan.
# Dicocokkan dengan foto ber-jam milik resort (Jun–Sep 2026: matahari menyentuh cakrawala 17.43–17.58).
KAL = [("Jan", "18.20", "18.15–18.22", 0), ("Feb", "18.20", "18.18–18.22", 0), ("Mar", "18.12", "18.06–18.18", 0),
       ("Apr", "17.58", "17.53–18.04", 1), ("Mei", "17.50", "17.49–17.52", 1), ("Jun", "17.51", "17.49–17.54", 2),
       ("Jul", "17.58", "17.55–18.00", 2), ("Agu", "18.00", "17.59–18.00", 2), ("Sep", "17.55", "17.53–17.58", 2),
       ("Okt", "17.51", "17.51–17.52", 1), ("Nov", "17.55", "17.51–18.00", 1), ("Des", "18.07", "18.01–18.13", 1)]
def kcell(m, t, r, k, big=54, pad="20px 10px"):
    bg = "#FFFDF9" if k else "rgba(138,95,72,.07)"
    col = "#E07A4B" if k else "#9A8478"
    dot = '<div style="position:absolute;top:12px;right:14px;width:12px;height:12px;border-radius:50%;background:linear-gradient(180deg,#FDB15D,#FF8A5C)"></div>' if k == 2 else ''
    return f'''<div style="position:relative;background:{bg};border-radius:24px;padding:{pad};text-align:center;box-shadow:{"0 8px 22px rgba(90,62,49,.10)" if k else "none"}">{dot}
      <div class="caps" style="font-size:18px;color:{"#7A5039" if k else "#9A8478"}">{m}</div>
      <div class="time" style="font-size:{big}px;color:{col};margin-top:8px">{t}</div>
      <div style="font-size:17px;color:#7A5039;margin-top:6px">{r}</div></div>'''
legend = '''<div style="display:flex;gap:30px;flex-wrap:wrap;font-size:21px;color:#5A3E31;margin-top:22px">
  <span><b style="color:#E07A4B">●</b> Musim terbaik (Apr–Des)</span><span><b style="color:#9A8478">●</b> Musim hujan, sering berawan</span>
  <span><span style="display:inline-block;width:14px;height:14px;border-radius:50%;background:linear-gradient(180deg,#FDB15D,#FF8A5C);vertical-align:-1px"></span> Terbukti dari foto kami</span></div>'''
T.append(f'''<div class="t f" id="kalender-senja-feed"><div class="top"><img src="{LOGO}" alt=""><span class="caps">Kalender senja</span></div>
  <div class="mid">
    <div class="pf" style="font-size:64px;line-height:1.05">Jam matahari terbenam <span class="it">sepanjang tahun</span></div>
    <div style="font-size:24px;color:#5A3E31;margin-top:10px">Pantai Sunari · WITA · datanglah ke pantai <b>30 menit sebelumnya</b></div>
    <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-top:28px">{"".join(kcell(*x, big=60, pad="28px 10px") for x in KAL)}</div>
    {legend}</div>
  <div class="ft"><span>SunaRi · Selayar</span><span>Simpan &amp; bagikan</span></div></div>''')
T[SLIDE5_AT] = T[-1].replace('id="kalender-senja-feed"', 'id="sunset-05"').replace('<span>Simpan &amp; bagikan</span>', '<span>05 / 20</span>')
T.append(f'''<div class="t s" id="kalender-senja-story"><div class="top" style="top:120px"><img src="{LOGO}" alt=""><span class="caps">Kalender senja</span></div>
  <div style="position:absolute;left:64px;right:64px;top:260px;bottom:330px;display:flex;flex-direction:column;justify-content:center">
    <div class="pf" style="font-size:72px;line-height:1.05">Kapan senja <span class="it">di bulanmu?</span></div>
    <div style="font-size:27px;color:#5A3E31;margin-top:12px">Jam matahari terbenam di Pantai Sunari (WITA)</div>
    <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-top:34px">{"".join(kcell(*x, big=70, pad="40px 10px") for x in KAL)}</div>
    {legend.replace("font-size:21px","font-size:23px")}
    <div style="font-size:24px;color:#7A5039;margin-top:20px">Datang ke pantai 30 menit sebelumnya · afterglow ±20 menit setelahnya.</div></div>
  <div class="ft" style="bottom:240px"><span>WA {WA}</span><span>{IG}</span></div></div>''')

(H / "sunset.html").write_text(f'<!doctype html><html lang="id"><head><meta charset="utf-8">{FONTS}<style>{CSS}</style></head><body>{"".join(T)}</body></html>')
print(len(T), "desain")
