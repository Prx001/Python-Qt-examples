import sys

from PyQt5.QtCore import QPoint, QPropertyAnimation, QSequentialAnimationGroup
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton


class Form(QWidget):
	def __init__(self):
		super().__init__()
		self.init_ui()

	def init_ui(self):
		self.resize(340, 300)
		self.setWindowTitle("QSequentialAnimationGroup")
		self.button1 = QPushButton("Button 1", self)
		self.button1.move(20, 20)
		self.button1.resize(self.button1.sizeHint())
		self.button2 = QPushButton("Button 2", self)
		self.button2.move(120, 20)
		self.button2.resize(self.button2.sizeHint())
		self.button3 = QPushButton("Button 3", self)
		self.button3.move(220, 20)
		self.button3.resize(self.button3.sizeHint())
		self.animations()
		self.show()

	def animations(self):
		self.anim1 = QPropertyAnimation(self.button1, b"pos")
		self.anim1.setDuration(500)
		self.anim1.setEndValue(QPoint(20, 250))
		self.anim2 = QPropertyAnimation(self.button2, b"pos")
		self.anim2.setDuration(500)
		self.anim2.setEndValue(QPoint(120, 250))
		self.anim3 = QPropertyAnimation(self.button3, b"pos")
		self.anim3.setDuration(500)
		self.anim3.setEndValue(QPoint(220, 250))

		self.anim_group = QSequentialAnimationGroup()
		self.anim_group.addAnimation(self.anim1)
		self.anim_group.addAnimation(self.anim2)
		self.anim_group.addAnimation(self.anim3)

		self.button1.clicked.connect(self.anim_group.start)
		self.button2.clicked.connect(self.anim_group.start)
		self.button3.clicked.connect(self.anim_group.start)


app = QApplication(sys.argv)
form = Form()
sys.exit(app.exec_())
