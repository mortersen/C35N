import sys
from PyQt5.QtWidgets import (
    QApplication,QMainWindow,QTabWidget,QWidget,QMessageBox,QHBoxLayout,QPushButton,
    QLabel,QDialog,QDataWidgetMapper,QTableView
)
from PyQt5.QtSql import QSqlDatabase,QSqlQuery,QSqlQueryModel
from PyQt5.QtGui import QPixmap

from UI.UI_MainWindow import Ui_mainWindow
from UI.UI_ComicBook import Ui_comicBook
from UI.UI_DBSourceWindow import Ui_DBSourceView
from UI.UI_Dlgabout import Ui_About

#导入数据库页面的，中部列表及右侧详细信息页面
from DBDocument import *
#导入数据库主页面，左侧树结构
from UI.UI_DBTreeMain import Ui_DBTreeMain

import img_rc

#连环画图片资源路径
picPath=[":/Icon/KJZ-C35N-1.png",":/Icon/KJZ-C35N-2.png",":/Icon/KJZ-C35N-3.png",
                      ":/Icon/KJZ-C35N-4.png",":/Icon/KJZ-C35N-5.png",":/Icon/KJZ-C35N-6.png",
                      ":/Icon/KJZ-C35N-7.png",":/Icon/KJZ-C35N-8.png",":/Icon/KJZ-C35N-9.png",
                      ":/Icon/KJZ-C35N-10.png",":/Icon/KJZ-C35N-11.png",":/Icon/KJZ-C35N-12.png",
                      ":/Icon/KJZ-C35N-13.png",":/Icon/KJZ-C35N-14.png",":/Icon/KJZ-C35N-15.png",
                      ":/Icon/KJZ-C35N-16.png"]

#文献数据库表名
tableName = ["Periodical","Book","Dissertation","ConferencePaper",
             "TraditionalOpera","SongBook","SouthSoundOpera"]

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
        self.DBTreeMain = Ui_DBTreeMain()
        self.DBTreeMain.setupUi(self.DBView)
        self.DBView.setObjectName("DBView")
        self.DBTreeMain.tree_LeftView.setHeaderHidden(True)


        self.isOpenDBView = False
        self.tableName = ""
        self.DBViewCurrentPage = 0
        self.DBViewEachPageCount = 20
        self.DBViewTotalRecord = 0
        self.queryModel = QSqlQueryModel()



        self.DBTreeMain.tree_LeftView.clicked.connect(self.on_DBTreeMain_Clicked)

        #初始化数据库
        self.DB = None
        self.createDB()

        #工具栏按钮信号绑定
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
    def on_DBTreeMain_Clicked(self,index):
        item = (self.DBTreeMain.tree_LeftView.currentItem().text(1))
        if(item == ""):
            return
        else:
            index = int(item)
            self.tableName = tableName[index]
            print(self.tableName)
            self.DBViewCurrentPage = 0
            self.DBViewEachPageCount = 20
            while self.DBTreeMain.layout_RightView.count():
                child = self.DBTreeMain.layout_RightView.takeAt(0)
                child.widget().deleteLater()
            if index == 0:#期刊
                self.DBTreeMain.layout_RightView.addWidget(DBDocumentQK(self.DB))
            elif index == 1:#图书
                self.DBTreeMain.layout_RightView.addWidget(DBDocumentTS(self.DB))
            elif index == 2:#学位论文
                self.DBTreeMain.layout_RightView.addWidget(DBDocumentXWLW(self.DB))
            elif index == 3:#会议论文
                self.DBTreeMain.layout_RightView.addWidget(DBDocumentHYLW(self.DB))
            elif index == 4:#戏曲
                self.DBTreeMain.layout_RightView.addWidget(DBDocumentXQ(self.DB))
            elif index == 5:#歌册
                self.DBTreeMain.layout_RightView.addWidget(DBDocumentQP(self.DB))
            elif index == 6:#南音
                self.DBTreeMain.layout_RightView.addWidget(DBDocumentNY(self.DB))

    #数据库浏览-下一页
    def DBViewNextPage(self):
        print("next page")

    #数据库浏览-上一页
    def DBViewPrePage(self):
        print("上一页")

    #数据库浏览-跳转页面
    def DBViewGoto(self):
        print("跳转页")

    #数据库浏览-阅读PDF
    def DBViewReadPDF(self):
        print("阅读PDF")

    #数据库浏览-下载PDF
    def DBViewDownload(self):
        print("下载PDF")

    #数据库浏览-获取每页展示的记录数量
    def DBViewGetEachPageCount(self):
        text = self.DBSourceView.comBox_EachRecordOfPage.currentText()
        print(text)



if __name__ == '__main__':
    mainApp = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.showMaximized()
    sys.exit(mainApp.exec_())

