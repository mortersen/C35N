from PyQt5.QtSql import QSqlQuery,QSqlQueryModel
from PyQt5.QtWidgets import QApplication,QWidget,QDataWidgetMapper,QAbstractItemView,QMessageBox
from PyQt5.QtCore import Qt,pyqtSignal

from UI.UI_TraditionalOperaDetail import Ui_TraditionalOperaDetail
from UI.UI_SouthSoundOperaDetail import Ui_SouthSoundOperaDetail
from UI.UI_SongBook import Ui_SongBookDetail
from UI.UI_ConferencePaperDetail import Ui_ConferencePaperDetail
from UI.UI_DissertationDetail import Ui_DissertationDetail
from UI.UI_PeriodicalDetail import Ui_PeriodicalDetail
from UI.UI_BookDetail import Ui_BookDetail
from UI.UI_DBSourceWindow import Ui_DBSourceView

#文献基础类
class DBDocumentBase(QWidget):
    signal_ReadPdf = pyqtSignal(str,str)#1:MD5,2:标题
    signal_Download = pyqtSignal(str,str,str)#1:表名，2:MD5,3:标题

    def __init__(self,DB):
        super().__init__()
        self.baseUI = Ui_DBSourceView()
        self.baseUI.setupUi(self)
        self.currentPage = 1
        self.eachPageRecord = 20
        self.totalRecord = 0
        self.totalPages = 0
        # 非查询状态标 False时执行条件查询语句，默认是非查询载入
        self.isAll = True
        self.baseUI.lab_QueryTotal.setText("")
        self.DB = DB
        self.DB.open()
        self.query = QSqlQuery(self.DB)
        self.queryModel = QSqlQueryModel(self)
        self.mapper = QDataWidgetMapper(self)

        self.baseUI.tableView.setModel(self.queryModel)

        # 获取默认选择模型
        self.selectionModel = self.baseUI.tableView.selectionModel()
        self.selectionModel.currentRowChanged.connect(self.do_currentRowChanged)
        #设置不可编辑
        #self.baseUI.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        #设置表格样式
        self.baseUI.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.baseUI.tableView.setSelectionMode(QAbstractItemView.SingleSelection)
        self.baseUI.tableView.setAlternatingRowColors(True)
        self.baseUI.tableView.verticalHeader().setDefaultSectionSize(40)
        #self.baseUI.tableView.horizontalHeader().setStretchLastSection(True)
        #self.baseUI.tableView.resizeColumnsToContents()

        #控件信号
        self.baseUI.comBox_EachRecordOfPage.currentIndexChanged.connect(self.get_EachRecordOfPage)
        self.baseUI.btn_PrePage.released.connect(self.on_PrePage)
        self.baseUI.btn_NextPage.released.connect(self.on_NextPage)
        self.baseUI.btn_Goto.released.connect(self.on_Goto)
        self.baseUI.btn_Reflash.released.connect(self.on_BtnReflash)
        self.baseUI.btn_Query.released.connect(self.on_BtnQuery)
        self.baseUI.lineEdit_Condition.returnPressed.connect(self.on_BtnQuery)

        #发送自定义信号
        self.baseUI.btn_ReadPDF.released.connect(self.on_ReadPDF_SignalEmit)
        self.baseUI.btn_Download.released.connect(self.on_Download_SignalEmit)

    #发射阅读PDF的信号给主窗口
    def on_ReadPDF_SignalEmit(self):
        print(self.objectName())
        pass
    #发射下载的信号给主窗口
    def on_Download_SignalEmit(self):
        print(self.objectName())
        pass
    #查询总记录数
    def getTotalRecord(self):
        pass

    #执行查询
    def recordQuery(self,limitIndex):
        pass

    def do_currentRowChanged(self,current,previous):
        pass

    #设置每页显示记录数量
    def get_EachRecordOfPage(self):
        pass

    def on_PrePage(self):
        print(self.objectName())

    def on_NextPage(self):
        print(self.objectName())

    def on_Goto(self):
        print(self.objectName())

    #重新载入
    def on_BtnReflash(self):
        if self.isAll == False:
            self.isAll = True
            self.clearQueryCondition()
        self.recordQuery(0)
        self.currentPage = 1
        self.baseUI.lab_CurrentPage.setText(str(self.currentPage))

    def on_BtnQuery(self):
        pass

    #清除有关查询的控件显示内容
    def clearQueryCondition(self):
        self.baseUI.comboBox_SearchBy.setCurrentIndex(0)
        self.baseUI.lineEdit_Condition.setText("")
        self.baseUI.lab_QueryTotal.setText("")

    #选择模型-行切换是更新组件界面
    def do_currentRowChanged(self,current,previous):
        #print(current.row())
        self.mapper.setCurrentIndex(current.row())

    #计算总页数
    def caculateTotoalPage(self):
        totoalPage = self.totalRecord//self.eachPageRecord
        if self.totalRecord % self.eachPageRecord > 0 :
            totoalPage += 1
        return totoalPage

    def get_EachRecordOfPage(self):
        pass

    # 处理阅读按钮按下，发射下载信号到主窗口，携带三个参数表名、MD5、标题
    def on_ReadPDF_SignalEmit(self):
        index = self.baseUI.tableView.currentIndex().row()
        if index < 0:
            index = 0
        #print("阅读按钮信号----->" + str(index))
        # 获取选中记录
        curRec = self.queryModel.record(index)
        MD5 = curRec.value("MD5")
        Title = curRec.value("Title")
        #print(Title)
        self.signal_ReadPdf.emit(MD5, Title)

