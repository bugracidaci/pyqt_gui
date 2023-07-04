import sys
from PyQt5 import QtWidgets

def  Pencere():
    app=QtWidgets.QApplication(sys.argv)
    pencere =QtWidgets.QWidget()
    pencere.setWindowTitle("Pencere")
    pencere.show()
    sys.exit(app.exec())
print("hello git!")
Pencere()