from PyQt5.QtWidgets import QApplication,QWidget,QMainWindow
import sys

def do():
    print(111)

class MainWin(QMainWindow,ui):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

if __name__ == '__main__':

    mainApp = QApplication(sys.argv)

    view = MainWin()
    view.show()

    sys.exit(mainApp.exec())

