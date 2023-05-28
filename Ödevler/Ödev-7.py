#                   7. Hafta Ödevi-1

#ödev: negatif bakiye durumnda para çekme işlemini ebgelleyelim

#ATM programı
bakiye = 5000
s_sifre = "123"
k_sifre = input("Lütfen Kart Şifrenizi Giriniz.\n > ")
ad = "Minik Kedi"

if k_sifre == s_sifre:
  print(f"Hoş Geldin {ad} ")
  print("Bakiye sorgulamak için 1, Para yatırmak için 2, Para çekmek için 3 tuşlarına, çıkmak için q ya basınız...")
  while True:
      islem = input("Lütfen Yapmak İstediğiniz İşlemi Seçiniz.\n > ")
      if islem == "q":
          print("İşlem Sonlandırıldı. Kartınızı Alınız!")
          break
      elif islem == "1":
          print(f"Güncel bakiyeniz:  {bakiye}")
      elif islem == "2":
         miktar = int(input("Yatırmak İstediğiniz Miktarı Giriniz: "))
         if miktar >= 0:
            bakiye += miktar
            print(f"Yatırdığınız Miktar: {miktar}₺. Yeni Bakiyeniz: {bakiye} ")
         else:
             print("Geçersiz Değer Girdiniz. Lütfen Tekrar Deneyin.")
      elif islem == "3":
          miktar = int(input("Çekmek İstediğiniz Miktarı Giriniz: "))
          if miktar >= 0:
              bakiye -= miktar
              print(f"Çektiğiniz Miktar: {miktar}₺. Kalan Bakiyeniz: {bakiye} ")
      else:
        print("Geçersiz Bir İşlem Seçtiniz: ")
else:
  print("Şifreniz Hatalı. Lütfen Tekrar Deneyin.")

#                   7. Hafta Ödevi-2

#ödev-2: while true kullanrak 10 soruluk bir bilgi yarışması kodlayınız..

dogru = "Tebrikler! Soruyu Doğru Yanıtladınız.\n"
yanlis = "Maalesef Soruyu Yanlış Cevapladınız. Doğru Cevap :"
while True:
    print("Bilgi Yarışmasına Hoş Geldiniz.")
    soru1 = input("Tarihin sıfır noktası olarak bilinen, insanlık tarihinin ilk somut kalıntılarının bulunduğu "
                  "Göbeklitepe hangi ilimizdedir?\n A) Şanlıurfa\n B) Gaziantep\n C) Konya\n > ")
    if soru1 == "a":
        print(dogru)
        soru2 = input("Tarihin bir başka dönüm noktası olarak gösterilir.\nSultanahmet Meydanı'nda, Yerebatan Sarnıcı "
                      "üstünde yer alır.\nİstanbul'a gelen turistlerin mutlaka uğrak yerleri arasındadır.\nBu ünlü "
                      "dikili taşın adı nedir?\n A) Beşiktaş\n B) Caesarea Dikilitaşı\n C) Milenyum Taşı\n > ")
        if soru2 == "c":
            print(dogru)
            soru3 = input("Dünyanın en büyük deniz kazalarından biri olarak tarihe geçti.\n1912 yılında 1.550 kişiye "
                          "mezar olan ünlü transatlantiğin adı nedir?\nÖdüllü Filmlere konu olmuştur.\n A) HMS Victory\n"
                          " B) Elizabeth\n C) Titanik\n > ")
            if soru3 == "c":
                print(dogru)
                soru4 = input("Suçluların yakalanmasında kullanılan en önemli delillerden biridir.\nSuçlunun geride "
                              "bıraktığı iz?\n A) Parmak İzi\n B) Saç Teli\n C) Maymuncuk\n > ")
                if soru4 == "A" or "a":
                    print(dogru)
                    soru5 = input("Dünya'nın en başarılı motorsporcusudur.\n2007 World Championship şampiyon pilotudur.\n"
                                  "Bir sezonda en fazla dünya şampiyonluğu olan motosporcumuzun adı nedir?\n "
                                  "A) Samiye Cahid Morkaya\n B) Kenan Sofuoğlu\n C) Renç Koçibey\n > ")
                    if soru5 == "b":
                        print(dogru)
                        print("Bütün Sorulara Doğru Cevap Verdin! Ama Maalesef Bunun İçin Sana Ödül Veremem.")
                        break
                    else:
                        print(y, B)
                        break
                else:
                    print(yanlis, "A")
                    break
            else:
                print(yanlis, "C")
                break
        else:
            print(yanlis, "C")
            break
    else:
        print(yanlis, "A")
        break
