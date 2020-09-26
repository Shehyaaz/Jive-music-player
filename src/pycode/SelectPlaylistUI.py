# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/shehyaaz/PycharmProjects/JiveMusicPlayer/venv/src/ui/select_playlist.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog, defaultTheme):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog.resize(400, 100)
        if defaultTheme:
            Dialog.setStyleSheet("background-color: rgb(114, 159, 207);")
        else:
            Dialog.setStyleSheet("background-color: rgb(150, 150, 150);")
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(40, 60, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 131, 31))
        self.label.setStyleSheet("color: rgb(238, 238, 236);\n"
"font: 14pt \"Ubuntu\";")
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(150, 20, 221, 31))
        self.comboBox.setStyleSheet("background-color: rgb(238, 238, 236);")
        self.comboBox.setObjectName("comboBox")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Select Playlist"))
        self.label.setText(_translate("Dialog", "Playlist Name:"))
