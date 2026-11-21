# Membuat Program Membentuk Segitiga Siku Siku dari Bintang

# Inputan Data
n = int(input("Masukkan n : "))
print("\n--Segitiga Siku Siku--")

# Proses Data dan 
for i in range(1, n + 1):
    print("*" * i)

print("\n--Segitiga Siku Siku Terbalik--")
for i in range(n, 0, -1):
    print("*" * i)