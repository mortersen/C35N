from PyQt5.QtWidgets import QWidget,QFileDialog,QMessageBox
from PyQt5.QtCore import pyqtSignal

from PyQt5.QtSql import QSqlQuery
from threading import Thread
import fitz,os

from UI.UI_DBTreeMain import Ui_DBTreeMain

#导入数据库页面的，中部列表及右侧详细信息页面
from DBDocument import *
from PDFWidget import WidgetPDFStream

#文献数据库表名
tableName = ["Periodical","Book","Dissertation","ConferencePaper",
             "TraditionalOpera","SongBook","SouthSoundOpera"]

class DBView(QWidget):
    Signal_DownloadOver = pyqtSignal(str)
    Signal_ReadPdfByTab = pyqtSignal(str,str,str)

    def __init__(self,DB):
        super().__init__()
        self.DB = DB
        self.tableName = ""
        self.UI = Ui_DBTreeMain()
        self.UI.setupUi(self)
        self.setObjectName("DBView")
        self.UI.tree_LeftView.setHeaderHidden(True)
        self.UI.tree_LeftView.clicked.connect(self.on_DBTreeMain_Clicked)

        self.Signal_DownloadOver.connect(self.on_DownloadOver)


    def on_DBTreeMain_Clicked(self,index):
        item = (self.UI.tree_LeftView.currentItem().text(1))
        if(item == ""):
            return
        else:
            index = int(item)
            self.tableName = tableName[index]
            while self.UI.layout_RightView.count():
                child = self.UI.layout_RightView.takeAt(0)
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
            self.UI.layout_RightView.addWidget(DocumentItem)
            DocumentItem.signal_ReadPdf.connect(self.openTab2ReadPDF)
            DocumentItem.signal_Download.connect(self.downloadPDF)


    #槽函数，发射信号，让主窗口加载PDF阅读
    def openTab2ReadPDF(self,MD5,title):
        self.Signal_ReadPdfByTab.emit(self.tableName,MD5,title)


    #槽函数，下载PDF
    def downloadPDF(self,tName,MD5,title):
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