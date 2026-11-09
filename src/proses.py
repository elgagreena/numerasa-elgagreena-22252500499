import random

DAFTAR_SOAL = {
    "1": [
        {
            "pertanyaan": "Ibu membeli 3 kg gula. Harga setiap kg Rp14.000. Berapa total harganya?",
            "jawaban": 42000
        },
        {
            "pertanyaan": "Andi memiliki 25 kelereng, lalu mendapat 15 kelereng lagi. Berapa jumlah kelereng Andi sekarang?",
            "jawaban": 40
        }
    ],
    "2": [
        {
            "pertanyaan": "Sebuah tas seharga Rp100.000 mendapat diskon 20%. Berapa harga diskonnya?",
            "jawaban": 20000
        },
        {
            "pertanyaan": "Harga sebuah buku Rp15.000. Jika membeli 3 buku, berapa total yang harus dibayar?",
            "jawaban": 45000
        }
    ],
    "3": [
        {
            "pertanyaan": "Perbandingan jumlah apel dan jeruk adalah 2 : 3. Jika ada 6 apel, berapa jumlah jeruk?",
            "jawaban": 9
        },
        {
            "pertanyaan": "Perbandingan siswa laki-laki dan perempuan adalah 3 : 2. Jika ada 15 siswa laki-laki, berapa siswa perempuan?",
            "jawaban": 10
        }
    ]
}


def pilih_soal(kategori, soal_terpakai):
    soal_tersedia = [
        soal for soal in DAFTAR_SOAL[kategori]
        if soal not in soal_terpakai
    ]

    if not soal_tersedia:
        return None

    soal = random.choice(soal_tersedia)
    soal_terpakai.append(soal)

    return soal


def periksa_jawaban(soal, jawaban):
    return jawaban == soal["jawaban"]


def hitung_nilai(jumlah_benar, total_soal):
    if total_soal == 0:
        return 0

    return (jumlah_benar / total_soal) * 100