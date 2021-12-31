import sys

from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QLineEdit, QInputDialog, QFontDialog,
                             QColorDialog, QVBoxLayout, QHBoxLayout, QDesktopWidget)


class Form(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.resize(300, 240)
		self.moveToCenter()
		self.setWindowTitle("Dialogs")
		label = QLabel("Your text:")
		self.lineEdit = QLineEdit()
		editDialogButton = QPushButton("Change text")
		editDialogButton.clicked.connect(self.showEditDialog)
		fontDialogButton = QPushButton("Change font")
		fontDialogButton.clicked.connect(self.showFontDialog)
		colorDialogButton = QPushButton("Change color")
		colorDialogButton.clicked.connect(self.showColorDialog)
		hbox1 = QHBoxLayout()
		hbox1.addStretch(1)
		hbox1.addWidget(label)
		hbox1.addWidget(self.lineEdit)
		hbox1.addWidget(editDialogButton)
		hbox1.addStretch(1)
		vbox = QVBoxLayout()
		vbox.addStretch(1)
		vbox.addLayout(hbox1)
		vbox.addStretch(2)
		hbox2 = QHBoxLayout()
		hbox2.addWidget(fontDialogButton)
		hbox2.addWidget(colorDialogButton)
		hbox2.addStretch(1)
		vbox.addLayout(hbox2)
		self.setLayout(vbox)
		self.show()

	def moveToCenter(self):
		qr = self.frameGeometry()
		cp = QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())

	def showEditDialog(self):
		text, ok = QInputDialog.getText(self, "Edit text", "Enter new text")
		if ok:
			self.lineEdit.setText(str(text))

	def showFontDialog(self):
		font, ok = QFontDialog.getFont()
		if ok:
			self.lineEdit.setFont(font)

	def showColorDialog(self):
		color = QColorDialog.getColor()
		if color.isValid():
			self.lineEdit.setStyleSheet("color: %s" % color.name())


app = QApplication(sys.argv)
form = Form()
sys.exit(app.exec_())
