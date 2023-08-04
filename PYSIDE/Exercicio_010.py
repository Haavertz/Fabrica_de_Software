from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QMainWindow, QPushButton
from PyQt5.QtGui import QPixmap
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exercicio - 10")
        self.setFixedSize(600,600)

        self.Botao = QPushButton("Image - 1", self)
        self.Botao.setGeometry(100,100,180,30)
        
        self.Botao.clicked.connect(self.Imagens)

        self.Botao2 = QPushButton("Image - 2", self)
        self.Botao2.setGeometry(300,100,180,30)

        self.Botao2.clicked.connect(self.imagens2)

    def Imagens(self):      
        self.image = QLabel()
        self.image.setPixmap(QPixmap("images.jpg"))
        self.setCentralWidget(self.image)
        self.image.setGeometry(100,100,180,30)
        return MainWindow

    def imagens2(self):
        self.image2 = QLabel()
        self.image2.setPixmap((QPixmap("Catjpg.jpg")))
        self.setCentralWidget(self.image2)
        self.image2.setGeometry(100,300,300,300)
        return 
        
App = QApplication(sys.argv)
Janela = MainWindow()
Janela.show()
App.exec()