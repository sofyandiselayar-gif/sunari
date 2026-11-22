"""Carousel "Tips Kano/Kayak Saat Senja" (20 slide, 1080x1350).
Beberapa foto berkualitas tinggi dipakai untuk 2 slide:
  - panorama: foto persegi 2252 px dibentang di 2 slide berurutan (geser = gambar menyambung)
  - dua potongan: foto potret 1351x2400 dipotong atas & bawah
Run: python3 social/build_kayak.py && node social/render_kayak.js  -> social/kayak-tips/*.png"""
import pathlib
H = pathlib.Path(__file__).parent
WA = "0821-8903-3044"; IG = "@sunaribeachresortselayar"
LOGO = "../assets/logo-sunari-color.png"; LOGO_D = "../assets/logo-sunari-color-dark.png"; P = "../assets/photos/"
N = 20
FONTS = '<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;1,400;1,500&family=Montserrat:wght@400;500;600;700&display=swap" rel="stylesheet">'
CSS = """
*{margin:0;padding:0;box-sizing:border-box}
body{background:#bbb;font-family:Montserrat,sans-serif;color:#3B2819}
.t{position:relative;overflow:hidden;margin:30px auto;width:1080px;height:1350px;background:#1d140e}
.bg{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.pano{position:absolute;top:0;width:2160px;height:1350px;object-fit:cover}
.logo{position:absolute;left:60px;top:54px;width:230px;filter:drop-shadow(0 2px 8px rgba(0,0,0,.5))}
.pg{position:absolute;right:60px;top:70px;font-weight:700;font-size:19px;letter-spacing:.24em;color:#FBF4EC;background:rgba(20,12,8,.45);padding:10px 18px;border-radius:999px}
.ph{position:absolute;left:0;top:0;width:1080px;height:780px;overflow:hidden}
.ph img{position:absolute;top:0;height:780px;object-fit:cover}
.panel{position:absolute;left:0;right:0;top:780px;bottom:0;background:#FBF4EC;padding:34px 64px 0}
.panel .ft{position:absolute;left:64px;right:64px;bottom:34px}
.card{position:absolute;left:48px;right:48px;bottom:48px;background:rgba(251,244,236,.96);border-radius:38px;padding:36px 44px 32px;box-shadow:0 24px 60px rgba(0,0,0,.35)}
.eb{display:flex;align-items:center;gap:14px;font-weight:700;font-size:19px;letter-spacing:.24em;text-transform:uppercase;color:#7A5039}
.no{width:46px;height:46px;border-radius:50%;display:inline-flex;align-items:center;justify-content:center;color:#fff;font-family:'Playfair Display',serif;font-size:24px;letter-spacing:0;background:linear-gradient(180deg,#FDB15D,#FF8A5C)}
.h{font-family:'Playfair Display',serif;font-weight:500;font-size:58px;line-height:1.08;margin-top:10px}
.h i{color:#9A6A4F}
.p{font-size:28px;line-height:1.5;margin-top:12px;color:#3B2819}
ul.k{list-style:none;margin-top:10px}
ul.k li{display:flex;gap:16px;padding:10px 0;border-top:1.5px solid rgba(138,95,72,.2);font-size:29px;line-height:1.38}
ul.k li:first-child{border-top:none}
ul.k li i{flex:none;font-style:normal;color:#E07A4B;font-weight:700}
.time{font-family:'Playfair Display',serif;font-weight:500;color:#E07A4B;line-height:1}
.sh{text-shadow:0 2px 14px rgba(0,0,0,.6),0 1px 3px rgba(0,0,0,.45)}
.gold{color:#FDB15D}
.ft{display:flex;justify-content:space-between;margin-top:16px;padding-top:14px;border-top:1.5px solid rgba(138,95,72,.25);font-weight:700;font-size:16px;letter-spacing:.22em;text-transform:uppercase;color:#7A5039}
"""
T = []
def bgimg(img, pos="50% 50%", pano=None):
    if pano is None:
        return f'<img class="bg" src="{P}{img}" style="object-position:{pos}" alt="">'
    return f'<img class="pano" src="{P}{img}" style="left:{-1080 * pano}px;object-position:{pos}" alt="">'
def slide(n, img, pos, eyebrow, title, body, pano=None, num=None, pill=""):
    no = f'<span class="no">{num}</span>' if num else ''
    w, left = (2160, -1080 * pano) if pano is not None else (1080, 0)
    T.append(f'''<div class="t" id="kayak-{n:02d}" style="background:#FBF4EC">
  <div class="ph"><img src="{P}{img}" style="left:{left}px;width:{w}px;object-position:{pos}" alt=""></div>
  <img class="logo" src="{LOGO_D}" alt=""><div class="pg" style="{pill}">{n:02d} / {N}</div>
  <div class="panel"><div class="eb">{no}{eyebrow}</div><div class="h">{title}</div>{body}
    <div class="ft"><span>SunaRi · Pantai Sunari</span><span>{"Geser →" if n < N else IG}</span></div></div></div>''')
