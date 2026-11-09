# Test Case Numerasa

Pengujian dilakukan untuk memastikan program Numerasa dapat menangani kondisi normal, batas, dan masukan tidak valid. Hasil pengujian dicatat berdasarkan keluaran aktual program.

| ID | Kategori | Input/Kondisi | Hasil yang Diharapkan | Hasil Aktual | Status |
|---|---|---|---|---|---|
| TC01 | Normal | Pengguna memilih kategori aritmetika sehari-hari (1). | Program menampilkan soal sesuai kategori. | Program menampilkan soal kategori Aritmetika Sehari-hari. | Berhasil |
| TC02 | Normal | Pengguna memasukkan jawaban yang benar. | Program menampilkan pesan bahwa jawaban benar. | Program menampilkan pesan "Jawaban kamu benar!". | Berhasil |
| TC03 | Normal | Pengguna memasukkan jawaban yang salah. | Program menampilkan pesan bahwa jawaban salah. | Program menampilkan pesan "Jawaban kamu belum tepat!". | Berhasil |
| TC04 | Normal | Pengguna menyelesaikan seluruh soal dengan jawaban benar. | Program menghitung dan menampilkan nilai akhir. | Program menampilkan 2 jawaban benar, 0 jawaban salah, dan nilai akhir 100.00. | Berhasil |
| TC05 | Batas | Pengguna memilih kategori dengan nomor terbesar (3). | Program menampilkan kategori terakhir dengan benar. | Program menampilkan kategori Perbandingan dengan dua soal berbeda. | Berhasil |
| TC06 | Tidak valid | Pengguna memasukkan pilihan menu di luar pilihan yang tersedia (4). | Program menampilkan pesan kesalahan. | Program menampilkan pesan "Pilihan tidak tersedia. Silakan jalankan kembali program." | Berhasil |
| TC07 | Tidak valid | Pengguna memasukkan jawaban dengan format bukan angka (abc). | Program menampilkan pesan kesalahan dan meminta jawaban kembali. | Program menampilkan pesan "Input harus berupa angka. Silakan coba lagi." dan meminta input ulang. | Berhasil |
| TC08 | Batas | Dua soal ditampilkan dalam satu sesi pada kategori yang sama. | Program tidak menampilkan soal yang sama dua kali. | Dua soal kategori Perbandingan berhasil ditampilkan tanpa pengulangan. | Berhasil |
| TC09 | Tidak valid | Pengguna memasukkan huruf pada pilihan kategori (abc). | Program menampilkan pesan kesalahan. | Program menampilkan pesan "Pilihan tidak tersedia. Silakan jalankan kembali program." | Berhasil |