from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit
from PyQt5.QtCore import QSize, Qt 
from PyQt5.QtGui import QPalette, QColor
import sys

class MainWindow2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Color - 004")
        self.initUI2()  # Chamando o método para inicializar a interface

    def initUI2(self):
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(51, 51, 51))  # Definindo a cor de fundo da janela
        palette.setColor(QPalette.WindowText, QColor(250, 250, 250))  # Definindo a cor do texto na janela
        self.setPalette(palette)  # Aplicando a paleta de cores à janela


app = QApplication(sys.argv)  # Criando uma instância da aplicação
janela = MainWindow2()  # Criando uma instância da janela personalizada
janela.show()  # Exibindo a janela
app.exec() # Iniciando o loop de eventos da aplicação e saindo corretamente no encerramento