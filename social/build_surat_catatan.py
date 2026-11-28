"""Dua carousel versi tamu (tanpa logo & WhatsApp), 10 slide 1080x1350, render HD 2x = 2160x2700:
  - "Surat untuk Diriku"  (tema 2, grading Earthy Beige)  -> social/surat/
  - "Catatan Satu Hari"   (tema 5, grading Bright & Airy) -> social/catatan/
Run: python3 social/grade_variasi.py semua earthy,cerah && python3 social/build_surat_catatan.py && node social/render_surat_catatan.js"""
import pathlib
H = pathlib.Path(__file__).parent
V = "../assets/photos/graded/variasi/"
FONTS = ('<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;1,400'
         '&family=Montserrat:wght@500;600;700&family=Caveat:wght@500;600;700&display=swap" rel="stylesheet">')
CSS = """
*{margin:0;padding:0;box-sizing:border-box}body{background:#bbb;font-family:Montserrat,sans-serif}
.t{position:relative;overflow:hidden;width:1080px;height:1350px;margin:30px auto;color:#45301F}
.cv{font-family:Caveat,cursive}
.pol{position:absolute;background:#fff;padding:20px;box-shadow:0 16px 34px rgba(90,62,49,.22)}
.pol img{width:100%;height:100%;object-fit:cover;display:block}
.tape{position:absolute;width:150px;height:44px}
.paper{background:#F4ECDF;background-image:repeating-linear-gradient(0deg,transparent 0 63px,rgba(160,120,90,.16) 63px 64px)}
.dots{background:#FFFCF6;background-image:radial-gradient(rgba(160,120,90,.22) 1.4px,transparent 1.6px);background-size:36px 36px}
.note{position:absolute;font-family:Caveat,cursive;font-weight:500;color:#4A3426}
.pg{position:absolute;left:0;right:0;bottom:44px;text-align:center;font-family:Caveat,cursive;font-size:36px;color:#A0603E}
"""
def pol(img, pos, x, y, w, h, rot, style, tape=None):
    tp = ""
    if tape:
        tx, ty, tr, tc = tape
        tp = f'<div class="tape" style="left:{tx}px;top:{ty}px;transform:rotate({tr}deg);background:{tc}"></div>'
    return (f'<div class="pol" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;transform:rotate({rot}deg)">'
            f'<img src="{V}{img}__{style}.jpg" style="object-position:{pos}" alt=""></div>{tp}')

# ---------- Tema 2: Surat untuk Diriku (Earthy Beige) ----------
E = "earthy"; TP = "rgba(230,200,155,.78)"
def s_top(k, img, pos, text, rot=-2):      # foto atas, tulisan bawah
    return f'''<div class="t paper" id="surat-{k:02d}">{pol(img, pos, 130, 100, 820, 640, rot, E, (465, 76, 3, TP))}
  <div class="note" style="left:120px;right:110px;top:810px;font-size:60px;line-height:1.16">{text}</div><div class="pg">— {k:02d} —</div></div>'''
def s_bot(k, img, pos, text, rot=2):       # tulisan atas, foto bawah
    return f'''<div class="t paper" id="surat-{k:02d}"><div class="note" style="left:120px;right:110px;top:100px;font-size:60px;line-height:1.16">{text}</div>
  {pol(img, pos, 130, 520, 820, 640, rot, E, (470, 496, -3, TP))}<div class="pg">— {k:02d} —</div></div>'''
def s_two(k, a, pa, b, pb, text):
    return f'''<div class="t paper" id="surat-{k:02d}">{pol(a, pa, 80, 100, 500, 640, -4, E, (250, 78, -6, TP))}
  {pol(b, pb, 500, 250, 500, 640, 3, E, (690, 230, 4, TP))}
  <div class="note" style="left:110px;right:110px;top:1000px;font-size:58px;line-height:1.16">{text}</div><div class="pg">— {k:02d} —</div></div>'''
