# 1. Judul Proyek

**Numerasa: Eksplorasi Numerasi dalam Kehidupan Sehari-hari**

# 2. Latar Belakang

Numerasi merupakan kemampuan menggunakan konsep matematika untuk menyelesaikan permasalahan dalam kehidupan sehari-hari. Namun, siswa SMP terkadang masih mengalami kesulitan dalam menerapkan konsep matematika pada situasi nyata.

Oleh karena itu, Numerasa dirancang sebagai program berbasis Python yang menyediakan latihan soal numerasi dengan konteks kehidupan sehari-hari. Program ini diharapkan dapat membantu siswa berlatih berhitung dan memahami penerapan matematika melalui soal-soal sederhana dan interaktif.

# 3. Pengguna dan Tujuan

**Pengguna:** Siswa Sekolah Menengah Pertama (SMP).

**Tujuan:** Membantu siswa melatih kemampuan numerasi melalui latihan soal yang berkaitan dengan kehidupan sehari-hari.

**User Story:**

Sebagai siswa SMP, saya ingin mengerjakan latihan soal numerasi yang berkaitan dengan kehidupan sehari-hari, agar saya dapat melatih kemampuan berhitung dan menerapkan konsep matematika dalam situasi nyata.

# 4. Ruang Lingkup

Numerasa merupakan program berbasis terminal menggunakan bahasa pemrograman Python.

Materi latihan dibatasi pada tiga kategori:
1. Aritmetika sehari-hari.
2. Belanja dan diskon.
3. Perbandingan.

Program berfokus pada penyajian soal, pemeriksaan jawaban, dan perhitungan nilai. Program tidak menggunakan antarmuka grafis, website, database, maupun layanan eksternal.

# 5. Kebutuhan

## A. Kebutuhan Fungsional

| Kode | Kebutuhan | Prioritas |
|---|---|---|
| F01 | Menampilkan pilihan kategori latihan numerasi. | Wajib |
| F02 | Menghasilkan soal sesuai kategori yang dipilih. | Wajib |
| F03 | Menerima dan memeriksa jawaban pengguna. | Wajib |
| F04 | Menghitung dan menampilkan nilai latihan. | Wajib |
| F05 | Menyimpan hasil latihan ke dalam file teks. | Tambahan |

## B. Kebutuhan Nonfungsional

1. Program dapat dijalankan melalui terminal di Visual Studio Code.
2. Program menggunakan bahasa pemrograman Python.
3. Menu dan instruksi mudah dipahami oleh siswa SMP.
4. Program memiliki validasi terhadap masukan pengguna.
5. Program dapat digunakan kembali untuk latihan berikutnya.

# 6. IPO (Input, Process, Output)

| Input | Process | Output |
|---|---|---|
| Pilihan kategori latihan | Memeriksa pilihan kategori | Kategori latihan yang dipilih |
| Jawaban pengguna | Membandingkan jawaban dengan kunci jawaban | Informasi benar atau salah |
| Jumlah jawaban benar | Menghitung nilai latihan | Nilai akhir pengguna |
| Hasil latihan | Menyimpan hasil ke file teks jika fitur digunakan | File hasil latihan |

# 7. Algoritma

## Pseudocode

MULAI
    Tampilkan judul program Numerasa
    Tampilkan menu kategori latihan
    Baca pilihan pengguna

    Jika pilihan valid:
        Buat soal sesuai kategori
        Atur nilai awal = 0

        Untuk setiap soal:
            Tampilkan soal
            Baca jawaban pengguna

            Jika jawaban benar:
                Tambahkan nilai

            Tampilkan hasil pemeriksaan jawaban

        Hitung nilai akhir
        Tampilkan nilai akhir

        Jika fitur penyimpanan digunakan:
            Simpan hasil latihan ke file teks
    Jika pilihan tidak valid:
        Tampilkan pesan kesalahan

SELESAI

# 8. Struktur Program

Program dirancang menggunakan beberapa file Python dengan pembagian fungsi sebagai berikut:

| File | Fungsi |
|---|---|
| `main.py` | Menjalankan program dan menampilkan menu utama. |
| `analisis.py` | Mengelola soal, pemeriksaan jawaban, dan perhitungan nilai. |
| `data_io.py` | Mengelola penyimpanan hasil latihan. |
| `utilitas.py` | Menyediakan fungsi pendukung program. |

# 9. Struktur Data

Struktur data yang direncanakan:

1. **List:** Menyimpan kumpulan soal dan pilihan latihan.
2. **Dictionary:** Menyimpan informasi soal, seperti pertanyaan, jawaban, dan kategori.
3. **String:** Menyimpan teks pertanyaan, pesan program, dan hasil latihan.
4. **Integer:** Menyimpan jawaban numerik dan nilai latihan.

# 10. Test Case

| ID | Kategori | Input/Kondisi | Hasil yang Diharapkan |
|---|---|---|---|
| TC01 | Normal | Pengguna memilih kategori aritmetika. | Program menampilkan soal aritmetika. |
| TC02 | Normal | Pengguna memasukkan jawaban yang benar. | Program menampilkan informasi jawaban benar. |
| TC03 | Normal | Pengguna menyelesaikan seluruh soal. | Program menampilkan nilai akhir. |
| TC04 | Batas | Pengguna memilih nomor kategori terakhir yang tersedia. | Program menampilkan kategori yang sesuai. |
| TC05 | Tidak valid | Pengguna memasukkan pilihan menu di luar pilihan tersedia. | Program menampilkan pesan kesalahan. |
| TC06 | Tidak valid | Pengguna memasukkan jawaban dengan format yang tidak sesuai. | Program meminta pengguna memasukkan jawaban kembali. |

# 11. Pembagian Tugas

Proyek dikerjakan secara individu oleh:

**Nama:** Elga Greena Rahma Tazkia

Tanggung jawab:
1. Merancang konsep dan kebutuhan program.
2. Menyusun algoritma dan struktur program.
3. Mengembangkan program menggunakan Python.
4. Melakukan pengujian dan debugging.
5. Menyusun dokumentasi dan mengelola repository GitHub.

# 12. Jadwal

| Tahap | Kegiatan | Target |
|---|---|---|
| P14 | Menyusun proposal, kebutuhan, IPO, pseudocode, struktur program, dan test case. | Rancangan proyek selesai. |
| P15 | Mengimplementasikan fitur program, melakukan integrasi, pengujian, dan debugging. | Program awal dapat dijalankan. |
| P16 | Menyelesaikan dokumentasi, menyiapkan demonstrasi, dan melakukan evaluasi proyek. | Proyek siap dipresentasikan. |

# 13. Repository

**Nama Repository:** `numerasa-elgagreena-2225250049`

**GitHub:** https://github.com/elgagreena/numerasa-elgagreena-2225250049