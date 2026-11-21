# Membuat Program Penentu Bilangan Bulat Ganjil/Genap dan Positif/Negatif
print("Menentukan Bilangan Inputan User")

# Inputan Data
angka = int(input("Masukkan Bilangan : "))

# Proses Data
if angka == 0:
    print("Bilangan nol")
else:
    if angka % 2 != 0:
     jenis = "ganjil"
    else:
     jenis = "genap"
    if angka > 0:
     sifat = "positif"
    else:
     sifat = "negatif"

# Output data
    print(f"Bilangan {sifat} dan {jenis}")
print()

# Versi 2
angka = int(input("Masukkan bilangan : "))

if angka == 0:
  print("Bilangan adalah nol")
elif angka % 2 != 0 and angka > 0:
  print("Bilangan adalah positif dan ganjil")
elif angka % 2 != 0 and angka < 0:
  print("Bilangan adalah negatif dan ganjil")
elif angka % 2 == 0 and angka > 0:
  print("Bilangan adalah positif dan genap")
else:
  print("Bilangan adalah negatif dan genap")
