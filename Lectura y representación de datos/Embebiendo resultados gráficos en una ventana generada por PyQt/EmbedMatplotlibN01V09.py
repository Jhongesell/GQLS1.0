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
        # w = 3
        # Y, X = np.mgrid[-w:w:100j, -w:w:100j]
        # U = 0.5 + 2*Y
        # V = -3 + X - 3*Y**2
        # speed = np.sqrt(U*U + V*V)

        # mask = np.zeros(U.shape, dtype=bool)
        # mask[40:60, 40:60] = True
        # U[:20, :20] = np.nan
        # U = np.ma.array(U, mask=mask)

        ## fig, ax = plt.subplots()
        # ax = self.figure.add_subplot(111)
        # ax.streamplot(X, Y, U, V, color='b')

        # ax.imshow(~mask, extent=(-w, w, -w, w), alpha=0.5,
        #     interpolation='nearest', cmap=plt.cm.gray)
        ##plt.show()

        Y, X = np.mgrid[-4:0:100j, -60:0:100j]
        U = -1 - X**2 + Y
        V = 1 + X - Y**2
        speed = np.sqrt(U*U + V*V)

        #fig0, ax0 = plt.subplots()
        ax0 = self.figure.add_subplot(111)
        #ax0 = self.figure.add_subplot(111)
        strm = ax0.streamplot(X, Y, U, V, color=U, linewidth=2, cmap=plt.cm.autumn)
        #fig0.colorbar(strm.lines)
        #ax0.colorbar(strm.lines)

        #fig1, (ax1, ax2) = plt.subplots(ncols=2)
        #fig1, (ax1, ax2) = plt.subplots(ncols=2)
        #ax1.streamplot(X, Y, U, V, density=[0.5, 1])

        #lw = 5*speed / speed.max()
        #ax2.streamplot(X, Y, U, V, density=0.6, color='k', linewidth=lw)

app = QApplication(sys.argv)
window = Window()
window.show()
app.exec()
