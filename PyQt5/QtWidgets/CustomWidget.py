import sys
from PyQt5.QtCore import Qt, QObject, pyqtSignal
from PyQt5.QtWidgets import QApplication, QWidget, QSlider, QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QPainter, QColor, QFont, QPen
class Listener(QObject):
	updateWidget = pyqtSignal(int)
class BurningWidget(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()
	def initUI(self):
		self.setMinimumSize(1, 30)
		self.value = 75
		self.nums = [75, 150, 225, 300, 375, 450, 525, 600, 675]
	def setValue(self, value):
		self.value = value
		self.repaint()
	def paintEvent(self, event):
		painter = QPainter()
		painter.begin(self)
		self.drawWidget(painter)
		painter.end()
	def drawWidget(self, painter):
		MAX_CAPACITY = 700
		OVER_CAPACITY = 750
		font = QFont("SansSerif", 10, QFont.Light)
		painter.setFont(font)
		size = self.size()
		w = size.width()
		h = size.height()
		step = int(round(w/10))
		till = int((w / OVER_CAPACITY) * self.value)
		full = int((w / OVER_CAPACITY) * MAX_CAPACITY)
		if self.value >= MAX_CAPACITY:
			painter.setPen(QColor(255, 255, 255))
			painter.setBrush(QColor(255, 255, 0))
			painter.drawRect(0, 0, full, h)
			painter.setPen(QColor(255, 175, 175))
			painter.setBrush(QColor(255, 0, 0))
			painter.drawRect(full, 0, till-full, h)
		elif self.value <= MAX_CAPACITY:
			painter.setPen(QColor(255, 255, 255))
			painter.setBrush(QColor(255, 255, 0))
			painter.drawRect(0, 0, till, h)
		pen = QPen(QColor(20, 20, 20))
		painter.setPen(pen)
		painter.setBrush(Qt.NoBrush)
		painter.drawRect(0, 0, w-1, h-1)
		j = 0
		for i in range(step, step*10, step):
			painter.drawLine(i, 0, i, 5)
			metrics = painter.fontMetrics()
			fw = metrics.width(str(self.nums[j]))
			painter.drawText(int(i-(fw/2)), int((h/2)+6), str(self.nums[j]))
			j += 1
class Form(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()
	def initUI(self):
		self.setGeometry(500, 300, 307, 119)
		self.setMinimumSize(307, 119)
		self.setWindowTitle("Burning Widget")
		OVER_CAPACITY = 750
		slider = QSlider(Qt.Horizontal)
		slider.setRange(1, OVER_CAPACITY)
		slider.setValue(75)
		self.listener = Listener()
		self.widget = BurningWidget()
		self.listener.updateWidget.connect(self.widget.setValue)
		slider.valueChanged.connect(self.changeValue)
		vbox = QVBoxLayout()
		vbox.addStretch(1)
		vbox.addWidget(slider)
		vbox.addStretch(1)
		vbox.addWidget(self.widget)
		vbox.addStretch(1)
		hbox = QHBoxLayout()
		hbox.addLayout(vbox)
		self.setLayout(hbox)
		self.show()
	def changeValue(self, value):
		self.listener.updateWidget.emit(value)
app = QApplication(sys.argv)
form = Form()
sys.exit(app.exec_())