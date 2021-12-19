from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from modules.editor import *
from modules.keyboard import *

import sys

def initUI(appClass):
    app = QApplication(sys.argv)  # make window and set title
    appClass.window = QWidget()
    appClass.window.setGeometry(100,100,300,300)
    appClass.window.setWindowTitle(appClass.filename + " : " + appClass.locale["title_suffix"])
    appClass.window.setFocus()

    print(appClass.window.isActiveWindow())

    initEditor(appClass)   # init editor and keyboard should probabally move this elsewhere
    keyboard = Keyboard        
    keyboard.initKeyboard(keyboard, appClass)

    appClass.layout = QVBoxLayout()  # add text box to window layout
    appClass.layout.addWidget(appClass.textBox)
    appClass.window.setLayout(appClass.layout)
    
    appClass.timer = QTimer()  # init filename popup box checks should also move this
    appClass.timer.timeout.connect(appClass.filenamePopupCheck)
    appClass.timer.start(100)

    appClass.window.show()
    sys.exit(app.exec_())