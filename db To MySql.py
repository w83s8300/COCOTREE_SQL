import pymysql 
import sqlite3
import pandas as pd
conn=sqlite3.connect("myDATA.db")
studentConn = conn.cursor()

db = pymysql.connect(host="127.0.0.1", 
                     user="user",
                     passwd="user1234",
                     database="cocotree")#連接資料庫

cursr = db.cursor()#cursor是前置緩衝區
sql='''SELECT * 
    from students   '''
studentConn.execute(sql)
data = studentConn.fetchall() 

sql='''Delete 
    from  students'''
cursr.execute(sql)#把新增資料放到資料庫
db.commit()##把新增資料放到資料庫


for i in range(0 ,len(data)):
    sql='''insert 
        into students (id,name,phone,Birthday,lesson,NEWvip,expire,Linetoken,ChannelSecret,LineId)    
        values ("{}","{}","{}","{}","{}","{}","{}","{}","{}","{}")'''.format(data[i][0],data[i][1],data[i][2],data[i][3],data[i][4],data[i][5],data[i][6],data[i][7],data[i][8],data[i][9])
    cursr.execute(sql)#把新增資料放到資料庫
    db.commit()##把新增資料放到資料庫



db.close()#關閉連接

