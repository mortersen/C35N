# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_ComicBook.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_comicBook(object):
    def setupUi(self, comicBook):
        comicBook.setObjectName("comicBook")
        comicBook.resize(400, 300)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(comicBook)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_PagePre = QtWidgets.QPushButton(comicBook)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_PagePre.sizePolicy().hasHeightForWidth())
        self.btn_PagePre.setSizePolicy(sizePolicy)
        self.btn_PagePre.setMinimumSize(QtCore.QSize(32, 0))
        self.btn_PagePre.setStyleSheet("border:none;")
        self.btn_PagePre.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icon/arrowleft.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_PagePre.setIcon(icon)
        self.btn_PagePre.setIconSize(QtCore.QSize(32, 64))
        self.btn_PagePre.setObjectName("btn_PagePre")
        self.horizontalLayout_2.addWidget(self.btn_PagePre)
        self.picLayout = QtWidgets.QHBoxLayout()
        self.picLayout.setObjectName("picLayout")
        self.lab_PicShow = QtWidgets.QLabel(comicBook)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(9)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lab_PicShow.sizePolicy().hasHeightForWidth())
        self.lab_PicShow.setSizePolicy(sizePolicy)
        self.lab_PicShow.setText("")
        self.lab_PicShow.setObjectName("lab_PicShow")
        self.picLayout.addWidget(self.lab_PicShow)
        self.horizontalLayout_2.addLayout(self.picLayout)
        self.btn_PageNext = QtWidgets.QPushButton(comicBook)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_PageNext.sizePolicy().hasHeightForWidth())
        self.btn_PageNext.setSizePolicy(sizePolicy)
        self.btn_PageNext.setMinimumSize(QtCore.QSize(32, 64))
        self.btn_PageNext.setStyleSheet("border:none;")
        self.btn_PageNext.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Icon/arrowright.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_PageNext.setIcon(icon1)
        self.btn_PageNext.setIconSize(QtCore.QSize(32, 64))
        self.btn_PageNext.setObjectName("btn_PageNext")
        self.horizontalLayout_2.addWidget(self.btn_PageNext)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 9)
        self.horizontalLayout_2.setStretch(2, 1)

        self.retranslateUi(comicBook)
        QtCore.QMetaObject.connectSlotsByName(comicBook)

    def retranslateUi(self, comicBook):
        _translate = QtCore.QCoreApplication.translate
        comicBook.setWindowTitle(_translate("comicBook", "Form"))
        self.lab_PicShow.setToolTip(_translate("comicBook", "左键上一页，右键下一页"))
import img_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    comicBook = QtWidgets.QWidget()
    ui = Ui_comicBook()
    ui.setupUi(comicBook)
    comicBook.show()
    sys.exit(app.exec_())