#封装戏曲
class DBDocumentXQ(DBDocumentBase):
    def __init__(self,DB):
        super().__init__(DB)
        self.win = QWidget()
        self.UI = Ui_TraditionalOperaDetail()
        self.UI.setupUi(self.win)
        self.baseUI.detailLayout.addWidget(self.win)

        #获得总记录数,总页数
        self.totalRecord = self.getTotalRecord()
        self.totalPages = self.caculateTotoalPage()
        self.baseUI.lab_Record.setText(str(self.totalRecord))
        self.baseUI.lab_CurrentPage.setText(str(self.currentPage))
        self.baseUI.lab_TotalPages.setText(str(self.totalPages))
        #初次载入
        self.recordQuery(0)


        self.queryModel.setHeaderData(0,Qt.Horizontal,"戏曲名")
        self.baseUI.tableView.setColumnWidth(0,400)
        self.queryModel.setHeaderData(1,Qt.Horizontal,"作者")
        self.queryModel.setHeaderData(2,Qt.Horizontal,"收录来源")
        self.queryModel.setHeaderData(3,Qt.Horizontal,"页数")
        self.queryModel.setHeaderData(4,Qt.Horizontal,"简介")

        self.baseUI.tableView.setColumnHidden(5,True)

        self.mapper.setModel(self.queryModel)
        self.mapper.addMapping(self.UI.lineEdit_Title, 0)
        self.mapper.addMapping(self.UI.lineEdit_Author, 1)
        self.mapper.addMapping(self.UI.lineEdit_Origin, 2)
        self.mapper.addMapping(self.UI.lineEdit_Pages, 3)
        self.mapper.addMapping(self.UI.textEdit_Summary, 4)

        self.mapper.toFirst()

    #处理下载按钮按下，发射下载信号到主窗口，携带三个参数表名、MD5、标题
    def on_Download_SignalEmit(self):
        index =  self.baseUI.tableView.currentIndex().row()
        if index < 0:
            return
        print("下载按钮信号----->"+str(index))
        #获取选中记录
        curRec = self.queryModel.record(index)
        MD5 = curRec.value("MD5")
        Title = curRec.value("Title")
        print(Title)
        self.signal_Download.emit("TraditionalOpera",MD5,Title)

    #执行查询模型
    def recordQuery(self,Index):
        try:
            szQurey = ("select Title, Author, Origin, Pages, Summary,md5 from TraditionalOpera limit %d,%d" % (
                Index, self.eachPageRecord))
            self.queryModel.setQuery(szQurey)
        except Exception:
            print(self.objectName() + Exception)

    def getTotalRecord(self):
        try:
            self.query.exec("select * from TraditionalOpera")
            self.query.last()
            return self.query.at() + 1
        except Exception:
            print(Exception)

    # 设置每页显示记录数量
    def get_EachRecordOfPage(self):
        text = self.baseUI.comBox_EachRecordOfPage.currentText()
        print(text)
        self.eachPageRecord = int(text)
        self.totalPages = self.caculateTotoalPage()
        self.currentPage = 1
        self.recordQuery(0)
        self.baseUI.lab_CurrentPage.setText(str(self.currentPage))
        self.baseUI.lab_TotalPages.setText(str(self.totalPages))
        self.mapper.toFirst()

    #下一页
    def on_NextPage(self):
        if self.currentPage + 1 > self.totalPages:
            return
        index = (self.currentPage ) * self.eachPageRecord
        self.recordQuery(index)
        self.currentPage += 1
        self.baseUI.lab_CurrentPage.setText(str(self.currentPage))

    #上一页
    def on_PrePage(self):
        if self.currentPage == 1:
            return
        index = (self.currentPage - 2) * self.eachPageRecord
        self.recordQuery(index)
        self.currentPage -= 1
        self.baseUI.lab_CurrentPage.setText(str(self.currentPage))

    #跳转页
    def on_Goto(self):
        text = self.baseUI.lineEdit_WhichPage.text().strip()
        if text == "":
            return
        if not text.isdigit() :
            QMessageBox.information(self,"提示","请输入跳转页码!")
            return
        pageIndex = int(text)
        if pageIndex < 1 or pageIndex > self.totalPages:
            QMessageBox.information(self,"提示","没有指定的页面，请重新输入")
            return
        index = (pageIndex - 1) * self.eachPageRecord
        self.recordQuery(index)
        self.currentPage = pageIndex
        self.baseUI.lab_CurrentPage.setText(str(self.currentPage))

    #条件查询
    def on_BtnQuery(self):
        condition = self.baseUI.lineEdit_Condition.text().strip()
        if condition == "":
            return
        fieldIndex = self.baseUI.comboBox_SearchBy.currentIndex()
        #print(fieldIndex,condition)
        if fieldIndex == 0:#按标题
            pass
            field = "Title"
        elif fieldIndex == 1:#按作者
            pass
            field = "Author"
        elif fieldIndex == 2:#按关键字
            QMessageBox.information(self, "提示", "无该项查询内容，请重新选择查询内容！")
            return
        elif fieldIndex == 3:#按主要内容
            field ="Summary"
        if self.isAll == True:#载入后首次查询
            self.isAll = False
        condition = "\'%"+condition + "%\'"
        sen = "select Title, Author, Origin, Pages, Summary,md5 from TraditionalOpera where %s like %s" % (field,condition)
        self.queryModel.setQuery(sen)
        self.baseUI.lab_QueryTotal.setText("共查询到 %d 条信息" % (self.queryModel.rowCount()))


