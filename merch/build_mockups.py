"""SunaRi Souvenir Collection: realistic flat mockups + tech-pack catalog (PDF).
Run: python3 merch/build_art.py && python3 merch/build_mockups.py && node merch/render.js
"""
import pathlib
H = pathlib.Path(__file__).parent
A = "artwork/"
AS = "../assets/"
GOLD, CORAL, DRIFT, DEEP, CREAM, SAND = "#FDB15D", "#FF8A5C", "#A67C64", "#5A3E31", "#FBF4EC", "#E6C89B"
WA = "0821-8903-3044"

# ------------------------------------------------------------------ helpers
def defs(uid):
    return f'''<defs>
  <filter id="b{uid}" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="30"/></filter>
  <filter id="b2{uid}" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="5"/></filter>
  <filter id="n{uid}"><feTurbulence type="fractalNoise" baseFrequency=".85" numOctaves="2" stitchTiles="stitch"/>
    <feColorMatrix values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 .07 0"/></filter>
  <linearGradient id="sx{uid}" x1="0" x2="1"><stop offset="0" stop-color="#000" stop-opacity=".16"/><stop offset=".22" stop-color="#000" stop-opacity="0"/>
    <stop offset=".78" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity=".16"/></linearGradient>
  <linearGradient id="cy{uid}" x1="0" x2="1"><stop offset="0" stop-color="#000" stop-opacity=".22"/><stop offset=".3" stop-color="#fff" stop-opacity=".28"/>
    <stop offset=".55" stop-color="#fff" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity=".28"/></linearGradient>
  <linearGradient id="sy{uid}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff" stop-opacity=".12"/><stop offset="1" stop-color="#000" stop-opacity=".12"/></linearGradient>
  <linearGradient id="mt{uid}" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#F5E3B5"/><stop offset=".45" stop-color="#C9A46A"/><stop offset="1" stop-color="#8E6B3A"/></linearGradient>
  <linearGradient id="wd{uid}" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#D8B48A"/><stop offset="1" stop-color="#B98B5E"/></linearGradient>
</defs>'''

def shaded(uid, path, fill, grad="sx", folds="", noise=True, stroke="rgba(0,0,0,.10)"):
    """Fill a shape, then clip shading/folds/noise to it."""
    return defs(uid) + f'''<clipPath id="c{uid}"><path d="{path}"/></clipPath>
  <path d="{path}" fill="{fill}" stroke="{stroke}" stroke-width="2"/>
  <g clip-path="url(#c{uid})"><rect width="1600" height="1600" fill="url(#{grad}{uid})"/>
    <g filter="url(#b{uid})">{folds}</g>{f'<rect width="1600" height="1600" filter="url(#n{uid})"/>' if noise else ''}</g>'''

def floor(cx, cy, rx, ry, op=.22):
    return f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="#5A3E31" opacity="{op}" style="filter:blur(18px)"/>'

def img(src, x, y, w, blend="multiply", extra=""):
    return f'<img src="{src}" style="position:absolute;left:{x}px;top:{y}px;width:{w}px;mix-blend-mode:{blend};{extra}">'

def svg(inner, uid):
    return f'<svg viewBox="0 0 1600 1600" width="1600" height="1600" style="position:absolute;left:0;top:0">{defs(uid)}{inner}</svg>'

def overlay(inner, uid, clip=None):
    """Folds drawn above the print (clipped to the garment) so artwork follows the fabric."""
    clip = clip or T(SHIRT)
    return (f'<svg viewBox="0 0 1600 1600" width="1600" height="1600" style="position:absolute;left:0;top:0;pointer-events:none;opacity:.4">{defs(uid+"o")}'
            f'<clipPath id="oc{uid}"><path d="{clip}"/></clipPath><g clip-path="url(#oc{uid})"><g filter="url(#b{uid}o)">{inner}</g></g></svg>')

# ------------------------------------------------------------------ garments
def T(p, s=1.2, ox=200, oy=150):
    """Transform 1000-box shirt coords to canvas."""
    import re
    def f(m):
        x, y = float(m.group(1)), float(m.group(2))
        return f"{ox + x*s:.0f} {oy + y*s:.0f}"
    return re.sub(r"(-?\d+(?:\.\d+)?) (-?\d+(?:\.\d+)?)", f, p)

SHIRT = "M300 70 C360 96 440 112 500 112 C560 112 640 96 700 70 L862 132 C905 152 945 235 988 362 L852 424 C836 392 818 365 802 346 L808 1032 C700 1062 300 1062 192 1032 L198 346 C182 365 164 392 148 424 L12 362 C55 235 95 152 138 132 Z"
NECK_IN = "M300 70 C360 150 640 150 700 70 C640 94 360 94 300 70 Z"
NECK_RIB = "M300 70 C360 150 640 150 700 70"
NECK_BACK = "M300 70 C360 100 640 100 700 70"
SH_DETAIL = "M24 340 L160 400 M976 340 L840 400 M196 1008 C300 1034 700 1034 804 1008"
SH_FOLDS = '<path d="{}" stroke="#000" stroke-opacity=".06" stroke-width="56" fill="none"/>'.format(T("M205 360 C262 430 252 540 238 640 M795 360 C738 430 748 540 762 640 M420 860 C455 930 440 990 450 1050 M600 900 C620 960 610 1010 620 1050"))
SH_HI = '<path d="{}" stroke="#fff" stroke-opacity=".14" stroke-width="70" fill="none"/>'.format(T("M330 300 C360 500 350 700 340 900 M660 280 C690 480 680 700 690 900"))

def shirt(uid, col, back=False, dark=False):
    neck = (f'<path d="{T(NECK_BACK)}" fill="none" stroke="#000" stroke-opacity=".18" stroke-width="22"/>' if back else
            f'<path d="{T(NECK_IN)}" fill="#000" fill-opacity=".22"/><path d="{T(NECK_RIB)}" fill="none" stroke="#000" stroke-opacity=".14" stroke-width="24"/>')
    return (floor(800, 1430, 560, 40) + shaded(uid, T(SHIRT), col, folds=SH_FOLDS + SH_HI) + neck +
            f'<path d="{T(SH_DETAIL)}" fill="none" stroke="#000" stroke-opacity=".14" stroke-width="4" stroke-dasharray="{"0" if not dark else "0"}"/>')

