import sys
import json

from PyQt5.QtCore import QAbstractListModel, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon

from Form import Ui_MainWindow


class TodoModel(QAbstractListModel):
	def __init__(self, todos=None):
		super().__init__()
		self.todos = todos or []
		self.completed_icon = QIcon("tick.png")

	def get_loaded_data(self, data: list):
		self.todos = data

	def add_todo(self, todo: tuple):
		self.todos.append(todo)

	def delete(self, index):
		del self.todos[index.row()]

	def complete(self, index):
		self.todos[index.row()] = (True, self.todos[index.row()][1])

	def data(self, index, role):
		if role == Qt.DisplayRole:
			text = self.todos[index.row()][1]
			return text
		if role == Qt.DecorationRole:
			status = self.todos[index.row()][0]
			if status:
				return self.completed_icon

	def rowCount(self, index):
		return len(self.todos)


class Form(QMainWindow, Ui_MainWindow):
	def __init__(self):
		super().__init__()

		self.setupUi(self)
		self.model = TodoModel()

		self.init_ui()

	def init_ui(self):
		self.todoView.setModel(self.model)
		self.addButton.clicked.connect(self.add_todo)
		self.deleteButton.clicked.connect(self.delete)
		self.completeButton.clicked.connect(self.complete)
		self.load_data()
		self.show()

	def load_data(self):
		try:
			with open("data.json", "r") as file:
				data = json.load(file)
			self.model.get_loaded_data(data)
		except FileNotFoundError:
			pass

	def save_data(self):
		with open("data.json", "w") as file:
			json.dump(self.model.todos, file)

	def add_todo(self):
		text = self.todoEdit.text()
		text = text.strip()
		if text:
			self.model.add_todo((False, text))
			self.model.layoutChanged.emit()
			self.todoEdit.setText("")

	def delete(self):
		if self.todoView.selectedIndexes():
			items = self.todoView.selectedIndexes()
			for item in items:
				self.model.delete(item)
			self.model.layoutChanged.emit()
			self.todoView.clearSelection()

	def complete(self):
		if self.todoView.selectedIndexes():
			items = self.todoView.selectedIndexes()
			for item in items:
				self.model.complete(item)
				self.model.dataChanged.emit(item, item)
			self.todoView.clearSelection()

	def closeEvent(self, event):
		self.save_data()
		super().closeEvent(event)


app = QApplication(sys.argv)
form = Form()
sys.exit(app.exec_())
