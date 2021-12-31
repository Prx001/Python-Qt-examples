import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor, QFont


class Form(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.setGeometry(500, 300, 300, 300)
		self.setWindowTitle("QPainter")
		self.text = "WTF IS THIS PAINTING IN Qt"
		self.show()

	def paintEvent(self, event):
		qp = QPainter()
		qp.begin(self)
		qp.setPen(QColor(255, 0, 0))
		qp.setFont(QFont("Decorative", 10))
		qp.drawText(event.rect(), Qt.AlignCenter, self.text)
		qp.end()


app = QApplication(sys.argv)
form = Form()
sys.exit(app.exec_())
