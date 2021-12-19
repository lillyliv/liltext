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

class App():
    
    def __init__(self):
        self.title = "app"
        self.localeFile = open('./locale/english.json')
        self.locale = json.load(self.localeFile)
        self.filename = ''
        self.filenamePopup = False
        self.hasShownFilenamePopup = False
        #initKeyboard()
        self.initUI()
    
    def checkFilenameBox(self):
        if self.filenamePopup and not self.hasShownFilenamePopup:
            self.hasShownFilenamePopup = True
            self.filenameBox()
    def setFilename(self):
        self.filename = self.filenameTextBox.toPlainText()
        self.filenameWindow.close()
    def filenameBox(self):
        self.filenameWindow = QWidget()
        self.filenameWindow.setGeometry(100,100,200,200)
        self.filenameWindow.setWindowTitle('set a filename')
        self.filenameWindow.setFocus()

        self.filenameTextBox = QTextEdit()
        self.filenameTextBox.setText('file.txt')

        self.filenameTextBox.setFont(self.editFont)

        pybutton = QPushButton('Click me', self.filenameWindow)
        pybutton.resize(100,32)
        pybutton.move(50, 50)        
        pybutton.clicked.connect(self.setFilename)
    
        self.filenameLayout = QHBoxLayout()
        self.filenameLayout.addWidget(self.filenameTextBox)
        self.filenameLayout.addWidget(pybutton)
        self.filenameWindow.setLayout(self.filenameLayout)
        self.filenameWindow.show()

    def initUI(self):
        app = QApplication(sys.argv)  # make window and set title
        self.window = QWidget()
        self.window.setGeometry(100,100,300,300)
        self.window.setWindowTitle(self.filename + " : " +self.locale["titleSuffix"])
        self.window.setFocus()
        print(self.window.isActiveWindow())

        initEditor(self)

        self.layout = QVBoxLayout()  # add text box to window layout
        self.layout.addWidget(self.textBox)
        self.window.setLayout(self.layout)
        
        keyboard = Keyboard        
        keyboard.initKeyboard(keyboard, self)

        self.timer = QTimer()
        self.timer.timeout.connect(self.checkFilenameBox)
        self.timer.start(100)

        self.window.show()

        sys.exit(app.exec_())

if __name__ == '__main__':
    app = App()
