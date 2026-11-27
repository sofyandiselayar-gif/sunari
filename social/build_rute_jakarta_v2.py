"""Feed carousel "Cara ke SunaRi dari Jakarta" versi 2 (10 slide, 1080x1350): gaya feed SunaRi terbaru (kartu foto/peta,
judul serif, kalimat storytelling, foto color grading). Data rute sama dengan build_rute_jakarta.py & brand guide.
Run: python3 social/build_rute_jakarta_v2.py && node social/render_rute_jakarta_v2.js -> social/rute-jakarta-v2/"""
import pathlib
H = pathlib.Path(__file__).parent
exec((H / "build_vipsuperior.py").read_text().split("KICK =")[0].replace("__file__", repr(str(H / "build_vipsuperior.py"))))
M = "../assets/maps/"; G = "../assets/photos/graded/"; N = 10; KICK = "Jakarta ke SunaRi"
CSS += """
.ph{background:#094473}
.chip{display:inline-block;margin-left:14px;padding:6px 14px;border-radius:30px;background:linear-gradient(90deg,#FDB15D,#FF8A5C);color:#fff;font-size:17px;letter-spacing:.14em;vertical-align:2px}
.opt{position:absolute;right:26px;top:24px;font-weight:700;font-size:19px;letter-spacing:.18em;text-transform:uppercase;color:#FBF4EC;padding:11px 20px;border-radius:999px}
.ttl{font-size:70px}
.sub{font-size:29px}
.rows{border-top:1.5px solid rgba(138,95,72,.3)}
.rows div{display:flex;justify-content:space-between;align-items:baseline;gap:20px;padding:20px 0;border-bottom:1.5px solid rgba(138,95,72,.3);font-size:29px;color:#45301F}
.rows b{font-family:'Playfair Display',serif;font-weight:400;font-size:40px;color:#C0592C;white-space:nowrap}
.rows small{display:block;font-size:17px;font-weight:700;letter-spacing:.18em;text-transform:uppercase;color:#9C8270;margin-top:4px}
"""
A, B, C, ALL = "#C0592C", "#7A5039", "#2F6E7E", "#45301F"
def foot(k): return f'<div class="bt"><span>SunaRi · Selayar</span><span class="h">#sunarisunsetmoment</span><span>{k:02d} / {N:02d}</span></div>'
def step(k, img, pos, col, opt, frm, to, dur, sub, extra=""):
    wide = k == 3   # peta Jakarta–Makassar berbentuk lanskap 2:1 -> kartu peta lebih pendek, teks naik
    ph, up = ('style="height:510px"', ' style="position:absolute;inset:0;transform:translateY(-330px)"') if wide else ("", "")
    rows3 = ('<div class="rows" style="position:absolute;left:64px;right:64px;top:870px">'
             '<div><span>Berangkat<small>Jakarta</small></span><b style="font-size:32px">Bandara Soekarno-Hatta</b></div>'
             '<div><span>Tiba<small>Makassar</small></span><b style="font-size:32px">Bandara Sultan Hasanuddin</b></div>'
             f'<div><span>Durasi<small>pesawat</small></span><b>±{dur}</b></div></div>') if wide else ""
    return f'''<div class="t" id="rute-{k:02d}"><div class="ph" {ph}><img src="{img}" style="object-position:{pos}{extra}" alt=""><img class="lg" src="{LOGO_D}" alt=""><div class="opt" style="background:{col}">{opt}</div></div>
  <div{up}><div class="kick">{KICK}<span class="chip">± {dur}</span></div><div class="ttl emb">{frm} <span style="color:{col}">→</span> <em>{to}</em></div><div class="sub">{sub}</div></div>{rows3}{foot(k)}</div>'''
T = []
# 1 · sampul
T.append(f'''<div class="t fc" id="rute-01"><img class="bgf" src="{G}senja__74-matahari-menyentuh-laut-kapal.jpg" style="object-position:50% 55%" alt="">
  <div class="vt"></div><div class="vb"></div>
  <div class="fk">Cara ke SunaRi</div><div class="fh">Dari Jakarta<br>ke Pantai Sunari</div>
  <div class="fs" style="top:460px">Lebih dekat dari yang kamu kira</div>
  <div class="fg">Simpan rutenya &nbsp;→</div><img class="fl" src="{LOGO_D}" alt=""></div>''')
