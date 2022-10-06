from pytube import YouTube as yt
from .resourcepath import resource_path

def download(id, *args, **kwargs):
    
    v = yt("https://youtu.be/" + id).streams.filter(only_audio=True).first()
    
    try:
        v.download(filename="output.mp3", output_path=resource_path("temp"))
    except:
        pass