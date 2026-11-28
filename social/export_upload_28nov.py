"""Ekspor 8 foto senja terbaik 28 Nov 2026 siap upload, dengan color grading look SunaRi.
  instagram/  1080x1350 (4:5, feed Instagram)
  tiktok/     1080x1920 (9:16, TikTok photo mode, Story, Reels)
Crop dulu, lalu diperkecil (tidak pernah diperbesar bila sumber asli 4000x3000), grading, sedikit sharpening, JPEG q95 4:4:4 tanpa EXIF/lokasi.
Run: python3 social/export_upload_28nov.py [folder_sumber]   (default: assets/photos/senja, 2400 px; file asli kamera lebih tajam)"""
import sys, pathlib, numpy as np
from PIL import Image, ImageOps, ImageFilter
from grade_senja_cerita import rgb2hsv, hsv2rgb
H = pathlib.Path(__file__).resolve().parent
SRC = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else H.parent / "assets/photos/senja"
OUT = H / "upload-28nov"
# file: (kekuatan grading, posisi x crop 4:5, posisi x crop 9:16) — urut prioritas
PICK = {"88-matahari-terbenam-langit-merah.jpg": (.35, .50, .50),
        "85-dua-tamu-bingkai-pohon-tirai.jpg": (.45, .40, .48),
        "92-kamboja-bingkai-matahari-tamu.jpg": (.60, .60, .55),
        "97-gazebo-tirai-pantulan-matahari.jpg": (.70, .60, .70),
        "96-kayak-pulau-awan.jpg": (.80, .50, .38),
        "93-kayak-dua-orang-pastel.jpg": (.80, .60, .62),
        "98-kayak-langit-merah.jpg": (.40, .85, .75),
        "91-tamu-memotret-matahari.jpg": (.50, .36, .90)}
def grade(im, s):
    a = np.asarray(im, float) / 255
    a = np.clip(a * (1 + s * np.array([0.05, 0.0, -0.10])), 0, 1)
    h, sat, v = rgb2hsv(a)
    g = (h > 0.17) & (h < 0.45); h = np.where(g, h - 0.035 * s, h); sat = np.where(g, sat * (1 - 0.22 * s), sat)
    bl = (h > 0.50) & (h < 0.72); sat = np.where(bl, sat * (1 - 0.30 * s), sat)
    o = (h < 0.12) | (h > 0.95); sat = np.where(o, np.clip(sat * (1 + 0.08 * s), 0, 1), sat)
    a = hsv2rgb(h % 1, sat, v)
    L = (0.299 * a[..., 0] + 0.587 * a[..., 1] + 0.114 * a[..., 2])[..., None]
    x = a; a = x + 0.10 * s * (x - x**2) * (2 * x - 1) * -1
    wh = np.clip((L - 0.55) / 0.45, 0, 1); ws = np.clip((0.40 - L) / 0.40, 0, 1)
    a = a * (1 - 0.14 * s * wh) + np.array([1.0, 0.82, 0.58]) * 0.14 * s * wh
    a = a * (1 - 0.22 * s * ws) + np.array([0x3B, 0x28, 0x19]) / 255 * 0.22 * s * ws
    a = 0.025 * s + np.clip(a, 0, 1) * (1 - 0.04 * s)
    return Image.fromarray((np.clip(a, 0, 1) * 255).astype(np.uint8))
def crop(im, W, Hh, px):
    w, h = im.size; cw = round(h * W / Hh)
    if cw > w: ch = round(w * Hh / W); return im.crop((0, (h - ch) // 2, w, (h - ch) // 2 + ch))
    x0 = round((w - cw) * px); return im.crop((x0, 0, x0 + cw, h))
for i, (f, (s, p45, p916)) in enumerate(PICK.items(), 1):
    src = ImageOps.exif_transpose(Image.open(SRC / f)).convert("RGB")
    for sub, (W, Hh, px) in {"instagram": (1080, 1350, p45), "tiktok": (1080, 1920, p916)}.items():
        c = crop(src, W, Hh, px); up = c.width < W
        im = grade(c.resize((W, Hh), Image.LANCZOS), s).filter(ImageFilter.UnsharpMask(1.0, 40, 2))
        (OUT / sub).mkdir(parents=True, exist_ok=True)
        name = f"{i:02d}-{f[3:]}"; im.save(OUT / sub / name, quality=95, subsampling=0, optimize=True)
        print(sub, name, "(diperbesar dari %dpx)" % c.width if up else "")