# 2 · ringkasan 3 opsi
def opt(col, lab, name, path, total):
    return f'''<div style="background:#fff;border-radius:20px;padding:30px 34px;box-shadow:0 10px 26px rgba(90,62,49,.12);border-left:8px solid {col};display:flex;justify-content:space-between;align-items:center;gap:24px">
      <div><div style="font-weight:700;font-size:18px;letter-spacing:.2em;text-transform:uppercase;color:{col}">{lab}</div>
      <div style="font-family:'Playfair Display',serif;font-size:50px;margin-top:6px">{name}</div>
      <div style="font-size:24px;color:#5A3E31;margin-top:8px">{path}</div></div>
      <div style="text-align:right;flex:none"><div style="font-weight:700;font-size:16px;letter-spacing:.2em;text-transform:uppercase;color:#9C8270">Di jalan</div>
      <div style="font-family:'Playfair Display',serif;font-size:56px;color:{col};white-space:nowrap">{total}</div></div></div>'''
T.append(f'''<div class="t" id="rute-02">
  <div class="kick" style="top:90px">3 jalan menuju senja</div>
  <div class="ttl emb" style="top:132px">Pilih yang <em>paling cocok</em></div>
  <div style="position:absolute;left:64px;right:64px;top:290px;display:flex;flex-direction:column;gap:26px">
    {opt(A, "Opsi A · Paling cepat", "Udara", "Pesawat → pesawat → mobil", "±3,5 jam")}
    {opt(B, "Opsi B · Paling berkesan", "Darat &amp; feri", "Pesawat → mobil → feri → mobil", "±10–11 jam")}
    {opt(C, "Opsi C · Santai di kapal", "Kapal langsung", "Pesawat → KM Dharma Kartika III → mobil", "±10–11 jam")}</div>
  <div class="sub" style="top:960px;text-align:center;font-family:'Playfair Display',serif;font-style:italic;color:#7A5039">Semua jalan berakhir di senja yang sama.<br><span style="font-family:Montserrat;font-style:normal;font-size:22px">*Belum termasuk waktu transit &amp; menunggu jadwal</span></div>
  {foot(2)}</div>''')
T.append(step(3, M + "08_jakarta_makassar.png", "52% 50%", ALL, "Semua opsi", "Jakarta", "Makassar", "2 jam 30 menit",
  "Pesawat ke Bandara Sultan Hasanuddin. Banyak jadwal setiap hari, dan di sinilah liburanmu dimulai."))
T.append(step(4, M + "04_rute1_pesawat_tanpa-sublabel.png", "50% 45%", A, "Opsi A · Udara", "Makassar", "Aroeppala", "45 menit",
  "Pesawat ke Bandara H. Aroeppala. Jadwalnya terbatas, cek minimal H-7. Dari jendela, birunya Selayar sudah menyapa."))
T.append(step(5, M + "05_rute2_darat_feri.png", "50% 30%", B, "Opsi B · Darat", "Makassar", "Bira", "4–5 jam",
  "Mobil atau bus dari Terminal Malengkeri. Berangkat pagi, nikmati jalan pesisir selatan Sulawesi."))
T.append(step(6, M + "05_rute2_darat_feri.png", "50% 64%", B, "Opsi B · Feri", "Bira", "Pamatata", "2 jam",
  "Feri penyeberangan ke Pulau Selayar. Cek jadwal lebih dulu, angin laut jadi penyambut pertama."))
T.append(step(7, M + "06_rute3_kapal_laut.png", "50% 46%", C, "Opsi C · Kapal", "Makassar", "Benteng", "10–11 jam",
  "KM Dharma Kartika III, tanpa ganti feri. Berangkat malam, tidak setiap hari. Tidur di kapal, bangun sudah di Selayar."))
# 8 · langkah terakhir
rows = "".join(f'<div><span>{a}<small>{o}</small></span><b>±{d}</b></div>' for a, o, d in
               [("Bandara H. Aroeppala", "dari Opsi A", "10–15 menit"), ("Pelabuhan Pamatata", "dari Opsi B", "1–1,5 jam"), ("Pelabuhan Benteng", "dari Opsi C", "20–30 menit")])
