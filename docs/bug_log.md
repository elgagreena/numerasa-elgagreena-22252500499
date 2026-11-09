# Bug Log Numerasa

Bug log digunakan untuk mencatat masalah yang ditemukan selama proses implementasi dan pengujian program Numerasa beserta penyebab dan perbaikannya.

| ID | Gejala | Penyebab | Perbaikan | Status |
|---|---|---|---|---|
| BUG01 | Soal yang sama dapat muncul dua kali dalam satu sesi latihan. | Fungsi `pilih_soal()` menggunakan `random.choice()` tanpa memeriksa soal yang sudah pernah ditampilkan. | Menambahkan parameter `soal_terpakai` untuk menyimpan soal yang sudah muncul sehingga soal tidak dipilih kembali. | Selesai |
| BUG02 | Program mengalami TypeError ketika fungsi `pilih_soal()` dipanggil dengan dua parameter. | Pemanggilan fungsi pada `main.py` belum sesuai dengan perubahan parameter pada `proses.py`. | Menyesuaikan pemanggilan fungsi menjadi `pilih_soal(pilihan, soal_terpakai)`. | Selesai |