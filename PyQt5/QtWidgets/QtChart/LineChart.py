import sys

from PyQt5.QtCore import Qt, QPointF, QEasingCurve
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtChart import QChart, QChartView, QLineSeries
from PyQt5.QtGui import QPainter


class Form(QMainWindow):
	def __init__(self):
		super().__init__()
		self.init_ui()

	def init_ui(self):
		self.resize(800, 600)
		self.setWindowTitle("LineChart")
		self.initialize_chart()
		self.show()

	def initialize_chart(self):
		series = QLineSeries(self)
		series.append(0, 6)
		series.append(2, 4)
		series.append(3, 8)
		series.append(7, 4)
		series.append(10, 5)
		series << QPointF(11, 1) << QPointF(13, 3) << QPointF(17, 6) << QPointF(18, 3) << QPointF(20, 2)

		chart = QChart()
		chart.setTitle("LineChart example")
		chart.addSeries(series)
		chart.setAnimationOptions(QChart.AllAnimations)
		chart.setAnimationEasingCurve(QEasingCurve.InOutCubic)

		chart.legend().setVisible(True)
		chart.legend().setAlignment(Qt.AlignTop)

		chart_view = QChartView(chart)
		chart_view.setRenderHint(QPainter.HighQualityAntialiasing)
		self.setCentralWidget(chart_view)


app = QApplication(sys.argv)
form = Form()
sys.exit(app.exec_())
