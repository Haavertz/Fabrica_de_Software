from PySide6.QtWidgets import (
    QApplication, QMainWindow, QFormLayout, QWidget, QLabel,
    QRadioButton, QCheckBox, QLineEdit, QSpinBox, QDoubleSpinBox,
    QPushButton, QComboBox, QFontComboBox, QDateEdit, QDateTimeEdit,
    QLCDNumber, QProgressBar, QDial, QSlider)
from PySide6.QtCore import Qt

import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Criação de um layout de formulário
        formulario = QFormLayout()

        # Adicionando componentes ao layout
        formulario.addRow(QCheckBox('Checkbox'))  # Caixa de seleção
        formulario.addRow(QRadioButton('Radio Button'))  # Botão de opção
        formulario.addRow("QLabel", QLabel("QLabel"))  # Rótulo de texto
        formulario.addRow("QPushButton", QPushButton("QPushButton"))  # Botão
        formulario.addRow("QLineEdit", QLineEdit("QLineEdit"))  # Campo de entrada de texto
        formulario.addRow("QDateEdit", QDateEdit())  # Campo de edição de data
        formulario.addRow("QDateTimeEdit", QDateTimeEdit())  # Campo de edição de data e hora
        formulario.addRow("QSpinBox", QSpinBox())  # Caixa de seleção de número inteiro
        formulario.addRow("QDoubleSpinBox", QDoubleSpinBox())  # Caixa de seleção de número decimal
        formulario.addRow("QComboBox", QComboBox())  # Caixa de combinação (lista suspensa)
        formulario.addRow("QFontComboBox", QFontComboBox())  # Caixa de combinação de fontes
        formulario.addRow("QProgressBar", QProgressBar())  # Barra de progresso
        formulario.addRow("QLCDNumber", QLCDNumber())  # Display de sete segmentos (números)
        formulario.addRow("QSlider", QSlider(Qt.Horizontal))  # Controle deslizante horizontal
        formulario.addRow("QDial", QDial())  # Controle de discagem

        # Criação de um widget e definindo o layout como o layout de formulário
        widget = QWidget()
        widget.setLayout(formulario)

        # Definindo o widget central da janela principal
        self.setCentralWidget(widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    window = MainWindow()
    window.show()
    app.exec()