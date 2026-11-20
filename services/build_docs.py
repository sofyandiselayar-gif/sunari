"""SunaRi service documents (transfer rates & tour packages) – A4, text-only SunaRi style.
Run: python3 services/build_docs.py && node services/render.js"""
import pathlib
H = pathlib.Path(__file__).parent
WA = "+62 821-8903-3044"
FONTS = '<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;1,400&family=Montserrat:wght@400;500;600;700&display=swap" rel="stylesheet">'
CSS = """
*{margin:0;padding:0;box-sizing:border-box}
body{background:#ddd;font-family:Montserrat,sans-serif;color:#45301F;font-variant-numeric:lining-nums;-webkit-font-smoothing:antialiased}
.page{width:794px;height:1123px;background:#FBF4EC;position:relative;overflow:hidden;margin:20px auto;padding:44px 56px 84px;page-break-after:always}
.page>*{position:relative;z-index:1}
.page>.paper,.page>.grain{position:absolute;inset:0;z-index:0;pointer-events:none}
.paper{background:radial-gradient(ellipse at 50% 22%,rgba(255,255,255,.6),rgba(255,255,255,0) 62%),radial-gradient(ellipse at 50% 118%,rgba(90,62,49,.10),rgba(90,62,49,0) 60%)}
.grain{opacity:.5}
/* embossed frames: double (outer raised + inner pressed) */
.page>.frame{position:absolute;inset:20px;z-index:0;pointer-events:none;box-shadow:inset 1px 1px 0 rgba(90,62,49,.25),inset -1px -1px 0 rgba(255,255,255,.95),1px 1px 0 rgba(255,255,255,.9),-1px -1px 0 rgba(90,62,49,.14)}
.page>.frame2{position:absolute;inset:28px;z-index:0;pointer-events:none;box-shadow:inset 1px 1px 0 rgba(90,62,49,.18),inset -1px -1px 0 rgba(255,255,255,.9)}
/* letterpress text: crisp white highlight below, soft shade – no blur on body copy so it stays sharp */
.page{text-shadow:0 1px 0 rgba(255,255,255,.85)}
.hd h1,h2,.card h4,.ft .wa,.price .v{text-shadow:0 1px 0 rgba(255,255,255,1),0 -1px 0 rgba(90,62,49,.18),1px 2px 2.5px rgba(90,62,49,.28)}
.it{font-style:italic;color:#8A5F48}
.hd h1 .it,h2 .it,.card h4 .it{background:linear-gradient(180deg,#E9B97A 0%,#B9783A 48%,#7E5222 72%,#D9A462 100%);-webkit-background-clip:text;background-clip:text;color:transparent;
  text-shadow:none;filter:drop-shadow(0 1px 0 rgba(255,255,255,.9)) drop-shadow(.6px 1.3px 1px rgba(90,62,49,.35));padding-right:.08em}
.caps{font-weight:600;text-transform:uppercase;letter-spacing:.24em;color:#8A5F48}
.hd{text-align:center} .hd img{width:190px;display:block;margin:0 auto;filter:drop-shadow(0 1.5px 0 rgba(255,255,255,.95)) drop-shadow(1px 2px 2px rgba(60,40,30,.32))}
.rule{display:flex;align-items:center;justify-content:center;gap:12px;margin:8px 0 8px}
.rule i{width:90px;height:2px;display:block;border-top:1px solid rgba(138,95,72,.5);border-bottom:1px solid rgba(255,255,255,.95)}
.rule svg{filter:drop-shadow(0 1px 0 rgba(255,255,255,.9)) drop-shadow(1px 1.5px 1.5px rgba(90,62,49,.3))}
.hd h1{font-family:'Playfair Display',serif;font-weight:500;font-size:38px;line-height:1.12;margin-top:6px;color:#45301F}
.hd p{font-size:13px;margin-top:8px}
.chips{display:flex;justify-content:center;gap:10px;margin-top:12px;flex-wrap:wrap}
.chip{font-size:11px;font-weight:500;padding:6px 14px;border-radius:20px;box-shadow:inset 1px 1px 2px rgba(90,62,49,.22),inset -1px -1px 0 rgba(255,255,255,.95),0 1px 0 rgba(255,255,255,.8)}
.chip b{color:#E07A4B}
h2{font-family:'Playfair Display',serif;font-weight:500;font-size:24px;display:flex;align-items:center;gap:12px;margin:24px 0 10px;color:#45301F}
h2::after{content:"";flex:1;height:2px;border-top:1px solid rgba(138,95,72,.45);border-bottom:1px solid rgba(255,255,255,.95)}
h2 .n{font-family:Montserrat;font-weight:700;font-size:11px;letter-spacing:.18em;color:#C0592C;text-shadow:0 1px 0 rgba(255,255,255,.9)}
.sub{font-size:12px;margin:-2px 0 8px}
table{width:100%;border-collapse:collapse;font-size:13px} .big table{font-size:14.5px} .big td{padding:10px 6px} .cols table{font-size:13.5px} .cols td{padding:9.5px 6px} .itn table{font-size:13.5px} .itn td{padding:9px 6px}
th{font-weight:700;font-size:9.5px;letter-spacing:.16em;text-transform:uppercase;color:#8A5F48;text-align:left;padding:8px 6px;border-bottom:1px solid rgba(138,95,72,.55);box-shadow:0 1px 0 rgba(255,255,255,.9)}
td{padding:8px 6px;border-bottom:1px solid rgba(138,95,72,.22);vertical-align:top;line-height:1.4}
tr:last-child td{border-bottom:1px solid rgba(138,95,72,.4)}
td.r,th.r{text-align:right} td.b{font-weight:600} td.hi{font-weight:700;color:#A84A24}
td.t{white-space:nowrap;font-weight:700;width:104px;color:#8A5F48}
.cols{display:flex;gap:26px} .cols>div{flex:1;min-width:0}
.card{padding:12px 15px;border-radius:4px;background:transparent;box-shadow:inset 1px 1px 2px rgba(90,62,49,.24),inset -1px -1px 0 rgba(255,255,255,.95),0 1px 0 rgba(255,255,255,.8)}
.card h4{font-family:'Playfair Display',serif;font-weight:500;font-size:18px;line-height:1.25;color:#45301F}
.card p{font-size:12.5px;margin-top:5px;line-height:1.5}
ul.l{list-style:none;font-size:13.5px;line-height:1.5}
ul.l li{padding:3.5px 0 3.5px 20px;position:relative}
ul.l.ok li::before{content:"";position:absolute;left:2px;top:10px;width:8px;height:8px;border-radius:50%;background:radial-gradient(circle at 35% 30%,#FDB15D,#E07A4B 70%);box-shadow:0 1px 0 rgba(255,255,255,.9),.5px 1px 1px rgba(90,62,49,.35)}
ul.l.no li::before{content:"–";position:absolute;left:2px;top:3px;color:#8A5F48;font-weight:700}
ul.l.dot li::before{content:"";position:absolute;left:3px;top:11px;width:6px;height:6px;border-radius:50%;background:#8A5F48;box-shadow:0 1px 0 rgba(255,255,255,.9)}
.note{font-size:11px;margin-top:8px;line-height:1.5}
.terms{font-size:12px;line-height:1.5} .terms b{display:block;font-weight:700;margin-top:9px}
.price{text-align:center;padding:14px 8px} .price .v{font-family:'Playfair Display',serif;font-weight:500;font-size:23px;margin-top:4px}
.ft{position:absolute;left:56px;right:56px;bottom:36px;display:flex;justify-content:space-between;align-items:flex-end;padding-top:10px}
.ft::before{content:"";position:absolute;left:0;right:0;top:0;height:2px;border-top:1px solid rgba(138,95,72,.45);border-bottom:1px solid rgba(255,255,255,.95)}
.ft .wa{font-family:'Playfair Display',serif;font-weight:500;font-size:19px} .ft .wa span{font-style:italic;color:#8A5F48}
.ft .r{text-align:right;font-size:9.5px;font-weight:600;letter-spacing:.16em;text-transform:uppercase;color:#8A5F48;line-height:1.7}
.compact h2{margin:18px 0 8px} .compact .terms{font-size:13px} .compact .hd img{width:160px}
@page{size:210mm 297mm;margin:0} @media print{body{background:none}.page{margin:0}}
"""
GRAIN = '<svg class="grain" width="100%" height="100%"><filter id="gr"><feTurbulence type="fractalNoise" baseFrequency=".9" numOctaves="3" stitchTiles="stitch"/><feColorMatrix values="0 0 0 0 .35  0 0 0 0 .24  0 0 0 0 .18  0 0 0 .08 0"/></filter><rect width="100%" height="100%" filter="url(#gr)"/></svg>'
SUN = '''<svg viewBox="0 0 200 200" width="22" height="22"><defs><linearGradient id="sg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FDB15D"/><stop offset="1" stop-color="#FF8A5C"/></linearGradient>
<mask id="sm"><rect width="200" height="200" fill="white"/><rect y="112" width="200" height="5"/><rect y="126" width="200" height="7"/><rect y="142" width="200" height="9"/><rect y="160" width="200" height="11"/><rect y="180" width="200" height="13"/></mask></defs>
<circle cx="100" cy="100" r="96" fill="url(#sg)" mask="url(#sm)"/></svg>'''

