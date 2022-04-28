import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton


class Form(QMainWindow):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.setGeometry(450, 250, 250, 200)
		self.setWindowTitle("Event sender")
		button1 = QPushButton("Button 1", self)
		button1.resize(button1.sizeHint())
		button1.move(25, 20)
		button1.clicked.connect(self.buttonClicked)
		button2 = QPushButton("Button 2", self)
		button2.resize(button2.sizeHint())
		button2.move(151, 20)
		button2.clicked.connect(self.buttonClicked)
		self.statusBar().showMessage("Ready")
		self.show()

	def buttonClicked(self):
		sender = self.sender()
		self.statusBar().showMessage(sender.text() + " was pressed")


app = QApplication(sys.argv)
form = Form()
sys.exit(app.exec_())
