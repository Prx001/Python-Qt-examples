import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit
class Form(QMainWindow):
	def __init__(self):
		super().__init__()
		self.initUI()
	def initUI(self):
		self.resize(450, 450)
		self.move(400, 250)
		self.setWindowTitle("TextEdit")
		textEdit = QTextEdit()
		self.setCentralWidget(textEdit)
		self.show()
app = QApplication(sys.argv)
form = Form()
sys.exit(app.exec_())