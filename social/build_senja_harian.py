"""Story harian "Senja Hari Ini" 22 Nov – 31 Des 2026 (1 gambar per hari, 1080x1920).
Jam terbenam dihitung astronomis untuk Pantai Sunari (6.13°LS, 120.47°BT, WITA).
Run: python3 social/build_senja_harian.py && node social/render_senja_harian.js -> social/senja-harian/senja-YYYY-MM-DD.png"""
import pathlib, math, datetime as dt
H = pathlib.Path(__file__).parent
TAG = "#sunarisunsetmoment"; WA = "0821-8903-3044"
LOGO = "../assets/logo-sunari-color-dark.png"; P = "../assets/photos/"
LAT, LON = -6.13, 120.47
def sunset_min(d):
    g = 2 * math.pi / 365 * (d.timetuple().tm_yday - 1)
    eot = 229.18 * (0.000075 + 0.001868 * math.cos(g) - 0.032077 * math.sin(g) - 0.014615 * math.cos(2 * g) - 0.040849 * math.sin(2 * g))
    dec = 0.006918 - 0.399912 * math.cos(g) + 0.070257 * math.sin(g) - 0.006758 * math.cos(2 * g) + 0.000907 * math.sin(2 * g) - 0.002697 * math.cos(3 * g) + 0.00148 * math.sin(3 * g)
    ha = math.degrees(math.acos(math.cos(math.radians(90.833)) / (math.cos(math.radians(LAT)) * math.cos(dec)) - math.tan(math.radians(LAT)) * math.tan(dec)))
    return round(720 - 4 * (LON - ha) - eot + 480)
