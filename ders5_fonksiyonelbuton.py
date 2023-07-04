import sys
from PyQt5 import QtWidgets

class Pencere(QtWidgets.QWidget):
    def __init__(self):
        super().__init__() # QWidget sınıfını inherit ederek üzerine birşeyler kattık

        self.init_ui() #arayüz fonksiyonumuz

    def init_ui(self):
        self.yazı_alanı=QtWidgets.QLabel("henüz tıklanmadı.")
        self.buton=QtWidgets.QPushButton("bana tıkla")
        self.say=0

        v_box=QtWidgets.QVBoxLayout()
        v_box.addWidget(self.buton)
        v_box.addWidget(self.yazı_alanı)
        v_box.addStretch()

        h_box=QtWidgets.QHBoxLayout()

        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()

        self.setLayout(h_box) #oluşacak nesneye oluşturuğumuz layoutu atıyoruz

        self.buton.clicked.connect(self.click) #connect ile bir fonksiyonu başka bir fonksiyona bağlayabiliyoruz

    def click(self):
        self.say +=1
        self.yazı_alanı.setText(str(self.say)+" defa tıklandı")


app=QtWidgets.QApplication(sys.argv)

pencere =Pencere()
pencere.show()
sys.exit(app.exec())