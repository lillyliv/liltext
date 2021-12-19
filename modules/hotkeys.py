import sys
import json

def initHotkeys():
    global hotkeys
    hotkeyFile = open('./hotkeys/hotkeys.json')
    hotkeys = json.load(hotkeyFile)

def getHotkey(ctrl, alt, char):
    global hotkeys
    for i in hotkeys["hotkeys"]:
        if i["ctrl"] == ctrl and i["alt"] == alt and i["key"] == char:
            return i["name"]
    return ""