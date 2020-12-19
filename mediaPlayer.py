from PyQt5 import QtWidgets
from ui_mediaPlayer import Ui_MediaPlayer
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, \
	QSlider, QStyle, QSizePolicy, QFileDialog, QMessageBox
import sys
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtGui import QIcon, QPalette
from PyQt5.QtCore import Qt, QUrl

class MediaWindow(QtWidgets.QMainWindow, Ui_MediaPlayer):

	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.show()

	# Functions connecting
		self.actionAdd_File.triggered.connect(self.open_file)
		self.actionQuit.triggered.connect(self.closeEvent)
		self.actionHelp.triggered.connect(self.aboutEvent)
		self.playBtn.clicked.connect(self.play_video)
		self.movieLengthSlider.sliderMoved.connect(self.set_pos)
		self.volumeSlider.sliderMoved.connect(self.set_vol)
		self.volumeBtn.clicked.connect(self.switch_vol)

		self.mediaPlayer.stateChanged.connect(self.mediaPlayOrStop)
		self.mediaPlayer.positionChanged.connect(self.position_changed)
		self.mediaPlayer.durationChanged.connect(self.duration_changed)

	# Functions defining

	def hhmmss(self, ms):
		# s = 1000
		# m = 60000
		# h = 360000
		h, r = divmod(ms, 360000)
		m, r = divmod(r, 60000)
		s, _ = divmod(r, 1000)
		return ("%02d:%02d:%02d" % (h, m, s)) if h else ("%d:%02d" % (m, s))

	# Open file for 'Open File' button in menuBar
	def open_file(self):
		filename, _ = QFileDialog.getOpenFileName(self, "Open Video")

		if filename != '':
			self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(filename)))
			self.playBtn.setEnabled(True)
			self.volumeBtn.setEnabled(True)
	# Close function for quit button in menuBar
	def closeEvent(self, event):
		self.close()

	def aboutEvent(self, event):
		about = QMessageBox.about(self, 'About', "This my first program that was written with pyqt5\n Thanks for using it")
	# Play function
	def play_video(self):
		if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
			self.mediaPlayer.pause()

		else:
			self.mediaPlayer.play()

	# Change pause and play buttons
	def mediaPlayOrStop(self, state):
		if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
			self.playBtn.setIcon(QIcon("images/pause.png"))
		else:
			self.playBtn.setIcon(QIcon("images/play.png"))

	def position_changed(self, position):
		self.movieLengthSlider.setValue(position)
		if position >= 0:
			self.startLabel.setText(self.hhmmss(position))

	def duration_changed(self, duration):
		self.movieLengthSlider.setMaximum(duration)
		if duration >= 0:
			self.fullLabel.setText(self.hhmmss(duration))

	def set_pos(self, pos):
		self.mediaPlayer.setPosition(pos)
	# Volume sliding
	def set_vol(self, vol):
		self.mediaPlayer.setVolume(vol)
		self.volumeLabel.setText(str(vol))
		if vol >= 60:
			self.volumeBtn.setIcon(QIcon("images/volume100.png"))
		elif vol >= 30 and vol <= 59:
			self.volumeBtn.setIcon(QIcon("images/volume60.png"))
		elif vol >= 1 and vol <= 30:
			self.volumeBtn.setIcon(QIcon("images/volume30.png"))
		elif vol == 0:
			self.volumeBtn.setIcon(QIcon("images/novolume.png"))
	# Mute and unmute the video
	def switch_vol(self):
		if self.mediaPlayer.volume() == 0:
			self.set_vol(50)
			self.volumeSlider.setValue(50)
			self.volumeLabel.setText(str(50))
		elif self.mediaPlayer.volume() != 0:
			self.set_vol(0)
			self.volumeSlider.setValue(0)
			self.volumeLabel.setText(str(0))