def header(kicker, title, sub, chips=""):
    return f'''<div class="hd"><img src="../assets/logo-sunari-color.png"><div class="rule"><i></i>{SUN}<i></i></div>
  <div class="caps" style="font-size:10.5px">{kicker}</div><h1>{title}</h1><p>{sub}</p>{f'<div class="chips">{chips}</div>' if chips else ''}</div>'''
def footer(n, total):
    return f'''<div class="ft"><div><div class="caps" style="font-size:9px">Informasi &amp; reservasi</div><div class="wa"><span>WhatsApp</span> {WA}</div></div>
  <div class="r">SunaRi Beach Resort Selayar<br>Kepulauan Selayar, Sulawesi Selatan · {n}/{total}</div></div>'''
def page(inner, n, total, cls=''):
    return f'<div class="page {cls}"><div class="frame"></div><div class="frame2"></div>{inner}{footer(n, total)}</div>'
def table(head, rows, right_from=1, hi_last=False):
    th = "".join(f'<th class="{"r" if i >= right_from else ""}">{h}</th>' for i, h in enumerate(head))
    tr = ""
    for r in rows:
        tds = ""
        for i, c in enumerate(r):
            cls = ("b " if i == 0 else "") + ("r " if i >= right_from else "") + ("hi" if hi_last and i == len(r) - 1 else "")
            tds += f'<td class="{cls.strip()}">{c}</td>'
        tr += f"<tr>{tds}</tr>"
    return f"<table><tr>{th}</tr>{tr}</table>"
