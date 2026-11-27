"""Carousel 10 slide "Bungalow Mana yang Cocok Buat Kamu?" (feed 1080x1350, export retina 2160x2700).
Run: python3 social/grade_pilih_bungalow.py && python3 social/build_pilih_bungalow.py && node social/render_pilih_bungalow.js  -> social/pilih-bungalow/*.png
Skrip & teks: social/SKRIP_PILIH_BUNGALOW.md"""
import pathlib
H = pathlib.Path(__file__).parent
WA = "0821-8903-3044"
LOGO_L = "../assets/logo-sunari-cream.png"       # di atas foto
LOGO_D = "../assets/logo-sunari-driftwood.png"   # di atas Shell Cream
P = "../assets/photos/"
TOTAL = 10
FONTS = '<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;1,400;1,500&family=Montserrat:wght@400;500;600;700&display=swap" rel="stylesheet">'
CSS = """
*{margin:0;padding:0;box-sizing:border-box}
body{background:#bbb;font-family:Montserrat,sans-serif;color:#5A3E31}
.t{position:relative;overflow:hidden;margin:30px auto;background:#FBF4EC;width:1080px;height:1350px}
.bg{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.sh{text-shadow:0 2px 16px rgba(0,0,0,.55),0 1px 3px rgba(0,0,0,.4)}
.pf{font-family:'Playfair Display',serif;font-weight:500}
.it{font-style:italic}
.gold{color:#FDB15D}
.caps{font-weight:700;text-transform:uppercase;letter-spacing:.26em}
.logo{position:absolute;left:50%;transform:translateX(-50%);top:52px;width:200px}
.ft{position:absolute;left:72px;right:72px;bottom:56px;display:flex;justify-content:space-between;font-weight:600;font-size:17px;letter-spacing:.24em;text-transform:uppercase;color:#7A5039;padding-top:20px;border-top:1px solid rgba(166,124,100,.45)}
.ft.l{color:#FBF4EC;border-top-color:rgba(251,244,236,.5)}
.sun{display:inline-block;width:14px;height:14px;border-radius:50%;background:linear-gradient(135deg,#FF8A5C,#FDB15D);margin-right:14px}
.row{display:flex;align-items:center;justify-content:space-between;gap:24px;padding:38px 0;border-bottom:1px solid rgba(166,124,100,.45)}
.row:last-child{border-bottom:none}
.row .a{font-family:'Playfair Display',serif;font-style:italic;font-size:38px;line-height:1.2;color:#5A3E31}
.row .b{font-weight:700;font-size:21px;letter-spacing:.2em;text-transform:uppercase;color:#E07A4B;text-align:right;flex:none}
.facts{list-style:none}
.facts li{display:flex;gap:18px;align-items:baseline;font-size:29px;line-height:1.36;margin-top:10px}
.facts li::before{content:"";flex:none;width:11px;height:11px;border-radius:50%;background:linear-gradient(135deg,#FF8A5C,#FDB15D);transform:translateY(-3px)}
.pill{display:inline-block;margin-top:24px;font-weight:600;font-size:23px;letter-spacing:.04em;color:#5A3E31;background:#FBF4EC;padding:14px 26px}
.pill b{font-weight:700;letter-spacing:.2em;text-transform:uppercase;font-size:17px;color:#E07A4B;margin-right:12px}
"""
T = []
def foot(n, light=False, right=None):
    r = right or ("GESER →" if n < TOTAL else f"{n:02d} / {TOTAL:02d}")
    return f'<div class="ft{" l" if light else ""}"><span>SunaRi · Selayar</span><span>{r}</span></div>'

def photo(n, img, pos, kicker, title, body, grad_top=.78, grad_bot=.82, tid=None):
    T.append(f'''<div class="t" id="pilih-{n:02d}"><img class="bg" src="{P}{img}" style="object-position:{pos}" alt="">
  <div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(40,24,14,{grad_top}) 0%,rgba(40,24,14,.42) 32%,rgba(40,24,14,0) 46%,rgba(40,24,14,.25) 58%,rgba(40,24,14,{grad_bot}) 100%)"></div>
  <img class="logo" src="{LOGO_L}" alt="">
  <div class="sh" style="position:absolute;left:72px;right:72px;top:205px;color:#FBF4EC">
    <div class="caps" style="font-size:21px;color:#FDB15D">{kicker}</div>
    <div class="pf" style="font-size:92px;line-height:1.03;margin-top:14px;letter-spacing:-.01em">{title}</div></div>
  <div class="sh" style="position:absolute;left:72px;right:72px;bottom:130px;color:#FBF4EC">{body}</div>
  {foot(n, True)}</div>''')

def tipe(n, img, pos, kicker, title, facts, cocok, **kw):
    li = "".join(f"<li>{f}</li>" for f in facts)
    body = f'<ul class="facts">{li}</ul><div class="pill" style="text-shadow:none"><b>Cocok untuk</b>{cocok}</div>'
    photo(n, img, pos, kicker, title, body, **kw)

