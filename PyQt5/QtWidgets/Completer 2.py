import sys

from PyQt5.QtCore import Qt, QAbstractListModel
from PyQt5.QtWidgets import QApplication, QWidget, QCompleter, QLineEdit
from PyQt5.QtGui import QIcon


class Model(QAbstractListModel):
	def __init__(self):
		super().__init__()
		self.stuff = ["alpha", "omega", "omicron", "zeta"]
		self.icon = QIcon("icon.ico")

	def data(self, index, role):
		if role == Qt.DisplayRole:
			text = self.stuff[index.row()]
			return text
		if role == Qt.DecorationRole:
			return self.icon
		if role == Qt.EditRole:
			text = self.stuff[index.row()]
			return text

	def rowCount(self, index):
		return len(self.stuff)


class Form(QWidget):
	def __init__(self):
		super().__init__()
		self.init_ui()

	def init_ui(self):
		self.text_edit = QLineEdit(self)
		self.text_edit.resize(400, 30)
		self.setWindowTitle("QCompleter")
		self.model = Model()
		self.completer = QCompleter(self.model, self)
		self.completer.setCaseSensitivity(Qt.CaseInsensitive)
		self.text_edit.setCompleter(self.completer)
		self.text_edit.move(20, 20)
		self.show()


app = QApplication(sys.argv)
form = Form()
sys.exit(app.exec_())
