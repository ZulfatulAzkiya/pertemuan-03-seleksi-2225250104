# Program menentukan jenis segitiga

a = float(input("Sisi pertama: "))
b = float(input("Sisi kedua: "))
c = float(input("Sisi ketiga: "))

# Mengecek apakah sisi dapat membentuk segitiga
if a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a:

    # Menentukan jenis segitiga
    if a == b:
        if b == c:
            print("Segitiga sama sisi.")
        else:
            print("Segitiga sama kaki.")
    else:
        if a == c:
            print("Segitiga sama kaki.")
        else:
            if b == c:
                print("Segitiga sama kaki.")
            else:
                print("Segitiga sembarang.")

else:
    print("Ketiga sisi tidak dapat membentuk segitiga.")