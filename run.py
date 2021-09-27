from flask import Flask, request
from PyQt5 import QtGui
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import QApplication
import sys
from threading import Timer
import urllib.request

app = Flask(__name__)

@app.route("/")
def hello():
    return "<a href='/shutdown'>dasd</a>"

@app.route("/shutdown")
def shutdown():
    shutdown_server()
    return "Server shut down..."

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

class MyWebEngineView(QWebEngineView):

    #Overriding the close event so the server stops when the window is closed
    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        urllib.request.urlopen("http://127.0.0.1:5000/shutdown")
        return super().closeEvent(a0)

def ui(location):
    qt_app = QApplication(sys.argv)
    web = MyWebEngineView()
    web.setWindowTitle("Hello World")
    web.resize(500,500)
    web.setZoomFactor(1)
    web.load(QUrl(location))
    web.show()
    sys.exit(qt_app.exec_())

if __name__ == "__main__":

    if sys.frozen == "windows_exe":
        sys.stderr._error = "inhibit log creation"
    
    Timer(1, lambda: ui("http://127.0.0.1:5000")).start()
    app.run(debug=False)
