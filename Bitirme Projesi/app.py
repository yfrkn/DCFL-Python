from flask import Flask, render_template, request
import random

harf = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u", "v", "y", "z", "q", "w", "x",
        "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "R", "S", "T", "U", "V", "Y", "Z", "Q", "W", "X"]
tr_harf = ["ç", "Ç", "ğ", "Ğ", "İ", "ö", "Ö", "ş", "Ş", "ü", "Ü"]
sayi = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
karakter = ["!", ".", "-", "/", "*", "#", '"', "+", "=", ":"]
pw = ""
sayac = 0
rsayi = 0

app = Flask(__name__)

@app.route('/', methods = ['GET','POST'])
def index():
    if request.method == 'POST':
        if request.form.get('mainpage'):
            return render_template('index.html')
        elif request.form.get('createpass'):
            return render_template('createpass.html')
        elif request.form.get('checkpass'):
            return render_template('checkpass.html')
        elif request.form.get("not"):
            return render_template('notortalama.html')
        elif request.form.get("hesap"):
            return render_template('hesapmakinesi.html')
        elif request.form.get("tahmin"):
            return render_template('sayitahmini.html')
    return render_template('index.html')


@app.route('/createpass', methods = ['GET','POST'])
def createpass():
    if request.method == 'POST':
        if request.form.get('8'):
            pw = ""
            for i in range(1, 9):
                sec = random.randint(1,3)
                if sec == 1:
                    pw += random.choice(harf)
                elif sec == 2:
                    pw += random.choice(sayi)
                elif sec == 3:
                    pw += random.choice(karakter)
            return render_template('createpass.html', pw = pw)
        elif request.form.get('8-12'):
            pw = ""
            for i in range(1, random.randint(9,13)):
                sec = random.randint(1,3)
                if sec == 1:
                    pw += random.choice(harf)
                elif sec == 2:
                    pw += random.choice(sayi)
                elif sec == 3:
                    pw += random.choice(karakter)
            return render_template('createpass.html', pw = pw)
        elif request.form.get('12'):
            pw = ""
            for i in range(1, 13):
                sec = random.randint(1,3)
                if sec == 1:
                    pw += random.choice(harf)
                elif sec == 2:
                    pw += random.choice(sayi)
                elif sec == 3:
                    pw += random.choice(karakter)
            return render_template('createpass.html', pw = pw)
        elif request.form.get("12-16"):
            pw = ""
            for i in range(1, random.randint(13,17)):
                sec = random.randint(1,3)
                if sec == 1:
                    pw += random.choice(harf)
                elif sec == 2:
                    pw += random.choice(sayi)
                elif sec == 3:
                    pw += random.choice(karakter)
            return render_template('createpass.html', pw = pw)
        elif request.form.get("16"):
            pw = ""
            for i in range(1, 17):
                sec = random.randint(1,3)
                if sec == 1:
                    pw += random.choice(harf)
                elif sec == 2:
                    pw += random.choice(sayi)
                elif sec == 3:
                    pw += random.choice(karakter)
            return render_template('createpass.html', pw = pw)
    return render_template('createpass.html')


@app.route('/checkpass', methods = ['GET','POST'])
def checkpass():
    if request.method == 'POST':
        if request.form.get('check'):
            h = 0
            s = 0
            k = 0
            k_sifre = request.form.get('password')

            for i in k_sifre:
                if i in harf or i in tr_harf:
                    h += 1
                elif str(i) in sayi:
                    s += 1
                elif i in karakter:
                    k += 1

            if h+s+k < 8:
                guc = "Hemen Değiştirmelisin"
                neden = "Şifren 8 Karakterden Kısa"
            elif h == 0:
                guc = "Hemen Değiştirmelisin"
                neden = "Şifrende Hiç Harf Yok" 
            elif 0 < h < 2:
                guc = "İdare Eder"
                neden = "Şifrende Çok Az Harf Var" 
            elif s == 0:
                guc = "Hemen Değiştirmelisin"
                neden = "Şifrende Hiç Sayı Yok" 
            elif 0 < s < 2:
                guc = "İdare Eder"
                neden = "Şifrende Çok Az Sayı Var" 
            elif k == 0:
                guc = "Hemen Değiştirmelisin"
                neden = "Şifrende Hiç Özel Karakter Yok" 
            elif 0 < k < 2:
                guc = "İdare Eder"
                neden = "Şifrende Çok Az Özel Karakter Var"
            else:
                guc = "Şifren Çok Güvenli!"
                neden = "Şifren Oldukça Uzun. Sayılar ve Özel Karakterler İçeriyor"

            return render_template('checkpass.html', guc = guc, neden = neden)

    return render_template('checkpass.html')


