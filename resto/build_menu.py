"""Bajoy Beach Resto menu (SunaRi brand): A4 print + 2 Instagram stories.
Run: python3 resto/build_menu.py && node resto/render.js"""
import pathlib
H = pathlib.Path(__file__).parent
WA = "0821-8903-3044"
MENU = {
 "Makanan": [("Nasi Goreng Sunari", 45), ("Nasi Goreng Seafood", 45), ("Nasi Goreng Egois", 45), ("Nasi Goreng Kampung", 45),
             ("Ayam Lalapan", 50), ("Ayam Bakar", 50), ("Beef Sandwich", 30), ("Beef Sandwich D.", 40),
             ("Egg Sandwich", 25), ("Egg Sandwich D.", 35), ("Indomie Goreng", 20), ("Indomie Kuah", 20)],
 "Snack": [("French Fries", 25), ("Toast", 25), ("Banana Roll", 25), ("Fried Cassava", 25), ("Fried Banana", 25)],
 "Drinks": [("Chocolate M.S", 25), ("Oreo M.S", 25), ("Orange Punch", 25), ("Watermelon L.M", 25), ("Green Tea", 25), ("Hot Tea", 10),
            ("Ice Tea", 20), ("Black Coffee", 20), ("Coffee Milk", 20), ("Milk Tea", 25), ("Original Coconut", 25), ("Saronso", 25)],
 "Juice": [("Avocado", 25), ("Watermelon", 25), ("Melon", 25), ("Mango", 25), ("Dragon Fruit", 25), ("Soursop Fruit", 25), ("Apple", 25), ("Orange", 25)],
 "Soft Drink": [("Coke", 15), ("Fanta", 15), ("Sprite", 15), ("Fresh Tea", 15), ("Pulpy", 15), ("Mineral Water", 10)],
}
FONTS = '<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;1,400&family=Montserrat:wght@400;500;600&display=swap" rel="stylesheet">'
CSS = """
*{margin:0;padding:0;box-sizing:border-box} body{background:#ddd;padding:30px;display:flex;gap:30px;align-items:flex-start;flex-wrap:wrap;font-family:Montserrat,sans-serif;color:#5A3E31;font-variant-numeric:lining-nums}
.pg{position:relative;background:#FBF4EC;overflow:hidden;flex:none}
.pf{font-family:'Playfair Display',serif;font-weight:400} .it{font-style:italic;color:#A67C64}
.caps{font-weight:600;text-transform:uppercase;letter-spacing:.32em;color:#A67C64}
.sec{margin-top:var(--secgap)} .sec:first-child{margin-top:0}
.sec h3{font-family:'Playfair Display',serif;font-weight:400;font-size:var(--h);display:flex;align-items:center;gap:14px}
.sec h3::after{content:"";flex:1;height:1px;background:#A67C64;opacity:.45}
.row{display:flex;align-items:baseline;font-size:var(--f);line-height:1.25;padding:var(--rp) 0}
.row .n{white-space:nowrap} .row .dots{flex:1;border-bottom:1.5px dotted rgba(166,124,100,.6);margin:0 8px;transform:translateY(-4px)}
.row .p{font-weight:600;white-space:nowrap}
"""
def section(name, items):
    rows = "".join(f'<div class="row"><span class="n">{n}</span><span class="dots"></span><span class="p">{p}K</span></div>' for n, p in items)
    return f'<div class="sec"><h3>{name}</h3>{rows}</div>'

def hours(dark=False, size=1.0):
    c = "#FBF4EC" if dark else "#5A3E31"
    return f'''<div style="display:flex;gap:{int(26*size)}px;align-items:stretch;color:{c}">
  <div style="flex:1;border:1px solid rgba(166,124,100,.55);padding:{int(12*size)}px {int(16*size)}px">
    <div class="caps" style="font-size:{8.5*size:.1f}px">Tamu menginap</div><div class="pf" style="font-size:{22*size:.0f}px;margin-top:4px">07.00 – 21.00</div></div>
  <div style="flex:1;border:1px solid rgba(166,124,100,.55);padding:{int(12*size)}px {int(16*size)}px">
    <div class="caps" style="font-size:{8.5*size:.1f}px">Tamu tidak menginap</div><div class="pf" style="font-size:{22*size:.0f}px;margin-top:4px">07.00 – 19.00</div></div></div>'''

def sun(size):
    gaps = "".join(f'<rect x="0" y="{y}" width="200" height="{h}" fill="black"/>' for y, h in [(112,5),(126,7),(142,9),(160,11),(180,13)])
    return f'''<svg viewBox="0 0 200 200" width="{size}" height="{size}"><defs><linearGradient id="sg{size}" x1="0" y1="0" x2="0" y2="1">
  <stop offset="0" stop-color="#FDB15D"/><stop offset="1" stop-color="#FF8A5C"/></linearGradient><mask id="sm{size}"><rect width="200" height="200" fill="white"/>{gaps}</mask></defs>
  <circle cx="100" cy="100" r="96" fill="url(#sg{size})" mask="url(#sm{size})"/></svg>'''

