"""Versi Story Instagram (1080x1920, export retina 2160x3840) dari carousel "Bungalow Mana yang Cocok Buat Kamu?".
Teks & foto (sudah di-grade tema SunaRi) sama dengan feed. Zona aman: konten di antara 250px dari atas dan 300px dari bawah.
Run: python3 social/grade_pilih_bungalow.py && python3 social/build_pilih_bungalow_story.py && node social/render_pilih_bungalow_story.js
-> social/pilih-bungalow-story/*.png"""
import pathlib
H = pathlib.Path(__file__).parent
WA = "0821-8903-3044"
LOGO_L = "../assets/logo-sunari-cream.png"
LOGO_D = "../assets/logo-sunari-driftwood.png"
G = "../assets/photos/graded/pilih__"
N = 10
FONTS = '<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;1,400;1,500&family=Montserrat:wght@400;500;600;700&display=swap" rel="stylesheet">'
CSS = """
*{margin:0;padding:0;box-sizing:border-box}
body{background:#bbb;font-family:Montserrat,sans-serif;color:#5A3E31}
.s{position:relative;overflow:hidden;margin:30px auto;background:#FBF4EC;width:1080px;height:1920px}
.bg{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.sh{text-shadow:0 2px 16px rgba(0,0,0,.55),0 1px 3px rgba(0,0,0,.4)}
.pf{font-family:'Playfair Display',serif;font-weight:500}
.gold{color:#FDB15D}
.caps{font-weight:700;text-transform:uppercase;letter-spacing:.26em}
.logo{position:absolute;left:50%;transform:translateX(-50%);top:236px;width:220px}
.no{position:absolute;right:76px;top:262px;font-weight:600;font-size:20px;letter-spacing:.3em}
.ft{position:absolute;left:76px;right:76px;bottom:320px;display:flex;justify-content:space-between;font-weight:600;font-size:19px;letter-spacing:.26em;text-transform:uppercase;color:#7A5039;padding-top:22px;border-top:1px solid rgba(166,124,100,.45)}
.ft.l{color:#FBF4EC;border-top-color:rgba(251,244,236,.5)}
.sun{display:inline-block;flex:none;width:15px;height:15px;border-radius:50%;background:linear-gradient(135deg,#FF8A5C,#FDB15D);margin-right:16px}
.row{display:flex;align-items:center;justify-content:space-between;gap:24px;padding:40px 0;border-bottom:1px solid rgba(166,124,100,.45)}
.row:last-child{border-bottom:none}
.row .a{font-family:'Playfair Display',serif;font-style:italic;font-size:42px;line-height:1.2;color:#5A3E31}
.row .b{font-weight:700;font-size:22px;letter-spacing:.2em;text-transform:uppercase;color:#E07A4B;text-align:right;flex:none}
.facts{list-style:none}
.facts li{display:flex;gap:20px;align-items:baseline;font-size:34px;line-height:1.38;margin-top:12px}
.facts li::before{content:"";flex:none;width:13px;height:13px;border-radius:50%;background:linear-gradient(135deg,#FF8A5C,#FDB15D);transform:translateY(-4px)}
.pill{display:inline-block;margin-top:30px;font-weight:600;font-size:27px;line-height:1.4;color:#5A3E31;background:#FBF4EC;padding:18px 30px;text-shadow:none}
.pill b{display:block;font-weight:700;letter-spacing:.22em;text-transform:uppercase;font-size:18px;color:#E07A4B;margin-bottom:6px}
"""
T = []
def foot(n, light=False):
    r = "Ketuk untuk lanjut →" if n < N else "Sampai jumpa di Selayar"
    return f'<div class="ft{" l" if light else ""}"><span>SunaRi · Selayar</span><span>{r}</span></div>'
def no(n, light=False):
    return f'<div class="no" style="color:{"#FBF4EC" if light else "#7A5039"}">{n:02d} / {N:02d}</div>'
GRAD = "background:linear-gradient(180deg,rgba(40,24,14,.8) 0%,rgba(40,24,14,.55) 22%,rgba(40,24,14,0) 38%,rgba(40,24,14,.15) 52%,rgba(40,24,14,.88) 82%,rgba(40,24,14,.92) 100%)"

def photo(n, img, pos, kicker, title, body, title_size=104):
    T.append(f'''<div class="s" id="story-{n:02d}"><img class="bg" src="{G}{img}" style="object-position:{pos}" alt="">
  <div style="position:absolute;inset:0;{GRAD}"></div>
  <img class="logo" src="{LOGO_L}" alt="">
  <div class="sh" style="position:absolute;left:76px;right:76px;top:400px;color:#FBF4EC">
    <div class="caps" style="font-size:23px;color:#FDB15D">{kicker}</div>
    <div class="pf" style="font-size:{title_size}px;line-height:1.03;margin-top:16px;letter-spacing:-.01em">{title}</div></div>
  <div class="sh" style="position:absolute;left:76px;right:76px;bottom:420px;color:#FBF4EC">{body}</div>
  {foot(n, True)}</div>''')

