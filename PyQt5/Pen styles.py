import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QPen, QColor
class Form(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()
	def initUI(self):
		self.setGeometry(300, 300, 300, 300)
		self.setWindowTitle("Pen styles")
		self.show()
	def paintEvent(self, event):
		painter = QPainter()
		painter.begin(self)
		self.drawLines(painter)
	def drawLines(self, painter):
		pen = QPen(QColor(0, 0, 0), 3, Qt.SolidLine)
		painter.setPen(pen)
		painter.drawLine(20, 40, 250, 40)
		pen.setStyle(Qt.DotLine)
		painter.setPen(pen)
		painter.drawLine(20, 80, 250, 80)
		pen.setStyle(Qt.DashLine)
		painter.setPen(pen)
		painter.drawLine(20, 120, 250, 120)
		pen.setStyle(Qt.DashDotLine)
		painter.setPen(pen)
		painter.drawLine(20, 160, 250, 160)
		pen.setStyle(Qt.DashDotDotLine)
		painter.setPen(pen)
		painter.drawLine(20, 200, 250, 200)
		pen.setStyle(Qt.CustomDashLine)
		pen.setDashPattern([1, 4, 7, 4])
		painter.setPen(pen)
		painter.drawLine(20, 240, 250, 240)
app = QApplication(sys.argv)
form = Form()
sys.exit(app.exec_())