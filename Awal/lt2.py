# Membuat program menghitung segitiga diinput
print("Menghitung Luas Segitiga Dari Nilai Yang Diinput :")

# Inputan Data
alas = float(input("Masukkan alas (cm) = "))
tinggi = float(input("Masukkan tinggi (cm) = "))

# Proses Data
luas = 0.5 * alas * tinggi

# Output
print(f"Luas = {luas} cm^2")

# Program menghitung luas balok
print("Menghitung Luas Balok Dari Nilai Yang Diinput :")
# Input Data
panjang = int(input("Masukkan Panjang (cm) = "))
lebar = int(input("Masukkan Lebar (cm) = "))
tinggi = int(input("Masukkan Tinggi (cm) = "))

# Proses menghitung
luas = 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)

# Proses Output
print(f"Luas Balok = {luas} cm^2")