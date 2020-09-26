# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/shehyaaz/PycharmProjects/JiveMusicPlayer/venv/src/ui/songinfo.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SongInfo(object):
    def setupUi(self, SongInfo):
        SongInfo.setObjectName("SongInfo")
        SongInfo.resize(478, 230)
        self.centralwidget = QtWidgets.QWidget(SongInfo)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(-1, -1, 491, 411))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.frame.setStyleSheet("background-color: rgb(114, 159, 207);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.artistfield = QtWidgets.QLineEdit(self.frame)
        self.artistfield.setGeometry(QtCore.QRect(130, 20, 311, 25))
        self.artistfield.setStyleSheet("background-color: rgb(238, 238, 236);")
        self.artistfield.setReadOnly(True)
        self.artistfield.setObjectName("artistfield")
        self.artist = QtWidgets.QLabel(self.frame)
        self.artist.setGeometry(QtCore.QRect(9, 20, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.artist.setFont(font)
        self.artist.setStyleSheet("color: rgb(238, 238, 236);")
        self.artist.setAlignment(QtCore.Qt.AlignCenter)
        self.artist.setObjectName("artist")
        self.track = QtWidgets.QLabel(self.frame)
        self.track.setGeometry(QtCore.QRect(10, 70, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.track.setFont(font)
        self.track.setStyleSheet("color: rgb(238, 238, 236);")
        self.track.setAlignment(QtCore.Qt.AlignCenter)
        self.track.setObjectName("track")
        self.trackfield = QtWidgets.QLineEdit(self.frame)
        self.trackfield.setGeometry(QtCore.QRect(130, 70, 311, 25))
        self.trackfield.setStyleSheet("background-color: rgb(238, 238, 236);")
        self.trackfield.setReadOnly(True)
        self.trackfield.setObjectName("trackfield")
        self.releasedate = QtWidgets.QLabel(self.frame)
        self.releasedate.setGeometry(QtCore.QRect(10, 120, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.releasedate.setFont(font)
        self.releasedate.setStyleSheet("color: rgb(238, 238, 236);")
        self.releasedate.setAlignment(QtCore.Qt.AlignCenter)
        self.releasedate.setObjectName("releasedate")
        self.releasedatefield = QtWidgets.QLineEdit(self.frame)
        self.releasedatefield.setGeometry(QtCore.QRect(130, 120, 311, 25))
        self.releasedatefield.setStyleSheet("background-color: rgb(238, 238, 236);")
        self.releasedatefield.setReadOnly(True)
        self.releasedatefield.setObjectName("releasedatefield")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(200, 180, 89, 25))
        self.pushButton.setStyleSheet("background-color: rgb(238, 238, 236);")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.frame)
        SongInfo.setCentralWidget(self.centralwidget)

        self.retranslateUi(SongInfo)
        QtCore.QMetaObject.connectSlotsByName(SongInfo)

    def retranslateUi(self, SongInfo):
        _translate = QtCore.QCoreApplication.translate
        SongInfo.setWindowTitle(_translate("SongInfo", "Song Information"))
        self.artist.setText(_translate("SongInfo", "Artist :"))
        self.track.setText(_translate("SongInfo", "Track :"))
        self.releasedate.setText(_translate("SongInfo", "Release Date :"))
        self.pushButton.setText(_translate("SongInfo", "OK"))
