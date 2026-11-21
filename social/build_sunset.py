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
def foot(n, light=False, total=10):
    return f'<div class="ft{" l" if light else ""}"><span>SunaRi · Selayar</span><span>{n:02d} / {total:02d}</span></div>'

# ================================================================== CAROUSEL (10)
# 1 cover
T.append(f'''<div class="t f" id="sunset-01"><img class="bg" src="{P}senja/31-kayak-siluet-matahari-merah-story.jpg" style="object-position:50% 30%" alt="">
  <div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,.5) 0%,rgba(0,0,0,.15) 40%,rgba(0,0,0,0) 55%,rgba(0,0,0,.35) 100%)"></div>
  <img src="{LOGO_D}" style="position:absolute;left:72px;top:60px;width:240px;filter:drop-shadow(0 2px 8px rgba(0,0,0,.45))" alt="">
  <div class="sh" style="position:absolute;left:72px;right:72px;top:220px;color:#FBF4EC">
    <div style="font-weight:700;font-size:22px;letter-spacing:.28em;text-transform:uppercase;color:#FDB15D">Panduan senja · Pantai Sunari</div>
    <div class="time" style="font-size:210px;margin-top:8px">17.50</div>
    <div class="pf" style="font-size:60px;line-height:1.1;margin-top:4px">Jam paling ditunggu <i class="gold">di Selayar.</i></div></div>
  <div class="sh" style="position:absolute;left:72px;right:72px;bottom:130px;color:#FBF4EC;font-size:28px">Waktu terbaik, spot foto &amp; tips memotret senja. Simpan postinganSimpan postingan ini ↓nbsp;iniSimpan postingan ini ↓nbsp;↓</div>
  {foot(1, True)}</div>''')

# 2 timeline
T.append(f'''<div class="t f" id="sunset-02"><div class="top"><img src="{LOGO}" alt=""><span class="caps">Jadwal sore ideal</span></div>
  <div class="mid">
    <div class="pf" style="font-size:66px;line-height:1.05">Satu sore, <span class="it">tanpa&nbsp;terburu&#8209;buru</span></div>
    <div style="margin-top:20px">
      {"".join(f'<div class="row"><div class="time">{t}</div><div class="tx"><b>{a}</b><span>{b}</span></div></div>' for t, a, b in [
        ("14.00", "Check-in", "Simpan koper, istirahat sejenak di teras."),
        ("16.00", "Turun ke pantai", "Pilih spot, sewa kayak, siapkan kamera."),
        ("16.50", "Golden hour", "Cahaya hangat &amp; lembut, waktu terbaik foto potret."),
        ("17.50", "Matahari terbenam", "Matahari menyentuh cakrawala, tepat di depan pantai."),
        ("18.10", "Afterglow", "Langit berubah jingga-ungu. Jangan buru-buru pulang!"),
        ("18.30", "Senja Dinner", "Ikan bakar &amp; seafood di tepi pantai (pesan H-1).")])}
    </div></div>
  {foot(2)}</div>''')

# 3 arrival
T.append(f'''<div class="t f" id="sunset-03"><div class="top"><img src="{LOGO}" alt=""><span class="caps">Kapan harus tiba?</span></div>
  <div class="mid">
    <div class="caps" style="font-size:22px">Tiba di resort paling lambat</div>
    <div class="time" style="font-size:250px;color:#E07A4B;margin-top:10px">15.00</div>
    <div class="pf" style="font-size:56px;line-height:1.15;margin-top:10px">Supaya senja pertamamu <span class="it">tidak terlewat.</span></div>
    <div class="card" style="margin-top:46px">
      <ul class="tips" style="margin-top:0">
        <li><i>·</i><span>Check-in mulai <b>14.00 WITA</b>.</span></li>
        <li><i>·</i><span>Dari Bandara H. Aroeppala hanya <b>±10–15 menit</b>. Penerbangan siang = aman.</span></li>
        <li><i>·</i><span>Lewat feri Bira–Pamatata? Masih <b>±1–1,5 jam</b> ke resort, jadi pilih penyeberangan pagi.</span></li>
      </ul></div></div>
  {foot(3)}</div>''')

# 4 best months
T.append(f'''<div class="t f" id="sunset-04"><img class="bg" src="{P}senja/24-pohon-tepi-pantai-senja.jpg" style="object-position:50% 55%" alt="">
  <div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,.35) 0%,rgba(0,0,0,0) 30%,rgba(0,0,0,0) 45%,rgba(0,0,0,.65) 100%)"></div>
  <img src="{LOGO_D}" style="position:absolute;left:72px;top:60px;width:230px" alt="">
  <div class="sh" style="position:absolute;left:72px;right:72px;bottom:150px;color:#FBF4EC">
    <div style="font-weight:700;font-size:22px;letter-spacing:.28em;text-transform:uppercase;color:#FDB15D">Bulan terbaik</div>
    <div class="pf" style="font-size:150px;line-height:1;margin-top:10px">April <span style="color:#FDB15D">–</span> Desember</div>
    <div style="font-size:30px;line-height:1.5;margin-top:22px">Langit lebih cerah &amp; laut tenang. Matahari terbenam tepat di depan Pantai Sunari, sekitar <b>17.50–18.00 WITA</b>.</div></div>
  {foot(4, True)}</div>''')

