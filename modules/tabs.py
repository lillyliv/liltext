def initTabs(appClass):
    appClass.currentTab = 0
    appClass.tabs = ['']
    appClass.tabNames = ['']

def tabLeft(appClass):
    appClass.tabLeft = False

    appClass.tabs[appClass.currentTab] = appClass.textBox.toPlainText()

    if appClass.currentTab == 0:
        return
    else:
        appClass.currentTab = appClass.currentTab - 1
        appClass.textBox.setText(appClass.tabs[appClass.currentTab])

def tabRight(appClass):
    appClass.tabRight = False

    if(len(appClass.tabs) <= appClass.currentTab + 1):
        appClass.tabs.append('')
        appClass.tabNames.append('')

    appClass.tabs[appClass.currentTab] = appClass.textBox.toPlainText()

    appClass.currentTab = appClass.currentTab + 1
    appClass.textBox.setText(appClass.tabs[appClass.currentTab])