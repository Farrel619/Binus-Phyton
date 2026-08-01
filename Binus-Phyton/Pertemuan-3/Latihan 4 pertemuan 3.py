a = int(input("Masukkan Sisi A: "))
b = int(input("Masukkan Sisi B: "))
c = int(input("Masukkan Sisi C: "))
if  a + b <= c or a + c <= b or b + c <= a:
    print("Bukan segitiga")
elif a==b==c:
    print("Segitiga sama sisi")
elif a==b or b==c or c==a:
    print("Segitiga sama kaki")
else
    print("Segitiga Sembarang")