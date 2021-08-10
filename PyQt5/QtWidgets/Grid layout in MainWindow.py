import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QGridLayout, QAction
class Widget(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()
	def initUI(self):
		grid = QGridLayout()
		button0 = QPushButton("0")
		button1 = QPushButton("1")
		button2 = QPushButton("2")
		button3 = QPushButton("3")
		button4 = QPushButton("4")
		grid.addWidget(button0, 3, 0, 1, 1)
		grid.addWidget(button1, 4, 0, 1, 1)
		grid.addWidget(button2, 0, 2, 1, 1)
		grid.addWidget(button3, 0, 4, 1, 1)
		self.setLayout(grid)
class Form(QMainWindow):
	def __init__(self):
		super().__init__()
		self.initUI()
	def initUI(self):
		self.setGeometry(500, 300, 300, 250)
		widget = Widget()
		self.setCentralWidget(widget)
		menubar = self.menuBar()
		exitAct = QAction("Exit", self)
		exitAct.triggered.connect(self.close)
		options = menubar.addMenu("Options")
		options.addAction(exitAct)
		self.show()
app = QApplication(sys.argv)
form = Form()
sys.exit(app.exec_())