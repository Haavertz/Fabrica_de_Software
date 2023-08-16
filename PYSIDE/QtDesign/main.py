from arquivo_ui import Ui_MainWindow, QApplication, QMainWindow


class Main(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Tela Login")

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    w = Main()
    w.show()
    app.exec()