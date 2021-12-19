'''

Text editor and development tools by Lilly (lillyliv#5756)

Version β (beta)

'''

import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import json

import threading

from modules.editor import *
from modules.keyboard import *
from modules.filenamePopup import *

class App():
    
    def __init__(self):
        self.title = "app"
        self.localeFile = open('./locale/english.json')
        self.locale = json.load(self.localeFile)
        self.filename = ''
        self.filenamePopup = False
        self.hasShownFilenamePopup = False


        self.initUI()

    def filenamePopupCheck(self):
        if self.filenamePopup == True:

            popup = filenamePopup()
            popup.checkFilenameBox(self)

    def initUI(self):
        app = QApplication(sys.argv)  # make window and set title
        self.window = QWidget()
        self.window.setGeometry(100,100,300,300)
        self.window.setWindowTitle(self.filename + " : " + self.locale["title_suffix"])
        self.window.setFocus()
        print(self.window.isActiveWindow())

        initEditor(self)

        self.layout = QVBoxLayout()  # add text box to window layout
        self.layout.addWidget(self.textBox)
        self.window.setLayout(self.layout)
        
        keyboard = Keyboard        
        keyboard.initKeyboard(keyboard, self)

        self.timer = QTimer()
        self.timer.timeout.connect(self.filenamePopupCheck)
        self.timer.start(100)

        self.window.show()

        sys.exit(app.exec_())

if __name__ == '__main__':
    app = App()
