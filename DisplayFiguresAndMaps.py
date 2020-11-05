import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication , QMainWindow, QWidget, QLabel, QGridLayout
from StatisticsFromGitHub import GitHubCharts
from EarthQuakesMap import EarthQuakes

class EarthQuakesView(QWidget):
    """Window settings where user can select period of earthquakes on the map"""
    def __init__(self, parent=None):
        """Settings initializations"""
        super(EarthQuakesView, self).__init__(parent)

        #Text settings
        self.message_first = "Which period do you want to show?"
        self.text_1 = QLabel(self)
        self.text_1.setText(self.message_first)
        self.text_1.move(290, 0)
        self.text_1.setFont(QtGui.QFont("Times", 15))
        self.text_1.resize(self.text_1.sizeHint())

        #Buttons generate
        self.button_1 = QtWidgets.QPushButton(self)
        self.button_1.setText("Last hour")
        self.button_2 = QtWidgets.QPushButton(self)
        self.button_2.setText("Today")
        self.button_3 = QtWidgets.QPushButton(self)
        self.button_3.setText("Last week")
        self.button_4 = QtWidgets.QPushButton(self)
        self.button_4.setText("Last month")
        self.button_5 = QtWidgets.QPushButton(self)
        self.button_5.setText("Back")

        #Buttons layout
        scheme = QGridLayout()

        scheme.addWidget(self.button_1)
        scheme.addWidget(self.button_2)
        scheme.addWidget(self.button_3)
        scheme.addWidget(self.button_4)
        scheme.addWidget(self.button_5)

        self.setLayout(scheme)

class LanguagesView(QWidget):
    """Window settings where user can select a language to view its graph"""
    def __init__(self, parent=None):
        """Settings initializations"""
        super(LanguagesView, self).__init__(parent)

        #Text settings
        message_first = "Which language do you want to show?"
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
        scheme = QGridLayout()

        scheme.addWidget(self.button_1, 1, 0)
        scheme.addWidget(self.button_2, 1, 1)
        scheme.addWidget(self.button_3, 2, 0)
        scheme.addWidget(self.button_4, 2, 1)
        scheme.addWidget(self.button_5, 3, 0)
        scheme.addWidget(self.button_6, 3, 1)
        scheme.addWidget(self.button_7, 4, 0)
        scheme.addWidget(self.button_8, 4, 1)
        scheme.addWidget(self.button_9, 5, 0, 1, 2)

        self.setLayout(scheme)

class FirstMenu(QWidget):
    """First window settings"""
    def __init__(self, parent=None):
        """Settings initialization"""
        super(FirstMenu, self).__init__(parent)
        message_first = "This application's aim is show some charts and something else" \
                        "\nPress the button and display what you want"
        message_GitHub = "1. Press button 'GitHub' to show the best projects in diffrent languages from GitHub:"
        message_temperature = "2. Press buttton 'Earthquakes' to show map with earthquakes:"
        self.text_1 = QLabel(self)
        self.text_1.setText(message_first)
        self.text_1.move(200, 0)
        self.text_1.setFont(QtGui.QFont("Times", 15))

        self.text_2 = QtWidgets.QLabel(self)
        self.text_2.setText(message_GitHub)
        self.text_2.move(0, 100)
        self.text_2.setFont(QtGui.QFont("Times", 10))

        self.text_3 = QtWidgets.QLabel(self)
        self.text_3.setText(message_temperature)
        self.text_3.move(0, 200)
        self.text_3.setFont(QtGui.QFont("Times", 10))

        self.button_github = QtWidgets.QPushButton(self)
        self.button_github.setText("GitHub")
        self.button_github.move(600, 95)

        self.button_earthquake = QtWidgets.QPushButton(self)
        self.button_earthquake.setText("Earthquakes")
        self.button_earthquake.move(430, 195)

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
        self.first = FirstMenu(self)
        self.setCentralWidget(self.first)
        self.first.button_github.clicked.connect(self.clicked_Git_Hub)
        self.first.button_earthquake.clicked.connect(self.clicked_earthquakes)
        self.show()

    def clicked_Git_Hub(self):
        """Go to window where user can select which language statistics wants to see"""
        self.language = LanguagesView()
        self.setCentralWidget(self.language)
        self.language.button_1.clicked.connect(self.clicked_python)
        self.language.button_2.clicked.connect(self.clicked_c)
        self.language.button_3.clicked.connect(self.clicked_cpp)
        self.language.button_4.clicked.connect(self.clicked_c_sharp)
        self.language.button_5.clicked.connect(self.clicked_java)
        self.language.button_6.clicked.connect(self.clicked_java_script)
        self.language.button_7.clicked.connect(self.clicked_php)
        self.language.button_8.clicked.connect(self.clicked_sql)
        self.language.button_9.clicked.connect(self.clicked_back)
        self.show()

    def clicked_python(self):
        python_chart = GitHubCharts('python')

    def clicked_c(self):
        c_chart = GitHubCharts('c')

    def clicked_cpp(self):
        cpp_chart = GitHubCharts('cpp')

    def clicked_c_sharp(self):
        c_sharp_chart = GitHubCharts('c#')

    def clicked_java(self):
        java_chart = GitHubCharts('java')

    def clicked_java_script(self):
        java_script_chart = GitHubCharts('javascript')

    def clicked_php(self):
        php_chart = GitHubCharts('php')

    def clicked_sql(self):
        sql_chart = GitHubCharts('sql')

    def clicked_back(self):
        self.startUI()

    def clicked_earthquakes(self):
        self.earthquake = EarthQuakesView()
        self.setCentralWidget(self.earthquake)
        self.earthquake.button_1.clicked.connect(self.clicked_hour)
        self.earthquake.button_2.clicked.connect(self.clicked_today)
        self.earthquake.button_3.clicked.connect(self.clicked_week)
        self.earthquake.button_4.clicked.connect(self.clicked_month)
        self.earthquake.button_5.clicked.connect(self.clicked_back)
        self.show()

    def clicked_hour(self):
        hour = EarthQuakes('all_hour')

    def clicked_today(self):
        today = EarthQuakes('all_day')

    def clicked_week(self):
        week = EarthQuakes('all_week')

    def clicked_month(self):
        month = EarthQuakes('all_month')

if __name__ == '__main__':
    """Start the application"""
    app = QApplication(sys.argv)
    window = MainWindow()

    sys.exit(app.exec_())

