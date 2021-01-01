import xml.etree.ElementTree as ElementTree
import datetime
from datetime import datetime as dt
from datetime import timedelta
from .playitem import PlayItem

class PlayList(object):
    def __init__(self):
        pass

    @classmethod
    def fromxmltree(cls, xmltree):
        if xmltree.__class__ is not ElementTree.Element:
            raise TypeError('The object is not a valid xml.etree.ElementTree.Element object!')

        self = cls()
        self.Items = [PlayItem.fromxmlelement(item) for item in list(xmltree)]
        return self

    @classmethod
    def fromdict(cls, data):
        self = cls()
        self.Items = [PlayItem.fromdict(item) for item in data['PlayList']['PlayItem']]
        return self
    
    def __str__(self):
        tmp = ""
        for i in self.Items:
            tmp+=str(i)+"\n"
        return f"<PlayList>\n{tmp}</PlayList>"
     
    def __repr__(self):
        return f"Playlist from {self.Items[0].Vrijeme} to {self.Items[len(self.Items)-1].EndOfSong}"
     
    def __list__(self):
        return self.Items
    
    def get_xml_element(self):
        return ElementTree.fromstring(self.__str__().encode('windows-1250'))
    
