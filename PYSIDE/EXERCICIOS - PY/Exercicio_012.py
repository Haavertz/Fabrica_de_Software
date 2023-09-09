from PySide6.QtWidgets import QApplication, QWidget, QLabel, QMainWindow, QPushButton, QLineEdit, QCheckBox, QVBoxLayout
from PySide6.QtCore import Qt, QSize

import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exercicio - 12")
        self.setFixedSize(QSize(600,550))
        self.nome = QLabel("Nome:",self)
        self.cpf = QLabel("CPF:", self)
        self.fone = QLabel("Telefone:", self)
        self.Cadastro = QPushButton("Cadastrar",self)
        self.Qlabel = QLabel()
        
        self.nome_balao = QLineEdit(self)
        self.cpf_balao = QLineEdit(self)
        self.fone_balao = QLineEdit(self)
        self.quadrati()
        
        self.nome.setGeometry(30,30,180,30)
        self.cpf.setGeometry(40,70,180,30)
        self.fone.setGeometry(20,110,180,30)
        
        self.nome_balao.setGeometry(70,30,180,30)
        self.cpf_balao.setGeometry(70,70,180,30)
        self.fone_balao.setGeometry(70,110,180,30)
        self.Cadastro.setGeometry(50,500,500,30)
        
        # self.Cadastro.clicked.connect(self.All)
        
    def All(self):
        self.alt = QLabel()
        self.alt.setWidget
        
        pass
    def quadrati(self): 
        self.quadrati = QLabel("- Homen", self)
        self.quadrado = QCheckBox(self)
        self.quadrati.setGeometry(60,149,180,30)
        self.quadrado.setGeometry(40,150,180,30)
                
    
App = QApplication(sys.argv)
Jn = MainWindow()
Jn.show()
App.exec()