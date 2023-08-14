from PyQt5.QtWidgets import QApplication, QLineEdit, QMainWindow, QCheckBox, QPushButton, QLabel, QFont
import brazilcep
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.Init()
        
    def Init(self):
        self.setWindowTitle("Busque Cep")
        self.setFixedSize(700,400)
        self.Edit()        

        
        
    def Edit(self):
        self.Title = QLabel("BEM VINDO AO CEP", self)
        
        self.Title.setGeometry(100, 0, 50, 50)
        

App = QApplication(sys.argv)
Janela = MainWindow()
Janela.show()
App.exec()