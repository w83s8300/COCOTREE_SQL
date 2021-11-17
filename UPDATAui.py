from sqlite3.dbapi2 import DatabaseError
import pymysql
import sys
import requests
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtCore
from Buyui import Buy_data#連結Buiyui的Buy_data
from UPDATABata import Ui_Form #讀UPDATABata.py 
import subprocess
import pymysql 
import datetime
import time
import pandas as pd
from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler)
from linebot.exceptions import (
    InvalidSignatureError)
from linebot.models import *
app = Flask(__name__)

db = pymysql.connect(host="127.0.0.1", 
                     user="user",
                     passwd="user1234",
                     database="cocotree")#連接資料庫

studentConn = db.cursor()#cursor是前置緩衝區

class UPDATA(QWidget,Ui_Form):
    def __init__(self,parent=None):
        super(UPDATA, self).__init__(parent)
        self.setupUi(self)#初始化窗口
        #self.setGeometry(20, 105, 1240, 626)
        self.focusWidget() #???
        #self.clear_data()
        global record_data #global全區
        #取得資料表及資料
        studentConn.execute("SELECT * from students order by id")
        record_data=studentConn.fetchall()
        for x in range(0 ,len(record_data)):
            self.listWidget_All_id.addItem(str(record_data[x][0])+'   '+record_data[x][1])
        self.lineEdit_14.setText(str(len(record_data)))
        self.lineEdit_15.setText(str(len(record_data)))
        #LINE的開關
        self.checkBox.setChecked(True)
        self.checkBox.stateChanged.connect(self.checkBoxChangedAction)
        

        #滑鼠按左件處理
        self.listWidget_All_id.itemClicked.connect(self.list_data)
        self.pushButton_Attendclass.clicked.connect(self.Attendclass_data)
        self.pushButton_BUY.clicked.connect(self.BUY)
        self.pushButton_Refill.clicked.connect(self.Refill_data)
        #欄位處理
        self.lineEdit_id.returnPressed.connect(self.lineEdit_changed)
        self.lineEdit_name.returnPressed.connect(lambda:self.set_focus(2))
        self.lineEdit_phone.returnPressed.connect(lambda:self.set_focus(3))
        self.lineEdit_Birthday.returnPressed.connect(lambda:self.set_focus(4))
        self.lineEdit_lesson.returnPressed.connect(lambda:self.set_focus(5))
        self.lineEdit_Add.returnPressed.connect(lambda:self.set_focus(6))
        self.lineEdit_expire.returnPressed.connect(lambda:self.set_focus(7))
    
    #LINE的開關
    def checkBoxChangedAction(self, state):
        if (QtCore.Qt.Checked == state):
            Linecheck="ON"
  
        else:
            Linecheck="OFF"

    def clear_data(self):
         #清除欄位資料
        self.lineEdit_id.clear()
        self.lineEdit_name.clear()
        self.lineEdit_phone.clear()
        self.lineEdit_Birthday.clear()
        self.lineEdit_lesson.clear()
        self.lineEdit_Add.clear()
        self.lineEdit_expire.clear()

    def set_focus(self,id):
        #欄未取得游標
        if id == 1:self.lineEdit_name.setFocus()
        if id == 2:self.lineEdit_phone.setFocus()
        if id == 3:self.lineEdit_Birthday.setFocus()
        if id == 4:self.lineEdit_lesson.setFocus()
        if id == 5:self.lineEdit_Add.setFocus()
        if id == 6:self.lineEdit_expire.setFocus()

    def list_data(self, item):
        #滑鼠按下list資料查詢資料
        self.lineEdit_id.setText(item.text()[0:4])
        x=self.lineEdit_id.text()
        sql='''select * from students where id={}'''.format(x)
        studentConn.execute(sql)
        #studentConn.execute(sql, student_data)
        record_data=studentConn.fetchall() 
        record_index =1 
        self.lineEdit_15.setText(str(record_index))
        if len(record_data) > 0 : self.display_data(record_data)        
    
    def lineEdit_changed(self):
        #編號欄位按 Enter鍵判斷是否新資料
        x=student_data = self.lineEdit_id.text()
        sql='''select * from students where id={}'''.format(x)
        studentConn.execute(x)        
        record_data=studentConn.fetchall()     
        record_index =1 
        self.lineEdit_15.setText(str(record_index))
        if len(record_data) > 0 : self.display_data(record_data)
        else:
           self.lineEdit_name.setFocus() 

    def display_data(self, record_data):
        #資料顯示於欄位上
        self.clear_data()
        self.lineEdit_name.setFocus()
        record_index=int(self.lineEdit_15.text())
        self.lineEdit_id.setText(str(record_data[record_index-1][0]))
        self.lineEdit_name.setText(record_data[record_index-1][1])
        self.lineEdit_phone.setText(record_data[record_index-1][2])
        self.lineEdit_Birthday.setText(record_data[record_index-1][3])
        self.lineEdit_lesson.setText(str(record_data[record_index-1][4]))
        self.lineEdit_Add.setText(record_data[record_index-1][5])
        self.lineEdit_expire.setText(record_data[record_index-1][6]) 

    def Attendclass_data(self):
        #上課
        x=self.lineEdit_id.text()
        if x!="":
            sql=f'''Update students 
                set lesson=lesson-1
                where id={x}'''
            studentConn.execute(sql)#把新增資料放到資料庫
            db.commit()##把新增資料放到資料庫
            sql=f'''select * from students where id={x}'''
            studentConn.execute(sql)
            #studentConn.execute(sql, student_data)
            record_data=studentConn.fetchall() 
            record_index =1 
            self.lineEdit_15.setText(str(record_index))
            if len(record_data) > 0 : self.display_data(record_data)
            self.Line_data()

        else:
            self.errorui()


    def BUY(self):
        #買課 
        x=self.lineEdit_id.text()
        if x!="":
            #連結Buiyui的Buy_data
            dialog=Buy_data()
            result=dialog.exec_()
            date=dialog.dateTime()
            #==========================
            if date!="":
                y=int(date)
            else:y=0
            sql='''update students
            set lesson=lesson+{}
            where id={}'''.format(y,x)
            studentConn.execute(sql)
            db.commit()
            sql='''select * from students where id={}'''.format(x)
            studentConn.execute(sql)
            #studentConn.execute(sql, student_data)
            record_data=studentConn.fetchall() 
            record_index =1 
            self.lineEdit_15.setText(str(record_index))
            if len(record_data) > 0 : self.display_data(record_data)
            self.Line_data()
        else:
            self.errorui()

    def Refill_data(self):
        #續會員
        x=self.lineEdit_id.text()
        if x!="":
            sql='''select expire 
            from students
            where id={}'''.format(x)
            studentConn.execute(sql)#把新增資料放到資料庫
            allresults = studentConn.fetchall()
            y=allresults[0][0]
            y=datetime.datetime.strptime(y,"%Y-%m-%d")
            time_del = datetime.timedelta(days=365)
            y=y+time_del
            y=("{}-{}-{}".format(y.year, y.month, y.day))
            sql='''update students
                set expire="{}"
                where id={}'''.format(y,x)
            studentConn.execute(sql)
            db.commit()
            sql='''select * from students where id={}'''.format(x)
            studentConn.execute(sql)
            #studentConn.execute(sql, student_data)
            record_data=studentConn.fetchall() 
            record_index =1 
            self.lineEdit_15.setText(str(record_index))
            if len(record_data) > 0 : self.display_data(record_data)
            self.Line_data()
        else:
            self.errorui()
            
    def Line_data(self):
        pass
        #把資料傳到Line

        # Line=self.checkBox.isChecked()
        
        # if Line==True:
        #     x=self.lineEdit_id.text()
        #     sql='''select *
        #         from students
        #         where id={}'''.format(x)
        #     results=studentConn.execute(sql)
        #     y=results.fetchall()
        #     Line_Text=("會員編號:{} 名字:{} 剩下{} 堂到期日:{}".format(y[0][0],y[0][1],y[0][4],y[0][6]))

        #     def lineNotifyMessage(token, msg):
        #         headers = {
        #             "Authorization": "Bearer " + token, 
        #             "Content-Type" : "application/x-www-form-urlencoded"
        #         }

        #         payload = {'message': msg}
        #         r = requests.post("https://notify-api.line.me/api/notify", headers = headers, params = payload)
        #         return r.status_code
        #     #Channel access token

        #     Linetoken=(y[0][7])
        #     msg =Line_Text
        #     token = Linetoken
        #     lineNotifyMessage(token, msg)
        """
            #Channel access token
            Linetoken=(y[0][7])
            #Channel secret 
            ChannelSecret=(y[0][8])
            #Your user ID
            LineId=(y[0][9])
            # 必須放上自己的Channel Access Token
            line_bot_api = LineBotApi(Linetoken)
            # 必須放上自己的Channel Secret
            handler = WebhookHandler(ChannelSecret)
            #廣播內文
            Linetext=(Line_Text)
            line_bot_api.push_message(LineId,TextSendMessage(text=Linetext))
            
        """

    def errorui (self):
        subprocess.Popen('python errorui.py')

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = UPDATA()
    window.show()
    sys.exit(app.exec_())

