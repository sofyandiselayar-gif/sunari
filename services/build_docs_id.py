"""Versi Bahasa Indonesia dokumen layanan SunaRi (desain sama dengan build_docs.py).
Run: python3 services/build_docs.py && python3 services/build_docs_id.py && node services/render.js"""
import build_docs as B
from build_docs import header, page, table, ul, H, FONTS, CSS

def rp(v): return "Rp " + f"{v:,}".replace(",", ".")
def itin(rows):
    return "<table>" + '<tr><th>Waktu (WITA)</th><th>Kegiatan &amp; program</th></tr>' + "".join(f'<tr><td class="t">{t}</td><td>{a}</td></tr>' for t, a in rows) + "</table>"
DOCS = {}

# ------------------------------------------------------------ 1. Transfer
local = [("Bandara H. Aroeppala ↔ SunaRi Resort", 150000, 300000), ("Pelabuhan Benteng ↔ SunaRi Resort", 200000, 400000), ("Pelabuhan Pamatata ↔ SunaRi Resort", 400000, 800000)]
optA = [(n, "1 Mobil" if n <= 4 else "2 Mobil", v) for n, v in zip(range(1, 9), [1950000, 2000000, 2050000, 2100000, 4050000, 4100000, 4150000, 4200000])]
optB = [(n, "1 Mobil + Bus" if n <= 4 else "2 Mobil + Bus", v) for n, v in zip(range(1, 9), [1100000, 1550000, 2000000, 2450000, 3550000, 4000000, 4450000, 4900000])]
g = lambda n: f"{n} Tamu"
p1 = header("SunaRi Beach Resort Selayar", 'Tarif Layanan <span class="it">Transfer</span> &amp; Shuttle',
            "Layanan transportasi privat: bandara, pelabuhan &amp; shuttle antarkota dari Makassar (1–8 tamu)",
            '<span class="chip"><b>●</b> Kendaraan privat: khusus untuk rombongan Anda</span><span class="chip"><b>●</b> Sudah termasuk kendaraan, sopir, BBM &amp; parkir</span>')
p1 += '<h2><span class="n">01</span>Shuttle Lokal Selayar <span class="it">(sekali jalan)</span></h2><div class="sub">Penjemputan atau pengantaran antara titik transit utama di Selayar dan SunaRi Beach Resort.</div>'
p1 += '<div class="big">' + table(["Rute jemput / antar", "1–4 tamu (1 kendaraan)", "5–8 tamu (2 kendaraan)"], [(r, rp(a) + " / jalan", rp(b) + " / jalan") for r, a, b in local]) + "</div>"
p1 += '<h2><span class="n">02</span>Ketentuan &amp; <span class="it">fasilitas</span></h2>' + ul([
    "<b>Kapasitas kendaraan:</b> 1 mobil memuat maksimal 4 tamu + 4 koper ukuran sedang. Rombongan 5–8 tamu menggunakan 2 kendaraan.",
    "<b>Sudah termasuk:</b> kendaraan privat, sopir profesional, BBM dan biaya parkir standar.",
    "<b>Tiket kapal feri &amp; bus:</b> dihitung per orang sesuai tarif resmi operator. Tiket bus premium/sleeper sudah termasuk biaya penyeberangan feri.",
    "<b>Reservasi:</b> mohon konfirmasi jadwal perjalanan, waktu kedatangan dan data penumpang paling lambat 24 jam sebelumnya (H-1)."])
p1 += '''<div class="cols" style="margin-top:26px"><div class="card price"><div class="caps" style="font-size:9.5px">Check-in resort</div><div class="v">14.00 WITA</div></div>
  <div class="card price"><div class="caps" style="font-size:9.5px">Check-out resort</div><div class="v">12.00 WITA</div></div>
  <div class="card price"><div class="caps" style="font-size:9.5px">Pemesanan</div><div class="v">H-1</div></div></div>
  <div class="card" style="margin-top:14px;text-align:center"><h4>Rencanakan <span class="it">kedatangan Anda</span></h4><p>Kirimkan jadwal pesawat atau kapal Anda saat memesan agar waktu penjemputan bisa kami sesuaikan, dan perjalanan Anda berakhir dengan senja di Pantai Sunari.</p></div>'''
