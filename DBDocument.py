from PyQt5.QtWidgets import QApplication,QWidget
from UI.UI_TraditionalOperaDetail import Ui_TraditionalOperaDetail
from UI.UI_SouthSoundOperaDetail import Ui_SouthSoundOperaDetail
from UI.UI_SongBook import Ui_SongBookDetail
from UI.UI_ConferencePaperDetail import Ui_ConferencePaperDetail
from UI.UI_DissertationDetail import Ui_DissertationDetail
from UI.UI_PeriodicalDetail import Ui_PeriodicalDetail
from UI.UI_BookDetail import Ui_BookDetail
from UI.UI_DBSourceWindow import Ui_DBSourceView

class DBDocumentBase(QWidget):
    def __init__(self):
        super().__init__()
        self.baseUI = Ui_DBSourceView()
        self.baseUI.setupUi(self)

#封装戏曲
class DBDocumentXQ(DBDocumentBase):
    def __init__(self):
        super().__init__()
        self.win = QWidget()
        self.UI = Ui_TraditionalOperaDetail()
        self.UI.setupUi(self.win)
        self.baseUI.detailLayout.addWidget(self.win)


#封装期刊
class DBDocumentQK(DBDocumentBase):
    def __init__(self):
        super().__init__()
        self.win = QWidget()
        self.UI = Ui_PeriodicalDetail()
        self.UI.setupUi(self.win)
        self.baseUI.detailLayout.addWidget(self.win)

#封装图书
class DBDocumentTS(DBDocumentBase):
    def __init__(self):
        super().__init__()
        self.win = QWidget()
        self.UI = Ui_BookDetail()
        self.UI.setupUi(self.win)
        self.baseUI.detailLayout.addWidget(self.win)


#封装南音
class DBDocumentNY(DBDocumentBase):
    def __init__(self):
        super().__init__()
        self.win = QWidget()
        self.UI = Ui_SouthSoundOperaDetail()
        self.UI.setupUi(self.win)
        self.baseUI.detailLayout.addWidget(self.win)

#封装曲谱
class DBDocumentQP(DBDocumentBase):
    def __init__(self):
        super().__init__()
        self.win = QWidget()
        self.UI = Ui_SongBookDetail()
        self.UI.setupUi(self.win)
        self.baseUI.detailLayout.addWidget(self.win)


#封装会议论文
class DBDocumentHYLW(DBDocumentBase):
    def __init__(self):
        super().__init__()
        self.win = QWidget()
        self.UI = Ui_ConferencePaperDetail()
        self.UI.setupUi(self.win)
        self.baseUI.detailLayout.addWidget(self.win)

#封装学位论文
class DBDocumentXWLW(DBDocumentBase):
    def __init__(self):
        super().__init__()
        self.win = QWidget()
        self.UI = Ui_DissertationDetail()
        self.UI.setupUi(self.win)
        self.baseUI.detailLayout.addWidget(self.win)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    DBSourceView = DBDocumentHYLW()
    DBSourceView.show()
    sys.exit(app.exec_())