from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QFrame, QVBoxLayout
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Imagem")
        self.setFixedSize(500,500)

        self.frame = QFrame(self)
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setGeometry(100,100,300,300)

        self.image_lbl = QLabel(self.frame)
        self.image_lbl.setPixmap(QPixmap("images.jpg"))
        self.image_lbl.setScaledContents(True)








app = QApplication(sys.argv)
janela = MainWindow()
janela.show()
app.exec()