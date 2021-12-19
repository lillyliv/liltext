'''

Text editor and development tools by Lilly (lillyliv#5756)

Version α (alpha)

'''

import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import json

import threading

from modules.editor import *

def set_interval(func, arg, sec):
    def func_wrapper():
        set_interval(func, arg, sec)
        func(arg)
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t

class App():
    
    def __init__(self):
        self.title = "app"
        self.localeFile = open('./locale/english.json')
        self.locale = json.load(self.localeFile)

        self.initUI()

    def initUI(self):
        app = QApplication(sys.argv)  # make window and set title
        self.window = QWidget()
        self.window.setGeometry(100,100,300,300)
        self.window.setWindowTitle(self.locale["titleSuffix"])

        '''
        self.textBox = QTextEdit()
        self.textBox.setText("")  # make text box

        self.editFont = QFontDatabase.systemFont(QFontDatabase.FixedFont) # make font for text box
        self.editFont.setPointSize(16)
        self.textBox.setFont(self.editFont)
        '''
        initEditor(self)

        self.layout = QVBoxLayout()  # add text box to window layout
        self.layout.addWidget(self.textBox)
        self.window.setLayout(self.layout)

        self.window.show()
    
        sys.exit(app.exec_())

if __name__ == '__main__':
    app = App()
