import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication , QMainWindow, QWidget, QLabel, QGridLayout

class LanguagesView(QWidget):
    """Window settings where user can select a language to view its graph"""
    def __init__(self, parent=None):
        """Settings initializations"""
        super(LanguagesView, self).__init__(parent)

        #Texts settings
        message_first = "Which language do you want to search?"
        self.text_1 = QLabel(self)
        self.text_1.setText(message_first)
        self.text_1.move(290, 0)
        self.text_1.setFont(QtGui.QFont("Times", 15))
        self.text_1.resize(self.text_1.sizeHint())

        #Buttons generate
        self.button_1 = QtWidgets.QPushButton(self)
        self.button_1.setText("Python")
        self.button_2 = QtWidgets.QPushButton(self)
        self.button_2.setText("C")
        self.button_3 = QtWidgets.QPushButton(self)
        self.button_3.setText("C++")
        self.button_4 = QtWidgets.QPushButton(self)
        self.button_4.setText("C#")
        self.button_5 = QtWidgets.QPushButton(self)
        self.button_5.setText("Java")
        self.button_6 = QtWidgets.QPushButton(self)
        self.button_6.setText("JavaScript")
        self.button_7 = QtWidgets.QPushButton(self)
        self.button_7.setText("PHP")
        self.button_8 = QtWidgets.QPushButton(self)
        self.button_8.setText("SQL")
        self.button_9 = QtWidgets.QPushButton(self)
        self.button_9.setText("Back")

        #Buttons layout settings
        ukladT = QGridLayout()

        ukladT.addWidget(self.button_1, 1, 0)
        ukladT.addWidget(self.button_2, 1, 1)
        ukladT.addWidget(self.button_3, 2, 0)
        ukladT.addWidget(self.button_4, 2, 1)
        ukladT.addWidget(self.button_5, 3, 0)
        ukladT.addWidget(self.button_6, 3, 1)
        ukladT.addWidget(self.button_7, 4, 0)
        ukladT.addWidget(self.button_8, 4, 1)
        ukladT.addWidget(self.button_9, 5, 0, 1, 2)

        self.setLayout(ukladT)

class FirstMenu(QWidget):
    """First window settings"""
    def __init__(self, parent=None):
        """Settings initialization"""
        super(FirstMenu, self).__init__(parent)
        message_first = "This application's aim is show some charts and something else" \
                        "\nPress the button and display what you want"
        message_GitHub = "1. Press button 'GitHub' to show the best projects in diffrent languages from GitHub:"
        self.text_1 = QLabel(self)
        self.text_1.setText(message_first)
        self.text_1.move(200, 0)
        self.text_1.setFont(QtGui.QFont("Times", 15))

        self.text_2 = QtWidgets.QLabel(self)
        self.text_2.setText(message_GitHub)
        self.text_2.move(0, 100)
        self.text_2.setFont(QtGui.QFont("Times", 10))

        self.button = QtWidgets.QPushButton(self)
        self.button.setText("GitHub")
        self.button.move(600, 95)

class MainWindow(QMainWindow):
    """Application window settings"""
    def __init__(self, parent=None):
        """Settings initialization"""
        super(MainWindow, self).__init__(parent)
        self.setGeometry(300, 300, 300, 300)
        self.setFixedSize(1000, 600)
        self.setWindowTitle("DisplayFiguresAndMaps")
        self.startUI()

    def startUI(self):
        """Display first window in application"""
        self.nowy = FirstMenu(self)
        self.setCentralWidget(self.nowy)
        self.nowy.button.clicked.connect(self.clicked_Git_Hub)
        self.show()

    def clicked_Git_Hub(self):
        """Go to window where user can select which language statistics wants to see"""
        self.nowy2 = LanguagesView()
        self.setCentralWidget(self.nowy2)
        self.show()

if __name__ == '__main__':
    """Start the application"""
    app = QApplication(sys.argv)
    window = MainWindow()

    sys.exit(app.exec_())

