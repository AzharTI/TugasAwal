# Membuat Program Menentukan Bilangan Prima dalam Rentang Tertentu

# Inputan Data
bawah = int(input("Masukkan bawah : "))
atas = int(input("Masukkan atas : "))

# Proses Data
bil_prima = []
for angka in range(bawah, atas + 1):
    if angka > 1:
        prima = True

        for i in range(2, int(angka**0.5) + 1):
            if angka % i == 0:
                prima = False
                break
        if prima :
         bil_prima.append(angka)

# Output Data
print(f"Bilangan prima : {bil_prima}")
print(f"Jumlah bilangan : {len(bil_prima)}")
