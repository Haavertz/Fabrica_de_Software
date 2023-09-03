from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QFrame
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(800,600)
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("Poketex")
        
        self.button_pikachu = QPushButton('Cat')
        self.button_caramelo = QPushButton('Dog')
        
        self.image_frame = QFrame(self)
        self.image_frame.setFrameShape(QFrame.Box)
        self.image_frame.setFixedSize(600,400)
        self.image_frame.setLayout(QVBoxLayout())
        
        self.image_label = QLabel(self.image_frame)
        self.image_label.setAlignment(Qt.AlignCenter)
        # self.image_label.setScaledContents(True)
        
        layout = QVBoxLayout()
        layout.addWidget(self.button_pikachu)
        layout.addWidget(self.button_caramelo)

        
        self.button_pikachu.clicked.connect(self.display_pikachu)
        self.button_caramelo.clicked.connect(self.display_caramelo)
        
        self.setLayout(layout)
    
    def display_pikachu(self):
        pixmap = QPixmap('Catjpg.jpg')
        self.image(pixmap)
    
    def display_caramelo(self):
        pixmap = QPixmap('images.jpg')
        self.image(pixmap)
        
    def image(self):
        self.image_label.setScaledContents(True)
        self.image_label.setPixmap(QPixmap("Catjpg.jpg"))
        
       
        
    

app = QApplication(sys.argv)
janela = MainWindow()
janela.show()
app.exec()