def header(h, logo_w, title, sub, photo_pos=None):
    """Text-only header in SunaRi style: color logo, serif title, hairline, small sun accent."""
    return f'''<div style="position:absolute;left:0;right:0;top:0;height:{h}px;text-align:center">
  <img src="../assets/logo-sunari-color.png" style="display:block;margin:{int(h*0.1)}px auto 0;width:{logo_w}px">
  <div style="display:flex;align-items:center;justify-content:center;gap:{int(h*0.05)}px;margin-top:{int(h*0.04)}px">
    <div style="width:{int(h*0.32)}px;height:1px;background:#A67C64;opacity:.5"></div>{sun(int(h*0.09))}<div style="width:{int(h*0.32)}px;height:1px;background:#A67C64;opacity:.5"></div></div>
  <div style="margin-top:{int(h*0.035)}px">{title}{sub}</div></div>'''

# ---- A4 (794 x 1123 css px)
left = section("Makanan", MENU["Makanan"]) + section("Snack", MENU["Snack"]) + section("Soft Drink", MENU["Soft Drink"])
right = section("Drinks", MENU["Drinks"]) + section("Juice", MENU["Juice"])
a4 = f'''<div class="pg" id="menu-a4" style="width:794px;height:1123px;--h:23px;--f:12.2px;--rp:2.6px;--secgap:16px">
  {header(300, 230, '<div class="pf" style="font-size:50px;line-height:1">Bajoy Beach <span class="it">Resto</span></div>',
          '<div class="caps" style="font-size:10px;margin-top:12px">Resto &amp; Bar · SunaRi Beach Resort</div>')}
  <div style="position:absolute;inset:22px;border:1px solid rgba(166,124,100,.45);pointer-events:none"></div>
  <div style="position:absolute;left:56px;right:56px;top:326px;display:flex;gap:46px">
    <div style="flex:1">{left}</div><div style="flex:1">{right}</div></div>
  <div style="position:absolute;left:56px;right:56px;bottom:62px">{hours()}</div>
  <div style="position:absolute;left:56px;right:56px;bottom:26px;display:flex;justify-content:space-between;font-size:9px;letter-spacing:.22em;text-transform:uppercase;color:#A67C64">
    <span>Harga dalam ribu rupiah (K = 1.000)</span><span>Senja Dinner · pesan H-1 · WA {WA}</span></div>
</div>'''

# ---- Stories (1080 x 1920)
def story(id_, kicker, cols):
    body = "".join(cols)
    return f'''<div class="pg" id="{id_}" style="width:1080px;height:1920px;--h:44px;--f:26px;--rp:6px;--secgap:34px">
  {header(520, 310, '<div class="pf" style="font-size:80px;line-height:1">Bajoy Beach <span class="it">Resto</span></div>',
          f'<div class="caps" style="font-size:18px;margin-top:16px">{kicker}</div>', "50% 50%")}
  <div style="position:absolute;left:90px;right:90px;top:570px">{body}</div>
  <div style="position:absolute;left:90px;right:90px;bottom:300px">{hours(size=1.5)}</div>
  <div style="position:absolute;left:90px;right:90px;bottom:256px;text-align:center;font-size:16px;letter-spacing:.24em;text-transform:uppercase;color:#A67C64">Harga dalam ribu rupiah · WA {WA}</div>
</div>'''
s1 = story("menu-story-1-makanan", "Menu · Makanan &amp; Snack", [section("Makanan", MENU["Makanan"]), section("Snack", MENU["Snack"])])
s2 = story("menu-story-2-minuman", "Menu · Minuman",
           [f'<div style="display:flex;gap:56px"><div style="flex:1">{section("Drinks", MENU["Drinks"])}</div><div style="flex:1">{section("Juice", MENU["Juice"])}{section("Soft Drink", MENU["Soft Drink"])}</div></div>'])
(H / "menu.html").write_text(f'<!doctype html><html lang="id"><head><meta charset="utf-8">{FONTS}<style>{CSS}@page{{size:210mm 297mm;margin:0}}</style></head><body>{a4}{s1}{s2}</body></html>')
(H / "menu-print.html").write_text(f'<!doctype html><html lang="id"><head><meta charset="utf-8">{FONTS}<style>{CSS}body{{padding:0;background:none}}@page{{size:210mm 297mm;margin:0}}</style></head><body>{a4}</body></html>')

