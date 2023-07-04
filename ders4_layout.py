import sys
from PyQt5 import QtWidgets

def  Pencere():
    app=QtWidgets.QApplication(sys.argv)
    buton1=QtWidgets.QPushButton("Tamam")
    buton2=QtWidgets.QPushButton("iptal")
##
    h_box=QtWidgets.QHBoxLayout()
    h_box.addStretch()
    h_box.addWidget(buton2)
    h_box.addWidget(buton1)

    v_box=QtWidgets.QVBoxLayout()
    v_box.addStretch()
    v_box.addLayout(h_box)

    pencere =QtWidgets.QWidget()
    pencere.setWindowTitle("Pencere")

    pencere.setLayout(v_box)

    pencere.setGeometry(100,100,500,500)

    pencere.show()


    sys.exit(app.exec())

Pencere()