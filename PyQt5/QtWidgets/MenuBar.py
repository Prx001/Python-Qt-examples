import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QAction, QDesktopWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QPoint
class Form(QMainWindow):
	def __init__(self):
		super().__init__()
		self.initUI()
	def initUI(self):
		self.setWindowTitle("MenuBar")
		self.resize(300, 300)
		self.moveCenter()
		self.setWindowFlag(Qt.FramelessWindowHint)
		QButton = QPushButton("Quit", self)
		QButton.resize(QButton.sizeHint())
		QButton.move(10, 250)
		QButton.setToolTip("This is a <b>QPushButton</b> widget. Press to exit the form. You can also use the menu bar action to do so.")
		QButton.setStatusTip("Exit the application")
		QButton.clicked.connect(self.close)
		QMenuBar = self.menuBar()
		optionsMenu = QMenuBar.addMenu("Options")
		exitAction = QAction(QIcon("icon.ico"), "Exit", self)
		exitAction.setShortcut("Ctrl+Q")
		exitAction.setStatusTip("Exit the application")
		exitAction.triggered.connect(self.close)
		optionsMenu.addAction(exitAction)
		self.statusBar().showMessage("Ready")
		self.show()
	def moveCenter(self):
		qr = self.frameGeometry()
		cp = QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())
	def mousePressEvent(self, event):
		self.oldPos = event.globalPos()
	def mouseMoveEvent(self, event):
		delta = QPoint(event.globalPos() - self.oldPos)
		self.move(self.x() + delta.x(), self.y() + delta.y())
		self.oldPos = event.globalPos()
app = QApplication(sys.argv)
form = Form()
sys.exit(app.exec_())