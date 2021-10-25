import sys
from PyQt5.QtCore import QRect, QSize
from PyQt5.QtWidgets import QApplication, QWidget, QRubberBand
from PyQt5.QtGui import QPalette, QColor
class Form(QWidget):
	def __init__(self):
		super().__init__()
		self.show()
	def mousePressEvent(self, event):
		self.origin = event.pos()
		palette = QPalette()
		palette.setColor(QPalette.Highlight, QColor(170, 0, 255))
		self.rubberBand = QRubberBand(QRubberBand.Rectangle, self)
		self.rubberBand.setPalette(palette)
		self.rubberBand.setGeometry(QRect(self.origin, QSize()))
		self.rubberBand.show()

	def mouseMoveEvent(self, event):
		self.rubberBand.setGeometry(QRect(self.origin, event.pos()).normalized())

	def mouseReleaseEvent(self, event):
		self.rubberBand.hide()
app = QApplication(sys.argv)
form = Form()
sys.exit(app.exec_())