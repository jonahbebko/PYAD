from youtubesearchpython import VideosSearch as vs

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