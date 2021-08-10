import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QAction
class Form(QMainWindow):
	def __init__(self):
		super().__init__()
		self.initUI()
	def initUI(self):
		self.setWindowTitle("Submenu")
		self.setGeometry(450, 200, 300, 300)
		QMenuBar = self.menuBar()
		optionsMenu = QMenuBar.addMenu("Options")
		tasksSubMenu = QMenu("Tasks", self)
		exitAct = QAction("Exit", self)
		tasksSubMenu.addAction(exitAct)
		optionsMenu.addMenu(tasksSubMenu)
		self.show()
app = QApplication(sys.argv)
form = Form()
sys.exit(app.exec_())