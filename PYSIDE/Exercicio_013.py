from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QMainWindow, QPushButton, QLineEdit, QCheckBox, QVBoxLayout, QDialog
from PyQt5.QtCore import Qt, QSize

import sys

class MainWindow1(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exercicio - 13")
        # self.setFixedSize(800,400)
        self.button = QPushButton("BaH",self)
        self.button.setGeometry(100,100,500,100)
        self.button.clicked.connect(self.otaJanela)
        
     
    def otaJanela(self):
        self.SecordaryWindow = SecondaryWindow()
        self.SecordaryWindow.show()
        
class SecondaryWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ota Janela")
        
        
App = QApplication(sys.argv)
Jn = MainWindow1()
Jn.show()
App.exec()