from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QMainWindow, QPushButton, QLineEdit, QCheckBox, QVBoxLayout, QDialog
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QPixmap

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
        self.setFixedSize(QSize(600,600))
        self.butao = QPushButton("Image", self)
        self.butao.setGeometry(300,300,100,50)
        self.butao.clicked.connect(self.image)


    def image(self):
        self.image = QLabel()
        self.image.setPixmap(QPixmap("images.jpg"))
        self.setCentralWidget(self.image)
        self.image.setGeometry(100,100,100,100)
        
        
App = QApplication(sys.argv)
Jn = MainWindow1()
Jn.show()
App.exec()