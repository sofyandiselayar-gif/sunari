"""Highlight covers set 2 (1080x1920): 17 covers requested by owner.
Run: python3 social/build_highlights2.py && node social/render_highlights2.js"""
import pathlib
HERE = pathlib.Path(__file__).parent
D = "#A67C64"
S = f'fill="none" stroke="{D}" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"'
SUN = f'''<path d="M60 112 A40 40 0 0 1 140 112 Z" fill="{D}"/><g {S}><line x1="34" y1="112" x2="166" y2="112"/>
  <line x1="100" y1="50" x2="100" y2="60"/><line x1="58" y1="68" x2="65" y2="75"/><line x1="142" y1="68" x2="135" y2="75"/></g>'''
def month(m):
    return SUN + f'<text x="100" y="166" text-anchor="middle" font-family="Playfair Display" font-size="48" letter-spacing="4" fill="{D}">{m}</text>'
ICONS = [
 ("01-event", "Event", f'''<g {S}><path d="M30 64 Q100 112 170 64"/>
   <line x1="56" y1="80" x2="56" y2="92"/><line x1="100" y1="88" x2="100" y2="100"/><line x1="144" y1="80" x2="144" y2="92"/></g>
   <g fill="{D}"><circle cx="56" cy="100" r="9"/><circle cx="100" cy="108" r="9"/><circle cx="144" cy="100" r="9"/></g>
   <g {S}><path d="M84 160 V128 L124 120 V152"/></g><g fill="{D}"><ellipse cx="76" cy="160" rx="10" ry="8"/><ellipse cx="116" cy="152" rx="10" ry="8"/></g>'''),
 ("02-reservasi", "Reservasi Kamar", f'''<g {S}><rect x="50" y="62" width="100" height="90" rx="10"/><line x1="50" y1="88" x2="150" y2="88"/>
   <line x1="76" y1="50" x2="76" y2="72"/><line x1="124" y1="50" x2="124" y2="72"/><path d="M80 120 l14 14 l26 -28"/></g>'''),
 ("03-gusung", "Gusung Island", f'''<g {S}><path d="M40 136 Q100 116 160 136"/><path d="M100 128 Q96 96 104 66"/>
   <path d="M104 66 Q84 58 70 70"/><path d="M104 66 Q124 56 138 68"/><path d="M104 66 Q96 50 82 48"/><path d="M104 66 Q118 48 132 50"/>
   <path d="M36 158 q11 -8 22 0 t22 0 t22 0 t22 0 t22 0 t22 0"/></g>'''),
 ("04-bahuluang", "Bahuluang", f'''<g {S}><path d="M34 132 Q62 76 92 104 Q118 64 166 132"/><line x1="26" y1="132" x2="174" y2="132"/>
   <path d="M40 154 q11 -8 22 0 t22 0 t22 0 t22 0 t22 0 t22 0"/></g>'''),
 ("05-tamu", "Tamu", f'''<g {S}><circle cx="76" cy="78" r="18"/><path d="M42 146 q0 -40 34 -40 q34 0 34 40"/>
   <circle cx="128" cy="86" r="15"/><path d="M110 112 q8 -4 18 -4 q30 0 30 38"/></g>'''),
 ("06-ayunan", "Ayunan Raksasa", f'''<path d="M112 146 A30 30 0 0 1 172 146 Z" fill="{D}"/>
   <g {S}><line x1="70" y1="30" x2="46" y2="116"/><line x1="112" y1="30" x2="88" y2="116"/><line x1="38" y1="118" x2="96" y2="118"/>
   <line x1="40" y1="30" x2="150" y2="30"/><line x1="28" y1="146" x2="180" y2="146"/><path d="M44 168 q10 -7 20 0 t20 0 t20 0 t20 0 t20 0"/></g>'''),
 ("07-ramadhan", "Ramadhan", f'''<g {S}><path d="M118 50 A52 52 0 1 0 150 140 A42 42 0 1 1 118 50 Z"/></g>
   <path d="M142 78 l5 12 l13 1 l-10 8 l3 13 l-11 -7 l-11 7 l3 -13 l-10 -8 l13 -1 Z" fill="{D}"/>'''),
 ("08-kayak", "Kano / Kayak", f'''<g {S}><path d="M40 118 Q100 150 160 118 Q100 106 40 118 Z"/><line x1="66" y1="74" x2="134" y2="146"/>
   <path d="M60 68 l-6 -10 l14 2 Z" fill="{D}"/><path d="M140 152 l6 10 l-14 -2 Z" fill="{D}"/><circle cx="104" cy="94" r="8"/>
   <path d="M44 160 q10 -6 20 0 t20 0 t20 0 t20 0 t20 0"/></g>'''),
]
def ramadhan(year):
    return f'''<g {S}><path d="M112 34 A44 44 0 1 0 140 112 A35 35 0 1 1 112 34 Z"/></g>
   <path d="M136 58 l4 10 l11 1 l-8 7 l3 11 l-10 -6 l-9 6 l3 -11 l-8 -7 l11 -1 Z" fill="{D}"/>
   <text x="100" y="170" text-anchor="middle" font-family="Playfair Display" font-size="42" letter-spacing="3" fill="{D}" style="font-variant-numeric:lining-nums">{year}</text>'''