def itin(rows):
    return "<table>" + '<tr><th>Time (WITA)</th><th>Activities &amp; program</th></tr>' + "".join(f'<tr><td class="t">{t}</td><td>{a}</td></tr>' for t, a in rows) + "</table>"
def ul(items, kind="ok"):
    return f'<ul class="l {kind}">' + "".join(f"<li>{x}</li>" for x in items) + "</ul>"
def idr(v): return f"IDR {v:,}"

DOCS = {}

# ------------------------------------------------------------ 1. Transfer
local = [("H. Aroeppala Airport ↔ SunaRi Resort", 150000, 300000), ("Benteng Harbor ↔ SunaRi Resort", 200000, 400000), ("Pamatata Harbor ↔ SunaRi Resort", 400000, 800000)]
optA = [(1,"1 Car",1950000),(2,"1 Car",2000000),(3,"1 Car",2050000),(4,"1 Car",2100000),(5,"2 Cars",4050000),(6,"2 Cars",4100000),(7,"2 Cars",4150000),(8,"2 Cars",4200000)]
optB = [(1,"1 Car + Bus",1100000),(2,"1 Car + Bus",1550000),(3,"1 Car + Bus",2000000),(4,"1 Car + Bus",2450000),(5,"2 Cars + Bus",3550000),(6,"2 Cars + Bus",4000000),(7,"2 Cars + Bus",4450000),(8,"2 Cars + Bus",4900000)]
g = lambda n: f"{n} Guest{'s' if n > 1 else ''}"
p1 = header("SunaRi Beach Resort Selayar", 'Transfer &amp; <span class="it">Shuttle</span> Service Rates',
            "Private transport services: airport, harbor &amp; intercity shuttle from Makassar (1–8 guests)",
            '<span class="chip"><b>●</b> Private vehicle: exclusively for your group</span><span class="chip"><b>●</b> All-inclusive: vehicle, driver, fuel &amp; parking</span>')
