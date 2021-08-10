import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QLineEdit, QTextEdit
class Form(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()
	def initUI(self):
		self.move(450, 250)
		self.setWindowTitle("QGridLayout")
		nameLabel = QLabel("Name")
		nameEdit = QLineEdit()
		emailLabel = QLabel("Email")
		emailEdit = QLineEdit()
		commentLabel = QLabel("Comment")
		commentEdit = QTextEdit()
		grid = QGridLayout()
		grid.setSpacing(10)
		grid.addWidget(nameLabel, 1, 0)
		grid.addWidget(nameEdit, 1, 1)
		grid.addWidget(emailLabel, 2, 0)
		grid.addWidget(emailEdit, 2, 1)
		grid.addWidget(commentLabel, 3, 0)
		grid.addWidget(commentEdit, 3, 1, 6, 1)
		self.setLayout(grid)
		self.show()
app = QApplication(sys.argv)
form = Form()
sys.exit(app.exec_())