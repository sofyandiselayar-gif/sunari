"""Color grading tema SunaRi untuk carousel "Bungalow Mana yang Cocok Buat Kamu?" -> assets/photos/graded/pilih__*.jpg
Look sama dengan grade_senja_cerita.py (highlight keemasan, bayangan cokelat Driftwood Deep, hijau ke zaitun, biru dilembutkan,
hitam sedikit terangkat), tetapi resolusi penuh (maks. 3200 px) agar export 2160x2700 tetap HD. Foto asli tidak diubah.
Run: python3 social/grade_pilih_bungalow.py"""
from PIL import Image, ImageOps
import numpy as np, pathlib
from grade_senja_cerita import rgb2hsv, hsv2rgb
R = pathlib.Path(__file__).resolve().parent.parent / "assets/photos"

def grade(src, s):
    im = ImageOps.exif_transpose(Image.open(R / src)).convert("RGB"); im.thumbnail((3200, 3200), Image.LANCZOS)
    a = np.asarray(im, np.float32) / 255
    a = np.clip(a * (1 + s * np.array([0.05, 0.0, -0.10], np.float32)), 0, 1)   # white balance hangat
    h, sat, v = rgb2hsv(a)
    g = (h > 0.17) & (h < 0.45)                                                  # hijau -> zaitun, sedikit redup
    h = np.where(g, h - 0.035 * s, h); sat = np.where(g, sat * (1 - 0.22 * s), sat)
    bl = (h > 0.46) & (h < 0.72)                                                 # biru laut/langit -> lebih lembut
    sat = np.where(bl, sat * (1 - 0.30 * s), sat)
    o = (h < 0.12) | (h > 0.95)                                                  # oranye/merah sedikit diperkaya
    sat = np.where(o, np.clip(sat * (1 + 0.08 * s), 0, 1), sat)
    a = hsv2rgb(h % 1, sat, v)
    L = (0.299 * a[..., 0] + 0.587 * a[..., 1] + 0.114 * a[..., 2])[..., None]
    a = a - 0.10 * s * (a - a**2) * (2 * a - 1)                                  # S-curve lembut
    wh = np.clip((L - 0.55) / 0.45, 0, 1); ws = np.clip((0.40 - L) / 0.40, 0, 1)
    a = a * (1 - 0.14 * s * wh) + np.array([1.0, 0.82, 0.58]) * 0.14 * s * wh            # highlight keemasan
    a = a * (1 - 0.22 * s * ws) + np.array([0x3B, 0x28, 0x19]) / 255 * 0.22 * s * ws     # bayangan cokelat
    a = 0.025 * s + np.clip(a, 0, 1) * (1 - 0.04 * s)                            # hitam terangkat (matte)
    out = R / "graded" / ("pilih__" + src.replace("/", "__"))
    Image.fromarray((np.clip(a, 0, 1) * 255).astype(np.uint8)).save(out, quality=95, subsampling=0)
    return out.name

# kekuatan per foto: foto siang/biru/hijau lebih kuat, kayu oranye & foto senja lebih ringan
JOBS = {"vip-standard-bungalow/02-teras-view-pantai.jpg": 1.3,
        "standard-bungalow/01-teras-view-laut.jpg": 1.3,
        "vip-standard-bungalow/04-teras-view-laut.jpg": 1.3,
        "superior-bungalow/04-kamar-loteng.jpg": 1.1,
        "vip-superior-bungalow/06-bathtub-semi-outdoor.jpg": 0.8,
        "family-superior-bungalow/01-eksterior-taman.jpg": 1.5,
        "family-superior-bungalow/10-lantai-atas-kasur-kettle.jpg": 1.1,
        "senja/11-kayak-dan-pulau.jpg": 0.6}
if __name__ == "__main__":
    for f, s in JOBS.items(): print(grade(f, s))
