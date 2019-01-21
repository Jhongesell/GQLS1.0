# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'moduloCGUIN01.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(320, 240)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 67, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 67, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 70, 67, 17))
        self.label_3.setObjectName("label_3")
        self.botonN01 = QtWidgets.QPushButton(self.centralwidget)
        self.botonN01.setGeometry(QtCore.QRect(108, 10, 141, 25))
        self.botonN01.setObjectName("botonN01")
        self.botonN02 = QtWidgets.QPushButton(self.centralwidget)
        self.botonN02.setGeometry(QtCore.QRect(108, 40, 141, 25))
        self.botonN02.setObjectName("botonN02")
        self.botonN03 = QtWidgets.QPushButton(self.centralwidget)
        self.botonN03.setGeometry(QtCore.QRect(108, 70, 141, 25))
        self.botonN03.setObjectName("botonN03")
        self.resultado = QtWidgets.QTextEdit(self.centralwidget)
        self.resultado.setGeometry(QtCore.QRect(30, 120, 271, 70))
        self.resultado.setObjectName("resultado")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 320, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Modulo de Campo"))
        self.label.setText(_translate("MainWindow", "Paso N01"))
        self.label_2.setText(_translate("MainWindow", "Paso N02"))
        self.label_3.setText(_translate("MainWindow", "Paso N03"))
        self.botonN01.setText(_translate("MainWindow", "Importar TXT"))
        self.botonN02.setText(_translate("MainWindow", "Interpolar"))
        self.botonN03.setText(_translate("MainWindow", "Graficar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

