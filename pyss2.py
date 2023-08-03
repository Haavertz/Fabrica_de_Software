from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QLabel
from PyQt5.QtCore import Qt
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exercicio - 1")
        self.setFixedSize(600,400)
        self.lbl = QLabel("Hello World")
        font = self.lbl.font()
        font.setPointSize(20)
        self.lbl.setFont(font)
        self.setCentralWidget(self.lbl)


app = QApplication(sys.argv)
janela = MainWindow()
janela.show()
app.exec()