def tampilkan_menu():
    print("\n=== NUMERASA ===")
    print("Eksplorasi Numerasi dalam Kehidupan Sehari-hari")
    print("1. Aritmetika Sehari-hari")
    print("2. Belanja dan Diskon")
    print("3. Perbandingan")

    pilihan = input("Pilih kategori (1-3): ")
    return pilihan


def input_jawaban():
    while True:
        try:
            jawaban = int(input("Masukkan jawabanmu: "))
            return jawaban
        except ValueError:
            print("Input harus berupa angka. Silakan coba lagi.")