# Membuat Program Konversi Angka Menjadi Huruf

# Persyaratan Program dan Inputan Data
while True:
    try:
        angka = int(input("Masukkan angka (0-100) : "))
        if 0 <= angka <= 100:
            break
        else:
            print("**Angka tidak valid! Mohon hanya masukkan angka dari 0 sampai 100**\n")
    except ValueError:
        print("**MOHON MASUKKAN ANGKA, BUKAN HURUF!**\n")

# Proses Data
if angka >= 85:
    huruf = "A"
elif angka >= 70:
    huruf = "B"
elif angka >= 55:
    huruf = "C"
elif angka >= 40:
    huruf = "D"
else:
    huruf = "E"

# Output Data
print(f"Grade : {huruf}")

angka = int(input("masukkan angka : "))

if angka < 0 or angka > 100:
    print("angka tidak valid! masukkan 0 hingga 100")
else:
    if angka >= 85:
      print("Grade = A")
    elif angka >= 70:
      print("Grade = B")
    elif angka >= 55:
      print("Grade = C")
    elif angka >= 40:
      print("Grade = D")
    else:
      print("Grade = E")