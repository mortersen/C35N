# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_DissertationDetail.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DissertationDetail(object):
    def setupUi(self, DissertationDetail):
        DissertationDetail.setObjectName("DissertationDetail")
        DissertationDetail.resize(363, 437)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(DissertationDetail)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox = QtWidgets.QGroupBox(DissertationDetail)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.lineEdit_Title = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_Title.setObjectName("lineEdit_Title")
        self.horizontalLayout_3.addWidget(self.lineEdit_Title)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit_Author = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_Author.setObjectName("lineEdit_Author")
        self.horizontalLayout.addWidget(self.lineEdit_Author)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.lineEdit_TertiaryAuthor = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_TertiaryAuthor.setObjectName("lineEdit_TertiaryAuthor")
        self.horizontalLayout_5.addWidget(self.lineEdit_TertiaryAuthor)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.lineEdit_Publisher = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_Publisher.setObjectName("lineEdit_Publisher")
        self.horizontalLayout_4.addWidget(self.lineEdit_Publisher)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        self.lineEdit_DegreeLevel = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_DegreeLevel.setObjectName("lineEdit_DegreeLevel")
        self.horizontalLayout_6.addWidget(self.lineEdit_DegreeLevel)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit_Year = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_Year.setObjectName("lineEdit_Year")
        self.horizontalLayout_2.addWidget(self.lineEdit_Year)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_7.addWidget(self.label_7)
        self.lineEdit_Keywords = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_Keywords.setObjectName("lineEdit_Keywords")
        self.horizontalLayout_7.addWidget(self.lineEdit_Keywords)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textEdit_Abstract = QtWidgets.QTextEdit(self.groupBox_2)
        self.textEdit_Abstract.setObjectName("textEdit_Abstract")
        self.verticalLayout.addWidget(self.textEdit_Abstract)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.verticalLayout_3.addWidget(self.groupBox)

        self.retranslateUi(DissertationDetail)
        QtCore.QMetaObject.connectSlotsByName(DissertationDetail)

    def retranslateUi(self, DissertationDetail):
        _translate = QtCore.QCoreApplication.translate
        DissertationDetail.setWindowTitle(_translate("DissertationDetail", "Form"))
        self.groupBox.setTitle(_translate("DissertationDetail", "学位论文信息"))
        self.label_3.setText(_translate("DissertationDetail", "标    题："))
        self.label.setText(_translate("DissertationDetail", "作    者："))
        self.label_5.setText(_translate("DissertationDetail", "指导教师："))
        self.label_4.setText(_translate("DissertationDetail", "作者单位："))
        self.label_6.setText(_translate("DissertationDetail", "学位层级："))
        self.label_2.setText(_translate("DissertationDetail", "发表年份："))
        self.label_7.setText(_translate("DissertationDetail", "关 键 字："))
        self.groupBox_2.setTitle(_translate("DissertationDetail", "摘   要"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DissertationDetail = QtWidgets.QWidget()
    ui = Ui_DissertationDetail()
    ui.setupUi(DissertationDetail)
    DissertationDetail.show()
    sys.exit(app.exec_())
