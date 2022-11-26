import magic
import os
import libsfile.hashes as hashes
from plugins import exif
from plugins import pdf
from plugins import pe
from plugins import docx
from plugins import xlsx
from plugins import media


def analyzeFile(filename):
    fileobj = {}
    if not os.path.isfile(filename):
        return fileobj

    fileobj['name'] = os.path.basename(filename)
    fileobj['mime'] = magic.from_file(filename,mime=True)
    fileobj['desc'] = magic.from_file(filename)
    fileobj['md5'] = hashes.md5(filename)
    fileobj['sha1'] = hashes.sha1(filename)
    stats = os.stat(filename)
    fileobj['size'] = int(stats.st_size)

    if('application/x-dosexec' in fileobj['mime']):
        fileobj['detailed'] = pe.analyze(filename)
    elif('image' in fileobj['mime']):
        fileobj['detailed'] = exif.analyze(filename)
    elif 'application/pdf' in fileobj['mime']:
        fileobj['detailed'] = pdf.analyze(filename)
    elif 'application/vnd.openxmlformats-officedocument.wordprocessingml.document' in fileobj['mime']:
        fileobj['detailed'] = docx.analyze(filename)
    elif 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' in fileobj['mime']:
        fileobj['detailed'] = xlsx.analyze(filename)   
    
    return fileobj