p2 = header("SunaRi Beach Resort Selayar", 'Transfer <span class="it">Makassar</span> ↔ SunaRi', "Antarkota dari Makassar langsung ke SunaRi, termasuk penyeberangan feri (1–8 tamu)")
p2 += '<h2><span class="n">03</span>Pilih <span class="it">opsi Anda</span></h2><div class="sub">Pilih antara Mobil Privat langsung atau Bus Premium + Shuttle.</div>'
p2 += f'''<div class="cols">
  <div><div class="card" style="margin-bottom:8px"><h4>Opsi A · <span class="it">Mobil Privat Penuh</span></h4><p>Perjalanan mobil privat langsung Makassar ↔ Resort, termasuk penyeberangan feri. Paling nyaman &amp; praktis.</p></div>
  {table(["Tamu", "Armada", "Total harga"], [(g(n), f, rp(v)) for n, f, v in optA], right_from=2, hi_last=True)}</div>
  <div><div class="card" style="margin-bottom:8px"><h4>Opsi B · <span class="it">Bus Premium + Shuttle</span></h4><p>Bus sleeper/eksekutif (Makassar–Pamatata) + shuttle privat di Makassar &amp; Selayar. Pilihan lebih hemat.</p></div>
  {table(["Tamu", "Layanan", "Total harga"], [(g(n), f, rp(v)) for n, f, v in optB], right_from=2, hi_last=True)}</div></div>
  <div class="note">*Rincian harga: <b>Mobil Privat</b>: kendaraan Rp 1.900.000/unit + feri Rp 50.000/orang · <b>Bus Premium</b>: shuttle lokal Rp 650.000/unit + bus premium termasuk feri Rp 450.000/orang.</div>'''
DOCS["01_Tarif_Transfer_Shuttle"] = [p1, p2]

# ------------------------------------------------------------ tur
def tour(key, title_html, sub, highlights, rows, prices, incl, excl, car=False):
    gl = lambda n: f"{n} Orang" + (f" ({'1 Mobil' if n <= 4 else '2 Mobil'})" if car else "")
    a = header("SunaRi Beach Resort Selayar · Tur Privat", title_html, sub)
    a += '<h2><span class="n">01</span>Destinasi &amp; <span class="it">sorotan utama</span></h2>'
    hl = "".join(f'<div class="card"><div class="caps" style="font-size:9.5px">{k}</div><h4 style="margin-top:4px">{v}</h4></div>' for k, v in highlights)
    a += f'<div style="display:grid;grid-template-columns:1fr 1fr;gap:10px">{hl}</div>'
    a += '<h2><span class="n">02</span>Jadwal tur <span class="it">(satu hari penuh)</span></h2><div class="itn">' + itin(rows) + '</div>'
    b = '<div style="height:10px"></div><h2 style="margin-top:0"><span class="n">03</span>Pilihan paket &amp; <span class="it">harga per orang</span></h2>'
    b += '<div class="big">' + table(["Jumlah tamu", "Tanpa pemandu (ekonomi)", "Dengan pemandu lokal"], [(gl(n), rp(x) + " /orang", rp(y) + " /orang") for n, x, y in prices], hi_last=True) + '</div>'
    b += f'''<div class="cols" style="margin-top:6px"><div><h2><span class="n">04</span>Paket <span class="it">termasuk</span></h2>{ul(incl)}</div>
      <div><h2><span class="n">05</span>Tidak <span class="it">termasuk</span></h2>{ul(excl, "no")}</div></div>
      <div class="card" style="margin-top:22px;text-align:center"><h4>Sebelum berangkat</h4><p>Sarapan di SunaRi Beach Resort tersedia mulai pukul 07.00 sebelum keberangkatan. Jadwal dapat disesuaikan oleh kapten &amp; pemandu mengikuti cuaca, kondisi laut dan pasang-surut.</p></div>'''
    DOCS[key] = [a, b]

