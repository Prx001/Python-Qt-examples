import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QTextBrowser


class Form(QMainWindow):
	def __init__(self):
		"""MainWindow constructor."""
		super().__init__()
		# Main UI code goes here
		main = QTextBrowser()
		self.setCentralWidget(main)

		# Must come before the HTML is inserted
		main.document().setDefaultStyleSheet(
			"body {color: #333; font-size: 14px;} "
			"h2 {background: #CCF; color: #443;} "
			"h1 {background: #001133; color: white;} "
		)

		# TextBrowser background is a widget style, not a document style
		main.setStyleSheet("background-color: #EEF;")
		with open("htmls\\new.html", "r") as fh:
			main.insertHtml(fh.read())

		main.setOpenExternalLinks(True)

		# End main UI code
		self.show()


app = QApplication(sys.argv)
form = Form()
sys.exit(app.exec_())
