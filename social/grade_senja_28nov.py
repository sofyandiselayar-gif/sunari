"""Color grading foto senja 28 Nov 2026 (senja/85-99) untuk carousel & story "Senja Hari Ini · 28 Nov".
Look sama dengan grade_senja_cerita.py, tapi resolusi 2560 px (cukup untuk story 1080x1920 tanpa diperbesar).
Run: python3 social/grade_senja_28nov.py [folder_foto_asli]   (default assets/photos/senja; file asli kamera lebih tajam)"""
import sys, pathlib, numpy as np
from PIL import Image, ImageOps
from grade_senja_cerita import rgb2hsv, hsv2rgb
R = pathlib.Path(__file__).resolve().parent.parent / "assets/photos"
SRC = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else R / "senja"
JOBS = {"85-dua-tamu-bingkai-pohon-tirai.jpg": .45, "97-gazebo-tirai-pantulan-matahari.jpg": .7,
        "96-kayak-pulau-awan.jpg": .8, "92-kamboja-bingkai-matahari-tamu.jpg": .6, "91-tamu-memotret-matahari.jpg": .5,
        "88-matahari-terbenam-langit-merah.jpg": .35, "87-tamu-berhijab-tepi-pantai.jpg": .5,
        "99-pelayan-nampan-senja.jpg": .45, "98-kayak-langit-merah.jpg": .4}
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
if __name__ == "__main__":
    for f, s in JOBS.items():
        im = ImageOps.exif_transpose(Image.open(SRC / f)).convert("RGB"); im.thumbnail((2560, 2560), Image.LANCZOS)
        out = R / "graded" / ("senja__" + f); grade(im, s).save(out, quality=93, subsampling=0); print(out.name, im.size)
