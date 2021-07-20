import sys
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QFont
class ResizeResponseListener(QObject):
	TooThin = pyqtSignal()
	BackToNormal = pyqtSignal()
class Form(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()
	def initUI(self):
		self.setGeometry(500, 300, 300, 250)
		self.setWindowTitle("Responsive")
		self.button = QPushButton("Button 1")
		self.smallFont = QFont()
		self.smallFont.setPointSize(7)
		self.normalFont = QFont()
		self.normalFont.setPointSize(8)
		hbox = QHBoxLayout()
		hbox.addStretch(1)
		hbox.addWidget(self.button)
		hbox.addStretch(1)
		vbox = QVBoxLayout()
		vbox.addStretch(1)
		vbox.addLayout(hbox)
		vbox.addStretch(1)
		self.setLayout(vbox)
		self.listener = ResizeResponseListener()
		self.listener.TooThin.connect(self.Response1)
		self.listener.BackToNormal.connect(self.Response2)
		self.show()
	def resizeEvent(self, new_size):
		if new_size.size().height() < 150 or new_size.size().width() < 250:
			self.listener.TooThin.emit()
		else:
			self.listener.BackToNormal.emit()
	def Response1(self):
		self.button.setFont(self.smallFont)
	def Response2(self):
		self.button.setFont(self.normalFont)
app = QApplication(sys.argv)
form = Form()
sys.exit(app.exec_())