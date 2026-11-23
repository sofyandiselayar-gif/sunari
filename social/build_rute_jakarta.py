"""Carousel "Cara ke SunaRi dari Jakarta" (10 slide, 1080x1350). Data rute dari social/STORY_RUTE.md & brand guide.
Run: python3 social/build_rute_jakarta.py && node social/render_rute_jakarta.js -> social/rute-jakarta/"""
import pathlib
H = pathlib.Path(__file__).parent
LOGO = "../assets/logo-sunari-color.png"; LOGO_D = "../assets/logo-sunari-color-dark.png"
M = "../assets/maps/"; PH = "../assets/photos/"; WA = "0821-8903-3044"; N = 10
FONTS = '<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;1,400;1,500&family=Montserrat:wght@500;600;700;800&display=swap" rel="stylesheet">'
CSS = """
*{margin:0;padding:0;box-sizing:border-box}body{background:#bbb;font-family:Montserrat,sans-serif}
.t{position:relative;overflow:hidden;width:1080px;height:1350px;margin:30px auto;background:#FBF4EC;color:#45301F}
.emb{text-shadow:0 1.5px 0 rgba(255,255,255,.85),0 2px 4px rgba(90,62,49,.22)}
.ph{position:absolute;left:60px;right:60px;top:60px;height:760px;border-radius:24px;overflow:hidden;box-shadow:0 14px 36px rgba(90,62,49,.18)}
.ph img{width:100%;height:100%;object-fit:cover}
.ph .lg{position:absolute;left:28px;top:26px;width:190px;height:auto;filter:drop-shadow(0 2px 8px rgba(0,0,0,.5))}
.step{position:absolute;right:26px;top:24px;background:#C0592C;color:#FBF4EC;font-weight:800;font-size:22px;letter-spacing:.2em;text-transform:uppercase;padding:12px 20px;border-radius:999px}
.kick{position:absolute;left:64px;top:862px;font-weight:800;font-size:21px;letter-spacing:.3em;text-transform:uppercase;color:#C0592C}
.ttl{position:absolute;left:64px;right:64px;top:902px;font-family:'Playfair Display',serif;font-size:64px;white-space:nowrap;line-height:1.1}
.ttl em{font-style:italic;color:#A0603E}
.big{position:absolute;left:64px;right:64px;top:1020px;display:flex;gap:36px;align-items:baseline}
.big b{white-space:nowrap;flex:none;font-family:'Playfair Display',serif;font-weight:400;font-size:84px;line-height:1;color:#C0592C}
.big span{font-size:28px;line-height:1.4;color:#4A3426}
.sub{position:absolute;left:64px;right:64px;top:1020px;font-size:30px;line-height:1.5;color:#4A3426}
.bt{position:absolute;left:64px;right:64px;bottom:50px;display:flex;justify-content:space-between;font-weight:700;font-size:18px;letter-spacing:.26em;text-transform:uppercase;color:#7A5039;padding-top:16px;border-top:1.5px solid rgba(138,95,72,.3)}
.bt .h{color:#C0592C;letter-spacing:.12em;text-transform:none}
.fc .bgf{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.fc .vt{position:absolute;left:0;right:0;top:0;height:760px;background:linear-gradient(180deg,rgba(20,12,6,.7),rgba(20,12,6,.35) 60%,rgba(20,12,6,0))}
.fc .vb{position:absolute;left:0;right:0;bottom:0;height:380px;background:linear-gradient(0deg,rgba(20,12,6,.6),rgba(20,12,6,0))}
.list div{padding:30px 0 30px 60px;border-bottom:1.5px solid rgba(138,95,72,.3);font-size:34px;line-height:1.4;position:relative}
.list div i{position:absolute;left:0;top:28px;font-style:normal;font-size:32px}
"""
def foot(k): return f'<div class="bt"><span>SunaRi · Selayar</span><span class="h">#sunarisunsetmoment</span><span>{k:02d} / {N:02d}</span></div>'
def card(k, img, pos, step, kick, ttl, body):
    return f'''<div class="t" id="rute-{k:02d}"><div class="ph"><img src="{img}" style="object-position:{pos}" alt=""><img class="lg" src="{LOGO_D}" alt="">{f'<div class="step">{step}</div>' if step else ''}</div>
  <div class="kick">{kick}</div><div class="ttl emb">{ttl}</div>{body}{foot(k)}</div>'''
