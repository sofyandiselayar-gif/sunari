"""Peta dasar Jakarta–Makassar bergaya peta rute SunaRi (laut biru tua, pulau hijau, pantai toska).
Sumber: src/peta-indonesia-rute-asli.jpg (rute lain & label dihapus). Output: src/peta-dasar-indonesia.png (3200x1600)."""
from PIL import Image, ImageFilter, ImageChops
import numpy as np, pathlib
H = pathlib.Path(__file__).parent
a = np.asarray(Image.open(H / "src/peta-indonesia-rute-asli.jpg").convert("RGB")).astype(int)
r, g, b = a[..., 0], a[..., 1], a[..., 2]
land = (r > 228) & (g > 228) & (b > 228)
sea = (b > 200) & (r < 200) & (g > 190) & (b - r > 30)
lab = np.full(r.shape, -1); lab[land] = 1; lab[sea] = 0
for _ in range(60):                                   # isi piksel teks/rute/garis batas dari tetangga
    u = lab < 0
    if not u.any(): break
    L = np.asarray(Image.fromarray((lab == 1).astype(np.uint8) * 255).filter(ImageFilter.MaxFilter(3))) > 0
    S = np.asarray(Image.fromarray((lab == 0).astype(np.uint8) * 255).filter(ImageFilter.MaxFilter(3))) > 0
    lab[u & S & ~L] = 0; lab[u & L & ~S] = 1; lab[u & L & S] = 0
lab[lab < 0] = 0
m = Image.fromarray((lab * 255).astype(np.uint8)).filter(ImageFilter.MedianFilter(5))
W, Hh = 3200, 1600
m = m.resize((W, Hh), Image.LANCZOS).filter(ImageFilter.GaussianBlur(1.2))
mk = np.asarray(m, float) / 255; mk = np.clip((mk - 0.5) * 6 + 0.5, 0, 1)
rng = np.random.default_rng(7)
def blur(x, r): return np.asarray(Image.fromarray(np.clip(x * 255, 0, 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(r)), float) / 255
def fbm():
    out = np.zeros((Hh, W)); amp = 1.0; tot = 0
    for sc in (256, 128, 64, 32, 16, 8, 4):
        n = Image.fromarray((rng.random((Hh // sc + 2, W // sc + 2)) * 255).astype(np.uint8)).resize((W + 2 * sc, Hh + 2 * sc), Image.BICUBIC)
        out += amp * np.asarray(n, float)[sc:sc + Hh, sc:sc + W] / 255; tot += amp; amp *= 0.55
    return out / tot
# ---- relief 3D: tinggi dari jarak ke pantai + noise fraktal, lalu hillshade (cahaya dari barat laut)
d = (blur(mk, 6) + blur(mk, 18) + blur(mk, 45) + blur(mk, 90)) / 4
nz = fbm()
h = mk * (0.55 * d + 0.45 * (nz - 0.3) * np.sqrt(np.clip(d, 0, 1)) * 1.6)
hs = blur(np.clip(h, 0, 1), 1.5)
gy, gx = np.gradient(hs * 260)
nx, ny, nzv = -gx, -gy, np.ones_like(gx); ln = np.sqrt(nx**2 + ny**2 + nzv**2)
L = np.array([-0.6, -0.6, 0.55]); L = L / np.linalg.norm(L)
shade = np.clip((nx * L[0] + ny * L[1] + nzv * L[2]) / ln, 0, 1)
shade = 0.55 + 0.75 * shade
lo, mid, hi = np.array([0x2C, 0x5E, 0x22]), np.array([0x3E, 0x73, 0x2C]), np.array([0x76, 0x6A, 0x3A])
hn = np.clip(h * 1.6, 0, 1)[..., None]
landC = (lo * (1 - hn) + mid * hn) / 255
ridge = np.clip((h - 0.55) * 4, 0, 1)[..., None] * (nz[..., None] > 0.5)
landC = landC * (1 - 0.35 * ridge) + hi / 255 * 0.35 * ridge
landC = landC * shade[..., None]
edge = np.clip(mk - blur(np.asarray(Image.fromarray((mk * 255).astype(np.uint8)).filter(ImageFilter.MinFilter(3)), float) / 255, 1.0), 0, 1)
landC = landC * (1 - 0.45 * edge[..., None]) + np.array([0xE9, 0xDC, 0x9A]) / 255 * 0.45 * edge[..., None]   # garis pasir
# ---- laut: biru dalam + gradasi toska di perairan dangkal + awan tipis
sn = fbm()
seaC = (np.array([0x10, 0x46, 0x80]) / 255) * (0.88 + 0.22 * sn[..., None])
shallow1 = blur(np.asarray(Image.fromarray((mk * 255).astype(np.uint8)).filter(ImageFilter.MaxFilter(15)), float) / 255, 26)
shallow2 = blur(np.asarray(Image.fromarray((mk * 255).astype(np.uint8)).filter(ImageFilter.MaxFilter(5)), float) / 255, 7)
seaC = seaC * (1 - 0.6 * shallow1[..., None]) + np.array([0x1E, 0x8F, 0xB8]) / 255 * 0.6 * shallow1[..., None]
seaC = seaC * (1 - 0.9 * shallow2[..., None]) + np.array([0x5A, 0xE0, 0xDC]) / 255 * 0.9 * shallow2[..., None]
out = seaC * (1 - mk[..., None]) + landC * mk[..., None]
cl = np.clip((fbm() - 0.58) * 3.2, 0, 1); cl = blur(cl, 10) * 0.32
out = out * (1 - cl[..., None]) + cl[..., None]
vig = 1 - 0.18 * ((np.linspace(-1, 1, W)[None, :] ** 2 + np.linspace(-1, 1, Hh)[:, None] ** 2) / 2)
out = out * vig[..., None]
Image.fromarray((np.clip(out, 0, 1) * 255).astype(np.uint8)).save(H / "src/peta-dasar-indonesia.png")
print("ok")
