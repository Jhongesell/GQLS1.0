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

        title = "Lineas de corriente"
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
        print("hello")

        # Pie chart, where the slices will be ordered and plotted counter-clockwise:
        x = np.array([19, 6, 29, 5])

        labels = ['Tigre', 'Sixsimayo', 'Rayo', 'Lurin']
        explode = (0.0, 0.0, 0.0, 0.1)  # only "explode" the 2nd slice (i.e. 'Hogs')

        #fig1, ax = plt.subplots()
        #fig1,
        ax = self.figure.add_subplot(111)
        ax.pie(x, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
        ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

        #plt.show()

        #***********************
        # x = np.array([50, 30, 25])

        # labels = ['Apples', 'Bananas', 'Melons']
        # ax = self.figure.add_subplot(111)

        # ax.pie(x, labels=labels)


app = QApplication(sys.argv)
window = Window()
window.show()
app.exec()
