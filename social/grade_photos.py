"""Color grading tema SunaRi (hangat keemasan, bayangan cokelat) -> assets/photos/graded/. Foto asli tidak diubah.
Run: python3 social/grade_photos.py"""
from PIL import Image, ImageEnhance, ImageOps
import numpy as np, pathlib
R = pathlib.Path(__file__).resolve().parent.parent / "assets/photos"
def grade(src, dst, s=1.0):
    im = ImageOps.exif_transpose(Image.open(R / src)).convert("RGB")
    a = np.asarray(im, float) / 255
    L = (0.299*a[..., 0] + 0.587*a[..., 1] + 0.114*a[..., 2])[..., None]
    a = a * (1 + s*np.array([0.06, 0.0, -0.12]))                          # white balance hangat
    wh = np.clip((L-0.45)/0.55, 0, 1); ws = np.clip((0.42-L)/0.42, 0, 1)
    a = a*(1-0.18*s*wh) + np.array([1.0, 0.80, 0.55])*0.18*s*wh            # highlight keemasan
    a = a*(1-0.25*s*ws) + np.array([0x3B, 0x28, 0x19])/255*0.25*s*ws        # bayangan cokelat (Driftwood Deep)
    a = 0.03 + np.clip(a, 0, 1)*0.95                                        # sedikit fade, lembut
    out = ImageEnhance.Color(Image.fromarray((np.clip(a, 0, 1)*255).astype(np.uint8))).enhance(1 - 0.03*s)
    out.save(R / "graded" / dst, quality=95)
JOBS = [("pantai/05-kursi-santai-dan-kayak.jpg", 1.0), ("pantai/01-nelayan-pagi.jpg", 1.8),
        ("aktivitas/06-ayunan-gaun-merah-senja.jpg", 1.2), ("senja/59-makan-senja-payung-1810.jpg", 0.7),
        ("senja/25-pohon-senja-dekat.jpg", 0.6), ("senja/56-drone-kelapa-payung-1749.jpg", 0.6)]
for src, s in JOBS:
    grade(src, src.replace("/", "__"), s); print("graded", src)
