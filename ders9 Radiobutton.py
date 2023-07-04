import colorsys

from PyQt5 import QtWidgets
import sys

class Pencere(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def kontrol(self,python,php,java,yazı):

        if python:
            yazı.setText("Python seçildi")
        if php:
            yazı.setText("PHP seçildi")
        if java:
            yazı.setText("Java seçildi")
    def init_ui(self):
        self.radio_yazısı=QtWidgets.QLabel("hangi dili daha çok seviyorsun")

        self.Java=QtWidgets.QRadioButton("Java")
        self.Python=QtWidgets.QRadioButton("Python")
        self.PHP=QtWidgets.QRadioButton("PHP")

        self.yazı_alanı=QtWidgets.QLabel("")

        self.button=QtWidgets.QPushButton("Gönder")

        v_box=QtWidgets.QVBoxLayout()

        v_box.addWidget(self.radio_yazısı)
        v_box.addWidget(self.Java)
        v_box.addWidget(self.Python)
        v_box.addWidget(self.PHP)
        v_box.addStretch()
        v_box.addWidget(self.yazı_alanı)
        v_box.addWidget(self.button)

        self.setLayout(v_box)

        self.button.clicked.connect(lambda : self.kontrol(self.Python.isChecked(),self.PHP.isChecked(),self.Java.isChecked(),self.yazı_alanı))
        self.setWindowTitle("Radio Button")


        self.show()

app=QtWidgets.QApplication(sys.argv)
pencere=Pencere()
sys.exit(app.exec())