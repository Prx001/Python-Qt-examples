import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QGridLayout
class Form(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()
	def initUI(self):
		self.setGeometry(450, 250, 400, 400)
		self.setWindowTitle("Curser tracker")
		x = 0
		y = 0
		self.position_text = f"x = {x}; y = {y}"
		self.label = QLabel(self.position_text)
		grid = QGridLayout()
		grid.addWidget(self.label, 0, 0, Qt.AlignTop)
		self.setLayout(grid)
		self.show()
	def mouseMoveEvent(self, event):
		x = event.x()
		y = event.y()
		self.position_text = f"x = {x}; y = {y}"
		self.label.setText(self.position_text)
app = QApplication(sys.argv)
form = Form()
sys.exit(app.exec_())