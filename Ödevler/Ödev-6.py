#                   6. Hafta Ödevi-1

#1 den 1500 e kadar kaç kere 55 yan yana yazılır..
sayi1 = ""
for i in range(1, 1500):
    sayi1 += str(i)
print(sayi1.count("55"))

#                   6. Hafta Ödevi-2

#while tru ile istenildiği kadar sayı toplayan ya da sayı çarpan bir program yapınız...
toplam = 0
carpim = 1
islem = input("Toplama İşlemi İçin 1'e, Çarpma İşlemi İçin 2'ye Basın.\n > ")
if islem == "1":
    while True:
        sayi2 = int(input("Toplamak İçin Bir Sayı Girin. Çıkmak için Q Tuşuna Basın.\n > "))
        print(f"{toplam} + {sayi2} = {toplam+sayi2}")
        toplam += sayi2
        if sayi2 == "Q":
            print("Programdan Çıkılıyor...")
            break
elif islem == "2":
    while True:
        sayi3 = int(input("Çarpmak İçin Bir Sayı Girin. Çıkmak için Q Tuşuna Basın.\n > "))
        print(f"{carpim} * {sayi3} = {carpim * sayi3}")
        carpim *= sayi3
        if sayi3 == "Q":
            print("Programdan Çıkılıyor...")
            break
else:
    print("Yanlış Değer Girdiniz.")

#                   6. Hafta Ödevi-3

#250 faktöriyelin içinde 222 sayısı kaç kez tekrar ediyor...
faktoriyel = 1
for i in range(1, 251):
    faktoriyel *= i
faktoriyel = str(faktoriyel)
print(faktoriyel.count("222"))
