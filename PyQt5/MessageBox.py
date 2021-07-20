import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
class Form(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()
	def initUI(self):
		self.setGeometry(500, 500, 200, 120)
		self.setWindowTitle("Messagebox")
		self.show()
	def closeEvent(self, event):
		response = QMessageBox.warning(self, "Exit? :(", "Do you really want to exit this funny program? :(", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
		if response == QMessageBox.No:
			event.ignore()
		elif response == QMessageBox.Yes:
			event.accept()
app = QApplication(sys.argv)
form = Form()
sys.exit(app.exec_())