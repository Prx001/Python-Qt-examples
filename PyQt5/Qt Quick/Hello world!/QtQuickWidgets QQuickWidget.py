# QtQuickWidgets/QQuickWidget
import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
from PyQt5.QtQuickWidgets import QQuickWidget

if __name__ == "__main__":
	app = QApplication(sys.argv)
	view = QQuickWidget()
	view.setSource(QUrl("Sample_QML.qml"))
	view.show()
	sys.exit(app.exec_())
