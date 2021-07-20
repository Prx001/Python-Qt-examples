import sys
from PyQt5.QtWidgets import QApplication, QWidget, QFrame, QPushButton, QColorDialog
from PyQt5.QtGui import QColor
class Form(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()
	def initUI(self):
		self.setGeometry(450, 250, 250, 180)
		self.setWindowTitle("Color Dialog")
		col = QColor(0, 0, 0)
		button1 = QPushButton("Change color", self)
		button1.move(20, 20)
		button1.resize(button1.sizeHint())
		button1.clicked.connect(self.showDialog)
		self.frame = QFrame(self)
		self.frame.setGeometry(130, 22, 100, 100)
		self.frame.setStyleSheet("background-color: %s" % col.name())
		self.show()
	def showDialog(self):
		col = QColorDialog.getColor()
		if col.isValid():
			self.frame.setStyleSheet("background-color: %s" % col.name())
app = QApplication(sys.argv)
form = Form()
sys.exit(app.exec_())
