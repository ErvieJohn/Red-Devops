import sys
from PyQt5.QtWidgets import QMainWindow, QLabel
from PyQt5.QtWidgets import QGridLayout, QWidget, QDesktopWidget
from PyQt5.QtWidgets import (QApplication, QPushButton, QLabel)

from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import QRect

from PyQt5.QtGui import QPixmap

class ifugaoDesign(QMainWindow):
    def __init__(self):
            super().__init__()

            self.title = ""
            self.width = 1000
            self.height = 1000
            font = QtGui.QFont()
            font.setFamily("Palatino Linotype")
            font.setPointSize(12)
            font.setBold(False)
            font.setWeight(50)
            self.label.setFont(font)
            self.label.setStyleSheet("background-color: transparent;")
            self.label.setObjectName("label")
            self.initWindow()

    def initWindow(self):
        self.resize(self.width, self.height)
        self.center()
        self.setWindowTitle(self.title)

        self.backgroundWin()
        self.show()

    def center(self):
        # geometry of the main window
        qr = self.frameGeometry()

        # center point of screen
        cp = QDesktopWidget().availableGeometry().center()

        # move rectangle's center point to screen's center point
        qr.moveCenter(cp)

        # top left of rectangle becomes top left of window centering it
        self.move(qr.topLeft())

    def backgroundWin(self):
        self.background = QLabel(self)
        #self.background.setPixmap(QPixmap('Backgrounds/Cultural Background.jpg'))
        self.background.setGeometry(0, 0, self.width, self.height)#size and position of background

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = ifugaoDesign()
    sys.exit(app.exec_())
