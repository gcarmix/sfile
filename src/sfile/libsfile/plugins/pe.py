import pefile
import json

def analyze(filename):
    try:
        pe = pefile.PE(filename)
        pedump = pe.dump_dict()
        infos = pedump["Version Information"][0][2][5]
        return infos
    except:
        return {}

#"Version Information"
#"Imported Symbols"
#"Resource Directory"
