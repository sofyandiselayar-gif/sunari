"""Preview 5 tema carousel memakai gambar 1 (duduk di meja, pantai surut).
- 5 slide contoh ukuran penuh (1080x1350) + 1 frame papan preview (feed 4:5).
Run: python3 social/grade_variasi.py && python3 social/build_tema_preview.py && node social/render_tema_preview.js
-> social/tema-preview/tema-1..5.png (2160x2700) & social/tema-preview/5-tema-carousel-1-frame.png (4320x5400)"""
import pathlib
H = pathlib.Path(__file__).parent
V = "../assets/photos/graded/variasi/01-duduk-meja-pantai-surut__"
FONTS = ('<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;0,700;1,400;1,500'
         '&family=Montserrat:wght@400;500;600;700&family=Caveat:wght@500;700&display=swap" rel="stylesheet">')
CSS = """
*{margin:0;padding:0;box-sizing:border-box}body{background:#bbb;font-family:Montserrat,sans-serif}
.t{position:relative;overflow:hidden;width:1080px;height:1350px;background:#FBF4EC;color:#45301F}
.solo{margin:30px auto}
.pf{font-family:'Playfair Display',serif}.cv{font-family:Caveat,cursive}
.ph{position:absolute;overflow:hidden}.ph img{width:100%;height:100%;object-fit:cover;display:block}
"""
# Palet warna diambil dari foto (median area), lihat percakapan
PAL = [("#E0CCA1", "Pasir Pagi"), ("#C79759", "Kayu Meja"), ("#A9B1B1", "Laut Surut"), ("#3E4521", "Daun Ketapang"), ("#46382F", "Bayang Teduh")]

def film(i):  # 1. Adegan Film
    return f'''<div class="t" id="tema-{i}" style="background:#0c0c0c;color:#EDE6DA">
  <div style="position:absolute;left:0;right:0;top:170px;text-align:center;font-weight:600;font-size:20px;letter-spacing:.5em;color:#8d877e">SCENE 01 · PANTAI SUNARI</div>
  <div class="ph" style="left:0;right:0;top:449px;height:452px"><img src="{V}tealorange.jpg" style="object-position:35% 62%" alt=""></div>
  <div style="position:absolute;left:80px;right:80px;top:940px;text-align:center;font-weight:500;font-size:32px;color:#fff">Dia datang ke pantai ini tanpa rencana apa pun.</div>
  <div class="pf" style="position:absolute;left:0;right:0;top:1080px;text-align:center;font-style:italic;font-size:44px;color:#cfc6b8">Menari di Selayar</div>
  <div style="position:absolute;left:0;right:0;top:1146px;text-align:center;font-weight:600;font-size:17px;letter-spacing:.5em;color:#6f6a63">A SHORT FILM · 2026</div>
  <div style="position:absolute;right:70px;bottom:70px;font-weight:600;font-size:18px;letter-spacing:.3em;color:#6f6a63">GESER →</div></div>'''

def surat(i):  # 2. Surat untuk Diriku
    return f'''<div class="t" id="tema-{i}" style="background:#F4ECDF;background-image:repeating-linear-gradient(0deg,transparent 0 63px,rgba(160,120,90,.16) 63px 64px)">
  <div style="position:absolute;left:150px;top:110px;width:780px;height:600px;background:#fff;padding:22px;transform:rotate(-2.5deg);box-shadow:0 16px 36px rgba(90,62,49,.22)">
    <div class="ph" style="position:relative;width:100%;height:100%"><img src="{V}earthy.jpg" style="object-position:35% 55%" alt=""></div></div>
  <div style="position:absolute;left:470px;top:86px;width:150px;height:46px;background:rgba(230,200,155,.75);transform:rotate(3deg)"></div>
  <div class="cv" style="position:absolute;left:110px;right:110px;top:790px;font-size:66px;line-height:1.15;color:#4A3426;font-weight:500">
    Untukku,<br>yang akhirnya berani<br>berhenti sejenak...</div>
  <div class="cv" style="position:absolute;right:110px;top:1150px;font-size:46px;color:#A0603E">— aku, di Pantai Sunari</div></div>'''

def palet(i):  # 3. Palet Warna Selayar
    sw = "".join(f'''<div style="text-align:center"><div style="width:168px;height:168px;border-radius:50%;background:{c};margin:0 auto;box-shadow:0 8px 18px rgba(90,62,49,.18)"></div>
      <div class="pf" style="font-size:25px;margin-top:16px">{n}</div><div style="font-weight:600;font-size:16px;letter-spacing:.14em;color:#8A6A55;margin-top:4px">{c}</div></div>''' for c, n in PAL)
    return f'''<div class="t" id="tema-{i}">
  <div class="ph" style="left:60px;right:60px;top:60px;height:700px;border-radius:22px"><img src="{V}film.jpg" style="object-position:40% 55%" alt=""></div>
  <div style="position:absolute;left:60px;right:60px;top:800px"><div style="font-weight:700;font-size:19px;letter-spacing:.34em;color:#C0592C">PALET WARNA · 01</div>
    <div class="pf" style="font-size:56px;margin-top:10px">Warna yang <i style="color:#A0603E">kubawa pulang.</i></div></div>
  <div style="position:absolute;left:30px;right:30px;top:1010px;display:flex;justify-content:space-around">{sw}</div></div>'''

