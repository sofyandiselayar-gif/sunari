# Carousel "Location & Rute Akses": SunaRi Beach Resort Selayar

Proyek ini berisi 6 slide Instagram ukuran 1080×1350 px (rasio 4:5) dalam HTML/CSS murni.

## Struktur
```
location-carousel/
├── index.html        # 6 slide (#slide-1 … #slide-5) + sprite ikon SVG (stroke 1.5px)
├── styles.css        # token warna, tipografi, timeline, kartu, CTA
├── assets/logo-sunari.png
├── export.js         # render otomatis ke PNG retina (Playwright)
├── package.json
└── output/           # carousel-slide-1.png … carousel-slide-6.png (2160×2700 px)
```

## Desain
Palet tema SunaRi "Sunset Beach":

| Token | Nilai | Dipakai untuk |
|---|---|---|
| `--bg` | `#FBF4EC` Shell Cream | latar slide |
| `--ink` | `#45301F` Driftwood Deep | teks utama |
| `--accent` | `#8A5F48` Driftwood | label, ikon, timeline |
| `--accent-it` | `#A67C64` Driftwood | aksen judul italic |
| `--sun` | `#E07A4B` Coral Glow | penanda "Tercepat"/"Scenic Route", panah rute, "Geser →" |
| `--sun-grad` | `#FDB15D` → `#FF8A5C` Golden Hour → Coral Glow | tombol CTA, titik penanda |
| `--accent-soft` | Sandy Shore (transparan) | latar label estimasi waktu |
| peta | `#7BA7B6` Ocean Breeze | garis laut di slide sampul |

- **Font:** Playfair Display untuk judul, Plus Jakarta Sans untuk isi, jadwal, dan label.
- **Ikon:** pesawat, mobil, kapal feri, jam, pin lokasi, chat, kalender, dan bookmark. Semuanya garis tipis 1.5px dengan `vector-effect: non-scaling-stroke`, sehingga ketebalan garis tetap meskipun ukuran ikon berbeda.

## Export
```bash
npm install          # hanya jika Playwright belum terpasang
npx playwright install chromium   # hanya jika browser belum ada
node export.js       # atau: npm run export
```
Script ini menjalankan beberapa langkah secara berurutan:
1. Menunggu semua font termuat.
2. Memastikan setiap slide berukuran tepat 1080×1350.
3. Memberi peringatan bila ada konten yang terlalu dekat dengan footer (jaraknya kurang dari 24 px).
4. Menyimpan setiap slide ke `output/carousel-slide-N.png` dengan `deviceScaleFactor: 2`.

Untuk mengedit teks, ubah `index.html`, lalu jalankan `node export.js` lagi.
