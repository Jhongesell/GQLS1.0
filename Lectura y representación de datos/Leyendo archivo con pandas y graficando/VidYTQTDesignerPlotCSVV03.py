#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

#Importar aquí las librerías a utilizar
import pandas as pd
import matplotlib.pyplot as plt

from PyQt5 import uic, QtWidgets

qtCreatorFile = "appandasV02.ui" #Aquí va el nombre de tu archivo

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        #Aquí van los botones
        self.boton1.clicked.connect(self.getCSV)
        self.boton2.clicked.connect(self.plot)


    #Esta función abre el archivo CSV
    def getCSV(self):
        filePath, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Abrir archivo', '/home/jhon/Documentos/Tutoriales de Canales de Youtube')
        if filePath != "":
            print ("Dirección",filePath) #Opcional imprimir la dirección del archivo
            self.df = pd.read_csv(str(filePath))

    #Aquí van las nuevas funciones
    def plot(self):
        x=self.df['col1']
        y=self.df['col2']
        plt.plot(x,y)
        plt.show()
        stad_st="Estadísticas de col2: "+str(self.df['col2'].describe())
        self.resultado.setText(stad_st)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec())


#Archivo CSV para hacer la prueba: http://bit.ly/2N6eiN0
#Instrucción para convertir los archivos qrc en py:
#pyrcc5 -o logo3_rc.py loguito.qrc
#Instrucción para convertir los archivos ui en py:
#pyuic5 ap31.ui -o ap31.py
