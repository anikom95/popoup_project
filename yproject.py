from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QTimer, QUrl, QDir
from PyQt5.QtMultimedia import QSound
import sys
from random import randint

class PopupWindow(QMainWindow):
    width = 370
    height = 300

    def __init__(self):
        super(PopupWindow, self).__init__()
        self.screenWidth = QApplication.desktop().availableGeometry().width() 
        self.screenHeight = QApplication.desktop().availableGeometry().height() 
        self.initUI()


    def initUI(self):
        self.PopupWindow = []

        self.setGeometry((self.screenWidth-370),(self.screenHeight-300),370,300)
        self.sound = QSound("sounds/girl.wav")
        self.setWindowTitle('Wanna meet horny women?')

        self.button = QPushButton("Show me more", self)
        self.button.clicked.connect(self.buttonPressed)
        self.button.setGeometry(30,230,120,50)
        self.button.setObjectName("button")

        self.but1 = QPushButton("", self)
        self.but1.clicked.connect(self.tryClose)
        self.but1.setGeometry(305,0,20,20)
        self.but1.setObjectName("but1")

        self.but2 = QPushButton("", self)
        self.but2.clicked.connect(self.tryClose)
        self.but2.setGeometry(325,0,20,20)
        self.but2.setObjectName("but2")

        self.but3 = QPushButton("", self)
        self.but3.clicked.connect(self.tryClose)
        self.but3.setGeometry(345, 0, 20, 20)
        self.but3.setObjectName("but3")
        self.show()
    
    def buttonPressed(self):
        self.sound.play()
        self.sound.setLoops(20)

    def scatter(self):
        for win in self.PopupWindow:
            win.move(randint(50, self.width + 400), randint(1, self.height + 200))


    def tryClose(self):
        for i in range(1):
            newwin = PopupWindow()
            newwin.setVisible(True)
            self.PopupWindow.append(newwin)
        self.scatter()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet("""
            QPushButton#button {
                background-color: red;
                color: white;
                font-style: bold;
                font-size: 17px
            }
            QPushButton#button:pressed { 
                color: black; 
            }
            QPushButton#but1 {
                border-image: url("images/but1.jpg");
            }
            QPushButton#but2 {
                border-image: url("images/but2.jpg");
            }
            QPushButton#but3 {
                border-image: url("images/but3.jpg");
            } 
             QMainWindow {
                background-image: url("images/test.jpg");
                background-repeat: no-repeat;
            }
        """)
    win = PopupWindow() 
    win.show()
sys.exit(app.exec_())

