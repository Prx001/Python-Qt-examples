import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QAction
from PyQt5.QtGui import QIcon


class Form(QMainWindow):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.setWindowTitle("Toolbar")
		self.setGeometry(400, 250, 300, 300)
		exitAct = QAction(QIcon("icon.ico"), "Exit", self)
		exitAct.triggered.connect(self.close)
		QToolBar = self.addToolBar("View toolbar")
		QToolBar.addAction(exitAct)
		self.show()


app = QApplication(sys.argv)
form = Form()
sys.exit(app.exec_())
