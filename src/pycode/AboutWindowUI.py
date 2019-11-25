# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/shehyaaz/PycharmProjects/JiveMusicPlayer/venv/src/ui/aboutwindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_aboutWindow(object):
    def setupUi(self, aboutWindow):
        aboutWindow.setObjectName("aboutWindow")
        aboutWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        aboutWindow.resize(300, 201)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../resources/images/about.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        aboutWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(aboutWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(-10, 0, 311, 201))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.frame.setStyleSheet("background-color: rgb(114, 159, 207);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(20, 10, 81, 31))
        self.label.setStyleSheet("color:rgb(238, 238, 236);\n"
"font: 57 18pt \"Ubuntu\";")
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(self.frame)
        self.textEdit.setGeometry(QtCore.QRect(20, 40, 281, 121))
        self.textEdit.setStyleSheet("background-color:rgb(238, 238, 236);")
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(110, 170, 89, 25))
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.frame)
        aboutWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(aboutWindow)
        QtCore.QMetaObject.connectSlotsByName(aboutWindow)

    def retranslateUi(self, aboutWindow):
        _translate = QtCore.QCoreApplication.translate
        aboutWindow.setWindowTitle(_translate("aboutWindow", "About"))
        self.label.setText(_translate("aboutWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">About</span></p></body></html>"))
        self.textEdit.setHtml(_translate("aboutWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Jive Music Player </span>is a multimedia application </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">to play your locally downloaded songs.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;\">Developed by :</span><span style=\" font-weight:600;\"> Shakshi, Shivangi, Riyanchhi and Shehyaaz.</span></p></body></html>"))
        self.pushButton.setText(_translate("aboutWindow", "OK"))