#封装期刊
class DBDocumentQK(DBDocumentBase):
    def __init__(self,DB):
        super().__init__(DB)
        self.win = QWidget()
        self.UI = Ui_PeriodicalDetail()
        self.UI.setupUi(self.win)
        self.baseUI.detailLayout.addWidget(self.win)

        # 获得总记录数,总页数
        self.totalRecord = self.getTotalRecord()
        self.totalPages = self.caculateTotoalPage()
        self.baseUI.lab_Record.setText(str(self.totalRecord))
        self.baseUI.lab_CurrentPage.setText(str(self.currentPage))
        self.baseUI.lab_TotalPages.setText(str(self.totalPages))

        self.recordQuery(0)

        self.queryModel.setHeaderData(0, Qt.Horizontal, "标题")
        self.baseUI.tableView.setColumnWidth(0, 400)
        self.queryModel.setHeaderData(1, Qt.Horizontal, "作者")
        self.queryModel.setHeaderData(2, Qt.Horizontal, "期刊名")
        self.queryModel.setHeaderData(3, Qt.Horizontal, "期数号")
        self.queryModel.setHeaderData(4, Qt.Horizontal, "刊发年份")
        self.queryModel.setHeaderData(5, Qt.Horizontal, "页码")
        self.queryModel.setHeaderData(6, Qt.Horizontal, "卷数")
        self.queryModel.setHeaderData(7, Qt.Horizontal, "关键字")
        self.queryModel.setHeaderData(8, Qt.Horizontal, "摘要")

        self.baseUI.tableView.setColumnHidden(9, True)

        self.mapper.setModel(self.queryModel)
        self.mapper.addMapping(self.UI.lineEdit_Titel, 0)
        self.mapper.addMapping(self.UI.lineEdit_Author, 1)
        self.mapper.addMapping(self.UI.lineEdit_Journal, 2)
        self.mapper.addMapping(self.UI.lineEdit_Issue, 3)
        self.mapper.addMapping(self.UI.lineEdit_Year, 4)
        self.mapper.addMapping(self.UI.lineEdit_Pages,5)
        self.mapper.addMapping(self.UI.lineEdit_Volume,6)
        self.mapper.addMapping(self.UI.lineEdit_Keywords,7)
        self.mapper.addMapping(self.UI.textEdit_Abstract,8)

        self.mapper.toFirst()

    # 执行查询模型
    def recordQuery(self, Index):
        try:
            szQurey = ("select Title, Author,Journal,Issue,Year,Pages,Volume, Keyword, Abstract, MD5 from Periodical limit %d,%d" % (
                Index, self.eachPageRecord))
            self.queryModel.setQuery(szQurey)
        except Exception:
            print(self.objectName() + Exception)

    def getTotalRecord(self):
        try:
            self.query.exec("select * from Periodical")
            self.query.last()
            return self.query.at() + 1
        except Exception:
            print(Exception)

    # 设置每页显示记录数量
    def get_EachRecordOfPage(self):
        text = self.baseUI.comBox_EachRecordOfPage.currentText()
        print(text)
        self.eachPageRecord = int(text)
        self.totalPages = self.caculateTotoalPage()
        self.currentPage = 1
        self.recordQuery(0)
        self.baseUI.lab_CurrentPage.setText(str(self.currentPage))
        self.baseUI.lab_TotalPages.setText(str(self.totalPages))
        self.mapper.toFirst()

    # 下一页
    def on_NextPage(self):
        if self.currentPage + 1 > self.totalPages:
            return
        index = (self.currentPage ) * self.eachPageRecord
        self.recordQuery(index)
        self.currentPage += 1
        self.baseUI.lab_CurrentPage.setText(str(self.currentPage))

    # 上一页
    def on_PrePage(self):
        if self.currentPage == 1:
            return
        index = (self.currentPage - 2) * self.eachPageRecord
        self.recordQuery(index)
        self.currentPage -= 1
        self.baseUI.lab_CurrentPage.setText(str(self.currentPage))

    # 跳转页
    def on_Goto(self):
        text = self.baseUI.lineEdit_WhichPage.text().strip()
        if text == "":
            return
        if not text.isdigit():
            QMessageBox.information(self, "提示", "请输入数字!")
            return
        pageIndex = int(text)
        if pageIndex < 1 or pageIndex > self.totalPages:
            QMessageBox.information(self, "提示", "没有指定的页面，请重新输入")
            return
        index = (pageIndex - 1) * self.eachPageRecord
        self.recordQuery(index)
        self.currentPage = pageIndex
        self.baseUI.lab_CurrentPage.setText(str(self.currentPage))

    # 条件查询
    def on_BtnQuery(self):
        condition = self.baseUI.lineEdit_Condition.text().strip()
        if condition == "":
            return
        fieldIndex = self.baseUI.comboBox_SearchBy.currentIndex()
        # print(fieldIndex,condition)
        if fieldIndex == 0:  # 按标题
            pass
            field = "Title"
        elif fieldIndex == 1:  # 按作者
            pass
            field = "Author"
        elif fieldIndex == 2:  # 按关键字
            field = 'Keyword'
        elif fieldIndex == 3:  # 按主要内容
            field = "Abstract"
        if self.isAll == True:  # 载入后首次查询
            self.isAll = False
        condition = "\'%" + condition + "%\'"
        sen = "select Title, Author,Journal,Issue,Year,Pages,Volume, Keyword, Abstract, MD5 from Periodical where %s like %s" % (
            field, condition)
        self.queryModel.setQuery(sen)
        self.baseUI.lab_QueryTotal.setText("共查询到 %d 条信息" % (self.queryModel.rowCount()))

    #处理下载按钮按下，发射下载信号到主窗口，携带三个参数表名、MD5、标题
    def on_Download_SignalEmit(self):
        index =  self.baseUI.tableView.currentIndex().row()
        if index < 0:
            return
        print("下载按钮信号----->"+str(index))
        #获取选中记录
        curRec = self.queryModel.record(index)
        MD5 = curRec.value("MD5")
        Title = curRec.value("Title")
        print(Title)
        self.signal_Download.emit("Periodical",MD5,Title)


