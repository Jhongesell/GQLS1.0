from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

class Controles(QWidget):

    ruta = ""
    fichero_actual = ""

    def __init__(self, *args): 
        QWidget.__init__(self, *args)

        self.setWindowTitle("Programa Ejemplo")

        contenedor = QVBoxLayout()
        self.setLayout(contenedor)

        btnAbrir = QPushButton("Abrir",None)
        contenedor.addWidget(btnAbrir)
        self.connect(btnAbrir, SIGNAL("clicked()"), self.abrir)

        btnGuardar = QPushButton("Guardar",None)
        contenedor.addWidget(btnGuardar)
        self.connect(btnGuardar, SIGNAL("clicked()"), self.guardar)

        btnNuevo = QPushButton("Nuevo",None)
        contenedor.addWidget(btnNuevo)
        self.connect(btnNuevo, SIGNAL("clicked()"), self.nuevo)

        btnSalir = QPushButton("Salir",None)
        contenedor.addWidget(btnSalir)
        self.connect(btnSalir, SIGNAL("clicked()"), self.salir)

    def abrir(self):
        nombre_fichero = QFileDialog.getOpenFileName(self, "Abrir fichero", self.ruta)
        if nombre_fichero:
            self.fichero_actual = nombre_fichero
            self.setWindowTitle(QFileInfo(nombre_fichero).fileName())
            self.ruta = QFileInfo(nombre_fichero).path()

            # TODO - Aqui va el codigo

    def guardar(self):
        if self.fichero_actual:
            ruta_guardar = self.fichero_actual
        else:
            ruta_guardar = self.ruta

        nombre_fichero = QFileDialog.getSaveFileName(self, "Guardar fichero", ruta_guardar)
        if nombre_fichero:
            self.fichero_actual = nombre_fichero
            self.setWindowTitle(QFileInfo(nombre_fichero).fileName())
            self.ruta = QFileInfo(nombre_fichero).path()

            # TODO - Aqui va el codigo

    def nuevo(self):
        self.fichero_actual = ""
        self.ruta = ""
        self.setWindowTitle("Programa Ejemplo")

    def salir(self):
        exit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    controles = Controles()
    controles.show()
    sys.exit(app.exec_())