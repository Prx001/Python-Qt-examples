import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QTabWidget
from PyQt5.QtGui import QIcon


class Form(QMainWindow):
	def __init__(self):
		super().__init__()
		self.init_ui()
	
	def init_ui(self):
		self.resize(600, 500)
		tab = QTabWidget(self)
		self.setCentralWidget(tab)
		tab1 = QWidget()
		tab2 = QWidget()
		tab.addTab(tab1, QIcon("icon.ico"), "PyQt")
		tab.addTab(tab2, QIcon("icon.ico"), "PySide")
		tab.setMovable(True)
		self.show()


app = QApplication(sys.argv)
form = Form()
sys.exit(app.exec_())
