import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLCDNumber, QSlider
class Form(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()
	def initUI(self):
		self.setGeometry(450, 250, 200, 200)
		self.setWindowTitle("LCD slider")
		lcd = QLCDNumber()
		slider = QSlider(Qt.Horizontal)
		slider.valueChanged.connect(lcd.display)
		vbox = QVBoxLayout()
		vbox.addWidget(lcd)
		vbox.addWidget(slider)
		self.setLayout(vbox)
		self.show()
app = QApplication(sys.argv)
form = Form()
sys.exit(app.exec_())
