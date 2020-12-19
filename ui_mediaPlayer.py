# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mediaPlayer.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QUrl, QSize
# PyQt5 Multimedia imports for media playing
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget

# GUI media class
class Ui_MediaPlayer(object):
    def setupUi(self, MediaPlayer):
        MediaPlayer.setObjectName("MediaPlayer")
        MediaPlayer.setMinimumSize(QSize(720,480))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        MediaPlayer.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/player.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MediaPlayer.setWindowIcon(icon)
        MediaPlayer.setStyleSheet("background-color: #EDEDED;")
        self.centralwidget = QtWidgets.QWidget(MediaPlayer)
        self.centralwidget.setObjectName("centralwidget")
        MediaPlayer.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MediaPlayer)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 762, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.menubar.setFont(font)
        self.menubar.setStyleSheet("border-bottom: 1px solid black;")
        self.menubar.setObjectName("menubar")

        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuApp = QtWidgets.QMenu(self.menubar)
        self.menuApp.setObjectName("menuApp")
        MediaPlayer.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MediaPlayer)
        self.statusbar.setObjectName("statusbar")
        MediaPlayer.setStatusBar(self.statusbar)
        self.actionAdd_File = QtWidgets.QAction(MediaPlayer)
        self.actionAdd_File.setObjectName("actionAdd_File")
        self.actionHelp = QtWidgets.QAction(MediaPlayer)
        self.actionHelp.setObjectName("actionHelp")
        self.actionQuit = QtWidgets.QAction(MediaPlayer)
        self.actionQuit.setObjectName("actionQuit")
        self.menuFile.addAction(self.actionAdd_File)
        self.menuApp.addAction(self.actionHelp)
        self.menuApp.addAction(self.actionQuit)
        self.menubar.addAction(self.menuApp.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())

        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)

        # create videowidget object

        videowidget = QVideoWidget()

        # Play button
        self.playBtn = QtWidgets.QPushButton()
        self.playBtn.setEnabled(False)
        self.playBtn.setIcon(QIcon("images/play.png"))
        self.playBtn.setIconSize(QtCore.QSize(50, 50))
        self.playBtn.setStyleSheet("QPushButton {\n"
                                      "   background-color: transparent;\n"
                                      "    border-radius: 50%;\n"
                                      "    color: orange;\n"
                                      "    border: none;\n"
                                        "    width: 50px;\n"
                                        "    height: 50px;\n"
                                      "}\n")
        #  Start Label time
        self.startLabel = QtWidgets.QLabel()
        self.startLabel.setText('00:00')
        labelfont = QtGui.QFont()
        labelfont.setFamily("Arial")
        labelfont.setPointSize(16)
        self.startLabel.setFont(labelfont)

        # Movie length slider
        self.movieLengthSlider = QtWidgets.QSlider(Qt.Horizontal)
        self.movieLengthSlider.setRange(0,0)

        # Full length of the movie
        self.fullLabel = QtWidgets.QLabel()
        self.fullLabel.setText('00:00')
        self.fullLabel.setFont(labelfont)

        # Volume button
        self.volumeBtn = QtWidgets.QPushButton()
        self.volumeBtn.setEnabled(False)

        self.volumeBtn.setIcon(QIcon("images/volume60.png"))
        self.volumeBtn.setIconSize(QtCore.QSize(50, 50))
        self.volumeBtn.setStyleSheet("QPushButton {\n"
                                   "   background-color: transparent;\n"
                                   "    border-radius: 50%;\n"
                                   "    color: rgb(0, 0, 0);\n"
                                   "    border: none;\n"
                                   "    width: 50px;\n"
                                   "    height: 50px;\n"
                                   "}\n")


        # Movie volume slider
        self.volumeSlider = QtWidgets.QSlider(Qt.Horizontal)
        self.volumeSlider.setRange(0, 0)
        self.volumeSlider.setFocusPolicy(Qt.StrongFocus)
        self.volumeSlider.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.volumeSlider.setSingleStep(1)
        self.volumeSlider.setMinimum(0)
        self.volumeSlider.setMaximum(100)
        self.volumeSlider.setValue(50)
        self.volumeSlider.setStyleSheet("QSlider {\n"
                                      "    width: 50px;\n"
                                     "    height: 30px;\n"
                                     "}\n")
        self.volumeSlider.setMaximumSize(100, 30)

        self.volumeLabel = QtWidgets.QLabel()
        self.volumeLabel.setText('50')
        self.volumeLabel.setFont(labelfont)
        self.volumeLabel.setStyleSheet("QPushButton {\n"
                                     "   background-color: transparent;\n"
                                     "    color: rgb(0, 0, 0);\n"
                                     "    border: none;\n"
                                     "    width: 30px;\n"
                                     "    height: 50px;\n"
                                     "}\n")


        # Horizontal box for navigation
        self.hboxLayout = QtWidgets.QHBoxLayout()
        self.hboxLayout.setContentsMargins(0, 0, 0, 0)
        self.hboxLayout.addWidget(self.playBtn)
        self.hboxLayout.addWidget(self.startLabel)
        self.hboxLayout.addWidget(self.movieLengthSlider)
        self.hboxLayout.addWidget(self.fullLabel)
        self.hboxLayout.addWidget(self.volumeBtn)
        self.hboxLayout.addWidget(self.volumeSlider)

        # Vertical widget for all media
        self.vboxLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.vboxLayout.addWidget(videowidget)
        self.vboxLayout.addLayout(self.hboxLayout)

        self.setLayout(self.vboxLayout)
        self.mediaPlayer.setVideoOutput(videowidget)

        self.retranslateUi(MediaPlayer)
        QtCore.QMetaObject.connectSlotsByName(MediaPlayer)

    def retranslateUi(self, MediaPlayer):
        _translate = QtCore.QCoreApplication.translate
        MediaPlayer.setWindowTitle(_translate("MediaPlayer", "MediaPlayer"))
        self.menuFile.setTitle(_translate("MediaPlayer", "File"))
        self.menuApp.setTitle(_translate("MediaPlayer", "App"))
        self.actionAdd_File.setText(_translate("MediaPlayer", "Open File"))
        self.actionHelp.setText(_translate("MediaPlayer", "About"))
        self.actionQuit.setText(_translate("MediaPlayer", "Quit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MediaPlayer = QtWidgets.QMainWindow()
    ui = Ui_MediaPlayer()
    ui.setupUi(MediaPlayer)
    MediaPlayer.show()
    sys.exit(app.exec_())
