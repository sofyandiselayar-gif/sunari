"""Seri konten "Jeda": Storytelling & Slow Living.
Run: python3 social/build_slow.py && node social/render_slow.js  -> social/slow-living/*.png"""
import pathlib
H = pathlib.Path(__file__).parent
WA = "0821-8903-3044"
IG = "@sunaribeachresortselayar"
LOGO = "../assets/logo-sunari-color.png"
LOGO_D = "../assets/logo-sunari-color-dark.png"
P = "../assets/photos/"
FONTS = '<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;1,400;1,500&family=Montserrat:wght@400;500;600&display=swap" rel="stylesheet">'
CSS = """
*{margin:0;padding:0;box-sizing:border-box}
body{background:#bbb;font-family:Montserrat,sans-serif;color:#45301F}
.t{position:relative;overflow:hidden;margin:30px auto;background:#FBF4EC}
.f{width:1080px;height:1350px} .s{width:1080px;height:1920px}
.bg{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.veil{position:absolute;inset:0;background:linear-gradient(180deg,rgba(30,20,14,.38) 0%,rgba(30,20,14,0) 22%,rgba(30,20,14,0) 48%,rgba(30,20,14,.72) 100%)}
.veil.full{background:linear-gradient(180deg,rgba(30,20,14,.45) 0%,rgba(30,20,14,.15) 30%,rgba(30,20,14,.25) 60%,rgba(30,20,14,.75) 100%)}
.logo{position:absolute;left:64px;top:56px;width:230px}
.tag{position:absolute;right:64px;top:84px;font-weight:600;font-size:20px;letter-spacing:.26em;text-transform:uppercase;color:#FBF4EC;opacity:.92}
.txt{position:absolute;left:84px;right:84px;bottom:120px;color:#FBF4EC}
.txt .q{font-family:'Playfair Display',serif;font-weight:400;font-size:70px;line-height:1.16;text-shadow:0 3px 18px rgba(0,0,0,.35)}
.txt .q i{color:#FDB15D}
.txt .p{font-size:32px;line-height:1.55;margin-top:26px;max-width:860px;text-shadow:0 2px 12px rgba(0,0,0,.4)}
.rule{display:block;width:90px;height:2px;background:#FDB15D;margin-bottom:34px}
.ft{position:absolute;left:84px;right:84px;bottom:56px;display:flex;justify-content:space-between;font-weight:600;font-size:18px;letter-spacing:.24em;text-transform:uppercase;color:#FBF4EC;opacity:.85}
.panel{background:rgba(30,20,14,.42);-webkit-backdrop-filter:blur(8px);backdrop-filter:blur(8px);border-radius:40px;padding:70px 50px}
.pf{font-family:'Playfair Display',serif;font-weight:400}
.it{font-style:italic;color:#A67C64}
.caps{font-weight:600;text-transform:uppercase;letter-spacing:.24em;color:#8A5F48}
"""
SUN = '''<svg viewBox="0 0 200 200" width="{w}" height="{w}" style="display:block;margin:0 auto"><defs><linearGradient id="g{u}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FDB15D"/><stop offset="1" stop-color="#FF8A5C"/></linearGradient>
<mask id="m{u}"><rect width="200" height="200" fill="white"/><rect y="112" width="200" height="5"/><rect y="126" width="200" height="7"/><rect y="142" width="200" height="9"/><rect y="160" width="200" height="11"/><rect y="180" width="200" height="13"/></mask></defs>
<circle cx="100" cy="100" r="96" fill="url(#g{u})" mask="url(#m{u})"/></svg>'''
T = []

def photo(tid, img, pos, q, p="", tag="", fmt="f", veil="veil", foot=""):
    T.append(f'''<div class="t {fmt}" id="{tid}"><img class="bg" src="{P}{img}" style="object-position:{pos}" alt=""><div class="{veil}"></div>
  <img class="logo" src="{LOGO_D}" alt=""><div class="tag">{tag}</div>
  <div class="txt"{' style="bottom:380px"' if fmt == "s" else ""}><span class="rule"></span><div class="q">{q}</div>{f'<div class="p">{p}</div>' if p else ''}</div>
  <div class="ft"{' style="bottom:250px"' if fmt == "s" else ""}><span>{foot or "SunaRi · Selayar"}</span><span>{IG}</span></div></div>''')

