import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def init_text(self):
        message_first = "This application's aim is show some charts and something else" \
                  "\nPress the button and display what you want"
        message_GitHub = "1. Show the best projects in Python language from GitHub"
        text_1 = QLabel(message_first, self)
        text_1.move(200, 0)
        text_1.setFont(QFont("Times", 15))

        text_2 = QLabel(message_GitHub, self)
        text_2.move(0,100)
        text_2.setFont(QFont("Times", 10))

    def init_buttons(self):
        button_1 = QPushButton("GitHub", self)
        button_1.resize(button_1.sizeHint())
        button_1.move(420, 97)

    def initUI(self):
        #self.setGeometry(300, 300, 1000, 600)
        self.setWindowTitle("DisplayFiguresAndMaps")
        self.init_text()
        self.init_buttons()


        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.setFixedSize(1000, 600)
    sys.exit(app.exec_())

