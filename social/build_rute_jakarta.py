"""Carousel "Cara ke SunaRi dari Jakarta" (10 slide, 1080x1350). Data rute dari social/STORY_RUTE.md & brand guide.
Run: python3 social/build_rute_jakarta.py && node social/render_rute_jakarta.js -> social/rute-jakarta/"""
import pathlib
H = pathlib.Path(__file__).parent
LOGO = "../assets/logo-sunari-color.png"; LOGO_D = "../assets/logo-sunari-color-dark.png"
M = "../assets/maps/"; PH = "../assets/photos/"; WA = "0821-8903-3044"; N = 11
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
# 1 · hook: 20 foto senja terbaik dalam 1 frame (grid 5×4, terang → gelap) + kalimat soft selling
import numpy as _np
from PIL import Image as _Im
_G = ["74-matahari-menyentuh-laut-kapal", "72-ayunan-di-antara-kelapa", "70-perahu-nelayan-daun-kelapa", "71-siluet-tirai-matahari", "77-ayunan-siluet-dekat", "75-afterglow-dua-sahabat"]
_O = ["45-dua-kayak-matahari-1751", "35-matahari-cakrawala-1751", "64-kayak-double-bawah-matahari-1750", "65-kayak-single-matahari-terbenam-1753",
      "44-dua-kayak-emas-1743", "51-kayak-double-jalur-cahaya-1751", "52-pohon-kelapa-bungalow-1747", "29-dua-kursi-menghadap-senja",
      "28-matahari-di-bawah-daun", "47-payung-di-antara-kelapa-1755", "53-afterglow-lampu-gantung-1807", "60-berdua-bawah-payung-kelapa-1753",
      "10-kayak-pantulan", "37-afterglow-kayak-pelampung-1814"]
_R = H.parent / "assets/photos"
_tiles = []
for f in [("graded/senja__" + x + ".jpg") for x in _G] + [("senja/" + x + ".jpg") for x in _O]:
    _im = _Im.open(_R / f).convert("RGB"); _im.thumbnail((160, 160)); _a = _np.asarray(_im.convert("L"), float)
    _b = _np.asarray(_im.filter(__import__("PIL.ImageFilter", fromlist=["x"]).GaussianBlur(5)).convert("L"), float)
    _y, _x = _np.unravel_index(_b.argmax(), _b.shape)
    _tiles.append((_a.mean(), f, f"{round(100*_x/_b.shape[1])}% {round(100*_y/_b.shape[0])}%"))
_tiles = [(m, f, '50% 62%' if '44-dua-kayak' in f else pos) for m, f, pos in _tiles]
_tiles.sort(key=lambda z: -z[0])
assert len(_tiles) == 20
_grid = "".join(f'<img src="../assets/photos/{f}" style="width:100%;height:100%;object-fit:cover;object-position:{pos};border-radius:10px;display:block;min-width:0;min-height:0" alt="">' for _, f, pos in _tiles)
T.append(f'''<div class="t" id="rute-01">
  <div style="position:absolute;left:60px;right:60px;top:60px;height:740px;display:grid;grid-template-columns:repeat(5,1fr);grid-template-rows:repeat(4,1fr);gap:8px;padding:8px;background:#fff;border-radius:22px;box-shadow:0 14px 36px rgba(90,62,49,.18)">{_grid}</div>
  <div style="position:absolute;left:50%;top:772px;transform:translateX(-50%);background:#C0592C;color:#FBF4EC;font-weight:800;font-size:20px;letter-spacing:.24em;text-transform:uppercase;padding:14px 26px;border-radius:999px;white-space:nowrap;box-shadow:0 8px 20px rgba(192,89,44,.35)">Jakarta ✈️ Makassar ⛴️ Selayar</div>
  <div class="emb" style="position:absolute;left:64px;right:64px;top:868px;font-family:'Playfair Display',serif;font-size:72px;line-height:1.08;text-align:center;color:#45301F">Senja ini menunggumu<br>di <em style="color:#A0603E">Pantai Sunari.</em></div>
  <div style="position:absolute;left:90px;right:90px;top:1046px;font-size:29px;line-height:1.5;text-align:center;color:#4A3426">Begini cara ke Sunari Beach Resort dari Jakarta, lebih mudah dari yang kamu kira.</div>
  <div style="position:absolute;left:0;right:0;top:1160px;text-align:center;font-family:'Playfair Display',serif;font-style:italic;font-size:31px;color:#A0603E">Simpan dulu, biar liburanmu tinggal berangkat.</div>
  <div class="bt"><span>SunaRi · Selayar</span><span class="h">Geser untuk rutenya →</span><span>01 / {N:02d}</span></div></div>''')
