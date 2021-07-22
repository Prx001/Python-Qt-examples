import sys
from PyQt5.QtCore import QDir
from PyQt5.QtWidgets import QApplication, QMainWindow, QTreeView, QFileSystemModel
class Form(QMainWindow):
	def __init__(self):
		super().__init__()
		self.initUI()
	def initUI(self):
		self.resize(800, 600)
		self.setWindowTitle("Shit")
		self.tree_view = QTreeView()
		self.model = QFileSystemModel()
		print(QDir.rootPath())
		print(QDir.currentPath())
		self.model.setRootPath(QDir.rootPath())
		self.tree_view.setModel(self.model)
		# self.tree_view.setRootIndex(self.model.index(QDir.currentPath()))
		self.setCentralWidget(self.tree_view)
		self.show()
app = QApplication(sys.argv)
form = Form()
sys.exit(app.exec_())