ulang = "Y"
while ulang == "Y" or ulang == "y":
    a = int(input("Masukkan Sisi A: "))
    b = int(input("Masukkan Sisi B: "))
    c = int(input("Masukkan Sisi C: "))
    if  a + b <= c or a + c <= b or b + c <= a:
        print("Bukan segitiga")
    elif a==b==c:
        print("Segitiga sama sisi")
    elif a==b or b==c or c==a:
        print("Segitiga sama kaki")
    else:
        print("Segitiga Sembarang")
    ulang = input("Apakah Anda ingin mengulanginya? ") #Jika iya pencet "y" atau "Y", jika tidak pencet huruf apapun

print("\nProgram Berhenti")
print("Terima kasih telah menggunakan program saya ^^")