import fireplay
from xml.etree import ElementTree

def load(filename=None):
    if filename == None: return None

    tree=None
    with open(filename, 'br') as file:
        for enc in ['utf-8', 'windows-1250', 'windows-1252']:
            try:
                tree = ElementTree.fromstring(file.read().decode(enc))
                tree.encoding = enc
                break
            except:
                file.seek(0)
                pass
    return tree
