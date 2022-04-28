import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton


class DragDropButton(QPushButton):
	def __init__(self, text, parent):
		super().__init__(text, parent)
		self.setAcceptDrops(True)

	def dragEnterEvent(self, event):
		if event.mimeData().hasFormat("text/plain"):
			event.accept()
		else:
			event.ignore()

	def dropEvent(self, event):
		# self.setText("You just took order from a QPushButton! ;)")
		self.setText(event.mimeData().text())
		self.resize(self.sizeHint())


class Form(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.resize(350, 100)
		self.setWindowTitle("Drag and Drop")
		dd_button = DragDropButton("Drop text on me!", self)
		dd_button.move(20, 60)
		dd_button.resize(dd_button.sizeHint())
		self.show()


app = QApplication(sys.argv)
form = Form()
sys.exit(app.exec_())
# https://www.tutorialspoint.com/pyqt/pyqt_drag_and_drop.htm
