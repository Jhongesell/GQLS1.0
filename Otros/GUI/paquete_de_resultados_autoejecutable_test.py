# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'paquete_de_resultados.ui'
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
        Dialog.resize(538, 331)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_00_titulo_paquetederesultados = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_00_titulo_paquetederesultados.setFont(font)
        self.label_00_titulo_paquetederesultados.setObjectName(_fromUtf8("label_00_titulo_paquetederesultados"))
        self.verticalLayout.addWidget(self.label_00_titulo_paquetederesultados)
        self.graphicsView_graficodeseccionderio = QtGui.QGraphicsView(Dialog)
        self.graphicsView_graficodeseccionderio.setObjectName(_fromUtf8("graphicsView_graficodeseccionderio"))
        self.verticalLayout.addWidget(self.graphicsView_graficodeseccionderio)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Paquete de resultados", None))
        self.label_00_titulo_paquetederesultados.setText(_translate("Dialog", "Seccion del rio con sus caudales solidos y liquidos", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

