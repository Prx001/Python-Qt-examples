# from PyQt5.QtCore import (QIODevice, QFile, Qt, QMarginsF, QRect)
# from PyQt5.QtGui import (QPagedPaintDevice, QPdfWriter, QPainter, QFont)
# from PyQt5.QtWidgets import QWidget, QApplication
#
#
# class PdfWrite(QWidget):
# 	"""docstring for PdfWrite"""
#
# 	def __init__(self, *arg):
# 		super(PdfWrite, self).__init__(*arg)
#
# 	def writePdf(self, name):
# 		pdfFile = QFile(name)
# 		# Open the pdf file to be written
# 		pdfFile.open(QIODevice.WriteOnly)
#
# 		# Create pdf writer
# 		pPdfWriter = QPdfWriter(pdfFile)
# 		# Set paper to A4
# 		pPdfWriter.setPageSize(QPagedPaintDevice.A4)
# 		# Set the resolution of the paper to 300, so its pixels are 3508X2479
# 		pPdfWriter.setResolution(300)
# 		pPdfWriter.setPageMargins(QMarginsF(60, 60, 60, 60))
#
# 		pPdfPainter = QPainter(pPdfWriter)
#
# 		# Leave blank above the title
# 		iTop = 100
#
# 		# TEXTWidth2100
# 		iContentWidth = 2100
#
# 		# Title, size 22
# 		font = QFont()
# 		font.setFamily("simhei.ttf")
# 		fontSize = 22
# 		font.setPointSize(fontSize)
#
# 		pPdfPainter.setFont(font)
# 		pPdfPainter.drawText(QRect(0, iTop, iContentWidth, 90), Qt.AlignHCenter, "I am the title and I am proud")
#
# 		# Content, font size 16, left-aligned
# 		fontSize = 16
# 		font.setPointSize(fontSize)
# 		pPdfPainter.setFont(font)
#
# 		iTop += 90
# 		pPdfPainter.drawText(QRect(0, iTop, iContentWidth, 60), Qt.AlignLeft, "1, directory one")
# 		iTop += 90
# 		# Indent 2 characters on the left
# 		iLeft = 120
# 		pPdfPainter.drawText(QRect(iLeft, iTop, iContentWidth - iLeft, 60), Qt.AlignLeft,
# 							 "The content of my directory one.")
# 		iTop += 90
# 		pPdfPainter.drawText(QRect(0, iTop, iContentWidth, 60), Qt.AlignLeft, "2, directory two")
# 		iTop += 90
# 		pPdfPainter.drawText(QRect(iLeft, iTop, iContentWidth - iLeft, 60), Qt.AlignLeft,
# 							 "Contents of My Directory One")
#
# 		pPdfPainter.end()
# 		pdfFile.close()
#
#
# if __name__ == '__main__':
#
# 	import sys
# 	from PyQt5.QtWidgets import QFileDialog
#
# 	app = QApplication(sys.argv)
# 	pWrite = PdfWrite()
# 	pWrite.show()
# 	name = QFileDialog.getSaveFileName(None, "Save File", "123.pdf", "* .pdf")
# 	if name[0]:
# 		print(name[0])
# 		pWrite.writePdf(name[0])
# 	else:
# 		pWrite.close()
# 	sys.exit(app.exec_())
import random

from PyQt5 import QtCore, QtGui, QtWidgets


class Gui(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Gui, self).__init__(parent)
        self.resize(1280, 720)
        self.scene = QtWidgets.QGraphicsScene(
            0, 0, self.width() - 50, self.height() - 70
        )
        self.scene.setBackgroundBrush(QtGui.QBrush(QtCore.Qt.white))
        self.canvas = QtWidgets.QGraphicsView(self.scene)
        mainLayout = QtWidgets.QGridLayout(self)
        mainLayout.addWidget(self.canvas)

    @property
    def circleList(self):
        return [
            item
            for item in self.scene.items()
            if isinstance(item, QtWidgets.QGraphicsEllipseItem)
        ]

    def newCircle(self):
        self.scene.addEllipse(
            random.randint(100, 400),
            random.randint(100, 400),
            50 + random.random() * 200,
            50 + random.random() * 200,
        )

    def generateReport(self):
        printer = QtGui.QPdfWriter("Output.pdf")
        printer.setPageSize(QtGui.QPagedPaintDevice.A4)
        printer.setResolution(100)
        painter = QtGui.QPainter(printer)
        delta = 20
        f = painter.font()
        f.setPixelSize(delta)
        painter.setFont(f)
        # hide all items
        last_states = []
        for item in self.scene.items():
            last_states.append(item.isVisible())
            item.setVisible(False)

        target = QtCore.QRectF(0, 0, printer.width(), 0)

        for i, item in enumerate(self.circleList):
            item.setVisible(True)
            source = item.mapToScene(item.boundingRect()).boundingRect()
            target.setHeight(source.height())
            if target.bottom() > printer.height():
                printer.newPage()
                target.moveTop(0)
            self.scene.render(painter, target, source)
            f = painter.font()
            f.setPixelSize(delta)
            painter.drawText(
                QtCore.QRectF(
                    target.bottomLeft(), QtCore.QSizeF(printer.width(), delta + 5)
                ),
                "test",
            )
            item.setVisible(False)
            target.setTop(target.bottom() + delta + 20)
        # restore visibility
        for item, state in zip(self.scene.items(), last_states):
            item.setVisible(state)
        painter.end()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    w = Gui()
    for _ in range(200):
        w.newCircle()
    w.generateReport()
    w.show()
    sys.exit(app.exec_())