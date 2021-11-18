import sys

from PySide2.QtCore import QDir, QCoreApplication
from PySide2.QtWidgets import QApplication, QWidget
from PySide2.QtWinExtras import QWinJumpList, QWinJumpListItem, QWinJumpListCategory


class Form(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.resize(500, 300)
		self.setWindowTitle("Windows Jump Lists")
		jumplist = QWinJumpList()
		tasks = jumplist.tasks()
		newProject = QWinJumpListItem(QWinJumpListItem.Link)
		newProject.setTitle("Create new project")
		newProject.setFilePath(QDir.toNativeSeparators(QCoreApplication.applicationFilePath()))
		newProject.setArguments("--new-project")
		tasks.addItem(newProject)
		# tasks.addLink("Launch SDK Manager", QDir.toNativeSeparators(QCoreApplication.applicationDirPath()) + "\\sdk-manager.exe")
		tasks.setVisible(True)
		self.show()


app = QApplication(sys.argv)
form = Form()
sys.exit(app.exec_())