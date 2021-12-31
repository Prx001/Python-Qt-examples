import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QFontDialog, QVBoxLayout, QHBoxLayout


class Form(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.setGeometry(450, 250, 250, 180)
		self.setWindowTitle("Font Dialog")
		button1 = QPushButton("Change font", self)
		button1.clicked.connect(self.showDialog)
		self.label = QLabel("PyQt5 is awesome!", self)
		hbox1 = QHBoxLayout()
		hbox1.addStretch(1)
		hbox1.addWidget(self.label)
		hbox1.addStretch(1)
		vbox = QVBoxLayout()
		vbox.addStretch(1)
		vbox.addLayout(hbox1)
		vbox.addStretch(2)
		hbox2 = QHBoxLayout()
		hbox2.addWidget(button1)
		hbox2.addStretch(1)
		vbox.addLayout(hbox2)
		self.setLayout(vbox)
		self.show()

	def showDialog(self):
		font, ok = QFontDialog.getFont()
		if ok:
			self.label.setFont(font)


app = QApplication(sys.argv)
form = Form()
sys.exit(app.exec_())
