import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout
class Form(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()
	def initUI(self):
		self.setGeometry(400, 200, 250, 100)
		self.setWindowTitle("Nested QLayouts")
		previousButton = QPushButton("Previous", self)
		nextButton = QPushButton("Next", self)
		hbox = QHBoxLayout()
		hbox.addStretch(1)
		hbox.addWidget(previousButton)
		hbox.addWidget(nextButton)
		vbox = QVBoxLayout()
		vbox.addStretch(1)
		vbox.addLayout(hbox)
		self.setLayout(vbox)
		self.show()
app = QApplication(sys.argv)
form = Form()
sys.exit(app.exec_())