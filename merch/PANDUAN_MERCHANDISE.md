# SunaRi: Desain Souvenir & Oleh-oleh

**Isi folder `merch/`:**
- `artwork/`: **file untuk dicetak/ditempel** (PNG transparan, resolusi tinggi). Ini file yang dikirim ke tukang sablon/percetakan.
- `mockup/` & `mockup-clean/`: gambar contoh 25 produk jadi.
- `SunaRi_Katalog_Souvenir.pdf`: katalog + spesifikasi teknis untuk vendor.
- `merch-overview.png`: semua produk dalam satu gambar.
- Logo asli untuk dada kiri / bordir: `assets/logo-sunari-driftwood.png` dan `assets/logo-sunari-cream.png`.

---

## 1. Daftar artwork (siap cetak, PNG transparan 300 dpi)

| Kode | File | Desain | Untuk |
|---|---|---|---|
| A1 | `A1-back-print-light/dark` | Matahari bergaris + logo asli + "Tempat senja pulang" | Punggung kaos, poster |
| A2 | `A2-typography-light/dark` | SunaRi / Beach Resort / Selayar | Kaos, mug, buku catatan |
| A3 | `A3-sticker-round` | Stiker bulat "Where every day ends beautifully" | Stiker, gantungan akrilik |
| A4 | `A4-kayak-light/dark` | "Paddle into the sunset" | Kaos, mug enamel, stiker |
| A5 | `A5-pattern-tile` | Pola matahari & ombak (bisa diulang) | Sarung pantai, bandana, kertas kado |
| A6 | `A6-mark-pin` | Simbol matahari | Bordir topi, pin, grafir kayu |
| A7 | `A7-sun-stripes` | Matahari bergaris | Stiker, aksen kemasan |
| A8 | `A8-vintage-badge-light/dark` | Badge vintage dengan pohon kelapa | Kaos, pouch, tumbler, tatakan |
| A9 | `A9-sunset-landscape(-notext)` | Ilustrasi senja: pohon kelapa, laut, kayak | Handuk, magnet, kartu pos, sampul |
| A10 | `A10-greetings-selayar` | "Greetings from SELAYAR" (foto di dalam huruf) | Kaos putih, tote bag, kartu pos |
| A11 | `A11-chest-mini-light/dark` | Simbol + SunaRi, kecil | Dada kiri kaos/hoodie, stiker |
| A12 | `A12-hangtag-front/back` | Hang tag 5 × 9 cm | Label produk tekstil |

## 2. Produk (25) & spesifikasi
Spesifikasi lengkap per produk (bahan, ukuran, teknik cetak, posisi, tinta) ada di **`SunaRi_Katalog_Souvenir.pdf`** (30 halaman, A4 landscape), siap dikirim ke vendor.

| Kategori | Produk |
|---|---|
| Kaos | K01 Kaos krem depan · K02 Kaos krem belakang · K03 Kaos cokelat tua badge · K04 Kaos putih greetings · K05 Kaos pasir kayak · K06 Hoodie Driftwood |
| Topi | T01 Topi baseball · T02 Bucket hat |
| Tas | B01 Tote bag kanvas · B02 Pouch serbaguna |
| Drinkware | D01 Mug keramik · D02 Mug enamel · D03 Tumbler stainless |
| Tekstil | X01 Handuk pantai · X02 Sarung pantai / bandana |
| Aksesoris | A01 Gantungan akrilik · A02 Gantungan kayu · A03 Pin enamel + kartu · A04 Magnet kulkas · A05 Tatakan gelas |
| Alat tulis | S01 Buku catatan A5 · S02 Set kartu pos · S03 Lembar stiker |
| Kemasan | P01 Paper bag oleh-oleh · P02 Hang tag & label |

Mockup: `mockup/` (dengan nama produk) dan `mockup-clean/` (tanpa teks, untuk katalog/Instagram).

## 3. Warna (berikan ke vendor)
| Nama | HEX | Dipakai di |
|---|---|---|
| Golden Hour | `#FDB15D` | Atas matahari bergaris |
| Coral Glow | `#FF8A5C` | Bawah matahari bergaris |
| Driftwood | `#A67C64` | Logo, garis, teks |
| Driftwood Deep | `#5A3E31` | Teks tebal, kaos cokelat tua |
| Shell Cream | `#FBF4EC` | Tinta krem di kain gelap |

Minta vendor mencocokkan warna tinta dengan kode HEX di atas dan **minta sampel cetak** sebelum produksi massal. Warna layar dan warna tinta/kain bisa berbeda.

## 4. Catatan penting
- **Sablon manual (screen printing):** gradasi matahari (emas → coral) sulit disablon manual. Untuk sablon, gunakan 2 warna padat (emas & coral, tanpa gradasi). Untuk DTF/sublimasi, gradasi aman.
- **Logo asli masih berupa gambar (PNG), bukan vektor.** Aman untuk cetak ukuran kecil–sedang (dada, stiker, gantungan kunci). Untuk cetak besar (punggung kaos A1, spanduk) dan **bordir/pin**, sebaiknya logo asli dibuat ulang dalam format vektor (AI/SVG) oleh desainer, agar garis daun dan tulisan tetap tajam.
- **Bordir topi** memakai simbol matahari (bentuk sederhana) karena tulisan kuas pada logo asli terlalu halus untuk dibordir kecil.
- Teks pada artwork: "Tempat senja pulang", "Where every day ends beautifully", "Paddle into the sunset", "Pantai Sunari · Selayar". Ubah di `merch/build_art.py` / `merch/build_mockups.py` lalu jalankan `python3 merch/build_art.py && python3 merch/build_mockups.py && node merch/render.js`.
