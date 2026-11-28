"""Gambar katalog WhatsApp Business: Sewa Kayak (1080x1080).
2 item katalog (Kayak Single & Kayak Double, masing-masing 6 gambar) + 1 gambar daftar harga untuk dikirim di chat.
Run: python3 social/build_kayak_wa.py && node social/render_kayak_wa.js -> social/kayak-wa/*.png"""
import pathlib
H = pathlib.Path(__file__).parent
LOGO = "../assets/logo-sunari-color.png"; LOGO_D = "../assets/logo-sunari-color-dark.png"; P = "../assets/photos/"
FONTS = '<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;1,400;1,500&family=Montserrat:wght@500;600;700&display=swap" rel="stylesheet">'
CSS = """
*{margin:0;padding:0;box-sizing:border-box}body{background:#bbb;font-family:Montserrat,sans-serif}
.t{position:relative;overflow:hidden;width:1080px;height:1080px;margin:30px auto;background:#FBF4EC}
.t img.bg{width:100%;height:100%;object-fit:cover}
.lg{position:absolute;left:40px;top:36px;width:230px;filter:drop-shadow(0 2px 8px rgba(0,0,0,.5))}
.lb{position:absolute;left:40px;bottom:40px;background:rgba(251,244,236,.94);border-radius:16px;padding:16px 26px;font-weight:700;font-size:24px;letter-spacing:.18em;text-transform:uppercase;color:#45301F;box-shadow:0 6px 20px rgba(0,0,0,.18)}
.emb{text-shadow:0 1.5px 0 rgba(255,255,255,.85),0 2px 4px rgba(90,62,49,.22)}
.k{font-weight:700;font-size:21px;letter-spacing:.32em;text-transform:uppercase;color:#7A5039}
.pf{font-family:'Playfair Display',serif;color:#45301F}
.pr{position:absolute;right:40px;top:40px;background:linear-gradient(135deg,#FDB15D,#FF8A5C);color:#fff;border-radius:999px;padding:16px 32px;text-align:center;box-shadow:0 8px 24px rgba(90,62,49,.3)}
.pr b{display:block;font-size:44px;letter-spacing:.01em}.pr span{font-size:17px;font-weight:600;letter-spacing:.22em;text-transform:uppercase}
.fx{display:grid;grid-template-columns:1fr 1fr;column-gap:40px;border-top:1.5px solid rgba(138,95,72,.3)}
.fx div{padding:17px 0;border-bottom:1.5px solid rgba(138,95,72,.3);font-size:27px;color:#45301F}
.fx div::before{content:"";display:inline-block;width:10px;height:10px;border-radius:50%;background:linear-gradient(90deg,#FDB15D,#FF8A5C);margin-right:14px;vertical-align:middle}
.frame{position:absolute;inset:32px;border:1.5px solid rgba(138,95,72,.4)}
.ft{position:absolute;left:0;right:0;bottom:62px;text-align:center;font-weight:700;font-size:19px;letter-spacing:.32em;text-transform:uppercase;color:#7A5039}
"""
FX = ["Pelampung (life jacket)", "Dayung", "Air tenang &amp; landai", "Spot senja terbaik", "Foto siluet senja", "Bisa untuk anak*"]

def item(code, name, em, price, sub, cover, cover_pos, photos, people):
    T = [f'''<div class="t" id="wa-kayak-{code}-01">
  <div style="position:absolute;left:0;right:0;top:0;height:760px;overflow:hidden"><img class="bg" src="{P}{cover}" style="object-position:{cover_pos}" alt=""></div>
  <img class="lg" src="{LOGO_D}" alt="">
  <div class="pr"><b>{price}</b><span>per kayak</span></div>
  <div style="position:absolute;left:60px;right:60px;top:800px">
    <div class="k">SunaRi Beach Resort · Selayar</div>
    <div class="pf emb" style="font-size:84px;line-height:1.1;margin-top:10px">{name} <em style="color:#A0603E">{em}</em></div>
    <div style="font-size:28px;color:#4A3426;margin-top:12px">{sub}</div></div></div>''']
    for k, (img, pos, lb) in enumerate(photos, 2):
        T.append(f'''<div class="t" id="wa-kayak-{code}-{k:02d}"><img class="bg" src="{P}{img}" style="object-position:{pos}" alt=""><img class="lg" src="{LOGO_D}" alt=""><div class="lb">{lb}</div></div>''')
    n = len(photos) + 2
    T.append(f'''<div class="t" id="wa-kayak-{code}-{n:02d}"><div class="frame"></div>
  <img src="{LOGO}" style="position:absolute;left:50%;transform:translateX(-50%);top:80px;width:300px" alt="">
  <div style="position:absolute;left:90px;right:90px;top:320px;text-align:center">
    <div class="k">Sewa kayak · Pantai Sunari</div>
    <div class="pf emb" style="font-size:66px;margin:8px 0 6px">{name} <em style="color:#A0603E">{em}</em></div>
    <div class="pf" style="font-size:50px;color:#C8613A;margin-bottom:26px">{price} <span style="font-family:Montserrat;font-size:22px;color:#7A5039;letter-spacing:.2em;text-transform:uppercase">/ kayak</span></div>
    <div class="fx" style="text-align:left">{"".join(f"<div>{x}</div>" for x in FX)}</div>
    <div style="margin-top:26px;font-size:25px;color:#4A3426">{people} · Terbaik 17.00–18.10 WITA</div></div>
  <div class="ft">*Anak wajib didampingi orang dewasa</div></div>''')
    return T

