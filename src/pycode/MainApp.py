from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *

from MainWindow import Ui_MainWindow
from Controller import *
import sys,time

from mutagen.id3 import ID3
from PIL import Image
from PIL.ImageQt import ImageQt
from io import BytesIO

def hhmmss(ms):
    # s = 1000
    # m = 60000
    # h = 3600000000
    h, r = divmod(ms, 3600000000)
    m, r = divmod(r, 60000)
    s, _ = divmod(r, 1000)
    return ("%d:%02d:%02d" % (h,m,s)) if h else ("%d:%02d" % (m,s))

class ViewerWindow(QMainWindow):
    state = pyqtSignal(bool)

    def closeEvent(self, e):
        # Emit the window state, to update the viewer toggle button.
        self.state.emit(False)


class PlaylistModel(QAbstractListModel):
    def __init__(self, playlist, *args, **kwargs):
        super(PlaylistModel, self).__init__(*args, **kwargs)
        self.playlist = playlist

    def data(self, index, role):
        if role == Qt.DisplayRole:
            media = self.playlist.media(index.row())
            return media.canonicalUrl().fileName()

    def rowCount(self, index):
        return self.playlist.mediaCount()


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.audio_list = []
        self.audioTag = None
        self.defaultTheme = True
        #displaying splash screen
        self.splash = SplashScreenController(self)
        QTimer.singleShot(3000,self.setUpMainWindow)

    def setUpMainWindow(self):
        self.splash.close()
        self.setupUi(self)

        # Connect controllers to menu items
        # File menu items
        self.menuPlay.triggered.connect(self.open_file)
        self.add_to_fav.triggered.connect(self.addToFav)
        self.add_to_playlist.triggered.connect(self.addToPlaylist)
        self.rem_from_playlist.triggered.connect(self.remFromPlaylist)
        self.exit_player.triggered.connect(self.close)
        # Playlist menu items
        self.new_playlist.triggered.connect(self.newPlaylist)
        self.play_playlist.triggered.connect(self.playPlaylist)
        self.delete_playlist.triggered.connect(self.deletePlaylist)
        # Favourite menu items
        self.play_fav.triggered.connect(self.playFav)
        self.rem_from_fav.triggered.connect(self.remFromFav)
        # Preferences menu items
        self.actionDefault.triggered.connect(self.defaultPalette)
        self.actionFusion.triggered.connect(self.darkPalette)
        # Help menu items
        self.about.triggered.connect(self.displayAbout)

        # Create media player
        self.player = QMediaPlayer()
        self.player.error.connect(lambda : self.alert("error","Playlist Error", "An error has occurred when connecting to playlist"))

        # Setup the playlist.
        self.playlist = QMediaPlaylist()
        self.playlist.setPlaybackMode(QMediaPlaylist.Loop)
        self.player.setPlaylist(self.playlist)

        # Create Playlist view
        self.model = PlaylistModel(self.playlist)
        self.playlistView.setModel(self.model)
        self.playlist.currentIndexChanged.connect(self.playlist_position_changed)
        selection_model = self.playlistView.selectionModel()
        selection_model.selectionChanged.connect(self.playlist_selection_changed)

        # Connect control buttons/slides for media player.
        self.playButton.pressed.connect(self.playMusic)
        self.stopButton.pressed.connect(self.playStop)
        self.volumeSlider.valueChanged.connect(self.changeVolume)
        self.previousButton.pressed.connect(self.playlist.previous)
        self.nextButton.pressed.connect(self.playlist.next)
        self.infoButton.pressed.connect(self.songInfo)

        # Updating media player duration
        self.player.durationChanged.connect(self.update_duration)
        self.player.positionChanged.connect(self.update_position)
        self.timeSlider.valueChanged.connect(self.player.setPosition)

        self.setAcceptDrops(True)
        centerWindow(self)
        self.show()

    def dragEnterEvent(self, e):
        if e.mimeData().hasUrls():
            e.acceptProposedAction()

    def dropEvent(self, e):
        for url in e.mimeData().urls():
            self.playlist.addMedia(
                QMediaContent(url)
            )
        self.model.layoutChanged.emit()
        # If not playing, seeking to first of newly added + play.
        if self.player.state() != QMediaPlayer.PlayingState:
            i = self.playlist.mediaCount() - len(e.mimeData().urls())
            self.playlist.setCurrentIndex(i)
            self.player.play()

    def open_file(self):
        filter = "Audio Files (*.mp3 *.ogg *.wav *.m4a)"
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.ExistingFiles)
        path,_ = file_dialog.getOpenFileNames(self, "Play Now", "", filter)
        if path:
            for p in path:
                self.playlist.addMedia(
                    QMediaContent(
                        QUrl.fromLocalFile(p)
                    )
                )
                self.audio_list.append(p)
        self.model.layoutChanged.emit()

    def addToFav(self):
        filter = "Audio Files (*.mp3 *.ogg *.wav *.m4a)"
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.ExistingFiles)
        path, _ = file_dialog.getOpenFileNames(self, "Add to Favourites", "", filter)
        if path :
            for p in path :
                # add to favourites table
                pass

    def addToPlaylist(self):
        self.dialog = SelectPlaylistController(self, self.defaultTheme)
        # show playlist names from database
        self.dialog.show()
        if self.dialog.exec_():
            # save playlist name and open files
            print("OK")


    def remFromPlaylist(self):
        self.dialog = DeleteSongController(self, self.defaultTheme)
        # show playlist names from database
        self.dialog.show()
        if self.dialog.exec_():
            # delete playlist
            print("OK")

    def newPlaylist(self):
        self.dialog = NewPlaylistDialogController(self,self.defaultTheme)
        self.dialog.show()
        if self.dialog.exec_():
            # add playlist to database
            print("OK")

    def playPlaylist(self):
        self.dialog = SelectPlaylistController(self, self.defaultTheme)
        # show playlist names from database
        self.dialog.show()
        if self.dialog.exec_():
            # play playlist
            print("OK")

    def deletePlaylist(self):
        self.dialog = DeletePlaylistController(self, self.defaultTheme)
        # show playlist names from database
        self.dialog.show()
        if self.dialog.exec_():
            # delete playlist
            print("OK")

    def playFav(self):
        # from database get the urls of songs
        pass

    def remFromFav(self):
        self.dialog = DeleteFavController(self, self.defaultTheme)
        # show playlist names from database
        self.dialog.show()
        if self.dialog.exec_():
            # delete the selected song names
            print("OK")

    def defaultPalette(self):
        self.setStyleSheet("")
        self.defaultTheme = True

    def darkPalette(self):
        stylesheet = "background-color: rgb(150, 150, 150)"
        self.setStyleSheet(stylesheet)
        self.defaultTheme = False

    def displayAbout(self):
        self.aboutWindow = AboutWindowController(self)
        if not self.defaultTheme:
            self.aboutWindow.frame.setStyleSheet("background-color: rgb(150, 150, 150)")

    def addAlbumArt(self):
        try :
            img = Image.open(BytesIO(self.audioTag.get("APIC:").data))
            qim = ImageQt(img)
            self.songThumbnail.setPixmap(QPixmap.fromImage(qim))
        except Exception:
            self.songThumbnail.setPixmap(QPixmap("../../resources/images/coverart.jpeg"))

    # def previousSong(self):
    #     if self.playlist.isEmpty():
    #         self.alert("warn","Select Audio","Please select some audio files")
    #     else :
    #         if self.playlist.previous() == None:
    #             self.playlist.setCurrentIndex(self.playlist.mediaCount()-1)
    #         else :
    #             self.playlist.setCurrentIndex(self.playlist.previousIndex())
    #         self.playMusic()

    # def nextSong(self):
    #     if self.playlist.isEmpty():
    #         self.alert("warn","Select Audio","Please select some audio files")
    #     else:
    #         if self.playlist.next() == None:
    #             self.playlist.setCurrentIndex(0)
    #         else :
    #             self.playlist.setCurrentIndex(self.playlist.currentIndex()+1)
    #         #self.playMusic()

    def getSongInfo(self, audio):
        try :
            artist = audio['TPE1'].text[0]
            track = audio["TIT2"].text[0]
            releasedate = audio["TDRC"].text[0]
        except Exception:
            if artist == None :
                artist = "Not Found"
            if track == None :
                track = "Not Found"
            if releasedate == None :
                releasedate = "Not Found"
        return (artist, track, releasedate)

    def songInfo(self):
        if self.playlist.isEmpty():
            self.alert("warn", "Select Audio", "Please select some audio files")
        else :
            self.song_info = SongInfoController(self)
            if not self.defaultTheme:
                self.song_info.frame.setStyleSheet("background-color: rgb(150, 150, 150)")
            artist, track, releasedate = self.getSongInfo(self.audioTag)
            self.song_info.artistfield.setText(artist)
            self.song_info.trackfield.setText(track)
            self.song_info.releasedatefield.setText(str(releasedate))
            self.song_info.show()


    def playStop(self):
        if self.playlist.isEmpty():
            self.alert("warn","Select Audio","Please select some audio files")
        else :
            if self.player.state() == QMediaPlayer.PlayingState:
                icon = QIcon()
                icon.addPixmap(QPixmap("../../resources/images/play.png"), QIcon.Normal, QIcon.Off)
                self.playButton.setIcon(icon)
                self.player.stop()

    def playMusic(self):
        if not self.playlist.isEmpty() :
            if self.player.state() != QMediaPlayer.PlayingState:
                icon = QIcon()
                icon.addPixmap(QPixmap("../../resources/images/pause.png"),QIcon.Normal, QIcon.Off)
                self.playButton.setIcon(icon)
                self.player.play()

            elif self.player.state() == QMediaPlayer.PlayingState:
                icon = QIcon()
                icon.addPixmap(QPixmap("../../resources/images/play.png"),QIcon.Normal, QIcon.Off)
                self.playButton.setIcon(icon)
                self.player.pause()
        else :
            self.alert("warn", "Select Audio", "Please select some audio files")

    def update_duration(self, duration):
        #print("!", duration)
        #print("?", self.player.duration())
        self.timeSlider.setMaximum(duration)
        if duration >= 0:
            self.totalTimeLabel.setText(hhmmss(duration))

    def update_position(self, position):
        if position >= 0:
            self.currentTimeLabel.setText(hhmmss(position))
        # Disable the events to prevent updating triggering a setPosition event (can cause stuttering).
        self.timeSlider.blockSignals(True)
        self.timeSlider.setValue(position)
        self.timeSlider.blockSignals(False)

    def changeVolume(self):
        vol = self.volumeSlider.value()
        if vol == 0:
            self.volume.setPixmap(QPixmap("../../resources/images/volume-mute.png"))
        elif vol < 50:
            self.volume.setPixmap(QPixmap("../../resources/images/volume-down.png"))
        else :
            self.volume.setPixmap(QPixmap("../../resources/images/volume-up.png"))
        self.player.setVolume(vol)


    def playlist_selection_changed(self, ix):
        # We receive a QItemSelection from selectionChanged.
        i = ix.indexes()[0].row()
        self.audioTag = ID3(self.audio_list[i])
        self.addAlbumArt()
        self.playlist.setCurrentIndex(i)

    def playlist_position_changed(self, i):
        if i > -1:
            ix = self.model.index(i)
            self.playlistView.setCurrentIndex(ix)

    def toggle_viewer(self, state):
        if state:
            self.viewer.show()
        else:
            self.viewer.hide()

    def alert(self, type, title, text):
        msg = QMessageBox(self)
        if type == "info":
            msg.setIcon(QMessageBox.Information)
        elif type == "warn":
            msg.setIcon(QMessageBox.Warning)
        elif type == "error":
            msg.setIcon(QMessageBox.Critical)
        msg.setWindowTitle(title)
        msg.setText(text)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.show()

if __name__ == '__main__':
    try :
        app = QApplication([])
        app.setApplicationName("Jive Music Player")
        app.setStyle("Fusion")
        window = MainWindow()
        sys.exit(app.exec_())
    except Exception:
        print("Something unexpected has occurred:(")

#end of program

