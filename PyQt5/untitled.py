import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QCommandLinkButton, QCheckBox, QRadioButton, QToolTip, QDesktopWidget, QMessageBox
from PyQt5.QtGui import QIcon
class Form(QMainWindow):
	def __init__(self):
		super().__init__()
		self.initUI()
	def initUI(self):
		self.setWindowTitle("Avira engine core")
		self.setWindowIcon(QIcon(r"E:\Windows 7 Programs\Opera GX\73.0.3856.414\resources\FFF3F819-B6CE-4DE6-B4E4-8E2618ABC0D9.ico"))
		self.resize(400, 400)
		# self.move(100, 100)
		self.moveCenter()
		QButton = QPushButton("Why?", self)
		QButton.resize(QButton.sizeHint())
		QButton.setToolTip("Hi there bitch this is a <b>QPushButton</b>")
		QButton.move(200, 200)
		QButton.clicked.connect(QButton.hide)
		QComLnkBtn = QCommandLinkButton("Next", self)
		QComLnkBtn.resize(80, 43)
		QComLnkBtn.move(20, 20)
		QCheckbox = QCheckBox("Kill switch", self)
		QCheckbox.resize(QCheckbox.sizeHint())
		QCheckbox.move(320, 360)
		QCheckbox.setToolTip("Don't uncheck it bitch")
		QCheckbox.setChecked(True)
		QCheckbox.setTristate(True)
		QRadio = QRadioButton("How the fuck groupings work?", self)
		QRadio.resize(QRadio.sizeHint())
		QRadio.move(5, 300)
		self.show()
	def moveCenter(self):
		qr = self.frameGeometry()
		cp = QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())
	def closeEvent(self, event):
		response = QMessageBox.warning(self, "Hey stop right there", "Where are you going bitch?\nBitch really?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
		if response == QMessageBox.No:
			event.ignore()
		elif response == QMessageBox.Yes:
			event.accept()
app = QApplication(sys.argv)
form = Form()
sys.exit(app.exec_())