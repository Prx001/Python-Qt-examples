import sys
from PyQt5.QtCore import QSize, QPropertyAnimation
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
class Form(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()
	def initUI(self):
		self.setGeometry(500, 300, 300, 240)
		self.setWindowTitle("Animation")
		self.button = QPushButton("Animate it!", self)
		self.button.resize(self.button.sizeHint())
		self.button.move(20, 200)
		self.button.clicked.connect(self.animate)
		self.show()
	def animate(self):
		print(self.button.size())
		print("Animating it....")
		self.animation = QPropertyAnimation(self.button, b"size")
		self.animation.setDuration(1000)
		self.animation.setStartValue(QSize(75, 23))
		self.animation.setEndValue(QSize(120, 23))
		self.animation.start()
app = QApplication(sys.argv)
form = Form()
sys.exit(app.exec_())