T.append(f'''<div class="t" id="rute-08"><div class="ph" style="height:500px"><img src="{M}07_pulau_selayar.png" style="position:absolute;left:150px;top:-330px;width:680px;height:1209px;object-fit:fill" alt=""><div style="position:absolute;inset:0;box-shadow:inset 0 0 50px 34px #094473"></div><img class="lg" src="{LOGO_D}" alt=""><div class="opt" style="background:{ALL}">Langkah terakhir</div></div>
  <div class="kick" style="top:600px">{KICK} · naik mobil</div><div class="ttl emb" style="top:642px">Selangkah lagi ke <em>SunaRi</em></div>
  <div class="rows" style="position:absolute;left:64px;right:64px;top:750px">{rows}</div>
  <div style="position:absolute;left:64px;right:64px;top:1130px;background:#F3E3CC;border-radius:16px;padding:18px 24px;font-size:25px;line-height:1.4">Biar kami yang menjemput (berbayar). Kabari jadwal tibamu lewat WhatsApp.</div>
  {foot(8)}</div>''')
# 9 · payoff (Senja no. 10)
T.append(f'''<div class="t" id="rute-09"><div class="ph"><img src="{G}senja__52-pohon-kelapa-bungalow-1747.jpg" style="object-position:50% 50%" alt=""><img class="lg" src="{LOGO_D}" alt=""></div>
  <div class="kick">{KICK}<span class="chip">Sore</span></div><div class="ttl emb">Lalu senja <em>menyambut</em></div>
  <div class="sub">Sore itu saya sadar, perjalanan jauh ke Selayar terbayar lunas hanya dalam lima belas menit senja.</div>{foot(9)}</div>''')
# 10 · bekal + CTA
tips = ["Pesan tiket pesawat &amp; feri lebih awal, apalagi saat libur panjang", "Siapkan uang tunai secukupnya untuk di perjalanan",
        "Kabari jadwal tibamu, biar kami siapkan penjemputan", "Simpan lokasi SunaRi di Google Maps"]
T.append(f'''<div class="t" id="rute-10"><div class="frame"></div>
  <img src="{LOGO}" style="position:absolute;left:50%;transform:translateX(-50%);top:84px;width:280px" alt="">
  <div style="position:absolute;left:100px;right:100px;top:300px;text-align:center;color:#45301F">
    <div style="font-weight:700;font-size:21px;letter-spacing:.32em;text-transform:uppercase;color:#7A5039">Bekal sebelum berangkat</div>
    <div class="emb" style="font-family:'Playfair Display',serif;font-size:66px;line-height:1.1;margin-top:10px">Biar perjalanan <em style="color:#A0603E">tenang</em></div>
    <div class="fx" style="grid-template-columns:1fr;margin-top:30px">{"".join(f"<div>{x}</div>" for x in tips)}</div>
    <div style="font-family:'Playfair Display',serif;font-style:italic;font-size:30px;color:#7A5039;margin-top:26px">Bingung atur jadwalnya? Biar kami bantu.</div></div>
  <div style="position:absolute;left:0;right:0;bottom:150px;text-align:center">
    <div style="font-weight:700;font-size:19px;letter-spacing:.26em;text-transform:uppercase;color:#7A5039">Simpan &amp; tag teman perjalananmu</div>
    <div style="font-family:'Playfair Display',serif;font-size:54px;color:#45301F;margin-top:8px"><i style="color:#A0603E">WhatsApp</i> {WA}</div></div>
  <div style="position:absolute;left:0;right:0;bottom:96px;text-align:center;font-weight:600;font-size:19px;letter-spacing:.38em;text-transform:uppercase;color:#7A5039">Pantai Sunari · Selayar</div>
  <div style="position:absolute;left:0;right:0;bottom:62px;text-align:center;font-weight:700;font-size:17px;letter-spacing:.2em;color:#C0592C">#sunarisunsetmoment</div></div>''')
(H / "rute_jakarta_v2.html").write_text(f'<!doctype html><html lang="id"><head><meta charset="utf-8">{FONTS}<style>{CSS}</style></head><body>{"".join(T)}</body></html>')
print(len(T))