HOODIE = "M300 130 C360 150 640 150 700 130 L850 190 C900 220 930 330 950 600 L975 980 L880 995 L840 650 L812 420 L812 1000 L820 1050 L180 1050 L188 1000 L188 420 L160 650 L120 995 L25 980 L50 600 C70 330 100 220 150 190 Z"
def hoodie(uid, col):
    hood = T("M318 138 C300 10 700 10 682 138 C620 182 380 182 318 138 Z")
    hood_in = T("M372 144 C382 64 618 64 628 144 C580 196 420 196 372 144 Z")
    pocket = T("M320 760 L680 760 L726 950 L274 950 Z")
    rib = T("M180 1000 L820 1000 L820 1050 L180 1050 Z M25 960 L120 975 L118 995 L23 980 Z M975 960 L880 975 L882 995 L977 980 Z")
    strings = T("M450 175 L436 400 M550 175 L564 400")
    folds = '<path d="{}" stroke="#000" stroke-opacity=".07" stroke-width="56" fill="none"/>'.format(T("M190 430 C240 520 230 640 215 760 M810 430 C760 520 770 640 785 760 M80 650 C100 760 95 860 100 960 M920 650 C900 760 905 860 900 960"))
    return (floor(800, 1430, 600, 42) + shaded(uid, T(HOODIE), col, folds=folds) +
            f'<path d="{hood}" fill="{col}"/><path d="{hood}" fill="#000" fill-opacity=".08"/><path d="{hood_in}" fill="#000" fill-opacity=".35"/>'
            f'<path d="{pocket}" fill="none" stroke="#000" stroke-opacity=".18" stroke-width="5"/><path d="{rib}" fill="#000" fill-opacity=".10"/>'
            f'<path d="{strings}" stroke="{CREAM}" stroke-width="9" stroke-linecap="round"/>'
            f'<rect x="{200+430*1.2:.0f}" y="{150+398*1.2:.0f}" width="14" height="30" rx="4" fill="#C9A46A"/><rect x="{200+557*1.2:.0f}" y="{150+398*1.2:.0f}" width="14" height="30" rx="4" fill="#C9A46A"/>')

# ------------------------------------------------------------------ products
P = []   # (id, name, category, scene_html, specs dict)
def add(id_, name, cat, bg, html, spec):
    P.append((id_, name, cat, bg, html, spec))

# Kaos
add("K01-kaos-krem-depan", "Kaos Krem · Depan", "Kaos", "#EFE6DA",
    svg(shirt("k1", "#F4ECE1"), "k1") + img(AS+"logo-sunari-color.png", 870, 440, 270) + overlay(SH_FOLDS, "k1"),
    dict(artwork="Logo asli berwarna", warna="Krem / off-white", bahan="Katun combed 24s, 180–190 gsm", ukuran="S–XXL",
         cetak="Sablon plastisol 3 warna / DTF", posisi="Dada kiri, lebar 10 cm, 8 cm di bawah kerah", tinta="Coral #FF8A5C, Driftwood Deep #5A3E31, Driftwood #A67C64"))
add("K02-kaos-krem-belakang", "Kaos Krem · Belakang", "Kaos", "#EFE6DA",
    svg(shirt("k2", "#F4ECE1", back=True), "k2") + img(A+"A1-back-print-light.png", 545, 380, 510) + overlay(SH_FOLDS, "k2"),
    dict(artwork="A1 Back print (light)", warna="Krem / off-white", bahan="Katun combed 24s, 180–190 gsm", ukuran="S–XXL",
         cetak="DTF (gradasi matahari)", posisi="Punggung tengah, lebar 25 cm, 7 cm di bawah kerah", tinta="Full color"))
add("K03-kaos-cokelat-badge", "Kaos Cokelat Tua · Badge", "Kaos", "#E9DFD2",
    svg(shirt("k3", "#5A3E31", dark=True), "k3") + img(A+"A8-vintage-badge-dark.png", 610, 470, 380, "normal") + overlay(SH_FOLDS, "k3"),
    dict(artwork="A8 Vintage badge (dark)", warna="Cokelat tua", bahan="Katun combed 24s", ukuran="S–XXL",
         cetak="Sablon 3 warna (krem, emas, coral) / DTF", posisi="Dada tengah, Ø 22 cm", tinta="Krem #FBF4EC, Golden #FDB15D, Coral #FF8A5C"))
add("K04-kaos-putih-greetings", "Kaos Putih · Greetings", "Kaos", "#EDE4D8",
    svg(shirt("k4", "#FFFFFF"), "k4") + img(A+"A10-greetings-selayar.png", 560, 470, 480) + overlay(SH_FOLDS, "k4"),
    dict(artwork="A10 Greetings from Selayar", warna="Putih", bahan="Katun combed 30s", ukuran="S–XXL",
         cetak="DTF (foto di dalam huruf)", posisi="Dada tengah, lebar 26 cm", tinta="Full color"))
add("K05-kaos-pasir-kayak", "Kaos Pasir · Kayak", "Kaos", "#F1E8DC",
    svg(shirt("k5", "#E6C89B"), "k5") + img(A+"A4-kayak-light.png", 590, 470, 420) + overlay(SH_FOLDS, "k5"),
    dict(artwork="A4 Paddle into the sunset (light)", warna="Pasir / sand", bahan="Katun combed 24s", ukuran="S–XXL",
         cetak="Sablon 3 warna / DTF", posisi="Dada tengah, lebar 24 cm", tinta="Driftwood Deep, Golden, Coral"))
add("K06-hoodie", "Hoodie Driftwood", "Kaos", "#EFE6DA",
    svg(hoodie("h1", "#A67C64"), "h1") + img(A+"A11-chest-mini-dark.png", 870, 560, 230, "normal") + overlay(
        '<path d="{}" stroke="#000" stroke-opacity=".10" stroke-width="26" fill="none"/>'.format(T("M190 430 C240 520 230 640 215 760 M810 430 C760 520 770 640 785 760")), "h1", T(HOODIE)),
    dict(artwork="A11 Chest mini (dark)", warna="Driftwood", bahan="Fleece cotton 280 gsm", ukuran="S–XXL",
         cetak="Bordir 1 warna krem / sablon", posisi="Dada kiri, lebar 10 cm", tinta="Benang krem"))