p1 += '<h2><span class="n">01</span>Local Selayar Shuttle <span class="it">(one way)</span></h2><div class="sub">Pickup or drop-off between major transit hubs in Selayar and SunaRi Beach Resort.</div>'
p1 += '<div class="big">' + table(["Pickup / drop-off route", "1–4 guests (1 vehicle)", "5–8 guests (2 vehicles)"], [(r, idr(a) + " / way", idr(b) + " / way") for r, a, b in local]) + "</div>"
p1 += '<h2><span class="n">02</span>Terms &amp; <span class="it">inclusions</span></h2>' + ul([
    "<b>Vehicle capacity:</b> 1 car accommodates up to 4 guests + 4 medium suitcases. Groups of 5–8 guests use 2 vehicles.",
    "<b>Service inclusions:</b> private vehicle, professional driver, fuel and standard parking fees.",
    "<b>Ferry &amp; bus tickets:</b> calculated per person based on official operator rates. Premium/sleeper bus tickets include ferry crossing fees.",
    "<b>Reservation:</b> please confirm your travel schedule, arrival time and passenger details at least 24 hours prior (D-1)."])
p1 += '''<div class="cols" style="margin-top:26px"><div class="card price"><div class="caps" style="font-size:9.5px">Resort check-in</div><div class="v">14.00 WITA</div></div>
  <div class="card price"><div class="caps" style="font-size:9.5px">Resort check-out</div><div class="v">12.00 WITA</div></div>
  <div class="card price"><div class="caps" style="font-size:9.5px">Booking</div><div class="v">D-1</div></div></div>
  <div class="card" style="margin-top:14px;text-align:center"><h4>Plan your <span class="it">arrival</span></h4><p>Share your flight or ferry schedule when booking so we can time your pickup, and your journey ends with a sunset at Pantai Sunari.</p></div>'''
