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
        x1 = np.linspace(0.0, 5.0)
        #x2 = np.linspace(0.0, 2.0)

        y1 = np.cos(2 * np.pi * x1) * np.exp(-x1)
        #y2 = np.cos(2 * np.pi * x2)

        #plt.subplot(2, 1, 1)
        #plt.plot(x1, y1, 'o-')
        #plt.title('A tale of 2 subplots')
        #plt.ylabel('Damped oscillation')


        #plt.subplot(2, 1, 2)
        #plt.plot(x2, y2, '.-')
        #plt.xlabel('time (s)')
        #plt.ylabel('Undamped')

        ax = self.figure.add_subplot(111)
        ax.plot(x1, y1, '*-')
        ax.set_title('X vs Y')
        #ax.xlabel('Damped oscillation')

app = QApplication(sys.argv)
window = Window()
window.show()
app.exec()
