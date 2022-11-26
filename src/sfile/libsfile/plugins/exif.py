import PIL.Image
import PIL.ExifTags
def analyze(filename):
    try:
        img = PIL.Image.open(filename)
        exif = {
        PIL.ExifTags.TAGS[k]: v
        for k, v in img._getexif().items()
        if k in PIL.ExifTags.TAGS
    }
    except:
        exif = {}
    return exif