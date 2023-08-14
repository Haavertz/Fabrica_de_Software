from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit
from PyQt5.QtCore import QSize, Qt 
from PyQt5.QtGui import QPalette, QColor
import sys

class MainWindow2(QMainWindow):
    def __inti__(self):
        super().__init__()
        self.setWindowTitle("Color - 004")
        self.Inicio()
        
    def Inicio(self):
        palete = QPalette()
        palete.setColor(QPalette.janela, QColor(51,51,51))
        palete.setColor(QPalette.windowText, QColor(250, 250, 250))
        App.setPalette(palete)
        

if __name__ == "__main__":    
    App = QApplication(sys.argv)
    janela = MainWindow2()
    janela.show()
    App.exec()