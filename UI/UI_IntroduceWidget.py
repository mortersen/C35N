# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_IntroduceWidget.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_IntroduceWidget(object):
    def setupUi(self, IntroduceWidget):
        IntroduceWidget.setObjectName("IntroduceWidget")
        IntroduceWidget.resize(735, 618)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icon/approve.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        IntroduceWidget.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(IntroduceWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.label = QtWidgets.QLabel(IntroduceWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(0, 0))
        self.label.setMaximumSize(QtCore.QSize(800, 600))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/Icon/la0.jpg"))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(2, 2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.verticalLayout.setStretch(0, 2)
        self.verticalLayout.setStretch(1, 8)
        self.verticalLayout.setStretch(2, 2)

        self.retranslateUi(IntroduceWidget)
        QtCore.QMetaObject.connectSlotsByName(IntroduceWidget)

    def retranslateUi(self, IntroduceWidget):
        _translate = QtCore.QCoreApplication.translate
        IntroduceWidget.setWindowTitle(_translate("IntroduceWidget", "介绍页"))
import img_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    IntroduceWidget = QtWidgets.QWidget()
    ui = Ui_IntroduceWidget()
    ui.setupUi(IntroduceWidget)
    IntroduceWidget.show()
    sys.exit(app.exec_())
