"""Color grading "film hangat" untuk seri Menari di SunaRi -> assets/photos/graded/menari__*.jpg (foto asli tidak diubah).
Langit biru dilembutkan, kulit & kayu lebih hangat, hijau ke zaitun, hitam sedikit terangkat (matte).
Run: python3 social/grade_menari.py"""
from PIL import Image, ImageOps
import numpy as np, pathlib
R = pathlib.Path(__file__).resolve().parent.parent / "assets/photos"
def grade(p):
    im = ImageOps.exif_transpose(Image.open(p)).convert("RGB")
    a = np.asarray(im, float) / 255
    L = (0.299*a[..., 0] + 0.587*a[..., 1] + 0.114*a[..., 2])[..., None]
    a = L + (a - L) * 0.88                                                     # saturasi sedikit turun
    blue = np.clip((a[..., 2:3] - a[..., 0:1]) * 3, 0, 1)
    a = a*(1 - 0.25*blue) + (L*np.array([0.92, 0.97, 1.08]))*0.25*blue         # langit biru lebih lembut
    gr = np.clip((a[..., 1:2] - np.maximum(a[..., 0:1], a[..., 2:3])) * 4, 0, 1)
    a = a*(1 - 0.3*gr) + (L*np.array([0.98, 1.0, 0.72]))*0.3*gr                # hijau -> zaitun
    a = a * np.array([1.05, 1.0, 0.93])                                        # white balance hangat
    a = 0.035 + np.clip(a, 0, 1) * 0.94                                        # matte halus
    Image.fromarray((np.clip(a, 0, 1)*255).astype(np.uint8)).save(R / "graded" / ("menari__" + p.name), quality=93)
if __name__ == "__main__":
    for p in sorted((R / "menari").glob("*.jpg")): grade(p); print(p.name)