p2 = header("SunaRi Beach Resort Selayar", 'Intercity Transfer: <span class="it">Makassar</span> ↔ SunaRi', "Door-to-door journey from Makassar to SunaRi Beach Resort, including the ferry crossing (1–8 guests)")
p2 += '<h2><span class="n">03</span>Choose your <span class="it">option</span></h2><div class="sub">Choose between a direct Full Private Car or Premium Bus + Shuttle.</div>'
p2 += f'''<div class="cols">
  <div><div class="card" style="margin-bottom:8px"><h4>Option A · <span class="it">Full Private Car</span></h4><p>Direct private car journey Makassar ↔ Resort, including ferry crossing. Most convenient &amp; seamless travel.</p></div>
  {table(["Guests","Fleet","Total price"], [(g(n), f, idr(v)) for n, f, v in optA], right_from=2, hi_last=True)}</div>
  <div><div class="card" style="margin-bottom:8px"><h4>Option B · <span class="it">Premium Bus + Shuttle</span></h4><p>Sleeper/executive bus (Makassar–Pamatata) + private shuttle in Makassar &amp; Selayar. Cost-effective option.</p></div>
  {table(["Guests","Service","Total price"], [(g(n), f, idr(v)) for n, f, v in optB], right_from=2, hi_last=True)}</div></div>
  <div class="note">*Pricing breakdown: <b>Private Car</b>: vehicle IDR 1,900,000/unit + ferry IDR 50,000/person · <b>Premium Bus</b>: local shuttle IDR 650,000/unit + premium bus incl. ferry IDR 450,000/person.</div>'''
DOCS["01_Transfer_Shuttle_Rates"] = [p1, p2]

# ------------------------------------------------------------ tour builder
def tour(key, title_html, sub, highlights, rows, prices, incl, excl, car=False, note=""):
    gl = lambda n: f"{n} Person{'s' if n > 1 else ''}" + (f" ({'1 Car' if n <= 4 else '2 Cars'})" if car else "")
    a = header("SunaRi Beach Resort Selayar · Private Tour", title_html, sub)
    a += '<h2><span class="n">01</span>Key destinations &amp; <span class="it">highlights</span></h2>'
    hl = "".join(f'<div class="card"><div class="caps" style="font-size:9.5px">{k}</div><h4 style="margin-top:4px">{v}</h4></div>' for k, v in highlights)
    a += f'<div style="display:grid;grid-template-columns:1fr 1fr;gap:10px">{hl}</div>'
    a += '<h2><span class="n">02</span>Tour itinerary <span class="it">(full day)</span></h2><div class="itn">' + itin(rows) + '</div>'
    if note: a += f'<div class="note">{note}</div>'
    b = '<div style="height:10px"></div><h2 style="margin-top:0"><span class="n">03</span>Package options &amp; <span class="it">pricing per person</span></h2>'
    b += '<div class="big">' + table(["Number of guests", "Without guide (economy)", "With local tour guide"], [(gl(n), idr(x) + " /pax", idr(y) + " /pax") for n, x, y in prices], hi_last=True) + '</div>'
    b += f'''<div class="cols" style="margin-top:6px"><div><h2><span class="n">04</span>Package <span class="it">inclusions</span></h2>{ul(incl)}</div>
      <div><h2><span class="n">05</span>Package <span class="it">exclusions</span></h2>{ul(excl, "no")}</div></div>
      <div class="card" style="margin-top:22px;text-align:center"><h4>Before you go</h4><p>Breakfast at SunaRi Beach Resort is served from 07.00 before departure. Itineraries may be adjusted by the captain &amp; guide for weather, sea and tide conditions.</p></div>'''
    DOCS[key] = [a, b]

