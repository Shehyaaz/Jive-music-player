from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from SplashScreenUI import Ui_SplashWindow
from AboutWindowUI import Ui_aboutWindow
import NewPlaylistDialogUI
import SelectPlaylistUI
import DeletePlaylistUI
import DeleteFavUI
import DeleteSongUI
from SongInfoUI import Ui_SongInfo
from SongLyricsUI import Ui_SongLyrics

def centerWindow(window):
    qtRectangle = window.frameGeometry()
    centerPoint = QDesktopWidget().availableGeometry().center()
    qtRectangle.moveCenter(centerPoint)
    window.move(qtRectangle.topLeft())

class SplashScreenController(QMainWindow,Ui_SplashWindow):
    def __init__(self, *args, **kwargs):
        super(SplashScreenController, self).__init__(*args, **kwargs)
        self.setupUi(self)
        centerWindow(self)
        self.show()
        self.frame.anim.start()


class AboutWindowController(QMainWindow, Ui_aboutWindow):
    def __init__(self,*args,**kwargs):
        super(AboutWindowController,self).__init__(*args,**kwargs)
        self.setupUi(self)
        self.pushButton.pressed.connect(self.close)
        centerWindow(self)
        self.show()

class NewPlaylistDialogController(QDialog, NewPlaylistDialogUI.Ui_Dialog):
    def __init__(self,parent,defaultTheme,*args,**kwargs):
        super(NewPlaylistDialogController,self).__init__(parent,*args,**kwargs)
        self.setupUi(self,defaultTheme)

class DeletePlaylistController(QDialog, DeletePlaylistUI.Ui_Dialog):
    def __init__(self,parent,defaultTheme,*args,**kwargs):
        super(DeletePlaylistController,self).__init__(parent,*args,**kwargs)
        self.setupUi(self,defaultTheme)

class SelectPlaylistController(QDialog, SelectPlaylistUI.Ui_Dialog):
    def __init__(self,parent,defaultTheme,*args,**kwargs):
        super(SelectPlaylistController,self).__init__(parent,*args,**kwargs)
        self.setupUi(self,defaultTheme)

class DeleteFavController(QDialog, DeleteFavUI.Ui_Dialog):
    def __init__(self,parent,defaultTheme,*args,**kwargs):
        super(DeleteFavController,self).__init__(parent,*args,**kwargs)
        self.setupUi(self,defaultTheme)

class DeleteSongController(QDialog, DeleteSongUI.Ui_Dialog):
    def __init__(self,parent,defaultTheme,*args,**kwargs):
        super(DeleteSongController,self).__init__(parent,*args,**kwargs)
        self.setupUi(self,defaultTheme)

class SongInfoController(QMainWindow,Ui_SongInfo):
    def __init__(self, *args, **kwargs):
        super(SongInfoController, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.pushButton.pressed.connect(self.close)
        centerWindow(self)
        self.show()