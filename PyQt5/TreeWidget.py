import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTreeWidget, QTreeWidgetItem
class Form(QMainWindow):
	def __init__(self):
		super().__init__()
		self.initUI()
	def initUI(self):
		tw = QTreeWidget()
		tw.setHeaderLabels(["Shits", "Poops"])
		item0 = QTreeWidgetItem(tw, ["Shit one", "Poop one"])
		item1 = QTreeWidgetItem(tw, ["Shit two", "Poop two"])
		item00 = QTreeWidgetItem(item0, ["Nested shit one", "Nested poop one"])
		item10 = QTreeWidgetItem(item1, ["Nested shit two", "Nested poop two"])
		self.setCentralWidget(tw)
		self.show()
app = QApplication(sys.argv)
form = Form()
sys.exit(app.exec_())