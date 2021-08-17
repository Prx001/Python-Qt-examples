import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QComboBox
class Form(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()
	def initUI(self):
		self.setGeometry(450, 250, 300, 200)
		self.setWindowTitle("QComboBox")
		self.label = QLabel("Item 1", self)
		self.label.move(50, 150)
		combo = QComboBox(self)
		combo.addItems(["Item 1", "Item 2", "Item 3", "Item 4"])
		combo.move(50, 50)
		combo.setEditable(True)
		combo.activated[str].connect(self.onActivate)
		self.show()
	def onActivate(self, item):
		self.label.setText(item)
		self.label.adjustSize()
app = QApplication(sys.argv)
form = Form()
sys.exit(app.exec_())