"""Kalender Senja harian 22 Nov – 31 Des 2026 (Pantai Sunari, WITA).
Jam terbenam dihitung astronomis (6.13°LS, 120.47°BT), dibulatkan ke menit; cocok dengan foto ber-jam resort (Jun–Sep).
Run: python3 social/build_kalender_harian.py && node social/render_kalender_harian.js"""
import pathlib, math, datetime as dt
H = pathlib.Path(__file__).parent
WA = "0821-8903-3044"; IG = "@sunaribeachresortselayar"; TAG = "#sunarisunsetmoment"
LOGO = "../assets/logo-sunari-color-dark.png"
P = "../assets/photos/"
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
HOLIDAY = {dt.date(2026, 12, 25): "Natal"}
SPECIAL = {**HOLIDAY, dt.date(2026, 12, 31): "Akhir 2026"}

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
.wk .hd{text-align:center;font-weight:700;font-size:18px;letter-spacing:.18em;text-transform:uppercase;color:#9A8478;padding-bottom:4px}
.c{border-radius:18px;background:#FFFDF9;text-align:center;box-shadow:0 6px 16px rgba(90,62,49,.08);position:relative}
.c.e{background:transparent;box-shadow:none}
.c .d{font-weight:700;color:#7A5039}
.c .tm{font-family:'Playfair Display',serif;font-weight:500;color:#E07A4B;line-height:1}
.c.sp{background:linear-gradient(180deg,#FDB15D,#FF8A5C)}
.c.sp .d,.c.sp .tm,.c.sp .lb{color:#fff}
.c.we{background:#F6E2CB}
.c.we .d{color:#C0592C}
.c.ol{box-shadow:inset 0 0 0 3px #FF8A5C,0 6px 16px rgba(90,62,49,.08)}
.wk .hd.we{color:#C0592C}
.lg{display:flex;flex-wrap:wrap;gap:12px 26px;align-items:center;color:#5A3E31;font-weight:600}
.lg i{display:inline-block;width:26px;height:26px;border-radius:8px;vertical-align:-6px;margin-right:10px}
.c .lb{font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:#C0592C}
.bgph{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.veil{position:absolute;inset:0}
.ph-txt{color:#FBF4EC;text-shadow:0 2px 12px rgba(0,0,0,.55),0 1px 2px rgba(0,0,0,.5)}
.ph-txt .it{color:#FDB15D}
.ph-txt b{color:#fff}
.c{background:rgba(255,253,249,.94)}
.c .d,.c .tm,.c .lb{text-shadow:0 1.5px 0 rgba(255,255,255,1),0 2px 3px rgba(90,62,49,.30)}
.c .tm{font-weight:600;color:#D0612F}
.c .d{font-weight:800;color:#5A3E31}
.c.we{background:rgba(246,226,203,.95)}
.c.sp .d,.c.sp .tm,.c.sp .lb{text-shadow:0 1px 0 rgba(255,255,255,.35),0 2px 4px rgba(120,40,10,.45)}
.wk .hd{color:#5A3E31;font-weight:800;text-shadow:0 1px 0 rgba(255,255,255,.9)}
.wk .hd.we{color:#C0592C}
.lg,.note{text-shadow:0 1px 0 rgba(255,255,255,.9)}
.ft{position:absolute;left:64px;right:64px;display:flex;justify-content:space-between;font-weight:700;font-size:17px;letter-spacing:.22em;text-transform:uppercase;color:#7A5039;padding-top:16px;border-top:1.5px solid rgba(138,95,72,.35)}
.note{font-size:22px;line-height:1.5;color:#5A3E31}
"""
def grid(days, size):
    cell_h, dsz, tsz, lsz = size
    first = days[0]
    cells = [f'<div class="hd{" we" if i >= 5 else ""}">{h}</div>' for i, h in enumerate(HARI)]
    cells += ['<div class="c e"></div>'] * first.weekday()
    for d in days:
        sp = d in SPECIAL
        cls = " sp" if d in HOLIDAY else (" ol" if sp else (" we" if d.weekday() >= 5 else ""))
        if sp and d not in HOLIDAY and d.weekday() >= 5: cls += " we"
        lb = f'<div class="lb" style="font-size:{lsz}px;margin-top:4px">{SPECIAL[d]}</div>' if sp else ""
        cells.append(f'<div class="c{cls}" style="height:{cell_h}px;padding-top:{12 if not sp else 10}px">'
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

def page(pid, fmt, title, sub, days, size, top, foot_bottom, extra="", g=None, photo="", pos="50% 50%", band=400):
    T.append(f'''<div class="t {fmt}" id="{pid}">
  <div style="position:absolute;left:0;right:0;top:0;height:{band}px;overflow:hidden"><img class="bgph" src="{P}{photo}" style="object-position:{pos}" alt="">
    <div class="veil" style="background:linear-gradient(180deg,rgba(20,10,5,.30) 0%,rgba(20,10,5,0) 35%,rgba(20,10,5,0) 55%,rgba(20,10,5,.45) 100%)"></div></div>
  <div class="top ph-txt" style="top:{top}px"><img src="{LOGO}" alt="" style="filter:drop-shadow(0 2px 8px rgba(0,0,0,.45))"><span class="caps" style="font-size:19px;color:#FBF4EC">Kalender senja harian</span></div>
  <div class="ph-txt" style="position:absolute;left:64px;right:64px;bottom:{1350 - band + 22 if fmt == 'f' else 1920 - band + 26}px">
    <div class="pf" style="font-size:{70 if fmt == 'f' else 86}px;line-height:1.05">{title}</div>
    <div style="font-size:{21 if fmt == 'f' else 25}px;line-height:1.45;margin-top:6px">{sub}</div></div>
  <div style="position:absolute;left:64px;right:64px;top:{band + 22}px">{(g or grid)(days, size)}{extra}</div>
  <div class="ft" style="bottom:{foot_bottom}px"><span>Pantai Sunari · WITA</span><span>{TAG}</span></div></div>''')

T = []
nov = [dt.date(2026, 11, i) for i in range(1, 31)]; des = [d for d in DAYS if d.month == 12]
SUBN = "Jam matahari menyentuh laut di depan Pantai Sunari. Datang ke pantai <b>30 menit sebelumnya</b>."
SUBD = "Libur akhir tahun? Senja makin sore menjelang 2027. Tutup tahun dengan senja terakhir di Pantai Sunari."
key = lambda fs, full=True: f'''<div class="lg" style="font-size:{fs}px;margin-top:22px"><span><i style="background:#F6E2CB"></i>Akhir pekan</span>''' + ('''<span><i style="background:linear-gradient(180deg,#FDB15D,#FF8A5C)"></i>Hari libur nasional</span><span><i style="box-shadow:inset 0 0 0 3px #FF8A5C;background:#FFFDF9"></i>Senja terakhir 2026</span>''' if full else '<span style="font-weight:500">Tidak ada libur nasional di bulan ini</span>') + '</div>'
legend = lambda fs, full=True: key(fs, full) + f'''<div class="note" style="font-size:{fs}px;margin-top:14px">Golden hour ±40 menit sebelumnya · afterglow ±20 menit sesudahnya · jam dapat bergeser ±2 menit karena cuaca.</div>'''
page("kalender-harian-nov", "f", 'November <span class="it">2026</span>', SUBN, nov, (100, 22, 42, 12), 56, 50, legend(20, False), photo="senja/35-matahari-cakrawala-1751.jpg", pos="50% 55%", band=420)
page("kalender-harian-des", "f", 'Desember <span class="it">2026</span>', SUBD, des, (122, 24, 46, 13), 56, 50, legend(20), photo="senja/28-matahari-di-bawah-daun.jpg", pos="50% 58%", band=420)
page("story-kalender-harian-nov", "s", 'Senja <span class="it">November</span>', SUBN, nov, (114, 26, 50, 14), 140, 240, legend(24, False), photo="senja/12-kayak-matahari-merah-story.jpg", pos="50% 30%", band=660)
page("story-kalender-harian-des", "s", 'Senja <span class="it">Desember</span>', SUBD, des, (140, 28, 52, 15), 140, 240, legend(24), photo="senja/31-kayak-siluet-matahari-merah-story.jpg", pos="50% 43%", band=660)
(H / "kalender_harian.html").write_text(f'<!doctype html><html lang="id"><head><meta charset="utf-8">{FONTS}<style>{CSS}</style></head><body>{"".join(T)}</body></html>')
print(len(T), "desain")
for d in DAYS: print(d.isoformat(), HARI[d.weekday()], sunset(d))
