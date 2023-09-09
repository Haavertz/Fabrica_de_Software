from PySide6.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QMainWindow
from PySide6.QtCore import Qt
import sys

# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exercico - 8")
        self.setFixedSize(600,600)
        self.hora = QLabel("Digite o numero de hora: ", self)
        self.hora.setGeometry(50,20,180,80)
        
        self.hora = QLineEdit(self)
        self.hora.setGeometry(80,20,180,30)
        # self.input1 = QLineEdit(self)
        # self.input1.setGeometry(100,10,80,30)
        


App = QApplication(sys.argv)
Janela = MainWindow()
Janela.show()
App.exec()