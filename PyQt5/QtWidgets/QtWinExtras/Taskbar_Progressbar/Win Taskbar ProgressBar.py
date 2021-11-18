import sys

from PySide2.QtWidgets import QApplication, QWidget
from PySide2.QtGui import QIcon
from PySide2.QtWinExtras import QWinTaskbarButton


class Form(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.resize(500, 300)
		self.setWindowTitle("Windows Taskbar ProgressBar")
		self.show()
		taskbar_button = QWinTaskbarButton(self)
		taskbar_button.setWindow(self.windowHandle())
		taskbar_progress = taskbar_button.progress()
		taskbar_progress.setValue(60)
		taskbar_button.setOverlayIcon(QIcon("badge-1.ico"))
		taskbar_progress.show()


app = QApplication(sys.argv)
form = Form()
sys.exit(app.exec_())
# C++
# QWinTaskbarButton *button = new QWinTaskbarButton(widget);
# button->setWindow(widget->windowHandle());
# button->setOverlayIcon(QIcon(":/loading.png"));
#
# QWinTaskbarProgress *progress = button->progress();
# progress->setVisible(true);
# progress->setValue(50);
