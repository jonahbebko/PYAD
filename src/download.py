from pytube import YouTube as yt

def download(id, title="output.mp3", path="temp/", *args, **kwargs):
    
    v = yt("https://youtu.be/" + id).streams.filter(only_audio=True).first()
    
    try:
        v.download(filename=title, output_path=path)
    except:
        pass