import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QStyle
from PyQt5.QtGui import QIcon
from UI_Form import Ui_MainWindow


class Form(QMainWindow, Ui_MainWindow):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.init_ui()

	def init_ui(self):
		style = self.style()
		self.backward_action = QAction("")
		self.backward_action.setDisabled(True)
		self.backward_action.setIcon(style.standardIcon(QStyle.SP_ArrowBack))
		self.backward_action.triggered.connect(self.text_browser.backward)
		self.forward_action = QAction("")
		self.forward_action.setDisabled(True)
		self.forward_action.setIcon(QIcon(style.standardIcon(QStyle.SP_ArrowForward).pixmap(24, 24)))
		self.forward_action.triggered.connect(self.text_browser.forward)
		self.tool_bar.addAction(self.backward_action)
		self.tool_bar.addAction(self.forward_action)
		self.tool_bar.addAction(self.forward_action)
		self.text_browser.backwardAvailable.connect(lambda: self.backward_action.setEnabled(True) if self.text_browser.isBackwardAvailable() else self.backward_action.setDisabled(True))
		self.text_browser.forwardAvailable.connect(lambda: self.forward_action.setEnabled(True) if self.text_browser.isForwardAvailable() else self.forward_action.setDisabled(True))
		self.show()


app = QApplication(sys.argv)
form = Form()
sys.exit(app.exec_())
