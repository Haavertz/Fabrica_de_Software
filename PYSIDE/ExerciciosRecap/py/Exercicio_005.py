from PyQt5.QtWidgets import QApplication, QLineEdit, QMainWindow, QCheckBox, QPushButton, QLabel, QFont
import brazilcep
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.Init()  # Inicialização da interface ao criar a instância da classe
        
    def Init(self):
        self.setWindowTitle("Busque Cep")  # Definindo o título da janela
        self.setFixedSize(700, 400)  # Definindo o tamanho fixo da janela
        self.Edit()  # Chama o método para configurar os elementos de edição (interface)

    def Edit(self):
        self.Title = QLabel("BEM VINDO AO CEP", self)  # Criando um rótulo de texto
        self.Title.setGeometry(100, 0, 50, 50)  # Definindo a posição e tamanho do rótulo

# Inicialização da aplicação
App = QApplication(sys.argv)  # Criando uma instância da aplicação
Janela = MainWindow()  # Criando uma instância da classe MainWindow (janela personalizada)
Janela.show()  # Exibindo a janela
App.exec()  # Iniciando o loop de eventos da aplicação