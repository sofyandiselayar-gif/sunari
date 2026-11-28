"""Ekspor 6 gaya color grading untuk satu foto sebagai PNG HD tanpa kompresi (resolusi asli), langsung dari foto asli.
Run: python3 social/export_grading_png.py [nama-foto tanpa .jpg] -> social/variasi-grading/png/<no>-<gaya>.png"""
import sys, pathlib, numpy as np
from PIL import Image, ImageOps
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import grade_menari as gm, grade_variasi as gv
name = sys.argv[1] if len(sys.argv) > 1 else "01-duduk-meja-pantai-surut"
im = ImageOps.exif_transpose(Image.open(gv.R / "menari" / f"{name}.jpg")).convert("RGB")
out = pathlib.Path(__file__).parent / "variasi-grading" / "png"; out.mkdir(parents=True, exist_ok=True)
gm.rng = np.random.default_rng(7); gm.grade_image(im).save(out / "1-sinematik-soft.png", optimize=True)
a0 = np.asarray(im, float) / 255
for no, tag, fn in ((2, "earthy-beige", gv.earthy), (3, "warm-film", gv.film), (4, "bright-airy", gv.cerah), (5, "teal-orange", gv.tealorange), (6, "dark-moody", gv.dark)):
    a = np.clip(fn(a0.copy(), im) + gv.rng.normal(0, .009, a0.shape[:2])[..., None], 0, 1)
    Image.fromarray((a*255).astype(np.uint8)).save(out / f"{no}-{tag}.png", optimize=True)
for f in sorted(out.glob("*.png")): print(f.name, Image.open(f).size, round(f.stat().st_size/1e6, 1), "MB")
