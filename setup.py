
from distutils.core import setup
import py2exe

py2exe_options = {'py2exe': {"includes":["PyQt5.sip", "PyQt5.QtWebChannel", "PyQt5.QtNetwork", "PyQt5.QtWebEngineCore", "PyQt5.QtPrintSupport"]}}

setup(windows=['run.py'], options=py2exe_options)
