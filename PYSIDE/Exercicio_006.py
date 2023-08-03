from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QLabel
from PyQt5.QtCore import Qt, QSize
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exercicio_006")
        self.setFixedSize(QSize(600,400))
        self.lbl = QLabel("Hello Word")
        font = self.lbl.font()
        font.setPointSize(20)
        self.lbl.setFont(font)
        self.lbl.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.setCentralWidget(self.lbl)
        
        




App = QApplication(sys.argv)
janela = MainWindow()
janela.show()
App.exec()