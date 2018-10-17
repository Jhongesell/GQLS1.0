from PyQt5.QtWidgets import QDialog,QApplication , QListWidget, QCheckBox ,QComboBox, QGroupBox ,QDialogButtonBox , QVBoxLayout , QFrame,QTabWidget, QWidget, QLabel, QLineEdit
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

        name = QLabel("Nombre de usuario:")
        nameEdit = QLineEdit()

        dob = QLabel("Fecha de toma de muestra:")
        dobedit = QLineEdit()

        age = QLabel("Peso total:")
        ageedit = QLineEdit()

        PhoneNu = QLabel("Peso de filtro fino:")
        phonedit = QLineEdit()

        layout = QVBoxLayout()
        layout.addWidget(name)
        layout.addWidget(nameEdit)
        layout.addWidget(dob)
        layout.addWidget(dobedit)
        layout.addWidget(age)
        layout.addWidget(ageedit)
        layout.addWidget(PhoneNu)
        layout.addWidget(phonedit)

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
#        linux = QCheckBox("GNU/Linux")

        checkLayout = QVBoxLayout()
        checkLayout.addWidget(windows)
        checkLayout.addWidget(mac)
#        checkLayout.addWidget(linux)
        checkGroup.setLayout(checkLayout)


        mainLayout = QVBoxLayout()
#        mainLayout.addWidget(selecGroup)
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
        #layout.addWidget(listWidget)
        #layout.addWidget(checkBox)
        layout.addWidget(self.MyUI())
        self.setLayout(layout)



    def MyUI(self):
        canvas = Canvas(self, width=8, height=4)
        canvas.move(0,0)

class Canvas(FingureCanvas):
    def __init__(self, parent = None, width =5, height = 5, dpi =100):

        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)

        FingureCanvas.__init__(self, fig)
        self.setParent(parent)


        self.plot()

    def plot(self):
        print("hello")

        # Pie chart, where the slices will be ordered and plotted counter-clockwise:
        x = np.array([19, 6, 29, 5])

        labels = ['Tigre', 'Sexsemayo', 'Rayo', 'Lurin']
        explode = (0.0, 0.0, 0.0, 0.1)  # only "explode" the 2nd slice (i.e. 'Hogs')

        #fig1, ax = plt.subplots()
        #fig1,
        ax = self.figure.add_subplot(111)
        ax.pie(x, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
        ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.



if __name__ == "__main__":
    app = QApplication(sys.argv)
    tabdialog = TabDialog()
    tabdialog.show()
    app.exec()
