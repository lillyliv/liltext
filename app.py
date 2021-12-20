'''

Text editor and development tools by Lilly (lillyliv#5756)

Version δ (delta)

'''

import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import json

import threading

from modules.filenamePopup import *
from modules.ui import *
from modules.hotkeys import initHotkeys
from modules.style import initStyle

class App():
    
    def __init__(self):
        self.title = "app"
        self.localeFile = open('./locale/english.json')
        self.locale = json.load(self.localeFile)
        self.filename = ''
        self.filenamePopup = False
        self.hasShownFilenamePopup = False
        self.tabLeft = False
        self.tabRight = False
        self.currentTab = 0
        self.tabs = ['']
        self.tabNames = ['']

        initStyle(self)
        initHotkeys()

        initUI(self)
    def frame(self):
        self.filenamePopupCheck()
        if(self.tabLeft):
            tabLeft(self)
        elif(self.tabRight):
            tabRight(self)
        
        self.window.setWindowTitle(self.tabNames[self.currentTab] + " : " + self.locale["title_suffix"])

    def filenamePopupCheck(self):
        if self.filenamePopup == True:

            popup = filenamePopup()
            popup.checkFilenameBox(self)

if __name__ == '__main__':
    app = App()
