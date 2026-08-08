def identitas ():
    print("="*35)
    print("Nama     : Muhammad Farrel Ahsan")
    print("Asal     : Tangerang Selatan")
    print("="*35)
def hitung (nilai1,nilai2,operator):
    if operator == "+":
        return nilai1 + nilai2
    elif operator == "-":
        return nilai1 - nilai2
    elif operator == "*":
        return nilai1 * nilai2
    elif operator == "/":
        return nilai1 / nilai2
    elif operator == "&":
        return nilai1 & nilai2

identitas()


while True:
    pilihan = input("Masukkan Menu (+|-|/|*|%|stop): ")

    if pilihan == "stop":
        print("Program Berhenti")
        break

    if pilihan not in ["+", "-", "*", "/", "%"]:
        print("Menu tidak valid!")
        continue

    nilai1 = float(input("Masukkan Nilai 1: "))
    nilai2 = float(input("Masukkan Nilai 2: "))
    
    hasil = hitung(nilai1, nilai2, pilihan)

    if nilai1.is_integer():
        nilai1 = int(nilai1)

    if nilai2.is_integer():
        nilai2 = int(nilai2)

    if hasil.is_integer():
        hasil = int(hasil)

    nama_operasi = {
        "+": "penjumlahan",
        "-": "pengurangan",
        "*": "perkalian",
        "/": "pembagian",
        "%": "modulus"
    }

    print(f"Hasil {nama_operasi[pilihan]} {nilai1} {pilihan} {nilai2} adalah {hasil}")
    print()