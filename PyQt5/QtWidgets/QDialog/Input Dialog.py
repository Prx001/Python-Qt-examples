import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QInputDialog


class Form(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.setGeometry(450, 250, 290, 150)
		self.setWindowTitle("Input Dialog")
		button1 = QPushButton("Dialog", self)
		button1.move(20, 20)
		button1.clicked.connect(self.showDialog)
		self.lineEdit = QLineEdit(self)
		self.lineEdit.move(130, 22)
		self.show()

	def showDialog(self):
		text, ok = QInputDialog.getText(self, "Input Dialog", "Enter your name")
		if ok:
			self.lineEdit.setText(str(text))


app = QApplication(sys.argv)
form = Form()
sys.exit(app.exec_())
