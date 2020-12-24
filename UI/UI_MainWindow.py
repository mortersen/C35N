# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(800, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icon/goodFish.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mainWindow.setWindowIcon(icon)
        self.workView = QtWidgets.QWidget(mainWindow)
        self.workView.setObjectName("workView")
        mainWindow.setCentralWidget(self.workView)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(mainWindow)
        self.toolBar.setObjectName("toolBar")
        mainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.action_DB = QtWidgets.QAction(mainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Icon/home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_DB.setIcon(icon1)
        self.action_DB.setObjectName("action_DB")
        self.action_SearchContext = QtWidgets.QAction(mainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/Icon/query.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_SearchContext.setIcon(icon2)
        self.action_SearchContext.setObjectName("action_SearchContext")
        self.action_Setting = QtWidgets.QAction(mainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/Icon/setup.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Setting.setIcon(icon3)
        self.action_Setting.setObjectName("action_Setting")
        self.action_comicBook = QtWidgets.QAction(mainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/Icon/address.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_comicBook.setIcon(icon4)
        self.action_comicBook.setObjectName("action_comicBook")
        self.toolBar.addAction(self.action_comicBook)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_DB)
        self.toolBar.addAction(self.action_SearchContext)
        self.toolBar.addAction(self.action_Setting)
        self.toolBar.addSeparator()

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "陈三五娘数据库系统"))
        self.toolBar.setWindowTitle(_translate("mainWindow", "toolBar"))
        self.action_DB.setText(_translate("mainWindow", "数据库"))
        self.action_DB.setToolTip(_translate("mainWindow", "打开数据库视窗"))
        self.action_SearchContext.setText(_translate("mainWindow", "SearchContext"))
        self.action_SearchContext.setToolTip(_translate("mainWindow", "数据库检索"))
        self.action_Setting.setText(_translate("mainWindow", "Setting"))
        self.action_Setting.setToolTip(_translate("mainWindow", "系统设置"))
        self.action_comicBook.setText(_translate("mainWindow", "comicBook"))
        self.action_comicBook.setToolTip(_translate("mainWindow", "《陈三五娘（彩绘连环画）》全本 绘画：孔继昭"))
import img_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
