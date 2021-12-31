# From Qt documentation
# https://doc.qt.io/qtforpython-5/PySide2/QtCore/QDataStream.html
from PyQt5.QtCore import QFile, QIODevice, QDataStream

file_ = QFile("file.dat")
file_.open(QIODevice.WriteOnly)
# we will serialize the data into the file
out = QDataStream(file_)
# serialize a string
out.writeQString("the answer is")
# serialize an integer
out.writeInt32(42)
