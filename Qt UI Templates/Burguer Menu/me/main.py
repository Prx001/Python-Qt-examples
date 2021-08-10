import sys

from PyQt5.QtCore import QPropertyAnimation, QEasingCurve
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget

from Sample import Ui_Form


class Form(QMainWindow):
	def __init__(self):
		super().__init__()

		self.ui_form = Ui_Form()
		self.main_widget = QWidget()
		self.ui_form.setupUi(self.main_widget)
		self.animation = QPropertyAnimation(self.ui_form.left_menu_frame, b"minimumWidth")
		self.animation.setDuration(500)
		self.animation.setEasingCurve(QEasingCurve.InOutCubic)

		self.initUI()

	def initUI(self):
		self.resize(800, 600)
		self.setCentralWidget(self.main_widget)
		self.ui_form.toggle_button.clicked.connect(lambda: self.toggle_menu(250))
		self.ui_form.page1_button.clicked.connect(lambda: self.ui_form.stacked_widget.setCurrentIndex(0))
		self.ui_form.page2_button.clicked.connect(lambda: self.ui_form.stacked_widget.setCurrentIndex(1))
		self.ui_form.page3_button.clicked.connect(lambda: self.ui_form.stacked_widget.setCurrentIndex(2))
		self.show()

	def toggle_menu(self, new_width):
		width = self.ui_form.left_menu_frame.width()
		if width == 70:
			end_anim_width = new_width
		else:
			end_anim_width = 70
		self.animation.setStartValue(width)
		self.animation.setEndValue(end_anim_width)
		self.animation.start()


app = QApplication(sys.argv)
form = Form()
sys.exit(app.exec_())