tour("02_Gusung_Island_Tour", 'Exotic <span class="it">Gusung</span> Island Trip', "Private one-day island hopping &amp; snorkeling",
     [("Snorkeling spot 01", "Liang Kareta · coral garden &amp; marine life"), ("Beach exploration", "Liang Kareta Beach &amp; Bone Malea Beach"),
      ("Cave &amp; beach", "Balojaha · exotic sea cave &amp; photo spots"), ("Snorkeling spot 02", "Jekneia · premier underwater spot")],
     [("07.00 – 08.00", "Preparation &amp; breakfast at SunaRi Beach Resort."), ("08.00 – 08.30", "Departure from SunaRi Beach Resort by private boat charter."),
      ("08.30 – 09.30", "<b>Snorkeling spot 01 (Liang Kareta):</b> explore vibrant coral reefs and marine life."), ("09.30 – 10.30", "Visit Liang Kareta Beach and continue to Bone Malea Beach."),
      ("10.30 – 11.30", "<b>Balojaha Beach &amp; Cave:</b> sea cave exploration, photo session and swimming."), ("11.30 – 12.30", "Lunch break (exclusive lunchbox served on location)."),
      ("12.30 – 13.30", "<b>Snorkeling spot 02 (Jekneia):</b> underwater exploration at Jekneia coral garden."), ("13.30 – 14.30", "Free time, swimming and water activities (optional: kayaking)."),
      ("15.00", "Return journey and arrival back at SunaRi Beach Resort. Tour ends.")],
     [(1,990000,1740000),(2,615000,990000),(3,490000,740000),(4,427500,615000),(5,390000,540000),(6,365000,490000),(7,347143,454286),(8,333750,427500)],
     ["Private boat charter", "Full snorkeling gear set + life jacket", "Lunchbox + mineral water", "Entrance tickets to all destinations", "Experienced boat captain &amp; crew", "Local tour guide (with-guide option)"],
     ["Personal expenses &amp; shopping", "Additional photo / video documentation", "Optional water sports (canoe / kayak rental)", "Tipping for captain / crew / guide (discretionary)"])
tour("03_Bahuluang_Island_Tour", 'Exotic <span class="it">Bahuluang</span> Island Trip', "Overland &amp; private boat island exploration",
     [("Meeting &amp; transit point", "Turungan Village"), ("Snorkeling spot", "Coral Tomb (Makam Karang)"),
      ("Sandbar &amp; beach", "Bahuluang Sandbar &amp; Bahuluang Beach"), ("Nature exploration", "Lipang Cave &amp; marine garden")],
     [("07.00 – 08.00", "Breakfast at SunaRi Beach Resort &amp; tour preparation."), ("08.00 – 09.00", "Overland transfer from SunaRi Beach Resort to Turungan Village by private car."),
      ("09.00 – 10.00", "Arrival at Turungan Village (meet boat captain) &amp; boat crossing to Bahuluang Island."), ("10.00 – 11.00", "<b>Snorkeling at Coral Tomb (Makam Karang):</b> explore unique coral formations."),
      ("11.00 – 12.00", "Visit <b>Bahuluang Sandbar</b> (subject to sea tide conditions)."), ("12.00 – 13.00", "Visit <b>Bahuluang Beach</b> &amp; enjoy lunch (lunchbox) together."),
      ("13.00 – 14.00", "<b>Lipang Cave exploration:</b> cave adventure &amp; exotic landscape viewing."), ("15.00 – 16.00", "Return journey and arrival back at SunaRi Beach Resort. Tour ends.")],
     [(1,2640000,3540000),(2,1440000,1890000),(3,1040000,1340000),(4,840000,1065000),(5,900000,1080000),(6,790000,940000),(7,711429,840000),(8,652500,765000)],
     ["Private car transport (Resort ⇄ Turungan Village)", "Private boat charter", "Full snorkeling gear set + life jacket", "Lunchbox + mineral water", "Entrance tickets to all destinations", "Driver &amp; fuel", "Local tour guide (with-guide option)"],
     ["Personal expenses &amp; shopping", "Additional photo / video documentation", "Optional extra activities", "Tipping for driver / captain / guide (discretionary)"], car=True)
