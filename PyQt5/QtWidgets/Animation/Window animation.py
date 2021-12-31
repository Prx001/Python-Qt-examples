import sys

from PyQt5.QtCore import QSize, QPropertyAnimation
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QDesktopWidget
from PyQt5.QtGui import QIcon


class Form(QMainWindow):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.resize(400, 320)
		self.move_to_center()
		self.setWindowTitle("Window animation")
		animateAct = QAction(QIcon("animation.jpg"), "Animate", self)
		animateAct.triggered.connect(self.animate)
		toolbar = self.addToolBar("View toolbar")
		toolbar.addAction(animateAct)
		self.wide = False
		self.show()

	def animate(self):
		print(self.size())
		print("Animating it....")
		self.anim = QPropertyAnimation(self, b"size")
		self.anim.setDuration(1000)
		self.anim.setStartValue(self.size())
		if self.wide:
			self.anim.setEndValue(QSize(400, 320))
			self.wide = False
		elif not self.wide:
			self.anim.setEndValue(QSize(640, 560))
			self.wide = True
		self.anim.start()

	def move_to_center(self):
		qr = self.frameGeometry()
		cp = QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())


app = QApplication(sys.argv)
form = Form()
sys.exit(app.exec_())