ul = lambda items: '<ul class="k">' + "".join(f"<li><i>—</i><span>{x}</span></li>" for x in items) + "</ul>"

# 01 cover
T.append(f'''<div class="t" id="kayak-01">{bgimg("senja/18-kayak-berdua-pelampung.jpg", "50% 60%")}
  <div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,.45) 0%,rgba(0,0,0,0) 32%,rgba(0,0,0,0) 60%,rgba(0,0,0,.55) 100%)"></div>
  <img class="logo" src="{LOGO_D}" alt=""><div class="pg">01 / {N}</div>
  <div class="sh" style="position:absolute;left:64px;right:64px;top:200px;color:#FBF4EC">
    <div style="font-weight:700;font-size:22px;letter-spacing:.28em;text-transform:uppercase;color:#FDB15D">Tips kano &amp; kayak saat senja</div>
    <div style="font-family:'Playfair Display',serif;font-weight:500;font-size:92px;line-height:1.02;margin-top:14px">Mendayung<br><i class="gold">menyongsong senja.</i></div></div>
  <div class="sh" style="position:absolute;left:64px;right:64px;bottom:70px;color:#FBF4EC">
    <div style="font-size:30px;line-height:1.45">20 tips aman, nyaman &amp; tetap dapat foto terbaik di Pantai Sunari.</div>
    <div style="font-weight:700;font-size:20px;letter-spacing:.24em;text-transform:uppercase;margin-top:18px">Simpan &amp; geser →</div></div></div>''')

# 02-03 panorama (senja/09)
slide(2, "senja/09-kayak-pasangan.jpg", "50% 52%", "Kenapa saat senja?", 'Air paling tenang, <i>cahaya paling hangat</i>',
      ul(["Laut di depan Pantai Sunari tenang &amp; landai, cocok untuk pemula.", "Matahari terbenam tepat di depan pantai, jadi kamu mendayung <b>ke arah senja</b>.", "Cahaya keemasan membuat setiap foto jadi siluet cantik."]), pano=0)
slide(3, "senja/09-kayak-pasangan.jpg", "50% 52%", "Pilih kayakmu", 'Single atau <i>double?</i>',
      f'''<div style="display:grid;grid-template-columns:1fr 1fr;gap:18px;margin-top:18px">
        <div style="background:#FFFDF9;border-radius:24px;padding:22px 24px"><div class="eb" style="font-size:16px">Single · 1 orang</div><div class="time" style="font-size:68px;margin-top:10px">Rp 50.000</div><div class="p" style="font-size:25px;margin-top:8px">Bebas mengatur arah &amp; ritme sendiri.</div></div>
        <div style="background:#FFFDF9;border-radius:24px;padding:22px 24px"><div class="eb" style="font-size:16px">Double · 2 orang</div><div class="time" style="font-size:68px;margin-top:10px">Rp 100.000</div><div class="p" style="font-size:25px;margin-top:8px">Cocok untuk pasangan, sahabat, atau orang tua + anak.</div></div></div>''', pano=1)

# 04 jam
slide(4, "senja/35-matahari-cakrawala-1751.jpg", "50% 62%", "Jam terbaik", 'Mulai <i>pukul 17.00</i>',
      '''<div style="display:flex;gap:44px;margin-top:22px">
        <div><div class="time" style="font-size:88px">17.00</div><div class="p" style="font-size:24px;margin-top:6px">Turun ke air</div></div>
        <div><div class="time" style="font-size:88px">17.50</div><div class="p" style="font-size:24px;margin-top:6px">Matahari terbenam</div></div>
        <div><div class="time" style="font-size:88px">18.10</div><div class="p" style="font-size:24px;margin-top:6px">Sudah di pantai</div></div></div>
      <div class="p" style="font-size:27px;margin-top:22px">Cek jam senja tiap bulan di <b>Kalender Senja</b> kami.</div>''', num=1)

# 05 pelampung
slide(5, "senja/37-afterglow-kayak-pelampung-1814.jpg", "50% 69%", "Keselamatan", 'Pakai <i>pelampung</i>, selalu',
      ul(["Kenakan life jacket <b>sebelum</b> naik kayak, walau air terlihat dangkal.", "Kencangkan semua tali &amp; gesper sampai pas di badan.", "Berlaku juga untuk yang mahir berenang."]), num=2)

# 06-07 panorama (aktivitas/01)
slide(6, "aktivitas/01-kayak-sore.jpg", "50% 84%", "Naik kayak", 'Mulai dari air <i>setinggi lutut</i>',
      ul(["Dorong kayak sampai mengapung, jangan naik di atas pasir.", "Duduk dulu di tengah, lalu angkat kedua kaki masuk.", "Jaga badan tetap rendah agar kayak stabil."]), pano=0, num=3)
