def identitas ():
    print("="*35)
    print("Nama     : Muhammad Farrel Ahsan")
    print("Asal     : Tangerang Selatan")
    print("="*35)
    
def penjumlahan(nilai1, nilai2):
    return nilai1 + nilai2
def pengurangan(nilai1, nilai2):
    return nilai1 - nilai2
def perkalian(nilai1, nilai2):
    return nilai1 * nilai2
def pembagian(nilai1, nilai2):
    return nilai1 / nilai2
def modulus(nilai1, nilai2):
    return nilai1 % nilai2

identitas()


while True:
    pilihan = input("Masukkan Menu (+|-|/|*|%|stop): ")

    if pilihan == "stop":
        print("Program Berhenti. Terima kasih telah menggunakan program saya.")
        break

    if pilihan not in ["+", "-", "*", "/", "%"]:
        print("Menu tidak valid!")
        continue

    nilai1 = float(input("Masukkan Nilai 1: "))
    nilai2 = float(input("Masukkan Nilai 2: "))
    
    if nilai1.is_integer():
        nilai1 = int(nilai1)

    if nilai2.is_integer():
        nilai2 = int(nilai2)

    if pilihan == "+":
        hasil = penjumlahan(nilai1, nilai2)
        print(f"Hasil penjumlahan {nilai1} + {nilai2} adalah {hasil}")

    elif pilihan == "-":
        hasil = pengurangan(nilai1, nilai2)
        print(f"Hasil pengurangan {nilai1} - {nilai2} adalah {hasil}")

    elif pilihan == "*":
        hasil = perkalian(nilai1, nilai2)
        print(f"Hasil perkalian {nilai1} * {nilai2} adalah {hasil}")

    elif pilihan == "/":
        if nilai2 == 0:
            print("Tidak bisa dibagi dengan 0!")
        else:
            hasil = pembagian(nilai1, nilai2)
            print(f"Hasil pembagian {nilai1} / {nilai2} adalah {hasil}")

    elif pilihan == "%":
        if nilai2 == 0:
            print("Tidak bisa modulus dengan 0!")
        else:
            hasil = modulus(nilai1, nilai2)
            print(f"Hasil modulus {nilai1} % {nilai2} adalah {hasil}")
            
    if hasil.is_integer():
        hasil = int(hasil)