from PyQt5.QtWidgets import QDialog,QApplication , QListWidget, QCheckBox ,QComboBox, QGroupBox ,QDialogButtonBox , QVBoxLayout, QHBoxLayout , QFrame,QTabWidget, QWidget, QLabel, QLineEdit
import sys
from PyQt5.QtCore import QFileInfo
from PyQt5.QtGui import QIcon
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FingureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np


class TabDialog(QDialog):
    def __init__(self):
        super().__init__()

        title = "MENÚ PRINCIPAL (Gestor de Caudales Líquidos y Sólidos)"
        left = 100
        top = 175
        width = 800
        height = 500

        self.setWindowTitle(title)
        self.setGeometry(left, top, width, height)
        self.setWindowIcon(QIcon("myicon.png"))

        tabwidget = QTabWidget()
        tabwidget.addTab(FirstTab(), "Módulo de laboratorio")
        tabwidget.addTab(TabTwo(), "Módulo de campo")
        tabwidget.addTab(TabThree(), "Módulo de resultados")


        buttonbox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)

        buttonbox.accepted.connect(self.accept)
        buttonbox.rejected.connect(self.reject)

        vbox = QVBoxLayout()
        vbox.addWidget(tabwidget)

        vbox.addWidget(buttonbox)

        self.setLayout(vbox)

class FirstTab(QWidget):
    def __init__(self):

        super().__init__()

        codigodebot = QLabel("01. Código de botella:")
        codigodebotEdit = QLineEdit()

        numeroderepeticiones = QLabel("02. Número de repeticiones")
        numeroderepeticionesEdit = QLineEdit()

        fecha = QLabel("03. Fecha de toma de muestra:")
        fechaEdit = QLineEdit()

        niveldecota = QLabel("04. Nivel de cota")
        niveldecotaEdit = QLineEdit()

        codigodechapa = QLabel("05. Código de chapa")
        codigodechapaEdit = QLineEdit()

        pesobruto = QLabel("06. Peso total de botella con agua:")
        pesobrutoEdit = QLineEdit()

        pesotara = QLabel("07. Peso de la botella")
        pesotaraEdit = QLineEdit()

        pesoneto = QLabel("08. Peso del líquido")
        pesonetoEdit = QLineEdit()

        pesoinifiltfin = QLabel("09. Peso inicial del filtro fino")
        pesoinifiltfinEdit = QLineEdit()

        pesofinfiltfin = QLabel("10. Peso final del filtro fino")
        pesofinfiltfinEdit = QLineEdit()

        pesoinifiltgru = QLabel("11. Peso inicial del filtro grueso")
        pesoinifiltgruEdit = QLineEdit()

        pesofinfiltgru = QLabel("12. Peso final del filtro grueso")
        pesofinfiltgruEdit = QLineEdit()

        nombreestacion = QLabel("13. Nombre de la estación")
        nombreestacionEdit = QLineEdit()

        layout = QVBoxLayout()

        layout.addWidget(codigodebot)
        layout.addWidget(codigodebotEdit)
        layout.addWidget(numeroderepeticiones)
        layout.addWidget(numeroderepeticionesEdit)
        layout.addWidget(fecha)
        layout.addWidget(fechaEdit)
        layout.addWidget(niveldecota)
        layout.addWidget(niveldecotaEdit)
        layout.addWidget(codigodechapa)
        layout.addWidget(codigodechapaEdit)
        layout.addWidget(pesobruto)
        layout.addWidget(pesobrutoEdit)
        layout.addWidget(pesotara)
        layout.addWidget(pesotaraEdit)
        layout.addWidget(pesoneto)
        layout.addWidget(pesonetoEdit)
        layout.addWidget(pesoinifiltfin)
        layout.addWidget(pesoinifiltfinEdit)
        layout.addWidget(pesofinfiltfin)
        layout.addWidget(pesofinfiltfinEdit)
        layout.addWidget(pesoinifiltgru)
        layout.addWidget(pesoinifiltgruEdit)
        layout.addWidget(pesofinfiltgru)
        layout.addWidget(pesofinfiltgruEdit)
        layout.addWidget(nombreestacion)
        layout.addWidget(nombreestacionEdit)

        self.setLayout(layout)

class TabTwo(QWidget):
    def __init__(self):
        super().__init__()

        selectGroup = QGroupBox("Seleccione a donde va a exportar los datos")
        combo = QComboBox()
        list = ["Hoja de cálculo", "Archivo ASCII", "Base de datos"]
        combo.addItems(list)
        selecLayout = QVBoxLayout()
        selecLayout.addWidget(combo)
        selectGroup.setLayout(selecLayout)


        checkGroup = QGroupBox("Va a visualzar datos obtenidos de:")
        windows = QCheckBox("Perfilador vertical triple")
        mac = QCheckBox("Ojo de pez")

        checkLayout = QVBoxLayout()
        checkLayout.addWidget(windows)
        checkLayout.addWidget(mac)
        checkGroup.setLayout(checkLayout)


        mainLayout = QVBoxLayout()
        mainLayout.addWidget(selectGroup)
        mainLayout.addWidget(checkGroup)
        self.setLayout(mainLayout)




class TabThree(QWidget):
    def __init__(self):
        super().__init__()


        label = QLabel("Visualización de resultados")
        #listWidget = QListWidget()
        #list = []

        #for i in range(1,7):
        #    list.append("Punto de medición número N")

        #listWidget.insertItems(0, list)
        #checkBox = QCheckBox("Guardar imagen como archivo PNG")


        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(self.MyUI())
        self.setLayout(layout)



    def MyUI(self):
        canvas = Canvas(self, width=4, height=3)
        canvas.move(300,10)

class Canvas(FingureCanvas):
    def __init__(self, parent = None, width =5, height = 5, dpi =100):

        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)

        FingureCanvas.__init__(self, fig)
        self.setParent(parent)


        self.plot()

    def plot(self):
        print("hello")

        Y, X = np.mgrid[-4:0:100j, -60:0:100j]
        U = -1 - X**2 + Y
        V = 1 + X - Y**2
        speed = np.sqrt(U*U + V*V)

        ax0 = self.figure.add_subplot(111)
        strm = ax0.streamplot(X, Y, U, V, color=U, linewidth=2, cmap=plt.cm.autumn)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    tabdialog = TabDialog()
    tabdialog.show()
    app.exec()
