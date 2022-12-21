print("""
Hesap Makinesi

Toplama İşlemi - 1
Çıkarma İşlemi - 2
Çarpma İşlemi  - 3
Bölme İşlemi   - 4
""")
islem = input("İşlem Numarası : ")

if islem == "1":
    s1 = int(input("1. Sayı = "))
    s2 = int(input("2. Sayı = "))
    print(s1, "+", s2, "=", s1+s2)
elif islem == "2":
    s1 = int(input("1. Sayı = "))
    s2 = int(input("2. Sayı = "))
    print(s1, "-", s2, "=", s1-s2)
elif islem == "3":
    s1 = int(input("1. Sayı = "))
    s2 = int(input("2. Sayı = "))
    print(s1, "*", s2, "=", s1*s2)
elif islem == "4":
    s1 = int(input("1. Sayı = "))
    s2 = int(input("2. Sayı = "))
    print(s1, "/", s2, "=", s1/s2)
else:
    print("Hatalı işlem girdiniz.")
