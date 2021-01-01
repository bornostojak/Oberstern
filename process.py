# TODO: Take care of mixing and other things

import codecs
from loadlist import load
from xml.etree import ElementTree

filename = "testing/data.xml"


tree=load('testing/data.xml')
print(tree.tag)
