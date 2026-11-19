"""Instagram highlight covers (1080x1920). Icon sits in the centre safe circle that Instagram crops.
Run: python3 social/build_highlights.py && node social/render_highlights.js"""
import pathlib
HERE = pathlib.Path(__file__).parent
D = "#A67C64"  # Driftwood, single colour like the logo
S = f'fill="none" stroke="{D}" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"'
ICONS = [
 ("hl-1-sunari", "SunaRi", f'''<path d="M58 112 A42 42 0 0 1 142 112 Z" fill="{D}"/>
   <g {S}><line x1="36" y1="112" x2="164" y2="112"/><path d="M56 132 q11 -8 22 0 t22 0 t22 0 t22 0"/><path d="M74 150 q8 -6 17 0 t17 0 t17 0"/></g>'''),
 ("hl-2-senja", "Senja", f'''<g {S}><path d="M62 120 a38 38 0 0 1 76 0"/><line x1="40" y1="120" x2="160" y2="120"/>
   <line x1="100" y1="58" x2="100" y2="70"/><line x1="58" y1="76" x2="66" y2="84"/><line x1="142" y1="76" x2="134" y2="84"/>
   <line x1="40" y1="100" x2="50" y2="100"/><line x1="150" y1="100" x2="160" y2="100"/>
   <line x1="70" y1="138" x2="130" y2="138"/><line x1="84" y1="154" x2="116" y2="154"/></g>'''),
 ("hl-3-kamar", "Kamar", f'''<g {S}><path d="M100 46 L52 150 M100 46 L148 150"/><line x1="42" y1="150" x2="158" y2="150"/>
   <path d="M88 150 V118 H112 V150"/><line x1="76" y1="98" x2="124" y2="98"/></g>'''),
 ("hl-4-resto", "Resto", f'''<g {S}><circle cx="100" cy="104" r="34"/><circle cx="100" cy="104" r="22"/>
   <path d="M48 62 V96 M40 62 V86 Q48 98 56 86 V62 M48 96 V150"/><path d="M152 62 Q140 80 146 104 H152 M152 62 V150"/></g>'''),
 ("hl-5-kayak", "Kayak", f'''<g {S}><path d="M40 118 Q100 150 160 118 Q100 106 40 118 Z"/><line x1="66" y1="74" x2="134" y2="146"/>
   <path d="M60 68 l-6 -10 l14 2 Z" fill="{D}"/><path d="M140 152 l6 10 l-14 -2 Z" fill="{D}"/><circle cx="104" cy="94" r="8"/>
   <path d="M44 160 q10 -6 20 0 t20 0 t20 0 t20 0 t20 0"/></g>'''),
 ("hl-6-lokasi", "Lokasi", f'''<g {S}><path d="M100 156 C78 126 62 106 62 84 a38 38 0 0 1 76 0 C138 106 122 126 100 156 Z"/>
   <circle cx="100" cy="84" r="14"/><path d="M58 160 H142"/></g>'''),
 ("hl-7-ulasan", "Ulasan", f'''<g {S}><path d="M100 50 L114 82 L148 85 L122 107 L130 141 L100 123 L70 141 L78 107 L52 85 L86 82 Z"/>
   <line x1="70" y1="160" x2="130" y2="160"/></g>'''),
 ("hl-8-booking", "Booking", f'''<g {S}><rect x="50" y="62" width="100" height="90" rx="10"/><line x1="50" y1="88" x2="150" y2="88"/>
   <line x1="76" y1="50" x2="76" y2="72"/><line x1="124" y1="50" x2="124" y2="72"/><path d="M80 120 l14 14 l26 -28"/></g>'''),
]
cells = ""
for hid, label, svg in ICONS:
    cells += f'''<div class="hl" id="{hid}"><div class="ring"><svg viewBox="0 0 200 200" width="620" height="620">{svg}</svg></div></div>\n'''
prev = "".join(f'<div class="p"><div class="c"><img src="highlights/{h}.png"></div><span>{l}</span></div>' for h, l, _ in ICONS)
html = f'''<!doctype html><html lang="id"><head><meta charset="utf-8"><title>SunaRi Highlights</title>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500&display=swap" rel="stylesheet">
<style>*{{margin:0;padding:0;box-sizing:border-box}} body{{background:#ddd6cc;padding:40px;display:flex;flex-wrap:wrap;gap:40px;font-family:Montserrat,sans-serif}}
.hl{{width:1080px;height:1920px;background:#FBF4EC;display:flex;align-items:center;justify-content:center;flex:none}}
.ring{{width:860px;height:860px;border:7px solid {D};border-radius:50%;display:flex;align-items:center;justify-content:center}}
#preview{{width:1080px;background:#fff;padding:40px 30px 50px;display:flex;gap:26px;flex:none}}
.p{{text-align:center;width:108px}} .c{{width:108px;height:108px;border-radius:50%;padding:4px;border:2px solid #dbdbdb;overflow:hidden}}
.c img{{width:100%;height:100%;border-radius:50%;object-fit:cover}} .p span{{display:block;font-size:17px;margin-top:10px;color:#262626}}
</style></head><body>
{cells}<div id="preview">{prev}</div></body></html>'''
(HERE / "highlights.html").write_text(html)
print("wrote highlights.html")