# ---- struktur: Opsi A (udara) & Opsi B (darat + feri), tiap langkah format sama
A_COL, B_COL, C_COL, ALL_COL = "#C0592C", "#7A5039", "#2F6E7E", "#45301F"
PATH = {"semua": ["Jakarta", "Makassar", "Selayar", "SunaRi"],
        "A": ["Jakarta", "Makassar", "Aroeppala", "SunaRi"],
        "B": ["Jakarta", "Makassar", "Bira", "Pamatata", "SunaRi"],
        "C": ["Jakarta", "Makassar", "Benteng", "SunaRi"]}
def tracker(path, active, col):
    out = []
    for i, n in enumerate(PATH[path]):
        on = i in active; done = i < min(active)
        dot = f'<span style="display:inline-block;width:24px;height:24px;border-radius:50%;background:{col if (on or done) else "#E8D8C6"};border:3px solid {col if on else "#E8D8C6"};vertical-align:middle"></span>'
        out.append(f'<div style="text-align:center;flex:none;width:150px;position:relative">{dot}<div style="font-size:21px;font-weight:{800 if on else 600};color:{col if on else "#9C8270"};margin-top:8px">{n}</div></div>')
    return ('<div style="position:absolute;left:64px;right:64px;top:1150px;display:flex;justify-content:space-between;align-items:flex-start">'
            '<div style="position:absolute;left:75px;right:75px;top:11px;height:3px;background:#E8D8C6"></div>' + "".join(out) + '</div>')
def step(k, mp, pos, col, opt, lang, frm, to, dur, naik, note, path, active, lgr=False):
    rows = "".join(f'<div style="display:flex;padding:16px 0;border-bottom:1.5px solid rgba(138,95,72,.25)"><div style="width:190px;flex:none;font-weight:800;font-size:20px;letter-spacing:.22em;text-transform:uppercase;color:#9C8270;padding-top:8px">{l}</div><div style="font-size:{s}px;line-height:1.35;{st}">{v}</div></div>'
                   for l, v, s, st in [("Durasi", dur, 46, f"font-family:'Playfair Display',serif;color:{col}"), ("Naik", naik, 30, ""), ("Catatan", note, 28, "color:#4A3426")])
    return f'''<div class="t" id="rute-{k:02d}">
  <div style="position:absolute;left:64px;right:64px;top:52px;display:flex;justify-content:space-between;align-items:center">
    <span style="background:{col};color:#FBF4EC;font-weight:800;font-size:20px;letter-spacing:.2em;text-transform:uppercase;padding:12px 22px;border-radius:999px">{opt}</span>
    <span style="font-weight:800;font-size:20px;letter-spacing:.24em;text-transform:uppercase;color:{col}">{lang}</span></div>
  <div class="ph" style="top:122px;height:560px;background:#094473"><img src="{mp}" style="object-position:{pos}" alt="">{'<div style="position:absolute;inset:0;box-shadow:inset 0 0 50px 34px #094473;pointer-events:none"></div>' if path == "C" else ''}<img class="lg" src="{LOGO_D}" style="{'left:auto;right:28px' if lgr else ''}" alt=""></div>
  <div class="emb" style="position:absolute;left:64px;right:64px;top:712px;font-family:'Playfair Display',serif;font-size:64px;line-height:1.1;white-space:nowrap">{frm} <span style="color:{col}">→</span> <em style="color:#A0603E">{to}</em></div>
  <div style="position:absolute;left:64px;right:64px;top:812px;border-top:1.5px solid rgba(138,95,72,.25)">{rows}</div>
  {tracker(path, active, col)}{foot(k)}</div>'''
