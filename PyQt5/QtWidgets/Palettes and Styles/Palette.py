import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtGui import QPalette, QColor


class Color(QWidget):
	def __init__(self, color):
		super().__init__()
		self.color = color
		self.initUI()

	def initUI(self):
		self.setAutoFillBackground(True)
		palette = self.palette()
		palette.setColor(QPalette.Window, QColor(self.color))
		self.setPalette(palette)


class Form(QMainWindow):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.resize(400, 300)
		color = Color("green")
		self.setCentralWidget(color)
		self.show()


app = QApplication(sys.argv)
form = Form()
sys.exit(app.exec_())
