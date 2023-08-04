from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QMainWindow, QPushButton, QFrame, QVBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.Inicio()
        self.setFixedSize(600,600)
        
    def Inicio(self):
        
        self.setWindowTitle("Exercicio - 10")

        self.Botao = QPushButton("Image - 1", self)
        self.Botao.setGeometry(100,100,180,30)
        
        self.Botao.clicked.connect(self.Imagens)

        self.Botao2 = QPushButton("Image - 2", self)
        self.Botao2.setGeometry(300,100,180,30)

        self.Botao2.clicked.connect(self.imagens2)
        
        self.image_frame = QFrame(self)
        self.image_frame.setFrameShape(QFrame.Box)
        self.image_frame.setFixedSize(300,300)
        self.image_frame.setLayout(QVBoxLayout())
        
        self.image_Qlabel = QLabel(self.image_frame)
        self.image_Qlabel.setAlignment(Qt.AlignCenter)
        self.image_frame.layout().addWidget(self.image_Qlabel)
        
        Layout = QVBoxLayout()
        Layout.addWidget(self.Botao)
        Layout.addWidget(self.Botao2)
        Layout.addWidget(self.image_frame)
        
        self.image_frame.setGeometry(140,180,180,30)
        self.setLayout(Layout)
        
    def Imagens(self):      
        self.image = QLabel()
        self.image.setPixmap(QPixmap("images.jpg"))
        self.setCentralWidget(self.image)
        self.image.setGeometry(100,100,180,30)


    def imagens2(self):
        self.image2 = QLabel()
        self.image2.setPixmap((QPixmap("Catjpg.jpg")))
        self.setCentralWidget(self.image2)
        self.image2.setGeometry(100,300,300,300)

    def ImagensT(self):
        self.image_Qlabel.setScaledContents(True)
        self.image_label.setPixmap()
        
App = QApplication(sys.argv)
Janela = MainWindow()
Janela.show()
App.exec()