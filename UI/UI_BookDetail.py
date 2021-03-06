# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_BookDetail.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_BookDetail(object):
    def setupUi(self, BookDetail):
        BookDetail.setObjectName("BookDetail")
        BookDetail.resize(310, 336)
        self.verticalLayout = QtWidgets.QVBoxLayout(BookDetail)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(BookDetail)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.lineEdit_Title = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_Title.setObjectName("lineEdit_Title")
        self.horizontalLayout_2.addWidget(self.lineEdit_Title)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.lineEdit_SecondaryTitle = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_SecondaryTitle.setObjectName("lineEdit_SecondaryTitle")
        self.horizontalLayout_3.addWidget(self.lineEdit_SecondaryTitle)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.lineEdit_Author = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_Author.setObjectName("lineEdit_Author")
        self.horizontalLayout_4.addWidget(self.lineEdit_Author)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.lineEdit__Pages = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit__Pages.setObjectName("lineEdit__Pages")
        self.horizontalLayout_5.addWidget(self.lineEdit__Pages)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.lineEdit_Year = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_Year.setObjectName("lineEdit_Year")
        self.horizontalLayout_5.addWidget(self.lineEdit_Year)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        self.lineEdit__Publisher = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit__Publisher.setObjectName("lineEdit__Publisher")
        self.horizontalLayout_6.addWidget(self.lineEdit__Publisher)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_7.addWidget(self.label_7)
        self.lineEdit_Keywords = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_Keywords.setObjectName("lineEdit_Keywords")
        self.horizontalLayout_7.addWidget(self.lineEdit_Keywords)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_8.addWidget(self.label_8)
        self.textEdit_Abstract = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit_Abstract.setObjectName("textEdit_Abstract")
        self.horizontalLayout_8.addWidget(self.textEdit_Abstract)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.verticalLayout.addWidget(self.groupBox)
        self.verticalLayout.setStretch(0, 9)

        self.retranslateUi(BookDetail)
        QtCore.QMetaObject.connectSlotsByName(BookDetail)

    def retranslateUi(self, BookDetail):
        _translate = QtCore.QCoreApplication.translate
        BookDetail.setWindowTitle(_translate("BookDetail", "Form"))
        self.groupBox.setTitle(_translate("BookDetail", "图书信息"))
        self.label.setText(_translate("BookDetail", "书  名："))
        self.label_3.setText(_translate("BookDetail", "丛书名："))
        self.label_2.setText(_translate("BookDetail", "作  者："))
        self.label_5.setText(_translate("BookDetail", "页  数："))
        self.label_4.setText(_translate("BookDetail", "出版年份："))
        self.label_6.setText(_translate("BookDetail", "出版社："))
        self.label_7.setText(_translate("BookDetail", "关键字："))
        self.label_8.setText(_translate("BookDetail", "摘  要："))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BookDetail = QtWidgets.QWidget()
    ui = Ui_BookDetail()
    ui.setupUi(BookDetail)
    BookDetail.show()
    sys.exit(app.exec_())
