import pymysql
import pandas as pd

# db = pymysql.connect(host="127.0.0.1", 
#                      user="user",
#                      passwd="user1234")#連接資料庫
# cursor = db.cursor()#cursor是前置緩衝區

# sql = '''CREATE DATABASE cocotree
#             COLLATE utf8mb4_unicode_ci; '''# 建立資料庫


db = pymysql.connect(host="127.0.0.1", 
                     user="user",
                     passwd="user1234",
                     database="cocotree")#連接資料庫
cursor = db.cursor()#cursor是前置緩衝區

sql = ''' 
        CREATE TABLE students (
            id VARCHAR(20),
            name VARCHAR(20),
            phone VARCHAR(20),
            Birthday VARCHAR(20),
            lesson VARCHAR(20),
            NEWvip VARCHAR(20),
            expire VARCHAR(20),
            Linetoken VARCHAR(100),
            ChannelSecret VARCHAR(100),
            LineId VARCHAR(100)
)
'''


cursor.execute(sql)#把新增資料放到資料庫
data = cursor.fetchall()