# ---- Elegant embossed (letterpress) edition
EMB = """
.emb{background:#F3E8D8 !important}
.emb .paper{position:absolute;inset:0;pointer-events:none;z-index:0;
  background:radial-gradient(ellipse at 50% 30%,rgba(255,255,255,.55),rgba(255,255,255,0) 60%),radial-gradient(ellipse at 50% 120%,rgba(90,62,49,.10),rgba(90,62,49,0) 60%)}
.emb .grain{position:absolute;inset:0;pointer-events:none;z-index:0;opacity:.55}
.emb>*:not(.paper):not(.grain){z-index:1}
.emb .pf,.emb h3,.emb .row .n{color:#5A3E31;text-shadow:0 1px 0 rgba(255,255,255,.95),0 -1px 0 rgba(90,62,49,.16),1px 2px 2.5px rgba(90,62,49,.22)}
.emb .caps{color:#9A7058;text-shadow:0 1px 0 rgba(255,255,255,.9),0.5px 1px 1.2px rgba(90,62,49,.2)}
.emb .gold,.emb .row .p,.emb .it{background:linear-gradient(180deg,#F1D08E 0%,#C99643 45%,#8E6224 70%,#E5BD70 100%);-webkit-background-clip:text;background-clip:text;color:transparent !important;
  filter:drop-shadow(0 1px 0 rgba(255,255,255,.85)) drop-shadow(.6px 1.2px 1px rgba(90,62,49,.35));text-shadow:none}
.emb .sec h3::after{background:none;height:2px;border-top:1px solid rgba(154,112,88,.45);border-bottom:1px solid rgba(255,255,255,.9);opacity:1}
.emb .row .dots{border-bottom:none;height:2px;background-image:radial-gradient(circle,rgba(154,112,88,.55) 1px,transparent 1.3px);background-size:6px 2px;
  box-shadow:0 1px 0 rgba(255,255,255,.6)}
.emb .logo-emb{filter:drop-shadow(0 1.5px 0 rgba(255,255,255,.95)) drop-shadow(1px 2px 2px rgba(60,40,30,.32))}
.emb .box{border:none !important;box-shadow:inset 1px 1px 2px rgba(90,62,49,.22),inset -1px -1px 0 rgba(255,255,255,.95),0 1px 0 rgba(255,255,255,.8);border-radius:4px;background:rgba(255,255,255,.18)}
.emb .frame{border:none !important;box-shadow:inset 1px 1px 0 rgba(90,62,49,.22),inset -1px -1px 0 rgba(255,255,255,.95),1px 1px 0 rgba(255,255,255,.9),-1px -1px 0 rgba(90,62,49,.12)}
.emb .frame2{position:absolute;pointer-events:none;box-shadow:inset 1px 1px 0 rgba(90,62,49,.18),inset -1px -1px 0 rgba(255,255,255,.9)}
.emb svg.sunacc{filter:drop-shadow(0 1px 0 rgba(255,255,255,.9)) drop-shadow(1px 1.5px 1.5px rgba(90,62,49,.3))}
"""
GRAIN = '<svg class="grain" width="100%" height="100%"><filter id="gr"><feTurbulence type="fractalNoise" baseFrequency=".9" numOctaves="3" stitchTiles="stitch"/><feColorMatrix values="0 0 0 0 .35  0 0 0 0 .24  0 0 0 0 .18  0 0 0 .09 0"/></filter><rect width="100%" height="100%" filter="url(#gr)"/></svg>'
def emboss(html, old_id, new_id, frame_inset):
    h = html.replace(f'class="pg" id="{old_id}"', f'class="pg emb" id="{new_id}"', 1)
    i = h.index('>', h.index(f'id="{new_id}"')) + 1
    frames = f'<div class="frame2" style="inset:{frame_inset+10}px"></div>' if frame_inset else ''
    h = h[:i] + '<div class="paper"></div>' + GRAIN + frames + h[i:]
    h = h.replace('src="../assets/logo-sunari-color.png" style="display:block', 'class="logo-emb" src="../assets/logo-sunari-color.png" style="display:block')
    h = h.replace('<svg viewBox="0 0 200 200" width=', '<svg class="sunacc" viewBox="0 0 200 200" width=')
    h = h.replace('border:1px solid rgba(166,124,100,.45);pointer-events:none"', 'border:1px solid rgba(166,124,100,.45);pointer-events:none" class="frame"')
    h = h.replace('<div style="flex:1;border:1px solid rgba(166,124,100,.55);', '<div class="box" style="flex:1;border:1px solid rgba(166,124,100,.55);')
    return h
e_a4 = emboss(a4, "menu-a4", "menu-elegan-a4", 22)
e_s1 = emboss(s1, "menu-story-1-makanan", "menu-elegan-story-1-makanan", 0)
e_s2 = emboss(s2, "menu-story-2-minuman", "menu-elegan-story-2-minuman", 0)
for st in (e_s1, e_s2):
    pass
e_s1 = e_s1.replace('<div class="paper"></div>', '<div class="paper"></div><div class="frame" style="position:absolute;inset:40px;pointer-events:none"></div><div class="frame2" style="inset:52px"></div>', 1)
e_s2 = e_s2.replace('<div class="paper"></div>', '<div class="paper"></div><div class="frame" style="position:absolute;inset:40px;pointer-events:none"></div><div class="frame2" style="inset:52px"></div>', 1)
(H / "menu-elegan.html").write_text(f'<!doctype html><html lang="id"><head><meta charset="utf-8">{FONTS}<style>{CSS}{EMB}</style></head><body>{e_a4}{e_s1}{e_s2}</body></html>')
(H / "menu-elegan-print.html").write_text(f'<!doctype html><html lang="id"><head><meta charset="utf-8">{FONTS}<style>{CSS}{EMB}body{{padding:0;background:none}}@page{{size:210mm 297mm;margin:0}}</style></head><body>{e_a4}</body></html>')
print("ok")
