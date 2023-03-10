#                   5. Hafta Ödevi-1

#ödev: bir öğrencinin not aralığını harflerle ifade eden mini programı kodlayınız...

print("Aldığınız Nota Göre Notunuzu Harflerle İfade Eden Program")
sinavnotu = int(input("Sınavdan Aldığınız Notu Girin : "))
if 90 <= sinavnotu <= 100:
    print("Sınavdan AA Aldınız. Tebrikler!")
elif 85 <= sinavnotu <= 89:
    print("Sınavdan BA Aldınız.")
elif 80 <= sinavnotu <= 84:
    print("Sınavdan BB Aldınız.")
elif 75 <= sinavnotu <= 79:
    print("Sınavdan CB Aldınız.")
elif 70 <= sinavnotu <= 74:
    print("Sınavdan CC Aldınız.")
elif 65 <= sinavnotu <= 69:
    print("Sınavdan DC Aldınız.")
elif 60 <= sinavnotu <= 64:
    print("Sınavdan DD Aldınız.")
elif 50 <= sinavnotu <= 59:
    print("Sınavdan FD Aldınız.")
elif 0 <= sinavnotu <= 49:
    print("Sınavdan FF Aldınız.")
else:
    print("Hatalı Not Girdiniz.")
   
#                   5. Hafta Ödevi-2

#250 sayfalık bir kitap için 5 rakamı kaç kere kullanılmıştır...