#封装图书
class DBDocumentTS(DBDocumentBase):
    def __init__(self,DB):
        super().__init__(DB)
        self.win = QWidget()
        self.UI = Ui_BookDetail()
        self.UI.setupUi(self.win)
        self.baseUI.detailLayout.addWidget(self.win)

        # 获得总记录数,总页数
        self.totalRecord = self.getTotalRecord()
        self.totalPages = self.caculateTotoalPage()
        self.baseUI.lab_Record.setText(str(self.totalRecord))
        self.baseUI.lab_CurrentPage.setText(str(self.currentPage))
        self.baseUI.lab_TotalPages.setText(str(self.totalPages))

        self.recordQuery(0)

        self.queryModel.setHeaderData(0, Qt.Horizontal, "书名")
        self.baseUI.tableView.setColumnWidth(0, 300)
        self.queryModel.setHeaderData(1, Qt.Horizontal, "丛书名")
        self.queryModel.setHeaderData(2, Qt.Horizontal, "作者")
        self.queryModel.setHeaderData(3, Qt.Horizontal, "页数")
        self.queryModel.setHeaderData(4, Qt.Horizontal, "出版年份")
        self.queryModel.setHeaderData(5, Qt.Horizontal, "出版社")
        self.queryModel.setHeaderData(6, Qt.Horizontal, "关键字")
        self.queryModel.setHeaderData(7, Qt.Horizontal, "摘要")

        self.baseUI.tableView.setColumnHidden(8,True)

        self.mapper.setModel(self.queryModel)
        self.mapper.addMapping(self.UI.lineEdit_Title, 0)
        self.mapper.addMapping(self.UI.lineEdit_SecondaryTitle, 1)
        self.mapper.addMapping(self.UI.lineEdit_Author, 2)
        self.mapper.addMapping(self.UI.lineEdit__Pages, 3)
        self.mapper.addMapping(self.UI.lineEdit_Year, 4)
        self.mapper.addMapping(self.UI.lineEdit__Publisher, 5)
        self.mapper.addMapping(self.UI.lineEdit_Keywords, 6)
        self.mapper.addMapping(self.UI.textEdit_Abstract, 7)

        self.mapper.toFirst()

    # 执行查询模型
    def recordQuery(self, Index):
        try:
            szQurey = (
            "select Title, SecondaryTitle, Author, Pages, Year, Publisher, Keywords, Abstract, MD5 from Book limit %d,%d" % (
                Index, self.eachPageRecord))
            self.queryModel.setQuery(szQurey)
        except Exception:
            print(self.objectName() + Exception)

    def getTotalRecord(self):
        try:
            self.query.exec("select * from Book")
            self.query.last()
            return self.query.at() + 1
        except Exception:
            print(Exception)

    # 设置每页显示记录数量
    def get_EachRecordOfPage(self):
        text = self.baseUI.comBox_EachRecordOfPage.currentText()
        print(text)
        self.eachPageRecord = int(text)
        self.totalPages = self.caculateTotoalPage()
        self.currentPage = 1
        self.recordQuery(0)
        self.baseUI.lab_CurrentPage.setText(str(self.currentPage))
        self.baseUI.lab_TotalPages.setText(str(self.totalPages))
        self.mapper.toFirst()

    # 下一页
    def on_NextPage(self):
        if self.currentPage + 1 > self.totalPages:
            return
        index = (self.currentPage ) * self.eachPageRecord
        self.recordQuery(index)
        self.currentPage += 1
        self.baseUI.lab_CurrentPage.setText(str(self.currentPage))

    # 上一页
    def on_PrePage(self):
        if self.currentPage == 1:
            return
        index = (self.currentPage - 2) * self.eachPageRecord
        self.recordQuery(index)
        self.currentPage -= 1
        self.baseUI.lab_CurrentPage.setText(str(self.currentPage))

    # 跳转页
    def on_Goto(self):
        text = self.baseUI.lineEdit_WhichPage.text().strip()
        if text == "":
            return
        if not text.isdigit():
            QMessageBox.information(self, "提示", "请输入数字!")
            return
        pageIndex = int(text)
        if pageIndex < 1 or pageIndex > self.totalPages:
            QMessageBox.information(self, "提示", "没有指定的页面，请重新输入")
            return
        index = (pageIndex - 1) * self.eachPageRecord
        self.recordQuery(index)
        self.currentPage = pageIndex
        self.baseUI.lab_CurrentPage.setText(str(self.currentPage))

    # 条件查询
    def on_BtnQuery(self):
        condition = self.baseUI.lineEdit_Condition.text().strip()
        if condition == "":
            return
        fieldIndex = self.baseUI.comboBox_SearchBy.currentIndex()
        # print(fieldIndex,condition)
        if fieldIndex == 0:  # 按标题
            field = "Title"
        elif fieldIndex == 1:  # 按作者
            field = "Author"
        elif fieldIndex == 2:  # 按关键字
            field = 'Keywords'
        elif fieldIndex == 3:  # 按主要内容
            field = "Abstract"
        if self.isAll == True:  # 载入后首次查询
            self.isAll = False
        condition = "\'%" + condition + "%\'"
        sen = "select Title, SecondaryTitle, Author, Pages, Year, Publisher, Keywords, Abstract, MD5 from Book where %s like %s" % (
            field, condition)
        self.queryModel.setQuery(sen)
        self.baseUI.lab_QueryTotal.setText("共查询到 %d 条信息" % (self.queryModel.rowCount()))

    #处理下载按钮按下，发射下载信号到主窗口，携带三个参数表名、MD5、标题
    def on_Download_SignalEmit(self):
        index =  self.baseUI.tableView.currentIndex().row()
        if index < 0:
            return
        print("下载按钮信号----->"+str(index))
        #获取选中记录
        curRec = self.queryModel.record(index)
        MD5 = curRec.value("MD5")
        Title = curRec.value("Title")
        print(Title)
        self.signal_Download.emit("Book",MD5,Title)

