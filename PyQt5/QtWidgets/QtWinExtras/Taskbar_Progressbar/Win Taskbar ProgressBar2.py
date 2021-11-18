import sys

from PySide2.QtCore import QBasicTimer
from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QCheckBox, QHBoxLayout
from PySide2.QtGui import QIcon
from PySide2.QtWinExtras import QWinTaskbarButton


class Form(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.resize(500, 300)
		self.setWindowTitle("Windows Taskbar ProgressBar")
		self.start_stop_button = QPushButton("Start")
		self.start_stop_button.resize(self.start_stop_button.sizeHint())
		self.start_stop_button.clicked.connect(self.start_stop)
		self.pause_checkbox = QCheckBox("Pause")
		self.pause_checkbox.resize(self.pause_checkbox.sizeHint())
		self.pause_checkbox.clicked.connect(self.pause)
		self.stop_checkbox = QCheckBox("Stop")
		self.stop_checkbox.resize(self.stop_checkbox.sizeHint())
		self.stop_checkbox.clicked.connect(self.stop)
		self.overlay_checkbox = QCheckBox("Overlay icon")
		self.overlay_checkbox.resize(self.overlay_checkbox.sizeHint())
		self.overlay_checkbox.clicked.connect(self.toggle_overlay_icon)
		self.reset_button = QPushButton("Reset")
		self.reset_button.resize(self.reset_button.sizeHint())
		self.reset_button.clicked.connect(self.reset)
		self.hbox = QHBoxLayout()
		self.hbox.addWidget(self.start_stop_button)
		self.hbox.addWidget(self.pause_checkbox)
		self.hbox.addWidget(self.stop_checkbox)
		self.hbox.addWidget(self.overlay_checkbox)
		self.hbox.addWidget(self.reset_button)
		self.timer = QBasicTimer()
		self.step = 0
		self.setLayout(self.hbox)
		self.show()
		self.taskbar_init()

	def taskbar_init(self):
		self.taskbar_button = QWinTaskbarButton(self)
		self.taskbar_button.setWindow(self.windowHandle())
		self.taskbar_progress = self.taskbar_button.progress()
		self.taskbar_progress.setMinimum(0)
		self.taskbar_progress.setMaximum(100)
		self.taskbar_progress.setValue(0)
		self.taskbar_progress.setVisible(True)
		self.taskbar_progress.show()

	def timerEvent(self, timer_event):
		if self.step <= 100:
			self.taskbar_progress.setValue(self.step)
			self.step += 1
		else:
			self.timer.stop()
		return super().timerEvent(timer_event)

	def start_stop(self):
		if self.timer.isActive():
			self.timer.stop()
			self.start_stop_button.setText("Start")
			self.start_stop_button.resize(self.start_stop_button.sizeHint())
		elif not self.timer.isActive():
			self.timer.start(100, self)
			self.start_stop_button.setText("Stop")
			self.start_stop_button.resize(self.start_stop_button.sizeHint())

	def pause(self):
		if not self.taskbar_progress.isPaused():
			self.taskbar_progress.pause()
		elif self.taskbar_progress.isPaused():
			self.taskbar_progress.resume()

	def stop(self):
		if not self.taskbar_progress.isStopped():
			self.taskbar_progress.stop()
		elif self.taskbar_progress.isStopped():
			self.taskbar_progress.resume()

	def toggle_overlay_icon(self):
		if self.overlay_checkbox.isChecked():
			self.taskbar_button.setOverlayIcon(QIcon("badge-1.ico"))
		elif not self.overlay_checkbox.isChecked():
			self.taskbar_button.clearOverlayIcon()

	def reset(self):
		self.step = 0
		self.taskbar_progress.reset()


app = QApplication(sys.argv)
form = Form()
sys.exit(app.exec_())
