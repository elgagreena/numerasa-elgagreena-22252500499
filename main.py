from src.input_data import tampilkan_menu, input_jawaban
from src.proses import pilih_soal, periksa_jawaban, hitung_nilai
from src.output import tampilkan_soal, tampilkan_hasil, tampilkan_nilai


def jalankan_program():
    print("Selamat datang di NUMERASA!")
    print("Yuk, belajar numerasi melalui kehidupan sehari-hari.")

    kategori = {
        "1": "Aritmetika Sehari-hari",
        "2": "Belanja dan Diskon",
        "3": "Perbandingan"
    }

    pilihan = tampilkan_menu()

    if pilihan not in kategori:
        print("Pilihan tidak tersedia. Silakan jalankan kembali program.")
        return

    print(f"\nKategori: {kategori[pilihan]}")

    jumlah_benar = 0
    total_soal = 2
    soal_terpakai = []

    for nomor in range(total_soal):
        print(f"\nSoal ke-{nomor + 1}")

        soal = pilih_soal(pilihan, soal_terpakai)

        if soal is None:
            print("Soal untuk kategori ini sudah habis.")
            break

        tampilkan_soal(soal)

        jawaban = input_jawaban()
        benar = periksa_jawaban(soal, jawaban)

        tampilkan_hasil(benar)

        if benar:
            jumlah_benar += 1

    nilai = hitung_nilai(jumlah_benar, total_soal)
    tampilkan_nilai(jumlah_benar, total_soal, nilai)

    print("\nTerima kasih sudah belajar bersama NUMERASA!")


if __name__ == "__main__":
    jalankan_program()