import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from newvip import Ui_Form #讀UPDATABata.py 
import subprocess
import pymysql 
import datetime
import time
import pandas as pd


db = pymysql.connect(host="127.0.0.1", 
                     user="user",
                     passwd="user1234",
                     database="cocotree")#連接資料庫

studentConn = db.cursor()#cursor是前置緩衝區

class Newstudent_data(QWidget,Ui_Form):
    def __init__(self):
        super(Newstudent_data,self).__init__()
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
        self.pushButton_NewVip.clicked.connect(self.NewVip_data)
        self.pushButton_UpData.clicked.connect(self.UpData_Date)
        self.pushButton_Delete.clicked.connect(self.Delete_data)
        #欄位處理
        
        self.lineEdit_id.returnPressed.connect(self.lineEdit_changed)
        self.lineEdit_name.returnPressed.connect(lambda:self.set_focus(2))
        self.lineEdit_phone.returnPressed.connect(lambda:self.set_focus(3))
        #self.dateEdit_Birthday.returnPressed.connect(lambda:self.set_focus(4))
        self.lineEdit_lesson.returnPressed.connect(lambda:self.set_focus(4))
        #self.dateEdit_Add.returnPressed.connect(lambda:self.set_focus(6))
        self.lineEdit_expire.returnPressed.connect(lambda:self.set_focus(5))
    
    def clear_data(self):
         #清除欄位資料
        self.lineEdit_id.clear()
        self.lineEdit_name.clear()
        self.lineEdit_phone.clear()
        self.dateEdit_Birthday.clear()
        self.lineEdit_lesson.clear()
        self.dateEdit_Add.clear()
        self.lineEdit_expire.clear()

    def set_focus(self,id):
        #欄未取得游標
        if id == 1:self.lineEdit_name.setFocus()
        if id == 2:self.lineEdit_phone.setFocus()
        #if id == 3:self.dateEdit_Birthday.setFocus()
        if id == 3:self.lineEdit_lesson.setFocus()
        #if id == 5:self.dateEdit_Add.setFocus()
        if id == 4:self.lineEdit_expire.setFocus()
        if id == 5:self.lineEdit_id.setFocus()

    def list_data(self, item):
        #滑鼠按下list資料查詢資料
        y=self.lineEdit_id.setText(item.text()[0:4])
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
        self.lineEdit_phone.setText(record_data[record_index-1][2])
        z=(record_data[record_index-1][3])
        z=datetime.datetime.strptime(z,"%Y-%m-%d")
        z=QDate(z)
        self.dateEdit_Birthday.date().toString(Qt.ISODate)
        self.dateEdit_Birthday=QDateTimeEdit(z, self)
        self.dateEdit_Birthday.setDisplayFormat("yyyy-MM-dd")
        self.lineEdit_lesson.setText(str(record_data[record_index-1][4]))
        #self.dateEdit_Add.setText(record_data[record_index-1][5])
        self.lineEdit_expire.setText(record_data[record_index-1][6])        
                    
    def NewVip_data(self):
        #存入新一筆資料
        x=self.lineEdit_id.text()
        if x!="":
            id=self.lineEdit_id.text()
            name=self.lineEdit_name.text()
            phone=self.lineEdit_phone.text()
            Birthday=self.dateEdit_Birthday.date().toString(Qt.ISODate)#讀取時間
            lesson=self.lineEdit_lesson.text()
            NEWvip=self.dateEdit_Add.date().toString(Qt.ISODate)
            y=datetime.datetime.strptime(NEWvip,"%Y-%m-%d")
            time_del = datetime.timedelta(days=365)
            y=y+time_del
            expire=("{}-{}-{}".format(y.year, y.month, y.day))
            Linetoken="no"
            ChannelSecret="no"
            LineId="U2cae785ae644eaef81f9f59e4c2b9990"
            x=(str(id),name,phone,Birthday,lesson,NEWvip,expire,Linetoken,ChannelSecret,LineId)
            sql='''insert 
                into students (id,name,phone,Birthday,lesson,NEWvip,expire,Linetoken,ChannelSecret,LineId)    
                values ("{}","{}","{}","{}","{}","{}","{}","{}","{}","{}")'''.format(str(id),name,phone,Birthday,lesson,NEWvip,expire,Linetoken,ChannelSecret,LineId)
            studentConn.execute(sql)#把新增資料放到資料庫
            db.commit()##把新增資料放到資料庫
        else:
            self.errorui()


        self.listWidget_All_id.clear()
        studentConn.execute("SELECT * from students order by id")
        record_data=studentConn.fetchall()
        for x in range(0 ,len(record_data)):
            self.listWidget_All_id.addItem(str(record_data[x][0])+'   '+record_data[x][1])
        self.lineEdit_14.setText(str(len(record_data)))
        self.lineEdit_15.setText(str(len(record_data)))

    def UpData_Date(self):
        x=self.lineEdit_id.text()
        if x!="":

            id=int(self.lineEdit_id.text())
            name=self.lineEdit_name.text()
            phone=self.lineEdit_phone.text()
            Birthday=self.dateEdit_Birthday.date().toString(Qt.ISODate)#讀取時間
            lesson=self.lineEdit_lesson.text()
            NEWvip=self.dateEdit_Add.date().toString(Qt.ISODate)
            expire=self.lineEdit_expire.text()
            y=datetime.datetime.strptime(expire,"%Y-%m-%d")
            expire=("{}-{}-{}".format(y.year, y.month, y.day))
            sql='''update students 
                set name="{}",phone="{}",Birthday="{}",lesson="{}",NEWvip="{}",expire="{}"
                where id={}'''.format(name,phone,Birthday,lesson,NEWvip,expire,id)
            studentConn.execute(sql)
            db.commit()
            self.listWidget_All_id.clear()
            studentConn.execute("SELECT * from students order by id")
            record_data=studentConn.fetchall()
            for x in range(0 ,len(record_data)):
                self.listWidget_All_id.addItem(str(record_data[x][0])+'   '+record_data[x][1])
            self.lineEdit_14.setText(str(len(record_data)))
            self.lineEdit_15.setText(str(len(record_data)))

        else:
            self.errorui()

    def Delete_data(self):
        x=self.lineEdit_id.text()
        if x!="":
            sql='''DELETE
                from students
                where id={}'''.format(x)
            results=studentConn.execute(sql)
            db.commit()
            self.listWidget_All_id.clear()
            studentConn.execute("SELECT * from students order by id")
            record_data=studentConn.fetchall()
            for x in range(0 ,len(record_data)):
                self.listWidget_All_id.addItem(str(record_data[x][0])+'   '+record_data[x][1])
            self.lineEdit_14.setText(str(len(record_data)))
            self.lineEdit_15.setText(str(len(record_data)))
        else:
            self.errorui()

    def errorui (self):
        subprocess.Popen('python errorui.py')

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Newstudent_data()
    window.show()
    sys.exit(app.exec_())

