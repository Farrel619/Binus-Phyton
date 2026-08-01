import math

a = int(input("Masukkan Nilai A: "))
b = int(input("Masukkan Nilai B: "))
c = int(input("Masukkan NIlai C: "))
if a==0:
    print("ini bukan persamaan kuadrat")
else:
    d = b**2 - 4*a*c
    print(math.sqrt(d))
print(f"persamaan : {a}x^2 + {b}x + {c}")
print("diskriminan =", d)
if d < 0:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    print("Ini memiliki akar yang berbeda")
    print("x1 =", x1)
    print("x2 =", x2)
elif d == 0:
    x = -b / (2 * a)
    print("Ini memiliki akar ganda")
    print("x =", x)
else:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)