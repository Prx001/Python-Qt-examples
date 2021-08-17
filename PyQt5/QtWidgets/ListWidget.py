import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidget, QListWidgetItem
class Form(QMainWindow):
	def __init__(self):
		super().__init__()
		self.initUI()
	def initUI(self):
		self.resize(400, 300)
		self.setWindowTitle("QListWidget")
		list = QListWidget()
		list.addItem("Item 1")
		# Not necessary to use QListWidgetItem class, you can pass the string directly to the addWidget method
		# list.addItem(QListWidgetItem("Item 1"))
		list.addItem("Item 2")
		list.addItem("Item 3")
		# Or simply:
		# list.addItems(["Item 1", "Item 2", "Item 3"])
		self.setCentralWidget(list)
		self.show()
app = QApplication(sys.argv)
form = Form()
sys.exit(app.exec_())