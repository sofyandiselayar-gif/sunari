"""Color grading "sinematik soft" untuk seri Menari di SunaRi -> assets/photos/graded/menari__*.jpg (foto asli tidak diubah).
Kontras rendah, hitam terangkat, highlight roll-off; bayangan teal lembut, highlight peach hangat, kulit tetap natural;
hijau & biru langit diredam, glow halus di area terang, grain film tipis.
Run: python3 social/grade_menari.py"""
from PIL import Image, ImageOps, ImageFilter
import numpy as np, pathlib
R = pathlib.Path(__file__).resolve().parent.parent / "assets/photos"
rng = np.random.default_rng(7)
def lum(a): return (0.299*a[..., 0] + 0.587*a[..., 1] + 0.114*a[..., 2])[..., None]
def grade(p):
    im = ImageOps.exif_transpose(Image.open(p)).convert("RGB")
    a = np.asarray(im, float) / 255
    mx = a.max(-1, keepdims=True); mn = a.min(-1, keepdims=True); L = lum(a)
    # perlindungan kulit (merah > hijau > biru, cukup terang)
    skin = np.clip((a[..., 0:1] - a[..., 1:2]) * 6, 0, 1) * np.clip((a[..., 1:2] - a[..., 2:3]) * 6, 0, 1) * np.clip(L * 3 - .4, 0, 1)
    # saturasi turun (kulit dijaga), hijau ke sage, biru langit diredam
    sat = 0.78 + 0.17 * skin
    a = L + (a - L) * sat
    gr = np.clip((a[..., 1:2] - np.maximum(a[..., 0:1], a[..., 2:3])) * 5, 0, 1)
    a = a*(1 - .35*gr) + (L*np.array([.95, 1.02, .9]))*.35*gr
    bl = np.clip((a[..., 2:3] - a[..., 0:1]) * 3, 0, 1)
    a = a*(1 - .3*bl) + (L*np.array([.9, 1.0, 1.06]))*.3*bl
    mg = np.clip((np.minimum(a[..., 0:1], a[..., 2:3]) - a[..., 1:2]) * 3, 0, 1)       # magenta bougenvil diredam
    a = a*(1 - .3*mg) + (L*np.array([1.04, .97, 1.0]))*.3*mg
    # kurva lembut: kontras turun, hitam terangkat, highlight roll-off
    a = .5 + (a - .5) * .86
    a = np.where(a > .72, .72 + (a - .72) * .62, a)
    a = .055 + a * .93
    # split toning: bayangan teal, highlight peach
    L = lum(a)
    sh = np.clip((.5 - L) / .5, 0, 1) ** 1.5; hi = np.clip((L - .45) / .55, 0, 1) ** 1.5
    a = a + sh * np.array([-.02, .008, .03]) + hi * np.array([.035, .012, -.03])
    a = a * np.array([1.025, 1.0, .975])                                       # sedikit hangat
    a = np.clip(a, 0, 1)
    # glow halus dari area terang (screen)
    g = Image.fromarray((np.clip((lum(a) - .55) / .45, 0, 1)[..., 0] * 255).astype(np.uint8))
    r = max(im.size) / 60
    g = np.asarray(g.filter(ImageFilter.GaussianBlur(r)), float)[..., None] / 255
    glow = g * np.array([1.0, .93, .82]) * .22
    a = 1 - (1 - a) * (1 - glow)
    # grain film tipis
    n = rng.normal(0, .011, a.shape[:2])[..., None]
    a = np.clip(a + n * (1 - .5*lum(a)), 0, 1)
    Image.fromarray((a*255).astype(np.uint8)).save(R / "graded" / ("menari__" + p.name), quality=94)
if __name__ == "__main__":
    for p in sorted((R / "menari").glob("*.jpg")): grade(p); print(p.name)
