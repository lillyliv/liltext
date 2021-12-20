from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from .save import *

def setFilename():
    global appClass
    print('setting filename')
    appClass.tabNames[appClass.currentTab] = appClass.filenameTextBox.toPlainText()
    appClass.filenameWindow.close()
    save(appClass.tabNames[appClass.currentTab], appClass.textBox.toPlainText(), appClass)
def cancel():
    global appClass
    appClass.hasShownFilenamePopup = False
    appClass.filenamePopup = False
    appClass.filenameWindow.close()

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
        appClass.filenameWindow.setWindowFlag(Qt.WindowCloseButtonHint, False)

        appClass.filenameTextBox = QTextEdit()
        appClass.filenameTextBox.setText('file.txt')

        appClass.filenameTextBox.setFont(appClass.editFont)

        appClass.setButton = QPushButton(appClass.locale["set"], appClass.filenameWindow)
        appClass.setButton.resize(100,32)
        appClass.setButton.move(50, 50)        
        appClass.setButton.clicked.connect(setFilename)

        appClass.cancelButton = QPushButton(appClass.locale["cancel"], appClass.filenameWindow)
        appClass.cancelButton.resize(100,32)
        appClass.cancelButton.move(50, 50)        
        appClass.cancelButton.clicked.connect(cancel)
    
        appClass.filenameLayout = QVBoxLayout()
        appClass.filenameLayout.addWidget(appClass.filenameTextBox)
        appClass.filenameLayout.addWidget(appClass.setButton)
        appClass.filenameLayout.addWidget(appClass.cancelButton)
        appClass.filenameWindow.setLayout(appClass.filenameLayout)
        appClass.filenameWindow.show()