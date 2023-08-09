from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QMainWindow, QPushButton, QLineEdit, QCheckBox, QVBoxLayout, QDialog
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QPixmap
from Exercicio_015ma import soma

import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ExercicioMain - 15")
        self.setFixedSize(600,600)
        self.button1 = QLineEdit(int(self))
        self.button2 = QLineEdit(int(self))
        self.button3 = QPushButton("Somando...",self)
        self.button4 = QPushButton("Total",self)
        
        
        
        self.button1.setGeometry(100,100,70,30)
        self.button2.setGeometry(100,150,70,30)
        self.button3.setGeometry(200,110,80,60)
        self.button4.setGeometry(300,110,80,60)
        
        
    def Somar(self):
        tot = soma(
    
        )
        



app = QApplication(sys.argv)
janela = MainWindow()
janela.show()
app.exec()