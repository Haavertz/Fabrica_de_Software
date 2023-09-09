from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QCheckBox, QVBoxLayout, QWidget
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exercicio - 11")
        self.Qlabel = QLabel("Clique e aceite.")
        self.ck = QCheckBox("Aceito")
        
        layout = QVBoxLayout()
        layout.addWidget(self.Qlabel)
        layout.addWidget(self.ck)
        layout.addWidget(self.Qlabel)
        
        container = QWidget()
        container.setLayout(layout)
        
        self.setCentralWidget(container)
    

App = QApplication(sys.argv)
Janela = MainWindow()
Janela.show()
App.exec()