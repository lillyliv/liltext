from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from .save import *

def setFilename():
    global appClass
    print('setting filename')
    appClass.filename = appClass.filenameTextBox.toPlainText()
    appClass.filenameWindow.close()
    save(appClass.filename, appClass.textBox.toPlainText(), appClass)

class filenamePopup():
    def __init__(self):
        return

    def checkFilenameBox(self, aC):
        global appClass
        appClass = aC
        if appClass.filenamePopup and not appClass.hasShownFilenamePopup:
            appClass.hasShownFilenamePopup = True
            self.filenameBox()
    def filenameBox(self):
        appClass.filenameWindow = QWidget()
        appClass.filenameWindow.setGeometry(100,100,200,100)
        appClass.filenameWindow.setWindowTitle(appClass.locale["set_a_filename"])
        appClass.filenameWindow.setFocus()

        appClass.filenameTextBox = QTextEdit()
        appClass.filenameTextBox.setText('file.txt')

        appClass.filenameTextBox.setFont(appClass.editFont)

        appClass.setButton = QPushButton(appClass.locale["set"], appClass.filenameWindow)
        appClass.setButton.resize(100,32)
        appClass.setButton.move(50, 50)        
        appClass.setButton.clicked.connect(setFilename)
    
        appClass.filenameLayout = QHBoxLayout()
        appClass.filenameLayout.addWidget(appClass.filenameTextBox)
        appClass.filenameLayout.addWidget(appClass.setButton)
        appClass.filenameWindow.setLayout(appClass.filenameLayout)
        appClass.filenameWindow.show()