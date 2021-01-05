from PyQt5.QtWidgets import QApplication,QWidget,QMainWindow
import sys

def do():
    print(111)

class MainWin(QMainWindow,ui):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

if __name__ == '__main__':

    mainApp = QApplication(sys.argv)

    view = MainWin()
    view.show()

    sys.exit(mainApp.exec())

    szQurey = ("select Title, Author, Origin, Pages, Summary from TraditionalOpera limit %d,%d" % (
    limitIndex, self.eachPageRecord))

        self.queryModel.setHeaderData(0,Qt.Horizontal,"戏曲名")
        self.queryModel.setHeaderData(1, Qt.Horizontal, "作者")
        self.queryModel.setHeaderData(2, Qt.Horizontal, "收录来源")
        self.queryModel.setHeaderData(3, Qt.Horizontal, "页数")
        self.queryModel.setHeaderData(4, Qt.Horizontal, "简介")

        self.mapper.addMapping(self.UI.lineEdit_Title,0)
        self.mapper.addMapping(self.UI.lineEdit_Author,1)
        self.mapper.addMapping(self.UI.lineEdit_Origin,2)
        self.mapper.addMapping(self.UI.lineEdit_Pages,3)
        self.mapper.addMapping(self.UI.textEdit_Summary,4)
        self.mapper.toFirst()
