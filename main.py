#coding:utf-8


from PySide2.QtWidgets import QApplication
from PySide2 import QtCore, QtWidgets
from qtmodern import styles, windows
from Ui_main import Ui_Form
import pyttsx3
import config
from spider_weather import weather_ip

class MainWindow( QtWidgets.QWidget, Ui_Form):

    def __init__(self):     
        super().__init__()      # 继承父类的init方法
        # 使用ui文件导入定义界面类  
        self.ui = Ui_Form()
        # 初始化界面
        self.ui.setupUi(self)
        # 获取IP定位地址天气
        self.day7_weather = weather_ip.get_weather()
        # print('IP定位天气' + str(self.day7_weather))
        # 设置locationButton按钮文字为ip定位地址
        self.ui.locationButton.setText('IP:'+self.day7_weather['city'])
        self.show_weather()
        # self.ui.resultBrowser.append(text)
        # self.day7_weather = self.ui.locationButton.click()
        # 初始化下拉列表增加provinceBox的下拉选项
        self.ui.provinceBox.addItems(list(config.map.keys()))

        # 获取选中province_text 与city_text的下拉列表
        self.province_text = self.ui.provinceBox.currentText()

        # 初始化下拉列表增加cityBox的下拉选项
        self.ui.cityBox.addItems(list(config.map[self.province_text].keys()))
        # print(list(config.map[self.province_text].keys()))
        self.city_text = self.ui.cityBox.currentText()

        # 语音按钮
        self.ui.voice_Button.setText('语音播报')

        # 当改变了provinceBox时调用get_provinceBox_text函数
        # 当改变了cityBox时调用get_cityBox_info函数
        self.ui.provinceBox.currentIndexChanged.connect(self.get_provinceBox_text)
        self.ui.cityBox.currentIndexChanged.connect(self.get_cityBox_info)
        # 当点击时播报天气预报
        self.ui.voice_Button.clicked.connect(self.voice_text)


    def get_provinceBox_text(self):
        self.province_text = self.ui.provinceBox.currentText()
        self.ui.cityBox.clear()
        # self.ui.cityBox.addItems(list(config.map[self.province_text].keys()))
        # self.ui.cityBox.currentIndexChanged.connect(self.get_cityBox_info)

# 问题KeyError: '' set_weather的辽宁

    def get_cityBox_info(self):
        
        self.ui.cityBox.addItems(list(config.map[self.province_text].keys()))
        self.city_text = self.ui.cityBox.currentText()
        # print('省份+城市：' + self.province_text + self.city_text)
        # zone['region']][zone['city']
        select_region = {'region':self.province_text, 'city':self.city_text}
        # print(type(select_region))
        self.day7_weather = weather_ip.set_weather(select_region)
        self.show_weather()
        # print(self.day7_weather)
        # return self.day7_weather
        # self.zone_code = config.map[self.province_text][self.city_text]
        # print(self.zone_code)

    def show_weather(self):

# 10;05月11日,周三,暴雨,23～26℃,东南风&#10;05月12日,周四,暴雨,23～24℃,东南风&#10;05月13日,周五,中雨转大雨,22～26℃,北风&#10;05月14日,周六,中雨,18～23℃,东北风&#10;05月15日,周日,中雨,17～21℃,北风&#10;05月16日,周一,阴,16～20℃,北风&#10;05月17日,周二,阴,19～22℃,东北风', 'id': 59287, 'pinyin': 'guangzhou'
        self.ui.resultBrowser.clear()
        text_model = '{},周{},{},气温:{},{}'
        # self.ui.resultBrowser.documentTitle()
        self.ui.resultBrowser.append(self.day7_weather['city'])
        self.text_list = []
        self.text_list.append(self.day7_weather['city'])

        for i in range(1, 8):
            self.text = text_model.format(self.day7_weather['day' + str(i)][5], self.day7_weather['day' + str(i)][1],\
                                                self.day7_weather['day' + str(i)][2], self.day7_weather['day' + str(i)][0], self.day7_weather['day' + str(i)][3])
            self.ui.resultBrowser.append(self.text)
            self.text_list.append(self.text)
        # print(self.text)

    def voice_text(self):
        '''语音播报'''
        engine = pyttsx3.init()
        #说话
        for text in self.text_list:
            engine.say(text)
        #运行
        engine.runAndWait()

app = QApplication([])
# app.setWindowIcon(QIcon('icon/win_icon.gif'))
mainw = MainWindow()
mainw.setWindowTitle('spider天气')
# 禁止最大化按钮（只显示最小化按钮和关闭按钮）
mainw.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint | QtCore.Qt.WindowCloseButtonHint)

# 禁止拉伸窗口大小
mainw.setFixedSize(mainw.width(), mainw.height())
# styles.light(app)
styles.dark(app)
win = windows.ModernWindow(mainw)
win.show()
app.exec_()