#封装南音
class DBDocumentNY(DBDocumentBase):
    def __init__(self,DB):
        super().__init__(DB)
        self.win = QWidget()
        self.UI = Ui_SouthSoundOperaDetail()
        self.UI.setupUi(self.win)
        self.baseUI.detailLayout.addWidget(self.win)

        # 获得总记录数,总页数
        self.totalRecord = self.getTotalRecord()
        self.totalPages = self.caculateTotoalPage()
        self.baseUI.lab_Record.setText(str(self.totalRecord))
        self.baseUI.lab_CurrentPage.setText(str(self.currentPage))
        self.baseUI.lab_TotalPages.setText(str(self.totalPages))

        self.recordQuery(0)

        self.queryModel.setHeaderData(0, Qt.Horizontal, "曲谱名")
        self.baseUI.tableView.setColumnWidth(0, 200)
        self.queryModel.setHeaderData(1, Qt.Horizontal, "作者")
        self.queryModel.setHeaderData(2, Qt.Horizontal, "页码")
        self.queryModel.setHeaderData(3, Qt.Horizontal, "资源来源")

        self.baseUI.tableView.setColumnHidden(4, True)

        self.mapper.setModel(self.queryModel)
        self.mapper.addMapping(self.UI.lineEdit_Title, 0)
        self.mapper.addMapping(self.UI.lineEdit_Author, 1)
        self.mapper.addMapping(self.UI.lineEdit_Pages, 2)
        self.mapper.addMapping(self.UI.lineEdit_Origin, 3)

        self.mapper.toFirst()

    # 执行查询模型
    def recordQuery(self, Index):
        try:
            szQurey = ("select Title, Author, Pages, Origin, MD5 from SouthSoundOpera limit %d,%d" % (
                Index, self.eachPageRecord))
            self.queryModel.setQuery(szQurey)
        except Exception:
            print(self.objectName() + Exception)

    def getTotalRecord(self):
        try:
            self.query.exec("select * from SouthSoundOpera")
            self.query.last()
            return self.query.at() + 1
        except Exception:
            print(Exception)

    # 设置每页显示记录数量
    def get_EachRecordOfPage(self):
        text = self.baseUI.comBox_EachRecordOfPage.currentText()
        print(text)
        self.eachPageRecord = int(text)
        self.totalPages = self.caculateTotoalPage()
        self.currentPage = 1
        self.recordQuery(0)
        self.baseUI.lab_CurrentPage.setText(str(self.currentPage))
        self.baseUI.lab_TotalPages.setText(str(self.totalPages))
        self.mapper.toFirst()

    # 下一页
    def on_NextPage(self):
        if self.currentPage + 1 > self.totalPages:
            return
        index = (self.currentPage) * self.eachPageRecord
        self.recordQuery(index)
        self.currentPage += 1
        self.baseUI.lab_CurrentPage.setText(str(self.currentPage))

    # 上一页
    def on_PrePage(self):
        if self.currentPage == 1:
            return
        index = (self.currentPage - 2) * self.eachPageRecord
        self.recordQuery(index)
        self.currentPage -= 1
        self.baseUI.lab_CurrentPage.setText(str(self.currentPage))

    # 跳转页
    def on_Goto(self):
        text = self.baseUI.lineEdit_WhichPage.text().strip()
        if text == "":
            return
        if not text.isdigit():
            QMessageBox.information(self, "提示", "请输入数字!")
            return
        pageIndex = int(text)
        if pageIndex < 1 or pageIndex > self.totalPages:
            QMessageBox.information(self, "提示", "没有指定的页面，请重新输入")
            return
        index = (pageIndex - 1) * self.eachPageRecord
        self.recordQuery(index)
        self.currentPage = pageIndex
        self.baseUI.lab_CurrentPage.setText(str(self.currentPage))

    # 条件查询
    def on_BtnQuery(self):
        condition = self.baseUI.lineEdit_Condition.text().strip()
        if condition == "":
            return
        fieldIndex = self.baseUI.comboBox_SearchBy.currentIndex()
        # print(fieldIndex,condition)
        if fieldIndex == 0:  # 按标题
            field = "Title"
        elif fieldIndex == 1:  # 按作者
            field = "Author"
        elif fieldIndex == 2:  # 按关键字
            QMessageBox.information(self, "提示", "无该项查询内容，请重新选择查询内容！")
            return
        elif fieldIndex == 3:  # 按主要内容
            QMessageBox.information(self, "提示", "无该项查询内容，请重新选择查询内容！")
            return
        if self.isAll == True:  # 载入后首次查询
            self.isAll = False
        condition = "\'%" + condition + "%\'"
        sen = "select Title, Author, Pages, Origin, MD5 from SouthSoundOpera where %s like %s" % (
            field, condition)
        self.queryModel.setQuery(sen)
        self.baseUI.lab_QueryTotal.setText("共查询到 %d 条信息" % (self.queryModel.rowCount()))

    #处理下载按钮按下，发射下载信号到主窗口，携带三个参数表名、MD5、标题
    def on_Download_SignalEmit(self):
        index =  self.baseUI.tableView.currentIndex().row()
        if index < 0:
            return
        print("下载按钮信号----->"+str(index))
        #获取选中记录
        curRec = self.queryModel.record(index)
        MD5 = curRec.value("MD5")
        Title = curRec.value("Title")
        print(Title)
        self.signal_Download.emit("SouthSoundOpera",MD5,Title)

