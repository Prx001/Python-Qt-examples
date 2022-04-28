import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QBrush


class Form(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.resize(300, 200)
		self.setWindowTitle("Rounded rectangle")
		self.show()

	def paintEvent(self, event):
		painter = QPainter()
		painter.begin(self)
		painter.setPen(Qt.NoPen)
		painter.setBrush(QBrush(Qt.darkMagenta, Qt.SolidPattern))
		painter.drawRoundedRect(20, 20, 60, 20, 10, 10)
		painter.end()


app = QApplication(sys.argv)
form = Form()
sys.exit(app.exec_())