# Topi
CAP = ("M330 980 C330 680 470 560 640 560 C830 560 950 680 950 980 Z")
add("T01-topi-baseball", "Topi Baseball", "Aksesoris", "#EFE6DA",
    svg(floor(800, 1270, 480, 40) + shaded("c1", CAP, "#A67C64", folds='<path d="M420 700 C460 800 450 900 440 980" stroke="#000" stroke-opacity=".14" stroke-width="30" fill="none"/>') +
        '<path d="M640 560 C620 690 615 830 625 980 M640 560 C750 650 810 800 830 980 M640 560 C520 650 460 800 440 980" stroke="#000" stroke-opacity=".16" stroke-width="5" fill="none"/>'
        '<circle cx="640" cy="565" r="20" fill="#8F6A55"/><circle cx="520" cy="700" r="7" fill="#000" opacity=".25"/><circle cx="790" cy="700" r="7" fill="#000" opacity=".25"/>'
        '<path d="M290 980 C430 930 930 930 1060 985 C1140 1060 1080 1160 820 1170 C540 1170 330 1120 290 980 Z" fill="#8C6650"/>'
        '<path d="M290 980 C430 930 930 930 1060 985" fill="none" stroke="#000" stroke-opacity=".25" stroke-width="6"/>'
        '<path d="M320 1010 C470 965 920 965 1040 1015" fill="none" stroke="#fff" stroke-opacity=".25" stroke-width="3" stroke-dasharray="10 8"/>', "c1")
    + img(AS+"logo-sunari-color-dark.png", 470, 690, 330, "normal", "transform:skewY(-2deg)"),
    dict(artwork="Logo asli berwarna (versi gelap)", warna="Driftwood", bahan="Katun twill, 6 panel, strap besi", ukuran="All size (adjustable)",
         cetak="Bordir flat 3 warna", posisi="Panel depan tengah, lebar 10 cm", tinta="Benang coral, krem, pasir"))
add("T02-bucket-hat", "Bucket Hat", "Aksesoris", "#F1E8DC",
    svg(floor(800, 1220, 520, 40) +
        shaded("c2", "M560 620 C560 500 640 470 800 470 C960 470 1040 500 1040 620 L1080 900 L520 900 Z", "#F4ECE1", grad="cy", folds='') +
        shaded("c3", "M330 900 C450 850 1150 850 1270 900 L1360 1060 C1150 1140 450 1140 240 1060 Z", "#EDE2D3", grad="sy") +
        '<path d="M560 620 C640 600 960 600 1040 620" fill="none" stroke="#000" stroke-opacity=".15" stroke-width="5"/>'
        '<path d="M520 900 C640 880 960 880 1080 900" fill="none" stroke="#000" stroke-opacity=".18" stroke-width="8"/>'
        '<path d="M290 1000 C500 1070 1100 1070 1310 1000" fill="none" stroke="#000" stroke-opacity=".15" stroke-width="3" stroke-dasharray="10 8"/>', "c2")
    + img(AS+"logo-sunari-color.png", 640, 640, 320, "multiply"),
    dict(artwork="Logo asli berwarna", warna="Krem", bahan="Kanvas katun", ukuran="56–58 cm", cetak="Bordir flat 3 warna", posisi="Depan tengah, lebar 9 cm", tinta="Benang coral, cokelat tua, Driftwood"))

# Tas
add("B01-tote-bag", "Tote Bag Kanvas", "Tas", "#EFE6DA",
    svg(floor(800, 1470, 520, 36) +
        '<path d="M600 520 C600 220 1000 220 1000 520" fill="none" stroke="#D3BE9C" stroke-width="40"/>'
        '<path d="M640 520 C640 280 960 280 960 520" fill="none" stroke="#000" stroke-opacity=".08" stroke-width="40"/>' +
        shaded("b1", "M380 500 H1220 L1260 1430 H340 Z", "#E9DCC4", folds='<path d="M560 600 C600 900 580 1200 600 1420 M1050 600 C1020 900 1040 1200 1020 1420" stroke="#000" stroke-opacity=".08" stroke-width="40" fill="none"/>') +
        '<path d="M380 540 H1220" stroke="#000" stroke-opacity=".12" stroke-width="4" stroke-dasharray="12 8"/>'
        '<rect x="590" y="500" width="40" height="80" fill="#D3BE9C"/><rect x="970" y="500" width="40" height="80" fill="#D3BE9C"/>', "b1")
    + img(A+"A10-greetings-selayar.png", 470, 820, 660),
    dict(artwork="A10 Greetings from Selayar", warna="Kanvas natural", bahan="Kanvas 12 oz, tali 70 cm", ukuran="38 × 42 cm",
         cetak="DTF", posisi="Tengah, lebar 30 cm", tinta="Full color"))
add("B02-pouch", "Pouch Serbaguna", "Tas", "#F1E8DC",
    svg(floor(800, 1150, 470, 30) +
        shaded("p1", "M360 560 Q360 520 400 520 H1200 Q1240 520 1240 560 L1260 1100 Q1260 1130 1230 1130 H370 Q340 1130 340 1100 Z", "#5A3E31", grad="sy") +
        '<rect x="370" y="560" width="860" height="22" fill="#3E2A20"/><path d="M380 571 H1220" stroke="#C9A46A" stroke-width="6" stroke-dasharray="6 6"/>'
        '<rect x="1180" y="548" width="34" height="70" rx="8" fill="url(#mtp1)"/>', "p1")
    + img(A+"A8-vintage-badge-dark.png", 640, 660, 320, "normal"),
    dict(artwork="A8 Vintage badge (dark)", warna="Cokelat tua", bahan="Kanvas, ritsleting logam", ukuran="25 × 16 cm", cetak="Sablon 3 warna / DTF", posisi="Tengah, Ø 12 cm", tinta="Krem, Golden, Coral"))