#封装曲谱
class DBDocumentQP(DBDocumentBase):
    def __init__(self,DB):
        super().__init__(DB)
        self.win = QWidget()
        self.UI = Ui_SongBookDetail()
        self.UI.setupUi(self.win)
        self.baseUI.detailLayout.addWidget(self.win)

        # 获得总记录数,总页数
        self.totalRecord = self.getTotalRecord()
        self.totalPages = self.caculateTotoalPage()
        self.baseUI.lab_Record.setText(str(self.totalRecord))
        self.baseUI.lab_CurrentPage.setText(str(self.currentPage))
        self.baseUI.lab_TotalPages.setText(str(self.totalPages))

        self.recordQuery(0)

        self.queryModel.setHeaderData(0, Qt.Horizontal, "曲谱名")
        self.baseUI.tableView.setColumnWidth(0, 250)
        self.queryModel.setHeaderData(1, Qt.Horizontal, "作者")
        self.queryModel.setHeaderData(2, Qt.Horizontal, "页码")
        self.queryModel.setHeaderData(3, Qt.Horizontal, "资源来源")
        self.queryModel.setHeaderData(4, Qt.Horizontal, "简介")

        self.baseUI.tableView.setColumnHidden(5, True)

        self.mapper.setModel(self.queryModel)
        self.mapper.addMapping(self.UI.lineEdit_Title, 0)
        self.mapper.addMapping(self.UI.lineEdit_Author, 1)
        self.mapper.addMapping(self.UI.lineEdit_Pages, 2)
        self.mapper.addMapping(self.UI.lineEdit_Origin, 3)
        self.mapper.addMapping(self.UI.textEdit_Summary, 4)

        self.mapper.toFirst()

    # 执行查询模型
    def recordQuery(self, Index):
        try:
            szQurey = ("select Title, Author, Pages, Origin, Summary, MD5 from SongBook limit %d,%d" % (
                Index, self.eachPageRecord))
            self.queryModel.setQuery(szQurey)
        except Exception:
            print(self.objectName() + Exception)

    def getTotalRecord(self):
        try:
            self.query.exec("select * from SongBook")
            self.query.last()
            return self.query.at() + 1
        except Exception:
            print(Exception)

    # 设置每页显示记录数量
    def get_EachRecordOfPage(self):
        text = self.baseUI.comBox_EachRecordOfPage.currentText()
        print(text)
        self.eachPageRecord = int(text)
        self.totalPages = self.caculateTotoalPage()
        self.currentPage = 1
        self.recordQuery(0)
        self.baseUI.lab_CurrentPage.setText(str(self.currentPage))
        self.baseUI.lab_TotalPages.setText(str(self.totalPages))
        self.mapper.toFirst()

    # 下一页
    def on_NextPage(self):
        if self.currentPage + 1 > self.totalPages:
            return
        index = (self.currentPage) * self.eachPageRecord
        self.recordQuery(index)
        self.currentPage += 1
        self.baseUI.lab_CurrentPage.setText(str(self.currentPage))

    # 上一页
    def on_PrePage(self):
        if self.currentPage == 1:
            return
        index = (self.currentPage - 2) * self.eachPageRecord
        self.recordQuery(index)
        self.currentPage -= 1
        self.baseUI.lab_CurrentPage.setText(str(self.currentPage))

    # 跳转页
    def on_Goto(self):
        text = self.baseUI.lineEdit_WhichPage.text().strip()
        if text == "":
            return
        if not text.isdigit():
            QMessageBox.information(self, "提示", "请输入数字!")
            return
        pageIndex = int(text)
        if pageIndex < 1 or pageIndex > self.totalPages:
            QMessageBox.information(self, "提示", "没有指定的页面，请重新输入")
            return
        index = (pageIndex - 1) * self.eachPageRecord
        self.recordQuery(index)
        self.currentPage = pageIndex
        self.baseUI.lab_CurrentPage.setText(str(self.currentPage))

    # 条件查询
    def on_BtnQuery(self):
        condition = self.baseUI.lineEdit_Condition.text().strip()
        if condition == "":
            return
        fieldIndex = self.baseUI.comboBox_SearchBy.currentIndex()
        # print(fieldIndex,condition)
        if fieldIndex == 0:  # 按标题
            field = "Title"
        elif fieldIndex == 1:  # 按作者
            field = "Author"
        elif fieldIndex == 2:  # 按关键字
            QMessageBox.information(self, "提示", "无该项查询内容，请重新选择查询内容！")
            return
        elif fieldIndex == 3:  # 按主要内容
            field = 'Summary'
        if self.isAll == True:  # 载入后首次查询
            self.isAll = False
        condition = "\'%" + condition + "%\'"
        sen = "select Title, Author, Pages, Origin, Summary, MD5 from SongBook where %s like %s" % (
            field, condition)
        self.queryModel.setQuery(sen)
        self.baseUI.lab_QueryTotal.setText("共查询到 %d 条信息" % (self.queryModel.rowCount()))

    #处理下载按钮按下，发射下载信号到主窗口，携带三个参数表名、MD5、标题
    def on_Download_SignalEmit(self):
        index =  self.baseUI.tableView.currentIndex().row()
        if index < 0:
            return
        print("下载按钮信号----->"+str(index))
        #获取选中记录
        curRec = self.queryModel.record(index)
        MD5 = curRec.value("MD5")
        Title = curRec.value("Title")
        print(Title)
        self.signal_Download.emit("SongBook",MD5,Title)

