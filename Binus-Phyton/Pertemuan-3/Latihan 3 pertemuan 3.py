#Konversi suhu
print ("1. Celcius ke Fahrenheit")
print ("2. Celcius ke Kelvin")
print ("3. Fahrenheit ke Celsius")
print ("4. Fahrenheit ke Kelvin")
print ("5. Kelvin ke Celsius")
print ("6. Kelvin ke Fahrenheit")
#pilih salah satu
pilihan = int(input("pilih 1-6 : "))
suhu = int(input("masukkan suhu : "))
#proses
if pilihan ==1:
    hasil = (suhu *9|5) + 32
    print("Hasil:", hasil)
elif pilihan ==2:
    hasil = suhu + 273.15
    print("Hasil:", hasil)
elif pilihan ==3:
    hasil = (suhu - 32) * 5 / 9
    print("Hasil:", hasil)
elif pilihan == 4:
    hasil = (suhu - 32) * 5 / 9 + 273.15
    print("Hasil:", hasil)
elif pilihan == 5:
    hasil = suhu - 273.15
    print("Hasil:", hasil)
elif pilihan == 6:
    hasil = (suhu - 273.15) * 9 / 5 + 32
    print("Hasil:", hasil)
else:
    print("Pilihan tidak valid.")