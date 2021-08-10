import sys
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow
class MouseListener(QObject):
	mouseClickEvent = pyqtSignal()
class Form(QMainWindow):
	def __init__(self):
		super().__init__()
		self.initUI()
	def initUI(self):
		self.setGeometry(450, 250, 300, 200)
		self.setWindowTitle("Custom Signal")
		self.listener = MouseListener()
		self.listener.mouseClickEvent.connect(self.close)
		self.show()
	def mousePressEvent(self, event):
		self.listener.mouseClickEvent.emit()
app = QApplication(sys.argv)
form = Form()
sys.exit(app.exec_())