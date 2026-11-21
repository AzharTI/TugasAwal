def baca_angka(pesan):
    """Meminta input sampai pengguna memasukkan angka yang valid."""
    while True:
        try:
            return float(input(pesan))
        except ValueError:
            print("Input tidak valid. Masukkan angka, misalnya 12 atau 3.5.")


def main():
    print("=== Kalkulator Sederhana ===")

    while True:
        print("\nPilih operasi:")
        print("1. Penjumlahan (+)")
        print("2. Pengurangan (-)")
        print("3. Perkalian (*)")
        print("4. Pembagian (/)")
        print("0. Keluar")

        pilihan = input("Masukkan pilihan (0-4): ").strip()

        if pilihan == "0":
            print("Terima kasih telah menggunakan kalkulator.")
            break

        if pilihan not in {"1", "2", "3", "4"}:
            print("Pilihan tidak tersedia. Silakan pilih angka 0 sampai 4.")
            continue

        angka_pertama = baca_angka("Masukkan angka pertama: ")
        angka_kedua = baca_angka("Masukkan angka kedua: ")

        if pilihan == "1":
            hasil = angka_pertama + angka_kedua
        elif pilihan == "2":
            hasil = angka_pertama - angka_kedua
        elif pilihan == "3":
            hasil = angka_pertama * angka_kedua
        else:
            if angka_kedua == 0:
                print("Error: angka tidak bisa dibagi dengan nol.")
                continue
            hasil = angka_pertama / angka_kedua

        print(f"Hasil: {hasil:g}")


if __name__ == "__main__":
    main()