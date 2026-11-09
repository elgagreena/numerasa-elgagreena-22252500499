# NUMERASA
### Eksplorasi Numerasi dalam Kehidupan Sehari-hari

## Deskripsi
Numerasa merupakan program latihan numerasi berbasis Python yang ditujukan untuk siswa SMP. Program ini menyediakan soal-soal kontekstual yang berkaitan dengan kehidupan sehari-hari agar pengguna dapat melatih kemampuan berhitung dan menerapkan konsep matematika dalam situasi nyata.

## Fitur
- Menampilkan menu tiga kategori latihan.
- Menampilkan soal numerasi secara acak sesuai kategori.
- Menerima dan memeriksa jawaban pengguna.
- Menampilkan hasil jawaban benar atau salah.
- Menghitung dan menampilkan nilai akhir latihan.

Kategori latihan:
1. Aritmetika Sehari-hari
2. Belanja dan Diskon
3. Perbandingan

## Persyaratan
- Python 3.x
- Program dijalankan melalui terminal.

Program dikembangkan dan diuji menggunakan Python 3.13.15.

## Cara Menjalankan
1. Buka folder proyek Numerasa di Visual Studio Code.
2. Buka terminal.
3. Jalankan perintah berikut:

```bash
python main.py
```

4. Pilih kategori latihan yang tersedia.
5. Jawab soal yang ditampilkan hingga selesai.

## Struktur Folder
```text
numerasa/
├── README.md
├── proposal.md
├── .gitignore
├── main.py
├── data/
│   └── nilai_contoh.txt
├── src/
│   ├── __init__.py
│   ├── input_data.py
│   ├── proses.py
│   └── output.py
├── tests/
│   └── test_case.md
├── docs/
│   ├── bug_log.md
│   └── screenshot/
│       ├── uji-aritmetika.png
│       ├── uji-belanja-dan-diskon.png
│       ├── uji-perbandingan.png
│       ├── uji-input-menu.png
│       └── uji-input-jawaban.png
└── output/
    └── .gitkeep
```

## Test Case

| ID | Input/Kondisi | Hasil yang Diharapkan | Hasil Aktual | Status |
|---|---|---|---|---|
| TC01 | Memilih kategori 1. | Soal aritmetika ditampilkan. | Soal kategori Aritmetika Sehari-hari ditampilkan. | Berhasil |
| TC02 | Memasukkan jawaban benar. | Pesan jawaban benar ditampilkan. | Pesan "Jawaban kamu benar!" ditampilkan. | Berhasil |
| TC03 | Memasukkan jawaban salah. | Pesan jawaban salah ditampilkan. | Pesan "Jawaban kamu belum tepat!" ditampilkan. | Berhasil |
| TC04 | Menjawab seluruh soal dengan benar. | Nilai akhir dihitung. | Nilai akhir 100.00 ditampilkan. | Berhasil |
| TC05 | Memilih kategori 3. | Kategori terakhir ditampilkan. | Dua soal Perbandingan yang berbeda ditampilkan. | Berhasil |
| TC06 | Memasukkan pilihan menu 4. | Pesan kesalahan ditampilkan. | Pesan pilihan tidak tersedia ditampilkan. | Berhasil |
| TC07 | Memasukkan jawaban `abc`. | Pesan kesalahan dan input ulang ditampilkan. | Pesan input harus berupa angka ditampilkan. | Berhasil |
| TC08 | Menampilkan dua soal dalam satu sesi. | Soal tidak berulang. | Dua soal berbeda ditampilkan. | Berhasil |
| TC09 | Memasukkan `abc` pada pilihan menu. | Pesan kesalahan ditampilkan. | Pesan pilihan tidak tersedia ditampilkan. | Berhasil |

## Known Issues
- Setiap kategori saat ini memiliki dua soal.
- Program belum menyediakan fitur penyimpanan hasil latihan ke file teks.

## Anggota dan Kontribusi
**Elga Greena Rahma Tazkia**

Bertanggung jawab atas perancangan proyek, implementasi program, pengujian, dokumentasi, serta pengelolaan repositori GitHub.

## Referensi/Bantuan
- Bahan Ajar Algoritma dan Pemrograman Pertemuan 14 dan 15.
- Python 3 Documentation.
- Visual Studio Code Documentation.
- GitHub Docs.
- ChatGPT digunakan sebagai bantuan dalam memahami materi, penyelesaian kendala pemrograman, dan penyusunan dokumentasi. Implementasi dan pengujian program dilakukan serta diperiksa kembali oleh pengembang.