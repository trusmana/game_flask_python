from flask import Flask, render_template,request,session
import random

app = Flask(__name__, static_url_path='/static')
app.secret_key = "cobalagi"

@app.route("/")
def index():
    return render_template('index.html')

###### Aplikasi Tebak Kata
daftar_kata =["gajah", "kucing","semut","jerapah"] 

def pilih_kata():
    return random.choice(daftar_kata)

def acak_kata(word):
    acak = list(word)
    random.shuffle(acak)
    return ''.join(acak)

kata_sekarang = ""
list_kata = ""

@app.route("/tebak_kata",methods =["GET","POST"])
def play_game():
    global kata_sekarang,list_kata
    if request.method == "POST":
        form_kata = request.form['form_kata']
        if form_kata.lower() == kata_sekarang :
            message = " Anak Ayah Pintar !"
            kata_sekarang = pilih_kata()
            list_kata=(acak_kata(kata_sekarang))
        else:
            message = " Kata Salah, Cobalagi yach !"
    else:
        kata_sekarang = pilih_kata()
        list_kata = acak_kata(kata_sekarang)
        message = ""
    return render_template('game.html',word =list_kata,message = message)
###### End Aplikasi Tebak Kata

####Aplikasi Anaonim kata atau lawan kata
kata_antonim = {
    "besar": "pecil",
    "panjang": "pendek",
    "cerah": "gelap",
    "panas":"dingin",
}

def inisialisasi_permainan():
    kata_acak = random.choice(list(kata_antonim.keys()))
    antonim = kata_antonim[kata_acak]
    return kata_acak, antonim

@app.route("/anonim", methods=["GET","POST"])
def game_antonim():
    if request.method == "POST":
        tebakan_pemain = request.form.get("kata_tebakan")
        kata_acak, antonim = session.get("kata_acak", ""), session.get("antonim", "")

        if tebakan_pemain == antonim:
            pesan_hasil = "Benar! Anda menemukan antonimnya."
        else:
            pesan_hasil = "Salah. Cobalah lagi."

        kata_acak, antonim = inisialisasi_permainan()
        session["kata_acak"] = kata_acak
        session["antonim"] = antonim

        return render_template("game_antonim.html", kata_acak=kata_acak, pesan_hasil=pesan_hasil)

    else:
        kata_acak, antonim = inisialisasi_permainan()
        session["kata_acak"] = kata_acak
        session["antonim"] = antonim      
        return render_template("game_antonim.html", kata_acak=kata_acak,pesan_hasil ="")

####End Aplikasi Anaonim kata atau lawan kata

#### Aplikasi Perkalain
@app.route("/perkalian", methods = ["POST","GET"])
def game_perkalian():
    if request.method == "POST":
        pembilang = int(request.form["pembilang"])
        penyebut = int(request.form["penyebut"])
        nilai_jawaban = int(request.form["jawab"])
        hasil_perkalian = pembilang * penyebut

        if nilai_jawaban == hasil_perkalian:
            result = "Benar!"
        else:
            result = "Salah. Coba lagi."
            hasil_perkalian = pembilang * penyebut
            return render_template("perkalian.html", pembilang=pembilang, penyebut=penyebut, hasil=hasil_perkalian,message =result)

        pembilang = random.randint(1, 10)
        penyebut = random.randint(1, 10)
        return render_template("perkalian.html", pembilang=pembilang, penyebut=penyebut, result=result)

    pembilang = random.randint(1, 10)
    penyebut = random.randint(1, 10)
    return render_template("perkalian.html",pembilang=pembilang,penyebut =penyebut)


#### Aplikasi Perkalain
    