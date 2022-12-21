print("""
Hesap Makinesi

Toplama İşlemi - 1
Çıkarma İşlemi - 2
Çarpma İşlemi  - 3
Bölme İşlemi   - 4
""")
islem = input("İşlem Numarası : ")
s1 = int(input("1. Sayı = "))
s2 = int(input("2. Sayı = "))
if islem == "1":
    print(s1, "+", s2, "=", s1+s2)
elif islem == "2":
    print(s1, "-", s2, "=", s1-s2)
elif islem == "3":
    print(s1, "*", s2, "=", s1*s2)
elif islem == "4":
    print(s1, "/", s2, "=", s1/s2)
else:
    print("Hatalı işlem girdiniz.")