big = lambda n, t: f'<div class="big"><b>{n}</b><span>{t}</span></div>'
sub = lambda t: f'<div class="sub">{t}</div>'
T = []
# 1 · hook
T.append(f'''<div class="t fc" id="rute-01"><img class="bgf" src="{PH}pantai/04-kursi-santai-bawah-pohon.jpg" style="object-position:50% 60%" alt="">
  <div class="vt"></div><div class="vb"></div>
  <div style="position:absolute;left:80px;top:96px;font-weight:700;font-size:22px;letter-spacing:.4em;text-transform:uppercase;color:#FBF4EC;text-shadow:0 2px 10px rgba(0,0,0,.5)">Panduan perjalanan</div>
  <div style="position:absolute;left:76px;right:70px;top:146px;font-family:'Playfair Display',serif;font-size:98px;line-height:1.05;color:#FBF4EC;text-shadow:0 3px 18px rgba(0,0,0,.5)">Cara ke <em style="color:#FDB15D">Sunari Beach Resort</em> dari Jakarta ✈️🚗⛴️</div>
  <div style="position:absolute;left:80px;top:640px;font-family:'Playfair Display',serif;font-style:italic;font-size:44px;color:#FBF4EC;text-shadow:0 2px 12px rgba(0,0,0,.6)">(simpan dulu biar nggak lupa)</div>
  <div style="position:absolute;right:64px;bottom:64px;width:300px;height:300px;border-radius:50%;overflow:hidden;border:6px solid #FBF4EC;box-shadow:0 10px 30px rgba(0,0,0,.35)"><img src="{M}02_sulawesi.png" style="width:100%;height:100%;object-fit:cover;object-position:50% 62%;transform:scale(1.55);transform-origin:42% 62%" alt=""></div>
  <div style="position:absolute;left:80px;bottom:76px;font-weight:700;font-size:20px;letter-spacing:.38em;text-transform:uppercase;color:#FBF4EC">Geser &nbsp;→</div>
  <img src="{LOGO_D}" style="position:absolute;left:76px;bottom:120px;width:260px;filter:drop-shadow(0 2px 8px rgba(0,0,0,.45))" alt=""></div>''')
# 2 · gambaran rute
T.append(card(2, M + "03_tiga_rute.png", "50% 42%", "", "Gambaran besarnya", 'Jakarta → Makassar → <em>Selayar</em>',
  '<div class="big"><b>±5 jam</b><span>lewat udara<br>(belum termasuk transit)</span><b>±12 jam</b><span>lewat darat<br>&amp; feri</span></div>'))
# 3 · langkah 1
T.append(card(3, M + "02_sulawesi.png", "50% 55%", "Langkah 1", "Semua rute mulai dari sini", 'Jakarta → <em>Makassar</em> (UPG)',
  big("±2 jam 20 mnt", "Terbang ke Bandara Sultan Hasanuddin, Makassar. Banyak pilihan jadwal setiap hari.")))
# 4 · opsi cepat
T.append(card(4, M + "04_rute1_pesawat.png", "50% 45%", "Opsi cepat", "Langkah 2 · lewat udara", 'Makassar → <em>Aroeppala</em>',
  big("±45 menit", "Pesawat kecil ke Bandara H. Aroeppala, Selayar. Jadwal terbatas, cek di aplikasi tiket minimal H-7.")))
# 5 · opsi darat
T.append(card(5, M + "05_rute2_darat_feri.png", "50% 30%", "Opsi darat", "Langkah 2 · lewat darat", 'Makassar → <em>Bira</em>',
  big("±4–5 jam", "Dari Terminal Malengkeri ke Bira (Bulukumba). Jalan pesisir selatan Sulawesi.")))
# 6 · feri
T.append(card(6, M + "05_rute2_darat_feri.png", "50% 62%", "Opsi darat", "Langkah 3 · menyeberang", 'Feri Bira → <em>Pamatata</em>',
  big("±2 jam", "Menyeberang ke Pulau Selayar. Tips: berangkat dari Makassar pagi hari dan cek jadwal feri lebih dulu.")))
# 7 · ke resort
T.append(card(7, M + "07_pulau_selayar.png", "50% 50%", "Langkah terakhir", "Sampai di Pulau Selayar", 'Menuju <em>Sunari Beach Resort</em>',
  '<div class="sub"><b>Bandara Aroeppala</b> ±10–15 menit · <b>Benteng</b> ±20–30 menit · <b>Pamatata</b> ±1–1,5 jam.<br>Bisa kami jemput (berbayar), kabari jadwal tibamu lewat WhatsApp.</div>'))
