import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget


class Form(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.setGeometry(450, 250, 200, 150)
		self.setWindowTitle("Escape!")
		self.show()

	def keyPressEvent(self, event):
		if event.key() == Qt.Key_Escape:
			self.close()


app = QApplication(sys.argv)
form = Form()
sys.exit(app.exec_())
