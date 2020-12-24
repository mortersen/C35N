import sys
from PyQt5.QtWidgets import (
    QApplication,QMainWindow,QTabWidget,QWidget,QMessageBox,QHBoxLayout,QPushButton,
    QLabel,
)
from PyQt5.QtSql import QSqlDatabase
from PyQt5.QtGui import QPalette,QPixmap,QBrush,QPainter

from UI.UI_MainWindow import Ui_mainWindow
from UI.UI_ComicBook import Ui_comicBook
import img_rc

class ComicBook(QWidget,Ui_comicBook):
    def __init__(self):
        super().__init__()
        self.ui = Ui_comicBook()
        self.ui.setupUi(self)

        #载入连环画
        self.picPath=[":/Icon/KJZ-C35N-1.png",":/Icon/KJZ-C35N-2.png",":/Icon/KJZ-C35N-3.png",
                      ":/Icon/KJZ-C35N-4.png",":/Icon/KJZ-C35N-5.png",":/Icon/KJZ-C35N-6.png",
                      ":/Icon/KJZ-C35N-7.png",":/Icon/KJZ-C35N-8.png",":/Icon/KJZ-C35N-9.png",
                      ":/Icon/KJZ-C35N-10.png",":/Icon/KJZ-C35N-11.png",":/Icon/KJZ-C35N-12.png",
                      ":/Icon/KJZ-C35N-13.png",":/Icon/KJZ-C35N-14.png",":/Icon/KJZ-C35N-15.png",
                      ":/Icon/KJZ-C35N-16.png"]
        self.currentPic = 0
        self.ui.btn_PagePre.released.connect(self.prePage)
        self.ui.btn_PageNext.released.connect(self.nextPage)

    def prePage(self):
        temp = self.currentPic - 1
        if temp < 0 :
            self.currentPic = 15
        else:
            self.currentPic = temp

    def nextPage(self):
        temp = self.currentPic + 1
        if temp > 15:
            self.currentPic = 0
        else:
            self.currentPic = temp

    def paintEvent(self, e):
        pic = QPixmap(self.picPath[self.currentPic]).scaled(self.ui.lab_PicShow.width(),self.ui.lab_PicShow.height())
        self.ui.lab_PicShow.setPixmap(pic)
        super().paintEvent(e)

class MainWindow(QMainWindow,Ui_mainWindow):

    def __init__(self):
        super().__init__()
        self.ui =  Ui_mainWindow()
        self.ui.setupUi(self)
        self.resize(1027,768)

        self.comicBook = ComicBook()


        #初始化数据库
        self.DB = None
        self.createDB()

        self.ui.action_comicBook.triggered.connect(self.setComicBook)

    def setComicBook(self):
        self.setCentralWidget(self.comicBook)
    def comicBookNextPage(self,strMessage):
        print(strMessage)

    def createDB(self):
        if self.DB:
            return
        try:
            self.DB = QSqlDatabase.addDatabase("QSQLITE")
            self.DB.setDatabaseName("DB/C35N.db3")
            print("Open DB success!")
        except Exception as e:
            QMessageBox.critical(self,"错误","数据库驱动错误")
            print(e)

if __name__ == '__main__':
    mainApp = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(mainApp.exec_())

