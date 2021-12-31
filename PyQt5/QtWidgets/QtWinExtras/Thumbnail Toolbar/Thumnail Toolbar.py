import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtWinExtras import QWinThumbnailToolBar, QWinThumbnailToolButton
from PyQt5.QtGui import QIcon


class Form(QMainWindow):
	def __init__(self):
		super().__init__()
		self.init_ui()

	def init_ui(self):
		self.resize(350, 150)
		self.setWindowTitle("Thumbnail Toolbar")
		label = QLabel("Hover on the taskbar button")
		label.resize(label.sizeHint())
		label.setAlignment(Qt.AlignCenter)
		self.setCentralWidget(label)
		toolbar = QWinThumbnailToolBar(self)
		toolbutton = QWinThumbnailToolButton(toolbar)
		toolbutton.setToolTip("Python")
		toolbutton.setIcon(QIcon("icon.ico"))
		toolbar.addButton(toolbutton)
		self.show()
		toolbar.setWindow(self.windowHandle())  # You must the window AFTER the window show event


app = QApplication(sys.argv)
form = Form()
sys.exit(app.exec_())
