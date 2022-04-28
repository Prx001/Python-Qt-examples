import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QTableView
from PyQt5.QtGui import QStandardItemModel, QStandardItem


class Form(QMainWindow):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.resize(455, 160)
		self.setWindowTitle("QStandardItemModel")
		self.model = QStandardItemModel(3, 3)
		self.model.setVerticalHeaderLabels(["Row 1", "Row 2", "Row 3"])
		self.model.setHorizontalHeaderLabels(["Column 1", "Column 2", "Column 3"])
		self.model.setItem(0, 0, QStandardItem("11"))
		self.model.setItem(0, 1, QStandardItem("12"))
		self.model.setItem(0, 2, QStandardItem("13"))
		self.model.setItem(1, 0, QStandardItem("21"))
		self.model.setItem(1, 1, QStandardItem("22"))
		self.model.setItem(1, 2, QStandardItem("23"))
		self.model.setItem(2, 0, QStandardItem("31"))
		self.model.setItem(2, 1, QStandardItem("32"))
		self.model.setItem(2, 2, QStandardItem("33"))
		self.table = QTableView()
		self.table.setModel(self.model)
		self.setCentralWidget(self.table)
		self.show()


app = QApplication(sys.argv)
form = Form()
sys.exit(app.exec_())