#封装会议论文
class DBDocumentHYLW(DBDocumentBase):
    def __init__(self,DB):
        super().__init__(DB)
        self.win = QWidget()
        self.UI = Ui_ConferencePaperDetail()
        self.UI.setupUi(self.win)
        self.baseUI.detailLayout.addWidget(self.win)

        # 获得总记录数,总页数
        self.totalRecord = self.getTotalRecord()
        self.totalPages = self.caculateTotoalPage()
        self.baseUI.lab_Record.setText(str(self.totalRecord))
        self.baseUI.lab_CurrentPage.setText(str(self.currentPage))
        self.baseUI.lab_TotalPages.setText(str(self.totalPages))

        self.recordQuery(0)

        self.queryModel.setHeaderData(3, Qt.Horizontal, "标题")
        self.baseUI.tableView.setColumnWidth(3, 400)
        self.queryModel.setHeaderData(13, Qt.Horizontal, "论文集名")
        self.queryModel.setHeaderData(1, Qt.Horizontal, "作者")
        self.queryModel.setHeaderData(2, Qt.Horizontal, "发表年份")
        self.queryModel.setHeaderData(6, Qt.Horizontal, "页数")
        self.queryModel.setHeaderData(5, Qt.Horizontal, "会议名称")
        self.queryModel.setHeaderData(12, Qt.Horizontal, "主办机构")
        self.queryModel.setHeaderData(9, Qt.Horizontal, "关键字")
        self.queryModel.setHeaderData(10, Qt.Horizontal, "摘要")

        self.baseUI.tableView.setColumnHidden(0, True)
        self.baseUI.tableView.setColumnHidden(4, True)
        self.baseUI.tableView.setColumnHidden(7, True)
        self.baseUI.tableView.setColumnHidden(8, True)
        self.baseUI.tableView.setColumnHidden(11, True)
        self.baseUI.tableView.setColumnHidden(14, True)

        self.mapper.setModel(self.queryModel)
        self.mapper.addMapping(self.UI.lineEdit_Title, 3)
        self.mapper.addMapping(self.UI.lineEdit_TertiaryTitle, 8)
        self.mapper.addMapping(self.UI.lineEdit_PaperCollection, 13)
        self.mapper.addMapping(self.UI.lineEdit_Author, 1)
        self.mapper.addMapping(self.UI.lineEdit_Year, 2)
        self.mapper.addMapping(self.UI.lineEdit_AuthorAffiliation, 11)
        self.mapper.addMapping(self.UI.lineEdit_Pages, 6)
        self.mapper.addMapping(self.UI.lineEdit_SecondaryTitle, 5)
        self.mapper.addMapping(self.UI.lineEdit_PlacePublished, 7)
        self.mapper.addMapping(self.UI.lineEdit_HostUnit, 12)
        self.mapper.addMapping(self.UI.lineEdit_Keywords, 9)
        self.mapper.addMapping(self.UI.textEdit_Abstract, 10)
        self.mapper.toFirst()


    # 执行查询模型
    def recordQuery(self, Index):
        try:
            szQurey = ("select * from ConferencePaper limit %d,%d " % (Index, self.eachPageRecord))
            self.queryModel.setQuery(szQurey)
        except Exception:
            print(self.objectName() + Exception)


    def getTotalRecord(self):
        try:
            self.query.exec("select * from ConferencePaper")
            self.query.last()
            return self.query.at() + 1
        except Exception:
            print(Exception)

    # 设置每页显示记录数量
    def get_EachRecordOfPage(self):
        text = self.baseUI.comBox_EachRecordOfPage.currentText()
        print(text)
        self.eachPageRecord = int(text)
        self.totalPages = self.caculateTotoalPage()
        self.currentPage = 1
        self.recordQuery(0)
        self.baseUI.lab_CurrentPage.setText(str(self.currentPage))
        self.baseUI.lab_TotalPages.setText(str(self.totalPages))
        self.mapper.toFirst()


    # 下一页
    def on_NextPage(self):
        if self.currentPage + 1 > self.totalPages:
            return
        index = (self.currentPage) * self.eachPageRecord
        self.recordQuery(index)
        self.currentPage += 1
        self.baseUI.lab_CurrentPage.setText(str(self.currentPage))


    # 上一页
    def on_PrePage(self):
        if self.currentPage == 1:
            return
        index = (self.currentPage - 2) * self.eachPageRecord
        self.recordQuery(index)
        self.currentPage -= 1
        self.baseUI.lab_CurrentPage.setText(str(self.currentPage))


    # 跳转页
    def on_Goto(self):
        text = self.baseUI.lineEdit_WhichPage.text().strip()
        if text == "":
            return
        if not text.isdigit():
            QMessageBox.information(self, "提示", "请输入数字!")
            return
        pageIndex = int(text)
        if pageIndex < 1 or pageIndex > self.totalPages:
            QMessageBox.information(self, "提示", "没有指定的页面，请重新输入")
            return
        index = (pageIndex - 1) * self.eachPageRecord
        self.recordQuery(index)
        self.currentPage = pageIndex
        self.baseUI.lab_CurrentPage.setText(str(self.currentPage))

    # 条件查询
    def on_BtnQuery(self):
        condition = self.baseUI.lineEdit_Condition.text().strip()
        if condition == "":
            return
        fieldIndex = self.baseUI.comboBox_SearchBy.currentIndex()
        # print(fieldIndex,condition)
        if fieldIndex == 0:  # 按标题
            pass
            field = "Title"
        elif fieldIndex == 1:  # 按作者
            pass
            field = "Author"
        elif fieldIndex == 2:  # 按关键字
            field = 'Keywords'
        elif fieldIndex == 3:  # 按主要内容
            field = "Abstract"
        if self.isAll == True:  # 载入后首次查询
            self.isAll = False
        condition = "\'%" + condition + "%\'"
        sen = "select * from ConferencePaper where %s like %s" % (field, condition)
        self.queryModel.setQuery(sen)
        self.baseUI.lab_QueryTotal.setText("共查询到 %d 条信息" % (self.queryModel.rowCount()))

    #处理下载按钮按下，发射下载信号到主窗口，携带三个参数表名、MD5、标题
    def on_Download_SignalEmit(self):
        index =  self.baseUI.tableView.currentIndex().row()
        if index < 0:
            return
        print("下载按钮信号----->"+str(index))
        #获取选中记录
        curRec = self.queryModel.record(index)
        MD5 = curRec.value("MD5")
        Title = curRec.value("Title")
        print(Title)
        self.signal_Download.emit("ConferencePaper",MD5,Title)

#封装学位论文
class DBDocumentXWLW(DBDocumentBase):
    def __init__(self,DB):
        super().__init__(DB)
        self.win = QWidget()
        self.UI = Ui_DissertationDetail()
        self.UI.setupUi(self.win)
        self.baseUI.detailLayout.addWidget(self.win)

