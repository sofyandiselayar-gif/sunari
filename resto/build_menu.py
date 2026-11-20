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

def header(h, logo_w, title, sub, photo_pos="50% 55%"):
    return f'''<div style="position:absolute;left:0;right:0;top:0;height:{h}px;overflow:hidden">
  <img src="../assets/photos/aktivitas/03-ayunan-senja.jpg" style="width:100%;height:100%;object-fit:cover;object-position:{photo_pos}">
  <div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(40,26,20,.55),rgba(40,26,20,.15) 45%,rgba(40,26,20,.7))"></div>
  <img src="../assets/logo-sunari-color-dark.png" style="position:absolute;left:50%;transform:translateX(-50%);top:{int(h*0.08)}px;width:{logo_w}px">
  <div style="position:absolute;left:0;right:0;bottom:{int(h*0.1)}px;text-align:center;color:#FBF4EC">{title}{sub}</div></div>'''

# ---- A4 (794 x 1123 css px)
left = section("Makanan", MENU["Makanan"]) + section("Snack", MENU["Snack"]) + section("Soft Drink", MENU["Soft Drink"])
right = section("Drinks", MENU["Drinks"]) + section("Juice", MENU["Juice"])
a4 = f'''<div class="pg" id="menu-a4" style="width:794px;height:1123px;--h:23px;--f:12.2px;--rp:2.6px;--secgap:16px">
  {header(300, 230, '<div class="pf" style="font-size:54px;line-height:1">Bajoy Beach <span style="font-style:italic">Resto</span></div>',
          '<div class="caps" style="font-size:10px;color:#FBF4EC;margin-top:12px">Resto &amp; Bar · SunaRi Beach Resort</div>')}
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
  {header(520, 310, '<div class="pf" style="font-size:84px;line-height:1">Bajoy Beach <span style="font-style:italic">Resto</span></div>',
          f'<div class="caps" style="font-size:18px;color:#FBF4EC;margin-top:16px">{kicker}</div>', "50% 50%")}
  <div style="position:absolute;left:90px;right:90px;top:570px">{body}</div>
  <div style="position:absolute;left:90px;right:90px;bottom:300px">{hours(size=1.5)}</div>
  <div style="position:absolute;left:90px;right:90px;bottom:256px;text-align:center;font-size:16px;letter-spacing:.24em;text-transform:uppercase;color:#A67C64">Harga dalam ribu rupiah · WA {WA}</div>
</div>'''
s1 = story("menu-story-1-makanan", "Menu · Makanan &amp; Snack", [section("Makanan", MENU["Makanan"]), section("Snack", MENU["Snack"])])
s2 = story("menu-story-2-minuman", "Menu · Minuman",
           [f'<div style="display:flex;gap:56px"><div style="flex:1">{section("Drinks", MENU["Drinks"])}</div><div style="flex:1">{section("Juice", MENU["Juice"])}{section("Soft Drink", MENU["Soft Drink"])}</div></div>'])
(H / "menu.html").write_text(f'<!doctype html><html lang="id"><head><meta charset="utf-8">{FONTS}<style>{CSS}@page{{size:210mm 297mm;margin:0}}</style></head><body>{a4}{s1}{s2}</body></html>')
(H / "menu-print.html").write_text(f'<!doctype html><html lang="id"><head><meta charset="utf-8">{FONTS}<style>{CSS}body{{padding:0;background:none}}@page{{size:210mm 297mm;margin:0}}</style></head><body>{a4}</body></html>')
print("ok")
