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
def noise(sigma, scale):
    n = Image.fromarray((rng.random((Hh // scale, W // scale)) * 255).astype(np.uint8)).resize((W, Hh), Image.BICUBIC).filter(ImageFilter.GaussianBlur(sigma))
    return np.asarray(n, float) / 255
y = np.linspace(0, 1, Hh)[:, None, None]
seaC = (np.array([0x0E, 0x3A, 0x63]) * (1 - y) + np.array([0x0B, 0x33, 0x5A]) * y) / 255
seaC = seaC + (noise(6, 8)[..., None] - .5) * 0.05
halo = np.asarray(Image.fromarray((mk * 255).astype(np.uint8)).filter(ImageFilter.MaxFilter(9)).filter(ImageFilter.GaussianBlur(22)), float) / 255
halo2 = np.asarray(Image.fromarray((mk * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(6)), float) / 255
shallow = np.array([0x22, 0x9C, 0xB0]) / 255
seaC = seaC * (1 - .55 * halo[..., None]) + shallow * .55 * halo[..., None]
seaC = seaC * (1 - .35 * halo2[..., None]) + np.array([0x5F, 0xD0, 0xD2]) / 255 * .35 * halo2[..., None]
t = noise(10, 6)[..., None]; t2 = noise(3, 2)[..., None]
landC = np.array([0x2F, 0x5E, 0x2E]) / 255 * (1 - t) + np.array([0x5C, 0x86, 0x45]) / 255 * t
landC = landC * (0.9 + 0.2 * t2)
inner = np.asarray(Image.fromarray((mk * 255).astype(np.uint8)).filter(ImageFilter.MinFilter(9)).filter(ImageFilter.GaussianBlur(8)), float)[..., None] / 255
landC = landC * (0.85 + 0.15 * inner) + np.array([0xB9, 0xB0, 0x7A]) / 255 * 0.18 * (1 - inner)   # tepi pantai berpasir
out = seaC * (1 - mk[..., None]) + landC * mk[..., None]
Image.fromarray((np.clip(out, 0, 1) * 255).astype(np.uint8)).save(H / "src/peta-dasar-indonesia.png")
print("ok")
