import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout
class Form(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()
	def initUI(self):
		self.move(450, 250)
		self.setWindowTitle("QGridLayout")
		grid = QGridLayout()
		names = ["7", "4", "1", "8", "5", "2", "9", "6", "3"]
		positions = [(y, x) for x in range(3) for y in range(3)]
		for name, position in zip(names, positions):
			button = QPushButton(name)
			grid.addWidget(button, *position)
		self.setLayout(grid)
		self.show()
app = QApplication(sys.argv)
form = Form()
sys.exit(app.exec_())