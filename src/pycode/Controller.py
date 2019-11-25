from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from SplashScreenUI import Ui_SplashWindow
from AboutWindowUI import Ui_aboutWindow
from NewPlaylistDialog import Ui_Dialog

class SplashScreenController(QMainWindow,Ui_SplashWindow):
    def __init__(self, *args, **kwargs):
        super(SplashScreenController, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.show()
        self.frame.anim.start()


class AboutWindowController(QMainWindow, Ui_aboutWindow):
    def __init__(self,*args,**kwargs):
        super(AboutWindowController,self).__init__(*args,**kwargs)
        self.setupUi(self)
        self.
        self.show()

class NewPlaylistDialogController(QMainWindow, Ui_aboutWindow):
    def __init__(self,*args,**kwargs):
        super(AboutWindowController,self).__init__(*args,**kwargs)
        self.setupUi(self)
        self.show()