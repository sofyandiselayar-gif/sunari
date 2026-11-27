"""Feed carousel "Sehari ke Bahuluang" (20 slide, 1080x1350): perjalanan & aktivitas di Pulau Bahuluang,
berangkat dari SunaRi dan kembali menyambut senja di SunaRi. Soft selling, tanpa harga/paket.
Rute final: titik temu kapal sesuai pasang-surut (Bone Taringan / Turungan), Pasir Timbul diatur kapten, kapal pulang ±14.00.
Run: python3 social/build_bahuluang_feed20.py && node social/render_bahuluang_feed20.js -> social/bahuluang-feed-20/*.png"""
import pathlib
H = pathlib.Path(__file__).parent
exec((H / "build_vipsuperior.py").read_text().split("KICK =")[0].replace("__file__", repr(str(H / "build_vipsuperior.py"))))
# foto hasil color grading tema SunaRi (social/grade_bahuluang.py)
P = "../assets/photos/graded/"; B = P + "bahuluang__"; N = 20; KICK = "Sehari ke Bahuluang"
CSS += """
.chip{display:inline-block;margin-left:14px;padding:6px 14px;border-radius:30px;background:linear-gradient(90deg,#FDB15D,#FF8A5C);color:#fff;font-size:17px;letter-spacing:.14em;vertical-align:2px}
.sub{font-size:29px}
.tl{margin-top:22px;border-top:1.5px solid rgba(138,95,72,.3);text-align:left}
.tl div{display:flex;gap:24px;padding:12px 0;border-bottom:1.5px solid rgba(138,95,72,.3);font-size:24px;color:#45301F}
.tl b{flex:0 0 96px;font-weight:700;color:#C0592C;letter-spacing:.04em}
"""
# (foto, posisi, judul, teks, jam)
SL = [
 (B + "40-pantai-barat-air-toska-awan.jpg", "50% 60%", "Sehari ke<br>Bahuluang", "Berangkat pagi dari SunaRi, pulang menyambut senja", ""),
 (B + "51-pantai-barat-teluk-pasir-putih.jpg", "45% 50%", 'Satu hari, <em>banyak cerita</em>', "Snorkeling di air sebening kaca, pasir yang muncul di tengah laut, gua dengan stalaktit dan stalagmit yang indah, dan makan siang di pantai yang sepi.", ""),
 (P + "taman__05-meja-taman-view-laut-gazebo.jpg", "50% 55%", 'Pagi yang <em>pelan</em> di SunaRi', "Sarapan di Bajoy Beach Resto sambil memandang laut. Siapkan baju renang, topi, dan tabir surya.", "07.00"),
 (P + "pantai__02-perahu-nelayan-biru.jpg", "50% 55%", 'Mengikuti <em>laut</em> hari itu', "Pagi-pagi kami cek pasang-surut dan kabari kamu. Dari situ ditentukan titik temu dengan kapten kapal.", "08.00"),
 (B + "22-kapal-menuju-batu-berlubang.jpg", "50% 55%", 'Menyeberang <em>ke pulau</em>', "Air cukup tinggi, kapal berangkat dari Bone Taringan, sekitar 20 menit. Air surut, kita berangkat dari Turungan.", ""),
 (B + "21-laut-toska-dari-kapal.jpg", "50% 62%", 'Laut yang <em>berganti warna</em>', "Dari biru tua ke toska. Karang terlihat jelas dari sisi kapal.", ""),
 (B + "19-batu-berlubang.jpg", "50% 55%", 'Batu karang <em>berlubang</em>', "Salah satu pemandangan yang menyapa di perjalanan. Siapkan kamera.", ""),
 (B + "25-makam-karang-snorkeling-dan-kapal.jpg", "40% 60%", 'Tiba di <em>Makam Karang</em>', "Gosong karang putih di tengah laut, dikelilingi air jernih. Spot snorkeling pertama hari ini.", "10.00"),
 (B + "31-snorkeling-dekat-pondok-apung.jpg", "45% 50%", 'Air sebening <em>kaca</em>', "Masker dan pelampung sudah disiapkan. Ikan-ikan kecil datang menyapa di antara karang.", ""),
 (B + "35-berjalan-di-hamparan-karang.jpg", "50% 55%", 'Di atas <em>Makam Karang</em>', "Pakai sepatu air, lalu susuri punggung Makam Karang yang membentang ke tengah laut.", ""),
 (B + "36-kru-membantu-tamu-turun-kapal.jpg", "50% 60%", 'Ditemani kru yang <em>sigap</em>', "Naik-turun kapal, memasang alat snorkeling, mencari spot foto. Kru kapal selalu siap membantu.", ""),
 (B + "48-pasir-timbul-langit-biru.jpg", "50% 65%", 'Pasir yang <em>muncul</em>', "Pasir Timbul Bahuluang muncul di tengah laut. Kapten akan membawamu ke sana saat airnya paling pas.", ""),
 (B + "42-pantai-barat-rombongan-di-air.jpg", "50% 60%", 'Makan siang di <em>pasir putih</em>', "Rehat di pantai barat Bahuluang, Pantai Bone Kidi dan Bone Bakka. Lunchbox, air toska, tidak ada yang perlu dikejar.", ""),
 (B + "52-pantai-barat-rebahan-di-air.jpg", "45% 50%", 'Sebentar <em>rebahan</em>', "Biarkan air dangkal yang hangat melepas lelah. Kalau ingin, bisa juga mampir ke perkampungan Bahuluang.", ""),
 (B + "37-depan-gua-lipang.jpg", "40% 45%", 'Di depan <em>Gua Lipang</em>', "Tebing batu kapur menjulang, airnya toska sampai dasar terlihat.", ""),
 (B + "43-pintu-masuk-gua-lipang.jpg", "50% 45%", 'Melangkah <em>masuk</em>', "Pintu gua menyambut dengan kolam karang dan cahaya laut di belakang.", ""),
 (B + "47-dalam-gua-lipang-stalaktit-rombongan.jpg", "50% 40%", 'Sejuk di <em>dalam</em>', "Stalaktit menggantung di atas kepala, lantainya pasir putih. Gua yang dibentuk laut selama ribuan tahun.", ""),
 (B + "33-makam-karang-naik-kapal.jpg", "50% 60%", 'Saatnya <em>pulang</em>', "Sekitar pukul tiga kapal kembali ke titik temu, lalu perjalanan darat ke SunaRi.", "15.00"),
 (P + "senja__21-siluet-tamu-tepi-pantai.jpg", "50% 55%", 'Senja <em>menunggu</em> di SunaRi', "Sore hari sudah kembali. Masih sempat mandi dan rebahan, lalu duduk di Pantai Sunari menunggu matahari tenggelam.", "Sore"),
]
T = []
img, pos, t, sub, _ = SL[0]
T.append(f'''<div class="t fc" id="bahuluang-01"><img class="bgf" src="{img}" style="object-position:{pos}" alt="">
  <div class="vt"></div><div class="vb"></div>
  <div class="fk">Dari SunaRi Beach Resort</div><div class="fh">{t}</div><div class="fs">{sub}</div>
  <div class="fg">Ikuti perjalanannya &nbsp;→</div><img class="fl" src="{LOGO_D}" alt=""></div>''')
