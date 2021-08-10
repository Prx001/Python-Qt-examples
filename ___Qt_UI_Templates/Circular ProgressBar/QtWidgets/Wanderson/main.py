import sys
from PySide2.QtWidgets import QApplication, QMainWindow
from ui_splash_screen import Ui_SplashScreen
class SplashScren(QMainWindow):
	def __init__(self):
		super().__init__()

		self.ui_form = Ui_SplashScreen()
		self.ui_form.setupUi(self)

		self.init_ui()
	def init_ui(self):
		self.show()
app = QApplication(sys.argv)
splash_screen = SplashScren()
sys.exit(app.exec_())
