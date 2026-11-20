"""Flat product mockups for SunaRi souvenirs (uses merch/artwork/*.png)."""
import pathlib
H = pathlib.Path(__file__).parent
A = "artwork/"
FONTS = '<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;1,400&family=Montserrat:wght@500;600&display=swap" rel="stylesheet">'
SHIRT = "M330 60 Q500 130 670 60 L880 150 L985 390 L845 450 L800 360 L800 1040 Q500 1068 200 1040 L200 360 L155 450 L15 390 L120 150 Z"
COLLAR = "M330 60 Q500 175 670 60"
def shirt(col, art, w, top, blend="multiply", stroke="rgba(0,0,0,.12)"):
    return f'''<svg viewBox="0 0 1000 1100" width="900" height="990" style="position:absolute;left:150px;top:110px">
  <path d="{SHIRT}" fill="{col}" stroke="{stroke}" stroke-width="3"/><path d="{COLLAR}" fill="none" stroke="rgba(0,0,0,.18)" stroke-width="10"/>
  <path d="M200 360 L200 1040" stroke="rgba(0,0,0,.05)" stroke-width="30"/><path d="M800 360 L800 1040" stroke="rgba(0,0,0,.05)" stroke-width="30"/></svg>
  <img src="{A}{art}" style="position:absolute;left:{600 - w // 2}px;top:{top}px;width:{w}px;mix-blend-mode:{blend}">'''
def card(id_, title, sub, inner, bg="#EFE6DA"):
    return f'''<div class="mk" id="{id_}" style="background:{bg}">{inner}
  <div class="lab"><div class="t">{title}</div><div class="s">{sub}</div></div></div>'''
M = []
M.append(card("M01-kaos-krem-depan","Kaos krem · depan","Logo asli di dada kiri · sablon 1 warna Driftwood",
  shirt("#F3EADF","../../assets/logo-sunari-driftwood.png",230,330).replace("left:485px","left:610px")))
M.append(card("M02-kaos-krem-belakang","Kaos krem · belakang","Back print A1 · 25 × 31 cm",
  shirt("#F3EADF","A1-back-print-light.png",420,250)))
M.append(card("M03-kaos-cokelat-depan","Kaos cokelat tua · depan","Tipografi A2 versi terang",
  shirt("#5A3E31","A2-typography-dark.png",440,290,"normal","rgba(0,0,0,.25)")))
M.append(card("M04-kaos-putih-kayak","Kaos putih · depan","Desain kayak A4",
  shirt("#FFFFFF","A4-kayak-light.png",430,300)))
M.append(card("M05-tote-bag","Tote bag kanvas","Tipografi A2 · sablon 2 warna", f'''
  <svg viewBox="0 0 1200 1200" width="1200" height="1200" style="position:absolute;left:0;top:0">
   <path d="M430 330 Q430 120 600 120 Q770 120 770 330" fill="none" stroke="#D9C7A8" stroke-width="34"/>
   <path d="M300 320 H900 L930 1080 H270 Z" fill="#E9DCC4" stroke="rgba(0,0,0,.1)" stroke-width="3"/></svg>
  <img src="{A}A2-typography-light.png" style="position:absolute;left:350px;top:470px;width:500px;mix-blend-mode:multiply">'''))
M.append(card("M06-topi","Topi","Simbol bordir krem di atas topi Driftwood", f'''
  <svg viewBox="0 0 1200 1200" width="1200" height="1200" style="position:absolute;left:0;top:0">
   <path d="M260 700 Q260 330 600 330 Q940 330 940 700 Z" fill="#A67C64"/><path d="M600 330 V700" stroke="rgba(0,0,0,.15)" stroke-width="4"/>
   <path d="M420 365 Q480 520 470 700" fill="none" stroke="rgba(0,0,0,.1)" stroke-width="4"/><path d="M780 365 Q720 520 730 700" fill="none" stroke="rgba(0,0,0,.1)" stroke-width="4"/>
   <path d="M200 700 Q600 640 1000 700 Q980 820 600 830 Q220 820 200 700 Z" fill="#8F6A55"/><circle cx="600" cy="335" r="16" fill="#8F6A55"/></svg>
  <img src="../assets/mark-sunari-cream.svg" style="position:absolute;left:510px;top:460px;width:180px">'''))
M.append(card("M07-mug","Mug keramik","Matahari bergaris A7 + nama", f'''
  <svg viewBox="0 0 1200 1200" width="1200" height="1200" style="position:absolute;left:0;top:0">
   <path d="M820 470 Q990 470 990 640 Q990 810 820 810" fill="none" stroke="#F4EFE8" stroke-width="56"/>
   <path d="M820 470 Q990 470 990 640 Q990 810 820 810" fill="none" stroke="rgba(0,0,0,.08)" stroke-width="56"/>
   <rect x="300" y="330" width="540" height="620" rx="40" fill="#FBF8F3" stroke="rgba(0,0,0,.08)" stroke-width="3"/>
   <ellipse cx="570" cy="335" rx="270" ry="34" fill="#EFE8DE"/></svg>
  <img src="{A}A7-sun-stripes.png" style="position:absolute;left:445px;top:450px;width:250px">
  <div class="pf" style="position:absolute;left:300px;width:540px;top:735px;text-align:center;font-size:76px;color:#5A3E31">SunaRi</div>
  <div class="cp" style="position:absolute;left:300px;width:540px;top:840px;text-align:center;font-size:18px;color:#A67C64">Pantai Sunari · Selayar</div>'''))
