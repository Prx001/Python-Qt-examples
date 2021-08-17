import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QDialogButtonBox, QLabel, QVBoxLayout, QPushButton
class CustomDialog(QDialog):
	def __init__(self, parent=None):
		super().__init__(parent=parent)
		self.setWindowTitle("HELLO!")
		QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
		self.buttonBox = QDialogButtonBox(QBtn)
		self.buttonBox.accepted.connect(self.accept) # returns 1
		self.buttonBox.rejected.connect(self.reject) # returns 0
		self.layout = QVBoxLayout()
		message = QLabel("Something happened, is that OK?")
		message.setWhatsThis("I don't know what is this neither :|")
		self.layout.addWidget(message)
		self.layout.addWidget(self.buttonBox)
		self.setLayout(self.layout)
class Form(QMainWindow):
	def __init__(self):
		super().__init__()
		self.initUI()
	def initUI(self):
		self.resize(400, 300)
		self.setWindowTitle("Custom Dialog")
		button = QPushButton("Open dialog", self)
		button.resize(button.sizeHint())
		button.move(20, 20)
		self.dialog = CustomDialog(self)
		button.clicked.connect(self.open_dialog)
		self.show()
	def open_dialog(self):
		print(self.dialog.exec_())
app = QApplication(sys.argv)
form = Form()
sys.exit(app.exec_())