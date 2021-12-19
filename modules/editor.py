from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
 
from modules.highlighting import *

import re

def initEditor(app):
    app.textBox = QTextEdit()

    app.editFont = QFontDatabase.systemFont(QFontDatabase.FixedFont)
    app.editFont.setPointSize(app.font_size)

    app.textBox.setFont(app.editFont)

    app.textBox.setStyleSheet("""QPlainTextEdit{
	font-family:'Consolas';
	color: #ccc; 
	background-color: #2b2b2b;}""")
    app.textBox.show()