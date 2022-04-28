from PyQt5.QtCore import QDirIterator

my_dir = QDirIterator("C:\\", QDirIterator.Subdirectories)
while my_dir.hasNext():
	print(my_dir.next())
