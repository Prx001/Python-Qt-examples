# https://www.mfitzp.com/forum/t/pyqt5-qsettings-how-to-use-qsettings/509
from PyQt5.QtCore import QSettings
settings = QSettings('MyApplication', 'MyApplicationDesktop')
print(settings.fileName())
settings.setValue('customer_code', 8889)
settings.setValue('theme_selection', 'Dark')
settings.setValue('license', 'XXXXX-XXXX-XXXXX-XXXX')
# settings.remove('license')
keys = settings.allKeys()
print(keys)
if settings.contains("license"):
	print(settings.value("license"))
# settings.clear()

# https://www.riverbankcomputing.com/static/Docs/PyQt5/pyqt_qsettings.html