from pytube import YouTube as yt
import os, sys

def resource_path(relative_path):

    try:
        base_path = sys._MEIPASS
    except Exception as e:
        print(f"Exception in resource_path\n{e}")
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def download(id, title="output.mp3", path=resource_path("temp/"), *args, **kwargs):
    
    v = yt("https://youtu.be/" + id).streams.filter(only_audio=True).first()
    
    try:
        v.download(filename=title, output_path=path)
    except:
        pass