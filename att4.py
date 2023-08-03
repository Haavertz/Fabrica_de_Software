from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QLabel, QLineEdit
from PyQt5.QtCore import Qt, QSize
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exercicio - 4")
        self.setGeometry(100,100,300,150)
        
        self.label1 = QLabel("Numero 1: ", self)
        self.label1.setGeometry(10,10,80,30)
        
        self.input1 = QLineEdit(self)
        self.input1.setGeometry(100,10,80,30)
        
        
        self.label2 = QLabel("Numero 2: ", self)
        self.label2.setGeometry(10,10,80,30)

        self.input2 = QLineEdit(self)
        self.input2.setGeometry(100,50,80,30)
        
        self.label3 = QLabel("Numero 3: ", self)
        self.label3.setGeometry(10,10,80,30)

        self.input3 = QLineEdit(self)
        self.input3.setGeometry(100,90,80,30)


        self.label4 = QLabel("Numero 4: ", self)
        self.label4.setGeometry(10,10,80,30)

        self.input4 = QLineEdit(self)
        self.input4.setGeometry(100,130,80,30)

        self.resultado = QLabel(self)
        self.resultado.setGeometry(10,90,280,30)
        
        self.button = QPushButton("Calculando: ", self)
        self.button.setGeometry(190, 10, 100, 70)
        self.button.clicked.connect(self.imprimir)
        

    def imprimir(self):
        one = float(self.input1.text())
        two = float(self.input2.text())
        tree = float(self.input1.text())
        four = float(self.input2.text())
        resultado = (one + two + tree + four)/4
        print(f"Soma é: {resultado}")
        


app = QApplication(sys.argv)
janela = MainWindow()
janela.show()
app.exec()