ICONS.append(("07b-ramadhan-1447", "Ramadhan 1447H", ramadhan("1447 H")))
ICONS.append(("07c-ramadhan-1448", "Ramadhan 1448H", ramadhan("1448 H")))
ICONS.append(("07d-layangan", "Layangan", f'''<g {S}><path d="M104 30 L146 74 L104 128 L62 74 Z"/><line x1="104" y1="30" x2="104" y2="128"/><line x1="62" y1="74" x2="146" y2="74"/>
   <path d="M104 128 q-10 12 0 22 t0 22 t-6 14"/></g>
   <g fill="{D}"><path d="M94 144 l-12 -6 l2 12 Z"/><path d="M112 162 l12 -6 l-2 12 Z"/></g>'''))
ICONS.append(("07e-qna", "Q&A", f'''<g {S}><path d="M40 60 h84 a12 12 0 0 1 12 12 v38 a12 12 0 0 1 -12 12 h-44 l-22 18 v-18 h-18 a12 12 0 0 1 -12 -12 v-38 a12 12 0 0 1 12 -12 Z"/>
   <path d="M112 132 v12 a10 10 0 0 0 10 10 h22 l18 14 v-14 h4 a10 10 0 0 0 10 -10 v-30 a10 10 0 0 0 -10 -10 h-20"/></g>
   <text x="82" y="106" text-anchor="middle" font-family="Playfair Display" font-size="44" fill="{D}">Q</text><text x="150" y="146" text-anchor="middle" font-family="Playfair Display" font-size="34" fill="{D}">A</text>'''))
ICONS.append(("07f-promo", "Promo", f'''<g {S}><path d="M104 40 H156 a8 8 0 0 1 8 8 V100 L96 168 a10 10 0 0 1 -14 0 L36 122 a10 10 0 0 1 0 -14 Z"/>
   <circle cx="136" cy="68" r="9"/></g>
   <path d="M96 84 l7 15 l16 2 l-12 11 l3 16 l-14 -8 l-14 8 l3 -16 l-12 -11 l16 -2 Z" fill="{D}"/>'''))
ICONS.append(("07g-find-us", "Find Us", f'''<g {S}><path d="M100 30 a32 32 0 0 1 32 32 c0 26 -32 58 -32 58 s-32 -32 -32 -58 a32 32 0 0 1 32 -32 Z"/>
   <path d="M50 160 Q74 136 100 150 T146 146" stroke-dasharray="0.1 16"/></g>
   <circle cx="100" cy="62" r="11" fill="{D}"/><circle cx="36" cy="164" r="9" fill="{D}"/>
   <path d="M166 118 a12 12 0 0 1 12 12 c0 10 -12 22 -12 22 s-12 -12 -12 -22 a12 12 0 0 1 12 -12 Z" fill="{D}"/><circle cx="166" cy="130" r="4.5" fill="#FBF4EC"/>'''))
ICONS.append(("07h-kalender-senja", "Kalender Senja", f'''<g {S}><rect x="56" y="40" width="88" height="82" rx="10"/><line x1="56" y1="60" x2="144" y2="60"/>
   <line x1="78" y1="30" x2="78" y2="48"/><line x1="122" y1="30" x2="122" y2="48"/><line x1="70" y1="104" x2="130" y2="104"/></g>
   <path d="M82 104 A18 18 0 0 1 118 104 Z" fill="{D}"/>
   <g {S}><line x1="100" y1="72" x2="100" y2="78"/><line x1="80" y1="80" x2="84" y2="84"/><line x1="120" y1="80" x2="116" y2="84"/></g>
   <text x="100" y="166" text-anchor="middle" font-family="Playfair Display" font-size="44" letter-spacing="4" fill="{D}" style="font-variant-numeric:lining-nums">2026</text>'''))
for i, (m, name) in enumerate([("APR","Sunset April"),("MEI","Sunset Mei"),("JUN","Sunset Juni"),("JUL","Sunset Juli"),
                                ("AGU","Sunset Agustus"),("SEP","Sunset Sept"),("OKT","Sunset Oktober"),("NOV","Sunset November"),("DES","Sunset Desember")], 9):
    ICONS.append((f"{i:02d}-sunset-{m.lower()}", name, month(m)))
cells = "".join(f'<div class="hl" id="hl2-{h}"><div class="ring"><svg viewBox="0 0 200 200" width="620" height="620">{svg}</svg></div></div>\n' for h, _, svg in ICONS)
prev = "".join(f'<div class="p"><div class="c"><img src="highlights-v2/hl2-{h}.png"></div><span>{l}</span></div>' for h, l, _ in ICONS)
html = f'''<!doctype html><html lang="id"><head><meta charset="utf-8"><title>SunaRi Highlights 2</title>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400&family=Montserrat:wght@400&display=swap" rel="stylesheet">
<style>*{{margin:0;padding:0;box-sizing:border-box}} body{{background:#ddd6cc;padding:40px;display:flex;flex-wrap:wrap;gap:40px;font-family:Montserrat,sans-serif}}
.hl{{width:1080px;height:1920px;background:#FBF4EC;display:flex;align-items:center;justify-content:center;flex:none}}
.ring{{width:860px;height:860px;border:7px solid {D};border-radius:50%;display:flex;align-items:center;justify-content:center}}
#preview{{width:1260px;background:#fff;padding:40px 30px 30px;display:flex;flex-wrap:wrap;gap:30px 26px;flex:none}}
.p{{text-align:center;width:120px}} .c{{width:120px;height:120px;border-radius:50%;padding:4px;border:2px solid #dbdbdb;overflow:hidden}}
.c img{{width:100%;height:100%;border-radius:50%;object-fit:cover}} .p span{{display:block;font-size:16px;margin-top:10px;color:#262626;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}}
</style></head><body>
{cells}<div id="preview">{prev}</div></body></html>'''
(HERE / "highlights2.html").write_text(html)
print(len(ICONS), "covers")