# ---------------------------------------------------------------- A. Carousel "Kapan terakhir kali kamu berhenti?"
CA = [
 ("pantai/04-kursi-santai-bawah-pohon.jpg", "50% 60%", "Kapan terakhir kali kamu benar-benar <i>berhenti?</i>", "Bukan sekadar libur. Benar-benar berhenti, tanpa daftar yang harus diselesaikan."),
 ("pantai/02-perahu-nelayan-biru.jpg", "50% 60%", "Pagi tidak harus <i>dikejar.</i>", "Laut di depan Pantai Sunari bergerak pelan. Kamu boleh ikut pelan."),
 ("pantai/03-pulau-di-seberang.jpg", "50% 55%", "Istirahatkan matamu di garis <i>cakrawala.</i>", "Pulau Gusung di seberang tidak ke mana-mana. Begitu juga waktumu hari ini."),
 ("senja/05-tamu-di-meja.jpg", "50% 55%", "Duduk tanpa tujuan juga termasuk <i>rencana.</i>", "Angin laut, meja kayu, dan tidak ada yang perlu dibalas sekarang."),
 ("senja/29-dua-kursi-menghadap-senja.jpg", "50% 55%", "Dua kursi, satu senja, percakapan yang tidak <i>terburu&#8209;buru.</i>", "Kapan terakhir kali kamu bicara tanpa melirik jam?"),
 ("senja/21-siluet-tamu-tepi-pantai.jpg", "50% 60%", "Orang tersayang tidak butuh agenda. Mereka butuh <i>waktumu.</i>", ""),
 ("senja/28-matahari-di-bawah-daun.jpg", "50% 45%", "Saat matahari turun, biarkan lelahmu ikut <i>tenggelam.</i>", "Besok bisa dimulai lagi, dengan napas yang lebih panjang."),
]
for i, (img, pos, q, p) in enumerate(CA, 1):
    photo(f"jeda-carousel-{i:02d}", img, pos, q, p, tag=f"Jeda · {i:02d} / 08", veil="veil full" if i == 1 else "veil")
T.append(f'''<div class="t f" id="jeda-carousel-08"><img src="{LOGO}" style="position:absolute;left:50%;transform:translateX(-50%);top:110px;width:330px" alt="">
  <div style="position:absolute;left:100px;right:100px;top:430px;text-align:center">{SUN.format(w=96, u="c8")}
    <div class="pf" style="font-size:80px;line-height:1.12;margin-top:40px">Ambil jeda.<br><span class="it">Bernapaslah.</span></div>
    <div style="font-size:33px;line-height:1.6;margin-top:34px">Senja akan selalu menunggumu<br>di Pantai Sunari, Selayar.</div>
    <div class="caps" style="font-size:20px;margin-top:70px">Reservasi &amp; info</div>
    <div class="pf" style="font-size:54px;margin-top:10px">WhatsApp {WA}</div></div>
  <div style="position:absolute;left:84px;right:84px;bottom:56px;display:flex;justify-content:space-between" class="caps"><span style="font-size:18px">SunaRi · Selayar</span><span style="font-size:18px">Jeda · 08 / 08</span></div></div>''')

# ---------------------------------------------------------------- B. 6 post "Catatan Jeda"
CJ = [
 ("aktivitas/05-ayunan-raksasa-senja.jpg", "40% 55%", "Ayunkan kakimu, lepaskan <i>bebanmu.</i>"),
 ("senja/24-pohon-tepi-pantai-senja.jpg", "50% 50%", "Pohon pun meluruhkan daunnya, lalu tumbuh <i>kembali.</i>"),
 ("senja/27-tamu-dan-pohon-kelapa.jpg", "50% 45%", "Abadikan sebentar. Sisanya, nikmati dengan <i>matamu sendiri.</i>"),
 ("senja/17-kayak-berdua.jpg", "50% 55%", "Mendayung bersama, tanpa harus sampai <i>ke&nbsp;mana&#8209;mana.</i>"),
 ("malam/09-lilin-di-meja.jpg", "50% 55%", "Malam yang pelan, cahaya yang hangat, cerita yang <i>belum selesai.</i>"),
 ("senja/22-ranting-dan-matahari.jpg", "50% 60%", "Hal kecil, bila dilihat pelan&#8209;pelan, ternyata <i>indah.</i>"),
]
for i, (img, pos, q) in enumerate(CJ, 1):
    photo(f"catatan-jeda-{i:02d}", img, pos, q, tag=f"Catatan Jeda · {i:02d}")

