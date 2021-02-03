# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1000, 500) # 宽 高
        one = 10 # 第一行
        two = 30 # 第二行
        
        # 按钮 - 导入mp3
        self.import_file_btn = QtWidgets.QPushButton(Form)
        self.import_file_btn.setGeometry(QtCore.QRect(20,20,100,23))
        self.import_file_btn.setObjectName('impt_file_btn')
        self.import_file_btn.setText('导入MP3')

        # 按钮 - 导入词word
        self.import_ci_btn = QtWidgets.QPushButton(Form)
        self.import_ci_btn.setGeometry(QtCore.QRect(120,20,120,23))
        self.import_ci_btn.setObjectName('import_ci_btn')
        self.import_ci_btn.setText('导入词 word')

        # 按钮 - 播放
        self.btn_play = QtWidgets.QPushButton(Form)
        self.btn_play.setGeometry(QtCore.QRect(240,20,100,23))
        self.btn_play.setObjectName('btn_play')
        self.btn_play.setText('播放')

        # 按钮 - 暂停
        self.btn_stop = QtWidgets.QPushButton(Form)
        self.btn_stop.setGeometry(QtCore.QRect(340,20,100,23))
        self.btn_stop.setObjectName('btn_stop')
        self.btn_stop.setText('暂停')

        # 按钮 - 后退5秒
        self.btn_tui5s = QtWidgets.QPushButton(Form)
        self.btn_tui5s.setGeometry(QtCore.QRect(440,20,100,23))
        self.btn_tui5s.setObjectName('btn_tui5s')
        self.btn_tui5s.setText('后退5秒')

        # 按钮 - 进5秒
        self.btn_qian5s = QtWidgets.QPushButton(Form)
        self.btn_qian5s.setGeometry(QtCore.QRect(550,20,100,23))
        self.btn_qian5s.setObjectName('btn_qian5s')
        self.btn_qian5s.setText('前进5秒')

        # 按钮 - 打点
        self.btn_point = QtWidgets.QPushButton(Form)
        self.btn_point.setGeometry(QtCore.QRect(20,50,100,23))
        self.btn_point.setObjectName('btn_point')
        self.btn_point.setText('标记打点')

        # 按钮 - 导出LRC
        self.btn_lrc = QtWidgets.QPushButton(Form)
        self.btn_lrc.setGeometry(QtCore.QRect(120, 50, 120, 23))
        self.btn_lrc.setObjectName("btn_lrc")
        self.btn_lrc.setText("导出LRC")

        # 按钮 - 关闭
        self.cancel_Button = QtWidgets.QPushButton(Form)
        self.cancel_Button.setGeometry(QtCore.QRect(240, 50, 100, 23))
        self.cancel_Button.setObjectName("cancel_Button")
        self.cancel_Button.setText("关闭")

        # 文字 - 歌名
        self.song_name = QtWidgets.QLabel(Form)
        self.song_name.setGeometry(QtCore.QRect(870, 30, 54, 12))
        self.song_name.setObjectName("song_name")
        self.song_name.setText('歌名:')

        # 文字 - 歌名
        self.song_name_value = QtWidgets.QLabel(Form)
        self.song_name_value.setGeometry(QtCore.QRect(900, 30, 54, 12))
        self.song_name_value.setObjectName("song_name_value")
        self.song_name_value.setText('未选择歌曲')


        # # 输入框
        # self.user_lineEdit = QtWidgets.QLineEdit(Form)
        # self.user_lineEdit.setGeometry(QtCore.QRect(130, 100, 113, 20))
        # self.user_lineEdit.setObjectName("user_lineEdit")

        # # 文字
        # self.pwd_label = QtWidgets.QLabel(Form)
        # self.pwd_label.setGeometry(QtCore.QRect(50, 180, 54, 12))
        # self.pwd_label.setObjectName("pwd_label")
        # self.pwd_label.setText("密码2")

        # # 输入框
        # self.pwd_lineEdit = QtWidgets.QLineEdit(Form)
        # self.pwd_lineEdit.setGeometry(QtCore.QRect(130, 170, 113, 20))
        # self.pwd_lineEdit.setObjectName("pwd_lineEdit")

        # 按钮
        self.login_Button = QtWidgets.QPushButton(Form)
        self.login_Button.setGeometry(QtCore.QRect(50, 110, 75, 23))
        self.login_Button.setObjectName("login_Button")
        self.login_Button.setText("login")

        

        # 大文本框
        self.user_textBrowser = QtWidgets.QTextBrowser(Form)
        self.user_textBrowser.setGeometry(QtCore.QRect(270, 130, 221, 101))
        self.user_textBrowser.setObjectName("user_textBrowser")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "LRC制作工具"))
        # self.user_label.setText(_translate("Form", "用户名"))
        # self.pwd_label.setText(_translate("Form", "密码"))
        # self.login_Button.setText(_translate("Form", "登录"))
        # self.cancel_Button.setText(_translate("Form", "退出"))