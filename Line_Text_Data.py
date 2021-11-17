import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from Line_Text_UI import Ui_Form
import subprocess

class Line_Text_Data(QDialog,Ui_Form):
    def __init__(self,parent=None):
        super(Line_Text_Data, self).__init__(parent)
        self.setupUi(self)
        self.toolButton.clicked.connect(self.dateTime)

    def dateTime(self):
        return self.textEdit.toPlainText()#讀取文字

    @staticmethod#回傳資料
    def getDateTime(parent=None):
        dialog=Line_Text_Data(parent)
        result=dialog.exec_()
        date=dialog.dateTime()#讀dateTime
        return (date)
        



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Line_Text_Data()
    window.show()
    sys.exit(app.exec_())