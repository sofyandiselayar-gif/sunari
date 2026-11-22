"""Kalender Senja harian 22 Nov – 31 Des 2026 (Pantai Sunari, WITA).
Jam terbenam dihitung astronomis (6.13°LS, 120.47°BT), dibulatkan ke menit; cocok dengan foto ber-jam resort (Jun–Sep).
Run: python3 social/build_kalender_harian.py && node social/render_kalender_harian.js"""
import pathlib, math, datetime as dt
H = pathlib.Path(__file__).parent
WA = "0821-8903-3044"; IG = "@sunaribeachresortselayar"; TAG = "#sunarisunsetmoment"
LOGO = "../assets/logo-sunari-color.png"
LAT, LON = -6.13, 120.47
def sunset(d):
    g = 2 * math.pi / 365 * (d.timetuple().tm_yday - 1)
    eot = 229.18 * (0.000075 + 0.001868 * math.cos(g) - 0.032077 * math.sin(g) - 0.014615 * math.cos(2 * g) - 0.040849 * math.sin(2 * g))
    dec = 0.006918 - 0.399912 * math.cos(g) + 0.070257 * math.sin(g) - 0.006758 * math.cos(2 * g) + 0.000907 * math.sin(2 * g) - 0.002697 * math.cos(3 * g) + 0.00148 * math.sin(3 * g)
    ha = math.degrees(math.acos(math.cos(math.radians(90.833)) / (math.cos(math.radians(LAT)) * math.cos(dec)) - math.tan(math.radians(LAT)) * math.tan(dec)))
    m = round(720 - 4 * (LON - ha) - eot + 480)
    return f"{m // 60:02d}.{m % 60:02d}"
START, END = dt.date(2026, 11, 22), dt.date(2026, 12, 31)
DAYS = [START + dt.timedelta(i) for i in range((END - START).days + 1)]
HARI = ["Sen", "Sel", "Rab", "Kam", "Jum", "Sab", "Min"]
SPECIAL = {dt.date(2026, 11, 22): "Hari ini", dt.date(2026, 12, 25): "Natal", dt.date(2026, 12, 31): "Senja terakhir 2026"}

FONTS = '<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;1,400;1,500&family=Montserrat:wght@400;500;600;700&display=swap" rel="stylesheet">'
CSS = """
*{margin:0;padding:0;box-sizing:border-box}
body{background:#bbb;font-family:Montserrat,sans-serif;color:#3B2819}
.t{position:relative;overflow:hidden;margin:30px auto;width:1080px;background:#FBF4EC}
.f{height:1350px}.s{height:1920px}
.top{position:absolute;left:64px;right:64px;display:flex;align-items:center;justify-content:space-between}
.top img{width:230px}
.caps{font-weight:700;text-transform:uppercase;letter-spacing:.24em;color:#7A5039}
.pf{font-family:'Playfair Display',serif;font-weight:500}
.it{font-style:italic;color:#9A6A4F}
.wk{display:grid;grid-template-columns:repeat(7,1fr);gap:10px}
.wk .hd{text-align:center;font-weight:700;font-size:17px;letter-spacing:.18em;text-transform:uppercase;color:#9A8478;padding-bottom:4px}
.c{border-radius:18px;background:#FFFDF9;text-align:center;box-shadow:0 6px 16px rgba(90,62,49,.08);position:relative}
.c.e{background:transparent;box-shadow:none}
.c .d{font-weight:700;color:#7A5039}
.c .tm{font-family:'Playfair Display',serif;font-weight:500;color:#E07A4B;line-height:1}
.c.sp{background:linear-gradient(180deg,#FDB15D,#FF8A5C)}
.c.sp .d,.c.sp .tm,.c.sp .lb{color:#fff}
.c .lb{font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:#C0592C}
.ft{position:absolute;left:64px;right:64px;display:flex;justify-content:space-between;font-weight:700;font-size:17px;letter-spacing:.22em;text-transform:uppercase;color:#7A5039;padding-top:16px;border-top:1.5px solid rgba(138,95,72,.35)}
.note{font-size:22px;line-height:1.5;color:#5A3E31}
"""
def grid(days, size):
    cell_h, dsz, tsz, lsz = size
    first = days[0]
    cells = [f'<div class="hd">{h}</div>' for h in HARI]
    cells += ['<div class="c e"></div>'] * first.weekday()
    for d in days:
        sp = d in SPECIAL
        lb = f'<div class="lb" style="font-size:{lsz}px;margin-top:4px">{SPECIAL[d]}</div>' if sp else ""
        cells.append(f'<div class="c{" sp" if sp else ""}" style="height:{cell_h}px;padding-top:{12 if not sp else 10}px">'
                     f'<div class="d" style="font-size:{dsz}px">{d.day}</div><div class="tm" style="font-size:{tsz}px;margin-top:6px">{sunset(d)}</div>{lb}</div>')
    return '<div class="wk">' + "".join(cells) + "</div>"

