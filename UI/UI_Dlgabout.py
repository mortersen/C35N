# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_Dlgabout.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_About(object):
    def setupUi(self, About):
        About.setObjectName("About")
        About.setWindowModality(QtCore.Qt.ApplicationModal)
        About.resize(366, 153)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icon/info.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        About.setWindowIcon(icon)
        self.pushButton = QtWidgets.QPushButton(About)
        self.pushButton.setGeometry(QtCore.QRect(270, 120, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.groupBox = QtWidgets.QGroupBox(About)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 341, 101))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(120, 50, 211, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 9, 81, 81))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/Icon/goodFish.PNG"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(120, 20, 211, 21))
        self.label.setObjectName("label")
        self.groupBox.raise_()
        self.pushButton.raise_()

        self.retranslateUi(About)
        self.pushButton.clicked.connect(About.close)
        QtCore.QMetaObject.connectSlotsByName(About)

    def retranslateUi(self, About):
        _translate = QtCore.QCoreApplication.translate
        About.setWindowTitle(_translate("About", "About ..."))
        self.pushButton.setText(_translate("About", "OK"))
        self.label_2.setText(_translate("About", "泉州师范学院"))
        self.label.setText(_translate("About", "陈三五娘文献数据库V1.0"))
import img_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    About = QtWidgets.QDialog()
    ui = Ui_About()
    ui.setupUi(About)
    About.show()
    sys.exit(app.exec_())
