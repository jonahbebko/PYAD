# create a list of absent libraries, yell at the user to install them
# (this shouldn't be an issue since libraries are automatically added
# to the executable I made)
missingImports = []
try:
    from pytube import YouTube as yt
except:
    missingImports += "pytube"

try:
    from youtubesearchpython import VideosSearch as vs
except:
    missingImports += "youtubesearchpython"

import os

# max function but smaller
def m(l):
    return max([len(i) for i in l])

def search(title:str, num:int=5):

    # initialize lists (yes it hurts to look at, i know)
    durs, views, channels, titles, ids = [], [], [], [], []

    # search for video and add data to lists
    for video in vs(title, limit=num).result()['result']:

        durs.append(video['duration'])
        views.append(video['viewCount']['short'])

        # cut off channel/title if too long
        if len(video['channel']['name']) > 25:
            channels.append(video['channel']['name'][:22] + "...")
        else:
            channels.append(video['channel']['name'])

        if len(video['title']) > 40:
            titles.append(video['title'][:37] + '...')
        else:
            titles.append(video['title'])
        
        ids.append(video['id'])
    
    # return the id list since it's used for the downloader
    return ids

def download(id, path="."):
    vid = yt("https://youtu.be/" + id).streams.filter(only_audio=True).first()
    save = vid.download(output_path=path)

    # save memory by using a void variable
    # but this is python so who really cares about memory
    # it's about looking cool and smart
    base, _ = os.path.splitext(save)
    os.rename(save, base + ".mp3")