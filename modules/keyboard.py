from pynput import keyboard
from pynput.keyboard import Key, Controller

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from .save import *
from .hotkeys import *
from .tabs import *

def cleanModifiers():
    global ctrl
    global alt
    ctrl = False
    alt = False

class Keyboard():
    def __init__(self):
        print('started keyboard')
    def on_press(key):
        global appClass

        if appClass.window.isActiveWindow() == False:
            return

        global ctrl
        global alt
        if(key == keyboard.Key.ctrl): 
            ctrl = True  
        elif(key == keyboard.Key.alt):
            alt = True
        try:
            name = getHotkey(ctrl, alt, key.char)
            if name == "save":
                cleanModifiers()
                if(appClass.tabNames[appClass.currentTab] == ''):
                    appClass.filenamePopup = True
                else:
                    save(appClass.tabNames[appClass.currentTab], appClass.textBox.toPlainText(), appClass)
            elif name == "save_as":
                cleanModifiers()
                appClass.hasShownFilenamePopup = False
                appClass.filenamePopup = True
            elif name == "tab_left":
                cleanModifiers()
                appClass.tabLeft = True
            elif name == "tab_right":
                cleanModifiers()
                appClass.tabRight = True

        except AttributeError:
            pass

    def on_release(key):
        if appClass.window.isActiveWindow() == False:
            return

        global ctrl
        global alt
        if(key == keyboard.Key.ctrl):
            ctrl = False
        elif(key == keyboard.Key.alt):
            alt = False

    def initKeyboard(self,app):
        global window
        global appClass
        global alt
        global ctrl

        alt = False
        ctrl = False

        window = app.window
        appClass = app
    
        print(appClass.window.isActiveWindow())

        listener = keyboard.Listener(
            on_press=self.on_press,
            on_release=self.on_release)
        listener.start()
