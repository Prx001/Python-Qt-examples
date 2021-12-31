import sys

from PyQt5.QtCore import QBasicTimer
from PyQt5.QtWidgets import QApplication, QWidget, QProgressBar, QPushButton


class Form(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.setGeometry(450, 250, 280, 170)
		self.setWindowTitle("QProgressBar")
		self.pbar = QProgressBar(self)
		self.pbar.setGeometry(30, 40, 200, 25)
		self.button = QPushButton("Start", self)
		self.button.resize(self.button.sizeHint())
		self.button.move(40, 80)
		self.button.clicked.connect(self.doIt)
		self.timer = QBasicTimer()
		self.step = 0
		self.show()

	def timerEvent(self, time_event):
		if self.step >= 100:
			self.timer.stop()
			self.button.setText("Finished")
		self.step += 1
		self.pbar.setValue(self.step)
		return super().timerEvent(time_event)

	def doIt(self):
		if self.button.text() == "Finished":
			self.close()
		if self.timer.isActive():
			self.timer.stop()
			self.button.setText("Start")
		elif not self.timer.isActive():
			self.timer.start(100, self)
			self.button.setText("Stop")


app = QApplication(sys.argv)
form = Form()
sys.exit(app.exec_())
