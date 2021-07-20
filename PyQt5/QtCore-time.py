from PyQt5.QtCore import QDate, QTime, QDateTime, Qt
raw_date = QDate.currentDate()
print("This is raw date", raw_date)
print("This is ISO date", raw_date.toString(Qt.ISODate))
print("This is locale date", raw_date.toString(Qt.DefaultLocaleLongDate))
raw_time = QTime.currentTime()
print("This is raw time", raw_time)
print("This is ISO time", raw_time.toString(Qt.ISODate)) # 24-hour format
print("This is locale time", raw_time.toString(Qt.DefaultLocaleLongDate)) # AM PM 12-hour format
raw_datetime = QDateTime.currentDateTime()
print("This is raw date time", raw_datetime)
print("This is ISO date time", raw_datetime.toString(Qt.ISODate))
print("This is locale date time", raw_datetime.toString(Qt.DefaultLocaleLongDate))