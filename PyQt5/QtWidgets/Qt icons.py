import sys

from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QStyle


class Form(QMainWindow):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.resize(1000, 800)
		self.setWindowTitle("Qt icons")
		button = QPushButton("Button")
		style = button.style()
		icon = style.standardIcon(QStyle.SP_ComputerIcon)
		button.setIcon(icon)
		button.setIconSize(QSize(64, 64))
		self.setCentralWidget(button)
		self.show()


app = QApplication(sys.argv)
form = Form()
sys.exit(app.exec_())
