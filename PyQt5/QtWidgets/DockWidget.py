import sys

from PyQt5.QtCore import Qt, QDir
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QDockWidget, QTreeView, QFileSystemModel


class Form(QMainWindow):
	def __init__(self):
		super().__init__()
		self.dock_widget = QDockWidget("File Explorer", self)
		self.model = QFileSystemModel()
		self.tree_view = QTreeView(self)
		self.text_edit = QTextEdit(parent=self)
		self.init_ui()

	def init_ui(self):
		self.resize(800, 600)
		self.setWindowTitle("QDockWidget")
		self.model.setRootPath(QDir.rootPath())
		self.tree_view.setModel(self.model)
		self.dock_widget.setWidget(self.tree_view)
		self.dock_widget.setAllowedAreas(Qt.TopDockWidgetArea | Qt.BottomDockWidgetArea | Qt.LeftDockWidgetArea)
		self.setCentralWidget(self.text_edit)
		self.addDockWidget(Qt.LeftDockWidgetArea, self.dock_widget)
		self.show()


app = QApplication(sys.argv)
form = Form()
sys.exit(app.exec_())
