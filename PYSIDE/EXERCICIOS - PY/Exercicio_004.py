from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QLabel, QFormLayout
from PySide6.QtCore import Qt

import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()


        formulario =   QFormLayout()
       
        
        self.setWindowTitle("Exercicio2")
        self.button = QPushButton("butao", self)
        self.setFixedSize(300,300)
        self.button.setGeometry(100, 100 ,100 , 100)
        self.result_label = QLabel(self)
        self.result_label.setGeometry(10,90,280,30)

        formulario.addRow(self.button)
        formulario.addRow(self.result_label)
        
        self.button.clicked.connect(self.imprimir)
        
        widget = QWidget()
        widget.setLayout(formulario)

        # Definindo o widget central da janela principal
        self.setCentralWidget(widget)

    def imprimir(self):
        numero = 4
        if numero %2 == 0:
            print("Par")
        else:
            print("impar")


app = QApplication(sys.argv)
app.setStyle("Fusion")
janela = MainWindow()
janela.show()
app.exec()