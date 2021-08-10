import sys
from PyQt5.QtCore import QEvent, QPoint, QPropertyAnimation, QParallelAnimationGroup
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtGui import QFont
from Main_widget import Ui_Form
class Form(QMainWindow):
	def __init__(self):
		super().__init__()

		self.main_widget = QWidget()
		self.ui_form = Ui_Form()

		self.initUI()
	def initUI(self):
		self.ui_form.setupUi(self.main_widget)
		self.setFixedSize(self.main_widget.size())
		self.setCentralWidget(self.main_widget)
		self.define_animations()
		self.ui_form.username_line_edit.installEventFilter(self)
		self.ui_form.password_line_edit.installEventFilter(self)
		self.show()
	def define_animations(self):
		self.username_label_anim = QPropertyAnimation(self.ui_form.username_label, b"pos")
		self.username_label_anim.setDuration(200)
		self.username_label_anim.setStartValue(QPoint(62, 228))
		self.username_label_anim.setEndValue(QPoint(54, 220))

		self.username_label_anim_reverse = QPropertyAnimation(self.ui_form.username_label, b"pos")
		self.username_label_anim_reverse.setDuration(200)
		self.username_label_anim_reverse.setStartValue(QPoint(54, 220))
		self.username_label_anim_reverse.setEndValue(QPoint(62, 228))


		self.username_label_font_anim = QPropertyAnimation(self.ui_form.username_label, b"font")
		self.username_label_font_anim.setDuration(200)
		self.username_label_font_anim.setStartValue(QFont("Segoe UI", 9))
		self.username_label_font_anim.setEndValue(QFont("Segoe UI", 7))

		self.username_label_font_anim_reverse = QPropertyAnimation(self.ui_form.username_label, b"font")
		self.username_label_font_anim_reverse.setDuration(200)
		self.username_label_font_anim_reverse.setStartValue(QFont("Segoe UI", 7))
		self.username_label_font_anim_reverse.setEndValue(QFont("Segoe UI", 9))



		self.password_label_anim = QPropertyAnimation(self.ui_form.password_label, b"pos")
		self.password_label_anim.setDuration(200)
		self.password_label_anim.setStartValue(QPoint(62, 282))
		self.password_label_anim.setEndValue(QPoint(54, 274))

		self.password_label_anim_reverse = QPropertyAnimation(self.ui_form.password_label, b"pos")
		self.password_label_anim_reverse.setDuration(200)
		self.password_label_anim_reverse.setStartValue(QPoint(54, 274))
		self.password_label_anim_reverse.setEndValue(QPoint(62, 282))


		self.password_label_font_anim = QPropertyAnimation(self.ui_form.password_label, b"font")
		self.password_label_font_anim.setDuration(200)
		self.password_label_font_anim.setStartValue(QFont("Segoe UI", 9))
		self.password_label_font_anim.setEndValue(QFont("Segoe UI", 4))

		self.password_label_font_anim_reverse = QPropertyAnimation(self.ui_form.password_label, b"font")
		self.password_label_font_anim_reverse.setDuration(200)
		self.password_label_font_anim_reverse.setStartValue(QFont("Segoe UI", 4))
		self.password_label_font_anim_reverse.setEndValue(QFont("Segoe UI", 9))




		self.username_label_anims = QParallelAnimationGroup()
		self.username_label_anims.addAnimation(self.username_label_anim)
		self.username_label_anims.addAnimation(self.username_label_font_anim)

		self.username_label_anims2 = QParallelAnimationGroup()
		self.username_label_anims2.addAnimation(self.username_label_anim_reverse)
		self.username_label_anims2.addAnimation(self.username_label_font_anim_reverse)



		self.password_label_anims = QParallelAnimationGroup()
		# self.password_label_anims.addAnimation(self.password_label_anim)
		self.password_label_anims.addAnimation(self.password_label_font_anim)

		self.password_label_anims2 = QParallelAnimationGroup()
		# self.password_label_anims2.addAnimation(self.password_label_anim_reverse)
		self.password_label_anims2.addAnimation(self.password_label_font_anim_reverse)
	def eventFilter(self, object, event):
		if object == self.ui_form.username_line_edit:
			if event.type() == QEvent.FocusIn and self.ui_form.username_line_edit.text() == "":
				self.username_label_anims.start()
			elif event.type() == QEvent.FocusOut and self.ui_form.username_line_edit.text() == "":
				self.username_label_anims2.start()
		elif object == self.ui_form.password_line_edit:
			if event.type() == QEvent.FocusIn and self.ui_form.password_line_edit.text() == "":
				self.password_label_font_anim.start()
			elif event.type() == QEvent.FocusOut and self.ui_form.password_line_edit.text() == "":
				self.password_label_font_anim_reverse.start()
		return super().eventFilter(object, event)
app = QApplication(sys.argv)
form = Form()
sys.exit(app.exec_())