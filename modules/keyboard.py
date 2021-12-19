from pynput import keyboard
from pynput.keyboard import Key, Controller

class Keyboard():
    def __init__(self):
        print('started keyboard')
    def on_press(key):
        if appClass.window.isActiveWindow() == False:
            return

        global ctrl
        global alt
        if(key == keyboard.Key.ctrl): 
            ctrl = True  
        elif(key == keyboard.Key.alt):
            alt = True
        try:
            if ctrl == True and key.char == 's':
                #save(appClass.filename, appClass.textBox.toPlainText())
                #def save(appClass.filename, appClass.textBox.toPlainText()):
                file = open(appClass.filename, 'w')
                file.write(appClass.textBox.toPlainText())
                file.close()

        except AttributeError:
            pass
        try:
            print('Alphanumeric key pressed: {0} '.format(
                key.char))
        except AttributeError:
            print('special key pressed: {0}'.format(
                key))


    def on_release(key):
        if appClass.window.isActiveWindow() == False:
            return

        global ctrl
        global alt
        if(key == keyboard.Key.ctrl):
            ctrl = False
        elif(key == keyboard.Key.alt):
            alt = False

        print('Key released: {0}'.format(
            key))

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