# 1 hook ---------------------------------------------------------------
T.append(f'''<div class="t" id="pilih-01"><img class="bg" src="{P}graded/pilih__vip-standard-bungalow__02-teras-view-pantai.jpg" style="object-position:50% 55%" alt="">
  <div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(40,24,14,.78) 0%,rgba(40,24,14,.5) 40%,rgba(40,24,14,0) 58%,rgba(40,24,14,.55) 100%)"></div>
  <img class="logo" src="{LOGO_L}" alt="">
  <div class="sh" style="position:absolute;left:72px;right:72px;top:205px;color:#FBF4EC">
    <div class="caps" style="font-size:21px;color:#FDB15D">Panduan memilih · SunaRi</div>
    <div class="pf" style="font-size:116px;line-height:1.0;margin-top:16px;letter-spacing:-.015em">Bungalow<br>mana yang<br><i class="gold">cocok buat<br>kamu?</i></div></div>
  <div class="sh" style="position:absolute;left:72px;right:72px;bottom:130px;color:#FBF4EC;font-size:30px;line-height:1.5">Semuanya dekat pantai &amp; menghadap senja.<br>Tinggal pilih gayamu 👉</div>
  {foot(1, True)}</div>''')

# 2 kenali gayamu --------------------------------------------------------
rows2 = [("Sederhana, hangat, teras luas", "Standard"),
         ("Rumah panggung beratap rumbia", "VIP Standard"),
         ("Rumah kayu di antara pohon kelapa", "Superior"),
         ("Berendam di bawah langit terbuka", "VIP Superior"),
         ("Satu rumah, dua lantai, semua bersama", "Family Superior")]
T.append(f'''<div class="t" id="pilih-02">
  <img class="logo" src="{LOGO_D}" alt="">
  <div style="position:absolute;left:72px;right:72px;top:215px">
    <div class="caps" style="font-size:20px;color:#E07A4B">Kenali gayamu dulu</div>
    <div class="pf" style="font-size:104px;line-height:1.02;margin-top:14px;color:#5A3E31">Kamu yang <i style="color:#A67C64">mana?</i></div>
    <div style="font-size:27px;line-height:1.5;margin-top:22px;color:#5A3E31">Semua tipe dekat pantai &amp; menghadap senja.<br>Bedanya di gaya kamarnya.</div>
    <div style="margin-top:34px;border-top:1px solid rgba(166,124,100,.45)">{"".join(f'<div class="row"><span class="a">{a}</span><span class="b">{b}</span></div>' for a, b in rows2)}</div></div>
  {foot(2)}</div>''')

# 3-7 tipe -----------------------------------------------------------------
tipe(3, "graded/pilih__standard-bungalow__01-teras-view-laut.jpg", "50% 60%", "01 · Standard Bungalow", "Pagi menghadap<br><i class='gold'>laut Selayar</i>",
     ["Dekat pantai, menghadap view senja", "Queen bed, atap tinggi, teras pribadi luas", "Kamar mandi bambu berlantai batu alam", "2 orang, maks. 3 dengan 1 extra bed (berbayar)"],
     "pasangan yang ingin bangun pelan dengan kopi di teras.")
tipe(4, "graded/pilih__vip-standard-bungalow__04-teras-view-laut.jpg", "50% 60%", "02 · VIP Standard Bungalow", "Rumah panggung<br><i class='gold'>di tepi pantai</i>",
     ["Dekat pantai, menghadap view senja", "Beratap rumbia, lebih luas dari Standard", "King bed, area wastafel &amp; gantungan baju", "2 orang, maks. 3 dengan 1 extra bed (berbayar)"],
     "pencinta suasana rumah panggung yang ingin ruang lebih lega.")
tipe(5, "graded/pilih__superior-bungalow__04-kamar-loteng.jpg", "50% 50%", "03 · Superior Bungalow", "Rumah kayu di antara<br><i class='gold'>pohon kelapa</i>",
     ["Dekat pantai, menghadap view senja", "A-frame berloteng, king bed, TV", "Kamar mandi semi-outdoor dengan rain shower", "2 orang, maks. 3 dengan 1 extra bed (berbayar)"],
     "kamu yang suka suasana rumah kayu yang hangat &amp; lega.")
tipe(6, "graded/pilih__vip-superior-bungalow__06-bathtub-semi-outdoor.jpg", "50% 55%", "04 · VIP Superior Bungalow", "Berendam di bawah<br><i class='gold'>langit terbuka</i>",
     ["Dekat pantai, menghadap view senja", "Bathtub di kamar mandi semi-outdoor beratap kaca", "Air panas &amp; dingin (hanya di tipe ini)", "King bed, TV, mini bar, loteng"],
     "perayaan kecil atau liburan yang terasa istimewa.")
tipe(7, "graded/pilih__family-superior-bungalow__01-eksterior-taman.jpg", "55% 50%", "05 · Family Superior Bungalow", "Satu rumah,<br>dua lantai,<br><i class='gold'>semua bersama</i>",
     ["Dekat pantai, menghadap view senja", "Bungalow terbesar: normal 6 orang, maks. 8", "Kamar mandi di kedua lantai", "Teras atau balkon pribadi"],
     "keluarga besar atau rombongan teman.")

