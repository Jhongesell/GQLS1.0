#Instrucción para convertir los archivos qrc en py:
#pyrcc5 -o logo3_rc.py loguito.qrc
#Instrucción para convertir los archivos ui en py:
#pyuic5 ap31.ui -o ap31.py
#Código de ejemplo para correr las aplicaciones en Python:
import sys
from PyQt5 import uic, QtWidgets

qtCreatorFile = "gcls.ui" # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):

        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
