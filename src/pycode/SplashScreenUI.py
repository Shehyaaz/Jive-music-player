# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/shehyaaz/PycharmProjects/JiveMusicPlayer/venv/src/ui/splashscreen.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class AnimatedFrame(QtWidgets.QFrame):
    def __init__(self, *args):
        super(AnimatedFrame,self).__init__(*args)
        bytear = QtCore.QByteArray()
        bytear.append('bgcolor')
        self.anim = QtCore.QPropertyAnimation(self,bytear)
        self.anim.setStartValue(QtGui.QColor(236,236,236))
        self.anim.setKeyValueAt(0.5, QtGui.QColor(117,80,123))
        self.anim.setEndValue(QtGui.QColor(52,120,184))
        self.anim.setDuration(2500)
        self.anim.setLoopCount(1)

    def getBackColor(self):
        return self.palette().color(self.pal_ele)

    def setBackColor(self, col):
        bg = "background-color: rgb(%d,%d,%d);"%(col.red(),col.green(),col.blue())
        self.setStyleSheet(bg)

    pal_ele = QtGui.QPalette.Window
    bgcolor = QtCore.pyqtProperty(QtGui.QColor,getBackColor,setBackColor)

class Ui_SplashWindow(object):
    def setupUi(self, SplashWindow):
        SplashWindow.setObjectName("SplashWindow")
        SplashWindow.resize(500, 400)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../resources/images/app_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SplashWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(SplashWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(-10, -10, 511, 421))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        # self.frame = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.frame = AnimatedFrame(self.verticalLayoutWidget)
        #self.frame.setStyleSheet("background-color:rgb(52, 101, 164);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(60, 130, 381, 161))
        self.label.setStyleSheet("color:rgb(238, 238, 236);\n"
"font: 75 25pt \"Waree\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(220, 120, 51, 51))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../../resources/images/app_icon.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(20, 380, 431, 17))
        self.label_3.setStyleSheet("color:rgb(238, 238, 236)")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(370, 380, 21, 17))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("../../resources/images/copyright.png"))
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.frame)
        SplashWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashWindow)
        QtCore.QMetaObject.connectSlotsByName(SplashWindow)

    def retranslateUi(self, SplashWindow):
        _translate = QtCore.QCoreApplication.translate
        SplashWindow.setWindowTitle(_translate("SplashWindow", "Jive Music Player"))
        self.label.setText(_translate("SplashWindow", "Jive Music Player"))
        self.label_3.setText(_translate("SplashWindow", "Jive Music Player All Rights Reserved"))
