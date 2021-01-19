from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from UI.UI_ComicBook import Ui_comicBook


picPath=[":/Icon/la1.jpg",":/Icon/la2.jpg",":/Icon/la3.jpg",":/Icon/la4.jpg",
         ":/Icon/la5.jpg",":/Icon/la6.jpg",":/Icon/la7.jpg",":/Icon/la8.jpg",":/Icon/la9.jpg",
         ":/Icon/la10.jpg",":/Icon/la11.jpg",":/Icon/la12.jpg",":/Icon/la13.jpg",":/Icon/la14.jpg",
         ":/Icon/la15.jpg",":/Icon/la16.jpg"]

class ComicBook(QWidget):
    def __init__(self):
        super().__init__()
        self.UI = Ui_comicBook()
        self.UI.setupUi(self)
        self.width = QApplication.desktop().width() * 0.6
        self.height = self.width*692/920
        self.currentPic = -1
        self.UI.lab_PicShow.setAlignment(Qt.AlignCenter)
        self.on_comic_btnPageNext()

        self.UI.btn_PageNext.released.connect(self.on_comic_btnPageNext)
        self.UI.btn_PagePre.released.connect(self.on_comic_btnPagePre)


    #连环画下一页
    def on_comic_btnPageNext(self):
        temp = self.currentPic + 1
        if temp > 15:
            self.currentPic = 0
        else:
            self.currentPic = temp
        pic = QPixmap(picPath[self.currentPic]).scaled(self.width,self.height)
        self.UI.lab_PicShow.setPixmap(pic)

    #连环画上一页
    def on_comic_btnPagePre(self):
        temp = self.currentPic - 1
        if temp < 0:
            self.currentPic = 15
        else:
            self.currentPic = temp
        pic = QPixmap(picPath[self.currentPic]).scaled(self.width,self.height)
        self.UI.lab_PicShow.setPixmap(pic)


    #鼠标事件
    def mousePressEvent(self,event):
        if event.buttons() == Qt.LeftButton:
            self.UI.btn_PageNext.released.emit()
        elif event.buttons() == Qt.RightButton:
            self.UI.btn_PagePre.released.emit()
        else:
            return