# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_SouthSoundOperaDetail.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SouthSoundOperaDetail(object):
    def setupUi(self, SouthSoundOperaDetail):
        SouthSoundOperaDetail.setObjectName("SouthSoundOperaDetail")
        SouthSoundOperaDetail.resize(333, 374)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(SouthSoundOperaDetail)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(SouthSoundOperaDetail)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit_Title = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_Title.setObjectName("lineEdit_Title")
        self.horizontalLayout.addWidget(self.lineEdit_Title)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit_Author = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_Author.setObjectName("lineEdit_Author")
        self.horizontalLayout_2.addWidget(self.lineEdit_Author)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.lineEdit_Pages = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_Pages.setObjectName("lineEdit_Pages")
        self.horizontalLayout_3.addWidget(self.lineEdit_Pages)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_3)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.lineEdit_Origin = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_Origin.setObjectName("lineEdit_Origin")
        self.horizontalLayout_4.addWidget(self.lineEdit_Origin)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.verticalLayout.setStretch(0, 2)
        self.verticalLayout.setStretch(1, 2)
        self.verticalLayout.setStretch(2, 2)
        self.verticalLayout.setStretch(3, 4)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.verticalLayout_2.setStretch(0, 6)

        self.retranslateUi(SouthSoundOperaDetail)
        QtCore.QMetaObject.connectSlotsByName(SouthSoundOperaDetail)

    def retranslateUi(self, SouthSoundOperaDetail):
        _translate = QtCore.QCoreApplication.translate
        SouthSoundOperaDetail.setWindowTitle(_translate("SouthSoundOperaDetail", "Form"))
        self.groupBox.setTitle(_translate("SouthSoundOperaDetail", "南音曲谱信息"))
        self.label.setText(_translate("SouthSoundOperaDetail", "曲谱名："))
        self.label_2.setText(_translate("SouthSoundOperaDetail", "作  者："))
        self.label_3.setText(_translate("SouthSoundOperaDetail", "页码："))
        self.label_4.setText(_translate("SouthSoundOperaDetail", "资源来源："))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SouthSoundOperaDetail = QtWidgets.QWidget()
    ui = Ui_SouthSoundOperaDetail()
    ui.setupUi(SouthSoundOperaDetail)
    SouthSoundOperaDetail.show()
    sys.exit(app.exec_())
