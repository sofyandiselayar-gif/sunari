# Carousel "Location & Rute Akses": SunaRi Beach Resort Selayar

Proyek ini berisi 7 slide Instagram ukuran 1080×1350 px (rasio 4:5) dalam HTML/CSS murni.

## Struktur
```
location-carousel/
├── index.html        # 7 slide (#slide-1 … #slide-5) + sprite ikon SVG (stroke 1.5px)
├── styles.css        # token warna, tipografi, timeline, kartu, CTA
├── assets/logo-sunari.png
├── export.js         # render otomatis ke PNG retina (Playwright)
├── package.json
└── output/           # carousel-slide-1.png … carousel-slide-7.png (2160×2700 px)
```

## Desain (v2: model peta, selaras dengan story "Rute ke SunaRi")
- **Latar:** setiap slide memakai peta ilustrasi penuh dari `assets/maps/` (1080×1920). Area peta yang tampil (crop) diatur lewat `--y` di tag `<img class="map">`.
- **Kartu informasi:** berwarna Shell Cream `#FBF4EC` (transparansi 96%), sudut 40px, dengan bayangan lembut. Posisinya di bawah, supaya label penting di peta tetap terlihat.
- **Palet SunaRi "Sunset Beach":**
  - teks Driftwood Deep `#45301F`;
  - label dan aksen italic Driftwood `#8A5F48` / `#A67C64`;
  - highlight Coral Glow `#E07A4B`;
  - tombol CTA bergradasi Golden Hour → Coral (`#FDB15D` → `#FF8A5C`).
- **Warna nomor rute** diambil dari peta: ① `#E8674A`, ② `#2B8289`, ③ `#D8932D`.
- **Font:** Playfair Display untuk judul, Plus Jakarta Sans untuk isi.
- **Ikon:** garis tipis 1.5px.

| Slide | Peta | Isi |
|---|---|---|
| 1 | Sulawesi | Sampul "Cara Mudah Menuju SunaRi Beach Resort" |
| 2 | 3 rute | Ringkasan ① Udara · ② Darat & feri · ③ Kapal langsung |
| 3 | Rute 1 | Jalur udara: ±45 menit, lalu ±10–15 menit ke resort |
| 4 | Rute 2 | Terminal Malengkeri → Bira → feri → Pamatata → SunaRi |
| 5 | Rute 3 | KM Dharma Kartika III → Benteng → SunaRi |
| 6 | Pulau Selayar | Resort Pickup: penjemputan lokal & paket transfer |
| 7 | Indonesia | Ringkasan alamat + CTA WhatsApp |

## Export
```bash
npm install          # hanya jika Playwright belum terpasang
npx playwright install chromium   # hanya jika browser belum ada
node export.js       # atau: npm run export
```
Script ini menjalankan beberapa langkah secara berurutan:
1. Menunggu semua font termuat.
2. Memastikan setiap slide berukuran tepat 1080×1350.
3. Memastikan kartu informasi berada di dalam slide, dan menampilkan posisi atas kartu (`card starts at y=…`) untuk memastikan label peta tidak tertutup.
4. Menyimpan setiap slide ke `output/carousel-slide-N.png` dengan `deviceScaleFactor: 2`.

Untuk mengedit teks, ubah `index.html`, lalu jalankan `node export.js` lagi.
