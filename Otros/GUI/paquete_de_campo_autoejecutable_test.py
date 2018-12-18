# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'paquete_de_campo.ui'
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
        Dialog.resize(685, 199)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_00_titulo_paquetedecampo = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_00_titulo_paquetedecampo.setFont(font)
        self.label_00_titulo_paquetedecampo.setObjectName(_fromUtf8("label_00_titulo_paquetedecampo"))
        self.verticalLayout.addWidget(self.label_00_titulo_paquetedecampo)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_01_rutadearchivos = QtGui.QLabel(Dialog)
        self.label_01_rutadearchivos.setObjectName(_fromUtf8("label_01_rutadearchivos"))
        self.horizontalLayout.addWidget(self.label_01_rutadearchivos)
        self.lineEdit_01_rutadearchivos = QtGui.QLineEdit(Dialog)
        self.lineEdit_01_rutadearchivos.setEnabled(False)
        self.lineEdit_01_rutadearchivos.setObjectName(_fromUtf8("lineEdit_01_rutadearchivos"))
        self.horizontalLayout.addWidget(self.lineEdit_01_rutadearchivos)
        self.pushButton_01_rutadearchivos = QtGui.QPushButton(Dialog)
        self.pushButton_01_rutadearchivos.setObjectName(_fromUtf8("pushButton_01_rutadearchivos"))
        self.horizontalLayout.addWidget(self.pushButton_01_rutadearchivos)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.pushButton_02_Guardar = QtGui.QPushButton(Dialog)
        self.pushButton_02_Guardar.setObjectName(_fromUtf8("pushButton_02_Guardar"))
        self.verticalLayout.addWidget(self.pushButton_02_Guardar)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.lineEdit_01_rutadearchivos, self.pushButton_01_rutadearchivos)
        Dialog.setTabOrder(self.pushButton_01_rutadearchivos, self.pushButton_02_Guardar)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Paquete de campo", None))
        self.label_00_titulo_paquetedecampo.setText(_translate("Dialog", "Formulario para lectura de datos", None))
        self.label_01_rutadearchivos.setText(_translate("Dialog", "Ruta de archivos", None))
        self.pushButton_01_rutadearchivos.setText(_translate("Dialog", "&Examinar", None))
        self.pushButton_02_Guardar.setText(_translate("Dialog", "&Guardar", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

