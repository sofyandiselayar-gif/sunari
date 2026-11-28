# Katalog WhatsApp Business: Sewa Kayak

Gambar 1080 × 1080 (persegi 1:1). **2 item katalog** (Kayak Single & Kayak Double, masing-masing 6 gambar) + **1 gambar daftar harga** untuk dikirim langsung di chat atau Status.
Harga kayak **boleh** dicantumkan (lihat `brand/BRAND_GUIDE.md`).
Untuk membuat ulang: `python3 social/build_kayak_wa.py && node social/render_kayak_wa.js`

---

## 1. Gambar

### Item 1: Kayak Single
| No | File | Isi |
|---|---|---|
| 1 | `wa-kayak-single-01.png` | **Sampul** + harga Rp 50.000 (foto utama) |
| 2 | `wa-kayak-single-02.png` | Matahari merah |
| 3 | `wa-kayak-single-03.png` | Menuju matahari |
| 4 | `wa-kayak-single-04.png` | Matahari tenggelam |
| 5 | `wa-kayak-single-05.png` | Jalur cahaya |
| 6 | `wa-kayak-single-06.png` | Kartu info & harga |

### Item 2: Kayak Double
| No | File | Isi |
|---|---|---|
| 1 | `wa-kayak-double-01.png` | **Sampul** + harga Rp 100.000 (foto utama) |
| 2 | `wa-kayak-double-02.png` | Berdua di atas air |
| 3 | `wa-kayak-double-03.png` | Golden hour |
| 4 | `wa-kayak-double-04.png` | Pulau di cakrawala |
| 5 | `wa-kayak-double-05.png` | Jalur cahaya |
| 6 | `wa-kayak-double-06.png` | Kartu info & harga |

### Daftar harga (bukan item katalog)
`wa-kayak-harga.png`: Single & Double dalam satu gambar. Kirim di chat saat tamu bertanya, pasang di Status, atau sertakan bersama balasan cepat `/kayak`.

---

## 2. Isian item katalog (siap salin)

### Item 1: Kayak Single

**Nama barang**
```
Sewa Kayak Single (1 Orang)
```

**Harga**
```
50000
```
Mata uang: **IDR**.

**Deskripsi**
```
Mendayung sendiri menyongsong senja di Pantai Sunari 🛶🌅

Rp 50.000 per kayak, untuk 1 orang.

TERMASUK
• Pelampung (life jacket), wajib dipakai
• Dayung

WAKTU TERBAIK
• 17.00 turun ke air
• ±17.50 matahari terbenam
• 18.10 sudah kembali di pantai

CATATAN
• Air Pantai Sunari tenang dan landai
• Anak wajib didampingi orang dewasa

CARA PESAN
Ketuk "Kirim pesan", tulis tanggal & jam sewa. Kami siapkan kayaknya.

SunaRi Beach Resort · Pantai Sunari, Kepulauan Selayar
```

**Kode barang**
```
SUNARI-KAYAK-SINGLE
```

### Item 2: Kayak Double

**Nama barang**
```
Sewa Kayak Double (2 Orang)
```

**Harga**
```
100000
```
Mata uang: **IDR**.

**Deskripsi**
```
Senja untuk berdua, dari atas air di Pantai Sunari 🛶🌅

Rp 100.000 per kayak, untuk 2 orang.

TERMASUK
• 2 pelampung (life jacket), wajib dipakai
• 2 dayung

WAKTU TERBAIK
• 17.00 turun ke air
• ±17.50 matahari terbenam
• 18.10 sudah kembali di pantai

CATATAN
• Air Pantai Sunari tenang dan landai
• Cocok untuk pasangan, sahabat, atau orang tua & anak
• Anak wajib didampingi orang dewasa

CARA PESAN
Ketuk "Kirim pesan", tulis tanggal & jam sewa. Kami siapkan kayaknya.

SunaRi Beach Resort · Pantai Sunari, Kepulauan Selayar
```

**Kode barang**
```
SUNARI-KAYAK-DOUBLE
```

**Link** (opsional, untuk kedua item)
```
https://maps.app.goo.gl/iUWWHNCT7Vyu4i537
```

---

## 3. Cara menambahkan ke katalog

1. Buka **WhatsApp Business**.
2. Android: **⋮ → Alat bisnis → Katalog**. iPhone: **Pengaturan → Alat bisnis → Katalog**.
3. Ketuk **Tambah item baru** (➕).
4. **Tambah gambar**: pilih 6 gambar item **berurutan 01 → 06**. Gambar pertama menjadi foto utama.
5. Isi **Nama**, **Harga**, **Deskripsi**, **Kode barang** dari bagian 2 → **Simpan**.
6. Ulangi untuk item kedua.
7. *(Opsional)* Kelompokkan dalam **Koleksi** bernama `Sewa Kayak`: Katalog → **Koleksi → Buat koleksi** → pilih kedua item.

WhatsApp meninjau item (beberapa menit sampai 24 jam).

---

## 4. Membagikan

- Buka item atau koleksi → **bagikan** → **Salin link** (`https://wa.me/p/<ID-item>/6282189033044`).
- Ganti balasan cepat `/kayak` agar menyertakan link katalog dan gambar `wa-kayak-harga.png`:

```
Sewa kayak di Pantai Sunari 🛶
• Single (1 orang): Rp 50.000
• Double (2 orang): Rp 100.000
Termasuk pelampung & dayung.

Paling seru jam 17.00 menjelang senja 🌅
Lihat katalog: [link katalog kayak]
```

- Link WA langsung (pesan sudah terisi): [Sewa kayak](https://wa.me/6282189033044?text=Halo%20SunaRi%2C%20saya%20mau%20sewa%20kayak.%0ATanggal%3A%20%0AJam%3A%20%0ASingle%20%2F%20Double%3A%20%0AJumlah%20kayak%3A%20)

---

## 5. Perlu dikonfirmasi

- [ ] **Durasi sewa**: harga per sesi senja, per jam, atau tanpa batas waktu? Bila ada batas, tambahkan di deskripsi.
- [ ] Apakah tamu yang tidak menginap juga boleh menyewa?
- [ ] Batas usia anak (bila ada).
