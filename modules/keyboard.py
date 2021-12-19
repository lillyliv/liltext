from pynput import keyboard
from pynput.keyboard import Key, Controller

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from .save import *
from .hotkeys import *
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
                ctrl = False
                if(appClass.filename == ''):
                    appClass.filenamePopup = True
                else:
                    save(appClass.filename, appClass.textBox.toPlainText())
            elif name == "save_as":
                appClass.hasShownFilenamePopup = False
                appClass.filenamePopup = True
                alt = False

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
