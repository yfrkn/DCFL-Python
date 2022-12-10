# Ödev: okulumuzdaki öğretmenlerin, isimleri, branşları, girdikleri sınıfları; her bir öğretmenin bu verilerini bir listeye ekleyelim.
# Sonrasında bütün öğretmenleri de daha büyük bir listeye ekleyelim.
# bu listenin kaç elemanlı olduğunu ekrana yazdıralım
# öğretmen isimlerine göre alfabetik olarak ekrana yazdıralım
# öğretmenin isimleri yazarak onunla ilgili verilerin olduğu listeyi ekrana yazdıralım

ogretmenler = []
isimler = []
while True:
    isim = input("Öğretmenin İsmi : ")
    brans = input("Öğretmenin Branşı : ")
    sinif = input("Öğretmenin Girdiği Sınıflar : ")
    ogretmen = [isim, brans, sinif]
    ogretmenler.append(ogretmen)
    ogretmenler.sort()
    isimler.append(isim)
    isimler.sort()
    print("Öğretmen Sayısı : ", len(ogretmenler))
    print("Öğretmenlerin İsimleri : ", isimler)
    print("Öğretmenlerin Verileri : ", ogretmenler)
