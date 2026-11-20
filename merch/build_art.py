"""Merchandise artwork (print-ready, transparent PNG) for SunaRi souvenirs.
Run: python3 merch/build_art.py && node merch/render.js"""
import pathlib
H = pathlib.Path(__file__).parent
FONTS = '<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;1,400&family=Montserrat:wght@500;600;800&display=swap" rel="stylesheet">'
GOLD, CORAL, DRIFT, DEEP, CREAM = "#FDB15D", "#FF8A5C", "#A67C64", "#5A3E31", "#FBF4EC"
LOGO = {"d": "../assets/logo-sunari-color.png", "c": "../assets/logo-sunari-color-dark.png"}  # full-color logo (palette)

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
  <div style="display:flex;justify-content:center">{sun(id_, 200)}</div>
  <img src="{LOGO[k]}" style="width:960px;display:block;margin:10px auto 0">
  <div style="width:110px;height:3px;background:{acc};margin:30px auto 0"></div>
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
  <div style="position:absolute;left:320px;top:150px">{sun(id_+'s', 360)}</div>
  <img src="{LOGO["d"]}" style="position:absolute;left:160px;top:400px;width:680px">
</div>'''

def kayak(id_, k):
    ink = DEEP if k == "d" else CREAM
    return f'''<div class="art" id="{id_}" style="width:1000px;height:1080px;color:{ink};text-align:center">
  <div style="position:relative;width:640px;height:420px;margin:40px auto 0">
    <div style="position:absolute;left:120px;top:0">{sun(id_, 400)}</div>
    <svg viewBox="0 0 200 120" width="640" height="384" style="position:absolute;left:0;top:150px" fill="none" stroke="{ink}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round">
      <path d="M30 70 Q100 96 170 70 Q100 60 30 70 Z" fill="{ink}"/><circle cx="104" cy="40" r="10" fill="{ink}" stroke="none"/>
      <path d="M92 70 Q96 52 104 52 Q114 52 116 70 Z" fill="{ink}"/><line x1="70" y1="30" x2="138" y2="84"/><path d="M64 24 l-6 -9 l14 3 Z" fill="{ink}"/><path d="M144 90 l6 9 l-14 -3 Z" fill="{ink}"/>
      <path d="M20 100 q10 -6 20 0 t20 0 t20 0 t20 0 t20 0 t20 0 t20 0 t20 0"/></svg>
  </div>
  <div class="pf" style="font-size:96px;font-style:italic;margin-top:60px">Paddle into the sunset</div>
  <img src="{LOGO[k]}" style="width:560px;display:block;margin:26px auto 0">