slide(7, "aktivitas/01-kayak-sore.jpg", "50% 84%", "Memegang dayung", 'Tangan <i>selebar bahu</i>',
      ul(["Genggam gagang dayung dengan jarak kedua tangan sedikit lebih lebar dari bahu.", "Bilah dayung tegak, bagian cekung menghadap ke arahmu.", "Genggam rileks, jangan terlalu kencang supaya tidak cepat pegal."]), pano=1, num=4)

# 08-09
slide(8, "senja/12-kayak-matahari-merah-story.jpg", "50% 57%", "Teknik dasar", 'Dayung kiri, <i>dayung kanan</i>',
      ul(["Celupkan bilah dekat kaki, tarik ke belakang sampai pinggul.", "Bergantian kiri &amp; kanan dengan ritme pelan dan teratur.", "Putar badan sedikit, jangan hanya mengandalkan lengan."]), num=5)
slide(9, "senja/41-kayak-single-belakang-b-1753.jpg", "50% 62%", "Belok &amp; berhenti", 'Kendalikan arah <i>dengan tenang</i>',
      ul(["<b>Belok kanan:</b> dayung lebih sering atau lebih lebar di sisi kiri, dan sebaliknya.", "<b>Mundur/rem:</b> celupkan dayung di samping pinggul lalu dorong ke depan.", "Latih dulu di dekat pantai sebelum mendayung lebih jauh."]), num=6)

# 10-11 panorama (senja/11)
slide(10, "senja/11-kayak-dan-pulau.jpg", "50% 100%", "Mendayung berdua", 'Satu kayak, <i>satu ritme</i>',
      ul(["Yang di <b>depan</b> menentukan ritme dayungan.", "Yang di <b>belakang</b> mengikuti ritme &amp; mengarahkan kayak.", "Sepakati aba-aba sederhana: \"kiri\", \"kanan\", \"stop\"."]), num=7)
slide(11, "senja/51-kayak-double-jalur-cahaya-1751.jpg", "50% 58%", "Arah &amp; jarak", 'Tetap di <i>depan resort</i>',
      ul(["Mendayung sejajar pantai, di area yang masih terlihat dari bibir pantai.", "Pulau Gusung di seberang terlihat dekat, tapi <b>bukan</b> tujuan kayak sore.", "Tanyakan batas area aman ke staf sebelum berangkat."]), num=8)

# 12 surut
slide(12, "senja/52-pohon-kelapa-bungalow-1747.jpg", "50% 56%", "Pasang-surut", 'Perhatikan <i>air surut</i>',
      ul(["Saat surut, karang &amp; lamun muncul dekat permukaan.", "Jangan menyeret kayak atau berdiri di atas karang: melukai kaki &amp; merusak terumbu.", "Pilih jalur air yang lebih dalam, atau tunggu air pasang."]), num=9)

# 13-14 dua potongan (senja/45)
slide(13, "senja/44-dua-kayak-emas-1743.jpg", "50% 60%", "Lindungi mata &amp; kulit", 'Jangan menatap <i>matahari langsung</i>',
      ul(["Pakai kacamata hitam &amp; topi, pantulan air menambah silau.", "Oleskan tabir surya ramah karang sebelum turun ke air.", "Minum air putih sebelum &amp; sesudah mendayung."]), num=10)
slide(14, "senja/02b-pantai-kayak-di-pasir-balanced.jpg", "50% 52%", "Yang perlu dibawa", 'Bekal <i>secukupnya</i>',
      ul(["Ponsel di <b>pouch tahan air</b> dengan tali leher.", "Baju yang boleh basah &amp; sandal air.", "Tinggalkan dompet &amp; barang berharga di kamar."]), num=11)

# 15-16 foto
slide(15, "senja/39-kayak-single-samping-1753.jpg", "50% 58%", "Foto dari kayak", 'Aman dulu, <i>baru foto</i>',
      ul(["Berhenti mendayung &amp; letakkan dayung melintang di pangkuan sebelum memotret.", "Ikat ponsel ke pergelangan atau leher.", "Turunkan exposure di layar supaya langit jingga tidak pucat."]), num=12)
slide(16, "senja/15-dua-kayak-oranye.jpg", "50% 36%", "Foto siluet terbaik", 'Diambil <i>dari bibir pantai</i>',
      ul(["Minta teman memotret dari pantai, sejajar jalur cahaya matahari.", "Pose favorit: dayung terangkat ke atas atau membentuk garis miring.", "Jam emasnya: <b>17.30–17.50</b>, saat matahari masih bulat di atas laut."]), num=13, pill="top:auto;bottom:600px")

