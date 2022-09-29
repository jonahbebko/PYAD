from pytube import YouTube as yt
import os

def download(id, path="."):
    vid = yt("https://youtu.be/" + id).streams.filter(only_audio=True).first()
    save = vid.download(output_path=path)

    # save memory by using a void variable
    # but this is python so who really cares about memory
    # it's about looking cool and smart
    base, _ = os.path.splitext(save)
    os.rename(save, base + ".mp3")