@app.route('/notortalama', methods = ['GET','POST'])
def notortalama():
    if request.method == 'POST':
        if request.form.get('hesapla'):
            snot1 = request.form.get("not1")
            snot2 = request.form.get("not2")
            pnot1 = request.form.get("not3")
            pnot2 = request.form.get("not4")
            if snot1 == "" or snot2 == "":
                ort = "Lütfen Sınav Notlarını Girin"
            elif pnot1 != "" and pnot2 != "":
                if 0 <= int(snot1) <= 100 and 0 <= int(snot2) <= 100 and 0 <= int(pnot1) <= 100 and 0 <= int(pnot2) <= 100:
                    ort = (int(snot1)+int(snot2)+int(pnot1)+int(pnot2))/4
                else:
                    ort = "Sınav ya da Performans Notlarınız 100'den Büyük veya 0'dan Küçük Olamaz."

            elif pnot1 == "" and pnot2 == "":
                if 0 <= int(snot1) <= 100 and 0 <= int(snot2) <= 100:
                    ort = (int(snot1)+int(snot2))/2
                else:
                    ort = "Sınav Notlarınız 100'den Büyük veya 0'dan Küçük Olamaz."

            elif pnot1 != "" and pnot2 == "":
                if 0 <= int(snot1) <= 100 and 0 <= int(snot2) <= 100 and 0 <= int(pnot1) <= 100:
                    ort = (int(snot1)+int(snot2)+int(pnot1))/3
                else:
                    ort = "Performans Notlarınız 100'den Büyük veya 0'dan Küçük Olamaz."

            elif pnot1 == "" and pnot2 != "":
                if 0 <= int(snot1) <= 100 and 0 <= int(snot2) <= 100 and 0 <= int(pnot2) <= 100:
                    ort = (int(snot1)+int(snot2)+int(pnot2))/3
                else:
                    ort = "Performans Notlarınız 100'den Büyük veya 0'dan Küçük Olamaz."

            return render_template('notortalama.html', ort = ort)
    return render_template('notortalama.html')


@app.route('/sayitahmini', methods = ['GET','POST'])
def sayitahmini():
    if request.method == 'POST':
        global rsayi, sayac
        if request.form.get('10'):
            durum = "1 - 10 Arasında Bir Sayı Tuttum"
            ornek = "Tahmininiz | Örnek : 6"
            rsayi = random.randint(1, 10)
            return render_template('sayitahmini.html', durum = durum, ornek = ornek)
        elif request.form.get('100'):
            durum = "1 - 100 Arasında Bir Sayı Tuttum"
            ornek = "Tahmininiz | Örnek : 43"
            rsayi = random.randint(1, 100)
            return render_template('sayitahmini.html', durum = durum, ornek = ornek)
        elif request.form.get('1000'):
            durum = "1 - 1000 Arasında Bir Sayı Tuttum"
            ornek = "Tahmininiz | Örnek : 579"
            rsayi = random.randint(1, 1000)
            return render_template('sayitahmini.html', durum = durum, ornek = ornek)
        elif request.form.get("tahmin"):
            tahmin = request.form.get("ktahmin")
            if tahmin == "":
                dy = "?"
                yakinlik = "Lütfen Tahmininizi Girin"
                durum = "Tahmininiz"
                ornek = "Örnek : 6 / 43 / 579"
                return render_template('sayitahmini.html', dy = dy, yakinlik = yakinlik, durum = durum, ornek = ornek)
            if rsayi == 0:
                dy = "?"
                yakinlik = "Henüz Bir Sayı Tutmadım"
                durum = "Sayı Tutmam İçin Yukarıdaki Butonlardan Birine Basın"
                ornek = "Örnek : 1-100 Arasında Bir Sayı Tut"
                return render_template('sayitahmini.html', dy = dy, yakinlik = yakinlik, durum = durum, ornek = ornek)
            else:
                sayac += 1
                if rsayi == int(tahmin):
                    dy = "Doğru!"
                    yakinlik = f"{sayac}. Denemede Doğru Bildiniz"
                    sayac = 0
                elif rsayi > int(tahmin):
                    dy = "Yanlış"
                    yakinlik = "Tuttuğum Sayı Daha Büyük"
                elif rsayi < int(tahmin):
                    dy = "Yanlış"
                    yakinlik = "Tuttuğum Sayı Daha Küçük"

                durum = "Tahmininiz"
                ornek = "Örnek : 6 / 43 / 579"
                return render_template('sayitahmini.html', dy = dy, yakinlik = yakinlik, durum = durum, ornek = ornek)
    return render_template('sayitahmini.html')


@app.route('/hesapmakinesi', methods = ['GET','POST'])
def hesapmakinesi():
    if request.method == 'POST':
        s1 = request.form.get("bir")
        s2 = request.form.get("iki")
        if request.form.get('topla'):
            if s1 == "" or s2 == "":
                sonuc = "Lütfen Sayıları Girin"
            else:
                sonuc = int(s1) + int(s2)
        if request.form.get('cikar'):
            if s1 == "" or s2 == "":
                sonuc = "Lütfen Sayıları Girin"
            else:
                sonuc = int(s1) - int(s2)
        if request.form.get('carp'):
            if s1 == "" or s2 == "":
                sonuc = "Lütfen Sayıları Girin"
            else:
                sonuc = int(s1) * int(s2)
        if request.form.get('bol'):
            if s1 == "" or s2 == "":
                sonuc = "Lütfen Sayıları Girin"
            else:
                sonuc = int(s1) / int(s2)
        if request.form.get('tambol'):
            if s1 == "" or s2 == "":
                sonuc = "Lütfen Sayıları Girin"
            else:
                sonuc = int(s1) // int(s2)
        if request.form.get('mod'):
            if s1 == "" or s2 == "":
                sonuc = "Lütfen Sayıları Girin"
            else:
                sonuc = int(s1) % int(s2)
        if request.form.get('us'):
            if s1 == "" or s2 == "":
                sonuc = "Lütfen Sayıları Girin"
            else:
                sonuc = int(s1) ** int(s2)
        return render_template('hesapmakinesi.html', sonuc = sonuc)
    return render_template('hesapmakinesi.html')

if __name__ == '__main__':
    app.run(debug=True)
