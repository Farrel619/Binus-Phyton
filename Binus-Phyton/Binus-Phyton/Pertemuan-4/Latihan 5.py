def konversi_nilai(huruf):
    data_nilai = {
        "A": 4.00,
        "A-": 3.75,
        "B+": 3.50,
        "B": 3.00,
        "B-": 2.75,
        "C+": 2.50,
        "C": 2.00,
        "C-": 1.75,
        "D": 1.50,
        "E": 1.20
    }

    return data_nilai.get(huruf.upper(), None)

total = 0
jumlah = 0

while True:
    nilai = input("Masukkan Kategori Nilai (Tekan Enter untuk Berhenti): ")

    if nilai == "":
        break

    angka = konversi_nilai(nilai)

    if angka is not None:
        total += angka
        jumlah += 1
    else:
        print("Kategori nilai tidak valid!")

if jumlah > 0:
    rata = total / jumlah

    if rata >= 4.00:
        kategori = "A"
    elif rata >= 3.75:
        kategori = "A-"
    elif rata >= 3.50:
        kategori = "B+"
    elif rata >= 3.00:
        kategori = "B"
    elif rata >= 2.75:
        kategori = "B-"
    elif rata >= 2.50:
        kategori = "C+"
    elif rata >= 2.00:
        kategori = "C"
    elif rata >= 1.75:
        kategori = "C-"
    elif rata >= 1.50:
        kategori = "D"
    else:
        kategori = "E"

    print("\nNilai rata-rata adalah {:.2f} dengan kategori {}".format(rata, kategori))
else:
    print("Tidak ada nilai yang dimasukkan.")