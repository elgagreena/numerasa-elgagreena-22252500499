# NUMERASA
### Eksplorasi Numerasi dalam Kehidupan Sehari-hari

## 1. Deskripsi Proyek

Numerasa merupakan program pembelajaran numerasi berbasis Python yang dirancang untuk membantu siswa SMP melatih kemampuan berhitung melalui soal-soal yang berkaitan dengan kehidupan sehari-hari.

Program ini dibuat untuk memberikan pengalaman belajar numerasi yang sederhana dan mudah digunakan melalui terminal.

## 2. Fitur Program

Program Numerasa memiliki beberapa fitur utama:
1. Menampilkan menu kategori latihan numerasi.
2. Menyediakan soal berdasarkan kategori yang dipilih.
3. Memeriksa jawaban pengguna.
4. Menghitung dan menampilkan nilai akhir.
5. Menangani input jawaban yang tidak valid.
6. Menghindari pengulangan soal dalam satu sesi latihan.

### Kategori Soal
- Aritmetika Sehari-hari
- Belanja dan Diskon
- Perbandingan

## 3. Teknologi yang Digunakan

- Bahasa pemrograman: Python
- Editor: Visual Studio Code
- Platform: Terminal/Command Prompt
- Version control: Git dan GitHub

## 4. Persyaratan

- Python versi 3.x
- Visual Studio Code
- Terminal untuk menjalankan program

## 5. Cara Menjalankan Program

1. Buka folder proyek Numerasa di Visual Studio Code.
2. Buka terminal.
3. Jalankan perintah berikut:

```bash
python main.py
```

4. Pilih salah satu kategori dengan memasukkan angka 1, 2, atau 3.
5. Jawab soal yang ditampilkan.
6. Program akan menampilkan hasil latihan dan nilai akhir.

## 6. Struktur Folder

```text
numerasa-elgagreena-2225250049/
├── README.md
├── proposal.md
├── main.py
├── .gitignore
├── data/
│   └── nilai_contoh.txt
├── src/
│   ├── __init__.py
│   ├── input_data.py
│   ├── proses.py
│   ├── output.py
│   ├── main.py
│   ├── data_io.py
│   ├── analisis.py
│   └── utilitas.py
├── tests/
│   └── test_case.md
├── output/
│   └── .gitkeep
└── docs/
    ├── bug_log.md
    └── screenshot/
```

## 7. Hasil Pengujian

Pengujian dilakukan untuk memastikan fitur program berjalan sesuai kebutuhan.

Berdasarkan pengujian yang telah dilakukan, seluruh 9 test case berhasil dijalankan dengan hasil sesuai harapan.

Rincian pengujian dapat dilihat pada file `tests/test_case.md`.

## 8. Bug dan Perbaikan

Selama implementasi ditemukan masalah berupa pengulangan soal dalam satu sesi latihan dan ketidaksesuaian parameter fungsi.

Kedua masalah tersebut telah diperbaiki. Catatan lengkap dapat dilihat pada file `docs/bug_log.md`.

## 9. Pengembang

Nama: Elga Greena Rahma Tazkia  
NIM: 22252500499  
Program Studi: Pendidikan Matematika  
Fakultas: FKIP  
Universitas: Universitas Sultan Ageng Tirtayasa

## 10. Referensi dan Bantuan

- Materi perkuliahan Algoritma dan Pemrograman Pendidikan Matematika.
- Dokumentasi resmi Python.
- Bantuan AI ChatGPT dalam proses pengembangan, penelusuran kesalahan, dan penyusunan dokumentasi.