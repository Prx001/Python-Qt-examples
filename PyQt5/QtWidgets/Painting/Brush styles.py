import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QBrush


class Form(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.setGeometry(500, 300, 355, 280)
		self.setWindowTitle("Brush styles")
		self.show()

	def paintEvent(self, event):
		painter = QPainter()
		painter.begin(self)
		brush = QBrush(Qt.SolidPattern)
		painter.setBrush(brush)
		painter.drawRect(10, 15, 90, 60)
		brush.setStyle(Qt.Dense1Pattern)
		painter.setBrush(brush)
		painter.drawRect(130, 15, 90, 60)
		brush.setStyle(Qt.Dense2Pattern)
		painter.setBrush(brush)
		painter.drawRect(250, 15, 90, 60)
		brush.setStyle(Qt.DiagCrossPattern)
		painter.setBrush(brush)
		painter.drawRect(10, 105, 90, 60)
		brush.setStyle(Qt.Dense5Pattern)
		painter.setBrush(brush)
		painter.drawRect(130, 105, 90, 60)
		brush.setStyle(Qt.Dense6Pattern)
		painter.setBrush(brush)
		painter.drawRect(250, 105, 90, 60)
		brush.setStyle(Qt.HorPattern)
		painter.setBrush(brush)
		painter.drawRect(10, 195, 90, 60)
		brush.setStyle(Qt.VerPattern)
		painter.setBrush(brush)
		painter.drawRect(130, 195, 90, 60)
		brush.setStyle(Qt.BDiagPattern)
		painter.setBrush(brush)
		painter.drawRect(250, 195, 90, 60)
		painter.end()


app = QApplication(sys.argv)
form = Form()
sys.exit(app.exec_())
