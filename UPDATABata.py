# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UPDATABata.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(487, 483)
        self.splitter = QtWidgets.QSplitter(Form)
        self.splitter.setGeometry(QtCore.QRect(110, 71, 165, 241))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.lineEdit_id = QtWidgets.QLineEdit(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_id.setFont(font)
        self.lineEdit_id.setObjectName("lineEdit_id")
        self.lineEdit_name = QtWidgets.QLineEdit(self.splitter)
        self.lineEdit_name.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_name.setFont(font)
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.lineEdit_phone = QtWidgets.QLineEdit(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_phone.setFont(font)
        self.lineEdit_phone.setObjectName("lineEdit_phone")
        self.lineEdit_Birthday = QtWidgets.QLineEdit(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_Birthday.setFont(font)
        self.lineEdit_Birthday.setObjectName("lineEdit_Birthday")
        self.lineEdit_lesson = QtWidgets.QLineEdit(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_lesson.setFont(font)
        self.lineEdit_lesson.setObjectName("lineEdit_lesson")
        self.lineEdit_Add = QtWidgets.QLineEdit(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_Add.setFont(font)
        self.lineEdit_Add.setObjectName("lineEdit_Add")
        self.lineEdit_expire = QtWidgets.QLineEdit(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_expire.setFont(font)
        self.lineEdit_expire.setObjectName("lineEdit_expire")
        self.splitter_3 = QtWidgets.QSplitter(Form)
        self.splitter_3.setGeometry(QtCore.QRect(10, 331, 281, 31))
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.pushButton_Attendclass = QtWidgets.QPushButton(self.splitter_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_Attendclass.setFont(font)
        self.pushButton_Attendclass.setObjectName("pushButton_Attendclass")
        self.pushButton_BUY = QtWidgets.QPushButton(self.splitter_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_BUY.setFont(font)
        self.pushButton_BUY.setObjectName("pushButton_BUY")
        self.pushButton_Refill = QtWidgets.QPushButton(self.splitter_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_Refill.setFont(font)
        self.pushButton_Refill.setObjectName("pushButton_Refill")
        self.listWidget_All_id = QtWidgets.QListWidget(Form)
        self.listWidget_All_id.setGeometry(QtCore.QRect(310, 71, 151, 251))
        self.listWidget_All_id.setObjectName("listWidget_All_id")
        self.splitter_2 = QtWidgets.QSplitter(Form)
        self.splitter_2.setGeometry(QtCore.QRect(21, 72, 73, 241))
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.label_id = QtWidgets.QLabel(self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_id.setFont(font)
        self.label_id.setObjectName("label_id")
        self.label_name = QtWidgets.QLabel(self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_name.setFont(font)
        self.label_name.setObjectName("label_name")
        self.label_phone = QtWidgets.QLabel(self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_phone.setFont(font)
        self.label_phone.setObjectName("label_phone")
        self.label_Birthday = QtWidgets.QLabel(self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_Birthday.setFont(font)
        self.label_Birthday.setObjectName("label_Birthday")
        self.label_lesson = QtWidgets.QLabel(self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_lesson.setFont(font)
        self.label_lesson.setObjectName("label_lesson")
        self.label_Add = QtWidgets.QLabel(self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_Add.setFont(font)
        self.label_Add.setObjectName("label_Add")
        self.label_expire = QtWidgets.QLabel(self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_expire.setFont(font)
        self.label_expire.setObjectName("label_expire")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setGeometry(QtCore.QRect(22, 10, 441, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit.setFont(font)
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.label_16 = QtWidgets.QLabel(Form)
        self.label_16.setGeometry(QtCore.QRect(300, 330, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_16.setObjectName("label_16")
        self.label_15 = QtWidgets.QLabel(Form)
        self.label_15.setGeometry(QtCore.QRect(300, 370, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_15.setObjectName("label_15")
        self.lineEdit_15 = QtWidgets.QLineEdit(Form)
        self.lineEdit_15.setEnabled(True)
        self.lineEdit_15.setGeometry(QtCore.QRect(390, 330, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_15.setFont(font)
        self.lineEdit_15.setText("")
        self.lineEdit_15.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.lineEdit_14 = QtWidgets.QLineEdit(Form)
        self.lineEdit_14.setEnabled(True)
        self.lineEdit_14.setGeometry(QtCore.QRect(390, 370, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_14.setFont(font)
        self.lineEdit_14.setText("")
        self.lineEdit_14.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.checkBox = QtWidgets.QCheckBox(Form)
        self.checkBox.setGeometry(QtCore.QRect(20, 370, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_Attendclass.setText(_translate("Form", "上課"))
        self.pushButton_BUY.setText(_translate("Form", "買課"))
        self.pushButton_Refill.setText(_translate("Form", "續會員"))
        self.label_id.setText(_translate("Form", "會員編號:"))
        self.label_name.setText(_translate("Form", "姓名:"))
        self.label_phone.setText(_translate("Form", "電話:"))
        self.label_Birthday.setText(_translate("Form", "生日:"))
        self.label_lesson.setText(_translate("Form", "課堂數:"))
        self.label_Add.setText(_translate("Form", "註冊日期:"))
        self.label_expire.setText(_translate("Form", "到期日:"))
        self.lineEdit.setText(_translate("Form", "會 員 基 本 資 料"))
        self.label_16.setText(_translate("Form", "目前筆數"))
        self.label_15.setText(_translate("Form", "總 筆 數"))
        self.checkBox.setText(_translate("Form", "Line的功能"))
