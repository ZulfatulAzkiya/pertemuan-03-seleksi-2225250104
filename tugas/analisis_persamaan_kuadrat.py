# Program menganalisis persamaan kuadrat
# Bentuk persamaan: ax^2 + bx + c = 0

import math

a = float(input("Masukkan nilai a: "))
b = float(input("Masukkan nilai b: "))
c = float(input("Masukkan nilai c: "))

if a == 0:
    print("Bukan persamaan kuadrat karena nilai a tidak boleh 0.")
else:
    # Menghitung diskriminan
    D = b**2 - 4*a*c

    print(f"Diskriminan = {D}")

    if D > 0:
        x1 = (-b + math.sqrt(D)) / (2*a)
        x2 = (-b - math.sqrt(D)) / (2*a)

        print("Persamaan memiliki dua akar real berbeda.")
        print(f"x1 = {x1}")
        print(f"x2 = {x2}")

    else:
        if D == 0:
            x = -b / (2*a)

            print("Persamaan memiliki satu akar real kembar.")
            print(f"x = {x}")

        else:
            print("Persamaan tidak memiliki akar real.")