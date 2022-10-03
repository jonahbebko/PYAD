from pytube import YouTube as yt
import os

def download(id, path="."):
    os.rename(yt("https://youtu.be/" + id).streams.filter(only_audio=True).first().download(output_path=path), "output.mp3")
    # one-line expressions are funny