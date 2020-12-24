import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QTabWidget,QWidget,QMessageBox,QHBoxLayout,QPushButton
from PyQt5.QtSql import QSqlDatabase
from PyQt5.QtGui import QPalette,QPixmap,QBrush



class MainWindow(QMainWindow):


    def createDB(self):
        if self.DB:
            return
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

    def paintEvent(self, e):
        pix = self.backgroundPicture.scaled(self.Width(),self.Height())
        palette = QPalette(self)
        palette.setBrush(self.backgroundRole(),pix)
        self.setPalette(palette)
        super().paintEvent(e)

if __name__ == '__main__':
    mainApp = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(mainApp.exec_())

