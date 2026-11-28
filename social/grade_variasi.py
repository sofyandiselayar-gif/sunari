"""Variasi color grading untuk satu foto: cerah, dark, film (warm film), tealorange, earthy (earthy beige).
Run: python3 social/grade_variasi.py [nama-foto-di-assets/photos/menari tanpa .jpg]
-> assets/photos/graded/variasi/<nama>__<gaya>.jpg (resolusi asli). Sinematik soft ada di social/grade_menari.py."""
from PIL import Image, ImageOps, ImageFilter
import numpy as np, pathlib, sys
R = pathlib.Path(__file__).resolve().parent.parent / "assets/photos"
rng = np.random.default_rng(3)
def lum(a): return (0.299*a[..., 0] + 0.587*a[..., 1] + 0.114*a[..., 2])[..., None]
def skin_mask(a):
    L = lum(a)
    return np.clip((a[..., 0:1]-a[..., 1:2])*6, 0, 1) * np.clip((a[..., 1:2]-a[..., 2:3])*6, 0, 1) * np.clip(L*3-.4, 0, 1)
def glow(a, amt, tint, im):
    g = Image.fromarray((np.clip((lum(a)-.55)/.45, 0, 1)[..., 0]*255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(max(im.size)/60))
    g = np.asarray(g, float)[..., None]/255 * np.array(tint) * amt
    return 1 - (1-a)*(1-g)
def cerah(a, im):
    sk = skin_mask(a)
    a = a ** 0.78                                                     # eksposur naik
    L = lum(a); a = L + (a-L) * (0.82 + .15*sk)                       # warna pastel, kulit dijaga
    bl = np.clip((a[..., 2:3]-a[..., 0:1])*3, 0, 1)
    a = a*(1-.25*bl) + (L*np.array([.93, 1.0, 1.05]))*.25*bl          # langit biru lembut
    a = .5 + (a-.5)*.84                                               # kontras rendah
    a = .07 + a*.93                                                   # bayangan terangkat
    a = a * np.array([1.025, 1.01, .99])                              # sedikit hangat, putih tetap bersih
    a = glow(np.clip(a, 0, 1), .16, [1, .97, .92], im)
    return a
def dark(a, im):
    sk = skin_mask(a)
    L = lum(a); a = L + (a-L) * (0.62 + .25*sk)                      # desaturasi, kulit dijaga
    gr = np.clip((a[..., 1:2]-np.maximum(a[..., 0:1], a[..., 2:3]))*5, 0, 1)
    a = a*(1-.4*gr) + (L*np.array([.9, .95, .78]))*.4*gr              # hijau -> olive gelap
    a = a ** 1.22                                                     # eksposur turun
    a = .5 + (a-.5)*1.12                                              # kontras sedikit naik
    a = np.clip(a, 0, 1)
    L = lum(a)
    sh = np.clip((.45-L)/.45, 0, 1); hi = np.clip((L-.5)/.5, 0, 1)
    a = a + sh*np.array([-.03, .01, .035]) + hi*np.array([.05, .02, -.035])   # bayangan teal, highlight amber
    a = .025 + np.clip(a, 0, 1)*.96                                   # hitam sedikit matte
    h, w = a.shape[:2]; y, x = np.ogrid[:h, :w]
    d = np.sqrt(((x-w/2)/(w/2))**2 + ((y-h/2)/(h/2))**2)
    a = a * (1 - .3*np.clip(d-.45, 0, 1)**1.6)[..., None]            # vignette
    a = glow(np.clip(a, 0, 1), .12, [1, .85, .65], im)
    return a
def film(a, im):
    L = lum(a); a = L + (a-L)*.88
    gr = np.clip((a[..., 1:2]-np.maximum(a[..., 0:1], a[..., 2:3]))*4, 0, 1)
    a = a*(1-.3*gr) + (L*np.array([.98, 1.0, .72]))*.3*gr             # hijau -> zaitun
    bl = np.clip((a[..., 2:3]-a[..., 0:1])*3, 0, 1)
    a = a*(1-.25*bl) + (L*np.array([.92, .97, 1.08]))*.25*bl
    a = a*np.array([1.07, 1.01, .9])                                  # hangat keemasan
    a = .045 + np.clip(a, 0, 1)*.93                                   # matte
    return a
def tealorange(a, im):
    sk = skin_mask(a); L = lum(a)
    a = .5 + (a-.5)*1.1
    sh = np.clip((.5-L)/.5, 0, 1); hi = np.clip((L-.4)/.6, 0, 1)
    a = a + sh*np.array([-.05, .02, .06]) + hi*np.array([.06, .015, -.06])
    bl = np.clip((a[..., 2:3]-a[..., 0:1])*3, 0, 1)
    a = a*(1-.35*bl) + (L*np.array([.7, 1.02, 1.12]))*.35*bl          # biru -> teal
    a = np.clip(a, 0, 1); L = lum(a); a = L + (a-L)*(1.05+.05*sk)
    return a
def earthy(a, im):
    sk = skin_mask(a); L = lum(a)
    a = L + (a-L)*(.55+.25*sk)                                        # sangat redup, kulit dijaga
    a = a*.82 + (L*np.array([1.08, .99, .86]))*.18                    # semua warna ke krem/beige
    bl = np.clip((a[..., 2:3]-a[..., 0:1])*3, 0, 1)
    a = a*(1-.4*bl) + (L*np.array([.98, .98, .98]))*.4*bl             # biru jadi abu lembut
    a = .5 + (a-.5)*.9; a = .05 + np.clip(a, 0, 1)*.93
    a = glow(np.clip(a, 0, 1), .1, [1, .95, .88], im)
    return a
def run(name):
    im = ImageOps.exif_transpose(Image.open(R/"menari"/f"{name}.jpg")).convert("RGB")
    a0 = np.asarray(im, float)/255
    out = R/"graded"/"variasi"; out.mkdir(exist_ok=True)
    for tag, fn in (("cerah", cerah), ("dark", dark), ("film", film), ("tealorange", tealorange), ("earthy", earthy)):
        a = fn(a0.copy(), im)
        a = np.clip(a + rng.normal(0, .009, a.shape[:2])[..., None], 0, 1)    # grain halus
        Image.fromarray((a*255).astype(np.uint8)).save(out/f"{name}__{tag}.jpg", quality=95, subsampling=0)
        print(out/f"{name}__{tag}.jpg")
if __name__ == "__main__":
    run(sys.argv[1] if len(sys.argv) > 1 else "01-duduk-meja-pantai-surut")
