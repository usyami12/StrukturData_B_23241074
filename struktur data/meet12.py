# Fungsi untuk mengecek apakah suatu bilangan adalah bilangan prima
def cek_prima(angka):
    if angka <= 1:
        return False
    for i in range(2, angka):
        if angka % i == 0:
            return False
    return True

# Meminta input dari pengguna
angka = int(input("Masukkan angka: "))

# Percabangan dan perulangan
if cek_prima(angka):
    print(f"{angka} adalah bilangan prima")
else:
    print(f"{angka} bukan bilangan prima")