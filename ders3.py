from PyQt5 import QtWidgets,QtGui
import sys

def Pencere():

    app=QtWidgets.QApplication(sys.argv)

    pencere=QtWidgets.QWidget()
    pencere.setWindowTitle("Ders3")
    ##
    buton=QtWidgets.QPushButton(pencere)
    buton.move(100,200)
    buton.setText("Button")
    ##
    etiket=QtWidgets.QLabel(pencere)
    etiket.setText("merhaba dünya")
    etiket.setGeometry(100,100,500,500)



    pencere.setGeometry(100,100,500,500)




    pencere.show()
    sys.exit(app.exec())

Pencere()