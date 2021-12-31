import sys

from PyQt5.QtWidgets import QApplication, QMainWindow


class Form(QMainWindow):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.statusBar().showMessage("Ready")
		self.setGeometry(500, 200, 300, 300)
		self.setWindowTitle("Statusbar")
		self.show()


app = QApplication(sys.argv)
form = Form()
sys.exit(app.exec_())
