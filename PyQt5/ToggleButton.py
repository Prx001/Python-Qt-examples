import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFrame
from PyQt5.QtGui import QColor
class Form(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()
	def initUI(self):
		self.setGeometry(450, 250, 280, 170)
		self.setWindowTitle("ToggleButtons")
		self.color = QColor(0, 0, 0)
		redToggle = QPushButton("Red", self)
		redToggle.setCheckable(True)
		redToggle.setChecked(False)
		redToggle.move(10, 10)
		redToggle.clicked[bool].connect(self.modifyColor)
		greenToggle = QPushButton("Green", self)
		greenToggle.setCheckable(True)
		greenToggle.setChecked(False)
		greenToggle.move(10, 60)
		greenToggle.clicked[bool].connect(self.modifyColor)
		blueToggle = QPushButton("Blue", self)
		blueToggle.setCheckable(True)
		blueToggle.setChecked(False)
		blueToggle.move(10, 110)
		blueToggle.clicked[bool].connect(self.modifyColor)
		self.frame = QFrame(self)
		self.frame.setGeometry(150, 20, 100, 100)
		self.frame.setStyleSheet("background-color: %s" % self.color.name())
		self.show()
	def modifyColor(self, switch):
		if switch:
			colorValue = 255
		elif not switch:
			colorValue = 0
		object = self.sender()
		if object.text() == "Red":
			self.color.setRed(colorValue)
		elif object.text() == "Green":
			self.color.setGreen(colorValue)
		elif object.text() == "Blue":
			self.color.setBlue(colorValue)
		self.frame.setStyleSheet("background-color: %s" % self.color.name())
app = QApplication(sys.argv)
form = Form()
sys.exit(app.exec_())