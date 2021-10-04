import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QPalette
class Form(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()
	def initUI(self):
		self.resize(400, 300)
		self.setWindowTitle("Palette")
		self.setAutoFillBackground(True)
		palette = self.palette()
		palette.setColor(QPalette.Disabled, QPalette.ButtonText, Qt.red)
		self.setPalette(palette)
		self.button = QPushButton("PushButton", self)
		self.button.resize(self.button.sizeHint())
		self.button.move(20, 20)
		self.button.setDisabled(True)
		self.show()
app = QApplication(sys.argv)
form = Form()
sys.exit(app.exec_())