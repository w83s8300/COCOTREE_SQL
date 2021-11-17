import pymysql 
import sys
import requests
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from Line_UI import Ui_Form#連結Buiyui的Buy_data
from Line_Data import Ui_Form #讀UPDATABata.py 
from Line_Text_Data import Line_Text_Data
import subprocess
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

class Line_Data(QWidget,Ui_Form):
    def __init__(self):
        super(Line_Data,self).__init__()
        self.setupUi(self) #初始化窗口
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

        #滑鼠按左件處理
        self.listWidget_All_id.itemClicked.connect(self.list_data)
        self.pushButton_UpData.clicked.connect(self.UpData_Data)
        self.pushButton_Allbroadcast.clicked.connect(self.Allbroadcast)
        self.pushButton_Broadcast.clicked.connect(self.Broadcast)
        
        #欄位處理
        self.lineEdit_id.returnPressed.connect(self.lineEdit_changed)
        self.lineEdit_name.returnPressed.connect(lambda:self.set_focus(2))
        self.lineEdit_Linetoken.returnPressed.connect(lambda:self.set_focus(3))
        
    def clear_data(self):
         #清除欄位資料
        self.lineEdit_id.clear()
        self.lineEdit_name.clear()
        self.lineEdit_Linetoken.clear()
        
    def set_focus(self,id):
        #欄未取得游標
        if id == 5:self.lineEdit_id.setFocus()
        if id == 1:self.lineEdit_name.setFocus()
        if id == 2:self.lineEdit_Linetoken.setFocus()
        
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
        studentConn.execute(sql) 
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
        self.lineEdit_Linetoken.setText(record_data[record_index-1][7])


    def UpData_Data(self):
        x=self.lineEdit_id.text()
        if x!="":
            id=int(self.lineEdit_id.text())
            Linetoken=self.lineEdit_Linetoken.text()
            sql='''update students 
                set Linetoken="{}"
                where id={}'''.format(Linetoken,id)
            studentConn.execute(sql)#把新增資料放到資料庫
            db.commit()##把新增資料放到資料庫
            self.listWidget_All_id.clear()
            studentConn.execute("SELECT * from students order by id")
            record_data=studentConn.fetchall()
            for x in range(0 ,len(record_data)):
                self.listWidget_All_id.addItem(str(record_data[x][0])+'   '+record_data[x][1])
            self.lineEdit_14.setText(str(len(record_data)))
            self.lineEdit_15.setText(str(len(record_data)))

        else:
            self.errorui()

    def Allbroadcast(self):
        dialog=Line_Text_Data()
        result=dialog.exec_()
        date=dialog.dateTime()
        Linetext=date
        #=========================
        sql='''select id
        from students'''
        results=studentConn.execute("SELECT id from students order by id")
        allstudent=results.fetchall()
        i=max(allstudent)
        i=int(i[0])
        n=1
        while n<=i:
            sql='''select *
            from students
            where id={}'''.format(n)
            results=studentConn.execute(sql)
            allresults=results.fetchall()
           #Channel access token
            Linetoken=(allresults[0][7])
            #Channel secret 
            ChannelSecret=(allresults[0][8])
            # 必須放上自己的Channel Access Token
            line_bot_api = LineBotApi(Linetoken)
             # 必須放上自己的Channel Secret
            handler = WebhookHandler(ChannelSecret)

    def Broadcast(self):
        x=self.lineEdit_id.text()
        if x!="":
            dialog=Line_Text_Data()
            result=dialog.exec_()
            date=dialog.dateTime()
            Linetext=date
            
            x=self.lineEdit_id.text()
            sql='''select *
            from students
            where id={}'''.format(x)
            results=studentConn.execute(sql)
            y=studentConn.fetchall()
            Line_Text=Linetext#Line的文字
            line_bot_api = LineBotApi(y[0][7])
            handler = WebhookHandler(y[0][8])
            Linetoken=(y[0][7])
            #Channel secret 
            ChannelSecret=(y[0][8])
            #Your user ID
            LineId=(y[0][9])
            # 必須放上自己的Channel Access Token
            line_bot_api = LineBotApi(Linetoken)
            # 必須放上自己的Channel Secret
            handler = WebhookHandler(ChannelSecret)
            
            
            line_bot_api = LineBotApi('<channel access token>')


            line_bot_api.reply_message('<reply_token>', TextSendMessage(text='Hello World!'))
        
            
            line_bot_api.push_message(TextSendMessage(text=Linetext))
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text=event.message.text))


        else:
            self.errorui()
    
    def errorui (self):
        subprocess.Popen('python errorui.py')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Line_Data()
    window.show()
    sys.exit(app.exec_())

