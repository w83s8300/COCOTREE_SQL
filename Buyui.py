import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from Buy import Ui_Form
import subprocess
import pymysql
import sqlite3
conn=pymysql.connect(host="127.0.0.1", 
                     user="user",
                     passwd="user1234",
                     database="cocotree")#連接資料庫
studentConn = conn.cursor()

class Buy_data(QDialog,Ui_Form):
    def __init__(self,parent=None):
        super(Buy_data, self).__init__(parent)
        self.setupUi(self)
        #self.toolButton.clicked.connect(self.dateTime)
        #在佈局中新增控制元件

    def dateTime(self):
        return self.lineEdit.text()#讀取文字

    @staticmethod#回傳資料
    def getDateTime(parent=None):
        dialog=Buy_data(parent)
        result=dialog.exec_()
        date=dialog.dateTime()#讀dateTime
        return (date)
        

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Buy_data()
    window.show()
    sys.exit(app.exec_())

