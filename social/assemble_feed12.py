"""Assemble the 12 feed carousels (order = grid preview, newest first) into feed-12-carousel/."""
import shutil, pathlib, glob, re
H = pathlib.Path(__file__).parent; OUT = H / "feed-12-carousel"
shutil.rmtree(OUT, ignore_errors=True)
ORDER = [("01-lebih-dari-menginap","camp-1.png","p01"),("02-senja-hari-ini","feed-senja.png","p02"),
         ("03-vip-superior","carousel/vs-1.png","vs"),("04-malam-di-sunari","camp-4.png","p04"),
         ("05-vip-standard","carousel/vp-1.png","vp"),("06-tempat-senja-pulang","feed-quote.png","p06"),
         ("07-pantai-sepi","camp-3.png","p07"),("08-sewa-kayak","feed-kayak.png","p08"),
         ("09-family-superior","carousel/fs-1.png","fs"),("10-menginap-menjelajah","camp-2.png","p10"),
         ("11-staycation-senja","feed-promo.png","p11"),("12-superior","carousel/sb-1.png","sb")]
for folder, cover, pre in ORDER:
    d = OUT / folder; d.mkdir(parents=True)
    shutil.copy(H / cover, d / "01.png")
    src = H / ("feed12" if pre.startswith("p") else "carousel")
    for f in sorted(src.glob(f"{pre}-*.png"), key=lambda x: int(re.search(r"-(\d+)\.png", x.name).group(1))):
        k = int(re.search(r"-(\d+)\.png", f.name).group(1))
        if k >= 2: shutil.copy(f, d / f"{k:02d}.png")
    print(folder, len(list(d.glob("*.png"))), "slide")