# 5-8 spots
def spot(n, img, pos, no, name, when, desc, tip):
    T.append(f'''<div class="t f" id="sunset-{n:02d}"><div class="top"><img src="{LOGO}" alt=""><span class="caps">Spot foto {no} / 04</span></div>
  <img class="photo" src="{P}{img}" style="position:absolute;left:72px;right:72px;width:936px;top:170px;height:640px;object-position:{pos}" alt="">
  <div style="position:absolute;left:72px;right:72px;top:850px">
    <div style="display:flex;align-items:center;justify-content:space-between"><div class="pf" style="font-size:62px">{name}</div><span class="tag">{when}</span></div>
    <div style="font-size:28px;line-height:1.5;margin-top:14px">{desc}</div>
    <div style="font-size:25px;line-height:1.5;margin-top:14px;color:#7A5039"><b>Tips:</b> {tip}</div></div>
  {foot(n)}</div>''')
spot(5, "senja/29-dua-kursi-menghadap-senja.jpg", "50% 55%", "01", "Bibir <span class='it'>pantai</span>", "17.30–18.00", "Tepat di depan resort, matahari turun lurus di atas laut. Jalur cahaya di air paling cantik dari sini.", "letakkan garis cakrawala di sepertiga bawah layar.")
spot(6, "aktivitas/05-ayunan-raksasa-senja.jpg", "40% 55%", "02", "Ayunan <span class='it'>raksasa</span>", "17.20–17.50", "Siluet berayun dengan matahari di cakrawala. Gratis untuk tamu.", "pakai mode burst saat ayunan di titik tertinggi.")
spot(7, "vip-standard-bungalow/02-teras-view-pantai.jpg", "50% 60%", "03", "Teras <span class='it'>VIP Standard</span>", "17.00–17.50", "Teras rumah panggung menghadap langsung ke arah matahari terbenam. Senja dari 'rumah sendiri'.", "foto dari dalam teras, jadikan tiang & atap sebagai bingkai.")
spot(8, "senja/17-kayak-berdua.jpg", "50% 55%", "04", "Di atas <span class='it'>kayak</span>", "17.00–17.40", "Mendayung di air tenang menyongsong senja. Sewa kayak single Rp 50.000, double Rp 100.000.", "minta teman memotret dari bibir pantai agar kayak jadi siluet.")

# 9 photo tips
T.append(f'''<div class="t f" id="sunset-09"><div class="top"><img src="{LOGO}" alt=""><span class="caps">Tips memotret senja</span></div>
  <div class="mid">
    <div class="pf" style="font-size:68px;line-height:1.05">Foto senja <span class="it">pakai ponsel</span></div>
    <ul class="tips">
      <li><i>1</i><span><b>Ketuk langit, bukan matahari</b>, lalu turunkan exposure (geser ☀ ke bawah). Warna jadi pekat, siluet tajam.</span></li>
      <li><i>2</i><span><b>Jangan zoom digital.</b> Mendekatlah, atau pakai lensa 2x/3x bawaan.</span></li>
      <li><i>3</i><span><b>Cari bingkai alami</b>: daun ketapang, ranting, atau tiang teras.</span></li>
      <li><i>4</i><span><b>Siluet lebih kuat dari wajah.</b> Posisikan orang membelakangi matahari.</span></li>
      <li><i>5</i><span><b>Bersihkan lensa</b> sebelum memotret, udara pantai membuatnya berkabut.</span></li>
      <li><i>6</i><span><b>Tunggu 15 menit setelah terbenam.</b> Afterglow sering jadi warna paling indah.</span></li>
    </ul></div>
  {foot(9)}</div>''')

# 10 CTA
T.append(f'''<div class="t f" id="sunset-10"><img class="bg" src="{P}senja/21-siluet-tamu-tepi-pantai.jpg" style="object-position:50% 60%" alt="">
  <div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,.3) 0%,rgba(0,0,0,0) 30%,rgba(0,0,0,.05) 50%,rgba(0,0,0,.7) 100%)"></div>
  <img src="{LOGO_D}" style="position:absolute;left:50%;transform:translateX(-50%);top:70px;width:280px" alt="">
  <div class="sh" style="position:absolute;left:72px;right:72px;bottom:150px;text-align:center;color:#FBF4EC">
    <div class="pf" style="font-size:76px;line-height:1.08">Senja berikutnya, <i class="gold">giliranmu.</i></div>
    <div style="font-size:28px;line-height:1.5;margin-top:20px">Tutup hari dengan <b>Senja Dinner</b> di tepi pantai, pesan paling lambat H-1.<br>Tag <b>{IG}</b> &amp; <b>#SenjaHariIni</b> di foto senjamu.</div>
    <div style="display:inline-block;margin-top:34px;padding:20px 40px;border-radius:999px;background:linear-gradient(90deg,#FDB15D,#FF8A5C);font-weight:700;font-size:28px;text-shadow:none">Reservasi · WA {WA}</div></div>
  {foot(10, True)}</div>''')

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
T.append(f'''<div class="t s" id="story-sunset-3"><img class="bg" src="{P}aktivitas/05-ayunan-raksasa-senja.jpg" style="object-position:40% 50%" alt="">
  <img src="{LOGO_D}" style="position:absolute;left:72px;top:130px;width:240px" alt="">
  <div style="position:absolute;left:56px;right:56px;bottom:330px;background:rgba(251,244,236,.96);border-radius:40px;padding:44px 48px">
    <div class="caps" style="font-size:22px">4 spot foto senja</div>
    {"".join(f'<div class="row" style="padding:16px 0"><div class="time" style="font-size:46px;width:300px">{t}</div><div class="tx"><b style="font-size:34px">{a}</b></div></div>' for t, a in [("17.30–18.00", "Bibir pantai"), ("17.20–17.50", "Ayunan raksasa"), ("17.00–17.50", "Teras VIP Standard"), ("17.00–17.40", "Di atas kayak")])}
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

(H / "sunset.html").write_text(f'<!doctype html><html lang="id"><head><meta charset="utf-8">{FONTS}<style>{CSS}</style></head><body>{"".join(T)}</body></html>')
print(len(T), "desain")
