# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QVBoxLayout,
    QWidget)
import d_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(802, 607)
        MainWindow.setStyleSheet(u"background-color: rgb(255, 0, 0);\n"
"background-color: rgb(0, 255, 127);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbd_Button2 = QPushButton(self.frame_2)
        self.lbd_Button2.setObjectName(u"lbd_Button2")
        self.lbd_Button2.setStyleSheet(u"background-color: rgb(85, 255, 255);")

        self.verticalLayout.addWidget(self.lbd_Button2)

        self.lbl_Login = QLabel(self.frame_2)
        self.lbl_Login.setObjectName(u"lbl_Login")

        self.verticalLayout.addWidget(self.lbl_Login, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.Spacer_ = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.Spacer_)

        self.Lbd_Line = QLineEdit(self.frame_2)
        self.Lbd_Line.setObjectName(u"Lbd_Line")
        self.Lbd_Line.setStyleSheet(u"background-color: rgb(3, 230, 255);")

        self.verticalLayout.addWidget(self.Lbd_Line)

        self.line = QFrame(self.frame_2)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line, 0, Qt.AlignHCenter)

        self.Spacer_1 = QSpacerItem(5, 12, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.Spacer_1)

        self.Lbd_Button = QPushButton(self.frame_2)
        self.Lbd_Button.setObjectName(u"Lbd_Button")
        self.Lbd_Button.setCursor(QCursor(Qt.UpArrowCursor))
        self.Lbd_Button.setStyleSheet(u"background-color: rgb(0, 255, 255);")

        self.verticalLayout.addWidget(self.Lbd_Button)


        self.horizontalLayout_2.addWidget(self.frame_2)


        self.verticalLayout_2.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 802, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/dasdas/d.qrc\"/><img src=\":/dasdas/d.qrc\"/><img src=\":/newPrefix/image-removebg-preview.png\"/></p></body></html>", None))
        self.lbd_Button2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.lbl_Login.setText(QCoreApplication.translate("MainWindow", u"My project", None))
        self.Lbd_Line.setPlaceholderText(QCoreApplication.translate("MainWindow", u"FAZUELI", None))
        self.Lbd_Button.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
    # retranslateUi
    
    

import sys
App = QApplication(sys.argv)
Janela = QMainWindow()
w = Ui_MainWindow()
w.setupUi(Janela)
Janela.show()
App.exec()