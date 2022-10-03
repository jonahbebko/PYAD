from pytube import YouTube as yt
import os

def download(id, path, *args, **kwargs):
    
    v = yt("https://youtu.be/" + id).streams.filter(only_audio=True).first()
    
    try:
        v.download(filename="output.mp3", output_path=path)
    except:
        pass