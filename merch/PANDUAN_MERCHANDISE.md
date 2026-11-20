# SunaRi: Desain Souvenir & Oleh-oleh

**Isi folder `merch/`:**
- `artwork/`: **file untuk dicetak/ditempel** (PNG transparan, resolusi tinggi). Ini file yang dikirim ke tukang sablon/percetakan.
- `mockup/`: gambar contoh produk jadi (untuk presentasi, katalog toko oleh-oleh, atau promosi Instagram).
- `merch-overview.png`: semua produk dalam satu gambar.
- Logo asli untuk dada kiri / bordir: `assets/logo-sunari-driftwood.png` dan `assets/logo-sunari-cream.png`.

---

## 1. Daftar artwork (siap cetak)

| Kode | File | Ukuran file | Ukuran cetak disarankan | Untuk |
|---|---|---|---|---|
| A1 | `A1-back-print-light.png` (tinta cokelat, kain terang) / `A1-back-print-dark.png` (tinta krem, kain gelap) | 3000 × 3750 px | Punggung kaos 25 × 31 cm | Kaos belakang, tote bag besar, poster |
| A2 | `A2-typography-light.png` / `A2-typography-dark.png` | 3000 × 2700 px | Dada 20–25 cm, tote 25 cm | Kaos depan, tote bag, mug, hoodie |
| A3 | `A3-sticker-round.png` | 3000 × 3000 px | Stiker Ø 5–8 cm, gantungan kunci Ø 5 cm | Stiker, gantungan kunci akrilik, tatakan gelas |
| A4 | `A4-kayak-light.png` / `A4-kayak-dark.png` | 3000 × 2700 px | Dada 20–25 cm | Kaos, tumbler, stiker |
| A5 | `A5-pattern-tile.png` | 3000 × 3000 px | Diulang (tile) berapa pun | Bandana, sarung pantai, kertas kado, kain |
| A6 | `A6-mark-pin.png` | 1800 × 1800 px | Pin Ø 3 cm, bordir 6–8 cm | Pin enamel, bordir topi |
| A7 | `A7-sun-stripes.png` | 1800 × 1800 px | Bebas | Mug, stiker, aksen kemasan |

Akhiran **-light** = untuk kain/benda berwarna terang (krem, putih, natural).
Akhiran **-dark** = untuk kain/benda berwarna gelap (cokelat tua, hitam, navy).

## 2. Produk & cara produksi

| Produk | Artwork | Bahan / warna | Teknik yang disarankan |
|---|---|---|---|
| Kaos krem: depan | Logo asli dada kiri ±9 cm | Katun combed 24s/30s, krem | Sablon plastisol 1 warna atau DTF |
| Kaos krem: belakang | A1 light | sama | DTF (gradasi matahari tetap halus) |
| Kaos cokelat tua | A2 dark | katun, cokelat tua | Sablon 2 warna (krem + emas) atau DTF |
| Kaos putih | A4 light | katun, putih | DTF |
| Tote bag | A2 light | kanvas natural | Sablon 2 warna |
| Topi | A6 / simbol krem | topi baseball, Driftwood | **Bordir** 1 warna krem |
| Mug | A7 + teks "SunaRi" | mug keramik putih | Print sublimasi |
| Tumbler | A4 light | tumbler krem | Print UV / sublimasi |
| Gantungan kunci | A3 | akrilik bening 3 mm | Print UV 2 sisi |
| Stiker | A3, A4, A7, simbol | vinyl, potong bentuk (die-cut) | Print vinyl + laminasi doff |
| Kartu pos | Foto senja + logo krem | art carton 260 gsm, 15 × 10 cm | Cetak offset/digital |
| Pin enamel | A6 | logam emas, enamel krem & cokelat | Soft enamel (pesan ke vendor pin) |
| Bandana / sarung pantai | A5 (diulang) | rayon/katun | Print kain (digital textile) |

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
- Teks pada artwork: "Tempat senja pulang", "Where every day ends beautifully", "Paddle into the sunset", "Pantai Sunari · Selayar". Ubah di `merch/build_art.py` lalu jalankan `python3 merch/build_art.py && node merch/render.js`.
