"""
import qtmodern.styles
import qtmodern.windows
win = Form()
qtmodern.styles.dark(app)
mw = qtmodern.windows.ModernWindow(win)
mw.show()
"""
import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip
from PyQt5.QtGui import QFont
import qtmodern.windows


class Form(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		QToolTip.setFont(QFont("SansSerif", 10))
		self.setToolTip("This is the main form")
		QButton = QPushButton("Next", self)
		QButton.setToolTip("<p style='color:red;'>Red tooltip using CSS!</p>")
		# button.setToolTip("<h1 href='https://google.com'>QPushButton</a>")
		QButton.resize(QButton.sizeHint())
		QButton.move(35, 35)
		self.setGeometry(500, 500, 240, 150)
		self.setWindowTitle("Tooltips")
		self.setMaximumWidth(450)
		self.setFixedHeight(150)
		self.show()


app = QApplication(sys.argv)
win = Form()
qtmodern.styles.dark(app)
mw = qtmodern.windows.ModernWindow(win)
mw.show()
# form = Form()
sys.exit(app.exec_())
