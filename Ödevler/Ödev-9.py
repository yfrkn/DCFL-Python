#10 soru olacak
#her soru arsında cevap süresi olarak 5 saniye verilecek
import time

sorular = ["Türkiye'nin Başkenti Neresidir?","Türkiye'nin En Uzun Nehri Nedir?", "Türkiye'nin En Büyük Gölü Nedir?",
           "En Eski Türk Destanı Hangisidir", "Anadolu Hisarı'nı Hangi Osmanlı Padişahı Yaptırmıştır?",
           "Kızılırmak, Hangi İlde Doğup Hangi İlden Denize Dökülür?",
           "Türkiye'nin En Büyük Camiisi Hangisidir?",
           "Tamamlandığında Avrupa'nın En Yüksek Binası Olacak Merkez Bankası Binasının Yüksekliği Kaç Metredir?",
           "Türkiye'nin 3 Ülkeye Sınırı Olan Tek İli Hangisidir?", "Son Osmanlı Halifesi Kimdir?"]
secenekler = ["A)Ankara B)İstanbul C)İzmir D)Bayburt", "A)Kızıl Irmak B)Yeşil Irmak C)Fırat D)Dicle",
              "A)Tuz Gölü, B)Van Gölü, C)Sapanaca Gölü, D)Tekros Gölü",
              "A)Bozkurt Destanı B)Şu Destanı C)Türeyiş Destanı D)Yaratılış Destanı",
              "A)Kanuni Sultan Süleyman B)Fatih Sultan Mehmed C)Yıldırım Beyazıt D)II. Murad",
              "A)Sivas - Kastamonu B)Tokat - Giresun C)Sivas - Samsun D)Tokat - Samsun",
              "A)Edirne - Selimiye Camii B)İstanbul - Çamlıca Camii C)İstanbul - Ayasofya Camii D)Adana - Sabancı Merkez Camii",
              "A)486 B)424 C)317 D)352", "A)Van B)Ağrı C)Iğdır D)Hatay",
              "A)Abdülmecit Efendi B)II. Abdülhamid C)Sultan Vahdettin D)Ahmed Nihad Efendi"]
dogrular = ["a", "a", "b", "d", "c", "c", "b", "d", "c", "a"]

def bilgiyarismasi():
    dogru_sayisi = 0
    puan = 0
    print("Bilgi Yarışması Başlıyor... Doğru Cevaplar +10, Yanlış Cevaplar -5 Puandır. Lütfen Şıkları a, b, c, d Şeklinde Giriniz :)")
    for i in range(0, 10):
        print(sorular[i])
        cevap = input(f"{secenekler[i]}\n > ")
        if cevap.lower() == dogrular[i]:
            print("Tebrikler! Doğru Cevap.\n")
            puan += 10
            dogru_sayisi += 1
        else:
            print("Üzgünüm. Yanlış Cevap.\n")
            puan -= 5

    print("Bilgi Yarışması Sona Erdi! ")
    print(f"10 Sorudan {dogru_sayisi} Tanesine Doğru Cevap Vererek {puan} Puan Kazandın!")

bilgiyarismasi()
