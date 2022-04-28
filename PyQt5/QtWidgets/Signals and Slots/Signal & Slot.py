import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton


class Form(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.setWindowTitle("Signals/Slots")
		self.setGeometry(300, 300, 250, 180)
		QButton = QPushButton("Exit", self)
		QButton.resize(QButton.sizeHint())
		QButton.move(8, 150)
		QButton.clicked.connect(self.close)
		self.show()


app = QApplication(sys.argv)
form = Form()
sys.exit(app.exec_())
