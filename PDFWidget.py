import sys
from threading import Thread
from PyQt5.QtWidgets import (QWidget,QApplication,QListView,QListWidget,QLabel,
                                QVBoxLayout,QListWidgetItem,QFileDialog,QMessageBox
                             )
from PyQt5.QtGui import QImage,QPixmap
from PyQt5.QtCore import QSize,Qt,pyqtSignal

from UI.UI_ReadPDF import Ui_widgetReadPDF

import fitz
import os
import win32api
import win32print

#主显示界面辅助类
class ShowImageWidget(QLabel):
    def __init__(self, *args, **kwargs):
        super(ShowImageWidget, self).__init__(*args, **kwargs)  # 继承父类
        self.setMouseTracking(True)  # 保证得到鼠标信息
        self.m_pixmap = None         # 原始QPixmap图像
        self.m_factor = 1            # 缩放因子

    # 设置显示图片
    def setpix(self, pix):
        self.m_pixmap = pix
        self.setPixmap(pix)

    # 鼠标滚轮事件
    def wheelEvent(self, ev):
        if ev.modifiers() & Qt.ControlModifier:  # 鼠标左键及Ctrl同时按下
            if ev.angleDelta().y() > 0:
                self.m_factor = self.m_factor * 1.05
            else:
                if self.m_factor > 0.2:
                    self.m_factor = self.m_factor * 0.95
            width = int(self.m_pixmap.width() * self.m_factor)
            height = int(self.m_pixmap.height() * self.m_factor)
            self.setPixmap(self.m_pixmap.scaled(QSize(width, height)))

class WidgetPDF(QWidget,Ui_widgetReadPDF):


    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.bOpened = False  # 文档是否打开
        self.pdfName = "./111.pdf"  # 文档名
        self.nPages = 0  # 文档总页数
        self.nCurr = -1  # 当前文档页码
        self.docDoc = None  # 当前pymupdf文档对象
        #self.bModified = False  # 是否已编辑过
        #self.bShrink = False  # 列表框收缩标志
        self.nMaxPages = 32  # 最大显示页数
        self.IMAGE_SIZE = QSize(147, 208)  # A4纸210*297, 乘0.7
        self.LISTITEM_SIZE = QSize(160, 250)

        self.iniUi()

    # 初始化listWidget
    def iniUi(self):

        self.listWidget.setViewMode(QListWidget.IconMode)
        self.listWidget.setIconSize(self.IMAGE_SIZE)  # Icon 大小
        self.listWidget.setMovement(QListView.Static)  # Listview显示状态
        self.listWidget.setResizeMode(QListView.Adjust)
        self.listWidget.setSpacing(12)  # 间距大小
        self.listWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        #self.showMaximized()

    # 设置窗口菜单控件状态
    def set_window_status(self):
        pass

    # 初始化事件
    def init_event_plot(self):
        #缩略图单击事件
        self.listWidget.clicked.connect(self.onclicked_listWidget)
        # 另存为
        self.actionSaveAs.released.connect(self.onclicked_actionSaveAs)
        # 打印pdf文档
        self.actionPrint.released.connect(self.onclicked_actionPrint)


    # 打开文档处理
    def open_doc(self):
        if self.pdfName:
            #row = self.cur.execute("SELECT FileBinary From BookFile where ID = ?;", (3,))
            #self.pdfName = row.fetchone()[0]
            #self.docDoc = fitz.open(None,row.fetchone()[0],'pdf')
            self.docDoc = fitz.open(self.pdfName)
            self.bOpened = True  # 设置文件打开
            #self.labelFileName.setText(self.pdfName)
            self.refresh_listWidget()
            # 显示第一页
            self.nCurr = 0
            self.show_current_page()