SURAT = [
    f'''<div class="t paper" id="surat-01">{pol("01-duduk-meja-pantai-surut", "35% 55%", 150, 110, 780, 600, -2.5, E, (470, 86, 3, TP))}
  <div class="note" style="left:110px;right:110px;top:790px;font-size:68px;line-height:1.14">Untukku,<br>yang akhirnya berani<br>berhenti sejenak...</div>
  <div class="note" style="right:110px;top:1150px;font-size:46px;color:#A0603E">— aku, di Pantai Sunari</div>
  <div style="position:absolute;right:70px;bottom:52px;font-weight:600;font-size:17px;letter-spacing:.3em;color:#A0603E">GESER →</div></div>''',
    s_top(2, "04-depan-bungalow-tersenyum", "50% 40%", "Ingat pagi itu?<br>Kamu keluar dari rumah kayu<br>tanpa membawa daftar apa pun."),
    s_bot(3, "09-profil-kerudung-palem", "42% 40%", "Angin laut menyentuh kerudungmu,<br>dan untuk pertama kalinya<br>kamu tidak terburu-buru."),
    s_two(4, "07-bougenvil-menengadah", "30% 40%", "08-bougenvil-tersenyum", "70% 35%", "Kamu menengadah lama sekali.<br>Lalu tersenyum, tanpa perlu alasan."),
    s_top(5, "10-berjalan-pantai-surut", "66% 55%", "Laut sedang surut. Kamu belajar,<br>yang pergi tidak selalu hilang.<br>Ia akan kembali.", 2),
    s_two(6, "03-nasi-goreng-teh-dingin", "60% 55%", "06-ponsel-di-meja", "40% 60%", "Teh dingin, nasi goreng, kerupuk.<br>Kamu memotretnya sekali,<br>lalu menyimpan ponsel."),
    s_bot(7, "02-duduk-meja-dekat", "30% 50%", "Kamu duduk lama di bawah ketapang,<br>membiarkan laut yang bercerita.", -2),
    s_top(8, "11-ayunan-dekat-langit", "30% 40%", "Di ayunan itu kamu tertawa,<br>seperti anak kecil<br>yang lupa caranya khawatir."),
    s_bot(9, "12-ayunan-lebar-laut", "46% 50%", "Jadi, kalau suatu hari kamu lelah lagi,<br>ingat hari ini. Ingat rasanya ringan.", 2),
    f'''<div class="t paper" id="surat-10">{pol("05-depan-bungalow-tangga", "52% 45%", 560, 120, 430, 560, 4, E, (700, 96, 6, TP))}
  <div class="note" style="left:110px;top:150px;width:430px;font-size:58px;line-height:1.18">Terima kasih<br>sudah merawat<br>dirimu hari ini.</div>
  <div class="note" style="left:110px;right:110px;top:800px;font-size:60px;line-height:1.18">Sampai jumpa lagi<br>di tempat yang membuatmu<br>pulang dengan hati ringan.</div>
  <div class="note" style="right:110px;top:1110px;font-size:54px;color:#A0603E">Peluk hangat,<br>aku, di Pantai Sunari</div></div>''']

# ---------- Tema 5: Catatan Satu Hari (Bright & Airy) ----------
C = "cerah"; PK = "rgba(247,167,161,.72)"; BL = "rgba(123,167,182,.6)"; YL = "rgba(253,177,93,.7)"
def head(k):
    return (f'<div class="cv" style="position:absolute;left:80px;top:56px;font-size:50px;font-weight:700">Catatan satu hari</div>'
            f'<div style="position:absolute;right:80px;top:76px;font-weight:600;font-size:17px;letter-spacing:.3em;color:#A0603E">{k:02d} / 10</div>')
def pill(txt, top=140, bg="#FDB15D"):
    return f'<div style="position:absolute;left:84px;top:{top}px;background:{bg};color:#45301F;font-weight:700;font-size:19px;letter-spacing:.2em;padding:9px 18px;border-radius:40px">{txt}</div>'
def c_one(k, label, img, pos, text, rot=1.8):
    return f'''<div class="t dots" id="catatan-{k:02d}">{head(k)}{pill(label)}
  {pol(img, pos, 110, 240, 860, 700, rot, C)}
  <div class="tape" style="left:180px;top:220px;transform:rotate(-8deg);background:{PK}"></div><div class="tape" style="right:170px;top:220px;transform:rotate(7deg);background:{BL}"></div>
  <div class="note" style="left:100px;right:100px;top:1010px;font-size:58px;line-height:1.18">{text}</div></div>'''
def c_two(k, label, a, pa, b, pb, text):
    return f'''<div class="t dots" id="catatan-{k:02d}">{head(k)}{pill(label)}
  {pol(a, pa, 80, 240, 470, 600, -3, C)}{pol(b, pb, 530, 300, 470, 600, 2.5, C)}
  <div class="tape" style="left:230px;top:222px;transform:rotate(-6deg);background:{YL}"></div><div class="tape" style="left:700px;top:282px;transform:rotate(5deg);background:{PK}"></div>
  <div class="note" style="left:100px;right:100px;top:1000px;font-size:56px;line-height:1.18">{text}</div></div>'''
