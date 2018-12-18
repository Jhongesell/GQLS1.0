# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'paquete_principal.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(422, 214)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_00_titulo_paqueteprincipal = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_00_titulo_paqueteprincipal.setFont(font)
        self.label_00_titulo_paqueteprincipal.setObjectName(_fromUtf8("label_00_titulo_paqueteprincipal"))
        self.verticalLayout.addWidget(self.label_00_titulo_paqueteprincipal)
        self.pushButton_01_paquetedecampo = QtGui.QPushButton(Dialog)
        self.pushButton_01_paquetedecampo.setObjectName(_fromUtf8("pushButton_01_paquetedecampo"))
        self.verticalLayout.addWidget(self.pushButton_01_paquetedecampo)
        self.pushButton_02_paquetedelaboratorio = QtGui.QPushButton(Dialog)
        self.pushButton_02_paquetedelaboratorio.setObjectName(_fromUtf8("pushButton_02_paquetedelaboratorio"))
        self.verticalLayout.addWidget(self.pushButton_02_paquetedelaboratorio)
        self.pushButton_03_interpolacionderio = QtGui.QPushButton(Dialog)
        self.pushButton_03_interpolacionderio.setObjectName(_fromUtf8("pushButton_03_interpolacionderio"))
        self.verticalLayout.addWidget(self.pushButton_03_interpolacionderio)
        self.pushButton_04_cargardatadesedimentosenelrio = QtGui.QPushButton(Dialog)
        self.pushButton_04_cargardatadesedimentosenelrio.setObjectName(_fromUtf8("pushButton_04_cargardatadesedimentosenelrio"))
        self.verticalLayout.addWidget(self.pushButton_04_cargardatadesedimentosenelrio)
        self.pushButton_05_mostrarresultados = QtGui.QPushButton(Dialog)
        self.pushButton_05_mostrarresultados.setObjectName(_fromUtf8("pushButton_05_mostrarresultados"))
        self.verticalLayout.addWidget(self.pushButton_05_mostrarresultados)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.pushButton_01_paquetedecampo, self.pushButton_02_paquetedelaboratorio)
        Dialog.setTabOrder(self.pushButton_02_paquetedelaboratorio, self.pushButton_03_interpolacionderio)
        Dialog.setTabOrder(self.pushButton_03_interpolacionderio, self.pushButton_04_cargardatadesedimentosenelrio)
        Dialog.setTabOrder(self.pushButton_04_cargardatadesedimentosenelrio, self.pushButton_05_mostrarresultados)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Paquete principal", None))
        self.label_00_titulo_paqueteprincipal.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">Software Hidrosedimentario para Rios</span></p></body></html>", None))
        self.pushButton_01_paquetedecampo.setText(_translate("Dialog", "Paquete de &campo", None))
        self.pushButton_02_paquetedelaboratorio.setText(_translate("Dialog", "Paquete de &laboratorio", None))
        self.pushButton_03_interpolacionderio.setText(_translate("Dialog", "&Interpolacion de seccion de rio", None))
        self.pushButton_04_cargardatadesedimentosenelrio.setText(_translate("Dialog", "Cargar &data de sedimentos en el rio", None))
        self.pushButton_05_mostrarresultados.setText(_translate("Dialog", "&Mostrar resultados", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

