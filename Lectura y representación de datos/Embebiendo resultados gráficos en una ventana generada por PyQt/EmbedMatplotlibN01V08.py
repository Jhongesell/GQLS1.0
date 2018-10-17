from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
import sys
from PyQt5.QtGui import QIcon
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FingureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        title = "Ventana para graficar funciones"
        left = 100
        top = 175
        width = 800
        height = 500

        icon = "icon.png"

        self.setWindowTitle(title)
        self.setGeometry(left, top, width, height)
        self.setWindowIcon(QIcon("icon.png"))

        self.MyUI()

    def MyUI(self):

        canvas = Canvas(self, width=8, height=4)
        canvas.move(0,0)

        button = QPushButton( "Botón 01", self)
        button.move(100, 450)

        button = QPushButton("Botón 02", self)
        button.move(600, 450)

class Canvas(FingureCanvas):
    def __init__(self, parent = None, width =5, height = 5, dpi =100):

        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)

        FingureCanvas.__init__(self, fig)
        self.setParent(parent)

        self.plot()

    def plot(self):
        #fig, ax = plt.subplots()
        ax = self.figure.add_subplot(111)

        L = 6
        x = np.linspace(0, L)
        ncolors = len(plt.rcParams['axes.prop_cycle'])
        shift = np.linspace(0, L, ncolors, endpoint=False)
        for s in shift:
            ax.plot(x, np.sin(x + s), 'o-')
        ax.set_xlabel('Eje x')
        ax.set_ylabel('Eje y')
        ax.set_title("Hoja de curvas")

app = QApplication(sys.argv)
window = Window()
window.show()
app.exec()