def tipe(n, img, pos, kicker, title, facts, cocok):
    li = "".join(f"<li>{f}</li>" for f in facts)
    photo(n, img, pos, kicker, title, f'<ul class="facts">{li}</ul><div class="pill"><b>Cocok untuk</b>{cocok}</div>')

# 1 hook
T.append(f'''<div class="s" id="story-01"><img class="bg" src="{G}vip-standard-bungalow__02-teras-view-pantai.jpg" style="object-position:50% 50%" alt="">
  <div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(40,24,14,.82) 0%,rgba(40,24,14,.6) 34%,rgba(40,24,14,0) 52%,rgba(40,24,14,.2) 66%,rgba(40,24,14,.85) 100%)"></div>
  <img class="logo" src="{LOGO_L}" alt="">
  <div class="sh" style="position:absolute;left:76px;right:76px;top:400px;color:#FBF4EC">
    <div class="caps" style="font-size:23px;color:#FDB15D">Panduan memilih · SunaRi</div>
    <div class="pf" style="font-size:138px;line-height:1.0;margin-top:20px;letter-spacing:-.015em">Bungalow<br>mana yang<br><i class="gold">cocok buat<br>kamu?</i></div></div>
  <div class="sh" style="position:absolute;left:76px;right:76px;bottom:420px;color:#FBF4EC;font-size:36px;line-height:1.5">Semuanya dekat pantai &amp; menghadap senja.<br>Tinggal pilih gayamu 👉</div>
  {foot(1, True)}</div>''')

# 2 kenali gayamu
rows2 = [("Sederhana, hangat, teras luas", "Standard"), ("Rumah panggung beratap rumbia", "VIP Standard"),
         ("Rumah kayu di antara pohon kelapa", "Superior"), ("Berendam di bawah langit terbuka", "VIP Superior"),
         ("Satu rumah, dua lantai, semua bersama", "Family<br>Superior")]
T.append(f'''<div class="s" id="story-02"><img class="logo" src="{LOGO_D}" alt="">{no(2)}
  <div style="position:absolute;left:76px;right:76px;top:420px">
    <div class="caps" style="font-size:22px;color:#E07A4B">Kenali gayamu dulu</div>
    <div class="pf" style="font-size:124px;line-height:1.02;margin-top:16px">Kamu yang <i style="color:#A67C64">mana?</i></div>
    <div style="font-size:32px;line-height:1.5;margin-top:26px">Semua tipe dekat pantai &amp; menghadap senja. Bedanya di gaya kamarnya.</div>
    <div style="margin-top:44px;border-top:1px solid rgba(166,124,100,.45)">{"".join(f'<div class="row"><span class="a">{a}</span><span class="b">{b}</span></div>' for a, b in rows2)}</div></div>
  {foot(2)}</div>''')

# 3-7 tipe
tipe(3, "standard-bungalow__01-teras-view-laut.jpg", "50% 60%", "01 · Standard Bungalow", "Pagi menghadap<br><i class='gold'>laut Selayar</i>",
     ["Dekat pantai, menghadap view senja", "Queen bed, atap tinggi, teras pribadi luas", "Kamar mandi bambu berlantai batu alam", "2 orang, maks. 3 dengan 1 extra bed (berbayar)"],
     "pasangan yang ingin bangun pelan dengan kopi di teras.")
tipe(4, "vip-standard-bungalow__04-teras-view-laut.jpg", "45% 60%", "02 · VIP Standard Bungalow", "Rumah panggung<br><i class='gold'>di tepi pantai</i>",
     ["Dekat pantai, menghadap view senja", "Beratap rumbia, lebih luas dari Standard", "King bed, area wastafel &amp; gantungan baju", "2 orang, maks. 3 dengan 1 extra bed (berbayar)"],
     "pencinta suasana rumah panggung yang ingin ruang lebih lega.")
tipe(5, "superior-bungalow__04-kamar-loteng.jpg", "50% 50%", "03 · Superior Bungalow", "Rumah kayu<br>di antara<br><i class='gold'>pohon kelapa</i>",
     ["Dekat pantai, menghadap view senja", "A-frame berloteng, king bed, TV", "Kamar mandi semi-outdoor dengan rain shower", "2 orang, maks. 3 dengan 1 extra bed (berbayar)"],
     "kamu yang suka suasana rumah kayu yang hangat &amp; lega.")
tipe(6, "vip-superior-bungalow__06-bathtub-semi-outdoor.jpg", "50% 50%", "04 · VIP Superior Bungalow", "Berendam<br>di bawah<br><i class='gold'>langit terbuka</i>",
     ["Dekat pantai, menghadap view senja", "Bathtub di kamar mandi semi-outdoor beratap kaca", "Air panas &amp; dingin (hanya di tipe ini)", "King bed, TV, mini bar, loteng"],
     "perayaan kecil atau liburan yang terasa istimewa.")
