"""Color grading profesional untuk carousel "Senja Hari Ini" -> assets/photos/graded/senja__*.jpg (foto asli tidak diubah).
Look SunaRi: highlight keemasan, bayangan cokelat (Driftwood Deep), hitam sedikit terangkat, hijau ke zaitun, biru dilembutkan.
Run: python3 social/grade_senja_cerita.py"""
from PIL import Image, ImageOps
import numpy as np, colorsys, pathlib
R = pathlib.Path(__file__).resolve().parent.parent / "assets/photos"
def rgb2hsv(a):
    mx = a.max(-1); mn = a.min(-1); d = mx - mn + 1e-6; v = mx; s = np.where(mx > 0, (mx - mn) / (mx + 1e-6), 0)
    r, g, b = a[..., 0], a[..., 1], a[..., 2]
    h = np.where(mx == r, ((g - b) / d) % 6, np.where(mx == g, (b - r) / d + 2, (r - g) / d + 4)) / 6
    return h, s, v
def hsv2rgb(h, s, v):
    i = np.floor(h * 6) % 6; f = h * 6 - np.floor(h * 6); p = v * (1 - s); q = v * (1 - f * s); t = v * (1 - (1 - f) * s)
    out = np.zeros(h.shape + (3,))
    for k, (x, y, z) in enumerate([(v, t, p), (q, v, p), (p, v, t), (p, q, v), (t, p, v), (v, p, q)]):
        m = i == k; out[m] = np.stack([x[m], y[m], z[m]], -1)
    return out
def grade(src, s):
    im = ImageOps.exif_transpose(Image.open(R / src)).convert("RGB"); im.thumbnail((1800, 1800))
    a = np.asarray(im, float) / 255
    a = a * (1 + s * np.array([0.05, 0.0, -0.10]))                          # white balance hangat
    a = np.clip(a, 0, 1)
    h, sat, v = rgb2hsv(a)
    g = (h > 0.17) & (h < 0.45)                                             # hijau -> zaitun, sedikit redup
    h = np.where(g, h - 0.035 * s, h); sat = np.where(g, sat * (1 - 0.22 * s), sat)
    bl = (h > 0.50) & (h < 0.72)                                            # biru -> lebih lembut
    sat = np.where(bl, sat * (1 - 0.30 * s), sat)
    o = (h < 0.12) | (h > 0.95)                                             # oranye/merah sedikit diperkaya
    sat = np.where(o, np.clip(sat * (1 + 0.08 * s), 0, 1), sat)
    a = hsv2rgb(h % 1, sat, v)
    L = (0.299 * a[..., 0] + 0.587 * a[..., 1] + 0.114 * a[..., 2])[..., None]
    x = a; a = x + 0.10 * s * (x - x**2) * (2 * x - 1) * -1                 # S-curve lembut
    wh = np.clip((L - 0.55) / 0.45, 0, 1); ws = np.clip((0.40 - L) / 0.40, 0, 1)
    a = a * (1 - 0.14 * s * wh) + np.array([1.0, 0.82, 0.58]) * 0.14 * s * wh      # highlight keemasan
    a = a * (1 - 0.22 * s * ws) + np.array([0x3B, 0x28, 0x19]) / 255 * 0.22 * s * ws  # bayangan cokelat
    a = 0.025 * s + np.clip(a, 0, 1) * (1 - 0.04 * s)                       # hitam terangkat (matte)
    out = R / "graded" / ("senja__" + src.split("/")[-1])
    Image.fromarray((np.clip(a, 0, 1) * 255).astype(np.uint8)).save(out, quality=95)
    return out.name
# kekuatan per foto: foto siang/biru lebih kuat, foto senja yang sudah jingga lebih ringan
JOBS = {"74-matahari-menyentuh-laut-kapal.jpg": .45, "79-meja-kayak-golden-hour.jpg": 1.0, "80-cahaya-masuk-resto.jpg": .8,
        "81-resto-tirai-senja.jpg": .6, "82-dua-tamu-meja-senja.jpg": .5, "71-siluet-tirai-matahari.jpg": .4,
        "83-fotografer-di-tepi-pantai.jpg": 1.0, "76-staf-bantu-ayunan.jpg": .5, "77-ayunan-siluet-dekat.jpg": .5,
        "72-ayunan-di-antara-kelapa.jpg": .9, "70-perahu-nelayan-daun-kelapa.jpg": .4, "73-kayak-pelampung-perahu.jpg": .55,
        "75-afterglow-dua-sahabat.jpg": .5}
if __name__ == "__main__":
    for f, s in JOBS.items(): print(grade("senja/" + f, s))