</div>'''

def pattern(id_):
    cells = ""
    for r in range(4):
        for c in range(-1, 5):
            x, y = c * 250 + (125 if r % 2 else 0), r * 250 + 30
            if (r + c) % 2:
                cells += f'<text x="{x}" y="{y + 118}" text-anchor="middle" font-family="Playfair Display" font-style="italic" font-size="48" fill="{CORAL}">SunaRi</text>'
                continue
            cells += f'<g transform="translate({x - 70},{y + 30}) scale(.7)"><path d="M58 112 A42 42 0 0 1 142 112 Z" fill="{CORAL}"/><line x1="36" y1="112" x2="164" y2="112" stroke="{DRIFT}" stroke-width="6" stroke-linecap="round"/><path d="M56 134 q11 -8 22 0 t22 0 t22 0 t22 0" fill="none" stroke="{DRIFT}" stroke-width="6" stroke-linecap="round"/></g>'
    return f'''<div class="art" id="{id_}" style="width:1000px;height:1000px;background:{CREAM}"><svg viewBox="0 0 1000 1000" width="1000" height="1000">{cells}</svg></div>'''

ARTS = [back_print("A1-back-print-light", "d"), back_print("A1-back-print-dark", "c"),
        type_print("A2-typography-light", "d"), type_print("A2-typography-dark", "c"),
        sticker("A3-sticker-round"), kayak("A4-kayak-light", "d"), kayak("A4-kayak-dark", "c"),
        pattern("A5-pattern-tile"),
        f'<div class="art" id="A6-mark-pin" style="width:600px;height:600px">{mark(DRIFT, 600)}</div>',
        f'<div class="art" id="A7-sun-stripes" style="width:600px;height:600px">{sun("ss", 600)}</div>']

import math
DEEP_ = DEEP
def palm(x, y, s, col, flip=False, lean=40):
    """Palm-tree silhouette rooted at (x,y)."""
    tx, ty = lean, -300
    out = f'<g transform="translate({x},{y}) scale({-s if flip else s},{s})" fill="{col}" stroke="none">'
    out += f'<path d="M-9 0 C 2 -100, {tx*0.5-6} -200, {tx-6} {ty} L {tx+6} {ty} C {tx*0.5+8} -200, 14 -100, 9 0 Z"/>'
    for a, L in [(-168,170),(-132,190),(-95,150),(-58,190),(-22,175),(12,150),(-112,120),(-75,125)]:
        r = math.radians(a)
        ex, ey = tx + L*math.cos(r), ty + L*math.sin(r) + L*0.45
        mx, my = (tx+ex)/2, (ty+ey)/2
        nx, ny = -(ey-ty), (ex-tx); n = math.hypot(nx, ny) or 1; nx, ny = nx/n, ny/n
        w = L*0.16
        c1 = (mx + nx*w, my + ny*w - L*0.18); c2 = (mx - nx*w*0.4, my - ny*w*0.4 - L*0.10)
        out += f'<path d="M{tx} {ty} Q{c1[0]:.1f} {c1[1]:.1f} {ex:.1f} {ey:.1f} Q{c2[0]:.1f} {c2[1]:.1f} {tx} {ty} Z"/>'
    out += f'<circle cx="{tx-4}" cy="{ty+8}" r="9"/><circle cx="{tx+8}" cy="{ty+12}" r="8"/></g>'
    return out

def vintage_badge(id_, k):
    ink = DEEP if k == "d" else CREAM
    return f'''<div class="art" id="{id_}" style="width:1000px;height:1000px">
  <svg viewBox="0 0 1000 1000" width="1000" height="1000">
    <defs><path id="t{id_}" d="M500 500 m-372 0 a372 372 0 1 1 744 0"/><path id="b{id_}" d="M128 500 a372 372 0 0 0 744 0"/>
      <linearGradient id="sky{id_}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{GOLD}"/><stop offset="1" stop-color="{CORAL}"/></linearGradient>
      <clipPath id="c{id_}"><circle cx="500" cy="500" r="292"/></clipPath>
      <mask id="m{id_}"><rect width="1000" height="1000" fill="white"/>{"".join(f'<rect x="0" y="{560+i*26}" width="1000" height="{6+i*2}" fill="black"/>' for i in range(6))}</mask></defs>
    <circle cx="500" cy="500" r="478" fill="none" stroke="{ink}" stroke-width="12"/>
    <circle cx="500" cy="500" r="452" fill="none" stroke="{ink}" stroke-width="3"/>
    <circle cx="500" cy="500" r="300" fill="none" stroke="{ink}" stroke-width="6"/>
    <g clip-path="url(#c{id_})">
      <circle cx="500" cy="560" r="190" fill="url(#sky{id_})" mask="url(#m{id_})"/>
      {"".join(f'<rect x="200" y="{720+i*30}" width="600" height="7" rx="3" fill="{ink}" opacity="{0.85-i*0.15}"/>' for i in range(4))}
      {palm(300, 760, 0.95, ink, lean=55)}{palm(700, 760, 0.8, ink, flip=True, lean=45)}
    </g>
    <text font-family="Playfair Display" font-size="118" letter-spacing="4" fill="{CORAL}" dy="22"><textPath href="#t{id_}" startOffset="50%" text-anchor="middle">SunaRi</textPath></text>
    <text font-family="Montserrat" font-weight="600" font-size="36" letter-spacing="11" fill="{ink}" dy="34"><textPath href="#b{id_}" startOffset="50%" text-anchor="middle">BEACH RESORT · SELAYAR</textPath></text>
    <g fill="{CORAL}"><path d="M142 500 l12 -12 l12 12 l-12 12 Z"/><path d="M834 500 l12 -12 l12 12 l-12 12 Z"/></g>
  </svg></div>'''

def landscape(id_, text=True):
    h = 1150 if text else 1000
    band = f'''<div style="position:absolute;left:0;right:0;top:1000px;height:150px;background:{CREAM};display:flex;align-items:center;justify-content:space-between;padding:0 60px">
      <img src="{LOGO["d"]}" style="height:128px"><span class="caps" style="font-size:24px;letter-spacing:.38em;color:{DRIFT}">Pantai Sunari · Selayar</span></div>''' if text else ""
    refl = "".join(f'<rect x="{700-w/2}" y="{690+i*34}" width="{w}" height="10" rx="5" fill="{GOLD}" opacity="{0.9-i*0.12}"/>' for i, w in enumerate([300,240,190,140,100,60]))
    return f'''<div class="art" id="{id_}" style="width:1400px;height:{h}px;position:relative">
  <svg viewBox="0 0 1400 1000" width="1400" height="1000">
    <defs><linearGradient id="s{id_}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{CREAM}"/><stop offset=".45" stop-color="#F7A7A1"/><stop offset="1" stop-color="{CORAL}"/></linearGradient>
      <linearGradient id="u{id_}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFE3B8"/><stop offset="1" stop-color="{GOLD}"/></linearGradient>
      <linearGradient id="w{id_}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#7BA7B6"/><stop offset="1" stop-color="#3F6676"/></linearGradient></defs>
    <rect width="1400" height="660" fill="url(#s{id_})"/>
    <circle cx="700" cy="660" r="190" fill="url(#u{id_})"/>
    <path d="M0 610 Q200 585 360 612 Q420 600 470 620 L0 640 Z" fill="#B98577" opacity=".7"/>
    <rect y="655" width="1400" height="345" fill="url(#w{id_})"/>
    {refl}
    <path d="M0 1000 L0 900 Q300 860 700 905 Q1050 940 1400 880 L1400 1000 Z" fill="{DEEP}"/>
    {palm(150, 960, 1.7, DEEP, lean=90)}{palm(320, 950, 1.15, DEEP, lean=40)}{palm(1240, 930, 1.5, DEEP, flip=True, lean=70)}
    <g transform="translate(860,770)" fill="{DEEP}"><path d="M-80 0 Q0 18 80 0 Q0 -8 -80 0 Z"/><circle cx="6" cy="-26" r="9"/><path d="M-6 -2 Q0 -18 6 -18 Q14 -18 16 -2 Z"/><path d="M-50 -48 L60 30" stroke="{DEEP}" stroke-width="5"/></g>
  </svg>{band}</div>'''

def greetings(id_):
    return f'''<div class="art" id="{id_}" style="width:1300px;height:760px;text-align:center">
  <div class="pf" style="font-size:110px;font-style:italic;color:{DRIFT};line-height:1">Greetings from</div>
  <div style="font-family:Montserrat,sans-serif;font-weight:800;font-size:250px;line-height:1;letter-spacing:.02em;margin-top:10px;
    background:url(../assets/photos/senja/15-dua-kayak-oranye.jpg) 50% 70%/cover;-webkit-background-clip:text;background-clip:text;color:transparent">SELAYAR</div>
  <img src="{LOGO["d"]}" style="width:640px;display:block;margin:20px auto 0">
