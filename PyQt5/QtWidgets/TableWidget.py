import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem


class Form(QMainWindow):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.setGeometry(500, 300, 455, 160)
		self.setWindowTitle("Form1")
		table = QTableWidget(self)
		self.setCentralWidget(table)
		table.setRowCount(3)
		table.setColumnCount(3)
		table.setVerticalHeaderItem(0, QTableWidgetItem("Row 1"))
		table.setVerticalHeaderItem(1, QTableWidgetItem("Row 2"))
		table.setVerticalHeaderItem(2, QTableWidgetItem("Row 3"))
		# or simply:
		# table.setVerticalHeaderLabels(["Row 1", "Row 2", "Row 3"])
		table.setHorizontalHeaderItem(0, QTableWidgetItem("Column 1"))
		table.setHorizontalHeaderItem(1, QTableWidgetItem("Column 2"))
		table.setHorizontalHeaderItem(2, QTableWidgetItem("Column 3"))
		# or simply:
		# table.setHorizontalHeaderLabels(["Column 1", "Column 2", "Column 3"])
		table.setItem(0, 0, QTableWidgetItem("11"))
		table.setItem(0, 1, QTableWidgetItem("12"))
		table.setItem(0, 2, QTableWidgetItem("13"))
		table.setItem(1, 0, QTableWidgetItem("21"))
		table.setItem(1, 1, QTableWidgetItem("22"))
		table.setItem(1, 2, QTableWidgetItem("23"))
		table.setItem(2, 0, QTableWidgetItem("31"))
		table.setItem(2, 1, QTableWidgetItem("32"))
		table.setItem(2, 2, QTableWidgetItem("33"))
		self.show()


app = QApplication(sys.argv)
form = Form()
sys.exit(app.exec_())
