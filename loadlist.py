import fireplay
from xml.etree import ElementTree

def load(filename=None):
    if filename == None: return None

    tree=None
    with open(filename, 'br') as file:
        tree = fireplay.PlayList.fromxml(file.read().decode('windows-1250'))
#        for enc in ['utf-8', 'windows-1250', 'windows-1252']:
#            try:
#                #tree = ElementTree.fromstring(file.read().decode(enc))
#                tree=fireplay.PlayList.fromxml(file.read().decode(enc))
#                tree.encoding = enc
#                break
#            except:
#                file.seek(0)
#                pass


    return tree

def loadtest():
    return load(filename='testing/mixed.xml')
