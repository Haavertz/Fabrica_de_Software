from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit
from PyQt5.QtCore import QSize, Qt 
import sys

#self. - para buscar dentro da QMainWindow (buscando localmente) 
#set - serve setar algo na tela, exemplo seria, setWindowTitle que serve para setar um titulo no programa.
#super().__init__() - serve para buscar da classe super class, ou seja, herda da funcao pai.
#.show() - serve para deixar a janela secundaria aberta.
#.app.exec() - serve para deixar a janela principál aberta. 

class MainWindow(QMainWindow):
    def __init__ (self):
        super().__init__()
        self.Main()
        
    def Main(self):
        
        self.setWindowTitle("Recapitulando - 1") #Titulo do programa
        self.setFixedSize(QSize(600,600)) #Deixando a tela fixa em 600 por 600 px
        
        self.label = QLabel("Hello Word!", self) #Colocamos um self para buscar esse titulo
        font1 = self.label.font() #Aqui estou criando uma variavel que está recebendo minha QLabel chamada Label (que seria meu titulo) e colocando uma font nela
        font1.setPointSize(30) #Após colocarmos o hello Word em uma variavel setaremos que ele receba uma font do tamanho 25(*opcional)
        self.label.setFont(font1) #Aqui iremos puxar a nossa QLabel(titulo) e usaremos a font que fizemos antes para colocar na label ou seja, setFont (setamos uma font nela)
        self.label.setGeometry(200,0,600,100) #Por fim utilizaremos o setGeometry para setar a posicao da self.label (Titulo) lembrando que usamos self. para pergamos algo local e passamos os valores (x, y, (tamanho x), (tamanho y))

        self.Nomes = QLabel("Name: ", self)
        font2 = self.Nomes.font() 
        font2.setPointSize(10)
        self.Nomes.setFont(font2)
        self.Nomes.setGeometry(10,150,50,30)
        
        #Quadrado para digitar
        
        self.NomesQ = QLineEdit(self) #Com o QLineEdit consigo criar um quadrado para digitar, assim como um valor.
        one = int(self.NomesQ.setText())
        self.NomesQ.setGeometry(50,152,90,30)
        
    def Soma(self):
        pass
        
        
app = QApplication(sys.argv) #Tela princial (sys.argv eu n lembro pra que serve)
janela = MainWindow()
janela.show()
app.exec()
        