tour("04_Polassi_Tambolongan_Tour", 'Exotic <span class="it">Polassi &amp; Tambolongan</span> Trip', "Nane Hill trekking, island hopping &amp; snorkeling",
     [("Polassi Island", "Nane Hill trekking &amp; Nane Hill Beach"), ("Meeting &amp; transit point", "Turungan Village"),
      ("Tambolongan Island", "Snorkeling spot &amp; beach"), ("Iconic highlight", "Tambolongan Sandbar")],
     [("07.00 – 08.00", "Breakfast at SunaRi Beach Resort &amp; tour preparation."), ("08.00 – 09.00", "Overland transfer from SunaRi Beach Resort to Turungan Village by private car."),
      ("09.00 – 10.30", "Arrival at Turungan Village &amp; boat crossing to Polassi Island."), ("10.30 – 11.45", "<b>Nane Hill trekking (±15 mins):</b> panoramic ocean views, sightseeing &amp; photos."),
      ("11.45 – 13.00", "Head to Nane Hill Beach, enjoy lunch (lunchbox) and rest."), ("13.00 – 14.00", "<b>Tambolongan Beach &amp; snorkeling spot:</b> coral reef exploration &amp; swimming."),
      ("14.00 – 15.00", "Visit <b>Tambolongan Sandbar</b> &amp; free time to relax."), ("15.00 – 16.30", "Return journey and arrival back at SunaRi Beach Resort. Tour ends.")],
     [(1,4147500,5047500),(2,2197500,2647500),(3,1547500,1847500),(4,1222500,1447500),(5,1207500,1387500),(6,1047500,1197500),(7,933214,1061786),(8,847500,960000)],
     ["Private car transport (Resort ⇄ Turungan Village)", "Private boat charter", "Full snorkeling gear set + life jacket", "Lunchbox + mineral water", "Entrance tickets to Nane Hill &amp; all attractions", "Driver &amp; fuel", "Local tour guide (with-guide option)"],
     ["Personal expenses &amp; shopping", "Additional photo / video documentation", "Optional extra activities", "Tipping for driver / captain / guide (discretionary)"], car=True)

# ------------------------------------------------------------ 5. Open trip
o1 = header("SunaRi Beach Resort Selayar · Open Trip", 'Explore <span class="it">Selayar</span> Island',
            "2-day open trip marine excursion: discover South Sulawesi's hidden paradise")
facts = [("Open trip price", "IDR 3,000,000", "per person"), ("Trip duration", "2 Days", "island hopping"), ("Minimum quota", "8 Persons", "per departure"), ("Meeting point", "Pick-up", "Selayar area / harbor")]
o1 += '<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:10px;margin-top:18px">' + "".join(
    f'<div class="card price"><div class="caps" style="font-size:8.5px">{k}</div><div class="v" style="{"color:#A84A24;font-size:20px" if i == 0 else ""}">{v}</div><div style="font-size:10.5px;margin-top:2px">{s}</div></div>' for i, (k, v, s) in enumerate(facts)) + "</div>"
def day(n, t, s, items):
    return f'''<h2><span class="n">DAY {n:02d}</span>{t}</h2><div class="sub" style="font-style:italic;font-family:'Playfair Display',serif;font-size:14px;color:#8A5F48">{s}</div>{ul(items, "dot")}'''
o1 += day(1, 'The hidden gems of <span class="it">Gusung</span> Island', "Pristine white sands, dramatic limestone cliffs &amp; untouched coral reefs", [
    "<b>Pick-up &amp; briefing:</b> morning group pick-up at the designated harbor meeting point, safety briefing and snorkeling gear distribution.",
    "<b>Balojaha Beach:</b> expansive stretches of white sand framed by crystal-clear turquoise water.",
    "<b>Liang Tarrusu Beach:</b> iconic limestone sea cliff with panoramic views, perfect for landscape photography.",
    "<b>Bone Malea Beach:</b> leisurely coastal lunch with freshly cooked lunch boxes by the shore.",
    "<b>Liang Kareta Beach:</b> secluded beach, open swimming and snorkeling over well-preserved coral gardens.",
    "<b>Return to harbor:</b> scenic cruise back and return transfer to your meeting point / resort."])