EXCL = ["Pengeluaran pribadi &amp; belanja", "Dokumentasi foto / video tambahan"]
tour("02_Tur_Pulau_Gusung", 'Tur Eksotis <span class="it">Pulau Gusung</span>', "Tur privat satu hari: hopping pulau &amp; snorkeling",
     [("Spot snorkeling 01", "Liang Kareta · taman karang &amp; biota laut"), ("Jelajah pantai", "Pantai Liang Kareta &amp; Pantai Bone Malea"),
      ("Gua &amp; pantai", "Balojaha · gua laut eksotis &amp; spot foto"), ("Spot snorkeling 02", "Jekneia · spot bawah laut terbaik")],
     [("07.00 – 08.00", "Persiapan &amp; sarapan di SunaRi Beach Resort."), ("08.00 – 08.30", "Berangkat dari SunaRi Beach Resort dengan kapal sewa privat."),
      ("08.30 – 09.30", "<b>Spot snorkeling 01 (Liang Kareta):</b> menjelajahi terumbu karang yang indah dan biota laut."), ("09.30 – 10.30", "Mengunjungi Pantai Liang Kareta lalu lanjut ke Pantai Bone Malea."),
      ("10.30 – 11.30", "<b>Pantai &amp; Gua Balojaha:</b> menjelajahi gua laut, sesi foto dan berenang."), ("11.30 – 12.30", "Istirahat makan siang (lunchbox eksklusif disajikan di lokasi)."),
      ("12.30 – 13.30", "<b>Spot snorkeling 02 (Jekneia):</b> menjelajahi taman karang bawah laut Jekneia."), ("13.30 – 14.30", "Waktu bebas, berenang dan aktivitas air (opsional: kayak)."),
      ("15.00", "Perjalanan pulang dan tiba kembali di SunaRi Beach Resort. Tur selesai.")],
     [(1,990000,1740000),(2,615000,990000),(3,490000,740000),(4,427500,615000),(5,390000,540000),(6,365000,490000),(7,347143,454286),(8,333750,427500)],
     ["Sewa kapal privat", "Perlengkapan snorkeling lengkap + pelampung", "Lunchbox + air mineral", "Tiket masuk semua destinasi", "Kapten kapal &amp; kru berpengalaman", "Pemandu lokal (untuk paket dengan pemandu)"],
     EXCL + ["Olahraga air opsional (sewa kano / kayak)", "Tip untuk kapten / kru / pemandu (sukarela)"])
tour("03_Tur_Pulau_Bahuluang", 'Tur Eksotis <span class="it">Pulau Bahuluang</span>', "Jelajah pulau lewat jalur darat &amp; kapal privat",
     [("Titik temu &amp; transit", "Desa Turungan"), ("Spot snorkeling", "Makam Karang"),
      ("Gosong pasir &amp; pantai", "Pasir Timbul &amp; Pantai Bahuluang"), ("Jelajah alam", "Gua Lipang &amp; taman laut")],
     [("07.00 – 08.00", "Sarapan di SunaRi Beach Resort &amp; persiapan tur."), ("08.00 – 09.00", "Perjalanan darat dari SunaRi Beach Resort ke Desa Turungan dengan mobil privat."),
      ("09.00 – 10.00", "Tiba di Desa Turungan (bertemu kapten kapal) &amp; menyeberang ke Pulau Bahuluang."), ("10.00 – 11.00", "<b>Snorkeling di Makam Karang:</b> melihat formasi karang yang unik."),
      ("11.00 – 12.00", "Mengunjungi <b>Pasir Timbul Bahuluang</b> (tergantung pasang-surut air laut)."), ("12.00 – 13.00", "Mengunjungi <b>Pantai Bahuluang</b> &amp; makan siang bersama (lunchbox)."),
      ("13.00 – 14.00", "<b>Jelajah Gua Lipang:</b> petualangan gua &amp; menikmati lanskap eksotis."), ("15.00 – 16.00", "Perjalanan pulang dan tiba kembali di SunaRi Beach Resort. Tur selesai.")],
     [(1,2640000,3540000),(2,1440000,1890000),(3,1040000,1340000),(4,840000,1065000),(5,900000,1080000),(6,790000,940000),(7,711429,840000),(8,652500,765000)],
     ["Transportasi mobil privat (Resort ⇄ Desa Turungan)", "Sewa kapal privat", "Perlengkapan snorkeling lengkap + pelampung", "Lunchbox + air mineral", "Tiket masuk semua destinasi", "Sopir &amp; BBM", "Pemandu lokal (untuk paket dengan pemandu)"],
     EXCL + ["Aktivitas tambahan opsional", "Tip untuk sopir / kapten / pemandu (sukarela)"], car=True)
