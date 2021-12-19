import sys
import json

from .highlighting import *

def initStyle(appClass):
    # global font_size
    # global keywords
    # global braces
    # global operators

    # styleFile = open("./style/style.json")
    # style = json.load(styleFile)
    
    # print(style["operators"])

    appClass.font_size = 20

    PythonHighlighter.keywords = [
        'and', 'assert', 'break', 'class', 'continue', 'def',
        'del', 'elif', 'else', 'except', 'exec', 'finally',
        'for', 'from', 'global', 'if', 'import', 'in',
        'is', 'lambda', 'not', 'or', 'pass', 'print',
        'raise', 'return', 'try', 'while', 'yield',
        'None', 'True', 'False',
    ]

    # Python operators
    PythonHighlighter.operators = [
        '=',
        # Comparison
        '==', '!=', '<', '<=', '>', '>=',
        # Arithmetic
        '\+', '-', '\*', '/', '//', '\%', '\*\*',
        # In-place
        '\+=', '-=', '\*=', '/=', '\%=',
        # Bitwise
        '\^', '\|', '\&', '\~', '>>', '<<',
    ]

    # Python braces
    PythonHighlighter.braces = [
        '\{', '\}', '\(', '\)', '\[', '\]',
    ]