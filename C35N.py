import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QTabWidget,QWidget,QMessageBox
from PyQt5.QtSql import QSqlDatabase

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
        self.createDB()

    def createDB(self):
        try:
            self.DB = QSqlDatabase.addDatabase("QSQLITE")
            self.DB.setDatabaseName("DB/C35N.db3")
            if self.DB.open():
                QMessageBox.information(self,"提示","成功链接数据库")
            else:
                QMessageBox.warning(self,"错误","数据库打开失败")
        except Exception as e:
            QMessageBox.critical(self,"错误","数据库驱动错误")
            print(e)

if __name__ == '__main__':
    mainApp = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(mainApp.exec_())

