import sys

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon


class Form(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.setWindowTitle("Title Icon")
		self.setWindowIcon(QIcon("icon.ico"))
		self.show()


app = QApplication(sys.argv)
form = Form()
sys.exit(app.exec_())
