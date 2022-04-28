import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QSplitter, QGridLayout


class Form(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.resize(800, 600)
		left_text_edit = QTextEdit()
		right_text_edit = QTextEdit()
		splitter = QSplitter()
		splitter.setOrientation(Qt.Horizontal)
		splitter.addWidget(left_text_edit)
		splitter.addWidget(right_text_edit)
		splitter.setSizes([splitter.size().width() * 2, splitter.size().width() * 8])
		grid = QGridLayout()
		grid.addWidget(splitter, 0, 0)
		self.setLayout(grid)
		self.show()


app = QApplication(sys.argv)
form = Form()
sys.exit(app.exec_())
