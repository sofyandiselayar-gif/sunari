# Carousel cerita "Senja Hari Ini · Sabtu, 28 Nov 2026" (10 slide, 1080×1350)

Desain di `social/senja-28nov/` (`s28-01…10.png`). Menggantikan carousel "Sunset Moment".
Foto: `assets/photos/senja/85–99`, di-grade dengan look "Senja Hari Ini" → `assets/photos/graded/senja__*`.
Buat ulang: `python3 social/grade_senja_28nov.py && python3 social/build_senja_28nov.py && node social/render_senja_28nov.js`.

Jam di tiap slide = jam pemotretan asli (EXIF), urut dari golden hour sampai afterglow.

| Slide | Jam | Foto | Cerita |
|---|---|---|---|
| 01 | 17.58 | `85` | Sampul: "Satu sore, satu cerita." · Geser, kita mulai dari 17.31 |
| 02 | 17.31 | `97` | Sore baru dimulai |
| 03 | 17.44 | `96` | Laut memanggil |
| 04 | 17.44 | `92` | Matahari turun pelan |
| 05 | 17.56 | `91` | Detik yang dinanti |
| 06 | 17.57 | `88` | Laut menyambutnya |
| 07 | 17.58 | `87` | Semua menghadap barat |
| 08 | 17.59 | `99` | Teh hangat tiba (staf, dari belakang: pastikan staf setuju) |
| 09 | 18.02 | `98` | Cerita belum usai |
| 10 | – | – | Besok sore, giliranmu: Senja berikutnya, tips, WhatsApp 0821-8903-3044 |

Tidak dipakai: `86` (mirip sampul), `93` (mirip `96`), `89/90/94/95` (profil wajah/anak).

## Versi Story (10 frame, 1080×1920)
Desain di `social/senja-28nov-story/` (`s28s-01…10.png`): cerita & urutan sama dengan feed, foto penuh, zona aman atas/bawah ±250 px.
Buat ulang: `python3 social/build_senja_28nov_story.py && node social/render_senja_28nov_story.js`.
Tips upload: tambahkan stiker lagu, dan di frame 10 tambahkan stiker tautan WhatsApp (lihat `social/STORY_BOOKING.md`).

## Caption
Satu sore, satu cerita. 🌅

Sabtu, 28 November di Pantai Sunari. Pukul 17.31 sore baru dimulai: cahaya menyelinap lewat tirai resto. Tak lama, dua sahabat mendayung kayak ke tengah laut yang setenang kaca.

17.57, matahari menyentuh cakrawala. Yang tadi mengobrol pun terdiam, semua menghadap barat. Semenit kemudian teh hangat tiba di meja, pas sekali untuk menutup sore.

Matahari sudah pulang, tapi jingganya masih tinggal. Besok sore, giliranmu yang duduk di sini.

Simpan dulu, biar liburanmu tinggal berangkat, dan tag orang yang ingin kamu ajak menunggu senja bersama.
Info & reservasi: WhatsApp 0821-8903-3044, biar kami bantu.

#sunarisunsetmoment #senjahariini #pantaisunari #selayar #sunsetselayar #senjaselayar #wisataselayar #sulawesiselatan

### Caption alternatif (lebih singkat)
Sabtu sore di Pantai Sunari, dari 17.31 sampai 18.02. 🌅

Cahaya di balik tirai, kayak yang mendayung pelan, dan teh hangat yang tiba tepat saat matahari tinggal segaris. Satu sore, satu cerita, dan besok sore giliranmu.

Simpan untuk liburanmu, tag yang ingin kamu ajak.
WhatsApp 0821-8903-3044, biar kami bantu.

#sunarisunsetmoment #senjahariini #pantaisunari #selayar #sunsetselayar

## Teks & stiker story (per frame)
Story tidak punya caption, jadi tempel teks pendek / stiker ini di tiap frame (letakkan di area kosong, jangan menutupi judul).

| Frame | Teks / stiker |
|---|---|
| 01 | Stiker lagu · teks: "Sore ini di Pantai Sunari 🌅" |
| 02 | "Masih 26 menit lagi…" |
| 03 | Stiker polling: "Kamu tim… 🛶 Kayak / 🪑 Duduk santai" |
| 04 | "Cahayanya sampai ke kaki 🌼" |
| 05 | Stiker kuis/emoji slider: "Seberapa suka senja seperti ini? 🧡" |
| 06 | "17.57. Diam sebentar ya." |
| 07 | Stiker pertanyaan: "Mau menunggu senja bareng siapa?" |
| 08 | "Teh atau kopi untuk sore seperti ini? ☕" (polling) |
| 09 | "Langitnya belum selesai 🌇" |
| 10 | Stiker tautan WhatsApp "Tanya & reservasi" + stiker hashtag #sunarisunsetmoment · lokasi: Pantai Sunari, Selayar |

Setelah diunggah, simpan ke highlight senja (mis. "Senja" / "Kalender Senja").

## Foto siap upload (8 terbaik)
`social/upload-28nov/instagram/` (1080×1350, 4:5 feed) dan `social/upload-28nov/tiktok/` (1080×1920, 9:16: TikTok photo mode, Story, Reels).
Dipilih dari 15 foto berdasarkan ketajaman, komposisi, dan aman dipakai (tanpa wajah/anak). Diekspor dari file asli kamera 4000×3000
(tidak ada yang diperbesar), color grading SunaRi, JPEG kualitas 95 tanpa EXIF/lokasi.
Buat ulang: `python3 social/export_upload_28nov.py <folder foto asli>`.

Urutan prioritas: 01 matahari terbenam (88) · 02 dua tamu di bawah pohon (85) · 03 kamboja & matahari (92) · 04 gazebo & tirai (97) ·
05 kayak & pulau (96) · 06 kayak pastel (93) · 07 kayak langit merah (98) · 08 tamu memotret matahari (91).
05 dan 06 mirip: jangan dipakai bersebelahan.