CHECK = ["bangun tanpa alarm", "jalan-jalan di taman bunga", "lihat laut surut dari dekat", "es teh di bawah ketapang", "main ayunan sampai puas"]
CATATAN = [
    f'''<div class="t dots" id="catatan-01">
  <div class="cv" style="position:absolute;left:80px;top:70px;font-size:120px;font-weight:700;line-height:1">Catatan<br>satu hari</div>
  <div class="cv" style="position:absolute;left:84px;top:330px;font-size:58px;color:#A0603E">yang berjalan pelan.</div>
  {pol("04-depan-bungalow-tersenyum", "50% 40%", 560, 90, 420, 520, 4, C)}
  {pol("08-bougenvil-tersenyum", "70% 35%", 90, 500, 470, 560, -4, C)}
  {pol("11-ayunan-dekat-langit", "30% 40%", 560, 640, 430, 540, 3, C)}
  <div class="tape" style="left:700px;top:70px;transform:rotate(6deg);background:{PK}"></div>
  <div class="tape" style="left:240px;top:480px;transform:rotate(-7deg);background:{BL}"></div>
  <div class="tape" style="left:700px;top:620px;transform:rotate(-4deg);background:{YL}"></div>
  <div style="position:absolute;left:84px;bottom:110px;font-weight:600;font-size:19px;letter-spacing:.3em;color:#7A5039">PANTAI SUNARI · SELAYAR</div>
  <div style="position:absolute;right:80px;bottom:56px;font-weight:600;font-size:17px;letter-spacing:.3em;color:#A0603E">GESER →</div></div>''',
    c_one(2, "PAGI · BUNGALOW KAYU", "05-depan-bungalow-tangga", "52% 45%", "bangun tanpa alarm. buka pintu,<br>langsung disambut daun palem."),
    c_one(3, "PAGI · DI TAMAN", "09-profil-kerudung-palem", "42% 40%", "udara pagi, angin laut,<br>dan wangi daun. pelan-pelan saja.", -1.8),
    c_one(4, "PAGI · TAMAN BOUGENVIL", "07-bougenvil-menengadah", "30% 45%", "bougenvil di mana-mana,<br>warnanya kayak permen."),
    c_one(5, "MENJELANG SIANG · PANTAI", "10-berjalan-pantai-surut", "66% 55%", "laut lagi surut. karangnya kelihatan,<br>airnya bening banget.", -1.8),
    c_one(6, "SIANG · DI BAWAH KETAPANG", "01-duduk-meja-pantai-surut", "35% 55%", "cari meja paling teduh,<br>pesan es teh. selesai."),
    c_two(7, "SIANG · MAKAN SIANG", "03-nasi-goreng-teh-dingin", "60% 55%", "06-ponsel-di-meja", "40% 60%", "menu: nasi goreng, kerupuk, es teh.<br>foto sekali, terus HP disimpan."),
    c_one(8, "SIANG · LIHAT LAUT", "02-duduk-meja-dekat", "30% 50%", "duduk lama, lihat laut.<br>tidak ada yang perlu dikejar.", -1.8),
    c_one(9, "SORE · AYUNAN", "12-ayunan-lebar-laut", "46% 50%", "terakhir: main ayunan!<br>rasanya kayak terbang."),
]
# Foto unik dalam seri: cover memakai 04, 08, 11; slide isi memakai 9 foto lainnya.
ck = "".join(f'<div style="display:flex;align-items:center;gap:22px;margin-bottom:34px"><div style="width:46px;height:46px;border:3px solid #45301F;border-radius:6px;position:relative;flex:none"><div class="cv" style="position:absolute;left:4px;top:-30px;font-size:64px;color:#C0592C;font-weight:700">✓</div></div><span>{c}</span></div>' for c in CHECK)
CATATAN.append(f'''<div class="t dots" id="catatan-10">{head(10)}{pill("MALAM · SEBELUM TIDUR", bg="#7BA7B6")}
  <div class="cv" style="position:absolute;left:84px;top:250px;font-size:72px;font-weight:700">hari ini sudah:</div>
  <div class="note" style="left:90px;right:90px;top:400px;font-size:64px;line-height:1.1">{ck}</div>
  <div class="cv" style="position:absolute;left:84px;top:1040px;font-size:90px;font-weight:700;color:#C0592C">hari yang sempurna :)</div>
  <div style="position:absolute;left:84px;bottom:70px;font-weight:600;font-size:19px;letter-spacing:.3em;color:#7A5039">PANTAI SUNARI · SELAYAR</div></div>''')

for name, slides in (("surat", SURAT), ("catatan", CATATAN)):
    (H / f"{name}.html").write_text(f'<!doctype html><html lang="id"><head><meta charset="utf-8">{FONTS}<style>{CSS}</style></head><body>{"".join(slides)}</body></html>')
    print(name, len(slides))