# Drinkware
add("D01-mug-keramik", "Mug Keramik", "Drinkware", "#EFE6DA",
    svg(floor(760, 1190, 420, 34) +
        '<path d="M1050 600 C1250 600 1250 980 1050 980" fill="none" stroke="#F7F2EA" stroke-width="64"/>'
        '<path d="M1050 600 C1250 600 1250 980 1050 980" fill="none" stroke="#000" stroke-opacity=".10" stroke-width="64"/>' +
        shaded("m1", "M430 470 H1090 V1110 Q1090 1170 1030 1170 H490 Q430 1170 430 1110 Z", "#FBF8F3", grad="cy", noise=False) +
        '<ellipse cx="760" cy="470" rx="330" ry="44" fill="#EFE8DE"/><ellipse cx="760" cy="476" rx="300" ry="34" fill="#5A3E31" opacity=".85"/>', "m1")
    + img(A+"A2-typography-light.png", 540, 620, 440),
    dict(artwork="A2 Typography (light)", warna="Putih", bahan="Keramik 11 oz", ukuran="Ø 8 × 9,5 cm", cetak="Sublimasi", posisi="Satu sisi, 18 × 8 cm", tinta="Full color"))
add("D02-mug-enamel", "Mug Enamel (Camping)", "Drinkware", "#F1E8DC",
    svg(floor(760, 1150, 380, 30) +
        '<path d="M1020 640 C1200 640 1200 940 1020 940" fill="none" stroke="#5A3E31" stroke-width="22"/>' +
        shaded("m2", "M470 560 H1050 V1080 Q1050 1120 1010 1120 H510 Q470 1120 470 1080 Z", "#FBF8F3", grad="cy", noise=False) +
        '<ellipse cx="760" cy="560" rx="290" ry="38" fill="#5A3E31"/><ellipse cx="760" cy="562" rx="276" ry="30" fill="#E8E2D8"/>'
        '<path d="M470 1080 Q470 1120 510 1120 H1010 Q1050 1120 1050 1080" fill="none" stroke="#5A3E31" stroke-width="12"/>', "m2")
    + img(A+"A4-kayak-light.png", 590, 700, 340),
    dict(artwork="A4 Kayak (light)", warna="Putih, bibir cokelat", bahan="Enamel baja 12 oz", ukuran="Ø 9 × 8 cm", cetak="Print transfer/decal enamel", posisi="Satu sisi, 10 × 9 cm", tinta="3 warna"))
add("D03-tumbler", "Tumbler Stainless", "Drinkware", "#EFE6DA",
    svg(floor(800, 1420, 260, 26) +
        shaded("t1", "M640 340 H960 V420 H640 Z", "#3E2A20", grad="cy", noise=False) +
        shaded("t2", "M610 420 H990 L950 1390 Q800 1420 650 1390 Z", "#A67C64", grad="cy", noise=False) +
        '<rect x="610" y="420" width="380" height="14" fill="#000" opacity=".15"/>', "t1")
    + img(A+"A8-vintage-badge-dark.png", 660, 760, 280, "normal"),
    dict(artwork="A8 Vintage badge (dark)", warna="Driftwood (powder coat)", bahan="Stainless 500 ml", ukuran="Ø 7 × 22 cm", cetak="Print UV / laser grafir", posisi="Tengah, Ø 6 cm", tinta="Krem, Golden, Coral"))

# Tekstil pantai
add("X01-handuk-pantai", "Handuk Pantai", "Tekstil", "#EDE4D8",
    svg(floor(800, 1250, 680, 40) +
        '<g stroke="#E6C89B" stroke-width="5">' + "".join(f'<line x1="{x}" y1="1180" x2="{x}" y2="1230"/>' for x in range(180, 1430, 22)) + '</g>', "x1")
    + '<div style="position:absolute;left:160px;top:420px;width:1280px;height:760px;overflow:hidden;box-shadow:0 0 0 1px rgba(0,0,0,.05)">'
      f'<img src="{A}A9-sunset-landscape.png" style="width:100%;height:100%;object-fit:cover">'
      '<div style="position:absolute;inset:0;background:linear-gradient(90deg,rgba(0,0,0,.08),rgba(255,255,255,.06) 30%,rgba(0,0,0,0) 60%,rgba(0,0,0,.1))"></div></div>',
    dict(artwork="A9 Sunset landscape", warna="Full color", bahan="Microfiber / katun terry", ukuran="140 × 70 cm", cetak="Print sublimasi tekstil", posisi="Full print", tinta="Full color"))
add("X02-sarung-pantai", "Sarung Pantai / Bandana", "Tekstil", "#F1E8DC",
    svg(floor(800, 1300, 560, 36), "x2")
    + f'<div style="position:absolute;left:330px;top:330px;width:940px;height:940px;transform:rotate(45deg) scale(.78);background:url({A}A5-pattern-tile.png) 0 0/300px 300px;box-shadow:0 30px 50px rgba(90,62,49,.18)">'
      '<div style="position:absolute;inset:0;background:linear-gradient(135deg,rgba(255,255,255,.18),rgba(0,0,0,0) 40%,rgba(0,0,0,.12))"></div>'
      '<div style="position:absolute;inset:18px;border:6px solid #A67C64;opacity:.7"></div></div>',
    dict(artwork="A5 Pattern (diulang)", warna="Krem + coral + Driftwood", bahan="Rayon / katun voile", ukuran="Sarung 110 × 170 cm, bandana 55 × 55 cm", cetak="Print digital tekstil", posisi="All-over + bingkai tepi", tinta="Full color"))

