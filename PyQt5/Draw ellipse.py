import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QPen, QBrush
class Form(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()
	def initUI(self):
		self.setGeometry(500, 300, 200, 280)
		self.setWindowTitle("Ellipse")
		self.show()
	def paintEvent(self, event):
		painter = QPainter()
		painter.begin(self)
		painter.setPen(QPen(Qt.black, 2, Qt.SolidLine))
		painter.setBrush(QBrush(Qt.white, Qt.SolidPattern))
		painter.drawEllipse(50, 50, 100, 200)
		painter.end()
app = QApplication(sys.argv)
form = Form()
sys.exit(app.exec_())