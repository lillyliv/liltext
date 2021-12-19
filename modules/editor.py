from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
 
def initEditor(app):
    app.textBox = QTextEdit()
    app.textBox.setText("")

    app.editFont = QFontDatabase.systemFont(QFontDatabase.FixedFont)
    app.editFont.setPointSize(18)

    app.textBox.setFont(app.editFont)
