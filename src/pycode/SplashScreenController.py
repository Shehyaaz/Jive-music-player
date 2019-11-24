from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from SplashScreenUI import Ui_SplashWindow

class SplashScreenController(QMainWindow,Ui_SplashWindow):
    def __init__(self, *args, **kwargs):
        super(SplashScreenController, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.show()
        self.frame.anim.start()