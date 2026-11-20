"""Merchandise artwork (print-ready, transparent PNG) for SunaRi souvenirs.
Run: python3 merch/build_art.py && node merch/render.js"""
import pathlib
H = pathlib.Path(__file__).parent
FONTS = '<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;1,400&family=Montserrat:wght@500;600&display=swap" rel="stylesheet">'
GOLD, CORAL, DRIFT, DEEP, CREAM = "#FDB15D", "#FF8A5C", "#A67C64", "#5A3E31", "#FBF4EC"
LOGO = {"d": "../assets/logo-sunari-driftwood.png", "c": "../assets/logo-sunari-cream.png"}

def sun(uid, size, ink=None):
    """Retro sunset: gradient disc with horizontal cut-outs in the lower half (transparent gaps)."""
    gaps = "".join(f'<rect x="0" y="{y}" width="200" height="{h}" fill="black"/>' for y, h in [(112,5),(126,7),(142,9),(160,11),(180,13)])
    fill = ink or f"url(#g{uid})"
    return f'''<svg viewBox="0 0 200 200" width="{size}" height="{size}">
  <defs><linearGradient id="g{uid}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{GOLD}"/><stop offset="1" stop-color="{CORAL}"/></linearGradient>
  <mask id="m{uid}"><rect width="200" height="200" fill="white"/>{gaps}</mask></defs>
  <circle cx="100" cy="100" r="96" fill="{fill}" mask="url(#m{uid})"/></svg>'''

def mark(color, size):
    return f'''<svg viewBox="0 0 200 200" width="{size}" height="{size}" fill="none" stroke="{color}" stroke-linecap="round">
  <circle cx="100" cy="100" r="92" stroke-width="4"/><path d="M58 112 A42 42 0 0 1 142 112 Z" fill="{color}" stroke="none"/>
  <line x1="36" y1="112" x2="164" y2="112" stroke-width="5"/><path d="M56 132 q11 -8 22 0 t22 0 t22 0 t22 0" stroke-width="5"/>
  <path d="M74 150 q8 -6 17 0 t17 0 t17 0" stroke-width="5"/></svg>'''

def back_print(id_, k):
    ink = DRIFT if k == "d" else CREAM
    return f'''<div class="art" id="{id_}" style="width:1000px;height:1250px;color:{ink}">
  <div style="display:flex;justify-content:center;margin-top:30px">{sun(id_, 560)}</div>
  <img src="{LOGO[k]}" style="width:900px;display:block;margin:-90px auto 0">
  <div class="caps" style="font-size:34px;letter-spacing:.42em;text-align:center;margin-top:34px;padding-left:.42em">Tempat senja pulang</div>
  <div style="width:110px;height:3px;background:{ink};opacity:.6;margin:34px auto 0"></div>
  <div class="caps" style="font-size:24px;letter-spacing:.38em;text-align:center;margin-top:30px;padding-left:.38em;opacity:.9">Pantai Sunari · Kepulauan Selayar</div>
</div>'''

def type_print(id_, k):
    ink = DEEP if k == "d" else CREAM
    acc = DRIFT if k == "d" else GOLD
    return f'''<div class="art" id="{id_}" style="width:1000px;height:900px;color:{ink};text-align:center;padding-top:40px">
  <div style="display:flex;justify-content:center">{sun(id_, 230)}</div>
  <div class="pf" style="font-size:250px;line-height:1;margin-top:20px">SunaRi</div>
  <div class="pf" style="font-size:84px;font-style:italic;color:{acc};margin-top:4px">Beach Resort</div>
  <div style="width:110px;height:3px;background:{acc};margin:38px auto 0"></div>
  <div class="caps" style="font-size:28px;letter-spacing:.42em;margin-top:34px;padding-left:.42em">Selayar · Sulawesi Selatan</div>
</div>'''

