"""Sampul (cover) profil WhatsApp Business: mozaik semua foto senja layak pakai + logo di tengah.
Ukuran 1211x681 (16:9), dirender 2x = 2422x1362.
Run: python3 social/build_wa_cover.py && node social/render_wa_cover.js -> social/wa-cover/"""
import glob, os, pathlib
import numpy as np
from PIL import Image, ImageOps, ImageFilter
H = pathlib.Path(__file__).parent; S = H.parent / "assets/photos/senja"
# dikecualikan: cap tanggal (01, 02, 02b, 26), wajah/anak/botol (58, 62, 63, 69), duplikat mirip (41, 43, 46, 61, 67),
# orang terlalu dekat (13, 34) supaya pas 55 kotak
EX = {"01", "02", "02b", "26", "58", "62", "63", "69", "61", "67", "41", "43", "46", "13", "34"}
items = []
for f in sorted(glob.glob(str(S / "*.jpg"))):
    n = os.path.basename(f)
    if n.split("-")[0] in EX: continue
    im = ImageOps.exif_transpose(Image.open(f)).convert("RGB"); im.thumbnail((200, 200))
    a = np.asarray(im.filter(ImageFilter.GaussianBlur(6)).convert("L"), float)
    y, x = np.unravel_index(a.argmax(), a.shape)
    items.append((n, round(100 * x / a.shape[1]), round(100 * y / a.shape[0]), float(np.asarray(im.convert("L")).mean())))
COLS, ROWS = 11, 5; CARD = set()
cells = sorted([(r, c) for r in range(ROWS) for c in range(COLS) if (r, c) not in CARD], key=lambda rc: (rc[0] + rc[1], rc[0]))
assert len(cells) == len(items), (len(cells), len(items))
items.sort(key=lambda t: -t[3])  # terang (golden hour) di kiri atas -> gelap (afterglow) di kanan bawah
tiles = "".join(f'<img src="../assets/photos/senja/{n}" style="grid-row:{r+1};grid-column:{c+1};object-position:{px}% {py}%" alt="">'
                for (n, px, py, _), (r, c) in zip(items, cells))
LOGO = "../assets/logo-sunari-color.png"
html = f'''<!doctype html><html lang="id"><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;1,400&family=Montserrat:wght@600;700&display=swap" rel="stylesheet">
<style>*{{margin:0;padding:0;box-sizing:border-box}}body{{background:#bbb}}
#wa-cover{{position:relative;width:1211px;height:681px;margin:20px auto;display:grid;grid-template-columns:repeat({COLS},1fr);grid-template-rows:repeat({ROWS},1fr);gap:2px;background:#FBF4EC;padding:2px}}
#wa-cover img{{width:100%;height:100%;object-fit:cover;display:block;min-height:0;min-width:0}}
.lgm{{position:absolute;left:50%;top:44%;transform:translate(-50%,-50%);width:600px!important;height:auto!important;object-fit:contain!important}}
.tg{{font-family:'Playfair Display',serif;font-style:italic;font-size:22px;color:#45301F;margin-top:8px;text-shadow:0 1px 0 #fff}}
.ln{{width:60px;height:2px;background:linear-gradient(90deg,#FDB15D,#FF8A5C);margin:12px auto}}
.sm{{font-family:Montserrat,sans-serif;font-weight:700;font-size:10.5px;letter-spacing:.3em;text-transform:uppercase;color:#7A5039}}
</style></head><body><div id="wa-cover">{tiles}
<img class="lgm" src="../assets/logo-sunari-sunset-halo.png" alt=""></div></body></html>'''
(H / "wa_cover.html").write_text(html); print(len(items), "foto")
