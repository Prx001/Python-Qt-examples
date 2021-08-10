from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
class PyToggle(QCheckBox):
    def __init__(self,
        width = 60,
        bg_color = "#777",
        circle_color = "#DDD",
        active_color = "#00BCff"
    ):
        QCheckBox.__init__(self)
        self.setFixedSize(width, 28)
        self.setCursor(Qt.PointingHandCursor)
        self._bg_color = bg_color
        self._circle_color = circle_color
        self._active_color = active_color
        self.stateChanged.connect(self.debug)
    def debug(self):
        print("Status:", self.isChecked())
    def hitButton(self, pos):
        return self.contentsRect().contains(pos)
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(Qt.NoPen)
        rect = QRect(0, 0, self.width(), self.height())
        if not self.isChecked():
            painter.setBrush(QColor(self._bg_color))
            painter.drawRoundedRect(0, 0, rect.width(), self.height(), self.height()/2, self.height()/2)
            painter.setBrush(QColor(self._circle_color))
            painter.drawEllipse(3, 3, 22, 22)
        elif self.isChecked():
            painter.setBrush(QColor(self._active_color))
            painter.drawRoundedRect(0, 0, rect.width(), self.height(), self.height()/2, self.height()/2)
            painter.setBrush(QColor(self._circle_color))
            painter.drawEllipse(self.width() - 26, 3, 22, 22)
        painter.end()