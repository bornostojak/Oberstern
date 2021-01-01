from fireplay import PlayItem, PlayList
from pydub import AudioSegment
import xml.etree.ElementTree as ElementTree
import codecs



def MixdownItems(items):
    product=None
    product_len = 0.0
    for item in items:
        try:
            if item.PathName.endswith(".mp3"):
                new = AudioSegment.from_mp3(item.PathName)
            elif item.PathName.endswith(".wav"):
                new = AudioSegment.from_wav(item.PathName)
            else:
                continue
        except:
            continue
        if product == None:
            product = new
        else:
            product.overlay(new, position=product_len)
        product_len += float(item.Trajanje)
    return product
            


encodings = ["utf-8", "windows-1250", "windows-1252"]
encoding = ""
for e in encodings:
    try:
        with codecs.open('smixana.xml', 'r', e) as file:
            tree = ElementTree.fromstring(file.read())
        encoding = e
    except:
        pass




#using fft to locate the good location in the start
#using markers to select the start and end of the news for 




playitems = [PlayItem(item) for item in list(tree) if item.tag=="PlayItem"]
output = MixdownItems(playlistitems)


