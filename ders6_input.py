import sys
from PyQt5 import QtWidgets

class Pencere(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.yazı_alanı=QtWidgets.QLineEdit() #textbox için
        self.temizle=QtWidgets.QPushButton("temizle")
        self.yazdır=QtWidgets.QPushButton("Yazdır")

        v_box=QtWidgets.QVBoxLayout()
        v_box.addWidget(self.yazı_alanı)
        v_box.addWidget(self.temizle)
        v_box.addWidget(self.yazdır)
        v_box.addStretch()

        self.setLayout(v_box)

        self.temizle.clicked.connect(self.click)
        self.yazdır.clicked.connect(self.click)

        self.show()

    def click(self):

#iki tane button var hangisinin basıldığını anlamak için
#Qwidget içindeki sender fonksiyonunu kullanacağız
        gönderici=self.sender()
        if gönderici.text()=="temizle":
            self.yazı_alanı.clear()
        else:
            print(self.yazı_alanı.text())

app=QtWidgets.QApplication(sys.argv)
nesne=Pencere()
sys.exit(app.exec())