M.append(card("M08-tumbler","Tumbler","Desain kayak A4", f'''
  <svg viewBox="0 0 1200 1200" width="1200" height="1200" style="position:absolute;left:0;top:0">
   <rect x="470" y="200" width="260" height="70" rx="16" fill="#5A3E31"/>
   <path d="M440 270 H760 L730 1060 Q600 1080 470 1060 Z" fill="#F3EADF" stroke="rgba(0,0,0,.08)" stroke-width="3"/>
   <path d="M480 270 L500 1060" stroke="rgba(255,255,255,.6)" stroke-width="16"/></svg>
  <img src="{A}A4-kayak-light.png" style="position:absolute;left:465px;top:520px;width:270px;mix-blend-mode:multiply">'''))
M.append(card("M09-gantungan-kunci","Gantungan kunci akrilik","Stiker bulat A3 · Ø 5 cm", f'''
  <svg viewBox="0 0 1200 1200" width="1200" height="1200" style="position:absolute;left:0;top:0">
   <circle cx="600" cy="230" r="60" fill="none" stroke="#B9B3AA" stroke-width="16"/><rect x="585" y="280" width="30" height="80" rx="8" fill="#B9B3AA"/>
   <circle cx="600" cy="680" r="330" fill="rgba(255,255,255,.55)" stroke="rgba(0,0,0,.08)" stroke-width="3"/><circle cx="600" cy="365" r="16" fill="#EFE6DA" stroke="#B9B3AA" stroke-width="5"/></svg>
  <img src="{A}A3-sticker-round.png" style="position:absolute;left:300px;top:380px;width:600px">'''))
M.append(card("M10-stiker","Lembar stiker","A3 · A7 · simbol · kayak", f'''
  <div style="position:absolute;left:170px;top:140px;width:860px;height:900px;background:#FFFFFF;box-shadow:0 20px 40px rgba(90,62,49,.15)"></div>
  <img src="{A}A3-sticker-round.png" style="position:absolute;left:220px;top:190px;width:420px">
  <img src="{A}A7-sun-stripes.png" style="position:absolute;left:700px;top:230px;width:260px">
  <img src="../assets/mark-sunari-driftwood.svg" style="position:absolute;left:700px;top:560px;width:260px">
  <img src="{A}A4-kayak-light.png" style="position:absolute;left:210px;top:660px;width:440px">'''))
M.append(card("M11-kartu-pos","Kartu pos","Foto senja + logo krem · 15 × 10 cm", f'''
  <div style="position:absolute;left:150px;top:300px;width:900px;height:600px;overflow:hidden;box-shadow:0 20px 40px rgba(90,62,49,.2);transform:rotate(-3deg)">
   <img src="../assets/photos/senja/17-kayak-berdua.jpg" style="width:100%;height:100%;object-fit:cover;object-position:50% 60%">
   <div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(40,26,20,.45),rgba(40,26,20,0) 50%)"></div>
   <img src="../assets/logo-sunari-cream.png" style="position:absolute;left:40px;top:34px;width:340px">
   <div class="cp" style="position:absolute;left:46px;bottom:30px;font-size:16px;color:#FBF4EC">Greetings from Pantai Sunari · Selayar</div></div>'''))
M.append(card("M12-pin","Pin enamel","Simbol · Ø 3 cm · enamel krem & emas", f'''
  <div style="position:absolute;left:400px;top:300px;width:400px;height:400px;border-radius:50%;background:#FBF4EC;border:22px solid #C9A46A;box-shadow:0 18px 30px rgba(90,62,49,.25),inset 0 0 0 4px rgba(0,0,0,.05)"></div>
  <img src="{A}A6-mark-pin.png" style="position:absolute;left:445px;top:345px;width:310px">'''))
M.append(card("M13-bandana","Bandana / sarung pantai","Pola A5 · bisa diulang tanpa sambungan", f'''
  <div style="position:absolute;left:200px;top:180px;width:800px;height:800px;transform:rotate(45deg) scale(.86);background:url({A}A5-pattern-tile.png) 0 0/260px 260px;box-shadow:0 20px 40px rgba(90,62,49,.18)"></div>'''))
sheet = "".join(f'<img src="mockup/{m.split(chr(34))[3]}.png">' for m in M)
html = f'''<!doctype html><html><head><meta charset="utf-8">{FONTS}<style>
*{{margin:0;padding:0;box-sizing:border-box}} body{{background:#ddd;padding:40px;display:flex;flex-wrap:wrap;gap:40px;font-family:Montserrat,sans-serif}}
.mk{{position:relative;width:1200px;height:1200px;overflow:hidden;flex:none}}
.lab{{position:absolute;left:60px;bottom:44px;color:#5A3E31}} .lab .t{{font-family:'Playfair Display',serif;font-size:46px}} .lab .s{{font-size:20px;letter-spacing:.06em;margin-top:8px;opacity:.75}}
.pf{{font-family:'Playfair Display',serif}} .cp{{font-weight:600;letter-spacing:.3em;text-transform:uppercase}}
#sheet{{width:2420px;background:#FBF4EC;padding:60px;display:grid;grid-template-columns:repeat(4,1fr);gap:20px}} #sheet img{{width:100%;display:block}}
#sheet h1{{grid-column:1/-1;font-family:'Playfair Display',serif;font-weight:400;font-size:80px;color:#5A3E31;margin-bottom:20px}} #sheet h1 i{{color:#A67C64}}
</style></head><body>{"".join(M)}<div id="sheet"><h1>SunaRi <i>Souvenir</i></h1>{sheet}</div></body></html>'''
(H / "mockups.html").write_text(html)
print(len(M), "mockups")
