# SunaRi Beach Resort Selayar

Aset brand untuk resort tepi pantai di Kepulauan Selayar dengan pemandangan matahari terbenam.

| Folder | Isi |
|---|---|
| `brand/BRAND_GUIDE.md` | Panduan brand: cerita, positioning, warna, tipografi, tone, strategi media sosial |
| `brand/palette-reference.jpg` | Referensi palet warna |
| `assets/` | Logo satu warna: Driftwood (utama) & Shell Cream (latar gelap); logo lama di `assets/original/` |
| `ota/DESKRIPSI_OTA_GOOGLE.md` | Deskripsi properti & 5 tipe kamar (ID/EN) untuk OTA dan Google Business Profile |
| `social/STORY_10_HARI.md` | Rencana story 10 hari + desain `social/stories/` |
| `social/TIKTOK_REELS.md` | Template caption Reels & TikTok (hook, shot, caption, hashtag) |
| `social/INSTAGRAM_BULAN_1.md` | Bio Instagram, highlight, dan 30 caption bulan pertama |
| `social/` | Template Instagram (feed, story, carousel room tour Superior / VIP Superior / Family Superior / Standard / VIP Standard) beserta sumber HTML-nya |
| `assets/photos/` | Foto asli kamar (5 tipe) dan 20 foto senja |

## Palet
*Sunset Beach*: `#F7A7A1` Sunset Pink · `#FF8A5C` Coral Glow · `#FDB15D` Golden Hour · `#7BA7B6` Ocean Breeze · `#E6C89B` Sandy Shore · `#A67C64` Driftwood
Pendukung: `#FBF4EC` Shell Cream · `#5A3E31` Driftwood Deep. Pita & bar memakai Sandy Shore, teks Driftwood Deep. Logo satu warna: Driftwood.

## Membuat ulang template media sosial
Gaya desain: minimalis & elegan ala brand board (Playfair Display + Montserrat, foto penuh dengan judul serif, foto berbingkai, latar Shell Cream).
Brand board: `brand/brand-board.png` (sumber `brand/build_board.py`, render dengan `node brand/render_board.js` setelah render template sosial).
Edit teks (jam senja, kamar, dll.) di bagian CONTENT `social/build_kit.py`, lalu jalankan:
```
python3 social/build_kit.py && node social/render.js
```

## Kontak
- WhatsApp: +62 821-8903-3044 (Sofyan)
- Alamat: Jl. Poros Benteng – Appatana KM 14, Dusun Tile-Tile Utara, Desa Patikarya, Kec. Bontosikuyu, Kab. Kepulauan Selayar, Sulawesi Selatan
- Google Maps: https://maps.app.goo.gl/iUWWHNCT7Vyu4i537
