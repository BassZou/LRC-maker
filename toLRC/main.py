# -*- coding: utf-8 -*-

from music import Music

#导入程序运行必须模块
import sys
#PyQt5中使用的基本控件都在PyQt5.QtWidgets模块中
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtGui import QIcon
from UI import Ui_Form

"""
1. 音乐播放
2. LRC 格式导出
3. 导入音乐
4. 读取word文本
"""
def start():
    #固定的，PyQt5程序都需要QApplication对象。sys.argv是命令行参数列表，确保程序可以双击运行
    app = QApplication(sys.argv)
    #初始化
    myWin = MyMainForm()
    myWin.setWindowIcon(QIcon('goodsongs.ico'))
    #将窗口控件显示在屏幕上
    myWin.show()
    #程序运行，sys.exit方法确保程序完整退出。
    sys.exit(app.exec_())


class MyMainForm(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)

        # 导入mp3
        self.import_file_btn.clicked.connect(self.openfile)

        # 添加退出按钮信号和槽。调用close函数
        self.cancel_Button.clicked.connect(self.close)
    
    def openfile(self):
        file_path = QFileDialog.getOpenFileName()[0]
        print('文件夹路径',file_path)
        musi = Music(file_path)
        musi.play()


    def display(self):
        file_path = QFileDialog.getOpenFileName()
        print('文件夹路径',file_path)

        #利用line Edit控件对象text()函数获取界面输入
        # username = self.user_lineEdit.text()
        # password = self.pwd_lineEdit.text()
        #利用text Browser控件对象setText()函数设置界面显示
        # self.user_textBrowser.setText("登录成功!\n" + "用户名是: "+ username+ ",密码是： "+ password)


if __name__ == '__main__':
    start()
    