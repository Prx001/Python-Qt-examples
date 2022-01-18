import sys

from PyQt5.QtCore import Qt, QDir
from PyQt5.QtWidgets import QApplication, QWidget, QCompleter, QLineEdit, QFileSystemModel


class Form(QWidget):
	def __init__(self):
		super().__init__()
		self.init_ui()

	def init_ui(self):
		self.text_edit = QLineEdit(self)
		self.text_edit.resize(400, 30)
		self.setWindowTitle("QCompleter")
		self.model = QFileSystemModel()
		self.model.setRootPath(QDir.rootPath())
		self.completer = QCompleter(self.model, self)
		self.completer.setCaseSensitivity(Qt.CaseInsensitive)
		self.text_edit.setCompleter(self.completer)
		self.text_edit.move(20, 20)
		self.show()


app = QApplication(sys.argv)
form = Form()
sys.exit(app.exec_())
