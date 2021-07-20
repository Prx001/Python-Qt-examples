import sys
import webbrowser

from PyQt5.QtCore import Qt, QPoint, QRect, QEvent, QPropertyAnimation, QBasicTimer
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLabel, QDesktopWidget

from Widget import Ui_Form as Widget


class Form(QMainWindow):
	def __init__(self):
		super().__init__()

		self.setStyleSheet("""QMainWindow {
	background-image: url(:/resources/resources/Wallpaper.png);
}""")
		self.widget1 = Widget()
		self.close_button = QPushButton(self)
		self.close_button.setGeometry(1230, 0, 50, 40)
		self.close_button.setStyleSheet("""QPushButton {
	border-image: url(:/resources/resources/Close.png);
}
QPushButton::hover {
	border-image: url(:/resources/resources/Close_hovered.png);
}""")
		self.close_button.setText("")
		self.help_button = QPushButton(self)
		self.help_button.setGeometry(1180, 0, 50, 40)
		self.help_button.setStyleSheet("""QPushButton {
	border-image: url(:/resources/resources/Help.png);
}
QPushButton::hover {
	border-image: url(:/resources/resources/Help_hovered.png);
}""")
		self.help_button.setText("")
		self.help_button.setObjectName("help_button")
		self.minimize_button = QPushButton(self)
		self.minimize_button.setGeometry(1130, 0, 50, 40)
		self.minimize_button.setStyleSheet("""QPushButton {
	border-image: url(:/resources/resources/Minimize.png);
}
QPushButton::hover {
	border-image: url(:/resources/resources/Minimize_hovered.png);
}""")
		self.minimize_button.setText("")
		self.minimize_button.setObjectName("minimize_button")
		self.left = QWidget(self)
		self.left.move(0, 0)
		self.widget1.valorant_logo = QLabel(self.left)
		self.widget1.valorant_logo.setGeometry(QRect(168, -51, 66, 61))
		self.widget1.valorant_logo.setStyleSheet("border-image: url(:/resources/resources/VALORANT.png);")
		self.widget1.valorant_logo.setText("")
		self.valorant_logo_animation = QPropertyAnimation(self.widget1.valorant_logo, b"geometry")
		self.valorant_logo_animation.setDuration(500)
		self.valorant_logo_animation.setStartValue(self.widget1.valorant_logo.geometry())
		self.valorant_logo_animation.setEndValue(QRect(168, 51, 66, 61))
		self.right = QWidget(self)
		self.right.move(400, 0)

		self.initUI()

	def initUI(self):
		self.resize(1280, 720)
		self.move_to_center()
		self.setFixedSize(self.size())
		self.setWindowFlag(Qt.FramelessWindowHint)
		self.widget1.setupUi(self.left)

		self.riot_games_logo_animation = QPropertyAnimation(self.widget1.riot_games_logo, b"geometry")
		self.riot_games_logo_animation.setDuration(500)
		self.riot_games_logo_animation.setStartValue(self.widget1.riot_games_logo.geometry())
		self.riot_games_logo_animation.setEndValue(QRect(138, -51, 126, 61))

		self.username_title_animation = QPropertyAnimation(self.widget1.username_label, b"geometry")
		self.username_title_animation.setDuration(200)
		self.username_title_animation.setStartValue(self.widget1.username_label.geometry())
		self.username_title_animation.setEndValue(QRect(62, 222, 59, 8))

		self.password_title_animation = QPropertyAnimation(self.widget1.password_label, b"geometry")
		self.password_title_animation.setDuration(200)
		self.password_title_animation.setStartValue(self.widget1.password_label.geometry())
		self.password_title_animation.setEndValue(QRect(62, 286, 61, 8))

		self.username_title_reverse_animation = QPropertyAnimation(self.widget1.username_label, b"geometry")
		self.username_title_reverse_animation.setDuration(200)
		self.username_title_reverse_animation.setStartValue(QRect(62, 222, 59, 8))
		self.username_title_reverse_animation.setEndValue(QRect(72, 236, 59, 8))

		self.password_title_reverse_animation = QPropertyAnimation(self.widget1.password_label, b"geometry")
		self.password_title_reverse_animation.setDuration(200)
		self.password_title_reverse_animation.setStartValue(QRect(62, 286, 61, 8))
		self.password_title_reverse_animation.setEndValue(QRect(72, 300, 61, 8))

		self.widget1.username_line_edit.installEventFilter(self)
		self.widget1.password_line_edit.installEventFilter(self)
		# self.installEventFilter(self)
		self.close_button.clicked.connect(self.close)
		self.minimize_button.clicked.connect(self.showMinimized)
		self.help_button.clicked.connect(self.show_help)
		self.widget1.login_button.setStyleSheet("border-image: url(:/resources/resources/Login_button_disabled.png);")
		self.widget1.login_button.pressed.connect(self.login_button_pressed)
		self.widget1.login_button.released.connect(self.login_button_released)
		self.widget1.username_line_edit.textChanged.connect(self.line_edit_text_changed)
		self.widget1.password_line_edit.textChanged.connect(self.line_edit_text_changed)
		self.widget1.facebook_button.clicked.connect(self.facebook_button_clicked)
		self.widget1.facebook_button.pressed.connect(self.facebook_button_pressed)
		self.widget1.facebook_button.released.connect(self.facebook_button_released)
		self.widget1.google_button.clicked.connect(self.google_button_clicked)
		self.widget1.google_button.pressed.connect(self.google_button_pressed)
		self.widget1.google_button.released.connect(self.google_button_released)
		self.widget1.apple_button.clicked.connect(self.apple_button_clicked)
		self.widget1.apple_button.pressed.connect(self.apple_button_pressed)
		self.widget1.apple_button.released.connect(self.apple_button_released)
		self.widget1.stay_signed_in_checkbox.stateChanged.connect(self.checkbox_state_changed)
		self.widget1.checkbox_label.installEventFilter(self)
		self.timer = QBasicTimer()
		self.second = 0
		self.show()
		self.timer.start(1000, self)

	def timerEvent(self, time_event):
		if self.second == 2:
			self.riot_games_logo_animation.start()
		if self.second == 3:
			self.valorant_logo_animation.start()
			del self.widget1.riot_games_logo
			self.timer.stop()
		self.second += 1
		return super().timerEvent(time_event)

	def eventFilter(self, object, event):
		if object == self.widget1.username_line_edit:
			if event.type() == QEvent.FocusIn and self.widget1.username_line_edit.text() == "":
				self.username_title_animation.start()
			elif event.type() == QEvent.FocusOut and self.widget1.username_line_edit.text() == "":
				self.username_title_reverse_animation.start()
		elif object == self.widget1.password_line_edit:
			if event.type() == QEvent.FocusIn and self.widget1.password_line_edit.text() == "":
				self.password_title_animation.start()
			elif event.type() == QEvent.FocusOut and self.widget1.password_line_edit.text() == "":
				self.password_title_reverse_animation.start()
		elif object == self.widget1.checkbox_label and event.type() == QEvent.MouseButtonDblClick:
			if not self.widget1.stay_signed_in_checkbox.isChecked():
				self.widget1.stay_signed_in_checkbox.setChecked(True)
			elif self.widget1.stay_signed_in_checkbox.isChecked():
				self.widget1.stay_signed_in_checkbox.setChecked(False)
		# if object == self:
		# 	if self.widget1.username_line_edit.hasFocus():
		# 		self.widget1.username_line_edit.clearFocus()
		# 	elif self.widget1.password_line_edit.hasFocus():
		# 		self.widget1.password_line_edit.clearFocus()
		# 	else:
		# 		pass
		return super().eventFilter(object, event)

	def show_help(self):
		webbrowser.open("https://support.riotgames.com/hc/en-us", new=2, autoraise=True)

	def line_edit_text_changed(self):
		if self.widget1.username_line_edit.text() != "" and self.widget1.password_line_edit.text() != "":
			self.widget1.login_button.setStyleSheet("""QPushButton {
	border-image: url(:/resources/resources/Login_button.png);
}
QPushButton::hover {
	border-image: url(:/resources/resources/Login_button_hovered.png);
}""")
		elif self.widget1.username_line_edit.text() == "" or self.widget1.password_line_edit.text() == "":
			self.widget1.login_button.setStyleSheet(
				"border-image: url(:/resources/resources/Login_button_disabled.png);")

	def login_button_pressed(self):
		self.widget1.login_button.setStyleSheet(
			"""border-image: url(:/resources/resources/Login_button_clicked.png);""")

	def login_button_released(self):
		self.widget1.login_button.setStyleSheet("""QPushButton {
	border-image: url(:/resources/resources/Login_button.png);
}
QPushButton::hover {
	border-image: url(:/resources/resources/Login_button_hovered.png);
}""")

	def facebook_button_clicked(self):
		webbrowser.open(
			"https://www.facebook.com/v8.0/dialog/oauth?client_id=344190606773871&redirect_uri=https%3A%2F%2Fauthenticate.riotgames.com%2Fredirects%2Ffacebook&state=0e2e4d7ec57976960f61b9f22eed0cb2da5450f8f20362c11833a0a4e0e0&scope=email",
			new=2, autoraise=True)

	def facebook_button_pressed(self):
		self.widget1.facebook_button.setStyleSheet("""QPushButton {
	border-image: url(:/resources/resources/Facebook_clicked.png);
}""")

	def facebook_button_released(self):
		self.widget1.facebook_button.setStyleSheet("""QPushButton {
	border-image: url(:/resources/resources/Facebook.png);
}
QPushButton::hover {
	border-image: url(:/resources/resources/Facebook_hovered.png);
}""")

	def google_button_clicked(self):
		webbrowser.open(
			"https://accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount?access_type=online&scope=openid%20profile%20email&state=e5fb53d0ec477f7222bf347dfa58f44491235be3bdcaf7a4afd81d35f43d&prompt=select_account&response_type=code&client_id=187685766663-ct6bdnthcq6jlllecpg1guhthoc7i8vv.apps.googleusercontent.com&redirect_uri=https%3A%2F%2Fauthenticate.riotgames.com%2Fredirects%2Fgoogle&flowName=GeneralOAuthFlow",
			new=2, autoraise=True)

	def google_button_pressed(self):
		self.widget1.google_button.setStyleSheet("""QPushButton {
	border-image: url(:/resources/resources/Google_clicked.png);
}""")

	def google_button_released(self):
		self.widget1.google_button.setStyleSheet("""QPushButton {
	border-image: url(:/resources/resources/Google.png);
}
QPushButton::hover {
	border-image: url(:/resources/resources/Google_hovered.png);
}""")

	def apple_button_clicked(self):
		webbrowser.open(
			"https://appleid.apple.com/auth/authorize?response_type=code%20id_token&response_mode=form_post&client_id=com.riotgames.authenticator.prod.client&redirect_uri=https%3A%2F%2Fauthenticate.riotgames.com%2Fredirects%2Fapple&scope=name%20email&nonce=0f42d321114d78d1537c53d0ea67accdb834607ca79f3dfb42f9eb934b1b",
			new=2, autoraise=True)

	def apple_button_pressed(self):
		self.widget1.apple_button.setStyleSheet("""QPushButton {
	border-image: url(:/resources/resources/Apple_clicked.png);
}""")

	def apple_button_released(self):
		self.widget1.apple_button.setStyleSheet("""QPushButton {
	border-image: url(:/resources/resources/Apple.png);
}
QPushButton::hover {
	border-image: url(:/resources/resources/Apple_hovered.png);
}""")

	def checkbox_state_changed(self):
		if self.widget1.stay_signed_in_checkbox.isChecked():
			self.widget1.checkbox_label.setStyleSheet(
				"""border-image: url(:/resources/resources/Checkbox_label_checked.png);""")
		elif not self.widget1.stay_signed_in_checkbox.isChecked():
			self.widget1.checkbox_label.setStyleSheet("""QLabel {
	border-image: url(:/resources/resources/Checkbox_label.png);
}
QLabel::hover {
	border-image: url(:/resources/resources/Checkbox_label_hovered.png);
}""")

	def mousePressEvent(self, event):
		self.oldPos = event.globalPos()

	def mouseMoveEvent(self, event):
		try:
			delta = QPoint(event.globalPos() - self.oldPos)
			self.move(self.x() + delta.x(), self.y() + delta.y())
			self.oldPos = event.globalPos()
		except (AttributeError, UnboundLocalError):
			pass

	def move_to_center(self):
		qr = self.frameGeometry()
		cp = QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())


app = QApplication(sys.argv)
form = Form()
sys.exit(app.exec_())