for k, (img, pos, t, sub, jam) in enumerate(SL[1:], 2):
    chip = f'<span class="chip">{"± " if jam[0].isdigit() else ""}{jam}</span>' if jam else ""
    T.append(f'''<div class="t" id="bahuluang-{k:02d}"><div class="ph"><img src="{img}" style="object-position:{pos}" alt=""><img class="lg" src="{LOGO_D}" alt=""></div>
  <div class="kick">{KICK}{chip}</div><div class="ttl emb">{t}</div><div class="sub">{sub}</div>
  <div class="bt"><span>SunaRi · Selayar</span><span class="h">#sunarisunsetmoment</span><span>{k:02d} / {N:02d}</span></div></div>''')
TL = [("07.00", "Sarapan di SunaRi"), ("08.00", "Berangkat ke titik temu"), ("·", "Kapal dari Bone Taringan / Turungan"), ("10.00", "Makam Karang &amp; snorkeling"),
      ("·", "Pasir Timbul, waktunya diatur kapten"), ("·", "Makan siang di Bone Kidi &amp; Bone Bakka"), ("·", "Jelajah Gua Lipang"), ("15.00", "Kapal pulang, senja di SunaRi")]
T.append(f'''<div class="t" id="bahuluang-20"><div class="frame"></div>
  <img src="{LOGO}" style="position:absolute;left:50%;transform:translateX(-50%);top:84px;width:280px" alt="">
  <div style="position:absolute;left:100px;right:100px;top:300px;text-align:center;color:#45301F">
    <div style="font-weight:700;font-size:21px;letter-spacing:.32em;text-transform:uppercase;color:#7A5039">Simpan alurnya</div>
    <div class="emb" style="font-family:'Playfair Display',serif;font-size:66px;line-height:1.1;margin-top:10px">Satu hari, <em style="color:#A0603E">satu pulau</em></div>
    <div class="tl">{"".join(f"<div><b>{a}</b>{b}</div>" for a, b in TL)}</div>
    <div style="font-family:'Playfair Display',serif;font-style:italic;font-size:29px;color:#7A5039;margin-top:22px">Ingin ke Bahuluang saat menginap? Biar kami bantu atur.</div></div>
  <div style="position:absolute;left:0;right:0;bottom:150px;text-align:center">
    <div style="font-weight:700;font-size:19px;letter-spacing:.26em;text-transform:uppercase;color:#7A5039">Simpan &amp; tag teman perjalananmu</div>
    <div style="font-family:'Playfair Display',serif;font-size:54px;color:#45301F;margin-top:8px"><i style="color:#A0603E">WhatsApp</i> {WA}</div></div>
  <div style="position:absolute;left:0;right:0;bottom:96px;text-align:center;font-weight:600;font-size:19px;letter-spacing:.38em;text-transform:uppercase;color:#7A5039">Pantai Sunari · Selayar</div>
  <div style="position:absolute;left:0;right:0;bottom:62px;text-align:center;font-weight:700;font-size:17px;letter-spacing:.2em;color:#C0592C">#sunarisunsetmoment</div></div>''')
(H / "bahuluang_feed20.html").write_text(f'<!doctype html><html lang="id"><head><meta charset="utf-8">{FONTS}<style>{CSS}</style></head><body>{"".join(T)}</body></html>')
print(len(T))
