import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap, QPainter, QPen
class Form(QMainWindow):
	def __init__(self):
		super().__init__()
		self.initUI()
	def initUI(self):
		self.resize(400, 400)
		self.setWindowTitle("Image viewer")
		self.image = QLabel("Drop image here")
		self.image.setAlignment(Qt.AlignCenter)
		self.setCentralWidget(self.image)
		self.image.setAcceptDrops(True)
		self.setAcceptDrops(True)
		self.show()
	def paintEvent(self, pain_event):
		painter = QPainter()
		painter.begin(self)
		painter.setPen(QPen(Qt.gray, 4, Qt.DashLine))
		painter.drawRect(10, 10, self.width() - 20, self.height() - 20)
		painter.end()
		super().paintEvent(pain_event)
	def dragEnterEvent(self, event):
		if event.mimeData().hasImage:
			event.accept()
		else:
			event.ignore()
	def dropEvent(self, event):
		print(event.mimeData().urls())
		self.image.setPixmap(QPixmap(event.mimeData().urls()[0].toLocalFile()))
app = QApplication(sys.argv)
form = Form()
sys.exit(app.exec_())