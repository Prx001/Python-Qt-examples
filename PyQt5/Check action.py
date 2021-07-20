import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction
class Form(QMainWindow):
	def __init__(self):
		super().__init__()
		self.initUI()
	def initUI(self):
		self.setWindowTitle("Checkable action")
		self.setGeometry(400, 200, 300, 300)
		self.QStatusBar = self.statusBar() # The self before the variable name is important. It defines a attribute for the main form named "QStatusBar" which can be accessed from "toggleStatusBar" method in the future.
		self.QStatusBar.showMessage("Ready")
		QMenuBar = self.menuBar()
		viewMenu = QMenuBar.addMenu("View")
		viewStatAct = QAction("View statusbar", self, checkable=True)
		viewStatAct.setChecked(True) # Set the default mode
		viewStatAct.triggered.connect(self.toggleStatusBar)
		viewStatAct.setStatusTip("Toggle statusbar")
		viewStatAct.setShortcut("Alt+S")
		viewMenu.addAction(viewStatAct)
		self.show()
	def toggleStatusBar(self, switch):
		if switch == True:
			self.QStatusBar.show()
		else:
			self.QStatusBar.hide()
app = QApplication(sys.argv)
form = Form()
sys.exit(app.exec_())