import sys
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QLineEdit, QTextEdit, QDesktopWidget
class ResizeResponseListener(QObject):
	resizedThin = pyqtSignal()
	resizedThiner = pyqtSignal()
	resizedThinest = pyqtSignal()
	resizedFat = pyqtSignal()
	resizedFater = pyqtSignal()
	resizedFatest = pyqtSignal()
	resizedShort = pyqtSignal()
	resizedShorter = pyqtSignal()
	resizedShortest = pyqtSignal()
	resizedTall = pyqtSignal()
	resizedTaller = pyqtSignal()
	resizedTallest = pyqtSignal()
class Form(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()
	def initUI(self):
		self.firstWidth = self.frameGeometry().width() + 1
		self.firstHeight = self.frameGeometry().height() + 1
		print(self.firstWidth)
		print(self.firstHeight)
		print(self.firstWidth - 300, self.firstHeight - 180)
		print(self.firstWidth + 300, self.firstHeight + 180)
		# self.moveToCenter()
		self.setMinimumSize(self.firstWidth - 300, self.firstHeight - 180)
		self.setMaximumSize(self.firstWidth + 300, self.firstHeight + 180)
		self.setWindowTitle("Responsive")
		nameLabel = QLabel("Name")
		nameEdit = QLineEdit()
		emailLabel = QLabel("Email")
		emailEdit = QLineEdit()
		commentLabel = QLabel("Comment")
		commentEdit = QTextEdit()
		self.grid = QGridLayout()
		self.grid.setSpacing(21)
		self.grid.addWidget(nameLabel, 1, 1)
		self.grid.addWidget(nameEdit, 1, 2)
		self.grid.addWidget(emailLabel, 2, 1)
		self.grid.addWidget(emailEdit, 2, 2)
		self.grid.addWidget(commentLabel, 3, 1)
		self.grid.addWidget(commentEdit, 3, 2, 6, 1)
		self.setLayout(self.grid)
		self.listener = ResizeResponseListener()
		self.listener.resizedThin.connect(self.thinResponse)
		self.listener.resizedThiner.connect(self.thinerResponse)
		self.listener.resizedThinest.connect(self.thinestResponse)
		self.listener.resizedFat.connect(self.fatResponse)
		self.listener.resizedFater.connect(self.faterResponse)
		self.listener.resizedFatest.connect(self.fatestResponse)
		self.listener.resizedShort.connect(self.shortResponse)
		self.listener.resizedShorter.connect(self.shorterResponse)
		self.listener.resizedShortest.connect(self.shortestResponse)
		self.listener.resizedTall.connect(self.tallResponse)
		self.listener.resizedTaller.connect(self.tallerResponse)
		self.listener.resizedTallest.connect(self.tallestResponse)
		self.show()
	def moveToCenter(self):
		qr = self.frameGeometry()
		cp = QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())
	def resizeEvent(self, new_size):
		resizedWidth = new_size.size().width()
		resizedHeight = new_size.size().height()
		# Thin, Thiner, Thinest
		if resizedWidth <= self.firstWidth - 100 and resizedWidth > self.firstWidth - 200:
			self.listener.resizedThin.emit()
		elif resizedWidth <= self.firstWidth - 200 and resizedWidth > self.firstWidth - 300:
			self.listener.resizedThiner.emit()
		elif resizedWidth == self.firstWidth - 300:
			self.listener.resizedThinest.emit()
		# Fat, Fater, Fatest
		if resizedWidth >= self.firstWidth + 100 and resizedWidth < self.firstWidth + 200:
			self.listener.resizedFat.emit()
		elif resizedWidth >= self.firstWidth + 200 and resizedWidth < self.firstWidth + 300:
			self.listener.resizedFater.emit()
		elif resizedWidth == self.firstWidth + 300:
			self.listener.resizedFatest.emit()
		# Short, Shorter, Shortes
		if resizedHeight <= self.firstHeight - 60 and resizedHeight > self.firstHeight - 120:
			self.listener.resizedShort.emit()
		elif resizedHeight <= self.firstHeight - 120 and resizedHeight > self.firstHeight - 180:
			self.listener.resizedShorter.emit()
		elif resizedHeight == self.firstHeight - 180:
			self.listener.resizedShortest.emit()
		# Tall, Taller, Tallest
		if resizedHeight >= self.firstHeight + 60 and resizedHeight < self.firstHeight + 120:
			self.listener.resizedTall.emit()
		elif resizedHeight >= self.firstHeight + 120 and resizedHeight < self.firstHeight + 180:
			self.listener.resizedTaller.emit()
		elif resizedHeight == self.firstHeight + 180:
			self.listener.resizedTaller.emit()
	def thinResponse(self):
		self.grid.setSpacing(15)
	def thinerResponse(self):
		self.grid.setSpacing(9)
	def thinestResponse(self):
		self.grid.setSpacing(3)
	def fatResponse(self):
		self.grid.setSpacing(27)
	def faterResponse(self):
		self.grid.setSpacing(33)
	def fatestResponse(self):
		self.grid.setSpacing(39)
	def shortResponse(self):
		self.grid.setSpacing(15)
	def shorterResponse(self):
		self.grid.setSpacing(9)
	def shortestResponse(self):
		self.grid.setSpacing(3)
	def tallResponse(self):
		self.grid.setSpacing(27)
	def tallerResponse(self):
		self.grid.setSpacing(33)
	def tallestResponse(self):
		self.grid.setSpacing(39)
app = QApplication(sys.argv)
form = Form()
sys.exit(app.exec_())