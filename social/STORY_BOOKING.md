# Story "Cara Reservasi" (How to Book)

Ada 6 story ukuran 1080×1920 (PNG) di `social/story-booking/`.
Untuk membuat ulang: `python3 social/build_booking.py && node social/render_booking.js`.

| File | Isi | Stiker yang ditambahkan di Instagram |
|---|---|---|
| `booking-01` | Sampul: "Cara Reservasi, cukup 3 langkah lewat WhatsApp" | — |
| `booking-02` | **Langkah 1:** chat admin di WhatsApp + nomor resmi | **Stiker Tautan** di kotak bergaris "ketuk di sini" |
| `booking-03` | **Langkah 2:** data yang dikirim (check-in, check-out, jumlah tamu, tipe kamar, antar-jemput) | — |
| `booking-04` | Daftar 5 tipe kamar & kapasitas (tanpa harga) | — |
| `booking-05` | **Langkah 3:** terima harga → transfer & kirim bukti → booking terkonfirmasi | — |
| `booking-06` | Ajakan "Chat kami sekarang" + nomor WhatsApp | **Stiker Tautan** di kotak bergaris |

## Tautan untuk stiker (salin persis)
```
https://wa.me/6282189033044?text=Halo%20SunaRi%2C%20saya%20mau%20reservasi%20kamar.%0ACheck-in%3A%20%0ACheck-out%3A%20%0AJumlah%20tamu%3A%20...%20dewasa%2C%20...%20anak%0ATipe%20kamar%3A%20%0AAntar-jemput%3A%20ya%20/%20tidak
```
Saat tautan ini diketuk, WhatsApp langsung terbuka ke nomor 0821-8903-3044 dengan pesan yang sudah terisi:
```
Halo SunaRi, saya mau reservasi kamar.
Check-in:
Check-out:
Jumlah tamu: ... dewasa, ... anak
Tipe kamar:
Antar-jemput: ya / tidak
```
Tautan juga tersimpan di `social/booking_link.txt`.

## Cara menempel stiker tautan
1. Unggah `booking-02`, lalu ketuk ikon stiker dan pilih **Tautan** (Link).
2. Tempel tautan di atas.
3. Ketuk **Sesuaikan teks stiker**, lalu tulis `CHAT ADMIN DI SINI`.
4. Ketuk stiker sampai warnanya putih/oranye. Geser stiker ke kotak bergaris "ketuk di sini" dan perbesar sampai menutupi kotaknya.
5. Ulangi untuk `booking-06`.
6. Unggah `booking-01` sampai `booking-06` berurutan, lalu simpan semuanya ke Highlight **Reservasi** (atau **Booking**).

## Tips
- Tempel stiker tautan yang sama juga di bio Instagram (Linktree) dan di caption Google Business.
- Kalau ada perubahan nomor atau isi pesan, ubah `MSG` di `build_booking.py`, lalu buat ulang story-nya.
