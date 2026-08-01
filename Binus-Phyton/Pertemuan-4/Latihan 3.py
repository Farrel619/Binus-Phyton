ulang = "Y"

while ulang == "Y" or ulang =="y":
    Nilai = int(input("Masukkan Nilai :"))
    if Nilai % 2 == 0:
        print("Angka", Nilai, "adalah angka genap")
    else :
        print ("Angka", Nilai, "adalah angka ganjil") 
 
    ulang = input("Apakah Anda ingin mengulanginya? ") #Jika iya pencet "y" atau "Y", jika tidak pencet huruf apapun

print("\nProgram Berhenti")
print("Terima kasih telah menggunakan program saya ^^")