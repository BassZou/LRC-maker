# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(549, 199)
        self.user_label = QtWidgets.QLabel(Form)
        self.user_label.setGeometry(QtCore.QRect(50, 40, 61, 21))
        self.user_label.setObjectName("user_label")
        self.user_lineEdit = QtWidgets.QLineEdit(Form)
        self.user_lineEdit.setGeometry(QtCore.QRect(130, 40, 113, 20))
        self.user_lineEdit.setObjectName("user_lineEdit")
        self.pwd_label = QtWidgets.QLabel(Form)
        self.pwd_label.setGeometry(QtCore.QRect(50, 80, 54, 12))
        self.pwd_label.setObjectName("pwd_label")
        self.pwd_lineEdit = QtWidgets.QLineEdit(Form)
        self.pwd_lineEdit.setGeometry(QtCore.QRect(130, 70, 113, 20))
        self.pwd_lineEdit.setObjectName("pwd_lineEdit")
        self.login_Button = QtWidgets.QPushButton(Form)
        self.login_Button.setGeometry(QtCore.QRect(50, 110, 75, 23))
        self.login_Button.setObjectName("login_Button")
        self.cancel_Button = QtWidgets.QPushButton(Form)
        self.cancel_Button.setGeometry(QtCore.QRect(160, 110, 75, 23))
        self.cancel_Button.setObjectName("cancel_Button")
        self.user_textBrowser = QtWidgets.QTextBrowser(Form)
        self.user_textBrowser.setGeometry(QtCore.QRect(270, 30, 221, 101))
        self.user_textBrowser.setObjectName("user_textBrowser")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "用户登录"))
        self.user_label.setText(_translate("Form", "用户名"))
        self.pwd_label.setText(_translate("Form", "密码"))
        self.login_Button.setText(_translate("Form", "登录"))
        self.cancel_Button.setText(_translate("Form", "退出"))