import sys,os
import fitz
from PDFWidget import WidgetPDF,WidgetPDFStream
from PyQt5.QtWidgets import (
    QApplication,QMainWindow,QTabWidget,QWidget,QMessageBox,QHBoxLayout,QPushButton,
    QLabel,QDialog,QDataWidgetMapper,QTableView,QFileDialog
)
from PyQt5.QtSql import QSqlDatabase,QSqlQuery,QSqlQueryModel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import pyqtSignal,QThread
from threading import Thread
from ComicBook import ComicBook
from DBView import DBView
from UI.UI_MainWindow import Ui_mainWindow
from UI.UI_ComicBook import Ui_comicBook
from UI.UI_DBSourceWindow import Ui_DBSourceView
from UI.UI_Dlgabout import Ui_About
from UI.UI_IntroduceWidget import Ui_IntroduceWidget

#导入数据库页面的，中部列表及右侧详细信息页面
from DBDocument import *
#导入数据库主页面，左侧树结构
from UI.UI_DBTreeMain import Ui_DBTreeMain

import img_rc

#文献数据库表名
tableName = ["Periodical","Book","Dissertation","ConferencePaper",
             "TraditionalOpera","SongBook","SouthSoundOpera"]

#关于对话框
class About(QDialog):
    def __init__(self):
        super().__init__()
        ui = Ui_About()
        ui.setupUi(self)


class IntroduceWidget(QDialog):
    def __init__(self):
        super().__init__()
        UI = Ui_IntroduceWidget()
        UI.setupUi(self)
        UI.label.setAlignment(Qt.AlignCenter)
        self.resize(972,720)


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui =  Ui_mainWindow()
        self.ui.setupUi(self)
        #窗体显示最小化和关闭按钮
        #self.setWindowFlags(Qt.WindowCloseButtonHint|Qt.WindowMinimizeButtonHint)


        #设置中心控制区的QTabWidget
        self.cenTab = QTabWidget()
        self.cenTab.setTabsClosable(True)
        self.cenTab.tabCloseRequested.connect(self.on_cenTab_close)
        self.setCentralWidget(self.cenTab)

        #初始化数据库
        self.DB = None
        self.createDB()

        #工具栏按钮信号绑定
        self.ui.action_comicBook.triggered.connect(self.setComicView)
        self.ui.action_DB.triggered.connect(self.setDBView)
        self.ui.action_About.triggered.connect(self.setAboutDial)
        self.ui.action_Introduce.triggered.connect(self.setIntroduceView)

        self.ui.action_DB.triggered.emit()


    #槽函数,显示介绍页
    def setIntroduceView(self):
        tab = IntroduceWidget()
        tab.exec()

    #槽函数，相应工具栏动作按钮
    def setComicView(self):
        tab = ComicBook()
        self.cenTab.addTab(tab,"连环画《陈三五娘》")
        self.cenTab.setCurrentWidget(tab)


    #槽函数，数据库浏览页
    def setDBView(self):
        tab = DBView(self.DB)
        tab.Signal_ReadPdfByTab.connect(self.on_OpenPdfTab)
        self.cenTab.addTab(tab,"数据库浏览")
        self.cenTab.setCurrentWidget(tab)


    #获取PDF文件二进制流
    def getPDFStream(self,tName,MD5):
        try:
            query = QSqlQuery(self.DB)
            tFileName = tName + "File"
            sqQuery = "select FileBinary from %s where MD5=?" % tFileName
            query.prepare(sqQuery)
            query.bindValue(0,MD5)
            query.exec()
            query.last()
            return query.value("fileBinary")
        except:
            return None

    #槽函数，打开标签页阅读PDF
    def on_OpenPdfTab(self,tName,MD5,title):
        stream = self.getPDFStream(tName,MD5)
        tab = WidgetPDFStream(stream, title)
        self.cenTab.addTab(tab, title[0:16])
        self.cenTab.setCurrentWidget(tab)

    def setAboutDial(self):
        about = About()
        about.exec_()

    #链接数据库
    def createDB(self):
        if self.DB:
            return
        try:
            self.DB = QSqlDatabase.addDatabase("QSQLITE")
            self.DB.setDatabaseName("DB/C35N.db3")
            #print("Open DB success!")
        except Exception as e:
            QMessageBox.critical(self,"错误","数据库驱动错误")
            print(e)

    #工作区标签页关闭
    def on_cenTab_close(self,index):
        self.cenTab.removeTab(index)



if __name__ == '__main__':
    mainApp = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.showMaximized()
    mainWindow.setIntroduceView()
    sys.exit(mainApp.exec_())

