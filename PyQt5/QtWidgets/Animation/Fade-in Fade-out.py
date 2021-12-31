import sys

from PyQt5.QtCore import QPropertyAnimation
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget


class Form(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.resize(400, 320)
		self.move_to_center()
		self.setWindowTitle("Fade-in Fade-out")
		self.setWindowOpacity(0.1)
		self.animation = QPropertyAnimation(self, b"windowOpacity")
		self.animation.setDuration(1000)
		self.animation.setStartValue(0.1)
		self.animation.setEndValue(1)
		self.show()
		self.animation.start()

	def move_to_center(self):
		qr = self.frameGeometry()
		cp = QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())

	def closeEvent(self, event):
		event.ignore()
		self.animation.setStartValue(1)
		self.animation.setEndValue(0.01)
		self.animation.start()


app = QApplication(sys.argv)
form = Form()
sys.exit(app.exec_())
