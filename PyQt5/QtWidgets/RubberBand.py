import sys

from PyQt5.QtCore import QRect, QSize
from PyQt5.QtWidgets import QApplication, QWidget, QRubberBand


class Form(QWidget):
	def __init__(self):
		super().__init__()
		self.show()

	def mousePressEvent(self, event):
		self.origin = event.pos()
		self.rubberBand = QRubberBand(QRubberBand.Rectangle, self)
		self.rubberBand.setGeometry(QRect(self.origin, QSize()))
		self.rubberBand.show()

	def mouseMoveEvent(self, event):
		self.rubberBand.setGeometry(QRect(self.origin, event.pos()).normalized())

	def mouseReleaseEvent(self, event):
		self.rubberBand.close()


app = QApplication(sys.argv)
form = Form()
sys.exit(app.exec_())
