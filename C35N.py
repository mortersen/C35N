import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QTabWidget,QWidget

from UI.MainWindow import Ui_MainWindow
from UI.IndexWidget import Ui_Index

class TabIndex(QWidget,Ui_Index):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.tabWidget.addTab(TabIndex(),"起始页")


if __name__ == '__main__':
    mainApp = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(mainApp.exec_())

