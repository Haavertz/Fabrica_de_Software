# Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o 
# valor seja invalido e continue pedindo até que o usuário informe um valor válido

from PySide6.QtWidgets import (QApplication, QVBoxLayout, 
QMainWindow, QLabel, QLineEdit, QWidget, QFrame, QPushButton)
from PySide6.QtGui import QIntValidator, QFont


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exercicio - 16")
        self.setFixedSize(350, 400)

        self.central = QWidget(self)
        self.setCentralWidget(self.central)

        layout = QVBoxLayout(self.central)

        self.frame = QFrame(self.central)
        self.frame.setFrameShape(QFrame.Box)

        self.layout_Frame = QVBoxLayout(self.frame)
        layout.addWidget(self.frame)

        self.lbl_Titulo = QLabel("          Bem vindo", self)
        self.font = QFont()
        self.font.setPixelSize(30)
        self.font.setBold(True)
        self.lbl_Titulo.setFont(self.font)

        self.lbl_Value = QLabel("Digite um valor entre 0 e 10", self)
        self.lbd_Value = QLineEdit(self)
        self.lbd_Value.setValidator(QIntValidator())

        self.button_Entrar = QPushButton("Confirmar", self)
        self.button_Entrar.clicked.connect(self.Adding)

        self.lbl_Valitor = QLabel(self)


        self.layout_Frame.addSpacing(300)
        self.layout_Frame.addWidget(self.lbl_Titulo)
        self.layout_Frame.addWidget(self.lbl_Value)
        self.layout_Frame.addWidget(self.lbd_Value)
        self.layout_Frame.addWidget(self.button_Entrar)
        self.layout_Frame.addWidget(self.lbl_Valitor)
        self.layout_Frame.addSpacing(300)


    def Adding(self):
        __value = int(self.lbd_Value.text())
        if __value >= 0 and __value <= 10:
            if __value == 7:
                self.lbl_Valitor.setText(f"O valor está correto!!")
            else:
                self.lbl_Valitor.setText(f"O valor {__value} entra porém é o valor errado tente novamente...")
        else:
            self.lbl_Valitor.setText(f"O valor está fora dos padroes")


if __name__ == "__main__":
    import sys
    App = QApplication(sys.argv)
    Janela = MainWindow()
    Janela.show()
    App.exec()