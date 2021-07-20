import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap
class Form(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setGeometry(450, 250, 300, 150)
        self.setWindowTitle("Pixmap")
        pixmap = QPixmap("icon.ico")
        label = QLabel(self)
        label.setPixmap(pixmap)
        self.setCentralWidget(label)
        self.show()
app = QApplication(sys.argv)
form = Form()
sys.exit(app.exec_())