import sys

from win32com.shell import shell
from PIL import Image, ImageQt
import win32api
import win32con
import win32ui
import win32gui
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QApplication, QMainWindow, QTreeWidget, QTreeWidgetItem
from PyQt5.QtGui import QIcon


def get_icon(PATH, size):
	SHGFI_ICON = 0x000000100
	SHGFI_ICONLOCATION = 0x000001000
	if size == "small":
		SHIL_SIZE = 0x00001
	elif size == "large":
		SHIL_SIZE = 0x00002
	else:
		raise TypeError("Invalid argument for 'size'. Must be equal to 'small' or 'large'")

	ret, info = shell.SHGetFileInfo(PATH, 0, SHGFI_ICONLOCATION | SHGFI_ICON | SHIL_SIZE)
	hIcon, iIcon, dwAttr, name, typeName = info
	ico_x = win32api.GetSystemMetrics(win32con.SM_CXICON)
	hdc = win32ui.CreateDCFromHandle(win32gui.GetDC(0))
	hbmp = win32ui.CreateBitmap()
	hbmp.CreateCompatibleBitmap(hdc, ico_x, ico_x)
	hdc = hdc.CreateCompatibleDC()
	hdc.SelectObject(hbmp)
	hdc.DrawIcon((0, 0), hIcon)
	win32gui.DestroyIcon(hIcon)

	bmpinfo = hbmp.GetInfo()
	bmpstr = hbmp.GetBitmapBits(True)
	img = Image.frombuffer(
		"RGBA",
		(bmpinfo["bmWidth"], bmpinfo["bmHeight"]),
		bmpstr, "raw", "BGRA", 0, 1
	)

	if size == "small":
		img = img.resize((16, 16), Image.ANTIALIAS)
	return img


class Form(QMainWindow):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.setGeometry(450, 250, 300, 300)
		tw = QTreeWidget(self)
		tw.setIconSize(QSize(32, 32))
		item0 = QTreeWidgetItem(tw, ["Item 1"])
		icon = QIcon()
		# QIMG = ImageQt.ImageQt(get_icon("Read_file_icons_and_use_as_QIcon.py", "large"))
		# icon.addPixmap(QPixmap.fromImage(QIMG))
		icon.addPixmap(ImageQt.toqpixmap(get_icon("Read_file_icons_and_use_as_QIcon.py", "large")))
		item0.setIcon(0, icon)
		self.setCentralWidget(tw)
		self.show()


app = QApplication(sys.argv)
form = Form()
sys.exit(app.exec_())
