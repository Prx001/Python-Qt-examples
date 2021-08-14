# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'splash_screenuuZZib.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen):
        if not SplashScreen.objectName():
            SplashScreen.setObjectName(u"SplashScreen")
        SplashScreen.resize(340, 340)
        self.centralwidget = QWidget(SplashScreen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.circularProgressBarBase = QFrame(self.centralwidget)
        self.circularProgressBarBase.setObjectName(u"circularProgressBarBase")
        self.circularProgressBarBase.setGeometry(QRect(10, 10, 320, 320))
        self.circularProgressBarBase.setFrameShape(QFrame.NoFrame)
        self.circularProgressBarBase.setFrameShadow(QFrame.Raised)
        self.circularProgress = QFrame(self.circularProgressBarBase)
        self.circularProgress.setObjectName(u"circularProgress")
        self.circularProgress.setGeometry(QRect(10, 10, 300, 300))
        self.circularProgress.setStyleSheet(u"QFrame {\n"
"	border-radius: 150px;\n"
"	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.999 rgba(255, 0, 127, 0), stop:1.0 rgba(85, 170, 255, 255));\n"
"}")
        self.circularProgress.setFrameShape(QFrame.NoFrame)
        self.circularProgress.setFrameShadow(QFrame.Raised)
        self.circularBg = QFrame(self.circularProgressBarBase)
        self.circularBg.setObjectName(u"circularBg")
        self.circularBg.setGeometry(QRect(10, 10, 300, 300))
        self.circularBg.setStyleSheet(u"QFrame {\n"
"	border-radius: 150px;\n"
"	background-color: rgba(77, 77, 127, 0);\n"
"}")
        self.circularBg.setFrameShape(QFrame.NoFrame)
        self.circularBg.setFrameShadow(QFrame.Raised)
        self.container = QFrame(self.circularProgressBarBase)
        self.container.setObjectName(u"container")
        self.container.setGeometry(QRect(25, 25, 270, 270))
        self.container.setStyleSheet(u"QFrame {\n"
"	border-radius: 135px;\n"
"	background-color: rgb(77, 77, 127);\n"
"}\n"
"")
        self.container.setFrameShape(QFrame.NoFrame)
        self.container.setFrameShadow(QFrame.Raised)
        self.layoutWidget = QWidget(self.container)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(30, 56, 210, 172))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.name_label = QLabel(self.layoutWidget)
        self.name_label.setObjectName(u"name_label")
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(12)
        self.name_label.setFont(font)
        self.name_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: none;")
        self.name_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.name_label, 0, 0, 1, 1)

        self.percentage = QLabel(self.layoutWidget)
        self.percentage.setObjectName(u"percentage")
        font1 = QFont()
        font1.setFamily(u"Roboto Th")
        font1.setPointSize(40)
        self.percentage.setFont(font1)
        self.percentage.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: none;")
        self.percentage.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.percentage, 1, 0, 1, 1)

        self.circularBg.raise_()
        self.circularProgress.raise_()
        self.container.raise_()
        SplashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashScreen)

        QMetaObject.connectSlotsByName(SplashScreen)
    # setupUi

    def retranslateUi(self, SplashScreen):
        SplashScreen.setWindowTitle(QCoreApplication.translate("SplashScreen", u"MainWindow", None))
        self.name_label.setText(QCoreApplication.translate("SplashScreen", u"<html><head/><body><p>Your Application Name!</p></body></html>", None))
        self.percentage.setText(QCoreApplication.translate("SplashScreen", u"<p><span style=\"font-size:68pt;\">0</span><span style=\"font-size: 58pt; vertical-align: super;\">%</span></p>", None))
    # retranslateUi    