# Aksesoris kecil
add("A01-gantungan-akrilik", "Gantungan Kunci Akrilik", "Aksesoris", "#EFE6DA",
    svg(floor(800, 1320, 330, 26) +
        '<circle cx="800" cy="300" r="78" fill="none" stroke="url(#mta1)" stroke-width="18"/>'
        '<g fill="url(#mta1)">' + "".join(f'<rect x="788" y="{380+i*26}" width="24" height="20" rx="9"/>' for i in range(5)) + '</g>'
        '<circle cx="800" cy="860" r="420" fill="#fff" fill-opacity=".45" stroke="#fff" stroke-opacity=".8" stroke-width="6"/>'
        '<circle cx="800" cy="480" r="22" fill="#EFE6DA" stroke="#C9C1B5" stroke-width="5"/>', "a1")
    + img(A+"A3-sticker-round.png", 420, 500, 760, "normal")
    + '<div style="position:absolute;left:480px;top:520px;width:260px;height:420px;border-radius:50%;background:linear-gradient(135deg,rgba(255,255,255,.55),rgba(255,255,255,0));transform:rotate(-30deg)"></div>',
    dict(artwork="A3 Sticker round", warna="Full color", bahan="Akrilik bening 3 mm, ring besi", ukuran="Ø 5,5 cm", cetak="Print UV 2 sisi", posisi="Penuh", tinta="Full color"))
add("A02-gantungan-kayu", "Gantungan Kunci Kayu", "Aksesoris", "#F1E8DC",
    svg(floor(800, 1250, 300, 24) +
        '<circle cx="800" cy="330" r="70" fill="none" stroke="url(#mta2)" stroke-width="16"/>'
        '<rect x="560" y="440" width="480" height="780" rx="70" fill="url(#wda2)"/>' +
        "".join(f'<path d="M570 {480+i*55} C700 {460+i*55} 900 {500+i*55} 1030 {476+i*55}" stroke="#8E6440" stroke-opacity=".25" stroke-width="3" fill="none"/>' for i in range(13)) +
        '<circle cx="800" cy="520" r="26" fill="#EFE6DA" stroke="#8E6440" stroke-opacity=".5" stroke-width="4"/>', "a2")
    + img(AS+"mark-sunari-driftwood.svg", 650, 650, 300, "multiply", "filter:brightness(.55) contrast(1.3);opacity:.85")
    + '<div style="position:absolute;left:560px;top:990px;width:480px;text-align:center;font-family:Playfair Display,serif;font-size:76px;color:#4A3022;opacity:.8;mix-blend-mode:multiply">SunaRi</div>',
    dict(artwork="A6 Simbol + teks SunaRi", warna="Kayu natural", bahan="Kayu mahoni/jati 5 mm", ukuran="4 × 6,5 cm", cetak="Laser grafir", posisi="Depan", tinta="Bekas bakar laser"))
add("A03-pin-enamel", "Pin Enamel + Kartu", "Aksesoris", "#EFE6DA",
    svg(floor(800, 1330, 380, 28) +
        '<rect x="500" y="260" width="600" height="1040" rx="20" fill="#C8A27A"/><rect x="500" y="260" width="600" height="1040" rx="20" fill="url(#sypn)"/>'
        '<circle cx="800" cy="330" r="22" fill="#EFE6DA"/>'
        '<circle cx="800" cy="720" r="230" fill="url(#mtpn)"/><circle cx="800" cy="720" r="196" fill="#FBF4EC"/>', "pn")
    + img(A+"A6-mark-pin.png", 620, 540, 360, "normal")
    + '<div style="position:absolute;left:640px;top:600px;width:150px;height:240px;border-radius:50%;background:linear-gradient(135deg,rgba(255,255,255,.7),rgba(255,255,255,0));transform:rotate(-35deg)"></div>'
    + '<div style="position:absolute;left:500px;top:1020px;width:600px;text-align:center"><img src="../assets/logo-sunari-color.png" style="width:380px;mix-blend-mode:multiply">'
      '<div style="font-family:Montserrat;font-weight:600;font-size:18px;letter-spacing:.4em;color:#5A3E31;margin-top:14px">PANTAI SUNARI · SELAYAR</div></div>',
    dict(artwork="A6 Simbol", warna="Emas, enamel krem & Driftwood", bahan="Soft enamel, kuningan, peniti kupu-kupu", ukuran="Ø 3 cm; kartu 6 × 10 cm", cetak="Soft enamel + kartu kraft cetak 1 warna", posisi="Tengah kartu", tinta="—"))
add("A04-magnet-kulkas", "Magnet Kulkas", "Aksesoris", "#F1E8DC",
    svg(floor(800, 1180, 520, 30), "a4")
    + '<div style="position:absolute;left:300px;top:420px;width:1000px;height:760px;border-radius:40px;overflow:hidden;box-shadow:0 26px 44px rgba(90,62,49,.25);transform:rotate(-4deg)">'
      f'<img src="{A}A9-sunset-landscape.png" style="width:100%;height:100%;object-fit:cover">'
      '<div style="position:absolute;inset:0;background:linear-gradient(135deg,rgba(255,255,255,.35),rgba(255,255,255,0) 35%)"></div></div>',
    dict(artwork="A9 Sunset landscape", warna="Full color, glossy", bahan="Akrilik 3 mm + magnet", ukuran="7 × 5,5 cm", cetak="Print UV", posisi="Penuh", tinta="Full color"))
add("A05-tatakan-gelas", "Tatakan Gelas (set 2)", "Aksesoris", "#EFE6DA",
    svg(floor(620, 1150, 330, 26) + floor(1030, 1060, 330, 26) +
        '<circle cx="620" cy="830" r="320" fill="url(#wda5)"/>' + "".join(f'<circle cx="620" cy="830" r="{r}" fill="none" stroke="#8E6440" stroke-opacity=".18" stroke-width="3"/>' for r in range(40, 320, 34)) +
        '<circle cx="1030" cy="740" r="320" fill="#FBF4EC"/><circle cx="1030" cy="740" r="320" fill="url(#sya5)"/>', "a5")
    + img(AS+"logo-sunari-driftwood.png", 360, 700, 520, "multiply", "filter:brightness(.5) contrast(1.4);opacity:.8")
    + img(A+"A8-vintage-badge-light.png", 760, 470, 540, "multiply"),
    dict(artwork="Logo asli (grafir) & A8 Badge (cetak)", warna="Kayu natural & krem", bahan="Kayu pinus 5 mm / MDF berlapis", ukuran="Ø 10 cm", cetak="Laser grafir / print UV", posisi="Tengah", tinta="Full color / grafir"))

