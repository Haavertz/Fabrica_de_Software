from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QAction
from PyQt5.QtCore import QSize, Qt 
import sys
import brazilcep

# Definição da classe da janela principal
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Busca CEP")  # Definindo o título da janela

# Solicitação de informações do CEP usando a biblioteca 'brazilcep'
endereco = brazilcep.get_address_from_cep("79097010")
print(endereco)  # Exibindo as informações do endereço

# Inicialização da aplicação
App = QApplication(sys.argv)  # Criando uma instância da aplicação
janela = MainWindow()  # Criando uma instância da classe MainWindow (janela personalizada)
janela.show()  # Exibindo a janela
App.exec()  # Iniciando o loop de eventos da aplicação
