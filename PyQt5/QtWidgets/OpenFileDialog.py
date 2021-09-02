import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QAction, QFileDialog
from pathlib import Path
user = str(Path.home())
class Form(QMainWindow):
	def __init__(self):
		super().__init__()
		self.initUI()
	def initUI(self):
		self.setGeometry(450, 250, 450, 300)
		self.setWindowTitle("Simple text reader")
		self.textEdit = QTextEdit(self)
		self.setCentralWidget(self.textEdit)
		QMenuBar = self.menuBar()
		fileMenu = QMenuBar.addMenu("File")
		openAct = QAction("Open", self)
		openAct.setShortcut("Ctrl+O")
		openAct.triggered.connect(self.showDialog)
		fileMenu.addAction(openAct)
		self.show()
	def showDialog(self):
		fileName = QFileDialog.getOpenFileName(self, "Select file to open", f"{user}\\Desktop", "*.txt")
		if fileName[0]:
			with open(fileName[0], "r") as file:
				content = file.read()
			self.textEdit.setText(str(content))
app = QApplication(sys.argv)
form = Form()
sys.exit(app.exec_())