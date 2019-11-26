# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/shehyaaz/PycharmProjects/JiveMusicPlayer/venv/src/ui/songlyrics.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SongLyrics(object):
    def setupUi(self, SongLyrics):
        SongLyrics.setObjectName("SongLyrics")
        SongLyrics.resize(342, 392)
        self.centralwidget = QtWidgets.QWidget(SongLyrics)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-1, -11, 361, 431))
        self.frame.setStyleSheet("background-color: rgb(114, 159, 207);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.textEdit = QtWidgets.QTextEdit(self.frame)
        self.textEdit.setGeometry(QtCore.QRect(10, 20, 321, 341))
        self.textEdit.setStyleSheet("background-color: rgb(238, 238, 236);")
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(130, 370, 89, 25))
        self.pushButton.setStyleSheet("background-color: rgb(238, 238, 236);")
        self.pushButton.setObjectName("pushButton")
        SongLyrics.setCentralWidget(self.centralwidget)

        self.retranslateUi(SongLyrics)
        QtCore.QMetaObject.connectSlotsByName(SongLyrics)

    def retranslateUi(self, SongLyrics):
        _translate = QtCore.QCoreApplication.translate
        SongLyrics.setWindowTitle(_translate("SongLyrics", "Lyrics"))
        self.textEdit.setPlaceholderText(_translate("SongLyrics", "Lyrics"))
        self.pushButton.setText(_translate("SongLyrics", "OK"))