# Kertas
add("S01-buku-catatan", "Buku Catatan A5", "Alat tulis", "#EFE6DA",
    svg(floor(800, 1430, 470, 30) +
        '<rect x="460" y="230" width="700" height="1000" rx="18" fill="#FBF4EC" transform="rotate(4 810 730)"/>' +
        shaded("n1", "M440 210 H1140 Q1158 210 1158 228 V1192 Q1158 1210 1140 1210 H440 Z", "#C8A27A", grad="sy") +
        '<rect x="440" y="210" width="40" height="1000" fill="#000" opacity=".12"/>'
        '<rect x="1060" y="210" width="30" height="1000" fill="#5A3E31"/>', "n1")
    + img(A+"A2-typography-light.png", 540, 440, 540, "multiply"),
    dict(artwork="A2 Typography (light)", warna="Sampul kraft", bahan="Kraft 300 gsm, isi 80 lbr HVS 80 gsm bergaris", ukuran="A5 (14,8 × 21 cm)", cetak="Sablon / print UV 3 warna", posisi="Sampul depan tengah, lebar 11 cm", tinta="Coral, Driftwood Deep, Driftwood"))
add("S02-kartu-pos", "Set Kartu Pos (3)", "Alat tulis", "#F1E8DC",
    svg(floor(800, 1250, 600, 34), "s2")
    + '<div style="position:absolute;left:180px;top:420px;width:820px;height:550px;box-shadow:0 20px 40px rgba(90,62,49,.22);transform:rotate(-9deg);background:#FBF4EC;padding:0">'
      f'<img src="{A}A10-greetings-selayar.png" style="width:86%;margin:70px 7% 0"></div>'
    + '<div style="position:absolute;left:600px;top:560px;width:820px;height:550px;box-shadow:0 20px 40px rgba(90,62,49,.22);transform:rotate(6deg);overflow:hidden">'
      f'<img src="{A}A9-sunset-landscape.png" style="width:100%;height:100%;object-fit:cover"></div>'
    + '<div style="position:absolute;left:330px;top:720px;width:820px;height:550px;box-shadow:0 26px 50px rgba(90,62,49,.28);transform:rotate(-2deg);overflow:hidden">'
      f'<img src="../assets/photos/senja/17-kayak-berdua.jpg" style="width:100%;height:100%;object-fit:cover;object-position:50% 60%">'
      '<div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(40,26,20,.45),rgba(40,26,20,0) 45%)"></div>'
      f'<img src="{AS}logo-sunari-color-dark.png" style="position:absolute;left:36px;top:30px;width:330px"></div>',
    dict(artwork="A10, A9, foto senja + logo", warna="Full color", bahan="Art carton 310 gsm, laminasi doff", ukuran="15 × 10 cm (A6)", cetak="Cetak digital/offset 2 sisi", posisi="Depan full; belakang kolom alamat + logo", tinta="Full color"))
add("S03-stiker", "Lembar Stiker Die-cut", "Alat tulis", "#EFE6DA",
    svg(floor(800, 1440, 470, 30) + '<rect x="330" y="200" width="940" height="1220" rx="10" fill="#FFFFFF"/>', "s3")
    + "".join(img(src, x, y, w, "normal", "filter:drop-shadow(5px 0 0 #fff) drop-shadow(-5px 0 0 #fff) drop-shadow(0 5px 0 #fff) drop-shadow(0 -5px 0 #fff) drop-shadow(0 6px 10px rgba(90,62,49,.25))")
              for src, x, y, w in [(A+"A3-sticker-round.png",380,250,440),(A+"A8-vintage-badge-light.png",850,250,380),(A+"A7-sun-stripes.png",880,690,300),
                                   (AS+"mark-sunari-driftwood.svg",420,740,300),(A+"A4-kayak-light.png",380,1060,460),(A+"A11-chest-mini-light.png",860,1120,380)]),
    dict(artwork="A3, A4, A7, A8, A11, simbol", warna="Full color", bahan="Vinyl putih + laminasi doff, tahan air", ukuran="Lembar A6; stiker 3–7 cm", cetak="Print vinyl + kiss-cut", posisi="6 stiker per lembar", tinta="Full color"))

# Kemasan
add("P01-paper-bag", "Paper Bag Oleh-oleh", "Kemasan", "#EFE6DA",
    svg(floor(800, 1450, 500, 34) +
        '<path d="M640 470 C640 260 960 260 960 470" fill="none" stroke="#5A3E31" stroke-width="14"/>' +
        shaded("q1", "M400 460 H1200 L1230 1420 H370 Z", "#C8A27A", grad="sx") +
        '<path d="M400 460 L470 520 H1130 L1200 460" fill="#000" fill-opacity=".10"/><circle cx="640" cy="500" r="10" fill="#3E2A20"/><circle cx="960" cy="500" r="10" fill="#3E2A20"/>', "q1")
    + img(AS+"logo-sunari-color.png", 470, 740, 660, "multiply")
    + '<div style="position:absolute;left:400px;top:1150px;width:800px;text-align:center;font-family:Montserrat;font-weight:600;font-size:22px;letter-spacing:.42em;color:#4A3022;opacity:.85">TEMPAT SENJA PULANG</div>',
    dict(artwork="Logo asli berwarna + tagline", warna="Kraft cokelat / krem", bahan="Kraft 150 gsm, tali katun", ukuran="25 × 33 × 10 cm", cetak="Sablon / offset 3 warna", posisi="Depan tengah, lebar 20 cm", tinta="Coral, Driftwood Deep, Driftwood"))
