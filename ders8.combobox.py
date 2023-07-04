from PyQt5 import QtWidgets
import sys

class Pencere(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def kontrol(self,checkboxdurumu,x):  # x yerine self.yazı_alanı gelecek
        if checkboxdurumu:
            x.setText("Tebrikler")
        else:
            x.setText("Ayıp ettin")
    def init_ui(self):

        self.checkbox=QtWidgets.QCheckBox("onaylıyor musunuz?")
        self.yazı_alanı=QtWidgets.QLabel()
        self.button=QtWidgets.QPushButton("Gönder")



        v_box=QtWidgets.QVBoxLayout()

        v_box.addWidget(self.checkbox)
        v_box.addWidget(self.yazı_alanı)
        v_box.addWidget(self.button)

        self.setLayout(v_box)
        self.setWindowTitle("checkbox")

        self.button.clicked.connect(lambda : self.kontrol(self.checkbox.isChecked(),self.yazı_alanı)) # birinci parametre bool değer ikinci parametre bir label lambda olmadan fonksiyonda kullanamayız 
        self.show()

app=QtWidgets.QApplication(sys.argv)
pencere=Pencere()
sys.exit(app.exec())