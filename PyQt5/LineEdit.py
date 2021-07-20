import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit
class Form(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()
	def initUI(self):
		self.setGeometry(450, 250, 280, 170)
		self.setWindowTitle("QLineEdit")
		self.label = QLabel(self)
		lineEdit = QLineEdit(self)
		self.label.move(60, 40)
		lineEdit.move(60, 100)
		lineEdit.textChanged.connect(self.onChange)
		self.show()
	def onChange(self, newText):
		self.label.setText(newText)
		self.label.adjustSize()
app = QApplication(sys.argv)
form = Form()
sys.exit(app.exec_())