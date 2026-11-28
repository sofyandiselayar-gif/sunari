# Story "Menari di SunaRi" (versi tamu)

10 frame PNG HD **2160 × 3840** (9:16, Instagram Story). Tanpa logo SunaRi & tanpa nomor WhatsApp.
Cerita sama dengan carousel `social/menari/`. Unggah berurutan `story-01.png` … `story-10.png` (bisa sekaligus atau 1 per hari).
Sumber: `social/build_menari_story.py` + `social/render_menari_story.js`.

Saran untuk tamu: tambahkan stiker lokasi "Pantai Sunari" dan lagu yang lembut di frame 1.
Area kosong di bagian bawah frame 10 bisa dipakai untuk stiker, tag teman, atau tanggal menginap.

## Versi 1 frame
`menari-satu-frame.png` (2160 × 3840): seluruh cerita dalam satu kolase 9 foto berurutan + judul & penutup.
Sumber: `social/build_menari_satu.py` + `social/render_menari_satu.js`.

## PDF HD
- `Menari_di_SunaRi_Story.pdf`: 10 halaman story.
- `Menari_di_SunaRi_1_Frame.pdf`: 1 halaman kolase.
Ukuran halaman 1080 × 1920 px (9:16), teks vektor (tajam di zoom berapa pun) + foto resolusi penuh. Dibuat dengan `node social/render_menari_pdf.js`.

## JPG HD
Folder `jpg/`: 10 frame story + `menari-satu-frame.jpg`, 2160 × 3840, kualitas 95, subsampling 4:4:4 (teks tetap tajam), ±0,4–2,3 MB per file.