tipe(7, "family-superior-bungalow__01-eksterior-taman.jpg", "55% 50%", "05 · Family Superior Bungalow", "Satu rumah,<br>dua lantai,<br><i class='gold'>semua bersama</i>",
     ["Dekat pantai, menghadap view senja", "Bungalow terbesar: normal 6 orang, maks. 8", "Kamar mandi di kedua lantai", "Teras atau balkon pribadi"],
     "keluarga besar atau rombongan teman.")

# 8 yang sama di semua tipe
inc = ["Sarapan", "AC &amp; Wi-Fi", "Set kopi/teh &amp; pemanas air", "Meja kerja/rias", "Tirai blackout", "Bantal &amp; selimut tambahan", "Setrika (atas permintaan)", "Teras pribadi &amp; kursi santai"]
li8 = "".join(f'<div style="display:flex;align-items:center;padding:22px 0;border-bottom:1px solid rgba(166,124,100,.45);font-size:30px">{"<span class=sun></span>"}{i}</div>' for i in inc)
T.append(f'''<div class="s" id="story-08"><img class="logo" src="{LOGO_D}" alt="">{no(8)}
  <div style="position:absolute;left:76px;right:76px;top:400px">
    <div class="caps" style="font-size:22px;color:#E07A4B">Yang sama di semua tipe</div>
    <div class="pf" style="font-size:80px;line-height:1.05;margin-top:14px">Apa pun pilihanmu,<br><i style="color:#A67C64">ini sudah termasuk</i></div>
    <img src="{G}family-superior-bungalow__10-lantai-atas-kasur-kettle.jpg" style="display:block;width:928px;height:440px;object-fit:cover;object-position:50% 55%;margin-top:36px" alt="">
    <div style="display:grid;grid-template-columns:1fr 1fr;column-gap:44px;margin-top:12px">
      <div>{"".join(li8.split("</div>")[i] + "</div>" for i in range(4))}</div><div>{"".join(li8.split("</div>")[i] + "</div>" for i in range(4, 8))}</div></div></div>
  {foot(8)}</div>''')

# 9 cara cepat memilih
rows9 = [("Berdua, santai &amp; hangat", "Standard<br>atau VIP Standard"), ("Berdua, suka loteng &amp; suasana kayu", "Superior"),
         ("Momen istimewa", "VIP Superior"), ("Keluarga atau rombongan, sampai 8 orang", "Family<br>Superior")]
T.append(f'''<div class="s" id="story-09"><img class="logo" src="{LOGO_D}" alt="">{no(9)}
  <div style="position:absolute;left:76px;right:76px;top:420px">
    <div class="caps" style="font-size:22px;color:#E07A4B">Cara cepat memilih</div>
    <div class="pf" style="font-size:120px;line-height:1.02;margin-top:16px">Masih bingung?<br><i style="color:#A67C64">Ikuti ini</i></div>
    <div style="margin-top:50px;border-top:1px solid rgba(166,124,100,.45)">{"".join(f'<div class="row" style="padding:46px 0"><span class="a">{a}</span><span class="b">{b}</span></div>' for a, b in rows9)}</div>
    <div style="display:flex;align-items:baseline;margin-top:40px;font-size:31px;line-height:1.5"><span class="sun"></span><span>Bertiga? Semua tipe berkapasitas 2 orang bisa menambah 1 extra bed (berbayar).</span></div></div>
  {foot(9)}</div>''')

# 10 CTA
T.append(f'''<div class="s" id="story-10"><img class="bg" src="{G}senja__11-kayak-dan-pulau.jpg" style="object-position:62% 50%" alt="">
  <div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(40,24,14,.7) 0%,rgba(40,24,14,.35) 30%,rgba(40,24,14,.1) 48%,rgba(40,24,14,.55) 68%,rgba(40,24,14,.9) 100%)"></div>
  <img class="logo" src="{LOGO_L}" alt="">
  <div class="sh" style="position:absolute;left:76px;right:76px;top:400px;color:#FBF4EC">
    <div class="caps" style="font-size:23px;color:#FDB15D">Sampai jumpa di Selayar</div>
    <div class="pf" style="font-size:130px;line-height:1.02;margin-top:16px;letter-spacing:-.01em">Sudah ketemu<br><i class="gold">pilihanmu?</i></div></div>
  <div class="sh" style="position:absolute;left:76px;right:76px;bottom:420px;max-width:700px;color:#FBF4EC;font-size:36px;line-height:1.5">
    <div>Simpan dulu, biar liburanmu tinggal berangkat.</div>
    <div style="margin-top:10px">Balas story ini atau chat kami, biar kami bantu memilih.</div>
    <div class="pill" style="font-size:32px"><b>WhatsApp</b>{WA}</div>
    <div class="pf" style="font-style:italic;font-size:34px;margin-top:34px;color:#FDB15D">Where every day ends beautifully.</div></div>
  {foot(10, True)}</div>''')

(H / "pilih_bungalow_story.html").write_text(f'<!doctype html><html lang="id"><head><meta charset="utf-8">{FONTS}<style>{CSS}</style></head><body>{"".join(T)}</body></html>', encoding="utf-8")
print(len(T), "story")
