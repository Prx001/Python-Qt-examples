import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QTreeWidget, QTreeWidgetItem, QMenu
class Form(QMainWindow):
	def __init__(self):
		super().__init__()
		self.initUI()
	def initUI(self):
		self.tw = QTreeWidget()
		self.tw.setHeaderLabels(["Shits", "Poops"])
		item0 = QTreeWidgetItem(self.tw, ["Shit one", "Poop one"])
		item1 = QTreeWidgetItem(self.tw, ["Shit two", "Poop two"])
		item00 = QTreeWidgetItem(item0, ["Nested shit one", "Nested poop one"])
		item10 = QTreeWidgetItem(item1, ["Nested shit two", "Nested poop two"])
		self.context_menu = QMenu(self)
		self.action = self.context_menu.addAction("")
		self.tw.setContextMenuPolicy(Qt.CustomContextMenu)
		self.tw.customContextMenuRequested.connect(self.show_context_menu)
		self.setCentralWidget(self.tw)
		self.show()
	def show_context_menu(self, pos):
		self.action.setText(self.tw.indexAt(pos).data())
		self.context_menu.exec_(self.mapToGlobal(pos))

app = QApplication(sys.argv)
form = Form()
sys.exit(app.exec_())