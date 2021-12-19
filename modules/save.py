import sys
def save(name, data):
    file = open(name, 'w')
    file.write(data)
    file.close()