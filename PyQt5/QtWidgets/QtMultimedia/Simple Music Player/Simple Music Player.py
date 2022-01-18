import sys

from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QSlider, QFileDialog, QInputDialog, QHBoxLayout, \
	QSizePolicy
from PyQt5.QtGui import QIcon
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtWinExtras import QWinThumbnailToolBar, QWinThumbnailToolButton


class Form(QWidget):
	def __init__(self):
		super().__init__()
		self.init_ui()

	def init_ui(self):
		self.resize(500, 200)
		self.setWindowTitle("Simple Music Player")
		self.play_pause = QPushButton("Play")
		self.play_pause.resize(self.play_pause.sizeHint())
		self.play_pause.setDisabled(True)
		self.position_slider = QSlider(Qt.Horizontal)
		self.position_slider.setMinimum(0)
		self.position_slider.setValue(0)
		self.position_slider.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
		self.volume_slider = QSlider(Qt.Horizontal)
		self.volume_slider.resize(self.volume_slider.sizeHint())
		self.volume_slider.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
		self.volume_slider.setMinimum(0)
		self.volume_slider.setMaximum(100)
		self.volume_slider.setValue(50)
		self.file_button = QPushButton("Choose file")
		self.file_button.resize(self.file_button.sizeHint())
		self.url_button = QPushButton("Play online from a URL")
		self.url_button.resize(self.url_button.sizeHint())
		self.url_button.setToolTip("Requires internet connection")
		self.layout = QHBoxLayout()
		self.layout.addWidget(self.play_pause)
		self.layout.addWidget(self.position_slider)
		self.layout.addWidget(self.volume_slider)
		self.layout.addWidget(self.file_button)
		self.layout.addWidget(self.url_button)
		self.setLayout(self.layout)
		self.player = QMediaPlayer(self, QMediaPlayer.StreamPlayback)
		self.player.setVolume(self.volume_slider.value())
		self.player.durationChanged.connect(lambda: self.position_slider.setMaximum(self.player.duration()))
		self.player.positionChanged.connect(self.update_position)
		self.player.stateChanged.connect(self.on_state_change)
		self.play_pause.clicked.connect(self.play_or_pause)
		self.position_slider.valueChanged.connect(lambda: self.player.setPosition(self.position_slider.value()))
		self.volume_slider.valueChanged.connect(lambda: self.player.setVolume(self.volume_slider.value()))
		self.file_button.clicked.connect(self.open_file_dialog)
		self.url_button.clicked.connect(self.open_url_dialog)
		self.thumbnail_toolbar = QWinThumbnailToolBar(self)
		self.thumbnail_button = QWinThumbnailToolButton(self.thumbnail_toolbar)
		self.thumbnail_button.setIcon(QIcon("play-svg.svg"))
		self.thumbnail_button.setToolTip("Play")
		self.thumbnail_toolbar.addButton(self.thumbnail_button)
		self.thumbnail_button.clicked.connect(self.play_or_pause)
		self.show()

	def open_file_dialog(self):
		file_name = QFileDialog.getOpenFileName(self, "Choose an audio file")
		if file_name[0]:
			reverse = file_name[0][::-1]
			self.setWindowTitle(reverse[:reverse.index("/")][::-1])
			self.content = QMediaContent(QUrl.fromLocalFile(file_name[0]))
			self.player.setMedia(self.content)
			self.play_pause.setEnabled(True)
			self.thumbnail_toolbar.setWindow(self.windowHandle())

	def open_url_dialog(self):
		url, ok = QInputDialog.getText(self, "Enter a URL", "URL")
		if ok:
			self.content = QMediaContent(QUrl(url))
			self.player.setMedia(self.content)
			self.play_pause.setEnabled(True)
			self.thumbnail_toolbar.setWindow(self.windowHandle())

	def play_or_pause(self):
		if self.player.state() == QMediaPlayer.PlayingState:
			self.player.pause()
			self.play_pause.setText("Play")
			self.thumbnail_button.setIcon(QIcon("play-svg.svg"))
			self.thumbnail_button.setToolTip("Play")
		elif self.player.state() != QMediaPlayer.PlayingState:
			self.player.play()
			self.play_pause.setText("Pause")
			self.thumbnail_button.setIcon(QIcon("pause-svg.svg"))
			self.thumbnail_button.setToolTip("Pause")

	def on_state_change(self, state):
		if state == QMediaPlayer.StoppedState:
			self.play_pause.setText("Play")
			self.thumbnail_button.setToolTip("Play")
			self.thumbnail_button.setIcon(QIcon("play-svg.svg"))

	def update_position(self, position):
		# Disable the events to prevent updating triggering a setPosition event (can cause stuttering).
		self.position_slider.blockSignals(True)
		self.position_slider.setValue(position)
		self.position_slider.blockSignals(False)


app = QApplication(sys.argv)
form = Form()
sys.exit(app.exec_())