T = []
T += item("single", "Kayak", "Single", "Rp 50.000", "1 orang · Mendayung menyongsong senja",
          "senja/39-kayak-single-samping-1753.jpg", "50% 62%",
          [("senja/03-kayak-matahari-merah.jpg", "50% 0%", "Matahari merah"),
           ("senja/40-kayak-single-belakang-a-1753.jpg", "50% 55%", "Menuju matahari"),
           ("senja/65-kayak-single-matahari-terbenam-1753.jpg", "50% 52%", "Matahari tenggelam"),
           ("senja/68-kayak-pelampung-jalur-cahaya-1748.jpg", "50% 55%", "Jalur cahaya")],
          "Untuk 1 orang")
T += item("double", "Kayak", "Double", "Rp 100.000", "2 orang · Senja untuk berdua",
          "senja/09-kayak-pasangan.jpg", "50% 60%",
          [("senja/17-kayak-berdua.jpg", "50% 60%", "Berdua di atas air"),
           ("senja/18-kayak-berdua-pelampung.jpg", "50% 65%", "Golden hour"),
           ("senja/11-kayak-dan-pulau.jpg", "50% 60%", "Pulau di cakrawala"),
           ("senja/51-kayak-double-jalur-cahaya-1751.jpg", "50% 50%", "Jalur cahaya")],
          "Untuk 2 orang")

# Daftar harga (dikirim di chat / status, bukan item katalog)
def card(name, em, price, who, img, pos):
    return f'''<div style="flex:1;background:#fff;border-radius:22px;overflow:hidden;box-shadow:0 10px 28px rgba(90,62,49,.16)">
  <div style="height:300px;overflow:hidden"><img src="{P}{img}" style="width:100%;height:100%;object-fit:cover;object-position:{pos}" alt=""></div>
  <div style="padding:24px 26px 28px;text-align:center">
    <div class="pf" style="font-size:46px">{name} <em style="color:#A0603E">{em}</em></div>
    <div style="font-size:21px;color:#7A5039;font-weight:600;letter-spacing:.16em;text-transform:uppercase;margin-top:4px">{who}</div>
    <div style="margin-top:16px;display:inline-block;background:linear-gradient(135deg,#FDB15D,#FF8A5C);color:#fff;border-radius:999px;padding:12px 30px;font-weight:700;font-size:36px">{price}</div></div></div>'''
T.append(f'''<div class="t" id="wa-kayak-harga"><div class="frame"></div>
  <img src="{LOGO}" style="position:absolute;left:50%;transform:translateX(-50%);top:62px;width:250px" alt="">
  <div style="position:absolute;left:70px;right:70px;top:218px;text-align:center">
    <div class="k">Daftar harga</div>
    <div class="pf emb" style="font-size:64px;margin-top:4px">Sewa <em style="color:#A0603E">Kayak</em></div></div>
  <div style="position:absolute;left:70px;right:70px;top:372px;display:flex;gap:34px">
    {card("Kayak", "Single", "Rp 50.000", "1 orang", "senja/65-kayak-single-matahari-terbenam-1753.jpg", "50% 64%")}
    {card("Kayak", "Double", "Rp 100.000", "2 orang", "senja/09-kayak-pasangan.jpg", "50% 60%")}</div>
  <div style="position:absolute;left:70px;right:70px;top:905px;text-align:center;font-size:23px;color:#4A3426;line-height:1.5">
    Harga per kayak · Termasuk pelampung &amp; dayung<br>Waktu terbaik 17.00 · Senja ±17.50 · Kembali 18.10 WITA</div>
  <div class="ft" style="bottom:52px;font-size:17px">WhatsApp 0821-8903-3044 · Pantai Sunari, Selayar</div></div>''')

(H / "kayak_wa.html").write_text(f'<!doctype html><html lang="id"><head><meta charset="utf-8">{FONTS}<style>{CSS}</style></head><body>{"".join(T)}</body></html>')
print(len(T))
