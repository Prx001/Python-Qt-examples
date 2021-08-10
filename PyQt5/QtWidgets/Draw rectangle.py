import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor
class Form(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()
	def initUI(self):
		self.setGeometry(500, 300, 350, 100)
		self.setWindowTitle("Draw colorful rectangles")
		self.show()
	def paintEvent(self, event):
		painter = QPainter()
		painter.begin(self)
		painter.setPen(QColor(0, 0, 0))
		painter.setBrush(QColor(255, 0, 0))
		painter.drawRect(10, 15, 90, 60)
		painter.setBrush(QColor(255, 80, 0, 160))
		painter.drawRect(130, 15, 90, 60)
		painter.setBrush(QColor(25, 0, 90, 200))
		painter.drawRect(250, 15, 90, 60)
		painter.end()
app = QApplication(sys.argv)
form = Form()
sys.exit(app.exec_())