import sys

from PyQt5.QtCore import QEasingCurve
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtChart import QChart, QChartView, QBarSet, QPercentBarSeries, QBarCategoryAxis
from PyQt5.QtGui import QPainter


class Form(QMainWindow):
	def __init__(self):
		super().__init__()
		self.init_ui()

	def init_ui(self):
		self.resize(800, 600)
		self.setWindowTitle("QtChart")
		self.initialize_chart()
		self.show()

	def initialize_chart(self):
		set0 = QBarSet("Python")
		set1 = QBarSet("C++")
		set2 = QBarSet("Java")
		set3 = QBarSet("C#")
		set4 = QBarSet("JavaScript")

		set0 << 2 << 4 << 1
		set1 << 1 << 3 << 2
		set2 << 1 << 4 << 2
		set3 << 3 << 2 << 4
		set4 << 2 << 4 << 1

		series = QPercentBarSeries()
		series.append(set0)
		series.append(set1)
		series.append(set2)
		series.append(set3)
		series.append(set4)

		chart = QChart()
		chart.setTitle("Popular programming language")
		chart.addSeries(series)
		chart.setAnimationOptions(QChart.AllAnimations)
		chart.setAnimationEasingCurve(QEasingCurve.InOutCubic)

		# chart.legend().setVisible(True)
		# chart.legend().setAlignment(Qt.AlignTop)

		categories = ["Jan", "Feb", "Mar"]
		axis = QBarCategoryAxis()
		axis.append(categories)
		chart.createDefaultAxes()
		chart.setAxisX(axis, series)

		chart_view = QChartView(chart)
		chart_view.setRenderHint(QPainter.HighQualityAntialiasing)
		self.setCentralWidget(chart_view)


app = QApplication(sys.argv)
form = Form()
sys.exit(app.exec_())
