from datetime import datetime as dt
from datetime import timedelta
import xml.etree.ElementTree as ElementTree
import json
from dicttoxml import dicttoxml


class PlayItem(object):
    """
    Object containing relevant song data.

    """

    def __init__(self):
        """
        Initialize an empty PlayItem with no elements loaded.

        """
        pass

    @classmethod
    def fromxmlelement(cls, xmlitem):
        """
        Create a PlayItem from a xml.etree.ElementTree element containing PlayItem data.

        """

        self = cls()
        self.ID = int(xmlitem[0].text)
        self.Naziv = xmlitem[1].text
        self.Autor = xmlitem[2].text
        self.Album = xmlitem[3].text
        self.Info = xmlitem[4].text
        self.Tip = int(xmlitem[5].text)
        self.Color = xmlitem[6].text
        self.NaKanalu = int(xmlitem[7].text)
        self.PathName = xmlitem[8].text
        self.ItemType = int(xmlitem[9].text)
        self.StartCue = float(xmlitem[10].text)
        self.EndCue = float(xmlitem[11].text)
        self.Pocetak = float(xmlitem[12].text)
        self.Trajanje = float(xmlitem[13].text)
        self.Vrijeme = Date.fromisoformat(xmlitem[14].text)
        self.StvarnoVrijemePocetka = Date.fromisoformat(xmlitem[15].text)
        self.VrijemeMinTermin = Date.fromisoformat(xmlitem[16].text)
        self.VrijemeMaxTermin = Date.fromisoformat(xmlitem[17].text)
        self.PrviU_Bloku = xmlitem[18].text
        self.ZadnjiU_Bloku = xmlitem[19].text
        self.JediniU_Bloku = xmlitem[20].text
        self.FiksniU_Terminu = xmlitem[21].text
        self.Reklama = xmlitem[22].text
        self.WaveIn = xmlitem[23].text
        self.SoftIn = int(xmlitem[24].text)
        self.SoftOut = int(xmlitem[25].text)
        self.Volume = int(xmlitem[26].text)
        self.OriginalStartCue = float(xmlitem[27].text)
        self.OriginalEndCue = float(xmlitem[28].text)
        self.OriginalPocetak = float(xmlitem[29].text)
        self.OriginalTrajanje = float(xmlitem[30].text)
        return self
    
    @classmethod
    def fromdict(cls, data):
        """
        Create a PlayItem from a dictionary object containing PlayItem data.

        """

        self = cls()
        self.ID = int(data['ID'])
        self.Naziv = data['Naziv']
        self.Autor = data['Autor']
        self.Album = data['Album']
        self.Info = data['Info']
        self.Tip = int(data['Tip'])
        self.Color = data['Color']
        self.NaKanalu = int(data['NaKanalu'])
        self.PathName = data['PathName']
        self.ItemType = int(data['ItemType'])
        self.StartCue = float(data['StartCue'])
        self.EndCue = float(data['EndCue'])
        self.Pocetak = float(data['Pocetak'])
        self.Trajanje = float(data['Trajanje'])
        self.Vrijeme = Date.fromisoformat(data['Vrijeme'])
        self.StvarnoVrijemePocetka = Date.fromisoformat(data['StvarnoVrijemePocetka'])
        self.VrijemeMinTermin = Date.fromisoformat(data['VrijemeMinTermin'])
        self.VrijemeMaxTermin = Date.fromisoformat(data['VrijemeMaxTermin'])
        self.PrviU_Bloku = data['PrviU_Bloku']
        self.ZadnjiU_Bloku = data['ZadnjiU_Bloku']
        self.JediniU_Bloku = data['JediniU_Bloku']
        self.FiksniU_Terminu = data['FiksniU_Terminu']
        self.Reklama = data['Reklama'].lower() == 'true'
        self.WaveIn = data['WaveIn'].lower() == 'true'
        self.SoftIn = int(data['SoftIn'])
        self.SoftOut = int(data['SoftOut'])
        self.Volume = int(data['Volume'])
        self.OriginalStartCue = float(data['OriginalStartCue'])
        self.OriginalEndCue = float(data['OriginalEndCue'])
        self.OriginalPocetak = float(data['OriginalPocetak'])
        self.OriginalTrajanje = float(data['OriginalTrajanje'])
        return self
        

    def as_json(self):
        """
        Returns a JSON string representation of the PlayItem.
        """
        return json.dumps({ str(key): str(val) for key, val in self.__dict__.items()})

    def __str__(self):
        """
        Returns a XML string representation of the PlayItem.
        """

        return f"<PlayItem>{dicttoxml({ str(key): str(val) for key, val in self.__dict__.items()}, custom_root='PlayItem', attr_type=False, root=False).decode('windows-1250')}</PlayItem>"

    def __repr__(self):
        """
        Returns a simplified string version of the object with the following structure:

        'Author Name - Song Title @ Time Of Start'
        """

        return f"{self.Naziv} by {self.Autor} @ {self.Vrijeme}"

    @property
    def Duration(self):
        """
        Returns a timedelta representation of the songs duration.
        It allows for simpler computing and calculating of song length with respect to datetime data.
        """
        return timedelta(seconds=self.Trajanje)
    @Duration.setter
    def Duration(self, value):
        self.Trajanje = value.total_seconds()
    
    @property
    def EndOfSong(self):
        """
        Returns the datetime data indicating when to pull the next item in the list.
        """
        return self.Vrijeme+self.Duration




class Date(dt):
    def __str__(self):
        return self.isoformat()

