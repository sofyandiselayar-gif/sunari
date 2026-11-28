"""Perkecil render 2x ke ukuran upload, simpan JPEG kualitas 95 (4:4:4, sRGB, tanpa metadata):
  upload-28nov/instagram-feed/   1080x1350  carousel feed Instagram
  upload-28nov/instagram-story/  1080x1920  Story Instagram
  upload-28nov/tiktok/           1080x1920  TikTok photo mode (frame yang sama dengan story)"""
import pathlib, shutil
from PIL import Image, ImageFilter
U = pathlib.Path(__file__).resolve().parent / "upload-28nov"
for src, dests, size in [("feed", ["instagram-feed"], (1080, 1350)), ("story", ["instagram-story", "tiktok"], (1080, 1920))]:
    for d in dests: (U / d).mkdir(parents=True, exist_ok=True)
    for i, f in enumerate(sorted((U / "_2x" / src).glob("*.png")), 1):
        im = Image.open(f).convert("RGB").resize(size, Image.LANCZOS).filter(ImageFilter.UnsharpMask(0.8, 30, 2))
        for d in dests: im.save(U / d / f"{i:02d}-senja-28nov-{d}.jpg", quality=95, subsampling=0, optimize=True)
shutil.rmtree(U / "_2x"); print("ok")
