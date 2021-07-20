import sys
import random
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter
class Form(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()
	def initUI(self):
		self.setGeometry(500, 300, 300, 200)
		self.setWindowTitle("Random points")
		self.show()
	def paintEvent(self, event):
		qp = QPainter()
		qp.begin(self)
		qp.setPen(Qt.red)
		size = self.size()
		for i in range(1000):
			x = random.randint(1, size.width() - 1)
			y = random.randint(1, size.height() - 1)
			qp.drawPoint(x, y)
		qp.end()
app = QApplication(sys.argv)
form = Form()
sys.exit(app.exec_())