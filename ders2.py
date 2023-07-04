from PyQt5 import QtWidgets,QtGui
import sys

def Pencere():
    app =QtWidgets.QApplication(sys.argv)
    pencere=QtWidgets.QWidget()
    pencere.setWindowTitle("Ders2")

    ##
    etiket=QtWidgets.QLabel(pencere)
    etiket.setText("etiket")
    etiket.move(200,30)
    etiket2=QtWidgets.QLabel(pencere)
    etiket2.setPixmap(QtGui.QPixmap("indir.jpg"))
    etiket2.move(200,50)
    pencere.setGeometry(100,100,500,500)
    ##
    
    pencere.show()

    sys.exit(app.exec_())
Pencere()