def grid3(days, size):
    cell_h, dsz, tsz, lsz = size
    out = []
    for d in days:
        sp = d in SPECIAL
        lb = f'<div class="lb" style="font-size:{lsz}px;margin-top:6px">{SPECIAL[d]}</div>' if sp else ""
        out.append(f'<div class="c{" sp" if sp else ""}" style="height:{cell_h}px;padding-top:22px">'
                   f'<div class="d" style="font-size:{dsz}px;letter-spacing:.12em;text-transform:uppercase">{HARI[d.weekday()]} · {d.day} Nov</div>'
                   f'<div class="tm" style="font-size:{tsz}px;margin-top:10px">{sunset(d)}</div>{lb}</div>')
    return '<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:16px">' + "".join(out) + "</div>"

def page(pid, fmt, title, sub, days, size, top, foot_bottom, extra="", g=None):
    T.append(f'''<div class="t {fmt}" id="{pid}">
  <div class="top" style="top:{top}px"><img src="{LOGO}" alt=""><span class="caps" style="font-size:19px">Kalender senja harian</span></div>
  <div style="position:absolute;left:64px;right:64px;top:{top + 110}px;bottom:{foot_bottom + 70}px;display:flex;flex-direction:column;justify-content:center">
    <div class="pf" style="font-size:{64 if fmt == 'f' else 74}px;line-height:1.05">{title}</div>
    <div class="note" style="margin-top:10px">{sub}</div>
    <div style="margin-top:26px">{(g or grid)(days, size)}</div>{extra}</div>
  <div class="ft" style="bottom:{foot_bottom}px"><span>Pantai Sunari · WITA</span><span>{TAG}</span></div></div>''')

T = []
nov = [dt.date(2026, 11, i) for i in range(1, 31)]; des = [d for d in DAYS if d.month == 12]
SUBN = "Jam matahari menyentuh laut di depan Pantai Sunari. Datang ke pantai <b>30 menit sebelumnya</b>."
SUBD = "Senja makin sore menjelang akhir tahun. Tutup 2026 dengan senja terakhir di Pantai Sunari."
legend = lambda fs: f'''<div class="note" style="font-size:{fs}px;margin-top:22px">Golden hour ±40 menit sebelumnya · afterglow ±20 menit sesudahnya · jam dapat bergeser ±2 menit karena cuaca.</div>'''
page("kalender-harian-nov", "f", 'November <span class="it">2026</span>', SUBN, nov, (118, 22, 42, 12), 56, 50, legend(21))
page("kalender-harian-des", "f", 'Desember <span class="it">2026</span>', SUBD, des, (140, 24, 46, 13), 56, 50, legend(21))
page("story-kalender-harian-nov", "s", 'Senja <span class="it">November</span>', SUBN, nov, (168, 26, 50, 14), 140, 240, legend(25))
page("story-kalender-harian-des", "s", 'Senja <span class="it">Desember</span>', SUBD, des, (200, 28, 50, 15), 140, 240, legend(25))
(H / "kalender_harian.html").write_text(f'<!doctype html><html lang="id"><head><meta charset="utf-8">{FONTS}<style>{CSS}</style></head><body>{"".join(T)}</body></html>')
print(len(T), "desain")
for d in DAYS: print(d.isoformat(), HARI[d.weekday()], sunset(d))
