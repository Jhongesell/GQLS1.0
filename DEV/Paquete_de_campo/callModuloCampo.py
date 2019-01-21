#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

#Importar aquí las librerías a utilizar
import pandas as pd
import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt

from PyQt5 import uic, QtWidgets
qtCreatorFile = "moduloCGUIN01.ui" #Aquí va el nombre de tu archivo
Ui_MainWindow,QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
	def __init__(self):
		QtWidgets.QMainWindow.__init__(self)
		Ui_MainWindow.__init__(self)
		self.setupUi(self)

		#Aquí van los botones
		self.botonN01.clicked.connect(self.getTXT)
        #self.botonN02.clicked.connect(self.interpol12D)
		self.botonN03.clicked.connect(self.plot)

	#Esta función abre el archivo CSV
	def getTXT(self):
		filePath, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '/home/jhon/Documentos/Clones descargadas de usuarios varios en Github/Jhon Gesell/GQLS1.0/DEV/Paquete_de_campo/')
		if filePath != "":
			print ("Dirección",filePath) #Opcional imprimir la dirección del archivo
			self.df = pd.read_csv(str(filePath,header=1,delim_whitespace=True))
            
    #def interpol2D(self):
     #   print("hola")

	#Aquí van las nuevas funciones
	def plot(self):
		x=self.df['col1']
		y=self.df['col2']
		plt.plot(x,y)
		plt.show()
		stad_st="Estadísticas del col2: " + str(self.df['col2'].describe())
		self.resultado.setText(stad_st)

if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	window = MyApp()
	window.show()
	sys.exit(app.exec())