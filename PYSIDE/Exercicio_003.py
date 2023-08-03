from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QLabel, QLineEdit
from PyQt5.QtCore import Qt, QSize
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exercicio - 3")
        self.setGeometry(100,100,300,150)
        
        self.label1 = QLabel("Numero 1: ", self)
        self.label1.setGeometry(10,10,80,30)
        
        self.input1 = QLineEdit(self)
        self.input1.setGeometry(100,10,80,30)
        
        
        self.label2 = QLabel("Numero 2: ", self)
        self.label2.setGeometry(10,10,80,30)

        self.input2 = QLineEdit(self)
        self.input2.setGeometry(100,50,80,30)
        
        self.resultado = QLabel(self)
        self.resultado.setGeometry(10,90,280,30)
        
        self.button = QPushButton("Calculando: ", self)
        self.button.setGeometry(190, 10, 100, 70)
        self.button.clicked.connect(self.imprimir)
        

    def imprimir(self):
        one = float(self.input1.text())
        two = float(self.input2.text())
        resultado = one + two
        print(f"Soma é: {resultado}")
        


app = QApplication(sys.argv)
janela = MainWindow()
janela.show()
app.exec()