tour("04_Tur_Polassi_Tambolongan", 'Tur Eksotis <span class="it">Polassi &amp; Tambolongan</span>', "Trekking Bukit Nane, hopping pulau &amp; snorkeling",
     [("Pulau Polassi", "Trekking &amp; Pantai Bukit Nane"), ("Titik temu &amp; transit", "Desa Turungan"),
      ("Pulau Tambolongan", "Spot snorkeling &amp; pantai"), ("Sorotan ikonik", "Pasir Timbul Tambolongan")],
     [("07.00 – 08.00", "Sarapan di SunaRi Beach Resort &amp; persiapan tur."), ("08.00 – 09.00", "Perjalanan darat dari SunaRi Beach Resort ke Desa Turungan dengan mobil privat."),
      ("09.00 – 10.30", "Tiba di Desa Turungan &amp; menyeberang ke Pulau Polassi."), ("10.30 – 11.45", "<b>Trekking Bukit Nane (±15 menit):</b> panorama laut, menikmati pemandangan &amp; berfoto."),
      ("11.45 – 13.00", "Menuju Pantai Bukit Nane, makan siang (lunchbox) dan beristirahat."), ("13.00 – 14.00", "<b>Pantai &amp; spot snorkeling Tambolongan:</b> menjelajahi terumbu karang &amp; berenang."),
      ("14.00 – 15.00", "Mengunjungi <b>Pasir Timbul Tambolongan</b> &amp; waktu bebas untuk bersantai."), ("15.00 – 16.30", "Perjalanan pulang dan tiba kembali di SunaRi Beach Resort. Tur selesai.")],
     [(1,4147500,5047500),(2,2197500,2647500),(3,1547500,1847500),(4,1222500,1447500),(5,1207500,1387500),(6,1047500,1197500),(7,933214,1061786),(8,847500,960000)],
     ["Transportasi mobil privat (Resort ⇄ Desa Turungan)", "Sewa kapal privat", "Perlengkapan snorkeling lengkap + pelampung", "Lunchbox + air mineral", "Tiket masuk Bukit Nane &amp; semua atraksi", "Sopir &amp; BBM", "Pemandu lokal (untuk paket dengan pemandu)"],
     EXCL + ["Aktivitas tambahan opsional", "Tip untuk sopir / kapten / pemandu (sukarela)"], car=True)

# ------------------------------------------------------------ 5. Open trip
o1 = header("SunaRi Beach Resort Selayar · Open Trip", 'Jelajah <span class="it">Pulau Selayar</span>',
            "Open trip wisata bahari 2 hari: temukan surga tersembunyi Sulawesi Selatan")
facts = [("Harga open trip", rp(3000000), "per orang"), ("Durasi", "2 Hari", "hopping pulau"), ("Kuota minimum", "8 Orang", "per keberangkatan"), ("Titik temu", "Penjemputan", "area / pelabuhan Selayar")]
o1 += '<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:10px;margin-top:18px">' + "".join(
    f'<div class="card price"><div class="caps" style="font-size:8.5px">{k}</div><div class="v" style="{"color:#A84A24;font-size:20px" if i == 0 else ("font-size:19px" if i == 3 else "")}">{v}</div><div style="font-size:10.5px;margin-top:2px">{s}</div></div>' for i, (k, v, s) in enumerate(facts)) + "</div>"
def day(n, t, s, items):
    return f'''<h2><span class="n">HARI {n:02d}</span>{t}</h2><div class="sub" style="font-style:italic;font-family:'Playfair Display',serif;font-size:14px;color:#8A5F48">{s}</div>{ul(items, "dot")}'''
o1 += day(1, 'Permata tersembunyi <span class="it">Pulau Gusung</span>', "Pasir putih alami, tebing kapur yang dramatis &amp; terumbu karang yang masih asri", [
    "<b>Penjemputan &amp; briefing:</b> penjemputan rombongan pagi hari di titik temu pelabuhan, briefing keselamatan dan pembagian alat snorkeling.",
    "<b>Pantai Balojaha:</b> hamparan pasir putih yang luas dengan air laut biru toska yang jernih.",
    "<b>Pantai Liang Tarrusu:</b> tebing kapur ikonik dengan pemandangan panorama, cocok untuk foto lanskap.",
    "<b>Pantai Bone Malea:</b> makan siang santai di tepi pantai dengan lunchbox yang baru dimasak.",
    "<b>Pantai Liang Kareta:</b> pantai yang tenang, berenang dan snorkeling di atas taman karang yang terjaga.",
    "<b>Kembali ke pelabuhan:</b> pelayaran pulang dan pengantaran ke titik temu / resort."])
o1 += day(2, 'Keajaiban <span class="it">Bahuluang &amp; Polassi</span>', "Panorama 360° Bukit Nane, pasir timbul, gua laut &amp; Makam Karang", [
    "<b>Berangkat pagi:</b> penjemputan tamu dan pengantaran ke pelabuhan keberangkatan.",
    "<b>Bukit Nane (Pulau Polassi):</b> pendakian ringan menuju panorama 360° perbukitan yang bertemu laut lepas.",
    "<b>Pasi Timbul Polassi:</b> gosong pasir putih yang muncul di tengah laut (tergantung pasang-surut).",
    "<b>Makan siang di pulau:</b> lunchbox hangat yang baru disiapkan, disantap di tepi pantai.",
    "<b>Liang Lipang (Pulau Bahuluang):</b> gua pesisir eksotis dengan formasi batu alami, lengkungan dan tebing kapur.",
    "<b>Snorkeling di Makam Karang:</b> gundukan karang bawah laut yang legendaris, dipenuhi ikan tropis.",
    "<b>Serah terima dokumentasi &amp; perpisahan:</b> pelayaran pulang, penyerahan paket foto &amp; video dan pengantaran."])
