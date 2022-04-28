import ctypes
dwm = ctypes.windll.dwmapi
dwm.DwmSetIconicThumbnail()
dwm.DwmSetWindowAttribute()
dwm.DwmSetIconicLivePreviewBitmap()