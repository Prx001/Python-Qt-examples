import sys

from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget


class Form(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.resize(300, 300)
		self.center()
		self.setWindowTitle("Form")
		self.show()

	def center(self):
		qr = self.frameGeometry()
		cp = QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())


app = QApplication(sys.argv)
form = Form()
sys.exit(app.exec_())