# 获得总记录数,总页数
        self.totalRecord = self.getTotalRecord()
        self.totalPages = self.caculateTotoalPage()
        self.baseUI.lab_Record.setText(str(self.totalRecord))
        self.baseUI.lab_CurrentPage.setText(str(self.currentPage))
        self.baseUI.lab_TotalPages.setText(str(self.totalPages))

        self.recordQuery(0)

        self.queryModel.setHeaderData(0, Qt.Horizontal, "标题")
        self.baseUI.tableView.setColumnWidth(0, 450)
        self.queryModel.setHeaderData(1, Qt.Horizontal, "作者")
        self.queryModel.setHeaderData(2, Qt.Horizontal, "指导老师")
        self.queryModel.setHeaderData(3, Qt.Horizontal, "作者单位")
        self.queryModel.setHeaderData(4, Qt.Horizontal, "学位层级")
        self.queryModel.setHeaderData(5, Qt.Horizontal, "发表年份")
        self.queryModel.setHeaderData(6, Qt.Horizontal, "关键字")
        self.queryModel.setHeaderData(7, Qt.Horizontal, "摘要")

        self.baseUI.tableView.setColumnHidden(8, True)

        self.mapper.setModel(self.queryModel)
        self.mapper.addMapping(self.UI.lineEdit_Title, 0)
        self.mapper.addMapping(self.UI.lineEdit_Author, 1)
        self.mapper.addMapping(self.UI.lineEdit_TertiaryAuthor, 2)
        self.mapper.addMapping(self.UI.lineEdit_Publisher, 3)
        self.mapper.addMapping(self.UI.lineEdit_DegreeLevel, 4)
        self.mapper.addMapping(self.UI.lineEdit_Year,5)
        self.mapper.addMapping(self.UI.lineEdit_Keywords,6)
        self.mapper.addMapping(self.UI.textEdit_Abstract,7)

        self.mapper.toFirst()

    # 执行查询模型
    def recordQuery(self, Index):
        try:
            szQurey = ("select Title, Author,TertiaryAuthor,Publisher,DegreeLevel,Year, Keyword, Abstract, MD5 from Dissertation limit %d,%d" % (
                Index, self.eachPageRecord))
            self.queryModel.setQuery(szQurey)
        except Exception:
            print(self.objectName() + Exception)

    def getTotalRecord(self):
        try:
            self.query.exec("select * from Dissertation")
            self.query.last()
            return self.query.at() + 1
        except Exception:
            print(Exception)

    # 设置每页显示记录数量
    def get_EachRecordOfPage(self):
        text = self.baseUI.comBox_EachRecordOfPage.currentText()
        print(text)
        self.eachPageRecord = int(text)
        self.totalPages = self.caculateTotoalPage()
        self.currentPage = 1
        self.recordQuery(0)
        self.baseUI.lab_CurrentPage.setText(str(self.currentPage))
        self.baseUI.lab_TotalPages.setText(str(self.totalPages))
        self.mapper.toFirst()

    # 下一页
    def on_NextPage(self):
        if self.currentPage + 1 > self.totalPages:
            return
        index = (self.currentPage ) * self.eachPageRecord
        self.recordQuery(index)
        self.currentPage += 1
        self.baseUI.lab_CurrentPage.setText(str(self.currentPage))

    # 上一页
    def on_PrePage(self):
        if self.currentPage == 1:
            return
        index = (self.currentPage - 2) * self.eachPageRecord
        self.recordQuery(index)
        self.currentPage -= 1
        self.baseUI.lab_CurrentPage.setText(str(self.currentPage))

    # 跳转页
    def on_Goto(self):
        text = self.baseUI.lineEdit_WhichPage.text().strip()
        if text == "":
            return
        if not text.isdigit():
            QMessageBox.information(self, "提示", "请输入数字!")
            return
        pageIndex = int(text)
        if pageIndex < 1 or pageIndex > self.totalPages:
            QMessageBox.information(self, "提示", "没有指定的页面，请重新输入")
            return
        index = (pageIndex - 1) * self.eachPageRecord
        self.recordQuery(index)
        self.currentPage = pageIndex
        self.baseUI.lab_CurrentPage.setText(str(self.currentPage))

    # 条件查询
    def on_BtnQuery(self):
        condition = self.baseUI.lineEdit_Condition.text().strip()
        if condition == "":
            return
        fieldIndex = self.baseUI.comboBox_SearchBy.currentIndex()
        # print(fieldIndex,condition)
        if fieldIndex == 0:  # 按标题
            pass
            field = "Title"
        elif fieldIndex == 1:  # 按作者
            pass
            field = "Author"
        elif fieldIndex == 2:  # 按关键字
            field = 'Keyword'
        elif fieldIndex == 3:  # 按主要内容
            field = "Abstract"
        if self.isAll == True:  # 载入后首次查询
            self.isAll = False
        condition = "\'%" + condition + "%\'"
        sen = "select Title, Author,TertiaryAuthor,Publisher,DegreeLevel,Year, Keyword, Abstract, MD5 from Dissertation where %s like %s" % (field, condition)
        self.queryModel.setQuery(sen)
        self.baseUI.lab_QueryTotal.setText("共查询到 %d 条信息" % (self.queryModel.rowCount()))

    #处理下载按钮按下，发射下载信号到主窗口，携带三个参数表名、MD5、标题
    def on_Download_SignalEmit(self):
        index =  self.baseUI.tableView.currentIndex().row()
        if index < 0:
            return
        print("下载按钮信号----->"+str(index))
        #获取选中记录
        curRec = self.queryModel.record(index)
        MD5 = curRec.value("MD5")
        Title = curRec.value("Title")
        print(Title)
        self.signal_Download.emit("Dissertation",MD5,Title)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    DBSourceView = DBDocumentHYLW()
    DBSourceView.show()
    sys.exit(app.exec_())