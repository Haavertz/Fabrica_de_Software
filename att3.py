from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QLabel
from PyQt5.QtCore import Qt
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exercicio3")
        self.setGeometry(100,100,300,150)
        
        self.label1 = QLabel("Numero 1: ", self)
        self.label1.setGeometry(10,10,80,30)
        
        self.label1 = QLabel(self)
        self.label1.setGeometry(100,50,80,30)
        
        
        self.label2 = QLabel("Numero 2: ", self)
        self.label2.setGeometry(10,10,80,30)
        
        self.label2 = QLabel(self)
        self.label2.setGeometry(100,50,80,30)
        
        self.button = QPushButton("Calculando: ", self)
        self.button.setGeometry(190, 10, 100, 70)
        


app = QApplication(sys.argv)
janela = MainWindow()
janela.show()
app.exec()