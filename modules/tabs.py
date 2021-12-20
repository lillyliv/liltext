def initTabs():
    global currentTab
    global tabs

    currentTab = 0
    tabs = ['']

def tabLeft(appClass):
    global currentTab
    global tabs

    appClass.tabLeft = False

    tabs[currentTab] = appClass.textBox.toPlainText()

    if currentTab == 0:
        return
    else:
        currentTab = currentTab - 1
        appClass.textBox.setText(tabs[currentTab])

def tabRight(appClass):
    global currentTab
    global tabs

    appClass.tabRight = False

    if(len(tabs) <= currentTab + 1):
        tabs.append('')

    tabs[currentTab] = appClass.textBox.toPlainText()

    currentTab = currentTab + 1
    appClass.textBox.setText(tabs[currentTab])