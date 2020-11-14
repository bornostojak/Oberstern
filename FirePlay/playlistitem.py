from datetime import datetime as dt
from datetime import timedelta
import xml.etree.ElementTree as ElementTree

from datetime import datetime as dt
from datetime import timedelta


class PlaylistItem(object):
    def __init__(self, xmlitem):
        self.ID = list(xmlitem)[0].text
        self.Naziv = list(xmlitem)[1].text
        self.Autor = list(xmlitem)[2].text
        self.Album = list(xmlitem)[3].text
        self.Info = list(xmlitem)[4].text
        self.Tip = list(xmlitem)[5].text
        self.Color = list(xmlitem)[6].text
        self.NaKanalu = list(xmlitem)[7].text
        self.PathName = list(xmlitem)[8].text
        self.ItemType = list(xmlitem)[9].text
        self.StartCue = list(xmlitem)[10].text
        self.EndCue = list(xmlitem)[11].text
        self.Pocetak = list(xmlitem)[12].text
        self.Trajanje = list(xmlitem)[13].text
        self.Vrijeme = list(xmlitem)[14].text
        self.StvarnoVrijemePocetka = list(xmlitem)[15].text
        self.VrijemeMinTermin = list(xmlitem)[16].text
        self.VrijemeMaxTermin = list(xmlitem)[17].text
        self.PrviU_Bloku = list(xmlitem)[18].text
        self.ZadnjiU_Bloku = list(xmlitem)[19].text
        self.JediniU_Bloku = list(xmlitem)[20].text
        self.FiksniU_Terminu = list(xmlitem)[21].text
        self.Reklama = list(xmlitem)[22].text
        self.WaveIn = list(xmlitem)[23].text
        self.SoftIn = list(xmlitem)[24].text
        self.SoftOut = list(xmlitem)[25].text
        self.Volume = list(xmlitem)[26].text
        self.OriginalStartCue = list(xmlitem)[27].text
        self.OriginalEndCue = list(xmlitem)[28].text
        self.OriginalPocetak = list(xmlitem)[29].text
        self.OriginalTrajanje = list(xmlitem)[30].text
    
    def __str__(self):
        return f"""<PlayItem>
<ID>{self.ID}</ID>
<Naziv>{self.Naziv}</Naziv>
<Autor>{self.Autor}</Autor>
<Album>{self.Album}</Album>
<Info>{self.Info}</Info>
<Tip>{self.Tip}</Tip>
<Color>{self.Color}</Color>
<NaKanalu>{self.NaKanalu}</NaKanalu>
<PathName>{self.PathName}</PathName>
<ItemType>{self.ItemType}</ItemType>
<StartCue>{self.StartCue}</StartCue>
<EndCue>{self.EndCue}</EndCue>
<Pocetak>{self.Pocetak}</Pocetak>
<Trajanje>{self.Trajanje}</Trajanje>
<Vrijeme>{self.Vrijeme}</Vrijeme>
<StvarnoVrijemePocetka>{self.StvarnoVrijemePocetka}</StvarnoVrijemePocetka>
<VrijemeMinTermin>{self.VrijemeMinTermin}</VrijemeMinTermin>
<VrijemeMaxTermin>{self.VrijemeMaxTermin}</VrijemeMaxTermin>
<PrviU_Bloku>{self.PrviU_Bloku}</PrviU_Bloku>
<ZadnjiU_Bloku>{self.ZadnjiU_Bloku}</ZadnjiU_Bloku>
<JediniU_Bloku>{self.JediniU_Bloku}</JediniU_Bloku>
<FiksniU_Terminu>{self.FiksniU_Terminu}</FiksniU_Terminu>
<Reklama>{self.Reklama}</Reklama>
<WaveIn>{self.WaveIn}</WaveIn>
<SoftIn>{self.SoftIn}</SoftIn>
<SoftOut>{self.SoftOut}</SoftOut>
<Volume>{self.Volume}</Volume>
<OriginalStartCue>{self.OriginalStartCue}</OriginalStartCue>
<OriginalEndCue>{self.OriginalEndCue}</OriginalEndCue>
<OriginalPocetak>{self.OriginalPocetak}</OriginalPocetak>
<OriginalTrajanje>{self.OriginalTrajanje}</OriginalTrajanje>
</PlayItem>\n
"""

    def __repr__(self):
        return self.__str__()

    def to_xml_element(self):
        return ElementTree.fromstring(str(self))

    def get_time(self):
        return dt.fromisoformat(self.Vrijeme)

    def get_duration_as_timedelta(self):
        return timedelta(seconds=float(self.Trajanje))

    def get_time_of_next(self):
        return self.get_time()+self.get_duration_as_timedelta()