hm = lambda m: f"{m // 60:02d}.{m % 60:02d}"
HARI = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]
BULAN = ["", "Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
SPECIAL = {dt.date(2026, 12, 25): "Selamat Hari Natal", dt.date(2026, 12, 31): "Senja terakhir 2026"}
PHOTOS = [("senja/12-kayak-matahari-merah-story.jpg", "50% 45%"), ("senja/35-matahari-cakrawala-1751.jpg", "50% 45%"), ("senja/47-payung-di-antara-kelapa-1755.jpg", "50% 45%"), ("senja/51-kayak-double-jalur-cahaya-1751.jpg", "50% 45%"), ("aktivitas/07-ayunan-gaun-merah-tengah.jpg", "50% 45%"), ("senja/50-meja-dua-gelas-bawah-daun-1752.jpg", "50% 45%"), ("senja/45-dua-kayak-matahari-1751.jpg", "50% 45%"), ("senja/34-pasangan-selfie-bawah-daun.jpg", "50% 45%"), ("senja/52-pohon-kelapa-bungalow-1747.jpg", "50% 45%"), ("senja/42-teras-bingkai-daun-1744.jpg", "50% 45%"), ("senja/39-kayak-single-samping-1753.jpg", "50% 45%"), ("senja/49-tamu-angkat-tangan-1756.jpg", "50% 45%"), ("senja/29-dua-kursi-menghadap-senja.jpg", "50% 45%"), ("senja/22-ranting-dan-matahari.jpg", "50% 45%"), ("senja/24-pohon-tepi-pantai-senja.jpg", "50% 45%"), ("senja/37-afterglow-kayak-pelampung-1814.jpg", "50% 45%"), ("senja/09-kayak-pasangan.jpg", "50% 45%"), ("senja/15-dua-kayak-oranye.jpg", "50% 45%"), ("senja/05-tamu-di-meja.jpg", "50% 45%"), ("senja/32-payung-lampu-senja-1751.jpg", "50% 45%"), ("senja/27-tamu-dan-pohon-kelapa.jpg", "50% 45%"), ("senja/06-di-bawah-daun.jpg", "50% 45%"), ("aktivitas/05-ayunan-raksasa-senja.jpg", "50% 45%"), ("senja/10-kayak-pantulan.jpg", "50% 45%"), ("senja/48-tamu-dan-drone-1758.jpg", "50% 45%"), ("senja/17-kayak-berdua.jpg", "50% 45%"), ("senja/33-payung-kelapa-senja-1749.jpg", "50% 45%"), ("senja/28-matahari-di-bawah-daun.jpg", "50% 45%"), ("senja/40-kayak-single-belakang-a-1753.jpg", "50% 45%"), ("senja/44-dua-kayak-emas-1743.jpg", "50% 45%"), ("senja/36-jalan-setapak-taman-golden.jpg", "50% 45%"), ("senja/14-daun-matahari-story.jpg", "50% 45%"), ("senja/11-kayak-dan-pulau.jpg", "50% 45%"), ("senja/38-blue-hour-kayak-1815.jpg", "50% 45%"), ("senja/30-matahari-merah-dan-daun.jpg", "50% 45%"), ("senja/19-pantai-di-bawah-daun.jpg", "50% 45%"), ("senja/08-meja-di-bawah-pohon.jpg", "50% 45%"), ("senja/18-kayak-berdua-pelampung.jpg", "50% 45%"), ("senja/13-tamu-bertopi-story.jpg", "50% 45%"), ("senja/21-siluet-tamu-tepi-pantai.jpg", "50% 45%")]
assert len(PHOTOS) == len(set(PHOTOS))  # tidak ada foto berulang
FONTS = '<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;0,600;1,400;1,500&family=Montserrat:wght@400;500;600;700;800&display=swap" rel="stylesheet">'
CSS = """
*{margin:0;padding:0;box-sizing:border-box}
body{background:#bbb;font-family:Montserrat,sans-serif}
.s{position:relative;overflow:hidden;width:1080px;height:1920px;margin:30px auto;background:#1d140e}
.bg{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.veil{position:absolute;inset:0;background:linear-gradient(180deg,rgba(15,8,4,.55) 0%,rgba(15,8,4,.15) 30%,rgba(15,8,4,0) 45%,rgba(15,8,4,.25) 60%,rgba(15,8,4,.6) 100%)}
.sh{color:#FBF4EC;text-shadow:0 3px 18px rgba(0,0,0,.6),0 1px 3px rgba(0,0,0,.55)}
.top{position:absolute;left:64px;right:64px;top:150px;display:flex;align-items:center;justify-content:space-between}
.pill{font-weight:800;font-size:20px;letter-spacing:.24em;text-transform:uppercase;color:#FBF4EC;background:rgba(15,8,4,.45);border:1px solid rgba(251,244,236,.35);padding:12px 20px;border-radius:999px}
.today{font-family:'Playfair Display',serif;font-weight:600;font-size:112px;line-height:1;letter-spacing:.01em;color:#FBF4EC}
.today i{font-style:italic;font-weight:500;color:#FDB15D}
.date{font-weight:800;font-size:26px;letter-spacing:.2em;text-transform:uppercase;color:#FDB15D}
.big{font-family:'Playfair Display',serif;font-weight:600;font-size:240px;line-height:.95;letter-spacing:-.01em}
.unit{font-weight:700;font-size:28px;letter-spacing:.2em;text-transform:uppercase}
.badge{display:inline-block;margin-top:18px;font-weight:800;font-size:21px;letter-spacing:.18em;text-transform:uppercase;color:#fff;background:linear-gradient(90deg,#FDB15D,#FF8A5C);padding:10px 20px;border-radius:999px;text-shadow:none}
.card{position:absolute;left:48px;right:48px;bottom:250px;background:rgba(251,244,236,.95);border-radius:36px;padding:26px 40px 22px;box-shadow:0 20px 50px rgba(0,0,0,.35)}
.row{display:flex;align-items:center;gap:26px;padding:13px 0;border-bottom:1.5px solid rgba(138,95,72,.2)}
.row:last-of-type{border-bottom:none}
.row .t{font-family:'Playfair Display',serif;font-weight:600;font-size:52px;color:#C0592C;width:250px;flex:none;line-height:1;text-shadow:0 1.5px 0 #fff,0 2px 3px rgba(90,62,49,.25)}
.row .t.hi{font-size:62px;color:#A84A24}
.row .l b{display:block;font-weight:800;font-size:26px;color:#3B2819}
.row .l span{font-size:21px;color:#6B4C3B}
.ft{display:flex;justify-content:space-between;margin-top:14px;padding-top:14px;border-top:1.5px solid rgba(138,95,72,.3);font-weight:800;font-size:17px;letter-spacing:.2em;text-transform:uppercase;color:#7A5039}
"""
START, END = dt.date(2026, 11, 22), dt.date(2026, 12, 31)
T = []
for i in range((END - START).days + 1):
    d = START + dt.timedelta(i); ss = sunset_min(d)
    img, pos = PHOTOS[i % len(PHOTOS)]
    badge = SPECIAL.get(d) or ("Akhir pekan" if d.weekday() >= 5 else "")
    rows = [(hm(ss - 40), "Golden hour dimulai", "Cahaya keemasan, terbaik untuk foto potret", False),
            (hm(ss - 30), "Waktunya ke pantai", "Pilih spot, sewa kayak, siapkan kamera", False),
            (hm(ss - 4), "Matahari menyentuh laut", "Siluet & jalur cahaya paling cantik", False),
            (hm(ss), "Matahari terbenam", "Tenggelam penuh di balik cakrawala", True),
            (f"{hm(ss + 1)}–{hm(ss + 20)}", "Afterglow", "Langit jingga, merah muda & ungu", False)]
    rows_html = "".join(f'<div class="row"><div class="t{" hi" if h else ""}" style="{"font-size:40px" if "–" in t else ""}">{t}</div><div class="l"><b>{a}</b><span>{b}</span></div></div>' for t, a, b, h in rows)
    T.append(f'''<div class="s" id="senja-{d.isoformat()}"><img class="bg" src="{P}{img}" style="object-position:{pos}" alt=""><div class="veil"></div>
  <div class="top"><img src="{LOGO}" style="width:250px;filter:drop-shadow(0 2px 8px rgba(0,0,0,.5))" alt=""><span class="pill">Pantai Sunari</span></div>
  <div class="sh" style="position:absolute;left:64px;right:64px;top:300px">
    <div class="today">Sunset <i>Today</i></div>
    <div class="date" style="margin-top:14px">{HARI[d.weekday()]} · {d.day} {BULAN[d.month]} {d.year}</div>
    <div class="big" style="margin-top:0">{hm(ss)}</div>
    <div class="unit" style="margin-top:22px">WITA · Matahari terbenam di Pantai Sunari</div>
    {f'<div class="badge">{badge}</div>' if badge else ''}</div>
  <div class="card">{rows_html}<div class="ft"><span>Pantai Sunari · Selayar</span><span>{TAG}</span></div></div></div>''')
(H / "senja_harian.html").write_text(f'<!doctype html><html lang="id"><head><meta charset="utf-8">{FONTS}<style>{CSS}</style></head><body>{"".join(T)}</body></html>')
print(len(T), "story")