# ---------------------------------------------------------------- C. 3 story interaktif
photo("story-jeda-1", "senja/14-daun-matahari-story.jpg", "50% 50%", "Hei, kamu yang sedang <i>lelah.</i>",
      "Berhenti sebentar di story ini, ya. Satu menit saja untuk dirimu sendiri.", tag="Jeda sejenak", fmt="s", veil="veil full", foot="Ketuk untuk lanjut →")
T.append(f'''<div class="t s" id="story-jeda-2"><img class="bg" src="{P}senja/23-pohon-meranggas-senja.jpg" style="object-position:50% 55%" alt=""><div class="veil full"></div>
  <img class="logo" src="{LOGO_D}" alt=""><div class="tag">Jeda sejenak</div>
  <div class="panel" style="position:absolute;left:72px;right:72px;top:380px;text-align:center;color:#FBF4EC">
    <div class="pf" style="font-size:76px;line-height:1.15;text-shadow:0 3px 18px rgba(0,0,0,.4)">Ayo bernapas<br><i style="color:#FDB15D">bersama.</i></div>
    {"".join(f'<div style="margin-top:{70 if k == 0 else 44}px"><div style="font-weight:600;font-size:24px;letter-spacing:.26em;text-transform:uppercase;color:#FDB15D">{a}</div><div class="pf" style="font-size:56px;margin-top:8px;text-shadow:0 2px 14px rgba(0,0,0,.4)">{b}</div></div>' for k, (a, b) in enumerate([("Tarik napas", "4 detik"), ("Tahan", "4 detik"), ("Hembuskan perlahan", "6 detik")]))}
    <div style="font-size:32px;line-height:1.55;margin-top:70px;text-shadow:0 2px 12px rgba(0,0,0,.45)">Ulangi tiga kali.<br>Rasakan bahumu turun pelan-pelan.</div></div>
  <div class="ft" style="bottom:240px"><span>SunaRi · Selayar</span><span>{IG}</span></div></div>''')
T.append(f'''<div class="t s" id="story-jeda-3"><img class="bg" src="{P}senja/29-dua-kursi-menghadap-senja.jpg" style="object-position:50% 55%" alt=""><div class="veil full"></div>
  <img class="logo" src="{LOGO_D}" alt=""><div class="tag">Jeda sejenak</div>
  <div class="panel" style="position:absolute;left:72px;right:72px;top:560px;text-align:center;color:#FBF4EC">
    <div class="pf" style="font-size:74px;line-height:1.15;text-shadow:0 3px 18px rgba(0,0,0,.4)">Dengan siapa kamu ingin menikmati <i style="color:#FDB15D">senja berikutnya?</i></div>
    <div style="margin:80px auto 0;width:760px;height:380px;border-radius:36px;border:3px dashed rgba(251,244,236,.7);display:flex;align-items:center;justify-content:center">
      <span style="font-weight:600;font-size:22px;letter-spacing:.24em;text-transform:uppercase;opacity:.85">Tempel stiker polling di sini</span></div>
    <div style="font-size:30px;line-height:1.55;margin-top:50px;text-shadow:0 2px 12px rgba(0,0,0,.45)">Tag orangnya di DM, mungkin mereka juga butuh jeda.</div></div>
  <div class="ft" style="bottom:240px"><span>SunaRi · Selayar</span><span>WA {WA}</span></div></div>''')

(H / "slow.html").write_text(f'<!doctype html><html lang="id"><head><meta charset="utf-8">{FONTS}<style>{CSS}</style></head><body>{"".join(T)}</body></html>')
print(len(T), "desain")
