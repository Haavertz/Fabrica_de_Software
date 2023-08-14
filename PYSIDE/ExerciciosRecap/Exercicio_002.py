from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QAction
from PyQt5.QtCore import QSize, Qt 
import sys
import brazilcep


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Busca CEP")
        
endereco = brazilcep.get_address_from_cep("79097010")
print(endereco)
    


App = QApplication(sys.argv)
janela = MainWindow()
janela.show()
App.exec()