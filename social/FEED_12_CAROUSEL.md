# SunaRi: 12 Carousel Feed (sesuai preview profil)

File: `social/feed-12-carousel/NN-nama/01.png …` (1080 × 1350). Slide 01 = gambar yang tampil di grid.
**Urutan upload: dari 12 ke 01** (postingan terakhir muncul di kiri atas grid).

| No | Folder | Slide | Isi |
|---|---|---|---|
| 01 | `01-lebih-dari-menginap` | 5 | Duduk & menikmati · makan malam di resto · malam di resort · CTA |
| 02 | `02-senja-hari-ini` | 8 | Jam senja · 6 foto senja (teras, kayak, taman) · tips menikmati senja |
| 03 | `03-vip-superior` | 6 | Room tour VIP Superior (bathtub & air panas) |
| 04 | `04-malam-di-sunari` | 8 | Langit biru · bangunan utama · taman berlampu · jalan setapak · resto malam · lilin · info malam |
| 05 | `05-vip-standard` | 6 | Room tour VIP Standard |
| 06 | `06-tempat-senja-pulang` | 5 | Kutipan · cerita nama SunaRi · perahu nelayan · tempat senja pulang |
| 07 | `07-pantai-sepi` | 8 | Pantai sepi · pagi tenang · ayunan raksasa · pantai landai & aman · senja di depan mata · duduk sampai gelap · info pantai |
| 08 | `08-sewa-kayak` | 5 | Kayak sore · single/double · harga kayak |
| 09 | `09-family-superior` | 6 | Room tour Family Superior |
| 10 | `10-menginap-menjelajah` | 6 | Menginap. Menjelajah. Melambat. Pulang. (1 slide per kata) |
| 11 | `11-staycation-senja` | 5 | Superior Bungalow · Senja Dinner · teras · info paket |
| 12 | `12-superior` | 6 | Room tour Superior |

Sumber desain: bagian `FEED12` dan `ROOMS` di `social/build_kit.py`. Susun ulang folder dengan `python3 social/assemble_feed12.py`.

⚠️ Perlu dicek:
- **11 Staycation Senja:** paket ini masih contoh. Pastikan isi paketnya disetujui sebelum diposting.
- **07 Pantai Sepi:** slide ayunan raksasa: "spot foto favorit … gratis" (dikonfirmasi gratis).
- Slide 01 dari no. 01, 04, 06, 07, 08, 10 adalah tile feed tanpa tulisan "Geser →"; di Instagram ikon carousel tetap muncul otomatis.
