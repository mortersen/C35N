from PyQt5 import uic
from PyQt5.QtWidgets import QApplication,QWidget
import sys

def do():
    print(111)

if __name__ == '__main__':

    mainApp = QApplication(sys.argv)

    dataViewWideget = uic.loadUi("UI/C35NMainWindows.ui")

    dataViewWideget.show()
    sys.exit(mainApp.exec())

