import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QCheckBox


class Form(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.setWindowTitle("QCheckBox")
		self.setGeometry(450, 250, 300, 250)
		cb = QCheckBox("Show window title", self)
		cb.move(20, 20)
		cb.toggle()
		cb.stateChanged.connect(self.toggleWindowTitle)
		self.show()

	def toggleWindowTitle(self, switch):
		if switch == Qt.Checked:
			self.setWindowTitle("QCheckBox")
		elif switch == Qt.Unchecked:
			self.setWindowTitle(" ")


app = QApplication(sys.argv)
form = Form()
sys.exit(app.exec_())
