import math

# Fungsi untuk mengecek apakah suatu bilangan adalah bilangan prima
def cek_prima(angka):
    if angka <= 1:
        return False
    if angka <= 3:
        return True
    if angka % 2 == 0 or angka % 3 == 0:
        return False
    i = 5
    while i * i <= angka:
        if angka % i == 0 or angka % (i + 2) == 0:
            return False
        i += 6
    return True

# Meminta input dari pengguna
angka = int(input("Masukkan angka: "))

# Percabangan dan perulangan
if cek_prima(angka):
    print(f"{angka} adalah bilangan prima")
else:
    print(f"{angka} bukan bilangan prima")