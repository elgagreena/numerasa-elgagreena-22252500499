def tampilkan_soal(soal):
    print("\n=== SOAL NUMERASA ===")
    print(soal["pertanyaan"])


def tampilkan_hasil(benar):
    if benar:
        print("Jawaban kamu benar!")
    else:
        print("Jawaban kamu belum tepat.")


def tampilkan_nilai(jumlah_benar, total_soal, nilai):
    print("\n=== HASIL LATIHAN ===")
    print(f"Jumlah soal: {total_soal}")
    print(f"Jawaban benar: {jumlah_benar}")
    print(f"Jawaban salah: {total_soal - jumlah_benar}")
    print(f"Nilai akhir: {nilai:.2f}")