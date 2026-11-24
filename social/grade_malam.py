"""Color grading malam tema SunaRi -> assets/photos/graded/malam__*.jpg (foto asli tidak diubah).
Biru malam dilembutkan ke navy hangat, lampu & kayu keemasan, bayangan cokelat tua, hitam sedikit terangkat.
Run: python3 social/grade_malam.py"""
from PIL import Image, ImageOps
import numpy as np, pathlib
R = pathlib.Path(__file__).resolve().parent.parent / "assets/photos"
def grade(name, s=1.0):
    im = ImageOps.exif_transpose(Image.open(R / "malam" / name)).convert("RGB"); im.thumbnail((1800, 1800))
    a = np.asarray(im, float) / 255
    L = (0.299*a[..., 0] + 0.587*a[..., 1] + 0.114*a[..., 2])[..., None]
    mx = a.max(-1, keepdims=True); mn = a.min(-1, keepdims=True); sat = (mx - mn) / (mx + 1e-6)
    blue = np.clip((a[..., 2:3] - a[..., 0:1]) * 3, 0, 1)                     # area biru (langit)
    navy = np.array([0x1E, 0x24, 0x3A]) / 255
    a = a * (1 - 0.35*s*blue) + (navy * (0.6 + 0.8*L)) * 0.35*s*blue           # langit -> navy hangat
    a = a * (1 + s*np.array([0.06, 0.02, -0.08]))                              # white balance hangat
    wh = np.clip((L - 0.45) / 0.55, 0, 1)
    a = a*(1 - 0.22*s*wh) + np.array([1.0, 0.80, 0.52])*0.22*s*wh              # lampu/kayu keemasan
    ws = np.clip((0.30 - L) / 0.30, 0, 1)
    a = a*(1 - 0.30*s*ws) + np.array([0x2A, 0x1E, 0x18])/255*0.30*s*ws         # bayangan cokelat tua
    gr = np.clip((a[..., 1:2] - np.maximum(a[..., 0:1], a[..., 2:3])) * 4, 0, 1)
    a = a*(1 - 0.25*s*gr) + (a.mean(-1, keepdims=True) * np.array([0.95, 0.95, 0.7]))*0.25*s*gr  # hijau -> zaitun
    a = 0.02*s + np.clip(a, 0, 1) * (1 - 0.03*s)                               # matte halus
    Image.fromarray((np.clip(a, 0, 1)*255).astype(np.uint8)).save(R / "graded" / ("malam__" + name), quality=95)
JOBS = {"23-jalan-setapak-taman-senja.jpg": 1.0, "20-gazebo-berlampu-kelapa.jpg": .9, "22-jalan-setapak-ke-pantai.jpg": 1.0,
        "15-teras-view-gazebo-berlampu.jpg": .8, "14-teras-kayu-sofa.jpg": .7, "18-kelapa-dan-bintang.jpg": 1.0,
        "24-family-superior-bulan.jpg": .8, "19-taman-bulan-jembatan.jpg": 1.0}
if __name__ == "__main__":
    for n, s in JOBS.items(): grade(n, s); print(n)