# 刷新listWidget

    #加载左侧缩略图
    def refresh_listWidget(self):
        if not self.bOpened:
            return
        self.set_window_status()    # 刷新菜单状态
        self.listWidget.clear()
        self.nPages = self.docDoc.pageCount
        if self.nPages <= 0:
            return
        for i in range(0, self.nPages):
            page = self.docDoc[i]  # 当前页
            zoom = int(30)
            rotate = int(0)
            trans = fitz.Matrix(zoom / 100.0, zoom / 100.0).preRotate(rotate)
            pix = page.getPixmap(matrix=trans, alpha=False)
            fmt = QImage.Format_RGBA8888 if pix.alpha else QImage.Format_RGB888
            qtimg = QImage(pix.samples, pix.width, pix.height, pix.stride, fmt)  # 当前页转换为QImage对象

            widget = QWidget(self)
            vboxLayout = QVBoxLayout()
            widget.setLayout(vboxLayout)
            listItem = QListWidgetItem(self.listWidget)  # 列表控件项
            listItem.setSizeHint(self.LISTITEM_SIZE)
            labelimg = QLabel(widget)
            labelimg.setPixmap(QPixmap.fromImage(qtimg).scaled(self.IMAGE_SIZE))  # 显示在一个QLabel上
            labelimg.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
            labeltxt = QLabel(widget)  # 页码序号
            labeltxt.setText("%d" % int(i + 1))
            labeltxt.setFixedHeight(30)
            labeltxt.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
            labeltxt.setWordWrap(True)
            vboxLayout.addWidget(labelimg)  # 图片和页码加入vboxLayout
            vboxLayout.addWidget(labeltxt)
            widget.setFixedHeight(self.LISTITEM_SIZE.height())

            self.listWidget.setItemWidget(listItem, widget)  # 显示到listWidget中
        listItem = QListWidgetItem(self.listWidget)  # listWidget最后一项显示异常,因此多加一项,需要再排查优化
        listItem.setSizeHint(QSize(0, 0))

    # 显示当前页
    def show_current_page(self):
        if not self.bOpened or self.nPages <= 0:
            return
        if self.nCurr < 0:
            return
        if self.nCurr >= self.nPages:
            self.nCurr = self.nPages - 1

        # 得到当前页
        page = self.docDoc[self.nCurr]
        zoom = int(200)
        rotate = int(0)
        trans = fitz.Matrix(zoom / 100.0, zoom / 100.0).preRotate(rotate)
        pix = page.getPixmap(matrix=trans, alpha=False)
        fmt = QImage.Format_RGBA8888 if pix.alpha else QImage.Format_RGB888
        qtimg = QImage(pix.samples, pix.width, pix.height, pix.stride, fmt) # 当前页转换为QImage对象
        # 准备显示控件
        widget = QWidget(self)
        vboxLayout = QVBoxLayout()
        labelimg = ShowImageWidget(widget)  # 使用一个自定义的QLabel控件
        labelimg.setpix(QPixmap.fromImage(qtimg).scaled(QSize(pix.width, pix.height)))
        labelimg.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        vboxLayout.addWidget(labelimg)
        widget.setLayout(vboxLayout)
        self.showArea.setWidget(widget)    # 添加到showArea

        # 更新状态栏页码
        self.label_FileStatus.setText("第 %d 页/共 %d 页" % (int(self.nCurr + 1), self.nPages))

    # 缩略图列表控件单击事件
    def onclicked_listWidget(self, index):
        self.nCurr = index.row()
        self.show_current_page()

    # 另存为
    def onclicked_actionSaveAs(self):
        if not self.bOpened:
            return
        filePath, fname = os.path.split(os.path.abspath(self.pdfName))
        newfileName, ok = QFileDialog.getSaveFileName(self, "文件另存为", filePath, "*.pdf")
        if newfileName:
            self.docDoc.save(newfileName)
            #先关闭当前文档
            self.bOpened = False  # 文档是否打开
            self.bModified = False
            self.pdfName = None  # 文档名
            self.nPages = 0  # 文档总页数
            self.nCurr = -1  # 当前文档页码
            self.docDoc = None  # 当前pymupdf文档对象
            #再打开新文档
            self.pdfName = newfileName
            self.labelFileName.setText(self.pdfName)
            self.docDoc = fitz.open(self.pdfName)
            self.bOpened = True  # 设置文件打开
            self.refresh_listWidget()
            # 显示第一页
            self.nCurr = 0
            self.show_current_page()

# 打印pdf文档

    #打印
    def onclicked_actionPrint(self):
        #if not self.bOpened :
        #    return
        #if self.bModified:
        #    QMessageBox.information(self, "Information", "已修改，请先保存", QMessageBox.Ok)
        #    return

        win32api.ShellExecute(
            0,
            "print",
            self.pdfName,
            #
            # If this is None, the default printer will
            # be used anyway.
            #
            '/d:"%s"' % win32print.GetDefaultPrinter(),
            ".",
            0
        )

class WidgetPDFStream(WidgetPDF):
    signal_SaveOver = pyqtSignal(str)

    def __init__(self,stream,title):
        super().__init__()
        #print(type(stream))
        self.stream = bytes(stream)
        self.docTitle = title

        self.init_event_plot()

        self.signal_SaveOver.connect(self.onSignalSaveOver)

        self.open_docByStream()

    def open_docByStream(self):
        try:
            #row = self.cur.execute("SELECT FileBinary From BookFile where ID = ?;", (3,))
            #self.pdfName = row.fetchone()[0]
            #print("OPen PDF:::")
            #print(type(self.stream))
            self.docDoc = fitz.open(None,self.stream,'PDF')
                #self.docDoc = fitz.open(self.pdfName)
            #print(self.docDoc)
            self.bOpened = True  # 设置文件打开
                #self.labelFileName.setText(self.pdfName)
            self.refresh_listWidget()
                # 显示第一页
            self.nCurr = 0
            self.show_current_page()
        except:
            pass
    #打印
    def onclicked_actionPrint(self):
        #if not self.bOpened :
        #    return
        #if self.bModified:
        #    QMessageBox.information(self, "Information", "已修改，请先保存", QMessageBox.Ok)
        #    return
        file = open("./temp.pdf",'wb')
        file.write(self.stream)
        file.close()

        print("stream print")
        win32api.ShellExecute(
            0,
            "print",
            "./temp.pdf",
            #
            # If this is None, the default printer will
            # be used anyway.
            #
            '/d:"%s"' % win32print.GetDefaultPrinter(),
            ".",
            0
        )

   # 另存为

    def onclicked_actionSaveAs(self):

        newfileName, ok = QFileDialog.getSaveFileName(self, "文件另存为", os.getcwd()+"\\"+self.docTitle+".pdf", "*.pdf")
        if ok:
            #self.docDoc.save(newfileName)
            def func():
                self.docDoc.save(newfileName)
                self.signal_SaveOver.emit(newfileName)
            saveThread = Thread(target=func)
            saveThread.start()

        else:
            return

    #槽函数，提示另存成功
    def onSignalSaveOver(self,name):
        QMessageBox.information(self, "提示", name + "文件另存为成功！")

if __name__ == '__main__':
    mainAPP = QApplication(sys.argv)
    mainWin = WidgetPDF()
    #mainWin = WidgetPDFStream(1,2,3)
    mainWin.show()

    sys.exit(mainAPP.exec_())