# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(715, 566)
        self.locationButton = QPushButton(Form)
        self.locationButton.setObjectName(u"locationButton")
        self.locationButton.setGeometry(QRect(30, 30, 121, 41))
        font = QFont()
        font.setFamily(u"\u5b8b\u4f53")
        font.setPointSize(12)
        self.locationButton.setFont(font)
        self.locationButton.setAutoDefault(False)
        self.provinceBox = QComboBox(Form)
        self.provinceBox.setObjectName(u"provinceBox")
        self.provinceBox.setGeometry(QRect(180, 30, 111, 41))
        self.provinceBox.setFont(font)
        self.provinceBox.setEditable(False)
        self.cityBox = QComboBox(Form)
        self.cityBox.setObjectName(u"cityBox")
        self.cityBox.setGeometry(QRect(380, 30, 111, 41))
        self.cityBox.setFont(font)
        self.resultBrowser = QTextBrowser(Form)
        self.resultBrowser.setObjectName(u"resultBrowser")
        self.resultBrowser.setGeometry(QRect(26, 120, 661, 421))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.resultBrowser.sizePolicy().hasHeightForWidth())
        self.resultBrowser.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamily(u"\u5b8b\u4f53")
        font1.setPointSize(14)
        font1.setBold(False)
        font1.setWeight(50)
        self.resultBrowser.setFont(font1)
        self.resultBrowser.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.resultBrowser.setStyleSheet(u"text-align:center;\n"
"line-height:30px;\n"
"")
        self.resultBrowser.setLineWidth(4)
        self.resultBrowser.setCursorWidth(0)
        self.verticalScrollBar = QScrollBar(Form)
        self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        self.verticalScrollBar.setGeometry(QRect(930, 110, 21, 431))
        self.verticalScrollBar.setOrientation(Qt.Vertical)
        self.voice_Button = QPushButton(Form)
        self.voice_Button.setObjectName(u"voice_Button")
        self.voice_Button.setGeometry(QRect(540, 30, 121, 41))
        self.voice_Button.setFont(font)
        self.voice_Button.setAutoDefault(False)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.locationButton.setText(QCoreApplication.translate("Form", u"\u5b9a\u4f4d\u5931\u8d25", None))
        self.resultBrowser.setDocumentTitle("")
        self.resultBrowser.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'\u5b8b\u4f53'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.voice_Button.setText("")
    # retranslateUi

