import sys

from PyQt5.QtCore import Qt, QAbstractTableModel
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableView


class TableModel(QAbstractTableModel):
	def __init__(self, data):
		super().__init__()
		self.inner_data = data

	def data(self, index, role):
		if role == Qt.DisplayRole:
			return self.inner_data[index.row()][index.column()]

	def rowCount(self, index):
		return len(self.inner_data)

	def columnCount(self, index):
		return len(self.inner_data[0])


class Form(QMainWindow):
	def __init__(self):
		super().__init__()

		self.init_ui()

	def init_ui(self):
		self.resize(500, 300)
		self.setWindowTitle("Table Model")
		table = QTableView()
		data = [
			[2, 3, 4, 3, 1, 4, 1, 3],
			[3, 1, 5, 3, 5, 8, 2, 7],
			[8, 3, 6, 2, 3, 8, 2, 0],
			[1, 5, 2, 6, 8, 9, 2, 5],
			[5, 2, 5, 7, 2, 4, 1, 8]
		]
		model = TableModel(data)
		table.setModel(model)
		self.setCentralWidget(table)
		self.show()


app = QApplication(sys.argv)
form = Form()
sys.exit(app.exec_())