o1 += day(2, 'The wonders of <span class="it">Bahuluang &amp; Polassi</span>', "360° Nane Hill panorama, tidal sandbars, sea caves &amp; Makam Karang", [
    "<b>Morning departure:</b> guest pick-up and transfer to the departure harbor.",
    "<b>Nane Hill (Polassi Island):</b> light scenic hike to a 360° panorama of rolling hills meeting the open sea.",
    "<b>Pasi Timbul Polassi:</b> the emerging white sandbar in the middle of the sea (subject to tides).",
    "<b>Island lunch break:</b> freshly prepared warm lunch box on the island shore.",
    "<b>Liang Lipang (Bahuluang Island):</b> exotic coastal cave with natural rock formations, arches and limestone cliffs.",
    "<b>Snorkeling at Makam Karang:</b> legendary underwater coral mound teeming with tropical fish.",
    "<b>Documentation handover &amp; farewell:</b> return cruise, photo &amp; video package handover and drop-off."])
o2 = header("SunaRi Beach Resort Selayar · Open Trip", 'Inclusions &amp; <span class="it">guidelines</span>', "Explore Selayar Island · 2-day open trip")
o2 += f'''<div class="cols"><div>
  <h2><span class="n">01</span>Included</h2>{ul(["<b>Land transfers:</b> round-trip meeting point / harbor transfers in Selayar.", "<b>Chartered boat:</b> shared island-hopping boat for 2 days.",
     "<b>Snorkeling gear:</b> mask, snorkel and life jacket.", "<b>Tickets &amp; permits:</b> all destination spots &amp; island areas.", "<b>Meals &amp; drinks:</b> lunch boxes and mineral water for 2 days.",
     "<b>Tour guide:</b> experienced, licensed local guide.", "<b>Full documentation:</b> high-res landscape &amp; underwater photos and videos."])}
  <h2><span class="n">02</span>Not included</h2>{ul(["Flights, ferry or transport tickets to/from Selayar Island.", "Hotel / resort accommodation in Selayar.", "Personal expenses outside the package.", "Voluntary gratuities for boat crew and guide."], "no")}
  <h2><span class="n">03</span>What to bring</h2>{ul(["Swimwear &amp; a dry change of clothes", "Reef-safe sunscreen", "Sunglasses &amp; sun hat", "Waterproof dry bag for phones &amp; cameras", "Water shoes or anti-slip sandals"], "dot")}
  </div><div><h2><span class="n">04</span>Terms &amp; conditions</h2><div class="terms">
  <b>1. Minimum quota</b>Minimum 8 persons per departure. If not met, the organizer may offer a price adjustment, rescheduling or a full refund as mutually agreed.
  <b>2. Weather &amp; sea conditions</b>Weather, wind or swell may affect duration and routing. For safety, the captain and guide may adjust or reroute snorkeling spots.
  <b>3. Tidal cycles</b>Pasi Timbul Polassi depends on natural tides; the visit is scheduled flexibly on the day.
  <b>4. Mobile coverage</b>Some outer islands have little or no signal. Please finish urgent communication before departure.
  <b>5. Fitness &amp; terrain</b>Nane Hill and coastal reefs require moderate fitness. Anti-slip footwear is strongly advised.
  <b>6. Group punctuality</b>As an open group trip, punctuality and cooperation keep the itinerary smooth for everyone.</div>
  <div class="card" style="margin-top:18px;text-align:center"><div class="caps" style="font-size:9.5px">Private chartered group</div>
  <p style="font-family:'Playfair Display',serif;font-style:italic;font-size:14.5px;margin-top:6px">Prefer a private excursion? Private charters with customizable schedules are available for families and corporate groups.</p></div>
  </div></div>'''
DOCS["05_Open_Trip_Explore_Selayar"] = [o1, o2]

for key, pages in DOCS.items():
    html = "".join(page(p, i + 1, len(pages), "compact" if key.startswith("05") and i == 1 else "") for i, p in enumerate(pages))
    (H / f"{key}.html").write_text(f'<!doctype html><html lang="en"><head><meta charset="utf-8">{FONTS}<style>{CSS}</style></head><body>{html}</body></html>')
print(len(DOCS), "documents")
