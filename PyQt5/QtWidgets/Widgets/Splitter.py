import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QFrame, QSplitter, QHBoxLayout


class Form(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.setGeometry(450, 250, 300, 200)
		self.setWindowTitle("QSplitter")
		topLeft = QFrame()
		topLeft.setFrameShape(QFrame.StyledPanel)
		topRight = QFrame()
		topRight.setFrameShape(QFrame.StyledPanel)
		bottom = QFrame()
		bottom.setFrameShape(QFrame.StyledPanel)
		splitter1 = QSplitter(Qt.Horizontal)
		splitter1.addWidget(topLeft)
		splitter1.addWidget(topRight)
		splitter2 = QSplitter(Qt.Vertical)
		splitter2.addWidget(splitter1)
		splitter2.addWidget(bottom)
		hbox = QHBoxLayout()
		hbox.addWidget(splitter2)
		self.setLayout(hbox)
		self.show()


app = QApplication(sys.argv)
form = Form()
sys.exit(app.exec_())
