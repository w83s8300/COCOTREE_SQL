import pymysql

db = pymysql.connect(host="127.0.0.1", 
                     user="user",
                     passwd="user1234",
                     database="cocotree")#連接資料庫
                    
cursr = db.cursor()#cursor是前置緩衝區

sql = '''CREATE TABLE IF NOT EXISTS students ( id varchar(100), \
                              name varchar(20),\
                                phone varchar(20),\
                                Birthday varchar(50),\
                                lesson varchar(20),\
                                NEWvip varchar(20),\
                                expire varchar(20),\
                                Linetoken varchar(100),\
                                ChannelSecret varchar(100),\
                                LineId varchar(100),
                                  )'''

cursr.execute(sql)
db.commit()