# 8 yang sama di semua tipe --------------------------------------------------
inc = ["Sarapan", "AC &amp; Wi-Fi", "Set kopi/teh &amp; pemanas air", "Meja kerja/rias", "Tirai blackout", "Bantal &amp; selimut tambahan", "Setrika (atas permintaan)"]
def inc_li(items):
    return "".join(f'<div style="display:flex;align-items:center;padding:21px 0;border-bottom:1px solid rgba(166,124,100,.45);font-size:27px;color:#5A3E31"><span class="sun"></span>{i}</div>' for i in items)
T.append(f'''<div class="t" id="pilih-08">
  <img class="logo" src="{LOGO_D}" alt="">
  <div style="position:absolute;left:72px;right:72px;top:205px">
    <div class="caps" style="font-size:20px;color:#E07A4B">Yang sama di semua tipe</div>
    <div class="pf" style="font-size:66px;line-height:1.05;margin-top:12px;color:#5A3E31">Apa pun pilihanmu,<br><i style="color:#A67C64">ini sudah termasuk</i></div>
    <img src="{P}graded/pilih__family-superior-bungalow__10-lantai-atas-kasur-kettle.jpg" style="display:block;width:936px;height:420px;object-fit:cover;object-position:50% 55%;margin-top:30px" alt="">
    <div style="display:grid;grid-template-columns:1fr 1fr;column-gap:44px;margin-top:10px;border-top:1px solid rgba(166,124,100,.45)">
      <div>{inc_li(inc[:4])}</div><div>{inc_li(inc[4:] + ["Teras pribadi &amp; kursi santai"])}</div></div></div>
  {foot(8)}</div>''')

# 9 cara cepat memilih --------------------------------------------------------
rows9 = [("Berdua, santai &amp; hangat", "Standard<br>atau VIP Standard"),
         ("Berdua, suka loteng &amp; suasana kayu", "Superior"),
         ("Momen istimewa", "VIP Superior"),
         ("Keluarga atau rombongan, sampai 8 orang", "Family Superior")]
T.append(f'''<div class="t" id="pilih-09">
  <img class="logo" src="{LOGO_D}" alt="">
  <div style="position:absolute;left:72px;right:72px;top:215px">
    <div class="caps" style="font-size:20px;color:#E07A4B">Cara cepat memilih</div>
    <div class="pf" style="font-size:96px;line-height:1.02;margin-top:14px;color:#5A3E31">Masih bingung?<br><i style="color:#A67C64">Ikuti ini</i></div>
    <div style="margin-top:40px;border-top:1px solid rgba(166,124,100,.45)">{"".join(f'<div class="row" style="padding:42px 0"><span class="a">{a}</span><span class="b">{b}</span></div>' for a, b in rows9)}</div>
    <div style="margin-top:34px;font-size:27px;line-height:1.55;color:#5A3E31"><span class="sun"></span>Bertiga? Semua tipe berkapasitas 2 orang bisa menambah 1 extra bed (berbayar).</div></div>
  {foot(9)}</div>''')

# 10 CTA ----------------------------------------------------------------------
T.append(f'''<div class="t" id="pilih-10"><img class="bg" src="{P}graded/pilih__senja__11-kayak-dan-pulau.jpg" style="object-position:55% 50%" alt="">
  <div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(40,24,14,.6) 0%,rgba(40,24,14,.25) 34%,rgba(40,24,14,.3) 60%,rgba(40,24,14,.8) 100%)"></div>
  <img class="logo" src="{LOGO_L}" alt="">
  <div class="sh" style="position:absolute;left:72px;right:72px;top:205px;color:#FBF4EC">
    <div class="caps" style="font-size:21px;color:#FDB15D">Sampai jumpa di Selayar</div>
    <div class="pf" style="font-size:112px;line-height:1.02;margin-top:14px;letter-spacing:-.01em">Sudah ketemu<br><i class="gold">pilihanmu?</i></div></div>
  <div class="sh" style="position:absolute;left:72px;right:72px;bottom:130px;max-width:600px;color:#FBF4EC;font-size:31px;line-height:1.5">
    <div>Simpan dulu, biar liburanmu tinggal berangkat.</div>
    <div style="margin-top:10px">Tag orang yang mau kamu ajak ke Selayar.</div>
    <div class="pill" style="text-shadow:none;margin-top:30px;font-size:27px"><b style="display:block;margin:0 0 8px">Biar kami bantu</b><span style="white-space:nowrap">WhatsApp {WA}</span></div>
    <div class="pf it" style="font-size:30px;margin-top:30px;color:#FDB15D">Where every day ends beautifully.</div></div>
  {foot(10, True)}</div>''')

(H / "pilih_bungalow.html").write_text(f'<!doctype html><html lang="id"><head><meta charset="utf-8">{FONTS}<style>{CSS}</style></head><body>{"".join(T)}</body></html>', encoding="utf-8")
print(len(T), "slide")