def optcard(col, lab, name, steps, total):
    li = "".join(f'<div style="display:flex;gap:16px;padding:20px 0;border-bottom:1.5px solid rgba(138,95,72,.2);font-size:29px;line-height:1.35"><b style="flex:none;width:34px;height:34px;border-radius:50%;background:{col};color:#FBF4EC;font-size:18px;display:flex;align-items:center;justify-content:center">{i}</b><span>{s}</span></div>' for i, s in enumerate(steps, 1))
    return f'''<div style="flex:1;background:#fff;border-radius:22px;padding:36px 30px;box-shadow:0 10px 28px rgba(90,62,49,.12);border-top:8px solid {col}">
      <div style="font-weight:800;font-size:19px;letter-spacing:.2em;text-transform:uppercase;color:{col}">{lab}</div>
      <div style="font-family:'Playfair Display',serif;font-size:54px;margin:10px 0 18px">{name}</div>{li}
      <div style="margin-top:30px;font-weight:700;font-size:20px;letter-spacing:.2em;text-transform:uppercase;color:#9C8270">Total di jalan</div>
      <div style="font-family:'Playfair Display',serif;font-size:66px;color:{col};line-height:1.1">{total}</div></div>'''
T.append(f'''<div class="t" id="rute-02">
  <div style="position:absolute;left:64px;top:70px;font-weight:800;font-size:21px;letter-spacing:.3em;text-transform:uppercase;color:#C0592C">3 jalan menuju senja</div>
  <div class="emb" style="position:absolute;left:64px;right:64px;top:110px;font-family:'Playfair Display',serif;font-size:70px;line-height:1.08;white-space:nowrap">Jakarta → Makassar → <em style="color:#A0603E">Selayar</em></div>
  <div style="position:absolute;left:64px;right:64px;top:250px;display:flex;gap:28px;align-items:stretch">
    {optcard(A_COL, "Opsi A · Paling cepat", "Udara", ["Pesawat Jakarta → Makassar", "Pesawat Makassar → Aroeppala", "Mobil ke SunaRi"], "±3,5 jam")}
    {optcard(B_COL, "Opsi B · Paling berkesan", "Darat &amp; feri", ["Pesawat Jakarta → Makassar", "Mobil Makassar → Bira", "Feri Bira → Pamatata", "Mobil ke SunaRi"], "±10–11 jam")}</div>
  <div style="position:absolute;left:64px;right:64px;top:1030px;background:#fff;border-radius:18px;border-left:8px solid {C_COL};box-shadow:0 8px 22px rgba(90,62,49,.1);padding:20px 26px;display:flex;align-items:center;gap:22px">
    <div style="flex:1"><div style="font-weight:800;font-size:18px;letter-spacing:.2em;text-transform:uppercase;color:{C_COL}">Opsi C · Santai di kapal</div>
      <div style="font-size:27px;margin-top:4px">KM Dharma Kartika III Makassar → Benteng</div></div>
    <div style="font-family:'Playfair Display',serif;font-size:50px;color:{C_COL};white-space:nowrap">±10–11 jam</div></div>
  <div style="position:absolute;left:64px;right:64px;top:1180px;font-size:22px;line-height:1.4;color:#7A5039;text-align:center">Pilih yang paling cocok, semuanya berakhir di senja yang sama. Geser →</div>
  {foot(2)}</div>''')
T.append(step(3, M + "08_jakarta_makassar.png", "62% 50%", ALL_COL, "Opsi A &amp; B", "Langkah 1", "Jakarta", "Makassar", "±2 jam 30 menit",
  "✈️ Pesawat ke Bandara Sultan Hasanuddin (UPG)", "Banyak pilihan jadwal setiap hari. Liburanmu dimulai di sini.", "semua", [0, 1]))
T.append(step(4, M + "04_rute1_pesawat_tanpa-sublabel.png", "50% 45.5%", A_COL, "Opsi A · Udara", "Langkah 2 dari 3", "Makassar", "Aroeppala", "±45 menit",
  "🛩️ Pesawat ke Bandara H. Aroeppala", "Jadwal terbatas, cek minimal H-7. Dari jendela, birunya Selayar sudah menyapa.", "A", [1, 2], lgr=True))