add("P02-hang-tag", "Hang Tag & Label", "Kemasan", "#F1E8DC",
    svg(floor(800, 1300, 520, 30) +
        '<path d="M700 140 C640 300 560 330 580 420" fill="none" stroke="#5A3E31" stroke-width="4"/>'
        '<path d="M900 140 C960 300 1040 330 1020 420" fill="none" stroke="#5A3E31" stroke-width="4"/>', "p2")
    + f'<img src="{A}A12-hangtag-front.png" style="position:absolute;left:330px;top:380px;width:420px;transform:rotate(-6deg);filter:drop-shadow(0 16px 24px rgba(90,62,49,.25))">'
    + f'<img src="{A}A12-hangtag-back.png" style="position:absolute;left:850px;top:380px;width:420px;transform:rotate(5deg);filter:drop-shadow(0 16px 24px rgba(90,62,49,.25))">',
    dict(artwork="A12 Hang tag depan & belakang", warna="Driftwood / krem", bahan="Art carton 350 gsm / kraft, tali katun", ukuran="5 × 9 cm", cetak="Cetak digital 2 sisi + lubang", posisi="Digantung di produk tekstil", tinta="Full color"))

# ------------------------------------------------------------------ pages
CSS = """
*{margin:0;padding:0;box-sizing:border-box} body{background:#ddd;font-family:Montserrat,sans-serif;color:#5A3E31;font-variant-numeric:lining-nums}
.mk{position:relative;width:1600px;height:1600px;overflow:hidden;margin:20px}
.mk .lab{position:absolute;left:80px;bottom:60px} .mk .lab .t{font-family:'Playfair Display',serif;font-size:58px}
.mk .lab .s{font-size:20px;letter-spacing:.32em;text-transform:uppercase;margin-top:12px;color:#A67C64}
.mk .code{position:absolute;right:80px;bottom:66px;font-size:20px;letter-spacing:.3em;color:#A67C64}
.pg{width:1123px;height:794px;background:#FBF4EC;position:relative;overflow:hidden;page-break-after:always;margin:20px auto}
.pf{font-family:'Playfair Display',serif;font-weight:400} .it{font-style:italic;color:#A67C64}
.caps{font-weight:600;font-size:10px;letter-spacing:.32em;text-transform:uppercase;color:#A67C64}
.foot{position:absolute;left:56px;right:56px;bottom:26px;display:flex;justify-content:space-between;font-size:9px;letter-spacing:.3em;text-transform:uppercase;color:#A67C64}
table{border-collapse:collapse;width:100%} td{padding:9px 0;border-bottom:1px solid rgba(166,124,100,.35);font-size:11.5px;vertical-align:top}
td:first-child{width:34%;font-weight:600;font-size:9px;letter-spacing:.22em;text-transform:uppercase;color:#A67C64;padding-top:11px}
.sum td{padding:4px 0!important;font-size:9.5px!important}
@media print{body{background:none}.pg{margin:0}.mk{display:none}}
@page{size:297mm 210mm;margin:0}
"""
FONTS = '<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;1,400&family=Montserrat:wght@500;600;800&display=swap" rel="stylesheet">'

mk = "".join(f'''<div class="mk" id="{id_}" style="background:{bg}">{html}
  <div class="lab"><div class="t">{name}</div><div class="s">{cat}</div></div><div class="code">{id_.split("-")[0]}</div></div>''' for id_, name, cat, bg, html, _ in P)

def foot(n): return f'<div class="foot"><span>SunaRi Souvenir Collection</span><span>{n:02d}</span></div>'
pages = []
pages.append(f'''<div class="pg" style="background:#5A3E31">
  <img src="{A}A9-sunset-landscape-notext.png" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;opacity:.95">
  <div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(40,26,20,.55),rgba(40,26,20,0) 55%)"></div>
  <img src="{AS}logo-sunari-color-dark.png" style="position:absolute;left:60px;top:56px;width:330px">
  <div style="position:absolute;right:64px;top:70px;color:#FBF4EC;text-align:right;text-shadow:0 2px 18px rgba(40,26,20,.35)"><div class="pf" style="font-size:66px;line-height:1.05">Souvenir<br><span style="font-style:italic">Collection</span></div>
  <div style="font-weight:600;font-size:11px;letter-spacing:.38em;margin-top:22px">KATALOG PRODUK &amp; SPESIFIKASI CETAK</div></div>
  <div style="position:absolute;right:56px;bottom:30px;color:#FBF4EC;font-size:10px;letter-spacing:.3em">SUNARI BEACH RESORT · PANTAI SUNARI · SELAYAR</div></div>''')
pages.append(f'''<div class="pg"><div style="position:absolute;left:56px;top:50px;right:56px">
  <div class="caps">01 · Fondasi</div><div class="pf" style="font-size:44px;margin-top:10px">Warna, huruf &amp; <span class="it">logo</span></div>
  <div style="display:flex;gap:16px;margin-top:34px">{"".join(f'<div style="flex:1"><div style="height:120px;background:{h};border:1px solid rgba(0,0,0,.06)"></div><div style="font-size:10px;font-weight:600;letter-spacing:.18em;margin-top:10px">{n.upper()}</div><div style="font-size:10px;margin-top:3px;opacity:.7">{h}</div></div>' for n, h in [("Golden Hour",GOLD),("Coral Glow",CORAL),("Driftwood",DRIFT),("Driftwood Deep",DEEP),("Sandy Shore",SAND),("Shell Cream",CREAM)])}</div>
  <div style="display:flex;gap:40px;margin-top:40px;align-items:center">
    <div style="flex:1.3;background:#fff;height:250px;display:flex;align-items:center;justify-content:center"><img src="{AS}logo-sunari-color.png" style="width:82%"></div>
    <div style="flex:1;background:{DEEP};height:250px;display:flex;align-items:center;justify-content:center"><img src="{AS}logo-sunari-color-dark.png" style="width:82%"></div>
    <div style="flex:1;font-size:11.5px;line-height:1.7">
      <div class="pf" style="font-size:30px">Playfair Display</div><div style="opacity:.7">Judul &amp; nama produk</div>
      <div style="font-weight:600;font-size:18px;margin-top:14px;letter-spacing:.2em">MONTSERRAT</div><div style="opacity:.7">Label, keterangan, teks kecil</div>
      <div style="margin-top:14px"><b>Logo asli berwarna adalah elemen utama</b> di setiap produk: SunaRi Coral, teks Driftwood Deep, daun Driftwood. Untuk benda gelap: teks krem, daun pasir. Simbol matahari hanya untuk produk sangat kecil (&lt; 4 cm).</div></div></div></div>{foot(2)}</div>''')
