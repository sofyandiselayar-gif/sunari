"""Feed carousel "Dari SunaRi ke Bahuluang" (10 slide, 1080x1350): cerita perjalanan satu hari, soft selling, SunaRi sebagai base.
Run: python3 social/build_bahuluang_feed.py && node social/render_bahuluang_feed.js -> social/bahuluang-feed/*.png"""
import pathlib
H = pathlib.Path(__file__).parent
exec((H / "build_vipsuperior.py").read_text().split("KICK =")[0].replace("__file__", repr(str(H / "build_vipsuperior.py"))))
P = "../assets/photos/"; N = 10; KICK = "Dari SunaRi ke Bahuluang"
CSS += """
.chip{display:inline-block;margin-left:14px;padding:6px 14px;border-radius:30px;background:linear-gradient(90deg,#FDB15D,#FF8A5C);color:#fff;font-size:17px;letter-spacing:.14em;vertical-align:2px}
.tl{margin-top:26px;border-top:1.5px solid rgba(138,95,72,.3);text-align:left}
.tl div{display:flex;gap:26px;padding:15px 0;border-bottom:1.5px solid rgba(138,95,72,.3);font-size:26px;color:#45301F}
.tl b{flex:0 0 108px;font-weight:700;color:#C0592C;letter-spacing:.04em}
"""
SL = [("bahuluang/10-air-dangkal-toska.jpg", "50% 60%", "Sehari ke<br>Bahuluang", "Pagi berangkat dari SunaRi, senja sudah kembali", ""),
      ("taman/05-meja-taman-view-laut-gazebo.jpg", "50% 55%", 'Semua dimulai <em>dari SunaRi</em>', "Sarapan pelan di Bajoy Beach Resto sambil memandang laut. Siapkan baju renang, topi, dan tabir surya.", "07.00"),
      ("bahuluang/05-kapal-menuju-pulau.jpg", "50% 62%", 'Mengikuti <em>laut</em> hari itu', "Pagi-pagi kami cek pasang-surut dan kabari kamu. Air cukup tinggi, kapal berangkat dari Bone Taringan, sekitar 20 menit. Air surut, kita berangkat dari Turungan.", "08.00"),
      ("bahuluang/14-snorkeling-makam-karang.jpg", "50% 55%", 'Menyapa <em>Makam Karang</em>', "Spot snorkeling dengan formasi karang yang unik. Airnya jernih, ikan-ikan kecil datang menyapa.", "10.00"),
      ("bahuluang/12-berjalan-di-pasir-timbul.jpg", "50% 55%", 'Pasir yang <em>muncul</em>', "Pasir Timbul Bahuluang muncul di tengah laut. Kapten akan membawamu ke sana saat airnya paling pas, lalu kamu bisa berjalan di atasnya.", ""),
      ("bahuluang/11-berjalan-ke-laut-dan-kapal.jpg", "50% 55%", 'Makan siang di <em>pasir putih</em>', "Rehat di Pantai Bahuluang. Lunchbox, air toska, dan tidak ada yang perlu dikejar.", ""),
      ("bahuluang/03-masuk-gua-lipang.jpg", "50% 50%", 'Masuk ke <em>Gua Lipang</em>', "Gua pesisir dengan lengkungan batu kapur, dibentuk laut selama ribuan tahun.", ""),
      ("bahuluang/06-gua-lipang-stalaktit.jpg", "50% 45%", 'Sejuk di <em>dalam</em>', "Stalaktit menggantung di atas kepala. Dari dalam gua, cahaya laut terlihat di ujung lorong.", ""),
      ("senja/21-siluet-tamu-tepi-pantai.jpg", "50% 55%", 'Pulang, senja <em>menunggu</em>', "Sekitar pukul dua kapal kembali. Sore hari sudah di SunaRi, masih sempat rebahan sebelum duduk di Pantai Sunari menunggu matahari tenggelam.", "14.00")]
T = []
img, pos, t, sub, _ = SL[0]
T.append(f'''<div class="t fc" id="bahuluang-01"><img class="bgf" src="{P}{img}" style="object-position:{pos}" alt="">
  <div class="vt"></div><div class="vb"></div>
  <div class="fk">{KICK}</div><div class="fh">{t}</div><div class="fs">{sub}</div>
  <div class="fg">Ikuti perjalanannya &nbsp;→</div><img class="fl" src="{LOGO_D}" alt=""></div>''')
for k, (img, pos, t, sub, jam) in enumerate(SL[1:], 2):
    T.append(f'''<div class="t" id="bahuluang-{k:02d}"><div class="ph"><img src="{P}{img}" style="object-position:{pos}" alt=""><img class="lg" src="{LOGO_D}" alt=""></div>
  <div class="kick">{KICK}{f'<span class="chip">± {jam}</span>' if jam else ""}</div><div class="ttl emb">{t}</div><div class="sub">{sub}</div>
  <div class="bt"><span>SunaRi · Selayar</span><span class="h">#sunarisunsetmoment</span><span>{k:02d} / {N:02d}</span></div></div>''')
TL = [("07.00", "Sarapan di SunaRi"), ("08.00", "Berangkat ke titik temu"), ("·", "Kapal dari Bone Taringan / Turungan"), ("10.00", "Tiba di Pulau Bahuluang"),
      ("·", "Makam Karang, Gua Lipang &amp; makan siang"), ("·", "Pasir Timbul, waktunya diatur kapten"), ("14.00", "Kapal pulang, sore di SunaRi")]
T.append(f'''<div class="t" id="bahuluang-10"><div class="frame"></div>
  <img src="{LOGO}" style="position:absolute;left:50%;transform:translateX(-50%);top:92px;width:300px" alt="">
  <div style="position:absolute;left:100px;right:100px;top:330px;text-align:center;color:#45301F">
    <div style="font-weight:700;font-size:21px;letter-spacing:.32em;text-transform:uppercase;color:#7A5039">Simpan alurnya</div>
    <div class="emb" style="font-family:'Playfair Display',serif;font-size:70px;line-height:1.1;margin-top:12px">Satu hari, <em style="color:#A0603E">satu pulau</em></div>
    <div class="tl">{"".join(f"<div><b>{a}</b>{b}</div>" for a, b in TL)}</div>
    <div style="font-family:'Playfair Display',serif;font-style:italic;font-size:30px;color:#7A5039;margin-top:26px">Ingin ke Bahuluang saat menginap? Biar kami bantu atur.</div></div>
  <div style="position:absolute;left:0;right:0;bottom:150px;text-align:center">
    <div style="font-weight:700;font-size:19px;letter-spacing:.26em;text-transform:uppercase;color:#7A5039">Simpan &amp; tag teman perjalananmu</div>
    <div style="font-family:'Playfair Display',serif;font-size:54px;color:#45301F;margin-top:8px"><i style="color:#A0603E">WhatsApp</i> {WA}</div></div>
  <div style="position:absolute;left:0;right:0;bottom:96px;text-align:center;font-weight:600;font-size:19px;letter-spacing:.38em;text-transform:uppercase;color:#7A5039">Pantai Sunari · Selayar</div>
  <div style="position:absolute;left:0;right:0;bottom:62px;text-align:center;font-weight:700;font-size:17px;letter-spacing:.2em;color:#C0592C">#sunarisunsetmoment</div></div>''')
(H / "bahuluang_feed.html").write_text(f'<!doctype html><html lang="id"><head><meta charset="utf-8">{FONTS}<style>{CSS}</style></head><body>{"".join(T)}</body></html>')
print(len(T))
