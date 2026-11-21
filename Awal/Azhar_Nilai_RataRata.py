# Program Menghitung Rata Rata Nilai
print("SPMB SMKN JABAR")
print()

# Inputan Data
a = float(input("Masukkan Nilai Bahasa Indonesia = "))
b = float(input("Masukkan Nilai Matematika = "))
c = float(input("Masukkan Nilai Bahasa Inggris = "))
print()

# Proses Data
nilai = (a + b + c) / 3

# Output Data
print("Anda Dinyatakan :")
if nilai >= 90:
    print("LULUS SPMB DENGAN SEMPURNA")
elif nilai >= 80:
    print("LULUS SPMB")
else:
    print("TIDAK LULUS SPMB")

print(f"Nilai Anda = {nilai} ")