arts = [("A1","A1-back-print-light","Back print"),("A2","A2-typography-light","Tipografi"),("A3","A3-sticker-round","Stiker bulat"),("A4","A4-kayak-light","Kayak"),
        ("A5","A5-pattern-tile","Pola"),("A6","A6-mark-pin","Simbol"),("A7","A7-sun-stripes","Matahari"),("A8","A8-vintage-badge-light","Vintage badge"),
        ("A9","A9-sunset-landscape","Landscape"),("A10","A10-greetings-selayar","Greetings"),("A11","A11-chest-mini-light","Chest mini"),("A12","A12-hangtag-front","Hang tag")]
cells = "".join(f'<div style="background:#fff;height:190px;position:relative;display:flex;align-items:center;justify-content:center;padding:16px"><img src="{A}{f}.png" style="max-width:100%;max-height:140px;object-fit:contain"><div style="position:absolute;left:12px;bottom:10px;font-size:9px;font-weight:600;letter-spacing:.2em">{c} · {n.upper()}</div></div>' for c, f, n in arts)
pages.append(f'''<div class="pg"><div style="position:absolute;left:56px;top:50px;right:56px">
  <div class="caps">02 · Artwork</div><div class="pf" style="font-size:44px;margin-top:10px">Perpustakaan <span class="it">desain</span></div>
  <div style="display:grid;grid-template-columns:repeat(6,1fr);gap:12px;margin-top:26px">{cells}</div>
  <div style="font-size:10.5px;margin-top:16px;opacity:.75">Semua file PNG transparan 300 dpi ada di folder <b>merch/artwork/</b>. Versi -light untuk benda terang, -dark untuk benda gelap.</div></div>{foot(3)}</div>''')
n = 4
for id_, name, cat, bg, html, sp in P:
    rows = "".join(f"<tr><td>{k}</td><td>{v}</td></tr>" for k, v in [("Kode", id_.split("-")[0]), ("Kategori", cat), ("Artwork", sp["artwork"]), ("Warna produk", sp["warna"]),
        ("Bahan", sp["bahan"]), ("Ukuran", sp["ukuran"]), ("Teknik cetak", sp["cetak"]), ("Posisi & ukuran cetak", sp["posisi"]), ("Tinta / benang", sp["tinta"])])
    pages.append(f'''<div class="pg"><img src="mockup-clean/{id_}.png" style="position:absolute;left:0;top:0;width:794px;height:794px">
  <div style="position:absolute;left:830px;right:44px;top:60px"><div class="caps">{cat}</div><div class="pf" style="font-size:30px;line-height:1.15;margin-top:8px">{name}</div>
  <table style="margin-top:20px">{rows}</table></div>{foot(n)}</div>''')
    n += 1
summary = "".join(f"<tr><td style='width:8%'>{i.split('-')[0]}</td><td style='font-size:11px;letter-spacing:0;text-transform:none;color:#5A3E31;font-weight:600'>{nm}</td><td>{s['ukuran']}</td><td>{s['cetak']}</td></tr>" for i, nm, _, _, _, s in P)
pages.append(f'''<div class="pg"><div style="position:absolute;left:56px;top:44px;right:56px">
  <div class="caps">Ringkasan produksi</div><div class="pf" style="font-size:34px;margin-top:8px">{len(P)} produk <span class="it">souvenir</span></div>
  <table class="sum" style="margin-top:14px">{summary}</table></div>{foot(n)}</div>''')
pages.append(f'''<div class="pg"><div style="position:absolute;left:56px;top:50px;right:56px;font-size:12px;line-height:1.75">
  <div class="caps">Catatan untuk vendor</div><div class="pf" style="font-size:40px;margin-top:10px">Sebelum <span class="it">produksi</span></div>
  <ol style="margin:24px 0 0 18px;max-width:900px">
  <li><b>Minta sampel/proof</b> setiap produk sebelum produksi massal. Warna di layar berbeda dengan tinta, benang, dan bahan.</li>
  <li><b>Cocokkan warna</b> dengan kode HEX di halaman 2. Untuk sablon, minta vendor mencocokkan ke kartu warna (Pantone) terdekat.</li>
  <li><b>Gradasi matahari</b> (Golden → Coral) hanya untuk DTF, sublimasi, print UV, dan cetak digital. Untuk sablon manual, gunakan 2 warna padat.</li>
  <li><b>Logo asli berupa file PNG</b> (bukan vektor). Aman untuk ukuran kecil–sedang. Untuk bordir, pin, dan cetak di atas 20 cm, buat ulang logo dalam format vektor (AI/SVG).</li>
  <li><b>Bordir &amp; pin</b> memakai simbol matahari, bukan tulisan kuas, agar detail tetap terbaca.</li>
  <li>Hubungi: SunaRi Beach Resort Selayar · WhatsApp {WA} · @sunaribeachresortselayar</li></ol></div>{foot(n+1)}</div>''')

html = f'<!doctype html><html lang="id"><head><meta charset="utf-8">{FONTS}<style>{CSS}</style></head><body>{mk}</body></html>'
(H / "mockups.html").write_text(html)
cat = f'<!doctype html><html lang="id"><head><meta charset="utf-8">{FONTS}<style>{CSS}</style></head><body>{"".join(pages)}</body></html>'
(H / "catalog.html").write_text(cat)
sheet = "".join(f'<img src="mockup/{p[0]}.png" style="width:100%;display:block">' for p in P)
(H / "overview.html").write_text(f'''<!doctype html><html><head><meta charset="utf-8">{FONTS}<style>*{{margin:0}}body{{background:#FBF4EC}}
#sheet{{width:2400px;padding:70px;display:grid;grid-template-columns:repeat(4,1fr);gap:20px;background:#FBF4EC}}
#sheet h1{{grid-column:1/-1;font-family:'Playfair Display',serif;font-weight:400;font-size:90px;color:#5A3E31;margin-bottom:10px}}#sheet h1 i{{color:#A67C64}}</style></head>
<body><div id="sheet"><h1>SunaRi <i>Souvenir Collection</i></h1>{sheet}</div></body></html>''')
print(len(P), "products,", len(pages), "catalog pages")
