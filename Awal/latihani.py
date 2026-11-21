# Menentukan bilangan ganjilnap nesitif
while True:
    try:
        angka = int(input("Masukkan Bilangan : "))
        break
    except ValueError:
        print("HARAP MASUKKAN ANGKA BUKAN KARAKTER!!\n")

if angka == 0:
    print("Bilangan adalah nol")
else:
    if angka > 0:
        sifat = "positif"
    else:
        sifat = "negatif"
    if angka % 2 != 0:
        jenis = "ganjil"
    else:
        jenis = "genap"

    print(f"Bilangan adalah {sifat} dan {jenis}")

while True:
    try:
        angka = int(input("Masukkan angka : "))
        break
    except ValueError:
        print("HARAP MASUKKAN ANGKA BUKAN KARAKTER!!\n")

if angka == 0:
    print("Angka adalah nol\n")
elif angka > 0 and angka % 2 != 0:
    print("Angka adalah positif dan ganjil\n")
elif angka < 0 and angka % 2 != 0:
    print("Angka adalah negatif dan ganjil\n")
elif angka > 0 and angka % 2 == 0:
    print("Angka adalah positif dan genap\n")
else:
    print("Angka adalah negatif dan genap\n")



# Program konversi angka
while True:
    try:
        n = int(input("Masukkan Angka : "))
        if 0 <= n <= 100:
            break
        else:
            print("**Angka tidak valid! Harap masukkan angka 0 hingga 100!**")
    except ValueError:
        print("HARAP MASUKKAN ANGKA BUKAN KARAKTER!!\n")

if n >= 80:
    print("Grade A")
elif n >= 70:
    print("Grade B")
elif n >= 50:
    print("Grade C")
elif n >= 30:
    print("Grade D")
elif n >= 10:
 print("Grade E")
else:
    print("Grade F")

while True:
   try:
      n = int(input("Masukkan angka : "))
      break
   
   except ValueError:
      print("HARAP MASUKKAN ANGKA BUKAN KARAKTER!!")

if n < 0 or n > 100:
    print("*angka  tidak valid!\n*")
else:
    if n > 80:
     print("Grade A\n")
    elif n > 70:
     print("Grade B\n")
    elif n > 50:
     print("Grade C\n")
    elif n > 30:
     print("Grade D\n")
    elif n > 10:
     print("Grade E\n")
    else:
     print("Grade F\n")



# Program deret bilangan dan dijumlah total dan genap saja
while True:
   try:
      b = int(input("Masukkan angka : "))
      if b <= 0:
         print("**Angka tidak valid!**")
      else:
         break
   except ValueError:
      print("MOHON MASUKKAN ANGKA BUKAN KARAKTER!!\n")

a = []
t = 0
g = 0

for i in range(1, b + 1):
   a.append(i)
   t += i
   if i % 2 == 0:
      g += i

print(f"Deret : {a}")
print(f"Jumlah total : {t}")
print(f"Jumlah genap : {g}\n")



# Program membentuk segitiga dari bintang
while True:
   try:
      tk = int(input("Masukkan n : "))
      if tk <= 0:
         print("Angka tidak valid. Silahkan coba lagi!")
      else:
       break
   except ValueError:
      print("**Masukkan Angka!**\n")

for i in range(1, tk + 1):
   print("*" * i)
print()
for i in range(tk, 0, -1):
   print("*" * i)
print()



# Program menentukan bilangan prima dari rentang bilangan yang diinput
while True:
   try:
      a1 = int(input("Mulai dari : "))
      a2 = int(input("Berakhir di : "))
      if a1 and a2 <= 0:
         print("Angka tidak valid!")
      elif a2 < a1:
         print("Angka akhir harus lebih dari angka awal.")
      else:
         break
   except ValueError:
      print("**MOHON MASUKKAN ANGKA!!**")
      
b_prima = []
for angka in range(a1, a2 + 1):
   if angka > 1:
      prima = True
      for penentu in range(2, int(angka**0.5) + 1):
         if angka % penentu == 0:
            prima = False
            break
      if prima:
         b_prima.append(angka)

print(f"Bilangan prima : {b_prima}")
print(f"Jumlah rentang bilangan : {len(b_prima)}")