import sys
from PySide2.QtCore import Qt, QBasicTimer
from PySide2.QtWidgets import QApplication, QMainWindow
from ui_splash_screen import Ui_SplashScreen
class SplashScreen(QMainWindow):
	def __init__(self):
		super().__init__()

		self.ui_form = Ui_SplashScreen()
		self.ui_form.setupUi(self)
		self.timer = QBasicTimer()
		self.times = 1
		self.percentage = 0

		self.init_ui()
	def init_ui(self):
		self.setWindowFlag(Qt.FramelessWindowHint)
		self.setAttribute(Qt.WA_TranslucentBackground)
		self.timer.start(10, self)
		self.show()
	def timerEvent(self, time_event):
		if self.times > 0.001:
			self.times -= 0.001
			self.percentage += 0.1
			gradiant_value = round(self.times, 3)
			percentagevalue = int(round(self.percentage, 0))
			styleSheet = """QFrame {"""
			background_styleSheet = f"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{gradiant_value - 0.001} rgba(255, 0, 127, 0), stop:{gradiant_value} rgba(85, 170, 255, 255));"
			styleSheet += "\n"
			styleSheet += "border-radius: 150px;\n"
			styleSheet += background_styleSheet
			styleSheet += "\n"
			styleSheet += "}"
			self.ui_form.circularProgress.setStyleSheet(styleSheet)
			self.ui_form.percentage.setText(f"""<p><span style="font-size:68pt;">{percentagevalue}</span><span style="font-size: 58pt; vertical-align: super;">%</span></p>""")
			# print(self.times)
			# print(styleSheet)
		else:
			self.timer.stop()
			self.ui_form.circularProgress.setStyleSheet("""QFrame {
	border-radius: 150px;
	background-color: rgb(85, 170, 255)
}""")
			self.ui_form.percentage.setText("""<p><span style="font-size:68pt;">100</span><span style="font-size: 58pt; vertical-align: super;">%</span></p>""")
app = QApplication(sys.argv)
splash_screen = SplashScreen()
sys.exit(app.exec_())
