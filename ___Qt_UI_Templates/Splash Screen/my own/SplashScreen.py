import sys
from PyQt5 import QtCore, QtGui, QtWidgets
class Form(QtWidgets.QMainWindow):
	def __init__(self):
		super().__init__()
		self.initUI(self)
	def initUI(self, SplashScreen):
		SplashScreen.setObjectName("SplashScreen")
		SplashScreen.resize(680, 400)
		SplashScreen.setWindowFlag(QtCore.Qt.FramelessWindowHint)
		SplashScreen.setAttribute(QtCore.Qt.WA_TranslucentBackground)
		self.centralwidget = QtWidgets.QWidget(SplashScreen)
		self.centralwidget.setObjectName("centralwidget")
		self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
		self.verticalLayout.setContentsMargins(10, 10, 10, 10)
		self.verticalLayout.setSpacing(0)
		self.verticalLayout.setObjectName("verticalLayout")
		self.dropShadowFrame = QtWidgets.QFrame(self.centralwidget)
		self.dropShadowFrame.setStyleSheet(" QFrame{\n"
		                                   "    background-color: rgb(56, 58, 89);\n"
		                                   "    color: rgb(220, 220, 220);\n"
		                                   "    border-radius: 10px\n"
		                                   "}")
		self.dropShadowFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.dropShadowFrame.setFrameShadow(QtWidgets.QFrame.Raised)
		self.dropShadowFrame.setObjectName("dropShadowFrame")
		self.lableTitle = QtWidgets.QLabel(self.dropShadowFrame)
		self.lableTitle.setGeometry(QtCore.QRect(3, 88, 655, 103))
		font = QtGui.QFont()
		font.setFamily("Segoe UI")
		font.setPointSize(40)
		self.lableTitle.setFont(font)
		self.lableTitle.setStyleSheet("color: rgb(254, 121, 199);")
		self.lableTitle.setAlignment(QtCore.Qt.AlignCenter)
		self.lableTitle.setObjectName("lableTitle")
		self.labelDescription = QtWidgets.QLabel(self.dropShadowFrame)
		self.labelDescription.setGeometry(QtCore.QRect(0, 174, 659, 33))
		font = QtGui.QFont()
		font.setFamily("Segoe UI")
		font.setPointSize(14)
		self.labelDescription.setFont(font)
		self.labelDescription.setStyleSheet("color: rgb(98, 114, 164);")
		self.labelDescription.setAlignment(QtCore.Qt.AlignCenter)
		self.labelDescription.setObjectName("labelDescription")
		self.progressBar = QtWidgets.QProgressBar(self.dropShadowFrame)
		self.progressBar.setGeometry(QtCore.QRect(30, 278, 593, 23))
		self.progressBar.setStyleSheet("QProgressBar {\n"
		                               "    background-color: rgb(98, 114, 164);\n"
		                               "    color: rgb(200, 200, 200);\n"
		                               "    border-style:  none;\n"
		                               "    border-radius: 10px;\n"
		                               "    text-align: center;\n"
		                               "}\n"
		                               "QProgressBar::chunk {\n"
		                               "    border-radius: 10px;\n"
		                               "    background-color: qlineargradient(spread:pad, x1:0, y1:0.529, x2:1, y2:0.495, stop:0 rgba(254, 121, 199, 255), stop:1 rgba(170, 85, 255, 255));\n"
		                               "}")
		self.progressBar.setProperty("value", 24)
		self.progressBar.setObjectName("progressBar")
		self.progressBar.setValue(0)
		self.timer = QtCore.QBasicTimer()
		self.step = 0
		self.labelLoading = QtWidgets.QLabel(self.dropShadowFrame)
		self.labelLoading.setGeometry(QtCore.QRect(0, 304, 659, 43))
		font = QtGui.QFont()
		font.setFamily("Segoe UI")
		font.setPointSize(12)
		self.labelLoading.setFont(font)
		self.labelLoading.setStyleSheet("color: rgb(98, 114, 164);")
		self.labelLoading.setAlignment(QtCore.Qt.AlignCenter)
		self.labelLoading.setObjectName("labelLoading")
		self.verticalLayout.addWidget(self.dropShadowFrame)
		SplashScreen.setCentralWidget(self.centralwidget)
		self.retranslateUi(SplashScreen)
		QtCore.QMetaObject.connectSlotsByName(SplashScreen)
	def retranslateUi(self, SplashScreen):
		_translate = QtCore.QCoreApplication.translate
		SplashScreen.setWindowTitle(_translate("SplashScreen", "MainWindow"))
		self.lableTitle.setText(_translate("SplashScreen", "<strong> YOUR </strong> APP NAME"))
		self.labelDescription.setText(_translate("SplashScreen", "<strong> APP </strong> DESCRIPTION"))
		self.labelLoading.setText(_translate("SplashScreen", "Loading..."))
		SplashScreen.show()
		self.boom(SplashScreen)
	def mousePressEvent(self, event):
		self.oldPos = event.globalPos()
	def mouseMoveEvent(self, event):
		delta = QtCore.QPoint(event.globalPos() - self.oldPos)
		self.move(self.x() + delta.x(), self.y() + delta.y())
		self.oldPos = event.globalPos()
	def timerEvent(self, time_event):
		if self.step >= 100:
			self.timer.stop()
		self.step += 1
		self.progressBar.setValue(self.step)
		return super().timerEvent(time_event)
	def boom(self, SplashScreen):
		self.timer.start(100, SplashScreen)
app = QtWidgets.QApplication(sys.argv)
form = Form()
sys.exit(app.exec_())