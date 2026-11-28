# SunaRi: Story "Satu Hari di SunaRi" (5 hari, 1 frame per hari)

Desain siap unggah: `social/satu-hari/hari-01-pagi.png` … `hari-05-ajakan.png` (1080 × 1920).
Sumber: `social/build_satu_hari.py` + `social/render_satu_hari.js`
(edit teks/foto lalu jalankan `python3 social/build_satu_hari.py && node social/render_satu_hari.js`).

**Alur:** Pagi → Siang → Senja → Malam → Ajakan reservasi. Tiap frame berdiri sendiri, punya penanda hari (titik 1–5) dan teaser "Besok: …" supaya orang kembali melihat story berikutnya.

**Jam unggah yang disarankan:** 07.00–08.00 (Hari 1), 12.00 (Hari 2), 16.30 (Hari 3), 19.00 (Hari 4), 16.00–17.00 (Hari 5).
Tambahkan semua ke highlight **Satu Hari** setelah hari ke-5.

| Hari | File | Stiker (letakkan di area kosong bawah, di bawah teaser "Besok") |
|---|---|---|
| 1 Pagi | `hari-01-pagi.png` | **Polling**: "Pagi ala kamu?" · "Kopi ☕" / "Teh 🍵" |
| 2 Siang | `hari-02-siang.png` | **Slider emoji** 🏖️: "Seberapa pengen rebahan di sini?" |
| 3 Senja | `hari-03-senja.png` | **Hitung mundur**: "Senja di SunaRi", isi jam senja hari itu (sekitar 17.58 WITA akhir November, cek pengamatan langsung) |
| 4 Malam | `hari-04-malam.png` | **Pertanyaan**: "Malam terbaikmu di pantai seperti apa?" |
| 5 Ajakan | `hari-05-ajakan.png` | **Tautan**: `https://wa.me/6282189033044?text=Halo%20SunaRi%2C%20saya%20mau%20reservasi`, teks tombol "Reservasi sekarang" |

## Story pendukung (opsional, dari HP)
- Hari 1: video 5 detik nelayan lewat atau secangkir kopi di teras.
- Hari 2: video kaki di pasir / kayak disewakan.
- Hari 3: video matahari menyentuh laut, teks jam asli (mis. "17.57 WITA ✨").
- Hari 4: video lampu gazebo menyala dengan suara ombak.
- Hari 5: repost jawaban terbaik dari kotak pertanyaan Hari 4.

## Catatan
- Foto dipakai: `pantai/02`, `pantai/04`, `senja/57`, `graded/malam__20`, `pantai/03` (semua tanpa wajah tamu/watermark).
- Teks sengaja ditaruh di atas area bawah 430 px, supaya stiker dan kolom balasan Instagram tidak menutupinya.