T.append(step(5, M + "05_rute2_darat_feri.png", "50% 30%", B_COL, "Opsi B · Darat", "Langkah 2 dari 4", "Makassar", "Bira", "±4–5 jam",
  "🚗 Mobil/bus dari Terminal Malengkeri", "Berangkat pagi, nikmati jalan pesisir selatan Sulawesi.", "B", [1, 2]))
T.append(step(6, M + "05_rute2_darat_feri.png", "50% 64%", B_COL, "Opsi B · Feri", "Langkah 3 dari 4", "Bira", "Pamatata", "±2 jam",
  "⛴️ Feri penyeberangan ke Pulau Selayar", "Cek jadwal lebih dulu. Angin laut jadi penyambut pertama.", "B", [2, 3]))
T.append(step(7, M + "06_rute3_kapal_laut.png", "50% 46%;transform:scale(.94);transform-origin:50% 62%", C_COL, "Opsi C · Kapal", "Langkah 2 dari 3", "Makassar", "Benteng", "±10–11 jam",
  "🚢 KM Dharma Kartika III, langsung tanpa feri", "Berangkat malam, tidak setiap hari. Tidur di kapal, bangun sudah di Selayar.", "C", [1, 2], lgr=True))
arr = [("Bandara H. Aroeppala", "dari Opsi A", "±10–15 menit"), ("Pelabuhan Pamatata", "dari Opsi B", "±1–1,5 jam"), ("Pelabuhan Benteng", "dari Opsi C", "±20–30 menit")]
rows7 = "".join(f'<div style="display:flex;align-items:center;padding:20px 0;border-bottom:1.5px solid rgba(138,95,72,.25)"><div style="flex:1"><div style="font-size:30px;font-weight:600">{a}</div><div style="font-size:19px;font-weight:700;letter-spacing:.18em;text-transform:uppercase;color:#9C8270;margin-top:4px">{o}</div></div><div style="font-family:Playfair Display,serif;font-size:46px;color:#C0592C;white-space:nowrap">{d}</div></div>' for a, o, d in arr)
T.append(f'''<div class="t" id="rute-08">
  <div style="position:absolute;left:64px;right:64px;top:52px;display:flex;justify-content:space-between;align-items:center">
    <span style="background:{ALL_COL};color:#FBF4EC;font-weight:800;font-size:20px;letter-spacing:.2em;text-transform:uppercase;padding:12px 22px;border-radius:999px">Semua opsi</span>
    <span style="font-weight:800;font-size:20px;letter-spacing:.24em;text-transform:uppercase;color:{ALL_COL}">Langkah terakhir</span></div>
  <div class="ph" style="top:122px;height:440px;background:#094473"><img src="{M}07_pulau_selayar.png" style="position:absolute;left:150px;top:-300px;width:680px;height:1209px;object-fit:fill" alt=""><div style="position:absolute;inset:0;box-shadow:inset 0 0 50px 34px #094473;pointer-events:none"></div><img class="lg" src="{LOGO_D}" alt=""></div>
  <div class="emb" style="position:absolute;left:64px;right:64px;top:592px;font-family:'Playfair Display',serif;font-size:64px;line-height:1.1">Selangkah lagi ke <em style="color:#A0603E">SunaRi</em></div>
  <div style="position:absolute;left:64px;right:64px;top:690px;font-weight:800;font-size:19px;letter-spacing:.24em;text-transform:uppercase;color:#9C8270">Dari titik kedatangan · naik mobil</div>
  <div style="position:absolute;left:64px;right:64px;top:730px;border-top:1.5px solid rgba(138,95,72,.25)">{rows7}</div>
  <div style="position:absolute;left:64px;right:64px;top:1110px;background:#F3E3CC;border-radius:18px;padding:20px 26px;font-size:26px;line-height:1.4">🚐 <b>Biar kami yang menjemput</b> (berbayar). Kabari jadwal tibamu lewat WhatsApp.</div>
  {foot(8)}</div>''')
# 8 · tips
tips = [("🎫", "Pesan tiket pesawat &amp; feri lebih awal, apalagi saat libur panjang"), ("💵", "Siapkan uang tunai secukupnya untuk di perjalanan"),
        ("🚐", "Kabari jadwal tibamu, biar kami siapkan penjemputan"), ("🗺️", "Simpan lokasi SunaRi di Google Maps, biar tidak tersesat")]
