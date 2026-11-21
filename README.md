# SunaRi Beach Resort Selayar

Aset brand untuk resort tepi pantai di Kepulauan Selayar dengan pemandangan matahari terbenam.

| Folder | Isi |
|---|---|
| `brand/BRAND_GUIDE.md` | Panduan brand: cerita, positioning, warna, tipografi, tone, strategi media sosial |
| `brand/palette-reference.jpg` | Referensi palet warna |
| `assets/` | Logo satu warna: Driftwood (utama) & Shell Cream (latar gelap); logo lama di `assets/original/` |
| `whatsapp/TEMPLATE_WHATSAPP_BUSINESS.md` | Profil, pesan otomatis, 17 balasan cepat, label & katalog WhatsApp Business |
| `ota/DESKRIPSI_OTA_GOOGLE.md` | Deskripsi properti & 5 tipe kamar (ID/EN) untuk OTA dan Google Business Profile |
| `resto/MENU_BAJOY.md` | Menu & jam buka Bajoy Beach Resto + desain menu A4 dan story |
| `social/SLOW_LIVING.md` | Seri "Jeda" (storytelling & slow living): carousel 8 slide, 6 post "Catatan Jeda", 3 story interaktif, 2 skrip Reels & caption (`social/slow-living/`) |
| `assets/maps/` | 7 peta rute Makassar → SunaRi (Indonesia, Sulawesi, 3 rute, rute 1–3, Pulau Selayar), format story 1080×1920 |
| `social/STORY_RUTE.md` | Story "Rute ke SunaRi": 7 story di atas peta (Indonesia → Sulawesi → 3 rute → Pulau Selayar) (`social/story-rute/`) |
| `location-carousel/` | Proyek HTML/CSS carousel 5 slide "Location & Rute Akses" (1080×1350) + export Playwright retina ke `output/` |
| `social/STORY_BOOKING.md` | Story "Cara Reservasi": 6 story alur pemesanan 3 langkah + tautan WhatsApp siap pakai untuk stiker (`social/story-booking/`) |
| `social/KAYAK_TIPS.md` | Carousel 20 slide "Tips Kano/Kayak Saat Senja" (`social/kayak-tips/`) |
| `social/SUNSET_GUIDE.md` | Seri "Panduan Senja": carousel 10 slide + 6 story, waktu terbaik, jam tiba, spot & tips foto sunset (`social/sunset-guide/`) |
| `social/STORY_QNA.md` | Story Q&A "Tanya SunaRi": 16 pertanyaan tamu sebelum menginap + sampul, penutup & template stiker (`social/story-qna/`) |
| `ebook/` | E-book A4 "Panduan Lengkap SunaRi" (22 halaman): kamar, fasilitas, resto & menu, aktivitas, tur pulau, rute, antar-jemput, reservasi & FAQ. PDF `SunaRi_Ebook_Panduan_Lengkap.pdf` + PNG per halaman. Versi English: `SunaRi_Ebook_Guest_Guide_EN.pdf` (`build_ebook_en.py`, `node ebook/render.js en`) |
| `services/` | Dokumen tarif Transfer & Shuttle + paket tur (Gusung, Bahuluang, Polassi & Tambolongan, Open Trip) — PDF A4 & PNG gaya SunaRi, versi English dan Bahasa Indonesia |
| `merch/PANDUAN_MERCHANDISE.md` | Desain souvenir: artwork siap cetak (`merch/artwork/`) & mockup produk (`merch/mockup/`) |
| `social/FEED_12_CAROUSEL.md` | 12 carousel sesuai preview profil (`social/feed-12-carousel/`) |
| `social/HIGHLIGHT_V2.md` | 17 cover highlight baru (event, reservasi, pulau, ayunan, Ramadhan, sunset bulanan) |
| `social/ISI_HIGHLIGHT.md` | Isi 8 highlight (17 story di `social/highlight-stories/`) + carousel FAQ |
| `social/STORY_10_HARI.md` | Rencana story 10 hari + desain `social/stories/` |
| `social/TIKTOK_REELS.md` | Template caption Reels & TikTok (hook, shot, caption, hashtag) |
| `social/INSTAGRAM_BULAN_1.md` | Bio Instagram, highlight, dan 30 caption bulan pertama |
| `social/` | Template Instagram (feed, story, carousel room tour Superior / VIP Superior / Family Superior / Standard / VIP Standard) beserta sumber HTML-nya |
| `assets/photos/` | Foto asli kamar, senja, resto, aktivitas, taman, acara, desa. Lihat `KATALOG_FOTO.md` |

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
