# Test Case Numerasa

Pengujian awal dilakukan untuk memastikan rancangan program Numerasa dapat menangani kondisi normal, batas, dan masukan tidak valid.

| ID | Kategori | Input/Kondisi | Hasil yang Diharapkan |
|---|---|---|---|
| TC01 | Normal | Pengguna memilih kategori aritmetika sehari-hari. | Program menampilkan soal sesuai kategori. |
| TC02 | Normal | Pengguna memasukkan jawaban yang benar. | Program menampilkan pesan bahwa jawaban benar. |
| TC03 | Normal | Pengguna memasukkan jawaban yang salah. | Program menampilkan pesan bahwa jawaban salah. |
| TC04 | Normal | Pengguna menyelesaikan seluruh soal. | Program menghitung dan menampilkan nilai akhir. |
| TC05 | Batas | Pengguna memilih kategori dengan nomor terbesar yang tersedia. | Program menampilkan kategori terakhir dengan benar. |
| TC06 | Tidak valid | Pengguna memasukkan pilihan menu di luar pilihan yang tersedia. | Program menampilkan pesan kesalahan dan meminta pilihan kembali. |
| TC07 | Tidak valid | Pengguna memasukkan jawaban dengan format bukan angka. | Program menampilkan pesan kesalahan dan meminta jawaban kembali. |