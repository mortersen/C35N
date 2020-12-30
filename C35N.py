import sys
from PyQt5.QtWidgets import (
    QApplication,QMainWindow,QTabWidget,QWidget,QMessageBox,QHBoxLayout,QPushButton,
    QLabel,QDialog
)
from PyQt5.QtSql import QSqlDatabase
from PyQt5.QtGui import QPixmap

from UI.UI_MainWindow import Ui_mainWindow
from UI.UI_ComicBook import Ui_comicBook
from UI.UI_DBSourceWindow import Ui_DBSourceView
from UI.UI_Dlgabout import Ui_About
#导入字段的详细信息UI界面
from UI.UI_BookDetail import Ui_BookDetail
from UI.UI_PeriodicalDetail import Ui_PeriodicalDetail
from UI.UI_DissertationDetail import Ui_DissertationDetail
from UI.UI_ConferencePaperDetail import Ui_ConferencePaperDetail

import img_rc


picPath=[":/Icon/KJZ-C35N-1.png",":/Icon/KJZ-C35N-2.png",":/Icon/KJZ-C35N-3.png",
                      ":/Icon/KJZ-C35N-4.png",":/Icon/KJZ-C35N-5.png",":/Icon/KJZ-C35N-6.png",
                      ":/Icon/KJZ-C35N-7.png",":/Icon/KJZ-C35N-8.png",":/Icon/KJZ-C35N-9.png",
                      ":/Icon/KJZ-C35N-10.png",":/Icon/KJZ-C35N-11.png",":/Icon/KJZ-C35N-12.png",
                      ":/Icon/KJZ-C35N-13.png",":/Icon/KJZ-C35N-14.png",":/Icon/KJZ-C35N-15.png",
                      ":/Icon/KJZ-C35N-16.png"]

#关于对话框
class About(QDialog):
    def __init__(self):
        super().__init__()
        ui = Ui_About()
        ui.setupUi(self)

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui =  Ui_mainWindow()
        self.ui.setupUi(self)

        #设置中心控制区的QTabWidget
        self.cenTab = QTabWidget()
        self.cenTab.setTabsClosable(True)
        self.cenTab.tabCloseRequested.connect(self.on_cenTab_close)
        self.setCentralWidget(self.cenTab)

        #连环画页面初始设置
        self.comicView = QWidget()
        self.comic = Ui_comicBook()
        self.comic.setupUi(self.comicView)
        self.comicView.setObjectName("COMICVIEW")
        self.isOpenComicView = False
        self.currentPic = -1
        self.comic.btn_PageNext.released.connect(self.on_comic_btnPageNext)
        self.comic.btn_PagePre.released.connect(self.on_comic_btnPagePre)

        #设置数据库浏览页面
        self.DBView = QWidget()
        self.DBSourceView = Ui_DBSourceView()
        self.DBSourceView.setupUi(self.DBView)
        self.DBView.setObjectName("DBView")
        self.DBSourceView.tree_LeftView.setHeaderHidden(True)
        self.BOOKDETAIL = Ui_ConferencePaperDetail()
        self.BOOKDETAIL.setupUi(self.DBSourceView.widget_RightDetail)

        self.isOpenDBView = False
        self.DBSourceView.tree_LeftView.clicked.connect(self.on_DBViewTree_Clicked)

        #初始化数据库
        self.DB = None
        self.createDB()

        self.ui.action_comicBook.triggered.connect(self.setComicView)
        self.ui.action_DB.triggered.connect(self.setDBView)
        self.ui.action_About.triggered.connect(self.setAboutDial)



    #槽函数，相应工具栏动作按钮
    def setComicView(self):
        if self.isOpenComicView == True :
            self.cenTab.setCurrentWidget(self.comicView)
        else:
            #self.comic.lab_PicShow.setPixmap(QPixmap(picPath[self.currentPic]))
            self.cenTab.addTab(self.comicView,"连环画故事《陈三五娘》")
            self.isOpenComicView = True
            print(self.comicView.objectName())

    def setDBView(self):
        if self.isOpenDBView == True:
            self.cenTab.setCurrentWidget(self.DBView)
        else:
            self.cenTab.addTab(self.DBView,"数据库浏览")
            self.isOpenDBView = True
            print(self.DBView.objectName())

    def setAboutDial(self):
        about = About()
        about.exec_()
    #连环画下一页
    def on_comic_btnPageNext(self):
        temp = self.currentPic + 1
        if temp > 15:
            self.currentPic = 0
        else:
            self.currentPic = temp
        pic = QPixmap(picPath[self.currentPic]).scaled(self.comic.lab_PicShow.width(),
                                                       self.comic.lab_PicShow.height())
        self.comic.lab_PicShow.setPixmap(pic)
    #连环画上一页
    def on_comic_btnPagePre(self):
        temp = self.currentPic - 1
        if temp < 0:
            self.currentPic = 15
        else:
            self.currentPic = temp
        pic = QPixmap(picPath[self.currentPic]).scaled(self.comic.lab_PicShow.width(),
                                                       self.comic.lab_PicShow.height())
        self.comic.lab_PicShow.setPixmap(pic)

    #链接数据库
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

    #工作区标签页关闭
    def on_cenTab_close(self,index):
        tabName = self.cenTab.currentWidget().objectName()
        if tabName == "COMICVIEW":
            self.isOpenComicView = False
        if tabName == "DBView":
            self.isOpenDBView = False
        self.cenTab.removeTab(index)

    #点击数据库浏览页资源树
    def on_DBViewTree_Clicked(self,index):
        item = self.DBSourceView.tree_LeftView.currentItem()
        print(item.text(0))


if __name__ == '__main__':
    mainApp = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.showMaximized()
    sys.exit(mainApp.exec_())

