import sys

from PyQt5.QtWidgets import QApplication, QWidget, QCalendarWidget, QLabel, QVBoxLayout


class Form(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.setGeometry(450, 250, 350, 300)
		self.setWindowTitle("Calendar")
		vbox = QVBoxLayout()
		self.calendar = QCalendarWidget()
		self.calendar.clicked.connect(self.showDate)
		date = self.calendar.selectedDate()
		vbox.addWidget(self.calendar)
		self.label = QLabel(date.toString())
		vbox.addWidget(self.label)
		self.setLayout(vbox)
		self.show()

	def showDate(self, date):
		self.label.setText(date.toString())


app = QApplication(sys.argv)
form = Form()
sys.exit(app.exec_())
