from PyQt5 import uic
from PyQt5.QtWidgets import QApplication,QWidget
import sys

if __name__ == '__main__':

    mainapp = QApplication(sys.argv)

    dataViewWideget = uic.loadUi("UI/DataViewWidget.ui")
    dataViewWideget.show()
    sys.exit(mainapp.exec())

