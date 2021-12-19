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

from modules.filenamePopup import *
from modules.ui import *

class App():
    
    def __init__(self):
        self.title = "app"
        self.localeFile = open('./locale/english.json')
        self.locale = json.load(self.localeFile)
        self.filename = ''
        self.filenamePopup = False
        self.hasShownFilenamePopup = False

        initUI(self)

    def filenamePopupCheck(self):
        if self.filenamePopup == True:

            popup = filenamePopup()
            popup.checkFilenameBox(self)

if __name__ == '__main__':
    app = App()
