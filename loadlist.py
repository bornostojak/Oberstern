import fireplay
from xml.etree import ElementTree

def load(filename=None):
    if filename == None: return None

    tree=None
    with open(filename, 'br') as file:
        data = file.read()
        for enc in ['utf-8', 'windows-1250', 'windows-1252']:
            try:
                tree = ElementTree.fromstring(file.read().decode(enc))
                tree.encoding = enc
                break
            except:
                pass
    return tree
