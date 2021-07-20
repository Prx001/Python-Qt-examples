import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
class Form(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()
	def initUI(self):
		self.setGeometry(500, 300, 350, 250)
		self.setWindowTitle("Absolute")
		label1 = QLabel("This is a test for absolute positioning in PyQt5.", self)
		label1.move(10, 10)
		label2 = QLabel("There are some disadvantages for using this layout manager.", self)
		label2.move(10, 30)
		label3 = QLabel("1-Widgets aren't responsive to window resize.", self)
		label3.move(10, 50)
		label4 = QLabel("2-There might be some problems with the program in other platforms.", self)
		label4.move(10, 65)
		label5 = QLabel("3-It takes so much time and effort.", self)
		label5.move(10, 80)
		self.show()
app = QApplication(sys.argv)
form = Form()
sys.exit(app.exec_())