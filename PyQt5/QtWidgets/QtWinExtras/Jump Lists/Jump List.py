import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtWinExtras import QWinJumpList, QWinJumpListItem


class Form(QMainWindow):
	def __init__(self):
		super().__init__()
		self.init_ui()

	def init_ui(self):
		self.resize(350, 150)
		self.setWindowTitle("Windows Jump Lists")
		label = QLabel("Right click the taskbar button")
		label.resize(label.sizeHint())
		label.setAlignment(Qt.AlignCenter)
		self.setCentralWidget(label)
		jump_list = QWinJumpList()
		jump_list.clear()
		tasks = jump_list.tasks()  # "Frequent" and "Recent" categories are also accessible
		taskmgr = QWinJumpListItem(QWinJumpListItem.Link)
		taskmgr.setTitle("Open Task Manager!")
		taskmgr.setFilePath("C:\\Windows\\system32\\taskmgr.exe")
		tasks.addItem(taskmgr)
		tasks.setVisible(True)  # Necessary
		self.show()


app = QApplication(sys.argv)
form = Form()
sys.exit(app.exec_())
