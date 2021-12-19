import sys
import json

from .highlighting import *

def initStyle(appClass):
    global font_size
    global keywords
    global braces
    global operators

    styleFile = open("./style/style.json")
    style = json.load(styleFile)
    
    #print(style["operators"])

    #appClass.font_size = 20
    appClass.font_size = style["font_size"]
    PythonHighlighter.keywords = style["keywords"]

    # Python operators
    PythonHighlighter.operators = style["ops"]

    # Python braces
    PythonHighlighter.braces = style["braces"]