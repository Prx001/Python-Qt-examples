import sys
from PyQt5.QtWidgets import QApplication, QWidget
app = QApplication(sys.argv)
form = QWidget()
form.setWindowTitle("Hello world!")
form.show()
sys.exit(app.exec_())