# 17 anak
slide(17, "senja/17-kayak-berdua.jpg", "50% 69%", "Bersama anak", 'Si kecil ikut <i>mendayung?</i>',
      ul(["Anak wajib memakai pelampung ukuran yang pas.", "Gunakan <b>kayak double</b>: anak di depan, orang dewasa di belakang.", "Tetap di air dangkal &amp; dekat pantai, selalu dalam pengawasan."]), num=14)

# 18 kembali
slide(18, "senja/38-blue-hour-kayak-1815.jpg", "50% 46%", "Waktunya kembali", 'Matahari tenggelam, <i>dayung pulang</i>',
      '''<div style="display:flex;gap:30px;margin-top:16px;align-items:baseline"><div class="time" style="font-size:92px">17.50</div><div class="p" style="margin:0">Matahari menyentuh laut: mulai dayung kembali.</div></div>
      <div style="display:flex;gap:30px;margin-top:10px;align-items:baseline"><div class="time" style="font-size:92px">18.10</div><div class="p" style="margin:0">Kayak sudah di pasir. Nikmati afterglow dari pantai.</div></div>''', num=15)

# 19 cuaca & etika
slide(19, "senja/10-kayak-pantulan.jpg", "50% 100%", "Cuaca &amp; etika", 'Laut yang <i>dihormati</i>',
      ul(["Angin kencang, ombak besar, atau awan gelap? Tunda dulu, senja masih ada besok.", "Beri tahu staf saat berangkat &amp; saat kembali.", "Jangan buang sampah ke laut, bawa kembali semua barangmu."]), num=16)

# 20 CTA
T.append(f'''<div class="t" id="kayak-20">{bgimg("senja/46-dua-kayak-emas-b-1743.jpg", "50% 95%")}
  <div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,.4) 0%,rgba(0,0,0,0) 30%,rgba(0,0,0,0) 45%,rgba(0,0,0,.35) 100%)"></div>
  <img class="logo" src="{LOGO_D}" alt=""><div class="pg">20 / {N}</div>
  <div class="card" style="text-align:center"><div class="eb" style="justify-content:center">Siap mendayung?</div>
    <div class="h" style="font-size:62px">Senja menunggumu <i>di air.</i></div>
    <div style="display:flex;justify-content:center;gap:40px;margin-top:20px">
      <div><div class="eb" style="font-size:16px;justify-content:center">Single</div><div class="time" style="font-size:52px;margin-top:6px">Rp 50.000</div></div>
      <div><div class="eb" style="font-size:16px;justify-content:center">Double</div><div class="time" style="font-size:52px;margin-top:6px">Rp 100.000</div></div></div>
    <div class="p" style="font-size:24px">Sewa di pantai depan resort · tag <b>{IG}</b> &amp; <b>#sunarisunsetmoment</b></div>
    <div style="display:inline-block;margin-top:18px;padding:16px 36px;border-radius:999px;background:linear-gradient(90deg,#FDB15D,#FF8A5C);color:#fff;font-weight:700;font-size:25px">Reservasi · WA {WA}</div></div></div>''')

(H / "kayak.html").write_text(f'<!doctype html><html lang="id"><head><meta charset="utf-8">{FONTS}<style>{CSS}</style></head><body>{"".join(T)}</body></html>')
print(len(T), "slide")

# ================================================================== VERSI STORY (1080x1920)
# Layout sama, tinggi 1920: foto 1080 px di atas, panel di bawah; isi di luar zona tombol IG (atas & bawah ±250 px).
SCSS = CSS + """
.t{height:1920px}
.ph{height:1080px}.ph img{height:1080px}
.panel{top:1080px;padding-top:40px}
.panel .ft{bottom:250px}
.logo{top:150px;width:250px}.pg{top:168px}
.h{font-size:62px}
ul.k li{font-size:31px}
"""
sh = "".join(T)
sh = sh.replace('id="kayak-', 'id="story-kayak-')
sh = sh.replace('style="top:auto;bottom:600px"', 'style="top:auto;bottom:900px"')          # slide 16 pill
sh = sh.replace('position:absolute;left:64px;right:64px;top:200px;color:#FBF4EC', 'position:absolute;left:64px;right:64px;top:360px;color:#FBF4EC')   # cover title
sh = sh.replace('position:absolute;left:64px;right:64px;bottom:70px;color:#FBF4EC', 'position:absolute;left:64px;right:64px;bottom:300px;color:#FBF4EC')  # cover bottom
sh = sh.replace('<div class="card" style="text-align:center">', '<div class="card" style="text-align:center;top:290px;bottom:auto">')  # CTA
(H / "kayak_story.html").write_text(f'<!doctype html><html lang="id"><head><meta charset="utf-8">{FONTS}<style>{SCSS}</style></head><body>{sh}</body></html>')
print(len(T), "story")