# 8 · tips
tips = [("🎫", "Pesan tiket pesawat &amp; feri lebih awal saat libur panjang"), ("💵", "Bawa uang tunai secukupnya untuk perjalanan"),
        ("🚐", "Kabari jadwal tiba supaya penjemputan bisa disiapkan"), ("⛴️", "Alternatif: KM Dharma Kartika III Makassar → Benteng ±10–11 jam (malam, tidak setiap hari)")]
T.append(f'''<div class="t" id="rute-08"><div style="position:absolute;inset:36px;border:1.5px solid rgba(138,95,72,.4)"></div>
  <img src="{LOGO}" style="position:absolute;left:84px;top:96px;width:240px" alt="">
  <div style="position:absolute;left:84px;top:250px;font-weight:800;font-size:21px;letter-spacing:.3em;text-transform:uppercase;color:#C0592C">Sebelum berangkat</div>
  <div class="emb" style="position:absolute;left:84px;right:84px;top:292px;font-family:'Playfair Display',serif;font-size:82px;line-height:1.08">Tips <em style="color:#A0603E">perjalanan</em></div>
  <div class="list" style="position:absolute;left:84px;right:84px;top:440px;border-top:1.5px solid rgba(138,95,72,.3)">{"".join(f"<div><i>{e}</i>{x}</div>" for e, x in tips)}</div>
  {foot(8)}</div>''')
# 9 · payoff
T.append(f'''<div class="t fc" id="rute-09"><img class="bgf" src="{PH}senja/52-pohon-kelapa-bungalow-1747.jpg" style="object-position:50% 45%" alt="">
  <div class="vt" style="height:520px"></div><div class="vb" style="height:620px;background:linear-gradient(0deg,rgba(20,12,6,.75),rgba(20,12,6,0))"></div>
  <div style="position:absolute;left:80px;right:80px;bottom:200px;font-family:'Playfair Display',serif;font-size:84px;line-height:1.1;color:#FBF4EC;text-shadow:0 3px 18px rgba(0,0,0,.5)">Sampai di sini, semua capek perjalanan <em style="color:#FDB15D">terbayar.</em> 🌅</div>
  <img src="{LOGO_D}" style="position:absolute;left:76px;top:80px;width:240px;filter:drop-shadow(0 2px 8px rgba(0,0,0,.45))" alt="">
  <div style="position:absolute;left:80px;right:80px;bottom:60px;display:flex;justify-content:space-between;font-weight:700;font-size:18px;letter-spacing:.26em;color:#FBF4EC"><span>SUNARI · SELAYAR</span><span>09 / {N:02d}</span></div></div>''')
# 10 · CTA
T.append(f'''<div class="t" id="rute-10"><div style="position:absolute;inset:36px;border:1.5px solid rgba(138,95,72,.4)"></div>
  <img src="{LOGO}" style="position:absolute;left:50%;transform:translateX(-50%);top:120px;width:380px" alt="">
  <div style="position:absolute;left:90px;right:90px;top:470px;text-align:center">
    <div style="font-weight:800;font-size:21px;letter-spacing:.3em;text-transform:uppercase;color:#C0592C">Butuh bantuan atur perjalanan?</div>
    <div class="emb" style="font-family:'Playfair Display',serif;font-size:84px;line-height:1.08;margin-top:14px">Chat <em style="color:#A0603E">kami</em> saja</div>
    <div style="font-family:'Playfair Display',serif;font-size:62px;margin-top:30px"><i style="color:#A0603E">WhatsApp</i> {WA}</div>
    <div class="list" style="margin-top:46px;border-top:1.5px solid rgba(138,95,72,.3);text-align:left">
      <div><i>🔖</i>Simpan untuk liburanmu</div><div><i>📩</i>Share ke teman tripmu</div><div><i>👥</i>Tag orang yang mau kamu ajak</div></div></div>
  <div style="position:absolute;left:0;right:0;bottom:96px;text-align:center;font-weight:600;font-size:19px;letter-spacing:.38em;text-transform:uppercase;color:#7A5039">Pantai Sunari · Selayar</div>
  <div style="position:absolute;left:0;right:0;bottom:62px;text-align:center;font-weight:700;font-size:17px;letter-spacing:.2em;color:#C0592C">#sunarisunsetmoment</div></div>''')
(H / "rute_jakarta.html").write_text(f'<!doctype html><html lang="id"><head><meta charset="utf-8">{FONTS}<style>{CSS}</style></head><body>{"".join(T)}</body></html>')
print(len(T))
