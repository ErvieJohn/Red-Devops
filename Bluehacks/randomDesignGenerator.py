import sys, random
from PyQt5.QtWidgets import QMainWindow, QLabel
from PyQt5.QtWidgets import QGridLayout, QWidget, QDesktopWidget
from PyQt5.QtWidgets import (QApplication, QPushButton, QLabel, QFileDialog)

from PyQt5 import QtGui, QtCore, Qt
from PyQt5.Qt import *
from PyQt5.QtCore import QRect, Qt, QTimer

from PyQt5.QtGui import QPainter, QBrush, QPen
 
from PyQt5.QtCore import Qt

from PyQt5.QtGui import QPixmap

class randomPattern(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "Random Wanno Generator"
        self.left = 500
        self.top = 100
        self.width = 900
        self.height = 900
        self.flag = False

        self.design1 = QLabel(self)
        self.design2 = QLabel(self)
        self.design3 = QLabel(self)
        self.design4 = QLabel(self)
        self.design5 = QLabel(self)
        self.design6 = QLabel(self)
        self.design7 = QLabel(self)

        self.initWindow()

    def initWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        self.button()
        self.show()

    def button(self):
        generateButton = QPushButton("Generate", self)
        generateButton.setGeometry(QRect(350+50, 750, 200, 70))
        generateButton.setFont(QtGui.QFont('Times New Roman',19))
        generateButton.clicked.connect(self.clickedGenerate)

        takeSsButton = QPushButton("Save", self)
        takeSsButton.setGeometry(QRect(350-150, 750, 200, 70))
        takeSsButton.setFont(QtGui.QFont('Times New Roman',19))
        takeSsButton.clicked.connect(self.save_screenshot)

    def clickedGenerate(self):
        self.design1.hide()
        self.design2.hide()
        self.design3.hide()
        self.design4.hide()
        self.design5.hide()
        self.design6.hide()
        self.design7.hide()

        self.flag = True
        self.update()

    def paintEvent(self, e):
        if self.flag:
            patterns = ["design1.png", "design2.png", "design3.png", "design4.png", "design5.png", "design6.png", "design7.png", "design8.png",
            "design9.png", "design10.png", "design11.png", "design12.png", "design13.png", "design14.png", "design15.png", "design16.png", "design17.png",
            "design18.png", "design19.png", "design20.png"]
            
            #print(patterns[randPatterns])
            #print(randPatterns)

            painter = QPainter()
            painter.begin(self)
            painter.setPen(QPen(Qt.black, 5, Qt.SolidLine))
            painter.setBrush(QColor(0,0,0))

            for i in range(8):
                painter.drawRect(0, 30+(i*100)+5, 700+195, 3)

            for i in range(7):
                randPatterns = random.randrange(0,20)
                
                if i == 0:
                    
                    self.design1.setPixmap(QPixmap("Designs/{}".format(patterns[randPatterns])))
                    
                    self.design1.setGeometry(0, 30+(i*100)+5+3, 900, 100-3)
                    self.design1.show()
                elif i == 1:
                    
                    self.design2.setPixmap(QPixmap("Designs/{}".format(patterns[randPatterns])))
                    
                    self.design2.setGeometry(0, 30+(i*100)+5+3, 900, 100-3)
                    self.design2.show()

                elif i == 2:
                    
                    self.design3.setPixmap(QPixmap("Designs/{}".format(patterns[randPatterns])))
                    
                    self.design3.setGeometry(0, 30+(i*100)+5+3, 900, 100-3)
                    self.design3.show()

                elif i == 3:
                    
                    self.design4.setPixmap(QPixmap("Designs/{}".format(patterns[randPatterns])))
                    
                    self.design4.setGeometry(0, 30+(i*100)+5+3, 900, 100-3)
                    self.design4.show()
                elif i == 4:
                    
                    self.design5.setPixmap(QPixmap("Designs/{}".format(patterns[randPatterns])))
                    
                    self.design5.setGeometry(0, 30+(i*100)+5+3, 900, 100-3)
                    self.design5.show()

                elif i == 5:
                    
                    self.design6.setPixmap(QPixmap("Designs/{}".format(patterns[randPatterns])))
                    
                    self.design6.setGeometry(0, 30+(i*100)+5+3, 900, 100-3)
                    self.design6.show()
                
                elif i == 6:
                    
                    self.design7.setPixmap(QPixmap("Designs/{}".format(patterns[randPatterns])))
                    
                    self.design7.setGeometry(0, 30+(i*100)+5+3, 900, 100-3)
                    self.design7.show()

            self.flag = False
            painter.end()

    def save_screenshot(self):
        #QTimer.singleShot(1000, self.take_screenshot)
        self.take_screenshot()
        img, _ = QFileDialog.getSaveFileName(self,"Salvar Arquivo",
                                            filter="PNG(*.png);; JPEG(*.jpg)")
        if img[-3:] == "png":
            self.preview_screen.save(img, "png")
        elif img[-3:] == "jpg":
            self.preview_screen.save(img, "jpg")
        
    def take_screenshot(self):
        x = 500
        y = 30+100+5+3
        width = 900
        height = 100*7
        self.preview_screen = QApplication.primaryScreen().grabWindow(QApplication.desktop().winId(), x, y, width, height)
        
    def closeEvent(self, event):
        close = QMessageBox.question(self,
                                     "Exit the program",
                                     "Are you sure?",
                                      QMessageBox.Yes | QMessageBox.No)
        if close == QMessageBox.Yes:
            event.accept()
            sys.exit(0)
        else:
            event.ignore()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = randomPattern()
    sys.exit(app.exec_())
