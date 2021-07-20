import sys
import os
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from py_toggle import PyToggle

class Form(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.container = QFrame()
        self.container.setObjectName("container")
        self.container.setStyleSheet("#container { background-color: #222 }")
        self.layout = QVBoxLayout()
        self.toggle = PyToggle(active_color="#aa00ff")
        self.layout.addWidget(self.toggle, Qt.AlignCenter, Qt.AlignCenter)
        self.container.setLayout(self.layout)
        self.setCentralWidget(self.container)
        self.show()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Form()
    sys.exit(app.exec_())