def sticker(id_):
    return f'''<div class="art" id="{id_}" style="width:1000px;height:1000px">
  <svg viewBox="0 0 1000 1000" width="1000" height="1000">
    <defs><path id="tp{id_}" d="M500 500 m-385 0 a385 385 0 1 1 770 0"/><path id="bp{id_}" d="M115 500 a385 385 0 0 0 770 0"/></defs>
    <circle cx="500" cy="500" r="490" fill="{CREAM}"/><circle cx="500" cy="500" r="470" fill="none" stroke="{DRIFT}" stroke-width="10"/>
    <circle cx="500" cy="500" r="300" fill="none" stroke="{DRIFT}" stroke-width="3" opacity=".6"/>
    <text font-family="Montserrat" font-weight="600" font-size="38" letter-spacing="7" fill="{DEEP}"><textPath href="#tp{id_}" startOffset="50%" text-anchor="middle">WHERE EVERY DAY ENDS BEAUTIFULLY</textPath></text>
    <text font-family="Montserrat" font-weight="600" font-size="40" letter-spacing="16" fill="{DRIFT}" dy="34"><textPath href="#bp{id_}" startOffset="50%" text-anchor="middle">PANTAI SUNARI · SELAYAR</textPath></text>
    <circle cx="160" cy="500" r="9" fill="{CORAL}"/><circle cx="840" cy="500" r="9" fill="{CORAL}"/>
  </svg>
  <div style="position:absolute;left:250px;top:200px">{sun(id_+'s', 500)}</div>
  <div class="pf" style="position:absolute;left:0;right:0;top:640px;text-align:center;font-size:96px;color:{DEEP}">SunaRi</div>
</div>'''

def kayak(id_, k):
    ink = DEEP if k == "d" else CREAM
    return f'''<div class="art" id="{id_}" style="width:1000px;height:900px;color:{ink};text-align:center">
  <div style="position:relative;width:640px;height:420px;margin:40px auto 0">
    <div style="position:absolute;left:120px;top:0">{sun(id_, 400)}</div>
    <svg viewBox="0 0 200 120" width="640" height="384" style="position:absolute;left:0;top:150px" fill="none" stroke="{ink}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round">
      <path d="M30 70 Q100 96 170 70 Q100 60 30 70 Z" fill="{ink}"/><circle cx="104" cy="40" r="10" fill="{ink}" stroke="none"/>
      <path d="M92 70 Q96 52 104 52 Q114 52 116 70 Z" fill="{ink}"/><line x1="70" y1="30" x2="138" y2="84"/><path d="M64 24 l-6 -9 l14 3 Z" fill="{ink}"/><path d="M144 90 l6 9 l-14 -3 Z" fill="{ink}"/>
      <path d="M20 100 q10 -6 20 0 t20 0 t20 0 t20 0 t20 0 t20 0 t20 0 t20 0"/></svg>
  </div>
  <div class="pf" style="font-size:96px;font-style:italic;margin-top:60px">Paddle into the sunset</div>
  <div class="caps" style="font-size:28px;letter-spacing:.42em;margin-top:30px;padding-left:.42em">Pantai Sunari · Selayar</div>
</div>'''

def pattern(id_):
    cells = ""
    for r in range(5):
        for c in range(-1, 6):
            x, y = c * 200 + (100 if r % 2 else 0), r * 200
            cells += f'<g transform="translate({x - 70},{y + 30}) scale(.7)"><path d="M58 112 A42 42 0 0 1 142 112 Z" fill="{CORAL}"/><line x1="36" y1="112" x2="164" y2="112" stroke="{DRIFT}" stroke-width="6" stroke-linecap="round"/><path d="M56 134 q11 -8 22 0 t22 0 t22 0 t22 0" fill="none" stroke="{DRIFT}" stroke-width="6" stroke-linecap="round"/></g>'
    return f'''<div class="art" id="{id_}" style="width:1000px;height:1000px;background:{CREAM}"><svg viewBox="0 0 1000 1000" width="1000" height="1000">{cells}</svg></div>'''

ARTS = [back_print("A1-back-print-light", "d"), back_print("A1-back-print-dark", "c"),
        type_print("A2-typography-light", "d"), type_print("A2-typography-dark", "c"),
        sticker("A3-sticker-round"), kayak("A4-kayak-light", "d"), kayak("A4-kayak-dark", "c"),
        pattern("A5-pattern-tile"),
        f'<div class="art" id="A6-mark-pin" style="width:600px;height:600px">{mark(DRIFT, 600)}</div>',
        f'<div class="art" id="A7-sun-stripes" style="width:600px;height:600px">{sun("ss", 600)}</div>']
html = f'''<!doctype html><html><head><meta charset="utf-8">{FONTS}<style>
*{{margin:0;padding:0;box-sizing:border-box}} body{{background:transparent;padding:40px;display:flex;flex-wrap:wrap;gap:60px;align-items:flex-start;font-family:Montserrat,sans-serif;font-variant-numeric:lining-nums}}
.art{{position:relative;flex:none}} .pf{{font-family:'Playfair Display',serif;font-weight:400}} .caps{{font-weight:600;text-transform:uppercase}}
</style></head><body>{"".join(ARTS)}</body></html>'''
(H / "art.html").write_text(html)
print(len(ARTS), "artworks")
