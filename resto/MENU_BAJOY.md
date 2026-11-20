# Bajoy Beach Resto: Menu & Jam Buka

**Jam buka**
| Tamu | Buka | Tutup |
|---|---|---|
| Menginap | 07.00 | 21.00 WITA |
| Tidak menginap | 07.00 | 19.00 WITA |

File desain:
- **Edisi elegan (timbul + foil emas):** `Menu_Bajoy_Elegan_A4.pdf` / `.png`, `menu-elegan-story-1-makanan.png`, `menu-elegan-story-2-minuman.png`
- Edisi polos: `Menu_Bajoy_A4.pdf` / `.png`, `menu-story-1-makanan.png`, `menu-story-2-minuman.png`

**Cetak edisi elegan sungguhan:** minta percetakan memakai kertas tekstur (cotton/fancy paper 300+ gsm) dengan **emboss/letterpress** untuk logo, judul dan nama menu, serta **hot print/foil emas** untuk harga dan kata *Resto*. File PNG/PDF menampilkan simulasi efeknya; untuk produksi, percetakan butuh file terpisah per efek (bisa saya siapkan).
Ubah menu/harga di `build_menu.py` (bagian `MENU`), lalu jalankan `python3 resto/build_menu.py && node resto/render.js`.

## Makanan
| Item | Harga |
|---|---|
| Nasi Goreng Sunari | Rp 45.000 |
| Nasi Goreng Seafood | Rp 45.000 |
| Nasi Goreng Egois | Rp 45.000 |
| Nasi Goreng Kampung | Rp 45.000 |
| Ayam Lalapan | Rp 50.000 |
| Ayam Bakar | Rp 50.000 |
| Beef Sandwich | Rp 30.000 |
| Beef Sandwich D. | Rp 40.000 |
| Egg Sandwich | Rp 25.000 |
| Egg Sandwich D. | Rp 35.000 |
| Indomie Goreng | Rp 20.000 |
| Indomie Kuah | Rp 20.000 |

## Snack
| Item | Harga |
|---|---|
| French Fries | Rp 25.000 |
| Toast | Rp 25.000 |
| Banana Roll | Rp 25.000 |
| Fried Cassava | Rp 25.000 |
| Fried Banana | Rp 25.000 |

## Drinks
| Item | Harga |
|---|---|
| Chocolate M.S | Rp 25.000 |
| Oreo M.S | Rp 25.000 |
| Orange Punch | Rp 25.000 |
| Watermelon L.M | Rp 25.000 |
| Green Tea | Rp 25.000 |
| Hot Tea | Rp 10.000 |
| Ice Tea | Rp 20.000 |
| Black Coffee | Rp 20.000 |
| Coffee Milk | Rp 20.000 |
| Milk Tea | Rp 25.000 |
| Original Coconut | Rp 25.000 |
| Saronso | Rp 25.000 |

## Juice
| Item | Harga |
|---|---|
| Avocado | Rp 25.000 |
| Watermelon | Rp 25.000 |
| Melon | Rp 25.000 |
| Mango | Rp 25.000 |
| Dragon Fruit | Rp 25.000 |
| Soursop Fruit | Rp 25.000 |
| Apple | Rp 25.000 |
| Orange | Rp 25.000 |

## Soft Drink
| Item | Harga |
|---|---|
| Coke | Rp 15.000 |
| Fanta | Rp 15.000 |
| Sprite | Rp 15.000 |
| Fresh Tea | Rp 15.000 |
| Pulpy | Rp 15.000 |
| Mineral Water | Rp 10.000 |

## Perlu dikonfirmasi
- Arti singkatan **D.** (Beef/Egg Sandwich D.), **M.S** dan **L.M**. Bisa ditulis lengkap agar tamu asing paham.
- **Ikan bakar** belum ada di daftar menu, padahal disebut di caption & deskripsi. Apakah ikan bakar menu Senja Dinner saja / harga sesuai berat?
- Ejaan yang saya rapikan: *Manggo* → **Mango**, *SeaFood* → **Seafood**.