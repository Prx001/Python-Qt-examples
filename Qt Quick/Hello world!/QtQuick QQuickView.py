# QtQuick/QQuickView
import sys

# from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
from PyQt5.QtQuick import QQuickView
from PyQt5.QtGui import QGuiApplication

if __name__ == "__main__":
	app = QGuiApplication(sys.argv)
	view = QQuickView()
	view.setSource(QUrl.fromLocalFile("Sample_QML.qml"))
	view.show()
	sys.exit(app.exec_())
