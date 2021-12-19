import sys
def save(name, data, appClass):
    file = open(name, 'w')
    file.write(data)
    file.close()
    appClass.window.setWindowTitle(appClass.filename + " : " + appClass.locale["title_suffix"])