import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTreeView, QDirModel
class Form(QMainWindow):
	def __init__(self):
		super().__init__()
		self.initUI()
	def initUI(self):
		self.resize(450, 200)
		self.setWindowTitle("Shit")
		self.tree_view = QTreeView()
		self.model = QDirModel()
		self.tree_view.setModel(self.model)
		self.setCentralWidget(self.tree_view)
		self.show()
app = QApplication(sys.argv)
form = Form()
sys.exit(app.exec_())