T.append(f'''<div class="t" id="rute-09"><div style="position:absolute;inset:36px;border:1.5px solid rgba(138,95,72,.4)"></div>
  <img src="{LOGO}" style="position:absolute;left:84px;top:96px;width:240px" alt="">
  <div style="position:absolute;left:84px;top:250px;font-weight:800;font-size:21px;letter-spacing:.3em;text-transform:uppercase;color:#C0592C">Supaya perjalananmu tenang</div>
  <div class="emb" style="position:absolute;left:84px;right:84px;top:292px;font-family:'Playfair Display',serif;font-size:82px;line-height:1.08">Bekal <em style="color:#A0603E">sebelum berangkat</em></div>
  <div class="list" style="position:absolute;left:84px;right:84px;top:440px;border-top:1.5px solid rgba(138,95,72,.3)">{"".join(f"<div><i>{e}</i>{x}</div>" for e, x in tips)}</div>
  {foot(9)}</div>''')
# 9 · payoff
T.append(f'''<div class="t fc" id="rute-10"><img class="bgf" src="{PH}senja/52-pohon-kelapa-bungalow-1747.jpg" style="object-position:50% 45%" alt="">
  <div class="vt" style="height:520px"></div><div class="vb" style="height:620px;background:linear-gradient(0deg,rgba(20,12,6,.75),rgba(20,12,6,0))"></div>
  <div style="position:absolute;left:80px;right:80px;bottom:200px;font-family:'Playfair Display',serif;font-size:84px;line-height:1.1;color:#FBF4EC;text-shadow:0 3px 18px rgba(0,0,0,.5)">Sampai di sini, semua capek perjalanan <em style="color:#FDB15D">terbayar.</em> 🌅</div>
  <img src="{LOGO_D}" style="position:absolute;left:76px;top:80px;width:240px;filter:drop-shadow(0 2px 8px rgba(0,0,0,.45))" alt="">
  <div style="position:absolute;left:80px;right:80px;bottom:60px;display:flex;justify-content:space-between;font-weight:700;font-size:18px;letter-spacing:.26em;color:#FBF4EC"><span>SUNARI · SELAYAR</span><span>10 / {N:02d}</span></div></div>''')
# 10 · CTA
T.append(f'''<div class="t" id="rute-11"><div style="position:absolute;inset:36px;border:1.5px solid rgba(138,95,72,.4)"></div>
  <img src="{LOGO}" style="position:absolute;left:50%;transform:translateX(-50%);top:120px;width:380px" alt="">
  <div style="position:absolute;left:90px;right:90px;top:470px;text-align:center">
    <div style="font-weight:800;font-size:21px;letter-spacing:.3em;text-transform:uppercase;color:#C0592C">Bingung atur perjalanannya?</div>
    <div class="emb" style="font-family:'Playfair Display',serif;font-size:84px;line-height:1.08;margin-top:14px">Biar kami <em style="color:#A0603E">bantu</em></div>
    <div style="font-family:'Playfair Display',serif;font-size:62px;margin-top:30px"><i style="color:#A0603E">WhatsApp</i> {WA}</div>
    <div class="list" style="margin-top:46px;border-top:1.5px solid rgba(138,95,72,.3);text-align:left">
      <div><i>🔖</i>Simpan untuk liburanmu berikutnya</div><div><i>📩</i>Kirim ke teman tripmu</div><div><i>👥</i>Tag orang yang ingin kamu ajak menikmati senja</div></div></div>
  <div style="position:absolute;left:0;right:0;bottom:96px;text-align:center;font-weight:600;font-size:19px;letter-spacing:.38em;text-transform:uppercase;color:#7A5039">Pantai Sunari · Selayar</div>
  <div style="position:absolute;left:0;right:0;bottom:62px;text-align:center;font-weight:700;font-size:17px;letter-spacing:.2em;color:#C0592C">#sunarisunsetmoment</div></div>''')
(H / "rute_jakarta.html").write_text(f'<!doctype html><html lang="id"><head><meta charset="utf-8">{FONTS}<style>{CSS}</style></head><body>{"".join(T)}</body></html>')
print(len(T))
