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

    #自定义信号
    Signal_DownloadOver = pyqtSignal(str)

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

        #设置数据库浏览页面
        self.DBView = QWidget()
        self.DBTreeMain = Ui_DBTreeMain()
        self.DBTreeMain.setupUi(self.DBView)
        self.DBView.setObjectName("DBView")
        self.DBTreeMain.tree_LeftView.setHeaderHidden(True)
        self.isOpenDBView = False
        self.tableName = ""#当前选中的数据表名
        self.DBTreeMain.tree_LeftView.clicked.connect(self.on_DBTreeMain_Clicked)

        #初始化数据库
        self.DB = None
        self.createDB()

        #工具栏按钮信号绑定
        self.ui.action_comicBook.triggered.connect(self.setComicView)
        self.ui.action_DB.triggered.connect(self.setDBView)
        self.ui.action_About.triggered.connect(self.setAboutDial)
        self.ui.action_Introduce.triggered.connect(self.setIntroduceView)

        self.Signal_DownloadOver.connect(self.on_DownloadOver)

        #self.comic.btn_PagePre.setVisible(False)
        #self.comic.btn_PageNext.setVisible(False)
        #self.ui.action_comicBook.triggered.emit()
        self.ui.action_DB.triggered.emit()


    #槽函数,显示介绍页
    def setIntroduceView(self):
        tab = IntroduceWidget()
        tab.exec()

    #槽函数，相应工具栏动作按钮
    def setComicView(self):
        tab = ComicBook()
        self.cenTab.addTab(tab,"简介-《陈三五娘》连环画")
        self.cenTab.setCurrentWidget(tab)

    #槽函数，数据库浏览页
    def setDBView(self):
        if self.isOpenDBView == True:
            self.cenTab.setCurrentWidget(self.DBView)
        else:
            self.cenTab.addTab(self.DBView,"数据库浏览")
            self.isOpenDBView = True
            #print(self.DBView.objectName())

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

    #获取PDF文件二进制流
    def getPDFStream(self,tName,MD5):
        try:
            query = QSqlQuery(self.DB)
            tFileName = tName + "File"
            sqQuery = "select FileBinary from %s where MD5=?" % tFileName
            #print(sqQuery)
            query.prepare(sqQuery)
            query.bindValue(0,MD5)
            query.exec()
            query.last()
            return query.value("fileBinary")
        except:
            return None


    #槽函数，打开标签页，阅读PDF
    def openTab2ReadPDF(self,MD5,title):
        stream = self.getPDFStream(self.tableName, MD5)
        tab = WidgetPDFStream(stream, title)
        self.cenTab.addTab(tab, title[0:16])
        self.cenTab.setCurrentWidget(tab)


    #槽函数，下载PDF
    def downloadPDF(self,tName,MD5,title):
        #print("这里是主窗口", tName, MD5, title)
        newFileName, ok = QFileDialog.getSaveFileName(self, "文件下载到", os.getcwd()+"\\"+title+".pdf", "*.pdf")
        if ok:
            pass
            def func():
                stream = bytes(self.getPDFStream(self.tableName, MD5))
                docDoc = fitz.open(None, stream, 'PDF')
                docDoc.save(newFileName)
            saveThread = Thread(target=func)
            saveThread.start()
            self.Signal_DownloadOver.emit(newFileName)
        else:
            return

    #槽函数响应下载完成
    def on_DownloadOver(self,str):
        QMessageBox.information(self, "提示", str + "文件下载成功！")

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
            #print(self.tableName)
            #self.DBViewCurrentPage = 0
            #self.DBViewEachPageCount = 20
            while self.DBTreeMain.layout_RightView.count():
                child = self.DBTreeMain.layout_RightView.takeAt(0)
                child.widget().deleteLater()
            if index == 0:#期刊
                DocumentItem = DBDocumentQK(self.DB)
            elif index == 1:#图书
                DocumentItem = DBDocumentTS(self.DB)
            elif index == 2:#学位论文
                DocumentItem =DBDocumentXWLW(self.DB)
            elif index == 3:#会议论文
                DocumentItem =DBDocumentHYLW(self.DB)
            elif index == 4:#戏曲
                DocumentItem = DBDocumentXQ(self.DB)
            elif index == 5:#歌册
                DocumentItem =(DBDocumentQP(self.DB))
            elif index == 6:#南音
                DocumentItem =(DBDocumentNY(self.DB))
            self.DBTreeMain.layout_RightView.addWidget(DocumentItem)
            DocumentItem.signal_ReadPdf.connect(self.openTab2ReadPDF)
            DocumentItem.signal_Download.connect(self.downloadPDF)


if __name__ == '__main__':
    mainApp = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.showMaximized()
    mainWindow.setIntroduceView()
    sys.exit(mainApp.exec_())

