import sqlite3
import subprocess
import sys
from threading import Thread
import cv2
import pyttsx3
from PyQt5 import QtWidgets
from pydub import AudioSegment
from pydub.playback import play
from speech_recognition import Recognizer, Microphone
import os

class Pencere(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.veritabanı_bağlantısı()
        self.init_ui()

    def veritabanı_bağlantısı(self):
        self.db_path = os.path.join(os.getcwd(),"database.db")
        self.bağlantı=sqlite3.connect(self.db_path) # yoksa databese oluşturur varsa bağlanır
        self.imleç=self.bağlantı.cursor()
        self.imleç.execute("create table if not exists üyeler (kullanıcı_adı TEXT, parola TEXT,foto BLOB)")
        self.update_backup()
        self.bağlantı.commit()

    def register(self):
        self.imleç=self.bağlantı.cursor()
        adı=self.kullanıcı_adı.text()
        adı=adı.strip()
        şifre=self.parola.text()
        self.take_picture()
        with open("x.jpg",'rb') as file:
            fotoğraf=file.read()
        self.imleç.execute("INSERT INTO üyeler (kullanıcı_adı,parola,foto) VALUES (?,?,?)",(adı,şifre,fotoğraf))
        self.bağlantı.commit()
        self.update_backup()
    def login(self):
        adı=self.kullanıcı_adı.text()
        par=self.parola.text()

        self.imleç.execute(f"select * from üyeler where kullanıcı_adı= '{adı}' and parola = '{par}'")
        data=(self.imleç.fetchall())
        print((data))

        if len(data):
            self.yazı_alanı.setText("hoşgeldin "+ adı)
            ilk_ad=adı.split()
            ses_motoru=pyttsx3.init()
            ses_motoru.setProperty('voice','turkish+f4')
            ses_motoru.setProperty('rate',120)
            ses_motoru.say(" hoşgeldin " + ilk_ad[0])
            ses_motoru.runAndWait()
        else:
            self.yazı_alanı.setText("kullanıcı adı veya şifre hatalı")
    def delete(self,x):
        print(x)
        adı=self.kullanıcı_adı.text().strip()
        sql_sesli=f"delete from üyeler where kullanıcı_adı like '%{x}%'"
        sql=f"delete from üyeler where kullanıcı_adı like '%{adı}%'"
        if x:
            self.imleç.execute(f"select kullanıcı_adı,parola from üyeler where kullanıcı_adı like '%{x}%'")
            data = (self.imleç.fetchall())
            print(data)
            if len(data):
                self.imleç.execute(sql_sesli)
                self.yazı_alanı.setText("Kayıt silinmiştir")
                engine = pyttsx3.init()
                engine.setProperty('voice', 'english+f4')
                engine.setProperty('rate', 170)
                engine.say(" Farewell to all the  "+self.ad +"s")
                engine.runAndWait()
            else:
                self.yazı_alanı.setText("Böyle bir kayıt bulunamadı")
                engine = pyttsx3.init()
                engine.setProperty('voice', 'english+f4')
                engine.setProperty('rate', 170)
                engine.say(" unfortunately there is no  "+self.ad +" in this database")
                engine.runAndWait()

        else:
            self.imleç.execute(f"select kullanıcı_adı,parola from üyeler where kullanıcı_adı like '%{adı}%'")
            data = (self.imleç.fetchall())
            if len(data):
                self.imleç.execute(sql)
                self.yazı_alanı.setText("Kayıt silinmiştir")
            else:
                self.yazı_alanı.setText("Böyle bir kayıt bulunamadı")
        self.bağlantı.commit()
        self.update_backup()
    def Show(self):

        #os.system('cmd /c "C:/Users/bugra/PycharmProjects/PyQt5_Uygulamaları/kullanıcıarayüzü.sqbpro"')
        #subprocess.call([r"C:/Users/bugra/PycharmProjects/PyQt5_Uygulamaları/kullanıcıarayüzü.sqbpro"],shell=True,)
        subprocess.call([r"backup.db"], shell=True, )

    def audio_Assist(self):
        self.tanıyıcı = Recognizer()
        with Microphone() as self.kaynak:
            kelimeler = self.record(self.tanıyıcı,self.kaynak)
            print(kelimeler)
            if "sil" in kelimeler or "kaydı sil" in kelimeler:
                engine = pyttsx3.init()
                engine.setProperty('voice', 'english+f4')
                engine.setProperty('rate', 170)
                engine.say(" What is username? ")
                engine.runAndWait()
                self.ad=self.record(self.tanıyıcı,self.kaynak)
                print(self.ad)
                engine.say("is it?" +self.ad)
                engine.runAndWait()
                cevap=self.record(self.tanıyıcı,self.kaynak)
                print(cevap.lower())
                if cevap.lower()=="evet":
                    self.kullanıcı_adı.setText(self.ad)
                    engine.say("okay I'm checking")
                    engine.runAndWait()
                    print("tamam")
                    self.delete(self.ad.lower())
                elif cevap.lower()=="hayır":
                    engine.say("I did not get it Would you repeat one more time ")
                    engine.runAndWait()
    def record(self,tanıyıcı,kaynak):
        ses=tanıyıcı.listen(kaynak)
        dizi=tanıyıcı.recognize_google(ses,key=None,language="tr-tr")
        return dizi

    def tread(self,x):
        Thread(target=x, args=()).start()

    def take_picture(self):
        kamera=cv2.VideoCapture(0)
        while True:
            return_value,kare=kamera.read()
            if not return_value:break
            cv2.imshow('kare', kare)
            cv2.moveWindow('kare', 10, 10)
            k = cv2.waitKey(10) & 0xff
            if k==27 or k==ord('q'):
                break
            if k==27 or k==ord('c'):
                cv2.imwrite("x.jpg" ,kare)
                cv2.waitKey(1000)
                break
        if kamera.isOpened():
            kamera.release()
        cv2.destroyAllWindows()
        #os.system(' cmd /c "C:/Users/bugra/Pictures/Saved Pictures/x.jpg" ')

    def update_backup(self):
        self.bu_path = os.path.join(os.getcwd(),"backup.db")
        self.backup=sqlite3.connect(self.bu_path)
        self.bağlantı.backup(self.backup,pages=-1)
        self.backup.close()

    def audio_play(self,Dosya):
        self.ses_dosyası=AudioSegment.from_wav(Dosya,"wav")
        play(self.ses_dosyası)

    def init_ui(self):
        self.kullanıcı_adı=QtWidgets.QLineEdit()
        self.parola=QtWidgets.QLineEdit()
        self.parola.setEchoMode(QtWidgets.QLineEdit.Password)
        self.giris=QtWidgets.QPushButton("giriş yap")
        self.kaydol=QtWidgets.QPushButton("kaydol")
        self.sil=QtWidgets.QPushButton("Kaydı sil")
        self.göster=QtWidgets.QPushButton("Veri tabanını göster")
        self.sesli_komut=QtWidgets.QPushButton("Sesli komut")
        self.yazı_alanı=QtWidgets.QLabel("")

        v_box=QtWidgets.QVBoxLayout()

        v_box.addWidget(self.kullanıcı_adı)
        v_box.addWidget(self.parola)
        v_box.addWidget(self.sesli_komut)
        v_box.addWidget(self.yazı_alanı)
        v_box.addStretch()
        v_box.addWidget(self.kaydol)
        v_box.addWidget(self.giris)
        v_box.addWidget(self.sil)
        v_box.addWidget(self.göster)

        h_box=QtWidgets.QHBoxLayout()

        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()

        self.setLayout(h_box)
        self.setWindowTitle("kullanıcı girişi")
        self.setGeometry(300,400,500,400)

        self.giris.clicked.connect(self.login)
        self.kaydol.clicked.connect(self.register)
        self.sil.clicked.connect(self.delete)
        self.göster.clicked.connect(lambda :self.tread(self.Show))
        self.sesli_komut.clicked.connect(self.audio_Assist)

        self.show()

app=QtWidgets.QApplication(sys.argv)
pencere=Pencere()
sys.exit(app.exec())