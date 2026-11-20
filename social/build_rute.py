"""Story "Rute ke SunaRi" (1080x1920) di atas peta assets/maps/.
Run: python3 social/build_rute.py && node social/render_rute.js  -> social/story-rute/*.png"""
import pathlib
H = pathlib.Path(__file__).parent
WA = "0821-8903-3044"
IG = "@sunaribeachresortselayar"
LOGO_D = "../assets/logo-sunari-color-dark.png"
M = "../assets/maps/"
FONTS = '<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;1,400;1,500&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">'
CSS = """
*{margin:0;padding:0;box-sizing:border-box}
body{background:#bbb;font-family:'Plus Jakarta Sans',sans-serif;color:#45301F}
.s{width:1080px;height:1920px;position:relative;overflow:hidden;margin:30px auto;background:#123a63}
.map{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.logo{position:absolute;left:64px;top:96px;width:300px;filter:drop-shadow(0 2px 10px rgba(0,0,0,.35))}
.tag{position:absolute;left:72px;top:262px;font-weight:700;font-size:20px;letter-spacing:.26em;text-transform:uppercase;color:#FBF4EC;opacity:.9;text-shadow:0 1px 8px rgba(0,0,0,.4)}
.card{position:absolute;left:56px;right:56px;bottom:250px;background:rgba(251,244,236,.96);border-radius:40px;padding:42px 48px 40px;box-shadow:0 24px 60px rgba(0,0,0,.30)}
.eyebrow{font-weight:700;font-size:20px;letter-spacing:.26em;text-transform:uppercase;color:#8A5F48;display:flex;align-items:center;gap:14px}
.num{width:52px;height:52px;border-radius:50%;color:#fff;display:inline-flex;align-items:center;justify-content:center;font-family:'Playfair Display',serif;font-size:28px;letter-spacing:0}
.h{font-family:'Playfair Display',serif;font-weight:500;font-size:64px;line-height:1.1;margin-top:14px}
.h i{color:#A67C64}
.p{font-size:30px;line-height:1.5;margin-top:16px;color:rgba(69,48,31,.85)}
.rows{margin-top:22px;border-top:1px solid rgba(90,62,49,.16)}
.row{display:flex;justify-content:space-between;align-items:baseline;gap:20px;padding:15px 0;border-bottom:1px solid rgba(90,62,49,.16);font-size:29px;line-height:1.3}
.row:last-child{border-bottom:none}
.row span:first-child{font-weight:600}
.row span:last-child{flex:none;font-weight:700;color:#E07A4B}
.foot{display:flex;justify-content:space-between;margin-top:22px;font-weight:600;font-size:18px;letter-spacing:.22em;text-transform:uppercase;color:#8A5F48}
.compact{padding:30px 40px 28px}
.compact .eyebrow{font-size:18px}
.compact .h{font-size:50px;margin-top:10px}
.compact .row{font-size:27px;padding:11px 0}
.compact .rows{margin-top:14px}
.compact .p{font-size:25px;margin-top:10px}
.compact .num{width:44px;height:44px;font-size:24px}
.sticker{margin-top:24px;height:150px;border-radius:30px;border:3px dashed rgba(224,122,75,.75);display:flex;align-items:center;justify-content:center;font-weight:700;font-size:20px;letter-spacing:.22em;text-transform:uppercase;color:#C0592C;background:rgba(253,177,93,.08)}
"""
C = {1: "#E8674A", 2: "#2B8289", 3: "#D8932D"}
S = []
def story(i, mp, inner, tag="Rute ke SunaRi", bottom=210, foot=True, cls=""):
    f = f'<div class="foot"><span>{i:02d} / 07</span><span>{IG}</span></div>' if foot else ""
    S.append(f'''<div class="s" id="rute-{i:02d}"><img class="map" src="{M}{mp}" alt="">
  <img class="logo" src="{LOGO_D}" alt=""><div class="tag">{tag}{"" if foot else f" · {i:02d}/07"}</div>
  <div class="card {cls}" style="bottom:{bottom}px">{inner}{f}</div></div>''')
rows = lambda rs: '<div class="rows">' + "".join(f'<div class="row"><span>{a}</span><span>{b}</span></div>' for a, b in rs) + "</div>"
num = lambda n: f'<span class="num" style="background:{C[n]}">{n}</span>'

story(1, "01_indonesia.png", '''<div class="eyebrow">Travel guide · Selayar</div>
  <div class="h" style="font-size:96px">Rute ke <i>SunaRi</i></div>
  <div class="p">Pulau Selayar, di ujung selatan Sulawesi. Ketuk untuk melihat jalannya →</div>''', bottom=330)
story(2, "02_sulawesi.png", '''<div class="eyebrow">Sulawesi Selatan</div>
  <div class="h" style="font-size:54px">Dari Makassar, <i>selangkah lagi</i></div>
  <div class="p" style="font-size:27px">Pulau Selayar ada di Laut Flores, di seberang Bira. Bisa lewat udara maupun laut.</div>''', cls="compact", bottom=200)
story(3, "03_tiga_rute.png", f'''<div class="eyebrow">Pilih jalanmu</div>
  <div class="h">Tiga rute <i>menuju senja</i></div>
  <div class="rows">
    <div class="row"><span>{num(1)}&nbsp; Udara</span><span>tercepat</span></div>
    <div class="row"><span>{num(2)}&nbsp; Darat &amp; feri</span><span>scenic route</span></div>
    <div class="row"><span>{num(3)}&nbsp; Kapal langsung</span><span>tanpa transit</span></div></div>''', cls="compact", foot=False, bottom=200)
story(4, "04_rute1_pesawat.png", f'''<div class="eyebrow">{num(1)} Opsi 1 · Jalur udara</div>
  {rows([("Makassar → Bandara H. Aroeppala", "±45 menit"), ("Bandara → SunaRi (mobil)", "±10–15 menit")])}
  <div class="p">Jadwal penerbangan menyesuaikan maskapai, cek H-7.</div>''', cls="compact", foot=False, bottom=200)
story(5, "05_rute2_darat_feri.png", f'''<div class="eyebrow">{num(2)} Opsi 2 · Darat &amp; feri</div>
  {rows([("Terminal Malengkeri → Bira", "±4–5 jam"), ("Feri Bira → Pamatata (ASDP)", "±2 jam"), ("Pamatata → SunaRi (mobil)", "±1–1,5 jam")])}''', cls="compact", foot=False, bottom=200)
story(6, "06_rute3_kapal_laut.png", f'''<div class="eyebrow">{num(3)} Opsi 3 · Kapal langsung</div>
  {rows([("KM Dharma Kartika III → Benteng", "±10–11 jam"), ("Benteng → SunaRi (mobil)", "±20–30 menit")])}
  <div class="p">Berangkat malam, tiba pagi · tidak setiap hari.</div>''', cls="compact", foot=False, bottom=200)
story(7, "07_pulau_selayar.png", f'''<div class="eyebrow">Sampai di Selayar</div>
  <div class="h" style="font-size:58px">Kami <i>jemput</i> Anda</div>
  <div class="p" style="font-size:28px">Dari Bandara Aroeppala, Pelabuhan Pamatata &amp; Benteng (berbayar). Kabari jadwal kedatangan via WhatsApp <b>{WA}</b>.</div>
  <div class="sticker">Tempel stiker tautan WhatsApp</div>''', bottom=210)

(H / "rute.html").write_text(f'<!doctype html><html lang="id"><head><meta charset="utf-8">{FONTS}<style>{CSS}</style></head><body>{"".join(S)}</body></html>')
print(len(S), "story")
