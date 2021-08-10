import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu
from PyQt5.QtGui import QIcon
class Form(QMainWindow):
	def __init__(self):
		super().__init__()
		self.initUI()
	def initUI(self):
		self.setWindowTitle("Context menu")
		self.setGeometry(400, 200, 300, 300)
		self.show()
		self.contextMenu = QMenu(self)
		newAct = self.contextMenu.addAction(QIcon("icon.ico"), "New")
		openAct = self.contextMenu.addAction(QIcon("icon.ico"), "Open File")
		openFolderAct = self.contextMenu.addAction(QIcon("icon.ico"), "Open Folder")
		openRecentAct = self.contextMenu.addAction(QIcon("icon.ico"), "Open Recent")
		saveAct = self.contextMenu.addAction(QIcon("icon.ico"), "Save")
		saveAsAct = self.contextMenu.addAction(QIcon("icon.ico"), "Save As")
		saveAllAct = self.contextMenu.addAction(QIcon("icon.ico"), "Save All")
		self.quitAct = self.contextMenu.addAction(QIcon("icon.ico"), "Quit")
	def contextMenuEvent(self, event):
		action = self.contextMenu.exec_(self.mapToGlobal(event.pos()))
		if action == self.quitAct:
			raise SystemExit
app = QApplication(sys.argv)
form = Form()
sys.exit(app.exec_())


# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu
# from PyQt5.QtGui import QIcon
# class Form(QMainWindow):
# 	def __init__(self):
# 		super().__init__()
# 		self.initUI()
# 	def initUI(self):
# 		self.setWindowTitle("Context menu")
# 		self.setGeometry(400, 200, 300, 300)
# 		self.show()
# 	def contextMenuEvent(self, event):
# 		contextMenu = QMenu(self)
# 		newAct = contextMenu.addAction(QIcon("icon.ico"), "New")
# 		openAct = contextMenu.addAction(QIcon("icon.ico"), "Open File")
# 		openFolderAct = contextMenu.addAction(QIcon("icon.ico"), "Open Folder")
# 		openRecentAct = contextMenu.addAction(QIcon("icon.ico"), "Open Recent")
# 		saveAct = contextMenu.addAction(QIcon("icon.ico"), "Save")
# 		saveAsAct = contextMenu.addAction(QIcon("icon.ico"), "Save As")
# 		saveAllAct = contextMenu.addAction(QIcon("icon.ico"), "Save All")
# 		quitAct = contextMenu.addAction(QIcon("icon.ico"), "Quit")
# 		action = contextMenu.exec_(self.mapToGlobal(event.pos()))
# 		if action == quitAct:
# 			raise SystemExit
# app = QApplication(sys.argv)
# form = Form()
# sys.exit(app.exec_())