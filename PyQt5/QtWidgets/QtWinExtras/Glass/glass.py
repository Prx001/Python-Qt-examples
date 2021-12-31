import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWinExtras import QtWin


class Form(QMainWindow):
	def __init__(self):
		super().__init__()
		self.init_ui()
		QtWin.extendFrameIntoClientArea(self.windowHandle(), -1, -1, -1, -1)
		QtWin.enableBlurBehindWindow(self.windowHandle())

	def init_ui(self):
		self.resize(300, 200)
		self.show()


app = QApplication(sys.argv)
form = Form()
sys.exit(app.exec_())