o2 = header("SunaRi Beach Resort Selayar · Open Trip", 'Fasilitas &amp; <span class="it">panduan</span>', "Jelajah Pulau Selayar · open trip 2 hari")
o2 += f'''<div class="cols"><div>
  <h2><span class="n">01</span>Termasuk</h2>{ul(["<b>Transportasi darat:</b> antar-jemput pulang-pergi titik temu / pelabuhan di Selayar.", "<b>Sewa kapal:</b> kapal hopping pulau bersama selama 2 hari.",
     "<b>Alat snorkeling:</b> masker, snorkel dan pelampung.", "<b>Tiket &amp; izin:</b> semua spot destinasi &amp; area pulau.", "<b>Makan &amp; minum:</b> lunchbox dan air mineral selama 2 hari.",
     "<b>Pemandu wisata:</b> pemandu lokal berpengalaman dan berlisensi.", "<b>Dokumentasi lengkap:</b> foto &amp; video lanskap dan bawah laut resolusi tinggi."])}
  <h2><span class="n">02</span>Tidak termasuk</h2>{ul(["Tiket pesawat, feri atau transportasi dari/ke Pulau Selayar.", "Penginapan hotel / resort di Selayar.", "Pengeluaran pribadi di luar paket.", "Tip sukarela untuk kru kapal dan pemandu."], "no")}
  <h2><span class="n">03</span>Yang perlu dibawa</h2>{ul(["Baju renang &amp; pakaian ganti kering", "Tabir surya ramah terumbu karang", "Kacamata hitam &amp; topi", "Dry bag tahan air untuk ponsel &amp; kamera", "Sepatu air atau sandal anti-selip"], "dot")}
  </div><div><h2><span class="n">04</span>Syarat &amp; ketentuan</h2><div class="terms">
  <b>1. Kuota minimum</b>Minimal 8 orang per keberangkatan. Jika tidak terpenuhi, penyelenggara dapat menawarkan penyesuaian harga, penjadwalan ulang atau pengembalian dana penuh sesuai kesepakatan.
  <b>2. Cuaca &amp; kondisi laut</b>Cuaca, angin atau gelombang dapat memengaruhi durasi dan rute. Demi keselamatan, kapten dan pemandu dapat mengubah atau mengalihkan spot snorkeling.
  <b>3. Pasang-surut</b>Pasi Timbul Polassi bergantung pada pasang-surut alami; kunjungannya dijadwalkan secara fleksibel di hari itu.
  <b>4. Sinyal ponsel</b>Beberapa pulau terluar memiliki sinyal lemah atau tidak ada sinyal. Selesaikan komunikasi penting sebelum berangkat.
  <b>5. Kebugaran &amp; medan</b>Bukit Nane dan karang pesisir membutuhkan kebugaran sedang. Alas kaki anti-selip sangat disarankan.
  <b>6. Ketepatan waktu</b>Karena ini open trip bersama, ketepatan waktu dan kerja sama membuat jadwal berjalan lancar untuk semua peserta.</div>
  <div class="card" style="margin-top:18px;text-align:center"><div class="caps" style="font-size:9.5px">Rombongan privat</div>
  <p style="font-family:'Playfair Display',serif;font-style:italic;font-size:14.5px;margin-top:6px">Ingin perjalanan privat? Sewa kapal privat dengan jadwal yang bisa disesuaikan tersedia untuk keluarga dan rombongan perusahaan.</p></div>
  </div></div>'''
DOCS["05_Open_Trip_Jelajah_Selayar"] = [o1, o2]

for key, pages in DOCS.items():
    html = "".join(page(p, i + 1, len(pages), "compact" if key.startswith("05") else "") for i, p in enumerate(pages))
    (H / f"{key}.html").write_text(f'<!doctype html><html lang="id"><head><meta charset="utf-8">{FONTS}<style>{CSS}</style></head><body>{html}</body></html>')
print(len(DOCS), "dokumen (ID)")
