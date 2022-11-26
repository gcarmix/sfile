import ffmpeg

def analyze(filename):
    try:
        metadata = ffmpeg.probe(filename)["streams"]
    except:
        metadata = {}
    return metadata