</div>'''

def chest_mini(id_, k):
    ink = DRIFT if k == "d" else CREAM
    return f'''<div class="art" id="{id_}" style="width:700px;height:360px;display:flex;align-items:center;justify-content:center">
  <img src="{LOGO[k]}" style="width:680px"></div>'''

def hangtag(id_, side):
    if side == "front":
        inner = f'<img src="{LOGO["c"]}" style="width:262px;margin-top:150px"><div class="caps" style="font-size:13px;letter-spacing:.35em;color:{CREAM};margin-top:30px">Tempat senja pulang</div><div style="position:absolute;left:0;right:0;bottom:40px;display:flex;justify-content:center">{mark(CREAM,64)}</div>'
        bg = DEEP
    else:
        inner = f'''<div style="margin-top:96px;color:{DEEP}"><img src="{LOGO["d"]}" style="width:230px"><div class="pf" style="font-size:30px;font-style:italic;margin:24px 26px 0;line-height:1.3">Dibawa pulang dari senja di Pantai Sunari.</div>
          <div style="width:50px;height:2px;background:{DRIFT};margin:26px auto"></div>
          <div class="caps" style="font-size:12px;letter-spacing:.25em;line-height:2">SunaRi Beach Resort<br>Kepulauan Selayar<br>@sunaribeachresortselayar</div></div>'''
        bg = CREAM
    return f'''<div class="art" id="{id_}" style="width:300px;height:540px;background:{bg};border-radius:14px;text-align:center;position:relative">
  <div style="position:absolute;left:130px;top:28px;width:40px;height:40px;border-radius:50%;background:#fff;box-shadow:inset 0 0 0 2px rgba(0,0,0,.08)"></div>{inner}</div>'''

ARTS += [vintage_badge("A8-vintage-badge-light","d"), vintage_badge("A8-vintage-badge-dark","c"),
         landscape("A9-sunset-landscape", True), landscape("A9-sunset-landscape-notext", False),
         greetings("A10-greetings-selayar"), chest_mini("A11-chest-mini-light","d"), chest_mini("A11-chest-mini-dark","c"),
         hangtag("A12-hangtag-front","front"), hangtag("A12-hangtag-back","back")]
html = f'''<!doctype html><html><head><meta charset="utf-8">{FONTS}<style>
*{{margin:0;padding:0;box-sizing:border-box}} body{{background:transparent;padding:40px;display:flex;flex-wrap:wrap;gap:60px;align-items:flex-start;font-family:Montserrat,sans-serif;font-variant-numeric:lining-nums}}
.art{{position:relative;flex:none}} .pf{{font-family:'Playfair Display',serif;font-weight:400}} .caps{{font-weight:600;text-transform:uppercase}}
</style></head><body>{"".join(ARTS)}</body></html>'''
(H / "art.html").write_text(html)
print(len(ARTS), "artworks")
