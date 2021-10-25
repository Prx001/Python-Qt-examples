import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QTextBrowser
from PyQt5.QtGui import QFont


class Form(QMainWindow):
	def __init__(self):
		super().__init__()
		self.init_ui()

	def init_ui(self):
		self.resize(400, 300)
		self.setWindowTitle("QTextBrowser")
		text_browser = QTextBrowser()
		text_browser.setOpenExternalLinks(True)
		text_browser.setFont(QFont("Segue UI", 20))
		text_browser.append("Some text")
		text_browser.append("<a href=https://qt.io>Qt</a>")
		self.setCentralWidget(text_browser)
		self.show()


app = QApplication(sys.argv)
form = Form()
sys.exit(app.exec_())
