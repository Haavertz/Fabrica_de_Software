import shutil
import sys
import os
from PySide6.QtWidgets import *
from PySide6.QtGui import QIcon
from untitled_ui import *


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Organizando Arquivo.")
        AppIcon = QIcon("image-removebg-preview.png")
        self.setWindowIcon(AppIcon)
        self.lbd_Button2.clicked.connect(self.open_path)
        self.Lbd_Button.clicked.connect(self.organize)
        
    def open_path(self):
        self.path = QFileDialog.getExistingDirectory(self,str('Arquivo com pasta'), '/Home', 
        QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks)
        self.Lbd_Button.setText(self.path)
        self.path = str(self.path)
  
        
App = QApplication(sys.argv)
Jn = MainWindow()
Jn.show()
App.exec()