def lookbook(i):  # 4. Lookbook Editorial
    return f'''<div class="t" id="tema-{i}" style="background:#ECE2D3">
  <div style="position:absolute;left:60px;right:60px;top:50px;display:flex;justify-content:space-between;font-weight:600;font-size:17px;letter-spacing:.36em;color:#7A5039"><span>SELAYAR EDIT</span><span>ISSUE 01</span></div>
  <div class="ph" style="left:450px;right:0;top:150px;height:1200px"><img src="{V}earthy.jpg" style="object-position:30% 50%" alt=""></div>
  <div class="pf" style="position:absolute;left:56px;top:150px;font-weight:700;font-size:104px;line-height:.95;color:#3B2A1E;letter-spacing:-.01em">BEACH<br>DAY</div>
  <div class="pf" style="position:absolute;left:62px;top:380px;font-style:italic;font-size:76px;color:#A0603E">in beige</div>
  <div style="position:absolute;left:62px;top:560px;width:300px;font-size:22px;line-height:2;color:#4A3426;border-top:1.5px solid rgba(90,62,49,.4);padding-top:18px">
    Hijab krem<br>Atasan rajut<br>Celana putih<br>Sandal jepit</div>
  <div style="position:absolute;left:62px;bottom:70px;font-weight:700;font-size:17px;letter-spacing:.34em;color:#7A5039">LOOK 01 / 06</div></div>'''

def diary(i):  # 5. Catatan Satu Hari
    return f'''<div class="t" id="tema-{i}" style="background:#FFFCF6;background-image:radial-gradient(rgba(160,120,90,.22) 1.4px,transparent 1.6px);background-size:36px 36px">
  <div class="cv" style="position:absolute;left:80px;top:70px;font-size:76px;font-weight:700;color:#45301F">Catatan satu hari</div>
  <div style="position:absolute;left:84px;top:176px;background:#FDB15D;color:#45301F;font-weight:700;font-size:20px;letter-spacing:.2em;padding:10px 20px;border-radius:40px">SIANG · DI BAWAH KETAPANG</div>
  <div style="position:absolute;left:110px;top:270px;width:860px;height:660px;background:#fff;padding:20px;transform:rotate(1.8deg);box-shadow:0 14px 32px rgba(90,62,49,.2)">
    <div class="ph" style="position:relative;width:100%;height:100%"><img src="{V}cerah.jpg" style="object-position:38% 55%" alt=""></div></div>
  <div style="position:absolute;left:180px;top:250px;width:140px;height:44px;background:rgba(247,167,161,.7);transform:rotate(-8deg)"></div>
  <div style="position:absolute;right:170px;top:250px;width:140px;height:44px;background:rgba(123,167,182,.6);transform:rotate(7deg)"></div>
  <div class="cv" style="position:absolute;left:100px;right:100px;top:990px;font-size:56px;line-height:1.2;color:#4A3426">teh dingin, laut surut,<br>dan aku yang tidak terburu-buru :)</div>
  <div style="position:absolute;right:90px;bottom:60px;font-weight:600;font-size:18px;letter-spacing:.3em;color:#A0603E">HARI 01</div></div>'''

T = [("Adegan Film", film), ("Surat untuk Diriku", surat), ("Palet Warna Selayar", palet), ("Lookbook Editorial", lookbook), ("Catatan Satu Hari", diary)]
solo = "".join(fn(k).replace('class="t"', 'class="t solo"', 1) for k, (_, fn) in enumerate(T, 1))
(H / "tema_preview.html").write_text(f'<!doctype html><html lang="id"><head><meta charset="utf-8">{FONTS}<style>{CSS}</style></head><body>{solo}</body></html>')

# Papan 1 frame: 2 tile besar (rekomendasi) di atas, 3 tile di bawah
def tile(k, x, y, w, rec=False):
    s = w / 1080; h = 1350 * s; name = T[k-1][0]
    badge = '<span style="margin-left:10px;background:#C0592C;color:#FBF4EC;font-weight:700;font-size:11px;letter-spacing:.14em;padding:5px 9px;border-radius:20px;vertical-align:middle">REKOMENDASI</span>' if rec else ""
    return f'''<div style="position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{h:.0f}px;overflow:hidden;border-radius:12px;box-shadow:0 10px 26px rgba(90,62,49,.2)">
    <div style="transform:scale({s:.5f});transform-origin:0 0;width:1080px;height:1350px">{T[k-1][1](k).replace('id="tema-', 'id="mini-')}</div></div>
  <div style="position:absolute;left:{x}px;top:{y + h + 12:.0f}px;width:{w}px"><span style="font-weight:700;font-size:15px;letter-spacing:.12em;color:#C0592C">{k:02d}</span>
    <span class="pf" style="font-size:{26 if rec else 22}px;margin-left:8px">{name}</span>{badge}</div>'''
BOARD = f'''<div class="t" id="board">
  <div style="position:absolute;left:44px;right:44px;top:36px;display:flex;justify-content:space-between;align-items:baseline">
    <div class="pf" style="font-size:44px">5 tema <i style="color:#A0603E">carousel</i></div>
    <div style="font-weight:700;font-size:14px;letter-spacing:.3em;color:#7A5039">CONTOH: GAMBAR 1</div></div>
  {tile(1, 44, 118, 483, True)}{tile(2, 553, 118, 483, True)}
  {tile(3, 44, 846, 315)}{tile(4, 382, 846, 315)}{tile(5, 721, 846, 315)}</div>'''
(H / "tema_board.html").write_text(f'<!doctype html><html lang="id"><head><meta charset="utf-8">{FONTS}<style>{CSS}</style></head><body>{BOARD}</body></html>')
print("ok")
