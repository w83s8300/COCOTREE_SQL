import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from error import Ui_Form
#from student import Ui_student

class error(QDialog,Ui_Form):
    def __init__(self,parent=None):
        super(error, self).__init__(parent)
        self.setupUi(self)
        #在佈局中新增控制元件

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = error()
    window.show()
    sys.exit(app.exec_())