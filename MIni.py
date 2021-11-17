import sys
import urllib.request as req
import bs4
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from MiniVip import Ui_MainWindow
from UPDATAui import UPDATA
from NEW_VIPui import Newstudent_data
from Line_Data import Line_Data
#from student import Ui_student
class Main_program(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Main_program,self).__init__()
        self.setupUi(self)
        #action1_1 name='學生資料維護' program_name='main-student.py'
        #action1_2 name='教師資料維護' program_name='main-teacher.py'
        #file.triggered[QAction].connect(self.sub_window)
        self.pushButton.clicked.connect(lambda:self.sub_window(1))
        self.pushButton_2.clicked.connect(lambda:self.sub_window(2))
        self.pushButton_3.clicked.connect(lambda:self.sub_window(3))
        #公告
        url="https://bsb.kh.edu.tw/afterschool/servlet/bsb?city=42"
        requuest=req.Request(url,headers={
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"
        })
        with req.urlopen(requuest) as response :
            data=response.read().decode("utf-8")
        root=bs4.BeautifulSoup(data,"html.parser")
        titles=root.find_all("td",align="left")
        for title in titles:
            self.listWidget.addItem(title.a.string)




    def sub_window(self,program_index):
        if program_index == 1:
            self.sud_window=UPDATA()
            self.sud_window.show()
            
        if program_index == 2:
            self.sud_window=Newstudent_data()
            self.sud_window.show()
            
        if program_index == 3:
            self.sud_window=Line_Data()
            self.sud_window.show()
            
    def bulletin(self):
        url="https://bsb.kh.edu.tw/afterschool/servlet/bsb?city=42"
        requuest=req.Request(url,headers={
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"
        })
        with req.urlopen(requuest) as response :
            data=response.read().decode("utf-8")

        root=bs4.BeautifulSoup(data,"html.parser")
        titles=root.find_all("td",align="left")
        for title in titles:
            print(title.a.string)

        



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Main_program()
    window.show()
    sys.exit(app.exec_())        