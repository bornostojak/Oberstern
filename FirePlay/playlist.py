import xml.etree.ElementTree as ElementTree
import datetime
from datetime import datetime as dt
from datetime import timedelta
from .playitem import PlayItem

class PlayList(object):
    def __init__(self, xmltree):
        self.Items = [PlayItem(item) for item in list(xmltree)]

    def __str__(self):
        tmp = ""
        for i in self.Items:
            tmp+=str(i)+"\n"
        return f"<PlayList>\n{tmp}</PlayList>"
    
    def __repr__(self):
        return str(self.__str__().encode('utf-8').decode('utf-8'))
    
    def __list__(self):
        return self.Items
    
    def get_xml_element(self):
        return ElementTree.fromstring(self.__str__().encode(encoding))
    

