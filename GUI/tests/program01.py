
import sys 
from PyQt5.QtWidgets import * 
                    
   
#Main Window 
class App(QWidget): 
    def __init__(self): 
        super().__init__() 
        self.title = 'Tabla con PyQt5'
        self.left = 0
        self.top = 0
        self.width = 300
        self.height = 200
   
        self.setWindowTitle(self.title) 
        self.setGeometry(self.left, self.top, self.width, self.height) 
   
        self.createTable() 
   
        self.layout = QVBoxLayout() 
        self.layout.addWidget(self.tableWidget) 
        self.setLayout(self.layout) 
   
        #Show window 
        self.show() 
   
    #Create table 
    def createTable(self): 
        self.tableWidget = QTableWidget() 
  
        #Row count 
        self.tableWidget.setRowCount(4)  
  
        #Column count 
        self.tableWidget.setColumnCount(2)   
        a = 3
        b = 4
        c = a+b
  
        self.tableWidget.setItem(0,0, QTableWidgetItem("Variable")) 
        self.tableWidget.setItem(0,1, QTableWidgetItem("Valor")) 
        self.tableWidget.setItem(1,0, QTableWidgetItem("a"))
        self.tableWidget.setItem(1,1, QTableWidgetItem(str(a)))
        self.tableWidget.setItem(2,0, QTableWidgetItem("b")) 
        self.tableWidget.setItem(2,1, QTableWidgetItem(str(b))) 
        self.tableWidget.setItem(3,0, QTableWidgetItem("c")) 
        self.tableWidget.setItem(3,1, QTableWidgetItem(str(c))) 
   
        #Table will fit the screen horizontally 
        self.tableWidget.horizontalHeader().setStretchLastSection(True) 
        self.tableWidget.horizontalHeader().setSectionResizeMode( 
            QHeaderView.Stretch) 
   
if __name__ == '__main__': 
    app = QApplication(sys.argv) 
    ex = App() 
    sys.exit(app.exec_()) 

